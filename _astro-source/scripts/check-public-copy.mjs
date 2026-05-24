import { readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative, extname, sep } from 'node:path';

const repoRoot = join(process.cwd(), '..');
const sourceRoot = process.cwd();

const scanRoots = [
  join(sourceRoot, 'src'),
  join(sourceRoot, 'public', 'dashboard-data'),
  join(sourceRoot, 'public', 'blog-visuals'),
  join(repoRoot, 'PUBLIC_COPY_STANDARD.md'),
  join(repoRoot, 'AGENTS.md'),
];

const extensions = new Set(['.astro', '.md', '.json', '.html', '.js', '.mjs', '.txt', '.xml']);
const ignoredParts = new Set(['node_modules', '.git', 'dist', '.astro', 'site-agent']);

const hardBlockers = [
  ['Proof Tour', /\bProof Tour\b/i],
  ['AML Proof', /\bAML Proof\b/i],
  ['proof page', /\bproof page\b/i],
  ['proof surface', /\bproof surface\b/i],
  ['proof path', /\bproof path\b/i],
  ['proof route', /\bproof route\b/i],
  ['Read the proof', /\bRead the proof\b/i],
  ['Wallet Risk Lab', /\bWallet Risk Lab\b/i],
  ['public workbench', /\bpublic workbench\b/i],
  ['Live Signals', /\bLive Signals\b/i],
  ['Experiments', /\bExperiments\b/],
  ['AI Learning', /\bAI Learning\b/i],
  ['vibe/vibes', /\bvibes?\b/i],
  ['magic', /\bmagic\b/i],
  ['truth layer', /\btruth layer\b/i],
  ['clean wallet', /\bclean wallet\b/i],
  ['safe wallet', /\bsafe wallet\b/i],
  ['guaranteed compliance', /\bguaranteed compliance\b/i],
  ['KYC approved', /\b(?:approved KYC|KYC approved)\b/i],
  ['autonomous profit', /\bautonomous profit\b/i],
  ['guaranteed return', /\bguaranteed return\b/i],
  ['live execution enabled', /\blive execution enabled\b/i],
  ['wallet authority true', /\bwallet authority\s*:\s*true\b/i],
  ['trade authority true', /\btrade authority\s*:\s*true\b/i],
];

const softBlockers = [
  ['roast/roaster', /\broasts?|roaster\b/i],
  ['receipt/receipts', /\breceipts?\b/i],
  ['demo', /\bdemo\b/i],
  ['lab/labs', /\blabs?\b/i],
  ['standalone proof', /\bproof\b/i],
];

const allow = [
  // This standard must name banned words so agents know what not to publish.
  { file: 'PUBLIC_COPY_STANDARD.md' },
  { file: 'AGENTS.md' },

  // Legitimate technical/historical context where replacing would be wrong or break links.
  { file: '_astro-source/src/content/blog/zkp-explained.md', pattern: /zero-knowledge proof|cryptographic proof/i },
  { pattern: /TRM Labs|Borealis AI lab|research lab|labour/i },
  { pattern: /magic-trace/i },

  // Historical repo names/URLs are allowed, but visible labels should still be professionalized nearby.
  { pattern: /github\.com\/hash02\/aml-roaster|github\.com\/hash02\/agent-framework-proof/i },
  { pattern: /slug:\s*["']roast-gallery["']|href=["']\/roast-gallery\/?["']|\/blog\/roast-gallery\//i },

  // CSS/internal identifiers are tolerated when not user-facing copy.
  { pattern: /class=|className=|const\s+\w*proof\w*|const\s+\w*roast\w*|function\s+renderRoasts|\.proof-|\.roast-|#roastCards|roastCards|ROAST_URL/i },

  // Boundary wording may say the product is not licensed.
  { pattern: /Not a licensed compliance product|not a licensed compliance product/i },
];

function* walk(path) {
  const st = statSync(path, { throwIfNoEntry: false });
  if (!st) return;
  if (st.isFile()) {
    yield path;
    return;
  }
  for (const name of readdirSync(path)) {
    const child = join(path, name);
    const rel = relative(repoRoot, child);
    if (rel.split(sep).some((part) => ignoredParts.has(part))) continue;
    yield* walk(child);
  }
}

function isAllowed(file, line) {
  const rel = relative(repoRoot, file).replaceAll('\\\\', '/').replaceAll('\\', '/');
  return allow.some((entry) => {
    if (entry.file && entry.file !== rel) return false;
    if (entry.pattern && !entry.pattern.test(line)) return false;
    return true;
  });
}

function collect(patterns) {
  const hits = [];
  for (const root of scanRoots) {
    for (const file of walk(root)) {
      if (!extensions.has(extname(file)) && !file.endsWith('AGENTS.md')) continue;
      const text = readFileSync(file, 'utf8');
      const lines = text.split(/\r?\n/);
      lines.forEach((line, index) => {
        for (const [label, regex] of patterns) {
          if (regex.test(line) && !isAllowed(file, line)) {
            hits.push({ file: relative(repoRoot, file), line: index + 1, label, text: line.trim().slice(0, 240) });
          }
        }
      });
    }
  }
  return hits;
}

const hardHits = collect(hardBlockers);
const softHits = collect(softBlockers);

if (softHits.length) {
  console.log(`PUBLIC_COPY_REVIEW soft hits: ${softHits.length}`);
  for (const hit of softHits.slice(0, 80)) {
    console.log(`soft ${hit.file}:${hit.line} [${hit.label}] ${hit.text}`);
  }
  if (softHits.length > 80) console.log(`... ${softHits.length - 80} more soft hits`);
}

if (hardHits.length) {
  console.error(`PUBLIC_COPY_BLOCKERS ${hardHits.length}`);
  for (const hit of hardHits.slice(0, 120)) {
    console.error(`${hit.file}:${hit.line} [${hit.label}] ${hit.text}`);
  }
  if (hardHits.length > 120) console.error(`... ${hardHits.length - 120} more blockers`);
  process.exit(1);
}

console.log('PUBLIC_COPY_CHECK PASS');
