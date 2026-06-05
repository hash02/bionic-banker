import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const blogDir = path.join(root, 'src', 'content', 'blog');
const publicDir = path.join(root, 'public');
const failures = [];

const autopublishedSlugs = [
  'ai-stock-picks-wrong-first-use-case',
  'fraud-controls-platform-controls',
  'agentic-payments-receipt-layer',
  'private-stablecoin-settlement-control-map'
];

function read(file) {
  if (!fs.existsSync(file)) {
    failures.push(`Missing file: ${path.relative(root, file)}`);
    return '';
  }
  return fs.readFileSync(file, 'utf8');
}

function frontmatterValue(md, key) {
  const match = md.match(new RegExp(`^${key}:\\s*["']?([^"'\\n]+)["']?`, 'm'));
  return match?.[1]?.trim() ?? '';
}

for (const slug of autopublishedSlugs) {
  const sourcePath = path.join(blogDir, `${slug}.md`);
  const md = read(sourcePath);
  if (!md) continue;

  const image = frontmatterValue(md, 'image');
  if (!image) failures.push(`${slug}: autopublished articles must have a frontmatter image`);
  if (image && !image.startsWith('/blog-visuals/')) failures.push(`${slug}: image must live under /blog-visuals/`);
  if (image) {
    const imagePath = path.join(publicDir, image.replace(/^\//, ''));
    if (!fs.existsSync(imagePath)) failures.push(`${slug}: image asset missing at ${path.relative(root, imagePath)}`);

    const staticRootPath = path.join(root, '..', image.replace(/^\//, ''));
    if (!fs.existsSync(staticRootPath)) failures.push(`${slug}: built/root static image asset missing at ${path.relative(path.join(root, '..'), staticRootPath)}`);
  }

  if (!/## Source trail/i.test(md)) failures.push(`${slug}: missing Source trail section`);
  if (!/## Clear limit/i.test(md)) failures.push(`${slug}: missing Clear limit(s) section`);
  if (!/not investment advice/i.test(md)) failures.push(`${slug}: missing explicit not-investment-advice boundary`);
  if (!/not legal advice/i.test(md)) failures.push(`${slug}: missing explicit not-legal-advice boundary`);
  if (!/not tax advice/i.test(md)) failures.push(`${slug}: missing explicit not-tax-advice boundary`);

  const externalLinks = [...md.matchAll(/https?:\/\/[^\s)]+/g)].map((m) => m[0]);
  if (new Set(externalLinks).size < 2) failures.push(`${slug}: needs at least two external source links`);

  const visualRefs = [...md.matchAll(/\/blog-visuals\/[^"')\s]+/g)].map((m) => m[0]);
  if (!visualRefs.length) failures.push(`${slug}: body or frontmatter must reference a visual asset`);

  const banned = [
    /copy this trade/i,
    /buy now/i,
    /sell now/i,
    /guaranteed return/i,
    /investment recommendation/i,
    /trading signal/i,
    /private key/i,
    /seed phrase/i,
    /C:\\Users\\/i,
    /\/home\/hash\//i,
    /Wukong/i,
    /Her reporting/i
  ];
  for (const pattern of banned) {
    if (pattern.test(md)) failures.push(`${slug}: banned public wording ${pattern}`);
  }
}

if (failures.length) {
  console.error('AUTOPUBLISHER_CONTRACT_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`AUTOPUBLISHER_CONTRACT_CHECK PASS — ${autopublishedSlugs.length} autopublished article(s) include image, citations, limits, and public-safety boundaries.`);
