import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve('..');
const htmlFiles = [];
function walk(dir) {
  if (!fs.existsSync(dir)) return;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (['node_modules', '.git', '_astro-source'].includes(entry.name)) continue;
      walk(p);
    } else if (entry.name.endsWith('.html')) {
      htmlFiles.push(p);
    }
  }
}
walk(root);

const assetExt = /\.(png|jpe?g|webp|gif|svg|avif|ico|css|js|pdf|json|md|xml|txt|html)$/i;
const localRoute = (url) => url.startsWith('/') && !url.startsWith('//');
const failures = [];

for (const file of htmlFiles) {
  const text = fs.readFileSync(file, 'utf8');
  const ids = new Set([...text.matchAll(/\sid=["']([^"']+)["']/g)].map((m) => m[1]));
  for (const match of text.matchAll(/(?:href|src)=["']([^"']+)["']/g)) {
    const raw = match[1];
    if (!localRoute(raw)) continue;
    const [withoutHash, hash] = raw.split('#');
    const url = withoutHash.split('?')[0];
    if (hash && (url === '' || url === path.posix.join('/', path.relative(root, file).replaceAll('\\','/')).replace(/index\.html$/, ''))) {
      if (!ids.has(hash)) failures.push(`${path.relative(root, file)} missing local anchor #${hash}`);
    }
    if (!url || url === '/') continue;
    let target;
    if (assetExt.test(url)) {
      target = path.join(root, url.slice(1));
    } else {
      target = path.join(root, url.slice(1), 'index.html');
    }
    if (!fs.existsSync(target)) failures.push(`${path.relative(root, file)} -> ${raw} missing ${path.relative(root, target)}`);
  }
}

if (failures.length) {
  console.error('PUBLIC_LINKS_ASSETS FAIL');
  for (const failure of failures.slice(0, 100)) console.error(`- ${failure}`);
  if (failures.length > 100) console.error(`... ${failures.length - 100} more`);
  process.exit(1);
}
console.log(`PUBLIC_LINKS_ASSETS PASS — checked ${htmlFiles.length} HTML files`);
