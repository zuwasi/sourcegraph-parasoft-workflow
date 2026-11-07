const { chromium } = require('/tmp/node_modules/playwright');
const EXE = '/home/danie/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome';
(async () => {
  const b = await chromium.launch({ headless: true, executablePath: EXE });
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  await p.goto('file:///mnt/c/Users/danie/Public-html-pages/misra-rule-7-5-zero-program/technical/index.html', { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  const n = parseInt(process.argv[2]);
  for (let i = 1; i < n; i++) { await p.keyboard.press('ArrowRight'); await p.waitForTimeout(120); }
  await p.waitForTimeout(600);
  await p.screenshot({ path: `/tmp/shots/deck_${String(n).padStart(2,'0')}.png` });
  await b.close();
})();
