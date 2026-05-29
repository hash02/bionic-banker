import fs from 'node:fs';
import path from 'node:path';

const sourceRoot = process.cwd();
const read = (p) => fs.readFileSync(p, 'utf8');
const fail = (msg) => { console.error(`CONTEXT_ENGINE_LAYER FAIL: ${msg}`); process.exitCode = 1; };

const article = read(path.join(sourceRoot, 'src/content/blog/context-engine-missing-layer.md'));
const systemMap = read(path.join(sourceRoot, 'src/pages/system-map.astro'));
const svg = read(path.join(sourceRoot, 'public/assets/context-engine-map.svg'));
const wallet = JSON.parse(read(path.join(sourceRoot, 'public/dashboard-data/public-wallet-watch-template.json')));

const required = [
  [article, 'The Context Engine Is the Missing Layer', 'article title'],
  [article, 'Access is not understanding', 'access-not-understanding section'],
  [article, 'Show the source, show the question, show what the system cannot decide.', 'Bionic rule'],
  [article, '/assets/context-engine-map.svg', 'article infographic link'],
  [systemMap, 'Context Engine Map', 'system map row'],
  [systemMap, 'context-engine-map.svg', 'system map image'],
  [svg, 'Source check', 'svg source check'],
  [svg, 'AML review question', 'svg AML output'],
];

for (const [text, phrase, label] of required) {
  if (!text.includes(phrase)) fail(`missing ${label}: ${phrase}`);
}

if (wallet.status !== 'public_wallet_watch_template_v3') fail('wallet watch template must be v3');
const report002 = wallet.report_records?.find((record) => record.id === 'public-wallet-watch-002');
if (!report002) fail('Report 002 missing');
if (!/No movement claim/i.test(report002.what_moved)) fail('Report 002 must avoid movement claim before source review');
if (!/Pancake/i.test(report002.clear_limit)) fail('Report 002 must keep Pancake blocked');

const forbidden = [
  /buy now/i,
  /sell now/i,
  /copy this trade/i,
  /guaranteed/i,
  /may_execute:\s*true/i,
  /wallet authority:\s*true/i,
  /Bankache/i,
  /Bancake/i,
];
for (const [label, text] of [['article', article], ['system-map', systemMap], ['wallet-json', JSON.stringify(wallet)]]) {
  for (const pattern of forbidden) {
    if (pattern.test(text)) fail(`${label} contains forbidden pattern: ${pattern}`);
  }
}

if (!process.exitCode) console.log('CONTEXT_ENGINE_LAYER PASS — article, visual, system map, and Report 002 are source-led and bounded.');
