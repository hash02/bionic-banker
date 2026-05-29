import fs from 'node:fs';
import path from 'node:path';

const sourceRoot = process.cwd();
const read = (p) => fs.readFileSync(p, 'utf8');
const fail = (msg) => { console.error(`PUBLIC_WALLET_WATCH FAIL: ${msg}`); process.exitCode = 1; };

const signals = read(path.join(sourceRoot, 'src/pages/signals.astro'));
const walletRisk = read(path.join(sourceRoot, 'src/pages/wallet-risk.astro'));
const aml = read(path.join(sourceRoot, 'src/pages/aml-status-evidence.astro'));
const catalog = JSON.parse(read(path.join(sourceRoot, 'public/dashboard-data/public-wallet-watch-template.json')));

const requiredSource = [
  [signals, 'Public Wallet Watch report format', 'signals report template heading'],
  [signals, 'walletWatch.report_fields', 'signals template field renderer'],
  [signals, '/dashboard-data/public-wallet-watch-template.json', 'signals source JSON link'],
  [signals, 'First public-wallet report shelf', 'signals report shelf heading'],
  [signals, 'watchlist_review_queue', 'signals watchlist review renderer'],
  [signals, 'report_records', 'signals report records renderer'],
  [walletRisk, 'Public addresses can improve the AML learning layer', 'wallet-risk AML connection'],
  [walletRisk, 'No wallet control, no private identity claim, no compliance verdict, and no copy-trading instruction', 'wallet-risk public limit'],
  [aml, 'Public blockchain watching belongs here only as source context', 'AML source-context section'],
  [aml, 'No accusation, no KYC approval, no filing, no wallet control, no Pancake unfreeze', 'AML blocked boundary'],
];

for (const [text, phrase, label] of requiredSource) {
  if (!text.includes(phrase)) fail(`missing ${label}: ${phrase}`);
}

if (catalog.status !== 'public_wallet_watch_template_v2') fail('template status must be public_wallet_watch_template_v2');
if (!catalog.report_fields?.some((field) => field.field === 'aml_review_question')) fail('template must include aml_review_question');
if (!catalog.blocked_actions?.some((item) => /No trading advice/i.test(item))) fail('template must block trading advice');
if (!catalog.blocked_actions?.some((item) => /Pancake/i.test(item))) fail('template must keep Pancake blocked');
if (!catalog.allowed_actions?.some((item) => /public blockchain explorers/i.test(item))) fail('template must allow public explorer sources');
if (!catalog.source_review_rule?.includes('source trail')) fail('template must include a source-review rule');
if (!catalog.watchlist_review_queue?.some((item) => /Exchange hot wallet label/i.test(item.label))) fail('watchlist queue must include exchange hot wallet label source class');
if (!catalog.report_records?.some((record) => record.id === 'public-wallet-watch-001')) fail('report shelf must include public-wallet-watch-001');
if (!catalog.report_records?.some((record) => /full address withheld until source review/i.test(record.address_or_label))) fail('first report must keep full address withheld until source review');

const forbidden = [
  /copy this trade/i,
  /buy now/i,
  /sell now/i,
  /guaranteed/i,
  /wallet authority:\s*true/i,
  /may_execute:\s*true/i,
  /Bankache/i,
  /Bancake/i,
];
for (const [label, text] of [['signals', signals], ['wallet-risk', walletRisk], ['aml-status', aml], ['template', JSON.stringify(catalog)]]) {
  for (const pattern of forbidden) {
    if (pattern.test(text)) fail(`${label} contains forbidden phrase/pattern: ${pattern}`);
  }
}

if (!process.exitCode) console.log('PUBLIC_WALLET_WATCH PASS — template, report shelf, AML connection, Pancake spelling, and safety boundaries are present.');
