import { createServer } from 'node:http';
import { createReadStream, existsSync, mkdirSync, rmSync, writeFileSync } from 'node:fs';
import { extname, join, normalize, relative, resolve } from 'node:path';
import { chromium } from 'playwright';

const args = new Map();
for (let i = 2; i < process.argv.length; i += 1) {
  const arg = process.argv[i];
  if (arg.startsWith('--')) {
    args.set(arg.slice(2), process.argv[i + 1] && !process.argv[i + 1].startsWith('--') ? process.argv[++i] : 'true');
  }
}

const sourceRoot = process.cwd();
const siteRoot = resolve(sourceRoot, args.get('site') || 'dist');
const reportRoot = resolve(sourceRoot, '..', 'qa-reports', 'latest');
const screenshotRoot = join(reportRoot, 'screenshots');

const routes = [
  { path: '/', name: 'home', requiredText: ['Bionic Banker', 'Start Quest', 'Signals', 'Apps'] },
  { path: '/risk-evidence-overview/', name: 'risk-evidence-overview', requiredText: ['Risk Review Overview', 'Wallet Risk', 'Agent Chess'] },
  { path: '/signals/', name: 'signals', requiredText: ['Signals', 'not trading performance'] },
  { path: '/apps/', name: 'apps', requiredText: ['Apps you can enter', 'Wallet Risk Assessment'] },
  { path: '/ai-intelligence/', name: 'ai-intelligence', requiredText: ['AI Intelligence', 'What Agent Her is watching'] },
  { path: '/aml-status-evidence/', name: 'aml-status-evidence', requiredText: ['AML', 'Evidence'] },
];

const viewports = [
  { name: 'mobile-390', width: 390, height: 844 },
  { name: 'mobile-360', width: 360, height: 740 },
  { name: 'tablet-768', width: 768, height: 1024 },
];

const mime = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.ico': 'image/x-icon',
  '.xml': 'application/xml; charset=utf-8',
};

function assertSiteRoot() {
  if (!existsSync(siteRoot)) {
    throw new Error(`Missing site root: ${siteRoot}. Run npm run build first or pass --site <dir>.`);
  }
  if (!existsSync(join(siteRoot, 'index.html'))) {
    throw new Error(`Site root does not contain index.html: ${siteRoot}`);
  }
}

function cleanReportRoot() {
  rmSync(reportRoot, { recursive: true, force: true });
  mkdirSync(screenshotRoot, { recursive: true });
}

function serveStatic(root) {
  const server = createServer((req, res) => {
    try {
      const url = new URL(req.url || '/', 'http://127.0.0.1');
      let pathname = decodeURIComponent(url.pathname);
      if (pathname.endsWith('/')) pathname += 'index.html';
      let file = normalize(join(root, pathname));
      if (!file.startsWith(normalize(root))) {
        res.writeHead(403).end('Forbidden');
        return;
      }
      if (!existsSync(file)) {
        const htmlFallback = join(root, pathname, 'index.html');
        if (existsSync(htmlFallback)) file = htmlFallback;
      }
      if (!existsSync(file)) {
        res.writeHead(404).end('Not found');
        return;
      }
      res.writeHead(200, { 'content-type': mime[extname(file).toLowerCase()] || 'application/octet-stream' });
      createReadStream(file).pipe(res);
    } catch (error) {
      res.writeHead(500).end(String(error?.stack || error));
    }
  });
  return new Promise((resolveListen) => {
    server.listen(0, '127.0.0.1', () => {
      const address = server.address();
      resolveListen({ server, baseUrl: `http://127.0.0.1:${address.port}` });
    });
  });
}

async function inspectPage(page, route, viewport) {
  const failures = [];
  const warnings = [];

  const bodyText = await page.locator('body').innerText().catch(() => '');
  for (const text of route.requiredText) {
    if (!bodyText.toLowerCase().includes(text.toLowerCase())) failures.push(`Required page text missing: ${text}`);
  }

  const metrics = await page.evaluate(() => {
    const doc = document.documentElement;
    const body = document.body;
    const h1 = document.querySelector('main h1, h1');
    const main = document.querySelector('main');
    const header = document.querySelector('header, nav');
    const all = Array.from(document.querySelectorAll('body *'));
    const viewportWidth = window.innerWidth;
    const overflowing = all
      .map((el) => {
        const rect = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        return {
          tag: el.tagName.toLowerCase(),
          cls: String(el.className || '').slice(0, 90),
          text: String(el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 80),
          left: Math.round(rect.left),
          right: Math.round(rect.right),
          width: Math.round(rect.width),
          display: style.display,
          visible: rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' && style.display !== 'none',
        };
      })
      .filter((item) => item.visible && (item.left < -3 || item.right > viewportWidth + 3))
      .slice(0, 8);

    const targetSelectors = [
      'header a',
      'nav a',
      '.hero-mobile-route-strip a',
      '.route-links a',
      '.scene-next a',
      '.tour-tab',
      '.mobile-menu a',
      '.mobile-nav a',
      'button[aria-label]',
    ];
    const tapTargets = Array.from(document.querySelectorAll(targetSelectors.join(',')))
      .filter((el) => {
        const rect = el.getBoundingClientRect();
        const style = window.getComputedStyle(el);
        return rect.width > 0 && rect.height > 0 && style.visibility !== 'hidden' && style.display !== 'none';
      })
      .map((el) => {
        const rect = el.getBoundingClientRect();
        return {
          tag: el.tagName.toLowerCase(),
          cls: String(el.className || '').slice(0, 90),
          text: String(el.textContent || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
          width: Math.round(rect.width),
          height: Math.round(rect.height),
        };
      })
      .filter((item) => item.width < 40 || item.height < 40)
      .slice(0, 10);

    const tourTabs = Array.from(document.querySelectorAll('.tour-tab')).map((tab) => {
      const rect = tab.getBoundingClientRect();
      const style = window.getComputedStyle(tab);
      return {
        text: String(tab.textContent || '').trim().replace(/\s+/g, ' '),
        display: style.display,
        gap: style.gap,
        height: Math.round(rect.height),
        width: Math.round(rect.width),
      };
    });

    const status = document.querySelector('.tour-status');
    const statusRect = status?.getBoundingClientRect();
    const headerRect = header?.getBoundingClientRect();
    const mainRect = main?.getBoundingClientRect();
    const h1Rect = h1?.getBoundingClientRect();

    return {
      scrollWidth: doc.scrollWidth,
      clientWidth: doc.clientWidth,
      bodyScrollWidth: body.scrollWidth,
      h1Top: h1Rect ? Math.round(h1Rect.top) : null,
      h1Bottom: h1Rect ? Math.round(h1Rect.bottom) : null,
      mainTop: mainRect ? Math.round(mainRect.top) : null,
      headerBottom: headerRect ? Math.round(headerRect.bottom) : null,
      statusTop: statusRect ? Math.round(statusRect.top) : null,
      statusBottom: statusRect ? Math.round(statusRect.bottom) : null,
      overflowing,
      tapTargets,
      tourTabs,
    };
  });

  if (metrics.scrollWidth > metrics.clientWidth + 4 || metrics.bodyScrollWidth > metrics.clientWidth + 4) {
    failures.push(`Horizontal overflow: document ${metrics.scrollWidth}px / body ${metrics.bodyScrollWidth}px exceeds viewport ${metrics.clientWidth}px`);
  }
  if ((metrics.scrollWidth > metrics.clientWidth + 4 || metrics.bodyScrollWidth > metrics.clientWidth + 4) && metrics.overflowing.length) {
    failures.push(`Visible elements overflow viewport: ${metrics.overflowing.map((item) => `${item.tag}.${item.cls || '-'} right=${item.right} text="${item.text}"`).join(' | ')}`);
  }
  if (metrics.headerBottom !== null && metrics.mainTop !== null && metrics.mainTop < metrics.headerBottom - 2) {
    failures.push(`Header overlaps main content: main top ${metrics.mainTop}px is above header bottom ${metrics.headerBottom}px`);
  }
  if (metrics.h1Top !== null && metrics.h1Top < 0) {
    failures.push(`Main heading starts above viewport: h1 top ${metrics.h1Top}px`);
  }
  if (metrics.statusTop !== null && metrics.statusTop < 0) {
    failures.push(`Tour status chips are clipped above viewport: top ${metrics.statusTop}px`);
  }
  if (viewport.width <= 390 && metrics.tapTargets.length) {
    failures.push(`Small mobile tap targets: ${metrics.tapTargets.map((item) => `${item.tag}.${item.cls || '-'} ${item.width}x${item.height} "${item.text}"`).join(' | ')}`);
  }

  if (route.name === 'risk-evidence-overview' && viewport.width <= 390) {
    for (const tab of metrics.tourTabs) {
      const gap = Number.parseFloat(tab.gap);
      if (tab.display.includes('flex') && (!Number.isFinite(gap) || gap < 8)) {
        failures.push(`Risk overview tour tab has cramped number/label spacing: gap=${tab.gap || '0'} text="${tab.text}"`);
        break;
      }
      if (tab.height < 44) {
        failures.push(`Risk overview tour tab below 44px mobile target: ${tab.height}px text="${tab.text}"`);
        break;
      }
    }
  }

  if (metrics.tapTargets.length > 0 && viewport.width >= 768) {
    warnings.push('Tap-target issue observed at tablet size; likely design should still be reviewed.');
  }

  return { failures, warnings, metrics };
}

function safeName(route, viewport) {
  return `${route.name}-${viewport.name}.png`;
}

function writeReport(results, baseUrl) {
  const failed = results.filter((result) => result.failures.length > 0);
  const lines = [];
  lines.push('# Bionic Banker Mobile QA Report');
  lines.push('');
  lines.push(`Generated: ${new Date().toISOString()}`);
  lines.push(`Site root: \`${relative(resolve(sourceRoot, '..'), siteRoot)}\``);
  lines.push(`Local URL: \`${baseUrl}\``);
  lines.push(`Status: **${failed.length ? 'FAIL' : 'PASS'}**`);
  lines.push('');
  lines.push('## Scope');
  lines.push('');
  lines.push('- Mobile/tablet viewport screenshots for public evidence routes.');
  lines.push('- Deterministic checks for horizontal overflow, clipped hero/status content, cramped route controls, tap target size, and required public route text.');
  lines.push('- This is a local QA scout: it reports and blocks; it does not publish or approve its own fixes.');
  lines.push('');
  lines.push('## Results');
  lines.push('');
  for (const result of results) {
    lines.push(`### ${result.route.path} — ${result.viewport.name}`);
    lines.push('');
    lines.push(`- Screenshot: \`screenshots/${result.screenshot}\``);
    lines.push(`- Status: **${result.failures.length ? 'FAIL' : 'PASS'}**`);
    if (result.failures.length) {
      for (const failure of result.failures) lines.push(`- Failure: ${failure}`);
    }
    if (result.warnings.length) {
      for (const warning of result.warnings) lines.push(`- Warning: ${warning}`);
    }
    lines.push('');
  }
  writeFileSync(join(reportRoot, 'report.md'), `${lines.join('\n')}\n`);
  writeFileSync(join(reportRoot, 'report.json'), JSON.stringify({ generatedAt: new Date().toISOString(), status: failed.length ? 'FAIL' : 'PASS', siteRoot, baseUrl, results }, null, 2));
}

async function main() {
  assertSiteRoot();
  cleanReportRoot();
  const { server, baseUrl } = await serveStatic(siteRoot);
  const results = [];
  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    for (const viewport of viewports) {
      const context = await browser.newContext({ viewport, deviceScaleFactor: 1, isMobile: viewport.width < 768 });
      for (const route of routes) {
        const page = await context.newPage();
        await page.route('**/*', (routeRequest) => {
          const requestUrl = routeRequest.request().url();
          if (requestUrl.startsWith(baseUrl)) return routeRequest.continue();
          return routeRequest.abort();
        });
        const pageErrors = [];
        const consoleErrors = [];
        page.on('pageerror', (error) => pageErrors.push(error.message));
        page.on('console', (message) => {
          if (['error'].includes(message.type())) consoleErrors.push(message.text());
        });
        const response = await page.goto(`${baseUrl}${route.path}`, { waitUntil: 'domcontentloaded', timeout: 15000 });
        await page.waitForLoadState('load', { timeout: 15000 }).catch(() => {});
        await page.waitForTimeout(250);
        const failures = [];
        const warnings = [];
        if (!response || response.status() >= 400) failures.push(`HTTP status ${response?.status() || 'missing response'}`);
        const inspection = await inspectPage(page, route, viewport);
        failures.push(...inspection.failures);
        warnings.push(...inspection.warnings);
        const actionableConsoleErrors = consoleErrors.filter((message) => !/Failed to load resource: net::ERR_FAILED/i.test(message));
        if (pageErrors.length) failures.push(`Page errors: ${pageErrors.join(' | ')}`);
        if (actionableConsoleErrors.length) failures.push(`Console errors: ${actionableConsoleErrors.join(' | ')}`);
        const screenshot = safeName(route, viewport);
        await page.screenshot({ path: join(screenshotRoot, screenshot), fullPage: true });
        results.push({ route, viewport, screenshot, failures, warnings, metrics: inspection.metrics });
        await page.close();
      }
      await context.close();
    }
  } finally {
    if (browser) await browser.close();
    server.close();
  }

  writeReport(results, baseUrl);
  const failures = results.flatMap((result) => result.failures.map((failure) => `${result.route.path} ${result.viewport.name}: ${failure}`));
  if (failures.length) {
    console.error(`MOBILE_QA FAIL (${failures.length} failures)`);
    for (const failure of failures.slice(0, 80)) console.error(`- ${failure}`);
    console.error(`Report: ${join(reportRoot, 'report.md')}`);
    process.exit(1);
  }
  console.log(`MOBILE_QA PASS — report written to ${join(reportRoot, 'report.md')}`);
}

main().catch((error) => {
  console.error(error?.stack || error);
  process.exit(1);
});
