import assert from 'node:assert/strict';
import { spawn } from 'node:child_process';
import { createServer } from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import test from 'node:test';

const cwd = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');

async function runWatcher(handler) {
  const server = createServer(handler);
  await new Promise((resolve) => server.listen(0, '127.0.0.1', resolve));
  try {
    return await new Promise((resolve, reject) => {
      const child = spawn(process.execPath, ['scripts/bionic-agent-watch.mjs', '--json'], {
        cwd,
        env: { ...process.env, BIONIC_BASE_URL: 'http://127.0.0.1:' + server.address().port },
      });
      let stdout = '';
      let stderr = '';
      const timer = setTimeout(() => { child.kill(); reject(new Error('watcher did not finish')); }, 5000);
      child.stdout.on('data', (chunk) => { stdout += chunk; });
      child.stderr.on('data', (chunk) => { stderr += chunk; });
      child.on('error', reject);
      child.on('close', (code) => {
        clearTimeout(timer);
        try { resolve({ code, report: JSON.parse(stdout) }); }
        catch (error) { reject(new Error(stderr || error.message)); }
      });
    });
  } finally {
    server.closeAllConnections();
    await new Promise((resolve) => server.close(resolve));
  }
}

test('identifies the site-owned health checker and requests HTML', async () => {
  const result = await runWatcher((req, res) => {
    const identified = req.headers['user-agent'] === 'BionicBankerHealth/1.0 (+https://bionicbanker.tech)'
      && req.headers.accept?.includes('text/html');
    res.writeHead(identified ? 200 : 403, { 'content-type': 'text/html' });
    res.end('<html><body>Site</body></html>');
  });
  assert.equal(result.code, 0);
  assert.equal(result.report.status, 'green');
});

test('a successful HTTP response with non-HTML content fails the watcher', async () => {
  const result = await runWatcher((_req, res) => {
    res.writeHead(200, { 'content-type': 'application/json' });
    res.end('{"status":"not-a-page"}');
  });
  assert.equal(result.report.status, 'amber');
  assert.equal(result.code, 1);
});

test('edge challenges stay failed and are identified separately from outages', async () => {
  const result = await runWatcher((_req, res) => {
    res.writeHead(403, { 'content-type': 'text/html', 'cf-mitigated': 'challenge' });
    res.end('<html><title>Just a moment...</title></html>');
  });
  assert.equal(result.code, 1);
  assert.ok(result.report.checkedFacts.routes.every((route) => route.error === 'access_challenge'));
});

test('an HTTP server failure cannot pass as healthy', async () => {
  const result = await runWatcher((_req, res) => {
    res.writeHead(503, { 'content-type': 'text/html' });
    res.end('<html>Unavailable</html>');
  });
  assert.equal(result.code, 1);
  assert.equal(result.report.status, 'amber');
});

