import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const pagePath = path.join(root, 'src/pages/risk-evidence-overview.astro');
const sourceJsonPath = path.join(root, 'public/dashboard-data/agent-chess-status.json');
const builtJsonPath = path.join(root, '..', 'dashboard-data/agent-chess-status.json');
const builtHtmlPath = path.join(root, '..', 'risk-evidence-overview/index.html');

function assert(condition, message) {
  if (!condition) throw new Error(message);
}
function read(file) {
  assert(fs.existsSync(file), `Missing required file: ${path.relative(root, file)}`);
  return fs.readFileSync(file, 'utf8');
}

const page = read(pagePath);
const sourceJsonText = read(sourceJsonPath);
const builtJsonText = read(builtJsonPath);
const builtHtml = read(builtHtmlPath);
const data = JSON.parse(sourceJsonText);
const builtData = JSON.parse(builtJsonText);

assert(page.includes('agent-chess-status.json'), 'Risk overview must import agent-chess-status.json.');
assert(page.includes('agent-chess-showcase'), 'Risk overview must render the Agent Chess showcase section.');
assert(page.includes('Coordinated AI work with human approval'), 'Showcase must name the public orchestration flow.');
assert(page.includes('No private data policy'), 'Showcase must render the no-private-data policy.');
assert(page.includes('agentChessLanes.map'), 'Showcase lanes must be backed by JSON data.');
assert(page.includes('agentChessFlow.map'), 'Showcase flow must be backed by JSON data.');
assert(page.includes('agentChessRoles.map'), 'Showcase roles must be backed by JSON data.');

assert(data.showcase_status === 'public_safe_overview_v1', 'Agent Chess JSON must have public_safe_overview_v1 status.');
assert(Array.isArray(data.lanes) && data.lanes.length >= 4, 'Agent Chess JSON must contain at least four lanes.');
assert(Array.isArray(data.flow) && data.flow.length === 4, 'Agent Chess JSON must contain the four-step flow.');
assert(Array.isArray(data.roles) && data.roles.length >= 4, 'Agent Chess JSON must contain public roles.');
assert(Array.isArray(data.no_private_data_policy) && data.no_private_data_policy.length >= 4, 'Agent Chess JSON must contain no-private-data policy bullets.');
assert(JSON.stringify(data) === JSON.stringify(builtData), 'Source and committed dashboard-data Agent Chess JSON must match exactly.');

const requiredBuiltPhrases = [
  'Agent Chess board',
  'Coordinated AI work with human approval',
  'No private data policy',
  'Public record: Move summary',
  'Public record: Review verdict',
  'Human approval is required'
];
for (const phrase of requiredBuiltPhrases) {
  assert(builtHtml.includes(phrase), `Built risk overview is missing Agent Chess phrase: ${phrase}`);
}

const stylesheetRefs = Array.from(builtHtml.matchAll(/href="([^"]+\.css)"/g), (match) => match[1]);
for (const href of stylesheetRefs) {
  const cssPath = href.startsWith('/')
    ? path.join(root, '..', href.slice(1))
    : path.resolve(path.dirname(builtHtmlPath), href);
  assert(fs.existsSync(cssPath), `Built risk overview references missing stylesheet: ${href}`);
}

const combined = [page, sourceJsonText, builtJsonText, builtHtml].join('\n').toLowerCase();
const banned = [
  'c:/users/',
  'c:\\users\\',
  '/users/himan/',
  '100.86.',
  '100.124.',
  'private prompt',
  'system prompt',
  'wallet address',
  'seed phrase',
  'api key',
  'token=',
  'secret=',
  'may_execute: true',
  'autonomous profit',
  'live execution enabled'
];
for (const phrase of banned) {
  assert(!combined.includes(phrase), `Agent Chess public surface contains banned phrase: ${phrase}`);
}

console.log('Agent Chess showcase source checks passed.');
