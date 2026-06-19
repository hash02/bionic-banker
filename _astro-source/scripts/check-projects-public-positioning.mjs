import fs from 'node:fs';
import path from 'node:path';

const sourceRoot = process.cwd();
const repoRoot = path.join(sourceRoot, '..');

function assert(condition, message) {
  if (!condition) throw new Error(message);
}
function read(file) {
  assert(fs.existsSync(file), `Missing required file: ${path.relative(sourceRoot, file)}`);
  return fs.readFileSync(file, 'utf8');
}

const projectsSourcePath = path.join(sourceRoot, 'src/pages/projects.astro');
const builtProjectsPath = path.join(repoRoot, 'projects/index.html');
const appsSourcePath = path.join(sourceRoot, 'src/pages/apps.astro');
const builtAppsPath = path.join(repoRoot, 'apps/index.html');
const sourceCatalogPath = path.join(sourceRoot, 'public/dashboard-data/public-proof-catalog.json');
const rootCatalogPath = path.join(repoRoot, 'dashboard-data/public-proof-catalog.json');

const source = read(projectsSourcePath);
const built = read(builtProjectsPath);
const appsSource = read(appsSourcePath);
const builtApps = read(builtAppsPath);
const sourceCatalogText = read(sourceCatalogPath);
const rootCatalogText = read(rootCatalogPath);
const sourceCatalog = JSON.parse(sourceCatalogText);

assert(sourceCatalogText === rootCatalogText, 'Root public-proof catalog must match Astro source catalog exactly.');

const requiredSourcePhrases = [
  'Kite Testnet Proof',
  'Kite testnet and decentralized-infrastructure work',
  'paper-mode portfolio state',
  'No real-fund execution, no wallet power, no order power',
  'Agent Operations Lessons',
  'Shows lessons from small agent systems',
  'No production authority, live credentials, or autonomous outside action',
  'project → feature → output → evidence',
];
for (const phrase of requiredSourcePhrases) {
  assert(source.includes(phrase), `Projects source missing required public-positioning phrase: ${phrase}`);
}

const requiredBuiltPhrases = [
  'Kite Testnet Proof',
  'Agent Operations Lessons',
  'No production authority, live credentials, or autonomous outside action',
  'project → feature → output → evidence',
];
for (const phrase of requiredBuiltPhrases) {
  assert(built.includes(phrase), `Built projects page missing required public-positioning phrase: ${phrase}`);
}

const kite = sourceCatalog.projects.find((project) => project.id === 'hermes-kite');
const operations = sourceCatalog.projects.find((project) => project.id === 'hardware-compute-environment');
assert(kite, 'Catalog missing hermes-kite entry.');
assert(operations, 'Catalog missing hardware-compute-environment entry.');
assert(kite.name === 'Kite Testnet Proof', 'Catalog display name for hermes-kite must be Kite Testnet Proof.');
assert(operations.name === 'Agent Operations Lessons', 'Catalog display name for hardware-compute-environment must be Agent Operations Lessons.');
assert(kite.sources.some((source) => source.url === 'https://github.com/hash02/hermes-kite'), 'Kite catalog entry must cite the public GitHub repository.');
assert(kite.limits.some((limit) => /No real-fund execution power/i.test(limit)), 'Kite catalog entry must state no real-fund authority.');
assert(kite.limits.some((limit) => /No wallet power/i.test(limit)), 'Kite catalog entry must state no wallet authority.');
assert(kite.limits.some((limit) => /No order power/i.test(limit)), 'Kite catalog entry must state no order authority.');
assert(operations.sources.some((source) => source.url === 'https://bionicbanker.tech/blog/agent-graveyard/'), 'Agent operations catalog entry must cite the public report.');
assert(operations.limits.some((limit) => /No production authority/i.test(limit)), 'Agent operations entry must state production authority boundary.');
assert(operations.limits.some((limit) => /No live credentials/i.test(limit)), 'Agent operations entry must state live credential boundary.');
assert(operations.limits.some((limit) => /No autonomous outside action/i.test(limit)), 'Agent operations entry must state outside action boundary.');

const cardLanguageSurface = [source, built, appsSource, builtApps].join('\n');
const requiredCardLanguage = [
  'Record',
  'What it cannot do',
  'View source catalog',
  'Records wallet-screening judgment',
  'Records human-reviewed agent operations',
];
for (const phrase of requiredCardLanguage) {
  assert(cardLanguageSurface.includes(phrase), `Projects/Apps card surface missing record-language phrase: ${phrase}`);
}

const publicSurface = [source, built, appsSource, builtApps, sourceCatalogText, rootCatalogText].join('\n').toLowerCase();
const banned = [
  'revenue direction',
  'buyer edge',
  'buyer-readable',
  'potential client',
  'private machinery',
  'workshop behind it',
  'sell repeatable',
  'hardware compute environment',
  'hermes kite',
  '44 percent accuracy',
  '3,792 research rows',
  'btc direction checks',
  'c:/users/',
  'c:\\users\\',
  '/users/himan/',
  '100.86.',
  '100.124.',
  'seed phrase',
  'private key',
  'api key',
  'token=',
  'secret=',
  'may_execute: true',
  'wallet authority: true',
  'trade authority: true',
  'live execution enabled',
  'autonomous profit',
  'guaranteed return',
  'recruiter',
  'hiring manager',
  'technical reviewer',
  'packaging backlog',
  'packaged work',
  'work drafts',
  'draft package',
  'existing draft',
  'being surfaced',
  'surfaced as public proof',
  'found in the archive',
  'what the archive proves',
  'public-facing summary',
];
for (const phrase of banned) {
  assert(!publicSurface.includes(phrase), `Projects public-positioning surface contains banned phrase: ${phrase}`);
}

console.log('PROJECTS_PUBLIC_POSITIONING_PASS');
