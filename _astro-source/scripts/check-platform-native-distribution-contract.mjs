import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const repoRoot = path.resolve(root, '..');
const fail = [];
const warn = [];

const read = (p) => fs.readFileSync(path.join(repoRoot, p), 'utf8');
const exists = (p) => fs.existsSync(path.join(repoRoot, p));

const requiredFiles = [
  'distribution/platform-native-distribution-agent-charter.md',
  'distribution/distribution-metrics-ledger.md',
  'distribution/post-ledger.json',
];

for (const file of requiredFiles) {
  if (!exists(file)) fail.push(`missing required distribution contract file: ${file}`);
}

const charter = exists('distribution/platform-native-distribution-agent-charter.md')
  ? read('distribution/platform-native-distribution-agent-charter.md')
  : '';
const ledger = exists('distribution/distribution-metrics-ledger.md')
  ? read('distribution/distribution-metrics-ledger.md')
  : '';

const requiredCharterPhrases = [
  'public value first',
  'platform-native format second',
  'Bionic article / asset link third',
  'recognizable mistake',
  'sharp control model',
  'practitioner question',
  'article link in first comment',
  'No AI-generated text inside images',
  'publish without approval',
  'engagement pods',
  'Borrow structure, not identity',
];

const charterLower = charter.toLowerCase();
for (const phrase of requiredCharterPhrases) {
  if (!charterLower.includes(phrase.toLowerCase())) fail.push(`distribution charter missing locked phrase: ${phrase}`);
}

const requiredLedgerFields = [
  'impressions_2h',
  'impressions_24h',
  'impressions_7d',
  'reactions',
  'comments',
  'reposts',
  'saves',
  'profile_views',
  'new_followers',
  'what_worked',
  'what_failed',
  'next_test',
];

for (const field of requiredLedgerFields) {
  if (!ledger.includes(field)) fail.push(`distribution metrics ledger missing field: ${field}`);
}

const distributionDir = path.join(repoRoot, 'distribution');
const captionFiles = fs.existsSync(distributionDir)
  ? fs.readdirSync(distributionDir).filter((name) => /^linkedin-.*\.md$/.test(name))
  : [];

for (const file of captionFiles) {
  const rel = `distribution/${file}`;
  const text = read(rel);
  if (!/first comment/i.test(text)) {
    warn.push(`${rel}: LinkedIn package should include first-comment link guidance`);
  }
  if (!/(engagement question|what ai-generated output|what would prove|question)/i.test(text)) {
    warn.push(`${rel}: LinkedIn package should include a practitioner engagement question`);
  }
  const captionBlock = text.match(/## Caption\s*([\s\S]*)/i)?.[1] || text;
  const mainBodyUrlCount = (captionBlock.match(/https?:\/\//g) || []).length;
  const hasFirstCommentSection = /first comment/i.test(text);
  if (mainBodyUrlCount > 0 && !hasFirstCommentSection) {
    warn.push(`${rel}: LinkedIn URL appears without first-comment section; old packages should be migrated before reuse`);
  }
  const hashtags = captionBlock.match(/#[A-Za-z][A-Za-z0-9_]*/g) || [];
  if (hashtags.length > 10) warn.push(`${rel}: too many hashtags (${hashtags.length}); target 5-8 sharp tags`);
}

const socialRoot = path.join(repoRoot, 'social-assets/linkedin-ready');
if (fs.existsSync(socialRoot)) {
  const stack = [socialRoot];
  while (stack.length) {
    const dir = stack.pop();
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const full = path.join(dir, entry.name);
      if (entry.isDirectory()) stack.push(full);
      if (entry.isFile() && entry.name.endsWith('.png')) {
        const rel = path.relative(repoRoot, full);
        const stat = fs.statSync(full);
        if (stat.size < 100_000) warn.push(`${rel}: PNG is small; verify it is not a placeholder`);
      }
    }
  }
}

if (fail.length) {
  console.error('PLATFORM_NATIVE_DISTRIBUTION_CONTRACT_FAIL');
  for (const item of fail) console.error(`- ${item}`);
  if (warn.length) {
    console.error('warnings:');
    for (const item of warn) console.error(`- ${item}`);
  }
  process.exit(1);
}

console.log('PLATFORM_NATIVE_DISTRIBUTION_CONTRACT_PASS');
console.log(`caption_packages_checked=${captionFiles.length}`);
if (warn.length) {
  console.log('warnings:');
  for (const item of warn) console.log(`- ${item}`);
}
