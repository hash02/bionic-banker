import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const sourceRoot = process.cwd();
const root = path.resolve('..');
const checks = [
  ['metric contract', 'node', ['scripts/check-proof-metric-contract.mjs']],
  ['json reader framing', 'node', ['scripts/check-json-reader-framing.mjs']],
  ['public links/assets', 'node', ['scripts/check-public-links-assets.mjs']],
];
const results = [];
for (const [label, command, args] of checks) {
  const run = spawnSync(command, args, { cwd: sourceRoot, encoding: 'utf8' });
  results.push({
    label,
    status: run.status === 0 ? 'pass' : 'fail',
    summary: (run.stdout || run.stderr || '').split('\n').filter(Boolean).slice(-3).join(' / '),
  });
}
const catalog = JSON.parse(fs.readFileSync(path.join(sourceRoot, 'public/dashboard-data/public-proof-catalog.json'), 'utf8'));
const articleCount = fs.readdirSync(path.join(sourceRoot, 'src/content/blog')).filter((name) => name.endsWith('.md')).length;
const projectsSource = fs.readFileSync(path.join(sourceRoot, 'src/pages/projects.astro'), 'utf8');
const publicCardCount = [...projectsSource.matchAll(/name:\s*'/g)].length;
const payload = {
  generated_at: new Date().toISOString(),
  status: results.every((r) => r.status === 'pass') ? 'pass' : 'fail',
  mission: 'Layer 3 public proof spine health',
  audience: 'AI-and-finance-literate readers, recruiters, collaborators, executives, investors, and serious learners.',
  style: 'AI-agent founder portfolio: sharp, product-forward, evidence-backed, and clear-limit aware.',
  flagship_order: ['Wallet Risk Assessment', 'AML Status Evidence', 'Fraud Alert Triage', 'Agent Chess / Agent Workflow', 'Site Health / Proof QA'],
  metrics: {
    public_system_cards: publicCardCount,
    evidence_catalog_lanes: catalog.projects.length,
    catalog_evidence_sources: catalog.projects.reduce((sum, project) => sum + (project.sources?.length || 0), 0),
    catalog_limits: catalog.projects.reduce((sum, project) => sum + (project.limits?.length || 0), 0),
    articles: articleCount,
  },
  checks: results,
  limit_note: 'Public-safe health summary only. No secrets, prompts, private paths, raw logs, wallet power, trading power, or compliance approval power.',
};
const out = path.join(sourceRoot, 'public/dashboard-data/site-health.json');
fs.writeFileSync(out, `${JSON.stringify(payload, null, 2)}\n`);
fs.mkdirSync(path.join(root, 'dashboard-data'), { recursive: true });
fs.copyFileSync(out, path.join(root, 'dashboard-data/site-health.json'));
console.log(`SITE_HEALTH ${payload.status.toUpperCase()} — wrote ${path.relative(sourceRoot, out)}`);
if (payload.status !== 'pass') process.exit(1);
