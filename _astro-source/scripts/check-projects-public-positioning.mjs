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
function readJson(file) {
  return JSON.parse(read(file));
}

const projectsSourcePath = path.join(sourceRoot, 'src/pages/projects.astro');
const builtProjectsPath = path.join(repoRoot, 'projects/index.html');
const sourceCatalogPath = path.join(sourceRoot, 'public/dashboard-data/public-proof-catalog.json');
const rootCatalogPath = path.join(repoRoot, 'dashboard-data/public-proof-catalog.json');

const source = read(projectsSourcePath);
const built = read(builtProjectsPath);
const sourceCatalogText = read(sourceCatalogPath);
const rootCatalogText = read(rootCatalogPath);
const sourceCatalog = JSON.parse(sourceCatalogText);

assert(sourceCatalogText === rootCatalogText, 'Root public-proof catalog must match Astro source catalog exactly.');

const requiredSourcePhrases = [
  'Hermes Kite',
  'Kite testnet and decentralized-infrastructure work',
  'paper-mode portfolio state',
  'No real-fund execution, no wallet power, no order power',
  'Hardware Compute Environment',
  'bounded local-compute and agent-infrastructure environment',
  'No private topology, addresses, credentials, wallet control, outside action control',
];

for (const phrase of requiredSourcePhrases) {
  assert(source.includes(phrase), `Projects source missing required public-positioning phrase: ${phrase}`);
}

const requiredBuiltPhrases = [
  'Hermes Kite',
  'Kite testnet and decentralized-infrastructure work',
  'paper-mode portfolio state',
  'No real-fund execution, no wallet power, no order power',
  'Hardware Compute Environment',
  'bounded local-compute and agent-infrastructure environment',
  'No private topology, addresses, credentials, wallet control, outside action control',
];

for (const phrase of requiredBuiltPhrases) {
  assert(built.includes(phrase), `Built projects page missing required public-positioning phrase: ${phrase}`);
}

const hermesKite = sourceCatalog.projects.find((project) => project.id === 'hermes-kite');
const hardware = sourceCatalog.projects.find((project) => project.id === 'hardware-compute-environment');
assert(hermesKite, 'Catalog missing hermes-kite entry.');
assert(hardware, 'Catalog missing hardware-compute-environment entry.');

assert(hermesKite.sources.some((source) => source.url === 'https://github.com/hash02/hermes-kite'), 'Hermes Kite catalog entry must cite the public GitHub repository.');
assert(hermesKite.limits.some((limit) => /No real-fund execution power/i.test(limit)), 'Hermes Kite catalog entry must state no real-fund authority.');
assert(hermesKite.limits.some((limit) => /No wallet power/i.test(limit)), 'Hermes Kite catalog entry must state no wallet authority.');
assert(hermesKite.limits.some((limit) => /No order power/i.test(limit)), 'Hermes Kite catalog entry must state no order authority.');

assert(hardware.sources.some((source) => source.url === 'https://bionicbanker.tech/blog/agent-graveyard/'), 'Hardware compute catalog entry must cite the public report.');
assert(hardware.limits.some((limit) => /No private topology or addresses/i.test(limit)), 'Hardware compute catalog entry must state topology/address boundary.');
assert(hardware.limits.some((limit) => /No credentials/i.test(limit)), 'Hardware compute catalog entry must state credential boundary.');
assert(hardware.limits.some((limit) => /No wallet control or outside-action power/i.test(limit)), 'Hardware compute catalog entry must state outside action limits.');

const publicSurface = [source, built, sourceCatalogText, rootCatalogText].join('\n').toLowerCase();
const banned = [
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
];

for (const phrase of banned) {
  assert(!publicSurface.includes(phrase), `Projects public-positioning surface contains banned phrase: ${phrase}`);
}

console.log('Projects public positioning checks passed.');
