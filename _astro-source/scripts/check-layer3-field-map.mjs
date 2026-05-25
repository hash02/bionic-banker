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
  ['layout', 'Start Quest'],
  ['layout', '/apps'],
  ['layout', '/signals'],
  ['layout', '/ai-intelligence'],
  ['layout', 'Blog'],
  ['home', 'AI, finance, and the world ahead.'],
  ['home', 'Bionic Banker follows how technology is changing money, risk, work, and the systems people trust.'],
  ['apps', 'Apps you can enter'],
  ['apps', 'bionicbanker.tech.com'],
  ['apps', 'The strongest serious route is Wallet Risk'],
  ['signals', '<h1 class="page-title">Signals</h1>'],
  ['signals', 'It is a research board, not a trading board.'],
  ['signals', 'Signals are prompts for judgment'],
  ['ai', 'What Her is watching'],
  ['ai', 'How Hash and Her watch the AI world'],
  ['ai', 'outside-world signal becomes a question'],
  ['css', '--bg:   #020403'],
  ['css', '--text:   #f4fff7'],
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

const bannedMainNav = ['Knowledge Base', 'Systems</a>', 'Risk Signals</a>', 'Articles</a>'];
for (const phrase of bannedMainNav) {
  if (files.layout.includes(phrase)) failures.push(`layout still exposes old main nav label: ${phrase}`);
}

if (failures.length) {
  console.error('LAYER3_FIELD_MAP_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}
console.log('LAYER3_FIELD_MAP_CHECK PASS');
