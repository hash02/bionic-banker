import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const failures = [];

function read(rel) {
  const file = path.join(root, rel);
  if (!fs.existsSync(file)) {
    failures.push(`missing expected file: ${rel}`);
    return '';
  }
  return fs.readFileSync(file, 'utf8');
}

function walk(dir, matcher = () => true) {
  const out = [];
  if (!fs.existsSync(dir)) return out;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) out.push(...walk(full, matcher));
    else if (matcher(full)) out.push(full);
  }
  return out;
}

function checkNo(rel, text, checks) {
  for (const [pattern, reason] of checks) {
    if (pattern.test(text)) failures.push(`${rel}: ${reason}`);
  }
}

const publicCodeChecks = [
  [/```python/i, 'raw Python fenced code block is public; summarize the control pattern instead'],
  [/from\s+flask\s+import/i, 'Flask/proxy implementation details are public'],
  [/app\.route\(/i, 'HTTP route implementation details are public'],
  [/subprocess\.(run|Popen)/i, 'subprocess adapter implementation is public'],
  [/http:\/\/localhost:\d+/i, 'local endpoint is public'],
  [/\bwhile\s+True:/i, 'raw long-running loop code is public'],
  [/def\s+chat_completions\s*\(/i, 'raw proxy function is public'],
  [/GROQ_API_KEY/i, 'credential environment variable name is public in reader content'],
  [/constrained system prompt/i, 'private prompt plumbing is public in reader content'],
  [/Extract system prompt/i, 'prompt extraction implementation is public'],
  [/brain\.py/i, 'private source filename is public in reader content'],
  [/decisions\s*=\s*think\(/i, 'raw decision pseudocode is public'],
];

for (const file of walk(path.join(root, 'src/content/blog'), (f) => f.endsWith('.md'))) {
  const rel = path.relative(root, file).replaceAll('\\', '/');
  checkNo(rel, fs.readFileSync(file, 'utf8'), publicCodeChecks);
}

for (const file of walk(path.join(root, 'public/blog-visuals'), (f) => f.endsWith('.html'))) {
  const rel = path.relative(root, file).replaceAll('\\', '/');
  checkNo(rel, fs.readFileSync(file, 'utf8'), publicCodeChecks);
}

const aml = JSON.parse(read('public/dashboard-data/aml-status-evidence-public.json'));
if (aml.status !== 'public_aml_status_record_v2') failures.push('AML public status record must use public_aml_status_record_v2');
const amlText = JSON.stringify(aml);
checkNo('public/dashboard-data/aml-status-evidence-public.json', amlText, [
  [/console-api\//i, 'private repo module path is public'],
  [/wukong-side/i, 'private machine/module name is public'],
  [/console\/src\/pages/i, 'private UI source path is public'],
  [/70-ops-logs/i, 'private operations-log path is public'],
  [/python\s+-m/i, 'raw local test command is public'],
  [/py_compile/i, 'raw compile command is public'],
  [/local artifact path/i, 'raw local artifact-path language is public'],
]);

for (const rel of [
  'src/pages/apps.astro',
  'src/pages/projects.astro',
  'src/pages/evidence.astro',
  'src/pages/reports.astro',
  'src/pages/intelligence.astro',
  'src/pages/aml-status-evidence.astro',
  'src/pages/risk-evidence-overview.astro',
  'public/dashboard-data/source-catalog.json',
  'public/dashboard-data/public-proof-catalog.json',
]) {
  const text = read(rel);
  checkNo(rel, text, [
    [/View source catalog JSON/i, 'reader CTA points to raw source catalog JSON'],
    [/Open notebook data/i, 'reader CTA points to raw notebook JSON'],
    [/Heartbeat data/i, 'reader CTA points to raw heartbeat JSON'],
    [/Source JSON/i, 'reader CTA exposes raw JSON as a primary proof link'],
    [/open snapshot\s*->/i, 'reader CTA opens raw heartbeat snapshot'],
    [/2,514 predictions made/i, 'stale prediction count is public'],
    [/53 percent accuracy/i, 'stale accuracy metric is public'],
    [/route:\s*['"]\/dashboard-data\/[^'"]+\.json['"]/i, 'reader route points directly to raw dashboard JSON'],
  ]);
}

const allPublicText = [
  ...walk(path.join(root, 'src/pages'), (f) => f.endsWith('.astro')),
  ...walk(path.join(root, 'src/content/blog'), (f) => f.endsWith('.md')),
  ...walk(path.join(root, 'public/dashboard-data'), (f) => f.endsWith('.json')),
].map((file) => fs.readFileSync(file, 'utf8')).join('\n');
checkNo('public source corpus', allPublicText, [
  [/C:\\Users\\himan/i, 'local Windows user path is public'],
  [/\/Users\/himan/i, 'local macOS/Linux user path is public'],
  [/PRIVATE_KEY\s*=/i, 'private key assignment is public'],
  [/BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY/i, 'private key block is public'],
  [/Authorization:\s*Bearer\s+[A-Za-z0-9._-]{12,}/i, 'bearer token is public'],
]);

if (failures.length) {
  console.error('PUBLIC_SAFETY_LEAK_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log('PUBLIC_SAFETY_LEAK_CHECK PASS — raw code, private paths, stale raw-JSON CTAs, and public leak patterns are blocked.');
