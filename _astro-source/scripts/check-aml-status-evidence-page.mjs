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

assert(page.includes('<BaseLayout title="AML Status Evidence"'), 'AML status evidence page must use BaseLayout with title "AML Status Evidence".');
assert(page.includes('aml-status-evidence-public.json'), 'AML status evidence page must import the public AML status evidence JSON catalog.');
assert(page.includes('may_execute'), 'AML status evidence page must visibly explain the may_execute boundary.');
assert(page.includes('false'), 'AML status evidence page must visibly show false execution authority.');
assert(page.includes('No KYC approval authority'), 'AML status evidence page must state the KYC boundary exactly.');
assert(page.includes('No wallet, trade, filing, or deploy authority'), 'AML status evidence page must state the execution boundary exactly.');
assert(page.includes('artifact provenance'), 'AML status evidence page must include artifact provenance wording.');

assert(layout.includes('href="/aml-status-evidence"'), 'Primary layout must expose /aml-status-evidence in navigation/mobile/footer.');
assert(projects.includes('/aml-status-evidence'), 'Systems page must link to the AML status evidence page.');
assert(proofTour.includes('/aml-status-evidence'), 'Proof tour must link to the AML status evidence page.');

assert(catalog.status === 'public_aml_status_evidence_v1', 'AML status evidence catalog status must be public_aml_status_evidence_v1.');
assert(catalog.boundary?.may_execute === false, 'Public AML status evidence catalog must keep may_execute false.');
assert(catalog.boundary?.kyc_approval_authority === false, 'Public AML status evidence catalog must keep KYC approval authority false.');
assert(catalog.boundary?.wallet_or_trade_authority === false, 'Public AML status evidence catalog must keep wallet/trade authority false.');
assert(catalog.provenance?.contract_doc?.includes('AML_LAYER1_STATUS_CONTRACT.md'), 'Catalog must point to the public-safe contract doc provenance.');
assert(Array.isArray(catalog.visible_claims) && catalog.visible_claims.length >= 4, 'Catalog must contain visible public claims.');

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
