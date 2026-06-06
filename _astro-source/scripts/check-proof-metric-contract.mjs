import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve('..');
const sourceRoot = process.cwd();
const fail = (msg) => { console.error(`METRIC_CONTRACT FAIL: ${msg}`); process.exitCode = 1; };

const read = (p) => fs.readFileSync(p, 'utf8');
const catalog = JSON.parse(read(path.join(sourceRoot, 'public/dashboard-data/public-proof-catalog.json')));
const projectsSource = read(path.join(sourceRoot, 'src/pages/projects.astro'));
const indexSource = read(path.join(sourceRoot, 'src/pages/index.astro'));
const overviewSource = read(path.join(sourceRoot, 'src/pages/risk-evidence-overview.astro'));
const blogDir = path.join(sourceRoot, 'src/content/blog');

const catalogSections = catalog.projects.length;
const catalogSources = catalog.projects.reduce((sum, project) => sum + (project.sources?.length || 0), 0);
const catalogLimits = catalog.projects.reduce((sum, project) => sum + (project.limits?.length || 0), 0);
const articleCount = fs.readdirSync(blogDir).filter((name) => name.endsWith('.md')).length;
const publicCardCount = [...projectsSource.matchAll(/name:\s*'/g)].length;

if (catalogSections !== 8) fail(`expected 8 catalog records, found ${catalogSections}`);
if (catalogSources !== 21) fail(`expected 21 catalog sources, found ${catalogSources}`);
if (catalogLimits !== 36) fail(`expected 36 catalog limits, found ${catalogLimits}`);
if (articleCount !== 52) fail(`expected 52 source articles, found ${articleCount}`);
if (publicCardCount !== 13) fail(`expected 13 systems, found ${publicCardCount}`);

const requiredPhrases = [
  [projectsSource, 'systems', 'projects source systems label'],
  [projectsSource, 'catalog source trails', 'projects source catalog source trails label'],
  [projectsSource, 'catalog limits', 'projects source catalog limits label'],
  [indexSource, 'Reader sections', 'homepage reader sections label'],
];

for (const [text, phrase, label] of requiredPhrases) {
  if (!text.includes(phrase)) fail(`missing ${label}: ${phrase}`);
}

const forbiddenCombos = [
  [indexSource, /\{proofCount\}\s*<\/div><div class="astat-l">Systems/i, 'homepage must not label proofCount as Systems'],
  [indexSource, /system sections/i, 'homepage must not use ambiguous system sections'],
  [projectsSource, /system areas/i, 'projects must not use ambiguous system areas'],
  [projectsSource, /explicit boundaries/i, 'projects should use catalog limits'],
  [overviewSource, /\{projects\.length\}\s*systems/i, 'overview must not label catalog records as systems'],
  [indexSource, /snapshotPriceStr|last_prediction|price_now|data-live-price|CoinGecko|Live · CoinGecko|BTC · \$|\$75,483/i, 'homepage must not render live-looking or stale BTC price literals'],
];
for (const [text, pattern, label] of forbiddenCombos) {
  if (pattern.test(text)) fail(label);
}

if (!process.exitCode) {
  console.log(`METRIC_CONTRACT PASS — ${publicCardCount} systems, ${catalogSections} catalog records, ${catalogSources} sources, ${catalogLimits} limits, ${articleCount} articles`);
}
