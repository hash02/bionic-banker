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
  systemMap: path.join(root, 'src/pages/system-map.astro'),
  worldMap: path.join(root, 'src/pages/world-map.astro'),
  about: path.join(root, 'src/pages/about.astro'),
  home: path.join(root, 'src/pages/index.astro'),
  projects: path.join(root, 'src/pages/projects.astro'),
  apps: path.join(root, 'src/pages/apps.astro'),
  layout: path.join(root, 'src/layouts/BaseLayout.astro'),
};

const source = Object.fromEntries(Object.entries(sourceFiles).map(([key, file]) => [key, read(file)]));

const startHerePhrases = [
  'Start Here',
  'Mission Map',
  '90-second quest',
  'Wallet Risk Assessment',
  'AML Status',
  'Fraud Alert Triage Workflow',
  'Agent Chess / Agent Workflow',
  'Health Board',
  'Reader',
  'Collaborator',
  'Strategic reader',
  'Technical explorer',
  'No live trading, wallet movement, or fund transfer authority',
];

const systemMapPhrases = [
  'Bionic Banker System Map',
  'simple map of AI-assisted finance risk work',
  '8 inspectable systems, one map',
  'Agent Workflow Case Review',
  'Record map',
  'Technical stack',
  'What it cannot do',
  'Questions for the reader',
  'System cards',
  'Catalog sections',
  'No SAR filing, KYC approval, enforcement, or final compliance decision',
];

const worldMapPhrases = [
  'AI + Finance World Map',
  'Regulated finance judgment, made visible through AI system records',
  'Five systems, one data story',
  'Reading paths',
  'The same records can be read from four angles',
  'No live trading, transfer, wallet-control, or fund-movement claim',
  'Public records only',
  'Representation standard',
  'Every useful page should answer six quiet questions',
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

for (const phrase of systemMapPhrases) {
  assert(source.systemMap.includes(phrase), `/system-map source is missing required phrase: ${phrase}`);
}

for (const phrase of worldMapPhrases) {
  assert(source.worldMap.includes(phrase), `/world-map source is missing required phrase: ${phrase}`);
}

for (const phrase of aboutPhrases) {
  assert(source.about.includes(phrase), `/about source is missing required phrase: ${phrase}`);
}

for (const phrase of ['/start-here', '/system-map', '/world-map', '/about']) {
  assert(source.home.includes(phrase) || source.layout.includes(phrase), `Site source must link to ${phrase}`);
}

for (const phrase of [
  'A wallet row can be scored and explained without pretending the score is a final verdict.',
  'An AML status can show what was checked while still refusing to approve, file, trade, deploy, or execute.',
  'Messy fraud signals can become a simple case note, source list, and human next step.',
  'Two AI workers can pass work back and forth while a person keeps final control.',
  'AI-assisted case work can leave a readable record without exposing private prompts or taking outside action.',
]) {
  assert(source.projects.includes(phrase), `Projects source missing plain-language proof line: ${phrase}`);
}

const noLongDashSurface = [source.startHere, source.systemMap, source.worldMap, source.about, source.home].join('\n');
for (const glyph of ['—', '–']) {
  assert(!noLongDashSurface.includes(glyph), `Edited public conversion surface contains long dash glyph: ${glyph}`);
}

const cyanPattern = /#67e8f9|#a7f3d0|#6fe7ff|rgba\(103,\s*232,\s*249|rgba\(111,\s*231,\s*255/i;
for (const [name, text] of Object.entries({
  startHere: source.startHere,
  fieldPack: source.systemMap,
  worldMap: source.worldMap,
  about: source.about,
  home: source.home,
  projects: source.projects,
  apps: source.apps,
})) {
  assert(!cyanPattern.test(text), `${name} still contains cyan/blue accent styling instead of green/black/white theme`);
}

const builtChecks = [
  [path.join(repoRoot, 'start-here/index.html'), ['Start Here', '90-second quest', 'No live trading, wallet movement, or fund transfer authority']],
  [path.join(repoRoot, 'system-map/index.html'), ['Bionic Banker System Map', 'Record map', 'Questions for the reader']],
  [path.join(repoRoot, 'world-map/index.html'), ['AI + Finance World Map', 'Five systems, one data story', 'Reading paths']],
  [path.join(repoRoot, 'about/index.html'), ['About Hash', 'Serious work can still feel alive']],
  [path.join(repoRoot, 'index.html'), ['href="/start-here"', 'href="/world-map"']],
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
  'opportunity pack',
  'role packet',
  'role packets',
  'recruiter',
  'review packet',
  'review packets',
  'case packet',
  'case packets',
  'portfolio-grade',
  'founder/operator proof map',
  'if you are reviewing this for a role',
  'questions for hash',
];
for (const phrase of banned) {
  assert(!combined.includes(phrase), `World map source contains banned phrase: ${phrase}`);
}

console.log('WORLD_MAP_CHECK PASS — mission map, system map, world map, source-led wording, green theme guard, and no-long-dash guard are present.');
