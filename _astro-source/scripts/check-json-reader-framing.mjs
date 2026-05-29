import fs from 'node:fs';
import path from 'node:path';

const sourceRoot = process.cwd();
const root = path.resolve('..');
const sourceFiles = [
  'src/pages/index.astro',
  'src/pages/projects.astro',
  'src/pages/apps.astro',
  'src/pages/evidence.astro',
  'src/pages/intelligence.astro',
  'src/pages/aml-status-evidence.astro',
  'src/pages/risk-evidence-overview.astro',
  'src/pages/reports.astro',
  'src/pages/fraud-alert-triage.astro',
].map((p) => path.join(sourceRoot, p)).filter(fs.existsSync);

const allowedPrimary = new Set([
  '/dashboard-data/aml-status-proof.json',
]);
const failures = [];

for (const file of sourceFiles) {
  const text = fs.readFileSync(file, 'utf8');

  for (const match of text.matchAll(/route:\s*['"]([^'"]+\.json)['"]/g)) {
    const url = match[1];
    if (url.includes('/dashboard-data/') && !allowedPrimary.has(url)) {
      failures.push(`${path.relative(sourceRoot, file)} uses raw JSON as a reader route: ${url}; point readers to a rendered page.`);
    }
  }

  for (const match of text.matchAll(/\{\s*label:\s*['"]([^'"]+)['"]\s*,\s*url:\s*['"]([^'"]+\.json)['"]/g)) {
    const label = match[1];
    const url = match[2];
    const lower = label.toLowerCase();
    if (allowedPrimary.has(url)) continue;
    if (/evidence records|public catalog|proof catalog|catalog/i.test(label)) {
      failures.push(`${path.relative(sourceRoot, file)} uses raw JSON as primary '${label}' link: ${url}; point primary readers to /evidence/ and reserve JSON for Raw JSON links.`);
    }
    if (!/raw json|json|heartbeat|status/i.test(lower) && url.includes('/dashboard-data/')) {
      failures.push(`${path.relative(sourceRoot, file)} has reader-facing label '${label}' for raw data URL ${url}`);
    }
  }
}

const evidencePage = path.join(sourceRoot, 'src/pages/evidence.astro');
if (!fs.existsSync(evidencePage)) failures.push('missing rendered /evidence page for public proof catalog');
const healthPage = path.join(sourceRoot, 'src/pages/proof/site-health.astro');
if (!fs.existsSync(healthPage)) failures.push('missing rendered /proof/site-health page for QA status');

if (failures.length) {
  console.error('JSON_READER_FRAMING FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}
console.log('JSON_READER_FRAMING PASS — rendered pages are primary and raw JSON is not a first-reader proof link');
