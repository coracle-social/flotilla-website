import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const pages = [
  ['index', 'http://localhost:4321/'],
  ['articles', 'http://localhost:4321/articles'],
  ['article-self-hosting', 'http://localhost:4321/articles/self-hosting-a-space'],
  ['terms', 'http://localhost:4321/terms'],
  ['404', 'http://localhost:4321/nope'],
];

const outDir = new URL('./rebuild-screenshots/', import.meta.url).pathname;
await mkdir(outDir, { recursive: true });

const browser = await chromium.launch();
const desktop = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
});
for (const [name, url] of pages) {
  const page = await desktop.newPage();
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 15000 });
    await page.waitForTimeout(800);
    await page.screenshot({ path: `${outDir}${name}-desktop.png`, fullPage: true });
    console.log(`desktop: ${name}`);
  } catch (e) {
    console.error(`fail ${name}: ${e.message}`);
  }
  await page.close();
}
const mobile = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
});
const page = await mobile.newPage();
await page.goto('http://localhost:4321/', { waitUntil: 'networkidle', timeout: 15000 });
await page.waitForTimeout(800);
await page.screenshot({ path: `${outDir}index-mobile.png`, fullPage: true });
console.log('mobile: index');
await page.close();

await browser.close();
