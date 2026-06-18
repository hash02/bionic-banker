import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const pagePath = path.join(root, 'src/pages/aml-status-evidence.astro');
const layoutPath = path.join(root, 'src/layouts/BaseLayout.astro');
const projectsPath = path.join(root, 'src/pages/projects.astro');
const proofTourPath = path.join(root, 'src/pages/risk-evidence-overview.astro');
const catalogPath = path.join(root, 'public/dashboard-data/aml-status-evidence-public.json');

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function read(file) {
  assert(fs.existsSync(file), `Missing required file: ${path.relative(root, file)}`);
  return fs.readFileSync(file, 'utf8');
}

const page = read(pagePath);
const layout = read(layoutPath);
const projects = read(projectsPath);
const proofTour = read(proofTourPath);
const catalog = JSON.parse(read(catalogPath));

assert(page.includes('<BaseLayout title="AML Status"'), 'AML status page must use BaseLayout with title "AML Status".');
assert(page.includes('aml-status-evidence-public.json'), 'AML status evidence page must import the public AML status evidence JSON catalog.');
assert(page.includes('Outside action allowed') || page.includes('No outside action'), 'AML status page must explain action approval in reader-facing language.');
assert(page.includes('Outside action allowed') && page.includes('No outside action'), 'AML status page must visibly explain that outside action is not approved.');
assert(page.includes('No wallet, trade, filing, deploy, or KYC approval power'), 'AML status page must state the KYC and execution limits plainly.');
assert(page.includes('No wallet, trade, filing, deploy, or KYC approval power'), 'AML status page must state the execution limits plainly.');
assert(page.includes('source trail'), 'AML status page must include source trail wording.');

assert(!layout.includes('href="/aml-status-evidence"'), 'Primary layout must not expose /aml-status-evidence in top navigation/mobile/footer; keep it as a deep evidence route.');
assert(projects.includes('/labs/aml-engine') || projects.includes('/risk-evidence'), 'Projects page must link to a public AML proof surface.');
assert(proofTour.includes('/aml-status-evidence'), 'Proof tour must link to the AML status evidence page.');

assert(catalog.status === 'public_aml_status_record_v2', 'AML status record catalog status must be public_aml_status_record_v2.');
assert(catalog.boundary?.may_execute === false, 'Public AML status evidence catalog must keep may_execute false.');
assert(catalog.boundary?.kyc_approval_authority === false, 'Public AML status evidence catalog must keep KYC approval authority false.');
assert(catalog.boundary?.wallet_or_trade_authority === false, 'Public AML status evidence catalog must keep wallet/trade authority false.');
assert(catalog.provenance?.contract_doc === 'AML status contract summary', 'Catalog must use public-safe source summary labels instead of private paths.');
assert(Array.isArray(catalog.visible_claims) && catalog.visible_claims.length >= 4, 'Catalog must contain visible public claims.');

const publicSafeText = JSON.stringify(catalog);
for (const phrase of ['console-api/', 'wukong-side', 'console/src/pages', '70-ops-logs', 'python -m', 'py_compile', 'artifact path']) {
  assert(!publicSafeText.toLowerCase().includes(phrase.toLowerCase()), `Public AML status record exposes private implementation detail: ${phrase}`);
}

const combined = [page, JSON.stringify(catalog)].join('\n').toLowerCase();
const banned = [
  'kyc approved',
  'approved kyc',
  'may execute: true',
  'may_execute: true',
  '"may_execute":true',
  'wallet authority: true',
  'trade authority: true',
  'filing authority: true',
  'licensed compliance product',
  'uses client data',
  'uses employer data',
  'c:/users/',
  '/users/himan/',
];
for (const phrase of banned) {
  assert(!combined.includes(phrase), `Public AML status evidence content contains banned phrase: ${phrase}`);
}

console.log('AML status evidence page source checks passed.');
