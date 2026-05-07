import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const pages = [
  ['index', 'https://flotilla.social'],
  ['support', 'https://flotilla.social/support'],
  ['data', 'https://flotilla.social/data'],
  ['cssp', 'https://flotilla.social/cssp'],
  ['terms', 'https://flotilla.social/terms'],
  ['privacy', 'https://flotilla.social/privacy'],
  ['articles', 'https://flotilla.social/articles'],
  ['article-what-is-flotilla', 'https://flotilla.social/articles/what-is-flotilla'],
  ['article-getting-started', 'https://flotilla.social/articles/getting-started'],
  ['article-joining-a-space', 'https://flotilla.social/articles/joining-a-space'],
  ['article-is-flotilla-private', 'https://flotilla.social/articles/is-flotilla-private'],
  ['article-community-and-support', 'https://flotilla.social/articles/community-and-support'],
  ['article-creating-a-space', 'https://flotilla.social/articles/creating-a-space'],
  ['article-self-hosting-a-space', 'https://flotilla.social/articles/self-hosting-a-space'],
  ['article-managing-a-space', 'https://flotilla.social/articles/managing-a-space'],
];

const outDir = new URL('./screenshots/', import.meta.url).pathname;
await mkdir(outDir, { recursive: true });

const browser = await chromium.launch();
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
});

for (const [name, url] of pages) {
  const page = await context.newPage();
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(1500);
    await page.screenshot({ path: `${outDir}${name}-desktop.png`, fullPage: true });
    console.log(`desktop: ${name}`);
  } catch (e) {
    console.error(`desktop fail ${name}: ${e.message}`);
  }
  await page.close();
}

const mobile = await browser.newContext({
  viewport: { width: 390, height: 844 },
  deviceScaleFactor: 2,
  isMobile: true,
});

for (const [name, url] of pages) {
  const page = await mobile.newPage();
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
    await page.waitForTimeout(1500);
    await page.screenshot({ path: `${outDir}${name}-mobile.png`, fullPage: true });
    console.log(`mobile: ${name}`);
  } catch (e) {
    console.error(`mobile fail ${name}: ${e.message}`);
  }
  await page.close();
}

await browser.close();
console.log('done');
