import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const sourcePath = path.join(root, 'src/pages/index.astro');
const builtPath = path.join(root, '..', 'index.html');

function assert(condition, message) {
  if (!condition) throw new Error(message);
}
function read(file) {
  assert(fs.existsSync(file), `Missing required file: ${path.relative(root, file)}`);
  return fs.readFileSync(file, 'utf8');
}

const source = read(sourcePath);
const built = read(builtPath);

assert(!source.includes('<!-- HERO -\n'), 'Homepage source has a damaged HERO comment that can hide page content.');

const requiredSourcePhrases = [
  'AI, finance, and the world ahead.',
  'Auditable AI workflows for finance risk.',
  'Bionic Banker shows how wallet risk, AML status, and fraud-triage systems turn signals into source trails, rationale, limitations, and human review decisions.',
  'Example: wallet row, risk score, rationale, limitation, human decision.',
  'See a Wallet Risk Record',
  'Inspect the Source Map',
  'Read Source Notes',
  '/wallet-risk',
  '/system-map',
  '/articles',
  '/apps',
  '/signals',
  '/fraud-alert-triage',
  '/proof/site-health',
  'agent-chess-showcase',
  'hero-mobile-route-strip',
  'Source-first workflow',
  'No wallet or trade power',
  'Human review required',
  'No autonomous compliance decisions',
  'Market Positioning Intelligence',
  'hero-os-panel',
];

for (const phrase of requiredSourcePhrases) {
  assert(source.includes(phrase), `Homepage source is missing required phrase: ${phrase}`);
}

const requiredBuiltPhrases = [
  'AI, finance, and the world ahead.',
  'Auditable AI workflows for finance risk.',
  'Bionic Banker shows how wallet risk, AML status, and fraud-triage systems turn signals into source trails, rationale, limitations, and human review decisions.',
  'Example: wallet row, risk score, rationale, limitation, human decision.',
  'See a Wallet Risk Record',
  'Inspect the Source Map',
  'Read Source Notes',
  'Operating view',
  'Signal becomes a record. A record becomes a decision.',
  'Wallet Risk Assessment',
  'AML Status',
  'Fraud Alert Workflow',
  'Agent Chess board',
  'Market Positioning Intelligence',
  'No wallet or trade power',
  'Human review required',
];

for (const phrase of requiredBuiltPhrases) {
  assert(built.includes(phrase), `Built homepage is missing required phrase: ${phrase}`);
}

const requiredBuiltLinks = [
  'href="/apps"',
  'href="/signals"',
  'href="/wallet-risk"',
  'href="/fraud-alert-triage"',
  'href="/proof/site-health"',
  'href="/risk-evidence-overview"',
  'href="/apps"',
  'href="/risk-evidence-overview#agent-chess-showcase"',
];

for (const link of requiredBuiltLinks) {
  assert(built.includes(link), `Built homepage is missing route link: ${link}`);
}

assert(built.includes('class="hero-wrap"'), 'Built homepage is missing the hero body. The BaseLayout slot may be empty or commented out.');
assert(built.includes('Public reading room for a 90-second visit'), 'Built homepage is missing the disciplined Start Here section.');

const stylesheetRefs = Array.from(built.matchAll(/href="([^"]+\.css)"/g), (match) => match[1]);
assert(stylesheetRefs.length > 0, 'Built homepage must reference at least one stylesheet.');
for (const href of stylesheetRefs) {
  const cssPath = href.startsWith('/')
    ? path.join(root, '..', href.slice(1))
    : path.resolve(path.dirname(builtPath), href);
  assert(fs.existsSync(cssPath), `Built homepage references missing stylesheet: ${href}`);
}

const combined = [source, built].join('\n').toLowerCase();
const banned = [
  'c:/users/',
  'c:\\users\\',
  '/users/himan/',
  '100.86.',
  '100.124.',
  'private prompt',
  'system prompt',
  'seed phrase',
  'api key',
  'token=',
  'secret=',
  'may_execute: true',
  'autonomous profit',
  'guaranteed return',
  'live execution enabled',
  'wallet authority: true',
  'trade authority: true',
];

for (const phrase of banned) {
  assert(!combined.includes(phrase), `Homepage evidence surface contains banned phrase: ${phrase}`);
}

console.log('Homepage evidence surface checks passed.');
