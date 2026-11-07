const { chromium } = require('/tmp/node_modules/playwright');
const EXE = '/home/danie/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome';
(async () => {
  const b = await chromium.launch({ headless: true, executablePath: EXE });
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  await p.goto('file:///mnt/c/Users/danie/Public-html-pages/misra-rule-7-5-zero-program/technical/index.html', { waitUntil: 'load' });
  await p.waitForTimeout(2500);
  const res = await p.evaluate(() => {
    return [...document.querySelectorAll('.slide')].map((s, i) => {
      const pad = getComputedStyle(s);
      return { n: i + 1, scrollH: s.scrollHeight, clientH: s.clientHeight,
               overflow: s.scrollHeight > s.clientHeight + 2,
               cls: s.className };
    });
  });
  for (const r of res) console.log(`slide ${r.n} (${r.cls}): ${r.scrollH}/${r.clientH} ${r.overflow ? 'OVERFLOW' : 'ok'}`);
  await b.close();
})();
