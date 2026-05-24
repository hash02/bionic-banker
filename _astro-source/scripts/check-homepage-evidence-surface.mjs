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

const requiredSourcePhrases = [
  'Bionic Banker is the evidence surface for agentic finance systems.',
  'what authority is explicitly not granted',
  '/wallet-risk',
  '/risk-evidence-overview',
  '/projects',
  '/dashboard',
  'agent-chess-showcase',
  'hero-mobile-route-strip',
  'No wallet or trade authority',
  'Human review required',
  'Public-safe evidence only',
  'hero-os-panel',
];

for (const phrase of requiredSourcePhrases) {
  assert(source.includes(phrase), `Homepage source is missing required phrase: ${phrase}`);
}

const requiredBuiltPhrases = [
  'Bionic Banker is the evidence surface for agentic finance systems.',
  'Operating view',
  'Assess → explain → gate → publish',
  'Wallet Risk Assessment',
  'Risk &amp; Evidence Overview',
  'Agent Chess board',
  'No wallet or trade authority',
  'Human review required',
];

for (const phrase of requiredBuiltPhrases) {
  assert(built.includes(phrase), `Built homepage is missing required phrase: ${phrase}`);
}

const requiredBuiltLinks = [
  'href="/wallet-risk"',
  'href="/risk-evidence-overview"',
  'href="/projects"',
  'href="/dashboard"',
  'href="/risk-evidence-overview#agent-chess-showcase"',
];

for (const link of requiredBuiltLinks) {
  assert(built.includes(link), `Built homepage is missing route link: ${link}`);
}

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
