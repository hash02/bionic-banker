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
const updates = read('src/pages/updates.astro');
const combined = `${layout}\n${updates}`;

for (const phrase of [
  'Get source notes and system records when Bionic Banker publishes a finance and AI source report. No trading calls, no hype.',
  'Read the update promise',
  '/updates',
  'https://t.me/BionicBanker',
]) {
  requireIncludes(layout, phrase, 'newsletter/update layout');
}

for (const phrase of [
  'Source notes and system records, not trading calls.',
  'what changed, what source supports it, what Bionic Banker recorded, and what the record cannot decide',
  'What it cannot do',
  'No trade instruction, no compliance approval, no KYC decision, no automated filing, and no wallet control.',
  'Telegram format',
  'Short release notes, with the limit included.',
  'These are learning records, not trading or compliance instructions.',
]) {
  requireIncludes(updates, phrase, 'updates reader promise');
}

for (const pattern of [
  /alpha/i,
  /best signals/i,
  /trading alerts/i,
  /copy trade/i,
  /guaranteed/i,
  /insider/i,
  /buy now/i,
  /sell now/i,
  /profit/i,
  /may_execute:\s*true/i,
  /wallet power:\s*true/i,
  /trade power:\s*true/i,
]) {
  requireAbsent(combined, pattern, 'updates public-safety language');
}

if (failures.length) {
  console.error('UPDATE_PROMISE_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log('UPDATE_PROMISE_CHECK PASS — subscription and Telegram promise stay source-led, non-advisory, and bounded.');
