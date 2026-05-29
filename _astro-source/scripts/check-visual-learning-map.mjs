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

if (map.status !== 'visual_learning_map_v1') failures.push('visual learning map status must be visual_learning_map_v1');
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
  for (const field of ['label', 'title', 'reader_question', 'visual_shape', 'next_surface', 'clear_limit']) {
    if (!lane[field]) failures.push(`${lane.id ?? 'unknown lane'} missing ${field}`);
  }
  if (!/limit|No |Not |not |cannot|human|approval/i.test(lane.clear_limit ?? '')) {
    failures.push(`${lane.id} must state a clear limit`);
  }
}

const aiPage = read('src/pages/ai-intelligence.astro');
for (const phrase of [
  'visual-learning-map.json',
  'Visual learning map',
  'source trail, system record, missing context, and clear limit',
  'Infographic queue',
]) {
  requirePhrase(aiPage, phrase, 'AI intelligence visual map phrase');
}

const plan = read('../VISUAL_LEARNING_ROADMAP.md');
for (const phrase of [
  'Bionic Banker Visual Learning Roadmap Implementation Plan',
  'country / public source / practice / what it teaches / what cannot be concluded',
  'what broke / missing control / safer check / Bionic Banker page that teaches it',
]) {
  requirePhrase(plan, phrase, 'visual roadmap plan phrase');
}

for (const phrase of ['Country-by-country risk practice notes', 'Learn from other people’s mistakes']) {
  requirePhrase(mapText, phrase, 'visual learning map data phrase');
}

const combined = [mapText, aiPage, plan].join('\n');
const banned = [
  /copy this trade/i,
  /buy now/i,
  /sell now/i,
  /KYC approved/i,
  /guaranteed compliance/i,
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

console.log('VISUAL_LEARNING_MAP_CHECK PASS — AI finance risk, compliance case-study, country-practice, and infographic roadmap is source-led and bounded.');
