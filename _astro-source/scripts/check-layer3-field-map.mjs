import { readFileSync } from 'node:fs';
import { join } from 'node:path';

const root = process.cwd();
const read = (p) => readFileSync(join(root, p), 'utf8');
const files = {
  layout: read('src/layouts/BaseLayout.astro'),
  home: read('src/pages/index.astro'),
  apps: read('src/pages/apps.astro'),
  signals: read('src/pages/signals.astro'),
  ai: read('src/pages/ai-intelligence.astro'),
  css: read('public/styles/global.css'),
};

const required = [
  ['layout', 'Start Here'],
  ['layout', '/apps'],
  ['layout', '/signals'],
  ['layout', '/ai-intelligence'],
  ['layout', 'Articles'],
  ['home', 'AI, finance, and the world ahead.'],
  ['home', 'Auditable AI workflows for finance risk.'],
  ['home', 'Bionic Banker shows how wallet risk, AML status, and fraud-triage systems turn signals into source trails, rationale, limitations, and human review decisions.'],
  ['home', 'Example: wallet row, risk score, rationale, limitation, human decision.'],
  ['apps', 'Apps you can enter'],
  ['apps', 'bionicbanker.tech'],
  ['apps', 'The clearest path is Wallet Risk'],
  ['apps', 'Agent Workflow Case Review'],
  ['apps', '/agent-prototype-sprint'],
  ['signals', '<h1 class="page-title">Signals are records for questions</h1>'],
  ['signals', 'source trails, review questions, and clear limits'],
  ['signals', 'Signals are prompts for judgment'],
  ['ai', 'What Bionic Banker is tracking'],
  ['ai', 'How the research loop works'],
  ['ai', 'outside-world signal becomes a question'],
  ['css', '--bg:   #010302'],
  ['css', '--text:   #f7fff9'],
  ['css', '#particle-canvas'],
  ['css', 'background: transparent !important'],
  ['css', 'opacity: 0.28'],
  ['layout', 'body,html{background:#010302}canvas{background:transparent}'],
];

const failures = [];
for (const [file, phrase] of required) {
  if (!files[file].includes(phrase)) failures.push(`${file} missing ${phrase}`);
}

const shellFiles = ['layout', 'home', 'apps', 'signals', 'ai'];
for (const file of shellFiles) {
  const text = files[file];
  if (/[—–]/.test(text)) failures.push(`${file} contains long dash glyph`);
  if (/\s->\s/.test(text)) failures.push(`${file} contains visible arrow glyph`);
}

const bannedMainNav = ['Knowledge Base', 'Start Quest</a>', 'Blog</a>'];
for (const phrase of bannedMainNav) {
  if (files.layout.includes(phrase)) failures.push(`layout still exposes old main nav label: ${phrase}`);
}

if (failures.length) {
  console.error('LAYER3_FIELD_MAP_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}
console.log('LAYER3_FIELD_MAP_CHECK PASS');
