import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const sourceRoot = process.cwd();
const repoRoot = join(sourceRoot, '..');

function read(file) {
  if (!existsSync(file)) throw new Error(`Missing required file: ${file}`);
  return readFileSync(file, 'utf8');
}

function assert(condition, message) {
  if (!condition) {
    console.error(`EPISTEMIC_HARNESS_FAIL: ${message}`);
    process.exit(1);
  }
}

const agents = read(join(repoRoot, 'AGENTS.md'));
const standard = read(join(repoRoot, 'PUBLIC_COPY_STANDARD.md'));
const packageJson = JSON.parse(read(join(sourceRoot, 'package.json')));

const requiredStandardPhrases = [
  'Uncertainty and source honesty harness',
  'sound correct before it sounds confident',
  'If a fact is not fully checked, say so clearly',
  'Do not invent paper titles, URLs, authors, studies, statistics, books, legal cases, quotes, company reports, or historical references',
  'not verified yet',
  'This page cannot decide',
  'This is a source note, not a conclusion',
];

for (const phrase of requiredStandardPhrases) {
  assert(standard.includes(phrase), `PUBLIC_COPY_STANDARD.md must preserve: ${phrase}`);
}

const requiredAgentPhrases = [
  'If a claim is uncertain, missing context, or only a best estimate, say so plainly',
  'Do not invent sources, URLs, studies, statistics, quotes, legal cases, company reports, or historical references',
  'npm run test:epistemic-harness',
];

for (const phrase of requiredAgentPhrases) {
  assert(agents.includes(phrase), `AGENTS.md must preserve: ${phrase}`);
}

assert(packageJson.scripts?.['test:epistemic-harness'] === 'node scripts/check-epistemic-harness.mjs', 'package.json must expose test:epistemic-harness');
assert(packageJson.scripts?.test?.includes('test:epistemic-harness'), 'npm test must include test:epistemic-harness');

const highRiskPublicFiles = [
  join(sourceRoot, 'src', 'pages', 'aml-status-evidence.astro'),
  join(sourceRoot, 'src', 'pages', 'wallet-risk.astro'),
  join(sourceRoot, 'src', 'pages', 'signals.astro'),
  join(sourceRoot, 'src', 'pages', 'risk-evidence-overview.astro'),
  join(sourceRoot, 'src', 'pages', 'projects.astro'),
].filter(existsSync);

const combined = highRiskPublicFiles.map((file) => read(file)).join('\n').toLowerCase();

for (const phrase of ['source trail', 'missing context', 'clear limit']) {
  assert(combined.includes(phrase), `high-risk public pages must preserve epistemic phrase: ${phrase}`);
}

const blockedPublicClaims = [
  ['guaranteed compliance', /guaranteed compliance/i],
  ['guaranteed return', /guaranteed return/i],
  ['safe wallet', /safe wallet/i],
  ['clean wallet', /clean wallet/i],
  ['approved KYC', /approved kyc|kyc approved/i],
  ['autonomous profit', /autonomous profit/i],
  ['live execution enabled', /live execution enabled/i],
  ['buy now', /buy now/i],
  ['sell now', /sell now/i],
  ['copy this trade', /copy this trade/i],
];

for (const [label, regex] of blockedPublicClaims) {
  assert(!regex.test(combined), `high-risk public pages must not contain unsafe claim: ${label}`);
}

console.log(`EPISTEMIC_HARNESS_CHECK PASS — docs, npm wiring, and ${highRiskPublicFiles.length} high-risk public pages preserve source/uncertainty limits.`);
