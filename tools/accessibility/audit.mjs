import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import { chromium } from 'playwright';
import AxeBuilder from '@axe-core/playwright';

const root = process.cwd();
const output = path.join(root, 'accessibility-report');
const live = process.env.AUDIT_TARGET !== 'local';
const sha = process.env.AUDIT_SHA || 'manual';
const tags = ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa', 'best-practice'];
const report = { generated: new Date().toISOString(), commit: sha, target: live ? 'live' : 'local', tags, pages: [], results: [], errors: [], skipped: [] };
await fs.mkdir(output, { recursive: true });

async function inventory(dir = root) {
  const found = [];
  for (const e of await fs.readdir(dir, { withFileTypes: true })) {
    if (e.name.startsWith('.') || ['node_modules', 'tools', 'accessibility-report'].includes(e.name)) continue;
    const full = path.join(dir, e.name);
    if (e.isDirectory()) found.push(...await inventory(full));
    else if (e.name.endsWith('.html')) found.push(path.relative(root, full).split(path.sep).join('/'));
  }
  return found.sort();
}
report.pages = await inventory();
let server;
let origin = 'https://britishtvhub.com';
if (!live) {
  const mime = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.jpg': 'image/jpeg' };
  server = http.createServer(async (req, res) => {
    try {
      let relative = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
      if (relative.endsWith('/')) relative += 'index.html';
      const file = path.resolve(root, '.' + relative);
      if (!file.startsWith(root + path.sep)) { res.writeHead(403).end(); return; }
      const data = await fs.readFile(file);
      res.writeHead(200, { 'Content-Type': mime[path.extname(file)] || 'application/octet-stream' }).end(data);
    } catch { res.writeHead(404).end('Not found'); }
  });
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  origin = `http://127.0.0.1:${server.address().port}`;
}
report.origin = origin;
const browser = await chromium.launch();
const escape = s => String(s).replace(/[&<>"']/g, x => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[x]));
async function scan(page, file, viewport, state) {
  const a = await new AxeBuilder({ page }).withTags(tags).analyze();
  report.results.push({ file, viewport, state, url: page.url(), engine: a.testEngine, violations: a.violations, incomplete: a.incomplete, passedRules: a.passes.length });
  await fs.writeFile(path.join(output, 'report.json'), JSON.stringify(report, null, 2));
}
async function settle(page) {
  await page.evaluate(async () => {
    if (document.fonts) await Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 3000))]);
    const height = Math.min(document.documentElement.scrollHeight, 40000);
    for (let y = 0; y < height; y += 900) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 25)); }
    window.scrollTo(0, 0);
  });
  await page.waitForTimeout(1200);
}
async function interactive(page, file, viewport) {
  if (file === 'index.html') {
    if (viewport === 'mobile') await page.locator('#nav-hamburger-btn').click();
    await page.locator('.nav-dropdown-toggle').click();
    await scan(page, file, viewport, 'discover-open');
    await page.locator('.nav-dropdown-toggle').click();
    await page.locator('.nav-search-toggle').click();
    await page.locator('#nav-search-input').fill('Vera');
    await scan(page, file, viewport, 'search-results');
  }
  if (file === 'shows-index.html') {
    await page.locator('#fdsSearchInput').fill('Vera');
    await scan(page, file, viewport, 'show-suggestions');
    await page.locator('#fdsSearchInput').press('ArrowDown');
    await page.locator('#fdsSearchInput').press('Enter');
    await scan(page, file, viewport, 'show-result');
  }
  if (['quiz.html', 'village-quiz.html', 'british-tv-personality-quiz.html', 'halloween-mystery-builder.html'].includes(file)) {
    for (let i = 0; i < 12 && await page.locator('#question-wrap').isVisible(); i++) {
      await page.locator('.opt-btn').first().click();
      await page.waitForTimeout(400);
    }
    await page.locator('#result-wrap').waitFor({ state: 'visible' });
    await scan(page, file, viewport, 'quiz-result');
  }
  if (file === 'shows/vera.html') {
    await page.locator('.wl-dd-toggle').first().click();
    await scan(page, file, viewport, 'watch-list-open');
  }
}

try {
  for (const [viewport, dimensions] of Object.entries({ desktop: { width: 1440, height: 1000 }, mobile: { width: 390, height: 844 } })) {
    const context = await browser.newContext({ viewport: dimensions, serviceWorkers: 'block' });
    // Avoid external checkout redirects; do not block fonts, images, chat or frames.
    await context.route('**/*', async route => {
      const r = route.request();
      if (r.isNavigationRequest() && r.frame().parentFrame() === null && new URL(r.url()).origin !== origin) await route.abort();
      else await route.continue();
    });
    for (const file of report.pages) {
      if (file === 'checkout-redirect.html') {
        if (viewport === 'desktop') report.skipped.push({ file, reason: 'External checkout redirect; destination requires separate assessment.' });
        continue;
      }
      const page = await context.newPage();
      page.setDefaultTimeout(15000);
      try {
        const url = new URL('/' + file, origin);
        url.searchParams.set('a11y', sha);
        const response = await page.goto(url.href, { waitUntil: 'domcontentloaded', timeout: 45000 });
        if (!response || (response.status() >= 400 && file !== '404.html')) throw new Error(`HTTP ${response?.status()}`);
        if (new URL(page.url()).origin !== origin) throw new Error('Unexpected external redirect');
        await settle(page);
        await scan(page, file, viewport, 'initial');
        await interactive(page, file, viewport);
        console.log(`${viewport} ${file}: scanned`);
      } catch (e) { report.errors.push({ file, viewport, message: e.message }); console.error(`${viewport} ${file}: ${e.message}`); }
      finally { await page.close(); }
    }
    await context.close();
  }
} finally {
  await browser.close();
  if (server) await new Promise(resolve => server.close(resolve));
}

const groups = new Map();
let instances = 0, reviews = 0, siteBlockingInstances = 0;
for (const r of report.results) {
  reviews += r.incomplete.reduce((n, v) => n + v.nodes.length, 0);
  for (const v of r.violations) {
    instances += v.nodes.length;
    if (!groups.has(v.id)) groups.set(v.id, { id: v.id, impact: v.impact, help: v.help, helpUrl: v.helpUrl, pages: new Set(), findings: [] });
    const g = groups.get(v.id); g.pages.add(r.file);
    for (const n of v.nodes) {
      const insideFrame = Array.isArray(n.target) && n.target.length > 1;
      const isYouTube = /ytmVideoInfo|html5-video-player|ytCoreImage|youtube\.com|youtube-nocookie\.com/i.test(n.html) || (insideFrame && /youtube/i.test(JSON.stringify(n.target)));
      const ownership = isYouTube ? "YouTube embedded player" : (insideFrame ? "Embedded third-party content" : "British TV Hub");
      g.findings.push({ file: r.file, viewport: r.viewport, state: r.state, selector: n.target, html: n.html, explanation: n.failureSummary, ownership });
      if (ownership === "British TV Hub" && ['critical', 'serious'].includes(v.impact)) siteBlockingInstances++;
    }
  }
}
report.summary = { inventory: report.pages.length, scannedPages: new Set(report.results.map(r => r.file)).size, scanStates: report.results.length, ruleGroups: groups.size, violationInstances: instances, siteBlockingInstances, manualReviewInstances: reviews, scanErrors: report.errors.length, skippedPages: report.skipped.length };
report.groups = [...groups.values()].map(g => ({ ...g, pages: [...g.pages] })).sort((a, b) => b.pages.length - a.pages.length);
await fs.writeFile(path.join(output, 'report.json'), JSON.stringify(report, null, 2));
const summary = `# Sitewide accessibility report\n\nCommit: ${sha}\nTarget: ${report.target}\n\n${JSON.stringify(report.summary, null, 2)}\n\nAutomated findings require review; this report does not establish full accessibility. Counts include repeated viewport and interaction states. Embedded third-party findings remain included and are labeled by ownership in the full report. Cross-origin chat, captions, keyboard behavior and screen-reader use still need manual verification.\n\n| Rule | Impact | Pages | Instances |\n| --- | --- | ---: | ---: |\n${report.groups.map(g => `| ${g.id} | ${g.impact} | ${g.pages.length} | ${g.findings.length} |`).join('\n')}\n\nScan errors: ${report.errors.length}. Skipped pages: ${report.skipped.length}. Full details are in report.json and report.html.\n`;
await fs.writeFile(path.join(output, 'summary.md'), summary);
if (process.env.GITHUB_STEP_SUMMARY) await fs.appendFile(process.env.GITHUB_STEP_SUMMARY, summary);
const details = report.groups.map(g => `<details><summary>${escape(g.id)} — ${g.pages.length} pages, ${g.findings.length} instances (${escape(g.impact)})</summary><p><a href="${escape(g.helpUrl)}">${escape(g.help)}</a></p>${g.findings.map(n => `<article><h3>${escape(n.file)} · ${escape(n.viewport)} · ${escape(n.state)} · ${escape(n.ownership)}</h3><pre>${escape(JSON.stringify(n.selector))}\n${escape(n.html)}\n${escape(n.explanation)}</pre></article>`).join('')}</details>`).join('');
await fs.writeFile(path.join(output, 'report.html'), `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>British TV Hub accessibility report</title><style>body{font:16px/1.6 Arial,sans-serif;max-width:1100px;margin:auto;padding:24px;color:#172033;background:#fff}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f0f2f6;padding:16px}details{border:1px solid #687080;padding:16px;margin:16px 0}summary{cursor:pointer;font-weight:bold}a{color:#164e9f}article{border-top:1px solid #687080}</style><h1>Sitewide accessibility report</h1><pre>${escape(summary)}</pre><h2>Grouped findings</h2>${details}<h2>Scan errors</h2><pre>${escape(JSON.stringify(report.errors, null, 2))}</pre><h2>Skipped pages</h2><pre>${escape(JSON.stringify(report.skipped, null, 2))}</pre></html>`);
console.log(JSON.stringify(report.summary));
// Third-party embed findings and first-party moderate/minor findings remain visible in
// the artifact, but only scan errors or serious/critical British TV Hub findings fail CI.
process.exitCode = report.errors.length || siteBlockingInstances ? 1 : 0;
