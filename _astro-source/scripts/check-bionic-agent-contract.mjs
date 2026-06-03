import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(process.cwd(), '..');
const astroRoot = process.cwd();
const failures = [];

function read(relFromRepo) {
  const file = path.join(root, relFromRepo);
  if (!fs.existsSync(file)) {
    failures.push(`missing ${relFromRepo}`);
    return '';
  }
  return fs.readFileSync(file, 'utf8');
}

function requireText(rel, text, patterns) {
  for (const [pattern, reason] of patterns) {
    if (!pattern.test(text)) failures.push(`${rel}: missing ${reason}`);
  }
}

function forbidText(rel, text, patterns) {
  for (const [pattern, reason] of patterns) {
    if (pattern.test(text)) failures.push(`${rel}: forbidden ${reason}`);
  }
}

const contract = read('BIONIC_BANKER_AGENT.md');
const agentTaskContract = read('agents/bionic_agent_contract.md');
const workflow = read('.github/workflows/bionic-watch.yml');
const watchTask = read('agents/tasks/watch.md');
const draftTask = read('agents/tasks/draft.md');
const publishTask = read('agents/tasks/publish.md');

requireText('BIONIC_BANKER_AGENT.md', contract, [
  [/AI finance agent/i, 'AI finance agent identity'],
  [/auditable finance-risk workflows/i, 'auditable finance-risk workflow frame'],
  [/source trail\s*->\s*checked fact\s*->\s*missing context\s*->\s*clear limit\s*->\s*human next question/i, 'epistemic loop'],
  [/Watcher, every 15 minutes/i, '15-minute watcher lane'],
  [/Scout, hourly or every 4-6 hours/i, 'scout lane'],
  [/Builder, daily/i, 'daily builder lane'],
  [/Publisher, gated/i, 'gated publisher lane'],
  [/Secret and connector policy/i, 'secret policy'],
  [/not investment advice/i, 'investment advice boundary'],
  [/not legal advice/i, 'legal advice boundary'],
  [/not tax advice/i, 'tax advice boundary'],
  [/no trade\/order authority/i, 'trade authority boundary'],
  [/no wallet power/i, 'wallet authority boundary'],
  [/Default headline frame should not be `crypto`/i, 'crypto-not-default branding rule'],
]);

requireText('agents/bionic_agent_contract.md', agentTaskContract, [
  [/watch -> scout -> draft -> verify -> queue -> gated publish -> live check -> analyst note/i, 'agent loop'],
  [/No browser automation for social media/i, 'social browser automation ban'],
  [/Missing connector handling/i, 'connector-missing posture'],
]);

requireText('agents/tasks/watch.md', watchTask, [
  [/Read-only/i, 'read-only watch task'],
  [/no deploy/i, 'no deploy watch boundary'],
  [/no social post/i, 'no social post watch boundary'],
]);

requireText('agents/tasks/draft.md', draftTask, [
  [/Website article is canonical/i, 'website-first draft rule'],
  [/queues, not posts/i, 'queue-not-post draft rule'],
]);

requireText('agents/tasks/publish.md', publishTask, [
  [/Approval requirement/i, 'approval gate'],
  [/Live URL is verified/i, 'live verification gate'],
]);

requireText('.github/workflows/bionic-watch.yml', workflow, [
  [/cron: '\*\/15 \* \* \* \*'/i, '15-minute schedule'],
  [/permissions:\s*\n\s*contents: read/i, 'read-only workflow permissions'],
  [/npm run test:bionic-agent-contract/i, 'contract check step'],
  [/node scripts\/bionic-agent-watch\.mjs --json/i, 'watcher step'],
]);

forbidText('agent contract corpus', [contract, agentTaskContract, workflow, watchTask, draftTask, publishTask].join('\n'), [
  [/BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY/i, 'private key block'],
  [/Authorization:\s*Bearer\s+[A-Za-z0-9._-]{12,}/i, 'bearer token value'],
  [/api[_-]?key\s*[:=]\s*['"][A-Za-z0-9_\-.]{16,}/i, 'API key assignment'],
  [/C:\\Users\\himan/i, 'private Windows path'],
  [/\/home\/hash\//i, 'private server path'],
  [/copy this trade/i, 'trading instruction'],
  [/guaranteed return/i, 'return guarantee'],
  [/live execution enabled/i, 'live execution authority claim'],
]);

const watcherScript = path.join(astroRoot, 'scripts', 'bionic-agent-watch.mjs');
if (!fs.existsSync(watcherScript)) failures.push('missing _astro-source/scripts/bionic-agent-watch.mjs');

if (failures.length) {
  console.error('BIONIC_AGENT_CONTRACT_CHECK FAIL');
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log('BIONIC_AGENT_CONTRACT_CHECK PASS — Bionic Banker Agent has identity, lanes, gates, secret policy, read-only watcher workflow, and public-safety boundaries.');
