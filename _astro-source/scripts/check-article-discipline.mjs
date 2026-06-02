import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const blogDir = path.join(root, 'src', 'content', 'blog');
const distDir = path.join(root, 'dist', 'blog');
const failures = [];

const priority = [
  'wallet-risk-notes',
  'what-claude-cant-do-for-kyc',
  'canada-stablecoin-settlement',
  'web3-is-just-finance-infrastructure',
  'agentic-ai-banking',
  'consensus-is-not-truth',
  'openclaw-security',
  'zkp-explained',
  'defi',
  'aml-engine'
];

const requiredSections = [
  '## Source trail',
  '## Related Bionic Banker records',
  '## Clear limits',
  '## Next read',
  '## Diagram hook'
];

function read(file) {
  if (!fs.existsSync(file)) {
    failures.push(`Missing file: ${path.relative(root, file)}`);
    return '';
  }
  return fs.readFileSync(file, 'utf8');
}

function slugToTitle(slug) {
  return slug.replaceAll('-', ' ');
}

for (const slug of priority) {
  const sourcePath = path.join(blogDir, `${slug}.md`);
  const md = read(sourcePath);
  if (!md) continue;

  for (const heading of requiredSections) {
    if (!md.includes(heading)) failures.push(`${slug}: missing ${heading}`);
  }

  const bionicLinks = [...md.matchAll(/\]\((\/(?:blog|wallet-risk|signals|ai-intelligence|aml-status-evidence|risk-evidence-overview|system-map|reports|articles|start-here)[^)]+)\)/g)].map((m) => m[1]);
  if (new Set(bionicLinks).size < 2) failures.push(`${slug}: needs at least two internal Bionic Banker record links`);

  const httpLinks = [...md.matchAll(/https?:\/\/[^\s)]+/g)].map((m) => m[0]);
  if (new Set(httpLinks).size < 2) failures.push(`${slug}: needs at least two external source links`);

  const clearLimit = md.match(/## Clear limits[\s\S]*?(?=\n## |$)/)?.[0] ?? '';
  const limitWords = ['not investment advice', 'not trading advice', 'not a compliance verdict', 'does not prove wrongdoing', 'requires human review', 'not a filing decision'];
  if (!limitWords.some((word) => clearLimit.toLowerCase().includes(word))) {
    failures.push(`${slug}: clear limits section needs explicit non-advisory or human-review boundary`);
  }

  const diagramHook = md.match(/## Diagram hook[\s\S]*?(?=\n## |$)/)?.[0] ?? '';
  if (!/diagram|infographic|visual/i.test(diagramHook)) failures.push(`${slug}: diagram hook must name a diagram/infographic/visual`);

  const builtPath = path.join(distDir, slug, 'index.html');
  if (fs.existsSync(builtPath)) {
    const built = read(builtPath);
    for (const phrase of ['Source trail', 'Related Bionic Banker records', 'Clear limits', 'Next read']) {
      if (!built.includes(phrase)) failures.push(`${slug}: built HTML missing ${phrase}`);
    }
  }
}

const banned = [
  /copy this trade/i,
  /buy now/i,
  /sell now/i,
  /guaranteed/i,
  /may_execute:\s*true/i,
  /private key/i,
  /seed phrase/i
];
for (const slug of priority) {
  const md = read(path.join(blogDir, `${slug}.md`));
  for (const pattern of banned) {
    if (pattern.test(md)) failures.push(`${slug}: banned public wording ${pattern}`);
  }
}

if (failures.length) {
  console.error('ARTICLE_DISCIPLINE_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log(`ARTICLE_DISCIPLINE_CHECK PASS — ${priority.length} priority articles carry source trails, internal records, limits, next reads, and diagram hooks.`);
