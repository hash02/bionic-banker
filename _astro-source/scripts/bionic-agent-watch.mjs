import fs from 'node:fs';
import path from 'node:path';
import process from 'node:process';

const args = new Set(process.argv.slice(2));
const outputJson = args.has('--json');
const root = path.resolve(process.cwd(), '..');
const astroRoot = process.cwd();
const baseUrl = (process.env.BIONIC_BASE_URL || 'https://bionicbanker.tech').replace(/\/$/, '');

function exists(relFromRepo) {
  return fs.existsSync(path.join(root, relFromRepo));
}

function listMarkdownFiles(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs.readdirSync(dir).filter((name) => name.endsWith('.md')).sort();
}

function sanitizeEnvPresence(names) {
  const out = {};
  for (const name of names) out[name] = Boolean(process.env[name]);
  return out;
}

async function checkRoute(route) {
  const url = `${baseUrl}${route}`;
  const started = Date.now();
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 10000);
    const res = await fetch(url, { method: 'GET', signal: controller.signal });
    clearTimeout(timeout);
    const text = await res.text();
    return {
      route,
      url,
      status: res.status,
      ok: res.ok,
      ms: Date.now() - started,
      bytes: text.length,
      hasHtml: /<html/i.test(text),
    };
  } catch (error) {
    return {
      route,
      url,
      ok: false,
      error: error?.name === 'AbortError' ? 'timeout' : String(error?.message || error),
      ms: Date.now() - started,
    };
  }
}

const criticalRoutes = ['/', '/articles/', '/wallet-risk/', '/reports/', '/updates/'];
const blogDir = path.join(astroRoot, 'src', 'content', 'blog');
const articleFiles = listMarkdownFiles(blogDir);

const requiredRepoFiles = [
  'BIONIC_BANKER_AGENT.md',
  'agents/bionic_agent_contract.md',
  'agents/tasks/watch.md',
  'agents/tasks/draft.md',
  'agents/tasks/publish.md',
  '.github/workflows/bionic-watch.yml',
];

const connectorPresence = sanitizeEnvPresence([
  'PLAUSIBLE_API_KEY',
  'GA4_SERVICE_ACCOUNT_JSON',
  'X_API_KEY',
  'LINKEDIN_ACCESS_TOKEN',
  'TELEGRAM_BOT_TOKEN',
]);

const routeChecks = [];
for (const route of criticalRoutes) routeChecks.push(await checkRoute(route));

const localFacts = {
  repoRoot: path.basename(root),
  sourceArticleCount: articleFiles.length,
  contractFiles: Object.fromEntries(requiredRepoFiles.map((rel) => [rel, exists(rel)])),
  packageJsonExists: exists('_astro-source/package.json'),
  publicCopyStandardExists: exists('PUBLIC_COPY_STANDARD.md'),
};

const blockers = [];
for (const [rel, ok] of Object.entries(localFacts.contractFiles)) {
  if (!ok) blockers.push(`missing ${rel}`);
}
for (const check of routeChecks) {
  if (!check.ok) blockers.push(`route ${check.route} failed: ${check.status || check.error}`);
  if (check.ok && !check.hasHtml) blockers.push(`route ${check.route} did not return HTML-like content`);
}
if (articleFiles.length < 1) blockers.push('no source article markdown files found');

const report = {
  status: blockers.length ? 'amber' : 'green',
  generatedAt: new Date().toISOString(),
  lane: 'read_only_watcher',
  baseUrl,
  checkedFacts: {
    routes: routeChecks,
    local: localFacts,
    connectorsPresentByNameOnly: connectorPresence,
  },
  missingContext: Object.entries(connectorPresence)
    .filter(([, present]) => !present)
    .map(([name]) => `${name} not configured in this run; analytics/social actions remain queue-only.`),
  clearLimits: [
    'This watcher does not edit files.',
    'This watcher does not deploy.',
    'This watcher does not post to social platforms.',
    'This watcher does not read or print secret values.',
    'Route checks prove reachability only, not business impact.',
  ],
  blockers,
  nextHumanQuestion: blockers.length
    ? 'Which blocker should be resolved before enabling any draft or publisher lane?'
    : 'Should the next gated lane create a daily draft package, still without posting?',
};

if (outputJson) {
  console.log(JSON.stringify(report, null, 2));
} else {
  console.log(`# Bionic Banker Agent Watch\n`);
  console.log(`Status: ${report.status}`);
  console.log(`Generated: ${report.generatedAt}`);
  console.log(`Base URL: ${report.baseUrl}`);
  console.log(`Source article count: ${articleFiles.length}`);
  console.log('\n## Routes');
  for (const check of routeChecks) console.log(`- ${check.route}: ${check.ok ? 'ok' : 'fail'} ${check.status || check.error || ''} (${check.ms}ms)`);
  console.log('\n## Limits');
  for (const limit of report.clearLimits) console.log(`- ${limit}`);
  if (blockers.length) {
    console.log('\n## Blockers');
    for (const blocker of blockers) console.log(`- ${blocker}`);
  }
}

if (blockers.some((b) => b.includes('missing') || b.includes('failed'))) process.exit(1);
