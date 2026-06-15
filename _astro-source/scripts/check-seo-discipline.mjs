import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(process.cwd(), '..');
const dist = path.resolve(process.cwd(), 'dist');
const target = fs.existsSync(dist) ? dist : root;
const htmlFiles = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    const rel = path.relative(target, full);
    if (entry.isDirectory()) {
      if (['node_modules', '.git'].includes(entry.name)) continue;
      walk(full);
    } else if (entry.name === 'index.html') {
      htmlFiles.push(full);
    }
  }
}
walk(target);

const ignorePrefixes = ['blog-visuals/', 'dashboard-data/', 'proof-pack/'];
const issues = [];
const text = (value='') => value.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
for (const file of htmlFiles) {
  const rel = path.relative(target, file).replaceAll(path.sep, '/');
  if (ignorePrefixes.some((prefix) => rel.startsWith(prefix))) continue;
  const html = fs.readFileSync(file, 'utf8');
  const title = html.match(/<title[^>]*>([\s\S]*?)<\/title>/i);
  const desc = html.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)/i);
  const canon = html.match(/<link[^>]+rel=["']canonical["'][^>]+href=["']([^"']*)/i);
  const h1s = html.match(/<h1\b/gi) || [];
  const titleText = text(title?.[1] || '');
  const descText = desc?.[1] || '';
  if (!titleText) issues.push(`${rel}: missing title`);
  if (titleText.length > 68) issues.push(`${rel}: title too long (${titleText.length})`);
  if (!descText) issues.push(`${rel}: missing description`);
  if (descText && descText.length < 50) issues.push(`${rel}: description too short (${descText.length})`);
  if (descText && descText.length > 185) issues.push(`${rel}: description too long (${descText.length})`);
  if (!canon) issues.push(`${rel}: missing canonical`);
  if (h1s.length !== 1) issues.push(`${rel}: expected 1 h1, found ${h1s.length}`);
}
if (issues.length) {
  console.log(`SEO_DISCIPLINE_REVIEW ${issues.length} soft issue(s)`);
  for (const issue of issues.slice(0, 80)) console.log(issue);
  if (issues.length > 80) console.log(`... ${issues.length - 80} more`);
  console.log('SEO_DISCIPLINE_SOFT_PASS — review above, not blocking publish');
  process.exit(0);
}
console.log(`SEO_DISCIPLINE_PASS ${htmlFiles.length} html files scanned`);
