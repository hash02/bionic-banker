import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const failures = [];

function read(rel) {
  const file = path.join(root, rel);
  if (!fs.existsSync(file)) {
    failures.push(`missing ${rel}`);
    return '';
  }
  return fs.readFileSync(file, 'utf8');
}

function requireIncludes(text, phrase, label) {
  if (!text.includes(phrase)) failures.push(`${label} missing phrase: ${phrase}`);
}

function requireAbsent(text, pattern, label) {
  if (pattern.test(text)) failures.push(`${label} contains blocked pattern: ${pattern}`);
}

const layout = read('src/layouts/BaseLayout.astro');
const home = read('src/pages/index.astro');
const signals = read('src/pages/signals.astro');
const ai = read('src/pages/ai-intelligence.astro');
const articles = read('src/pages/articles.astro');
const standard = read('../PUBLIC_COPY_STANDARD.md');

for (const phrase of [
  'Start Here',
  'Systems',
  'Articles',
  'Inside finance. Mapping AI systems, risk signals, source trails, and reports.',
]) {
  requireIncludes(layout, phrase, 'layout navigation discipline');
}
for (const pattern of [/Start Quest/g, />Apps</g, />Blog</g]) {
  requireAbsent(layout, pattern, 'layout navigation discipline');
}

for (const phrase of [
  'Start Here',
  'Public reading room',
  'What this is',
  'What you can inspect',
  'What it cannot do',
  'View systems',
  'System records, source trails, and limits',
]) {
  requireIncludes(home, phrase, 'homepage front-door discipline');
}
for (const pattern of [/Start Quest/g, /Things that run/g, /No answers yet/g, /Opportunity<\/a>/g]) {
  requireAbsent(home, pattern, 'homepage front-door discipline');
}

for (const phrase of [
  'Signals are records for questions',
  'Record accuracy, not trading accuracy',
  'Last 100 saved rows',
  'record check rate',
  'source trail before interpretation',
  'not investment advice, not trading performance, not a recommendation',
  'Related study',
  'Related system',
]) {
  requireIncludes(signals, phrase, 'signals discipline');
}
for (const pattern of [/Signal Board/g, /accuracy<\/span>/g, /\{confidence\} confidence<\/span>/g]) {
  requireAbsent(signals, pattern, 'signals discipline');
}

for (const phrase of [
  'What Bionic Banker is tracking',
  'Public intelligence filter',
  'How the research loop works',
  'source record, public note, clear limit',
]) {
  requireIncludes(ai, phrase, 'AI intelligence discipline');
}
for (const pattern of [/What Agent Her is watching/g, /Agent Her makes the map/g, /Both level up/g]) {
  requireAbsent(ai, pattern, 'AI intelligence discipline');
}

for (const phrase of [
  'AI Systems',
  'Finance Risk',
  'Blockchain / DeFi',
  'Builder Notes',
  'Article discipline',
  'Source links',
  'Internal records',
  'Limits',
  'Next read',
]) {
  requireIncludes(articles, phrase, 'articles discipline');
}
requireAbsent(articles, /const categories = \['AI', 'Blockchain', 'Finance', 'Tech'\]/, 'articles discipline');

for (const phrase of [
  'Every public concept page should end with source links, internal records, limits, and a next read.',
]) {
  requireIncludes(standard, phrase, 'public copy standard discipline');
}

const combined = [layout, home, signals, ai, articles].join('\n');
for (const pattern of [
  /copy this trade/i,
  /buy now/i,
  /sell now/i,
    /wallet power:\s*true/i,
  /trade power:\s*true/i,
  /may_execute:\s*true/i,
  /Bankache|Bancake/i,
  /licensed compliance product(?!, unless explicitly negated|\s*\-|\.)/i,
]) {
  requireAbsent(combined, pattern, 'public safety discipline');
}

if (failures.length) {
  console.error('SITE_DISCIPLINE_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log('SITE_DISCIPLINE_CHECK PASS — front door, signals, AI intelligence, articles, and public boundaries are disciplined.');
