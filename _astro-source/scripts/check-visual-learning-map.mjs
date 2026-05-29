import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const failures = [];

function read(rel) {
  const file = path.join(root, rel);
  if (!fs.existsSync(file)) {
    failures.push(`missing file: ${rel}`);
    return '';
  }
  return fs.readFileSync(file, 'utf8');
}

function requirePhrase(text, phrase, label) {
  if (!text.includes(phrase)) failures.push(`missing ${label}: ${phrase}`);
}

const mapText = read('public/dashboard-data/visual-learning-map.json');
let map;
try {
  map = JSON.parse(mapText);
} catch (error) {
  failures.push(`visual-learning-map.json is not valid JSON: ${error.message}`);
  map = { learning_lanes: [], infographic_backlog: [] };
}

if (map.status !== 'visual_learning_map_v2') failures.push('visual learning map status must be visual_learning_map_v2');
if (!map.risk_pattern_thesis) failures.push('visual learning map must include risk_pattern_thesis');
if (!Array.isArray(map.learning_lanes) || map.learning_lanes.length < 6) failures.push('visual learning map must include at least 6 learning lanes');
if (!Array.isArray(map.infographic_backlog) || map.infographic_backlog.length < 4) failures.push('visual learning map must include at least 4 infographic backlog items');

const requiredLaneIds = [
  'wallet-watch-map',
  'kyc-record-map',
  'stablecoin-settlement-map',
  'agent-risk-map',
  'country-practice-map',
  'failure-library-map',
];
const laneIds = new Set((map.learning_lanes ?? []).map((lane) => lane.id));
for (const id of requiredLaneIds) {
  if (!laneIds.has(id)) failures.push(`missing learning lane: ${id}`);
}

for (const lane of map.learning_lanes ?? []) {
  for (const field of ['label', 'title', 'reader_question', 'behavior_lens', 'visual_shape', 'next_surface', 'clear_limit']) {
    if (!lane[field]) failures.push(`${lane.id ?? 'unknown lane'} missing ${field}`);
  }
  if (!/limit|No |Not |not |cannot|human|approval/i.test(lane.clear_limit ?? '')) {
    failures.push(`${lane.id} must state a clear limit`);
  }
}

const aiPage = read('src/pages/ai-intelligence.astro');
const signalsPage = read('src/pages/signals.astro');
const walletFlowSvg = read('public/assets/public-wallet-watch-flow.svg');
for (const phrase of [
  'visual-learning-map.json',
  'Risk pattern thesis',
  'Critical feedback: the idea is strong only if each page follows one concrete trail.',
  'Visual learning map',
  'source trail, system record, missing context, and clear limit',
  'Infographic queue',
]) {
  requirePhrase(aiPage, phrase, 'AI intelligence visual map phrase');
}

const plan = read('../VISUAL_LEARNING_ROADMAP.md');
const thesisPlan = read('../BIONIC_BANKER_RISK_PATTERN_THESIS.md');
for (const phrase of [
  'Bionic Banker Visual Learning Roadmap Implementation Plan',
  'country / public source / practice / what it teaches / what cannot be concluded',
  'what broke / missing control / safer check / Bionic Banker page that teaches it',
]) {
  requirePhrase(plan, phrase, 'visual roadmap plan phrase');
}


for (const phrase of [
  'Bionic Banker Risk Pattern Thesis',
  'technology shift → behavior change → money trail → risk pattern → compliance question → software/filter idea → clear limit',
  'compare record shapes, not tribes.',
  'Patterns create questions, not commands.',
]) {
  requirePhrase(thesisPlan, phrase, 'risk pattern thesis plan phrase');
}

for (const phrase of [
  'Technology changes behavior. Behavior leaves trails.',
  'risk pattern',
  'software or filter idea',
  'Public trails are incomplete records.',
  'DeFi and centralized finance are different record systems',
]) {
  requirePhrase(mapText, phrase, 'risk pattern thesis data phrase');
}


for (const phrase of [
  'wallet-watch-infographic',
  'public-wallet-watch-flow.svg',
  'Source trail before interpretation.',
  'public source, label context, activity category, AML review question, missing context, and clear limit',
]) {
  requirePhrase(signalsPage, phrase, 'signals infographic phrase');
}

for (const phrase of [
  'Public wallet watch source to review question flow',
  'Source trail before interpretation',
  'Reader rule: show the source, show the question, show what the system cannot decide.',
]) {
  requirePhrase(walletFlowSvg, phrase, 'wallet watch SVG phrase');
}

for (const phrase of ['Country-by-country risk practice notes', 'Learn from other people’s mistakes']) {
  requirePhrase(mapText, phrase, 'visual learning map data phrase');
}

const combined = [mapText, aiPage, signalsPage, walletFlowSvg, plan, thesisPlan].join('\n');
const banned = [
  /copy this trade/i,
  /buy now/i,
  /sell now/i,
  /KYC approved/i,
  /guaranteed compliance/i,
  /prediction engine/i,
  /market prediction/i,
  /legal determination/i,
  /live execution enabled/i,
  /wallet power:\s*true/i,
  /trade power:\s*true/i,
  /from flask import/i,
  /subprocess\.(run|Popen)/i,
  /localhost:\d+/i,
  /GROQ_API_KEY/i,
  /console-api\//i,
  /wukong-side/i,
  /70-ops-logs/i,
  /Bankache/i,
  /Bancake/i,
];
for (const pattern of banned) {
  if (pattern.test(combined)) failures.push(`visual learning map contains banned public-safety pattern: ${pattern}`);
}

if (failures.length) {
  console.error('VISUAL_LEARNING_MAP_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log('VISUAL_LEARNING_MAP_CHECK PASS — AI finance risk, behavior trails, compliance case-study, country-practice, and infographic roadmap are source-led and bounded.');
