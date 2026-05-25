import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const repoRoot = path.resolve(root, '..');
const read = (p) => fs.readFileSync(path.join(root, p), 'utf8');
const readRoot = (p) => fs.readFileSync(path.join(repoRoot, p), 'utf8');

const failures = [];
const requireIncludes = (label, text, needle) => {
  if (!text.includes(needle)) failures.push(`${label} missing ${needle}`);
};
const requireAbsent = (label, text, needle) => {
  if (text.includes(needle)) failures.push(`${label} still contains ${needle}`);
};

const globalCss = read('public/styles/global.css');
requireIncludes('global.css', globalCss, '--surface-panel: rgba(3,16,8,0.92)');
requireIncludes('global.css', globalCss, '--surface-soft: rgba(31,160,104,0.055)');
requireIncludes('global.css', globalCss, 'linear-gradient(180deg, var(--bg) 0%, var(--bg2) 42%, var(--bg) 100%)');
requireAbsent('global.css', globalCss, '#5b73f8');
requireAbsent('global.css', globalCss, '#8b6cf7');
requireAbsent('global.css', globalCss, '#0a0a10');
requireAbsent('global.css', globalCss, '#888890');

const baseLayout = read('src/layouts/BaseLayout.astro');
requireIncludes('BaseLayout', baseLayout, "green-theme-consistent-");

const sourceFiles = [
  'src/pages/index.astro',
  'src/pages/start-here.astro',
  'src/pages/apps.astro',
  'src/pages/proof-pack.astro',
  'src/pages/about.astro',
  'src/pages/signals.astro',
  'src/pages/intelligence.astro',
  'src/pages/wallet-risk.astro',
  'src/pages/aml-status-evidence.astro',
  'src/pages/fraud-alert-triage.astro',
  'src/pages/agent-prototype-sprint.astro',
  'src/pages/risk-evidence-overview.astro',
  'src/pages/dashboard.astro',
];

for (const file of sourceFiles) {
  const text = read(file);
  requireAbsent(file, text, 'rgba(10,10,14');
  requireAbsent(file, text, '#0d0f18');
  requireAbsent(file, text, '#0e0e12');
  requireAbsent(file, text, '#0a0a10');
  requireAbsent(file, text, '#5b73f8');
  requireAbsent(file, text, '#8b6cf7');
}

const builtRoutes = [
  'index.html',
  'start-here/index.html',
  'apps/index.html',
  'proof-pack/index.html',
  'about/index.html',
  'signals/index.html',
  'ai-intelligence/index.html',
  'wallet-risk/index.html',
  'aml-status-evidence/index.html',
  'fraud-alert-triage/index.html',
  'agent-prototype-sprint/index.html',
];

for (const file of builtRoutes) {
  const text = readRoot(file);
  requireIncludes(file, text, 'green-theme-consistent-');
  requireAbsent(file, text, '#5b73f8');
  requireAbsent(file, text, '#8b6cf7');
  requireAbsent(file, text, 'rgba(10,10,14');
}

if (failures.length) {
  console.error('LAYER3_PALETTE_CONTRACT FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log('LAYER3_PALETTE_CONTRACT PASS — key routes use the green-black-white surface contract.');
