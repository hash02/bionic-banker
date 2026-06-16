import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const fail = [];

const read = (p) => fs.readFileSync(path.join(root, p), 'utf8');

const layout = read('src/layouts/BaseLayout.astro');
const index = read('src/pages/index.astro');
const aiModels = read('src/pages/ai-models.astro');
const articles = read('src/pages/articles.astro');
const projects = read('src/pages/projects.astro');
const aiIntel = read('src/pages/ai-intelligence.astro');
const robots = read('public/robots.txt');

const allowedNav = ['Blog', 'AI Models', 'AI Intelligence', 'Projects', 'About'];
const forbiddenNav = ['Risk', 'Signals', 'Labs', 'AI Governance', 'Start Here', 'News', 'Reports', 'System Map', 'Dashboard'];

const navBlock = layout.match(/<ul class="nav-links">([\s\S]*?)<\/ul>/)?.[1] || '';
for (const item of allowedNav) {
  if (!navBlock.includes(`>${item}</a>`)) fail.push(`missing required nav item: ${item}`);
}
for (const item of forbiddenNav) {
  if (navBlock.includes(`>${item}</a>`)) fail.push(`forbidden top-nav item exposed: ${item}`);
}

const footerExplore = layout.match(/<h4>Explore<\/h4>([\s\S]*?)<\/div>/)?.[1] || '';
for (const item of forbiddenNav) {
  if (footerExplore.includes(`>${item}</a>`)) fail.push(`forbidden footer item exposed: ${item}`);
}

const mobilePanel = layout.match(/panel\.innerHTML =([\s\S]*?);\n    document\.body\.appendChild\(panel\)/)?.[1] || '';
for (const item of forbiddenNav) {
  if (mobilePanel.includes(`>${item}</a>`)) fail.push(`forbidden mobile menu item exposed: ${item}`);
}
for (const item of allowedNav) {
  if (!mobilePanel.includes(`>${item}</a>`)) fail.push(`missing mobile menu item: ${item}`);
}

const publicEntryFiles = {
  'src/pages/index.astro': index,
  'src/pages/articles.astro': articles,
  'src/pages/ai-models.astro': aiModels,
  'src/pages/projects.astro': projects,
  'src/pages/ai-intelligence.astro': aiIntel,
};

const leakPatterns = [
  /revenue flywheel/i,
  /traffic and products/i,
  /planned pages/i,
  /comparison queue/i,
  /article discipline/i,
  /reading routes/i,
  /system-first starting points/i,
  /source-review queue/i,
  /open loops/i,
  /heartbeat/i,
  /Wukong/i,
  /Hermes/i,
  /local paths?/i,
  /raw commands?/i,
  /private prompts?/i,
  /internal automation/i,
  /operating rule/i,
  /visual roadmap/i,
  /Pancake/i,
];

for (const [file, text] of Object.entries(publicEntryFiles)) {
  for (const pattern of leakPatterns) {
    if (pattern.test(text)) fail.push(`${file} contains public/internal leak phrase: ${pattern}`);
  }
}

if (!index.includes('4</strong><span>clear paths</span>')) {
  fail.push('homepage must say exactly 4 clear paths');
}

const hiddenRoutes = [
  '/signals/', '/risk-evidence/', '/risk-evidence-overview/', '/ai-governance/', '/reports/',
  '/system-map/', '/start-here/', '/apps/', '/intelligence/', '/dashboard/', '/proof/',
  '/evidence/', '/gaps/', '/investigate/', '/learn/', '/world-map/', '/updates/'
];
for (const route of hiddenRoutes) {
  if (!robots.includes(`Disallow: ${route}`)) fail.push(`robots.txt must disallow hidden route: ${route}`);
}
if (robots.includes('Disallow: /ai-intelligence/')) {
  fail.push('robots.txt must allow /ai-intelligence/');
}
if (layout.includes("'/ai-intelligence/'") && layout.match(/hiddenPublicRoutes[\s\S]*'\/ai-intelligence\/'/)) {
  fail.push('/ai-intelligence/ must not be in hiddenPublicRoutes/noindex list');
}

if (fail.length) {
  console.error('PUBLIC_SIMPLICITY_CONTRACT_FAIL');
  for (const item of fail) console.error(`- ${item}`);
  process.exit(1);
}

console.log('PUBLIC_SIMPLICITY_CONTRACT_PASS');
console.log(`nav=${allowedNav.join(' | ')}`);
console.log('hidden_routes_guarded=' + hiddenRoutes.length);
