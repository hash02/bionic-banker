import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const fail = [];
const warn = [];

const workPath = path.join(root, 'src/pages/work.astro');
if (!fs.existsSync(workPath)) {
  fail.push('/work/ page source missing: src/pages/work.astro');
}

const text = fs.existsSync(workPath) ? fs.readFileSync(workPath, 'utf8') : '';
const lower = text.toLowerCase();

const required = [
  'I build governed AI systems for finance',
  'Himanshu',
  'Canadian banking',
  'AI governance',
  'AML Detection Engine',
  'Agent Governance / Audit Trail',
  'AI Financial Advice Review Layer',
  'Prototype proof',
  'Boundary:',
  'LinkedIn',
  'GitHub',
  'Python, LangGraph, FastAPI',
];

for (const phrase of required) {
  if (!text.includes(phrase)) fail.push(`/work/ missing required phrase: ${phrase}`);
}

const cardCount = (text.match(/title: '/g) || []).length;
if (cardCount < 3 || cardCount > 4) fail.push(`/work/ must have 3-4 proof definitions; found ${cardCount}`);

const firstProof = text.indexOf('AML Detection Engine');
const agentProof = text.indexOf('Agent Governance / Audit Trail');
const adviceProof = text.indexOf('AI Financial Advice Review Layer');
if (!(firstProof > -1 && agentProof > -1 && adviceProof > -1 && firstProof < agentProof && agentProof < adviceProof)) {
  fail.push('/work/ proof order must be AML first, Agent Governance second, Advice Review Layer third');
}

const forbidden = [
  'BTC direction',
  '44%',
  'May 2026',
  'Wukong',
  'Hermes',
  '/home/hash',
  'private prompt',
  'revenue flywheel',
  'traffic and products',
  'planned pages',
  'source-review queue',
  'heartbeat',
];
for (const phrase of forbidden) {
  if (text.includes(phrase)) fail.push(`/work/ contains forbidden first-impression/private/stale phrase: ${phrase}`);
}

const boundaryCount = (text.match(/boundary: '/g) || []).length;
if (boundaryCount < 3) fail.push(`/work/ must include boundary language on every proof definition; found ${boundaryCount}`);

const words = text
  .replace(/---[\s\S]*?---/, '')
  .replace(/<style>[\s\S]*?<\/style>/g, '')
  .replace(/<[^>]+>/g, ' ')
  .replace(/[{}()<>/="'.:,;`\[\]-]/g, ' ')
  .split(/\s+/)
  .filter(Boolean);
if (words.length > 900) warn.push(`/work/ source copy is ${words.length} words; keep visible page concise`);

const indexPath = path.join(root, 'src/pages/index.astro');
if (fs.existsSync(indexPath)) {
  const index = fs.readFileSync(indexPath, 'utf8');
  if (!index.includes('href="/work/"')) fail.push('homepage must include a CTA to /work/');
}

if (fail.length) {
  console.error('WORK_PAGE_CONTRACT_FAIL');
  for (const item of fail) console.error(`- ${item}`);
  if (warn.length) {
    console.error('warnings:');
    for (const item of warn) console.error(`- ${item}`);
  }
  process.exit(1);
}

console.log('WORK_PAGE_CONTRACT_PASS');
console.log(`proof_cards=${cardCount}`);
console.log(`visible_copy_words_estimate=${words.length}`);
if (warn.length) {
  console.log('warnings:');
  for (const item of warn) console.log(`- ${item}`);
}
