import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const read = (relativePath) => fs.readFileSync(path.join(root, relativePath), 'utf8');
const assertIncludes = (text, needle, label) => {
  if (!text.includes(needle)) {
    console.error(`CONTENT_SYSTEM_CHECK FAIL — missing ${label}: ${needle}`);
    process.exit(1);
  }
};
const assertNotIncludes = (text, needle, label) => {
  if (text.includes(needle)) {
    console.error(`CONTENT_SYSTEM_CHECK FAIL — forbidden ${label}: ${needle}`);
    process.exit(1);
  }
};

const page = read('src/pages/content-system.astro');
const layout = read('src/layouts/BaseLayout.astro');
const systemMap = read('src/pages/system-map.astro');
const packageJson = read('package.json');

[
  ['Bionic Banker Content System', 'page title'],
  ['One source record. Many public formats. Same limits.', 'hero rule'],
  ['Publish the full record first. Draft distribution second.', 'operating rule'],
  ['Long record', 'long record step'],
  ['Short note', 'short note step'],
  ['Platform draft', 'platform draft step'],
  ['Human post', 'human post step'],
  ['LinkedIn', 'LinkedIn format'],
  ['X', 'X format'],
  ['dev.to', 'dev.to format'],
  ['Telegram / email', 'Telegram email format'],
  ['Required draft packet', 'draft packet section'],
  ['Source page', 'source page field'],
  ['Clear limit', 'clear limit field'],
  ['Approval status', 'approval status field'],
  ['No automated public posting until templates are stable and approval is explicit.', 'automation approval guardrail'],
  ['No trading calls, copy-trade instructions, KYC decisions, SAR filings, or wallet-control claims.', 'public safety guardrail'],
  ['Status:</b> Draft only until reviewed and posted by a human.', 'human-posting status'],
].forEach(([needle, label]) => assertIncludes(page, needle, label));

[
  ['auto-post by default', 'auto-post phrasing'],
  ['guaranteed reach', 'social hype'],
  ['trading alert', 'trading alert framing'],
  ['I shipped', 'internal build log'],
  ['Hash asked', 'private conversation leak'],
  ['commit ', 'commit chatter'],
].forEach(([needle, label]) => assertNotIncludes(page, needle, label));

assertIncludes(layout, 'href="/content-system"', 'footer/mobile content-system link');
assertIncludes(systemMap, "['Content System', '/content-system'", 'system map content-system row');
assertIncludes(systemMap, '8 inspectable systems, one map.', 'system count updated');
assertIncludes(packageJson, 'test:content-system', 'package script');
assertIncludes(packageJson, 'npm run test:content-system', 'test chain');

console.log('CONTENT_SYSTEM_CHECK PASS — source-to-social draft system is website-first, approval-gated, and bounded.');
