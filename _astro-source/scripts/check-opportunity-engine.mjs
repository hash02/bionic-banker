import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const repoRoot = path.resolve(root, '..');

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

function read(file) {
  assert(fs.existsSync(file), `Missing required file: ${path.relative(repoRoot, file)}`);
  return fs.readFileSync(file, 'utf8');
}

const sourceFiles = {
  startHere: path.join(root, 'src/pages/start-here.astro'),
  fieldPack: path.join(root, 'src/pages/proof-pack.astro'),
  about: path.join(root, 'src/pages/about.astro'),
  home: path.join(root, 'src/pages/index.astro'),
  projects: path.join(root, 'src/pages/projects.astro'),
  apps: path.join(root, 'src/pages/apps.astro'),
  layout: path.join(root, 'src/layouts/BaseLayout.astro'),
};

const source = Object.fromEntries(Object.entries(sourceFiles).map(([key, file]) => [key, read(file)]));

const startHerePhrases = [
  'Start Quest',
  'Mission Map',
  '90-second quest',
  'Wallet Risk Assessment',
  'AML Status Evidence',
  'Fraud Alert Triage Workflow',
  'Agent Chess / Agent Workflow',
  'Health Board',
  'Recruiter',
  'Collaborator',
  'Executive / investor',
  'Technical explorer',
  'No live trading, wallet movement, or fund transfer authority',
];

const fieldPackPhrases = [
  'Bionic Banker Field Pack',
  'AI-assisted finance risk missions',
  'Five missions, one map',
  'Evidence map',
  'Technical stack',
  'Trust boundary',
  'Questions for Hash',
  'System cards',
  'Evidence map lanes',
  'No SAR filing, KYC approval, enforcement, or final compliance decision',
];

const aboutPhrases = [
  'About Hash',
  'I build maps for finance, AI agents, and risk work',
  'Serious work can still feel alive',
  'Core loop',
  'Good conversations start with a concrete mission',
];

for (const phrase of startHerePhrases) {
  assert(source.startHere.includes(phrase), `/start-here source is missing required phrase: ${phrase}`);
}

for (const phrase of fieldPackPhrases) {
  assert(source.fieldPack.includes(phrase), `/proof-pack source is missing required phrase: ${phrase}`);
}

for (const phrase of aboutPhrases) {
  assert(source.about.includes(phrase), `/about source is missing required phrase: ${phrase}`);
}

for (const phrase of ['/start-here', '/proof-pack', '/about']) {
  assert(source.home.includes(phrase) || source.layout.includes(phrase), `Site source must link to ${phrase}`);
}

for (const phrase of [
  'Can Hash reason about risk signals without turning a score into a verdict?',
  'Can Hash preserve auditability and authority boundaries?',
  'Can Hash turn messy fraud signals into a review-ready packet?',
  'Can Hash design AI-agent workflows where humans keep authority?',
]) {
  assert(source.projects.includes(phrase), `Projects source missing reviewer question: ${phrase}`);
}

const noLongDashSurface = [source.startHere, source.fieldPack, source.about, source.home].join('\n');
for (const glyph of ['—', '–']) {
  assert(!noLongDashSurface.includes(glyph), `Edited public conversion surface contains long dash glyph: ${glyph}`);
}

const cyanPattern = /#67e8f9|#a7f3d0|#6fe7ff|rgba\(103,\s*232,\s*249|rgba\(111,\s*231,\s*255/i;
for (const [name, text] of Object.entries({
  startHere: source.startHere,
  fieldPack: source.fieldPack,
  about: source.about,
  home: source.home,
  projects: source.projects,
  apps: source.apps,
})) {
  assert(!cyanPattern.test(text), `${name} still contains cyan/blue accent styling instead of green/black/white theme`);
}

const builtChecks = [
  [path.join(repoRoot, 'start-here/index.html'), ['Start Quest', '90-second quest', 'No live trading, wallet movement, or fund transfer authority']],
  [path.join(repoRoot, 'proof-pack/index.html'), ['Bionic Banker Field Pack', 'Evidence map', 'Questions for Hash']],
  [path.join(repoRoot, 'about/index.html'), ['About Hash', 'Serious work can still feel alive']],
  [path.join(repoRoot, 'index.html'), ['href="/start-here"', 'href="/proof-pack"']],
];

for (const [file, phrases] of builtChecks) {
  if (!fs.existsSync(file)) continue;
  const built = read(file);
  for (const phrase of phrases) {
    assert(built.includes(phrase), `${path.relative(repoRoot, file)} missing built phrase/link: ${phrase}`);
  }
}

const combined = Object.values(source).join('\n').toLowerCase();
const banned = [
  'seed phrase',
  'private key',
  'api key',
  'token=',
  'secret=',
  'wallet authority: true',
  'trade authority: true',
  'sar filing authority: true',
  'guaranteed return',
  'autonomous profit',
];
for (const phrase of banned) {
  assert(!combined.includes(phrase), `Opportunity engine source contains banned phrase: ${phrase}`);
}

console.log('OPPORTUNITY_ENGINE_CHECK PASS — mission map, field pack, about page, green theme guard, and no-long-dash guard are present.');
