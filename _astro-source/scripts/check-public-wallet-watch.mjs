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
  [walletRisk, 'Public addresses can improve the AML learning layer', 'wallet-risk AML connection'],
  [walletRisk, 'No wallet control, no private identity claim, no compliance verdict, and no copy-trading instruction', 'wallet-risk public limit'],
  [aml, 'Public blockchain watching belongs here only as source context', 'AML source-context section'],
  [aml, 'No accusation, no KYC approval, no filing, no wallet control, no Pancake unfreeze', 'AML blocked boundary'],
];

for (const [text, phrase, label] of requiredSource) {
  if (!text.includes(phrase)) fail(`missing ${label}: ${phrase}`);
}

if (catalog.status !== 'public_wallet_watch_template_v1') fail('template status must be public_wallet_watch_template_v1');
if (!catalog.report_fields?.some((field) => field.field === 'aml_review_question')) fail('template must include aml_review_question');
if (!catalog.blocked_actions?.some((item) => /No trading advice/i.test(item))) fail('template must block trading advice');
if (!catalog.blocked_actions?.some((item) => /Pancake/i.test(item))) fail('template must keep Pancake blocked');
if (!catalog.allowed_actions?.some((item) => /public blockchain explorers/i.test(item))) fail('template must allow public explorer sources');

const forbidden = [
  /copy this trade/i,
  /buy now/i,
  /sell now/i,
  /guaranteed/i,
  /wallet authority:\s*true/i,
  /may_execute:\s*true/i,
];
for (const [label, text] of [['signals', signals], ['wallet-risk', walletRisk], ['aml-status', aml], ['template', JSON.stringify(catalog)]]) {
  for (const pattern of forbidden) {
    if (pattern.test(text)) fail(`${label} contains forbidden phrase/pattern: ${pattern}`);
  }
}

if (!process.exitCode) console.log('PUBLIC_WALLET_WATCH PASS — template, AML connection, and safety boundaries are present.');
