import fs from 'node:fs';
import path from 'node:path';

const sourceRoot = process.cwd();
const repoRoot = path.resolve('..');
const fail = (msg) => { console.error(`HASH_WORLD_STYLE_CONTRACT FAIL: ${msg}`); process.exitCode = 1; };
const read = (p) => fs.readFileSync(p, 'utf8');

const pages = {
  home: read(path.join(sourceRoot, 'src/pages/index.astro')),
  startHere: read(path.join(sourceRoot, 'src/pages/start-here.astro')),
  fieldPack: read(path.join(sourceRoot, 'src/pages/proof-pack.astro')),
  amlStatus: read(path.join(sourceRoot, 'src/pages/aml-status-evidence.astro')),
  agentCase: read(path.join(sourceRoot, 'src/pages/agent-prototype-sprint.astro')),
  apps: read(path.join(sourceRoot, 'src/pages/apps.astro')),
  projects: read(path.join(sourceRoot, 'src/pages/projects.astro')),
  fraudTriage: read(path.join(sourceRoot, 'src/pages/fraud-alert-triage.astro')),
  riskOverview: read(path.join(sourceRoot, 'src/pages/risk-evidence-overview.astro')),
  baseLayout: read(path.join(sourceRoot, 'src/layouts/BaseLayout.astro')),
  publicCopyStandard: read(path.join(repoRoot, 'PUBLIC_COPY_STANDARD.md')),
  agents: read(path.join(repoRoot, 'AGENTS.md')),
};

const required = [
  [pages.publicCopyStandard, 'what it is, what it does, what supports it, what stays private, and what the system cannot do', 'public copy standard reader-first shape'],
  [pages.publicCopyStandard, 'World and voice anchors', 'public copy standard world anchors'],
  [pages.publicCopyStandard, 'Explanation ladder', 'public copy standard explanation ladder'],
  [pages.publicCopyStandard, 'start from the screen, move to the system, then show the check and the limit', 'screen to system explanation pattern'],
  [read(path.join(sourceRoot, 'src/pages/learn.astro')), 'The explanation pattern', 'knowledge base explanation pattern'],
  [pages.agents, 'Every public claim about numbers, rules, counts, or dates must be computed from source.', 'agent rule for computed claims'],
  [pages.startHere, 'AI-assisted finance risk workflows, mapped like missions with humans in control.', 'Start Quest thesis'],
  [pages.fieldPack, 'AI agents for finance risk. Simple records first, human control always.', 'Proof Pack thesis'],
  [pages.home, 'AI-assisted finance risk workflows', 'homepage category phrase'],
  [pages.home, 'Agents prepare. Humans decide', 'homepage human-control phrase'],
  [pages.baseLayout, 'Start Quest', 'nav start quest'],
  [pages.baseLayout, 'Proof Pack', 'nav/footer proof pack'],
];

for (const [text, phrase, label] of required) {
  if (!text.includes(phrase)) fail(`missing ${label}: ${phrase}`);
}

const visiblePublicFiles = [
  ['home', pages.home],
  ['start-here', pages.startHere],
  ['field-pack', pages.fieldPack],
  ['aml-status', pages.amlStatus],
  ['agent-case-review', pages.agentCase],
  ['apps', pages.apps],
  ['projects', pages.projects],
  ['fraud-triage', pages.fraudTriage],
  ['risk-evidence-overview', pages.riskOverview],
  ['base-layout', pages.baseLayout],
];

const staleVisiblePhrases = [
  ['Authority boundary', /Authority boundary/],
  ['Reviewer summary draft', /Reviewer summary draft/],
  ['AML Evidence label', /label:\s*'AML Evidence'/],
  ['Can approve outside action', /Can approve outside action/],
  ['human gates', /Human gates|human gates/],
  ['11 stale system cards', /\['System cards',\s*'11'/],
  ['proof page wording', /proof page/i],
  ['proof surface wording', /proof surface/i],
  ['proof route wording', /proof route/i],
  ['Open route wording', /Open route/i],
  ['Field Notes wording', /Field Notes|field notes|field note/i],
  ['Field Pack wording', /Field Pack|field pack/i],
  ['Field Map wording', /Field Map|field map/i],
  ['field packet wording', /field packet/i],
  ['surface area wording', /surface area/i],
  ['evidence catalog lanes wording', /evidence catalog lanes/i],
  ['risk evidence overview visible title', /Risk & Evidence Overview/i],
  ['evidence-first workflow wording', /Evidence-first workflow/i],
  ['evidence snapshot wording', /Evidence Snapshot/i],
  ['footer evidence link label', />Evidence<\/a>/i],
  ['visible permission checks wording', /permission checks/i],
  ['catalog evidence sources wording', /catalog evidence sources/i],
  ['visible evidence role label', /role:\s*'[^']*\/ Evidence \//i],
  ['strongest serious route wording', /strongest serious route/i],
  ['artifact provenance wording', /artifact provenance/i],
  ['human-gated wording', /human-gated/i],
  ['stale domain typo', /bionicbanker\.tech\.com/i],
  ['AML evidence public label', /AML evidence/i],
  ['permissions wording', /permissions/i],
  ['approval gates wording', /approval gates/i],
  ['human approval wording', /human approval/i],
];

for (const [name, text] of visiblePublicFiles) {
  for (const [label, pattern] of staleVisiblePhrases) {
    if (pattern.test(text)) fail(`${name} still contains stale/internal wording: ${label}`);
  }
}

if (!process.exitCode) {
  console.log('HASH_WORLD_STYLE_CONTRACT PASS — reader-first style, world anchors, current metrics, and clear-limit language are locked.');
}
