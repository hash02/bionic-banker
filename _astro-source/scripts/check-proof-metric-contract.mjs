import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve('..');
const sourceRoot = process.cwd();
const fail = (msg) => { console.error(`PROOF_METRIC_CONTRACT FAIL: ${msg}`); process.exitCode = 1; };

const read = (p) => fs.readFileSync(p, 'utf8');
const catalog = JSON.parse(read(path.join(sourceRoot, 'public/dashboard-data/public-proof-catalog.json')));
const projectsSource = read(path.join(sourceRoot, 'src/pages/projects.astro'));
const indexSource = read(path.join(sourceRoot, 'src/pages/index.astro'));
const overviewSource = read(path.join(sourceRoot, 'src/pages/risk-evidence-overview.astro'));
const blogDir = path.join(sourceRoot, 'src/content/blog');

const catalogLanes = catalog.projects.length;
const catalogSources = catalog.projects.reduce((sum, project) => sum + (project.sources?.length || 0), 0);
const catalogBoundaries = catalog.projects.reduce((sum, project) => sum + (project.limits?.length || 0), 0);
const articleCount = fs.readdirSync(blogDir).filter((name) => name.endsWith('.md')).length;
const publicCardCount = [...projectsSource.matchAll(/name:\s*'/g)].length;

if (catalogLanes !== 8) fail(`expected 8 evidence catalog lanes, found ${catalogLanes}`);
if (catalogSources !== 21) fail(`expected 21 catalog evidence sources, found ${catalogSources}`);
if (catalogBoundaries !== 36) fail(`expected 36 catalog boundaries, found ${catalogBoundaries}`);
if (articleCount !== 45) fail(`expected 45 source articles, found ${articleCount}`);
if (publicCardCount !== 11) fail(`expected 11 public system cards, found ${publicCardCount}`);

const requiredPhrases = [
  [projectsSource, 'public system cards', 'projects source public system cards label'],
  [projectsSource, 'evidence catalog lanes', 'projects source evidence catalog lanes label'],
  [projectsSource, 'catalog evidence sources', 'projects source catalog evidence sources label'],
  [projectsSource, 'catalog boundaries', 'projects source catalog boundaries label'],
  [indexSource, 'Catalog lanes', 'homepage catalog lanes label'],
  [indexSource, 'evidence catalog lanes', 'homepage evidence catalog lanes phrase'],
  [overviewSource, 'evidence catalog lanes', 'overview evidence catalog lanes phrase'],
];

for (const [text, phrase, label] of requiredPhrases) {
  if (!text.includes(phrase)) fail(`missing ${label}: ${phrase}`);
}

const forbiddenCombos = [
  [indexSource, /\{proofCount\}\s*<\/div><div class="astat-l">Systems/i, 'homepage must not label proofCount as Systems'],
  [indexSource, /system lanes/i, 'homepage must not use ambiguous system lanes'],
  [projectsSource, /system areas/i, 'projects must not use ambiguous system areas'],
  [projectsSource, /explicit boundaries/i, 'projects should use catalog boundaries'],
  [overviewSource, /\{projects\.length\}\s*systems/i, 'overview must not label catalog lanes as systems'],
];
for (const [text, pattern, label] of forbiddenCombos) {
  if (pattern.test(text)) fail(label);
}

if (!process.exitCode) {
  console.log(`PROOF_METRIC_CONTRACT PASS — ${publicCardCount} public system cards, ${catalogLanes} evidence catalog lanes, ${catalogSources} sources, ${catalogBoundaries} boundaries, ${articleCount} articles`);
}
