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
  proofPack: path.join(root, 'src/pages/proof-pack.astro'),
  home: path.join(root, 'src/pages/index.astro'),
  projects: path.join(root, 'src/pages/projects.astro'),
};

const source = Object.fromEntries(Object.entries(sourceFiles).map(([key, file]) => [key, read(file)]));

const startHerePhrases = [
  'Start Here / Reviewer Guide',
  'AI-assisted finance risk workflows that show their work and keep humans in control',
  '90-second path',
  'Wallet Risk Assessment',
  'AML Status Evidence',
  'Fraud Alert Triage Workflow',
  'Agent Chess / Agent Workflow',
  'Site Health / Proof QA',
  'Recruiter',
  'Collaborator',
  'Executive / investor',
  'Technical reviewer',
  'No live trading, wallet movement, or fund-transfer authority',
];

const proofPackPhrases = [
  'Bionic Banker Proof Pack',
  'A compressed proof packet for AI-assisted finance risk workflows',
  'Flagship systems',
  'Evidence map',
  'Technical stack',
  'Trust boundary',
  'Questions to ask Hash',
  'Public system cards',
  'Evidence catalog lanes',
  'No SAR filing, KYC approval, enforcement, or final compliance decision',
];

for (const phrase of startHerePhrases) {
  assert(source.startHere.includes(phrase), `/start-here source is missing required phrase: ${phrase}`);
}

for (const phrase of proofPackPhrases) {
  assert(source.proofPack.includes(phrase), `/proof-pack source is missing required phrase: ${phrase}`);
}

for (const phrase of ['/start-here', '/proof-pack']) {
  assert(source.home.includes(phrase), `Homepage source must link to ${phrase}`);
}

for (const phrase of [
  'Can Hash reason about risk signals without turning a score into a verdict?',
  'Can Hash preserve auditability and authority boundaries?',
  'Can Hash turn messy fraud signals into a review-ready packet?',
  'Can Hash design AI-agent workflows where humans keep authority?',
]) {
  assert(source.projects.includes(phrase), `Projects source missing reviewer question: ${phrase}`);
}

const builtChecks = [
  [path.join(repoRoot, 'start-here/index.html'), ['Start Here / Reviewer Guide', '90-second path', 'No live trading, wallet movement, or fund-transfer authority']],
  [path.join(repoRoot, 'proof-pack/index.html'), ['Bionic Banker Proof Pack', 'Evidence map', 'Questions to ask Hash']],
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

console.log('OPPORTUNITY_ENGINE_CHECK PASS — reviewer guide, proof pack, homepage links, and reviewer questions are present.');
