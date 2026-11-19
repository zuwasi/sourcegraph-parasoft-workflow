#!/usr/bin/env python3
"""Assemble the Rule 7.5 Zero Program technical deck from the ESL reference template."""
import re

REF = open('/tmp/ref_deck.html').read()
style = re.search(r'<style>.*?</style>', REF, re.S).group(0)
script = re.search(r'<script>.*?</script>', REF, re.S).group(0)
tail = re.search(r'</main>(.*?)<script>', REF, re.S).group(1)

R = 1.714  # tenant/github shots 1680x980
RP = 1.684  # parasoft report shots 1600x950

def shot(name, caption, w=1434, ratio=R, wide=False):
    h = round(w / ratio / 2) * 2
    cls = 'shot wideshot' if wide else 'shot'
    return (f'<figure class="{cls}" style="--w:{w}px;--r:{ratio:.3f}">'
            f'<figcaption>{caption}</figcaption>'
            f'<a class="zoom" href="../assets/{name}" draggable="false">'
            f'<img src="../assets/{name}" width="{h and w}" height="{h}" decoding="async" draggable="false" alt="{caption}"></a></figure>')

def shotw(name, caption, ratio, w=1434):
    h = round(w / ratio / 2) * 2
    return (f'<figure class="shot" style="--w:{w}px;--r:{ratio:.3f}">'
            f'<figcaption>{caption}</figcaption>'
            f'<a class="zoom" href="../assets/{name}" draggable="false">'
            f'<img src="../assets/{name}" width="{w}" height="{h}" decoding="async" draggable="false" alt="{caption}"></a></figure>')

S = []

# 01 — Title
S.append(f'''<section class="slide title"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Technical program brief · 01</div>
  <h1>The Rule 7.5 Zero Program: Sourcegraph finds, Parasoft decides</h1>
  <p class="subtitle">MISRA C:2025 Rule 7.5 taken to certified zero on a real open-source code base, then the same closed loop scaled to 1,095 findings across the top mechanical rules: the measured evidence, the scripts, the tenant queries, and the revertable branch topology</p>
  <div class="brandrow">
    <div class="brandchip ps"><img src="../assets/parasoft-logo.png" alt="Parasoft"><span>Parasoft C/C++test · opens and closes the loop</span></div>
    <div class="brandchip sg"><img src="../assets/SG-logo.png" alt="Sourcegraph"><span>Sourcegraph Cloud · finds, fixes at scale, guards</span></div>
  </div>
  <div class="grid2 mid">
    <div class="stack">
      <div class="card v"><div class="n">1095 &rarr; 766</div><div class="l">Whole-repo Parasoft MISRA C 2025 findings before and after three mechanical batch fixes; seed module went 8 &rarr; 0 in the pilot</div></div>
      <div class="card"><div class="n">1 loop, 2 tools</div><div class="l">Parasoft C/C++test 2026.1.3 opens and closes the loop as evidence of record; Sourcegraph Cloud (eswlab tenant) finds, fixes at scale, and guards</div></div>
    </div>
    <div class="person-card">
      <img src="../assets/daniel-liezrowice.jpg" width="140" height="140" alt="Daniel Liezrowice">
      <div>
        <strong>Daniel Liezrowice</strong>
        <span>CTO, ESL - Engineering Software Lab</span>
        <p>Embedded software consultancy, Parasoft and Perforce partner in Israel for over 20 years. This brief documents the ESL Sourcegraph + Parasoft zero-program demonstration.</p>
        <a href="https://www.linkedin.com/in/liezrowice/" target="_blank" rel="noopener">linkedin.com/in/liezrowice</a>
      </div>
    </div>
  </div>
  <div class="foot">Engineering Software Lab Ltd. · 7 November 2026 · Every number in this deck was measured, every screenshot is a genuine capture of the eswlab tenant, the local Parasoft reports, or the GitHub fork</div>
</div></section>''')

# 02 — The workflow loop
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>The workflow · 02</div>
  <h1>A closed loop with one decision point, executed on a real repo</h1>
  <p class="subtitle">The published ESL workflow, executed end to end on <code>driftregion/iso14229</code></p>
<div class="diagram">┌────────────────────────────────────────────────────────┐
│ 1. PARASOFT BASELINE SCAN        opens the loop        │
│ 2. SOURCEGRAPH MATCH QUERIES     step 5                │
│ 3. BATCH CHANGE SCRIPT DESIGN    v1, v2, ...           │
│ 4. DRY RUN → REVIEW → MERGE      step 6, revertable    │
│ 5. PARASOFT VERIFICATION SCAN    closes the loop       │
│    zero? ── no ──▶ back to step 3 (script v2, v3)      │
│ 6. HOLD ZERO  guard query in CI · pipeline scan ·      │
│    Code Monitor · dashboard · release-branch proof     │
└────────────────────────────────────────────────────────┘</div>
  <div class="grid2">
    <div class="card"><span class="tag">Parasoft decides</span><h3>Evidence of record</h3><p>Measures the problem (baseline), verifies the fix (zero or residual), re-measures on every pipeline run. Its report is the compliance artifact.</p></div>
    <div class="card v"><span class="tag">Sourcegraph finds &amp; fixes</span><h3>Scale and guard</h3><p>Turns each mechanical class into a search query, drives the batch fix, and holds zero with a standing guard query.</p></div>
  </div>
</div></section>''')

# 03 — The loop in nine steps (flowchart restored from the plan deck)
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>The workflow · 03</div>
  <h1>The loop in nine steps, as executed on the demo</h1>
  <p class="subtitle">Parasoft opens the loop and closes it; Sourcegraph acts in between; zero is when the verifier says zero</p>
  <div class="fchart">
  <svg viewBox="0 0 1160 470" width="100%" role="img" aria-label="Flowchart: Parasoft baseline scan measures the problem, 1,095 findings repo-wide and 8 in the seed module; extrapolation sizes the program at four repos and 400 branches; decision to automate; design Sourcegraph scripts; batch change fixes every incident; Parasoft verification scan; if not zero, redesign the script and iterate; if zero, scale to all repos and hold with a standing gate.">
    <defs>
      <marker id="ah" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#1d6bd0"/></marker>
      <marker id="ahr" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#c03535"/></marker>
      <marker id="ahg" markerWidth="9" markerHeight="9" refX="7.5" refY="4.5" orient="auto"><path d="M0,0 L9,4.5 L0,9 z" fill="#1e7d33"/></marker>
    </defs>
    <g font-family="Inter,Arial,sans-serif">
      <rect x="20" y="50" width="250" height="80" rx="10" fill="#fff4dc" stroke="#e8a317" stroke-width="2"/>
      <image href="../assets/parasoft-logo.png" x="186" y="58" width="70" height="28"/>
      <text x="35" y="78" font-size="11" font-weight="700" letter-spacing="1" fill="#8a5e00">1 &#183; PARASOFT STARTS</text>
      <text x="35" y="99" font-size="14" font-weight="600" fill="#24282d">Baseline C/C++test scan</text>
      <text x="35" y="118" font-size="13" fill="#5a626c">one module, small scope</text>

      <rect x="305" y="50" width="250" height="80" rx="10" fill="#fff4dc" stroke="#e8a317" stroke-width="2"/>
      <image href="../assets/parasoft-logo.png" x="471" y="58" width="70" height="28"/>
      <text x="320" y="78" font-size="11" font-weight="700" letter-spacing="1" fill="#8a5e00">2 &#183; MEASURE</text>
      <text x="320" y="99" font-size="14" font-weight="600" fill="#24282d">1,095 findings repo-wide</text>
      <text x="320" y="118" font-size="13" fill="#5a626c">8 in the seed module alone</text>

      <rect x="590" y="50" width="250" height="80" rx="10" fill="#fff4dc" stroke="#e8a317" stroke-width="2"/>
      <image href="../assets/parasoft-logo.png" x="756" y="58" width="70" height="28"/>
      <text x="605" y="78" font-size="11" font-weight="700" letter-spacing="1" fill="#8a5e00">3 &#183; EXTRAPOLATE</text>
      <text x="605" y="99" font-size="14" font-weight="600" fill="#24282d">~50,000 project-wide</text>
      <text x="605" y="118" font-size="13" fill="#5a626c">4 repos &#183; 400 branches</text>

      <rect x="875" y="50" width="250" height="80" rx="10" fill="#fdf6e3" stroke="#ffb30b" stroke-width="2"/>
      <image href="../assets/parasoft-logo.png" x="1041" y="58" width="70" height="28"/>
      <text x="890" y="78" font-size="11" font-weight="700" letter-spacing="1" fill="#8a5e00">4 &#183; DECIDE</text>
      <text x="890" y="99" font-size="14" font-weight="600" fill="#24282d">Hand-fixing: thousands of</text>
      <text x="890" y="118" font-size="14" font-weight="600" fill="#24282d">edits, no proof &#8594; automate</text>

      <line x1="270" y1="90" x2="298" y2="90" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>
      <line x1="555" y1="90" x2="583" y2="90" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>
      <line x1="840" y1="90" x2="868" y2="90" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>

      <rect x="875" y="215" width="250" height="106" rx="10" fill="#eaf2fd" stroke="#4f9efb" stroke-width="2"/>
      <rect x="1033" y="223" width="84" height="30" rx="6" fill="#0a0a0a"/>
      <image href="../assets/SG-logo.png" x="1041" y="228" width="68" height="20"/>
      <text x="890" y="256" font-size="11" font-weight="700" letter-spacing="1" fill="#1d6bd0">5 &#183; SOURCEGRAPH</text>
      <text x="890" y="277" font-size="14" font-weight="600" fill="#24282d">Design the scripts:</text>
      <text x="890" y="295" font-size="13" fill="#5a626c">match queries + value-preserving</text>
      <text x="890" y="312" font-size="13" fill="#5a626c">replacement rules</text>

      <rect x="590" y="215" width="250" height="106" rx="10" fill="#eaf2fd" stroke="#4f9efb" stroke-width="2"/>
      <rect x="748" y="223" width="84" height="30" rx="6" fill="#0a0a0a"/>
      <image href="../assets/SG-logo.png" x="756" y="228" width="68" height="20"/>
      <text x="605" y="256" font-size="11" font-weight="700" letter-spacing="1" fill="#1d6bd0">6 &#183; SOURCEGRAPH</text>
      <text x="605" y="277" font-size="14" font-weight="600" fill="#24282d">Run the Batch Change:</text>
      <text x="605" y="295" font-size="14" font-weight="600" fill="#24282d">finds every incident, fixes it</text>
      <text x="605" y="312" font-size="13" fill="#5a626c">reviewed PR, CI green</text>

      <rect x="305" y="215" width="250" height="92" rx="10" fill="#fff4dc" stroke="#e8a317" stroke-width="2"/>
      <image href="../assets/parasoft-logo.png" x="471" y="223" width="70" height="28"/>
      <text x="320" y="246" font-size="11" font-weight="700" letter-spacing="1" fill="#8a5e00">7 &#183; PARASOFT VERIFIES</text>
      <text x="320" y="267" font-size="14" font-weight="600" fill="#24282d">Verification re-scan:</text>
      <text x="320" y="286" font-size="13" fill="#5a626c">did Sourcegraph succeed?</text>
      <text x="320" y="303" font-size="13" fill="#5a626c">the scanner is the judge</text>

      <polygon points="145,215 255,261 145,307 35,261" fill="#fdf6e3" stroke="#ffb30b" stroke-width="2"/>
      <text x="145" y="256" font-size="13" font-weight="700" fill="#24282d" text-anchor="middle">Zero</text>
      <text x="145" y="273" font-size="13" font-weight="700" fill="#24282d" text-anchor="middle">findings?</text>

      <line x1="1000" y1="130" x2="1000" y2="208" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>
      <line x1="875" y1="261" x2="847" y2="261" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>
      <line x1="590" y1="261" x2="562" y2="261" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>
      <line x1="305" y1="261" x2="268" y2="261" stroke="#1d6bd0" stroke-width="2.5" marker-end="url(#ah)"/>

      <path d="M 145 215 L 145 172 L 1000 172 L 1000 206" fill="none" stroke="#c03535" stroke-width="2.5" stroke-dasharray="7 5" marker-end="url(#ahr)"/>
      <rect x="380" y="155" width="420" height="26" rx="13" fill="#c03535"/>
      <text x="590" y="173" font-size="13" font-weight="700" fill="#fff" text-anchor="middle">NOT ZERO: redesign the script (v2, v3, &#8230;) and run again</text>

      <line x1="145" y1="307" x2="145" y2="352" stroke="#1e7d33" stroke-width="2.5" marker-end="url(#ahg)"/>
      <text x="158" y="336" font-size="13" font-weight="700" fill="#1e7d33">YES</text>

      <rect x="20" y="355" width="250" height="80" rx="10" fill="#e9f7ee" stroke="#2fae5c" stroke-width="2"/>
      <text x="35" y="377" font-size="11" font-weight="700" letter-spacing="1" fill="#14532a">8 &#183; ZERO PROVEN</text>
      <text x="35" y="398" font-size="14" font-weight="600" fill="#24282d">Scale the proven script:</text>
      <text x="35" y="417" font-size="13" fill="#5a626c">merge across all 4 repos,</text>
      <text x="35" y="431" font-size="13" fill="#5a626c">400 branches inherit</text>

      <rect x="305" y="355" width="250" height="80" rx="10" fill="#e9f7ee" stroke="#2fae5c" stroke-width="2"/>
      <text x="320" y="377" font-size="11" font-weight="700" letter-spacing="1" fill="#14532a">9 &#183; HOLD AT ZERO</text>
      <text x="320" y="398" font-size="14" font-weight="600" fill="#24282d">Standing gate:</text>
      <text x="320" y="417" font-size="12.5" fill="#5a626c">SG guard query blocks new violations</text>
      <text x="320" y="432" font-size="12.5" fill="#5a626c">at the PR; Parasoft scans in CI</text>

      <line x1="270" y1="395" x2="298" y2="395" stroke="#1e7d33" stroke-width="2.5" marker-end="url(#ahg)"/>
    </g>
  </svg>
  </div>
  <div class="note">Parasoft opens the loop and closes it: the baseline scan sizes the problem (measured: 8 in the seed, 1,095 repo-wide), and every later scan is the verdict on Sourcegraph&#39;s work. Zero is when the verifier says zero, not when the tool claims it. On any non-zero scan we go straight back to script design, exactly as shown by the red loop.</div>
  <div class="foot">Iteration is cheap by design: each pass is a script edit plus a Batch Change preview, minutes of work, not another thousand hand edits.</div>
</div></section>''')

# 04 — Tool chain
S.append('''<section class="slide layers"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Tool chain · 04</div>
  <h1>The exact tool chain, versions, and invocation</h1>
  <p class="subtitle">Everything runs from one Windows host with WSL2 as the execution environment</p>
  <div class="grid3">
    <div class="card"><img class="cardlogo" src="../assets/parasoft-logo.png" alt="Parasoft"><span class="tag">Verifier</span><h3>Parasoft C/C++test Standard 2026.1.3</h3><p>Linux build 2026.1.3 (internal 10.7.4), driven headless with <code>cpptestcli</code>, config <code>builtin://MISRA C 2025</code>, compiler <code>gcc_12-64</code>, licensed from the DTP server on the Windows host.</p></div>
    <div class="card v"><img class="cardlogo" src="../assets/SG-logo.png" alt="Sourcegraph"><span class="tag">Finder / fixer</span><h3>Sourcegraph Cloud, eswlab tenant</h3><p><a href="https://eswlab.sourcegraphcloud.com/search" target="_blank" rel="noopener">eswlab.sourcegraphcloud.com</a>, site admin <code>daniell</code>, dedicated external service indexing the fork. Search API (<code>/search/stream</code>) and GraphQL for automation.</p></div>
    <div class="card"><span class="tag">Code host</span><h3>GitHub fork + branches</h3><p>Upstream <code>driftregion/iso14229</code> is never touched; all work lives on the fork's own branches. Verified: no PR exists upstream.</p></div>
  </div>
''' + shot('parasoft_baseline_seed_top.png', 'C/C++test 2026.1.3 HTML report header: the whole-repo baseline run that opens the loop at 1,095 findings', ratio=RP, w=900) + '''
<div class="note">Gotchas: the DTP license server has <code>start_deactivated=true</code> (re-activate in the legacy <code>/pst</code> console after a restart); after a Windows reboot the three Parasoft services must be restarted first; a full scan takes 15-20 minutes.</div>
</div></section>''')

# 04 — The demo repo
S.append(f'''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>The demo repo · 05</div>
  <h1>Why iso14229: real automotive-relevant C, one honest catch</h1>
  <p class="subtitle">ISO 14229 (Unified Diagnostic Services) is the road-vehicle diagnostics layer every ECU speaks; the library is a C99 amalgamation, exactly the shape MISRA C programs look like</p>
  <div class="shotrow">
    <div class="side">
      <p>The upstream <code>driftregion/iso14229</code> tree contains <strong>zero</strong> <code>INTn_C</code>/<code>UINTn_C</code> uses, so a fair Rule 7.5 demo needs a seeded branch: <code>demo/rule75_seed/</code> adds 11 realistic calibration constants and call sites. The seeding commit is <code>3d3f7ab9</code>, pushed to the fork branch <code>misra-rule-7-5-seed</code> and pinned there so Sourcegraph always shows the before-state.</p>
      <p>The amalgamation itself (<code>iso14229.c</code>, 2,657 KB with the header) compiles standalone with gcc 12, which makes the Parasoft on-the-fly <code>gcc -c</code> invocation trivial.</p>
      <div class="note">Honesty rule for the demo: seeded violations are labeled "Demo seed only" in the file headers; the 1,095-finding whole-repo campaign later in this brief runs on the untouched upstream code, no seed involved.</div>
    </div>
''' + shot('gh-fork-home.png', 'The fork github.com/zuwasi/iso14229: all demo work lives here; upstream driftregion/iso14229 is never touched', ratio=R) + '''
  </div>
</div></section>''')

# 05 — Seeding
S.append(f'''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>The seed · 06</div>
  <h1>Eleven seeded candidates across three mechanical classes and two expert exclusions</h1>
  <p class="subtitle">The seed as committed (<code>3d3f7ab9</code>, branch <code>misra-rule-7-5-seed</code>); Rule 7.5 applies at call sites too</p>
<div class="diagram">/* Mechanical class 1: unary minus inside the macro argument */
#define DEMO_TEMP_OFFSET   INT32_C(-40)
/*   (+3 more: -100, -500L, -5) */

/* Mechanical class 2: suffix inside the macro argument */
#define DEMO_MASK          UINT32_C(0xFFUL)
#define DEMO_SAMPLE_RATE   UINT32_C(100U)
#define DEMO_TIMEOUT_MS    UINT64_C(5000ULL)
/* Excluded from automation: signed minimum (no in-macro fix exists) */
#define DEMO_INT32_MIN_SENTINEL INT32_C(-2147483648)
/* Manual-review class: non-literal argument */
#define DEMO_DERIVED_GAIN  INT32_C(DEMO_TEMP_OFFSET)
/* calibration_demo.c call sites, same violation classes */
demo_trim         = INT32_C(-25);
demo_mask_applied = UINT32_C(0xFFUL);</div>
  <div class="tablewrap"><table>
    <thead><tr><th>Class</th><th class="num">Instances</th><th>Automation</th></tr></thead>
    <tbody>
      <tr><td>Negative inside macro, incl. signed minimum</td><td class="num">6</td><td>value-preserving relocation; signed minimum to expert</td></tr>
      <tr><td>Literal suffix inside macro (hex and decimal)</td><td class="num">4</td><td>strip suffix, value preserved</td></tr>
      <tr><td>Non-literal argument</td><td class="num">1</td><td>expert decision, never automated</td></tr>
      <tr><td><strong>Total seeded candidates</strong></td><td class="num"><strong>11</strong></td><td>3 mechanical + 2 human classes; plus 2 compliant reference forms</td></tr>
    </tbody>
  </table></div>
</div></section>''')

# 06 — Phase 1 baseline
S.append(f'''<section class="slide tall"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Phase 1 · 07</div>
  <h1>The seed baseline is 8 violations</h1>
  <p class="subtitle">C/C++test Standard 2026.1.3, <code>builtin://MISRA C 2025</code>, gcc_12-64, module <code>demo/rule75_seed</code>; cross-verified on 2025.2 with identical verdicts before the upgrade</p>
<div class="diagram">cpptestcli \\
  -localsettings .amp/in/cpptest_local.properties \\
  -config "builtin://MISRA C 2025" -compiler gcc_12-64 -module demo/rule75_seed \\
  -- gcc -I demo/rule75_seed -c demo/rule75_seed/calibration_demo.c</div>
  <div class="shotrow">
''' + shotw('donut_seed_baseline_8.jpeg', 'Baseline findings by severity: 8 total, 5 at severity 1 (Rule 7.5), 3 at severity 2 (Rule 8.4)', 1.615, w=600) + f'''
    <div class="side">
      <div class="tablewrap"><table style="table-layout:fixed;width:100%;min-width:0">
        <thead><tr><th>Rule</th><th class="num">Findings</th><th>Detail</th></tr></thead>
        <tbody>
          <tr><td>Rule 7.5 (Mandatory)</td><td class="num">5</td><td>4 suffix + 1 non-literal</td></tr>
          <tr><td>Rule 8.4 (Required)</td><td class="num">3</td><td>missing header declarations</td></tr>
        </tbody>
      </table></div>
      <p>The baseline is the contract: the verification scan must show the mechanical classes at zero, and the dashboard numbers come from this report.</p>
    </div>
  </div>
</div></section>''')

# 07 — Material finding
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Verifier finding · 08</div>
  <h1>The deck assumed negatives violate; the verifier disagrees, on two versions</h1>
  <p class="subtitle">The most valuable discovery of the pilot, found because the loop starts from the scanner, not from the standard's text</p>
  <div class="grid2">
    <div class="card"><span class="tag">Premise</span><h3>What the published plan assumed</h3><p>Rule 7.5 bans the minus inside <code>INTn_C(-N)</code>, so the demo would gate on negatives, suffixes, and non-literals: three automated classes.</p></div>
    <div class="card v"><span class="tag">Measured</span><h3>What Parasoft actually flags</h3><p>On <strong>both</strong> 2025.2 and 2026.1.3 with the MISRA C 2025 config: <strong>zero</strong> findings on any of the five <code>INTn_C(-N)</code> forms, including the signed minimum. Only suffix and non-literal forms are flagged (the 5 severity-1 findings).</p></div>
  </div>
  <div class="grid2">
    <div class="card"><span class="tag">Consequence 1</span><h3>The zero gate redefines itself from the scan</h3><p>Zero means the suffix + non-literal classes reach zero. The v1 script still normalizes negatives (value-preserving, matches the compliant style), but negatives no longer gate.</p></div>
    <div class="card v"><span class="tag">Consequence 2</span><h3>Reconciliation becomes a demo highlight</h3><p>Source inventory (11 candidates) vs scan (5 findings) diverges by design. The demo shows the divergence and explains it instead of hiding it: exactly what the reconciliation step exists to catch.</p></div>
  </div>
  <div class="note">Method note: this is why the loop's decision point must be the scanner. A workflow that trusted the standard's prose would have declared the seed non-compliant in a class the verifier does not measure.</div>
</div></section>''')

# 08 — Tenant + query design
S.append(f'''<section class="slide tall"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Phase 2 · 09</div>
  <h1>Three query lessons the tenant taught</h1>
  <p class="subtitle">eswlab tenant, license renewed 2026-11-06, fork indexed via a dedicated external service</p>
''' + shot('tenant-home.png', 'The eswlab Sourcegraph Cloud tenant (https://eswlab.sourcegraphcloud.com), authenticated as site admin daniell', ratio=R, w=560) + '''
  <div class="grid3">
    <div class="card"><span class="tag">Lesson 1</span><h3><code>fork:yes</code> is mandatory</h3><p>The repo is a GitHub fork; without the <code>fork:yes</code> predicate every query silently returns zero because fork filtering excludes it by default.</p></div>
    <div class="card v"><span class="tag">Lesson 2</span><h3><code>patternType:regexp</code></h3><p>The default is literal matching. Every structural pattern in this program is a regular expression and must opt in explicitly.</p></div>
    <div class="card"><span class="tag">Lesson 3</span><h3>Zoekt cannot negate</h3><p>Negated character classes (<code>[^)]</code>) silently return zero results. Every query uses positive classes instead of "anything but a paren".</p></div>
  </div>
</div></section>''')

# 09 — Class queries
S.append(f'''<section class="slide layers"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Phase 2 · 10</div>
  <h1>The three class queries, run live on the seed branch</h1>
  <p class="subtitle">Each mechanical class is one query; counts below are what the tenant returned on 2026-11-06</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Class</th><th>Query (patternType:regexp)</th><th class="num">Seed</th><th class="num">Cleaned</th></tr></thead>
    <tbody>
      <tr><td>Negative argument</td><td><code>(INT32_C|INT64_C|UINT32_C|UINT64_C)\\(\\s*-\\s*[0-9]+\\s*\\)</code></td><td class="num">6</td><td class="num">0</td></tr>
      <tr><td>Literal suffix</td><td><code>(\\...)\\(\\s*(0[xX][0-9a-fA-F]+|[0-9]+)\\s*[uUlL]+\\s*\\)</code></td><td class="num">4</td><td class="num">0</td></tr>
      <tr><td>Non-literal argument</td><td><code>(\\...)\\(\\s*[A-Za-z_][A-Za-z0-9_]*\\s*\\)</code></td><td class="num">1</td><td class="num">0</td></tr>
      <tr><td>Signed minimum (expert)</td><td><code>INT32_C\\(\\s*-\\s*2147483648\\s*\\)</code></td><td class="num">1</td><td class="num">0</td></tr>
    </tbody>
  </table></div>
''' + shot('tenant-query-negative-seed.png', 'Negative-argument query on @misra-rule-7-5-seed: 6 results in 0.07s, including the signed-minimum sentinel at calibration_constants.h line 27', ratio=R, w=1200) + '''
</div></section>''')

# 10 — Combined guard query
S.append(f'''<section class="slide prompt"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Phase 2 · 11</div>
  <h1>One combined guard query: 11 before, 0 after</h1>
  <p class="subtitle">The all-mechanical-classes query with <code>lang:C</code> so the fix script's own docstring cannot match; this is the exact query the PR gate runs</p>
<div class="diagram">repo:zuwasi/iso14229@BRANCH fork:yes lang:C patternType:regexp
  (INT32_C|INT64_C|UINT32_C|UINT64_C)\\(\\s*
    (-\\s*[0-9]+[uUlL]*            negative decimal
    |0[xX][0-9a-fA-F]+\\s*[uUlL]+  suffixed hex
    |[0-9]+\\s*[uUlL]+             suffixed decimal
    |[A-Za-z_][A-Za-z0-9_]*)      non-literal identifier
  \\s*\\)</div>
  <div class="shotrow tall">
''' + shot('tenant-seed-combined.png', 'Seed branch: 11 results in 0.13s, the full seeded inventory in one query', ratio=R) + shot('tenant-demo-combined-zero.png', 'Cleaned branch: "No results matched your search", 0 results in 0.12s', ratio=R) + '''
  </div>
</div></section>''')

# 11 — Reconciliation
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Reconciliation · 12</div>
  <h1>Inventory, scan, and search tell one story once you reconcile them</h1>
  <p class="subtitle">The step most teams skip, and the one that makes the demo credible</p>
  <div class="tablewrap"><table>
    <thead><tr><th>View</th><th class="num">Count</th><th>Why it differs</th></tr></thead>
    <tbody>
      <tr><td>Source inventory (seeded candidates)</td><td class="num">11</td><td>ground truth at source level, all shapes</td></tr>
      <tr><td>Sourcegraph combined query (seed)</td><td class="num">11</td><td>search sees every shape, including the negatives the verifier accepts</td></tr>
      <tr><td>Parasoft baseline (seed)</td><td class="num">5</td><td>verifier accepts the negative form on both tool versions (slide 07); flags suffix + non-literal only</td></tr>
      <tr><td>Parasoft verification (seed)</td><td class="num">0</td><td>all flagged classes zeroed by the v1 script + expert commit</td></tr>
      <tr><td>Sourcegraph combined query (cleaned)</td><td class="num">0</td><td>guard query goes green; Proof 1 for the hold-zero phase</td></tr>
    </tbody>
  </table></div>
  <div class="note">The 6-finding gap between inventory and scan is not noise: 5 negative forms + 1 non-literal mismatch. The non-literal <em>is</em> flagged; the negatives are not. Once explained, the divergence becomes the strongest slide in the compliance conversation.</div>
</div></section>''')

# 12 — v1 script
S.append('''<section class="slide tall"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Phase 3 · 13</div>
  <h1>The v1 transform script: two value-preserving rewrites, three exclusions</h1>
  <p class="subtitle"><code>iso14229/tools/rule75_v1.py</code>, commit <code>0fc00476</code>, fixture-tested before it ever touched the seed</p>
<div class="diagram">Transform 1 - suffix removal (value preserved):
  UINT32_C(0xFFUL)   ->  UINT32_C(0xFF)
  UINT64_C(5000ULL)  ->  UINT64_C(5000)

Transform 2 - minus relocation (value preserved):
  INT32_C(-40)       ->  (-INT32_C(40))

Excluded, reported for expert handling:
  INT32_C(-2147483648)      signed minimum: the "obvious" rewrite
                            (-INT32_C(2147483648)) is still
                            non-compliant; the fix is
                            ((-INT32_C(2147483647))-1)
  INT32_C(DEMO_TEMP_OFFSET) non-literal: needs a design decision,
                            not a rewrite
  out-of-range arguments    surfaced by compiler + scanner</div>
  <div class="grid2">
    <div class="card"><span class="tag">Fixture test</span><h3>Values identical before and after</h3><p>The fixture covers every transform and every exclusion; the test asserts <code>-40</code> stays <code>-40</code>, <code>0xFF</code> stays <code>0xFF</code>, and the excluded lines are untouched, then compiles the result.</p></div>
    <div class="card v"><span class="tag">Design rule</span><h3>Versioned scripts, never a one-off patch</h3><p>Every Parasoft non-zero verification produces a v2, v3, ... of the script. The script is the reviewable, reusable unit; the demo branch is disposable.</p></div>
  </div>
</div></section>''')

# 13 — Expert fixes
S.append('''<section class="slide tall"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Expert pass · 14</div>
  <h1>What automation must not touch: the expert commit</h1>
  <p class="subtitle">Commit <code>2c1f6403</code> (+9 &minus;4) closes the two exclusions and the three Rule 8.4 demo artifacts</p>
<div class="diagram">/* signed minimum: the only compliant spelling in C */
- #define DEMO_INT32_MIN_SENTINEL INT32_C(-2147483648)
+ #define DEMO_INT32_MIN_SENTINEL ((-INT32_C(2147483647))-1)

/* non-literal argument: use the constant directly */
- #define DEMO_DERIVED_GAIN  INT32_C(DEMO_TEMP_OFFSET)
+ #define DEMO_DERIVED_GAIN  DEMO_TEMP_OFFSET

/* Rule 8.4 (demo artifact): the three seed functions now have
   external declarations in the header */
+ void demo_seed_call_sites(void);
+ int32_t demo_get_trim(void);
+ uint32_t demo_get_mask(void);</div>
  <div class="tablewrap"><table>
    <thead><tr><th>Commit</th><th>Branch</th><th>Content</th></tr></thead>
    <tbody>
      <tr><td><code>3d3f7ab9</code></td><td><code>misra-rule-7-5-seed</code></td><td>seed: 11 candidates, pinned before-state</td></tr>
      <tr><td><code>0fc00476</code></td><td><code>misra-rule-7-5-demo</code></td><td>v1 script + mechanical fixes (+89 &minus;9)</td></tr>
      <tr><td><code>2c1f6403</code></td><td><code>misra-rule-7-5-demo</code></td><td>expert fixes: exclusions + declarations</td></tr>
    </tbody>
  </table></div>
  <div class="note">Both commits are pushed to the fork. The seed branch stays pinned so every before-query in this deck reproduces exactly, forever.</div>
</div></section>''')

# 14 — Seed verification zero
S.append(f'''<section class="slide tall"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Phase 5 · 15</div>
  <h1>Parasoft closes the loop: the seed is certified zero</h1>
  <p class="subtitle">Same command, same module, same config: 8 violations in, 0 violations out</p>
  <div class="shotrow tall">
''' + shotw('donut_seed_zero.jpeg', 'Verification scan findings: 0 total across all severities (the compliance evidence of record for the seed)', 1.615, w=760) + shot('tenant-demo-combined-zero.png', 'The other half of the proof: the tenant guard query on the cleaned branch returns 0 results', R) + '''
  </div>
  <div class="note">Report of record: <code>iso14229/reports/report.html</code>, regenerated by the 2026.1.3 verification run. Zero suppressed findings, zero exclusions in the config: the seed demo is a genuine zero, not a filtered one.</div>
</div></section>''')


# 16 — Parasoft in the loop (merged from the plan deck)
S.append(f'''<section class="slide layers"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>The verifier · 16</div>
  <h1>Parasoft enforces MISRA C 2025 and certifies the zero</h1>
  <p class="subtitle">The compliance pack in the test configuration: 388 of 388 MISRA C 2025 rules and directives enabled</p>
''' + shot('parasoft-misra-config.png', 'Real Parasoft C/C++test session: the MISRA C 2025 compliance pack selected in the test configuration (388 rules enabled), and the Quality Tasks panel listing per-file violations', ratio=1.778, w=1100) + f'''
  <div class="grid3">
    <div class="card"><img class="cardlogo" src="../assets/parasoft-logo.png" alt="Parasoft"><span class="tag">Standard config</span><h3><code>builtin://MISRA C 2025</code></h3><p>The built-in compliance pack, no cherry-picking: every MISRA C 2025 rule and directive enabled, compiler profile gcc_12-64.</p></div>
    <div class="card v"><span class="tag">Cross-version</span><h3>Same verdict on 2025.2 and 2026.1.3</h3><p>The pilot was verified on both versions before the upgrade: suffix and non-literal forms flagged, negative-in-macro accepted.</p></div>
    <div class="card"><span class="tag">Evidence</span><h3>The zero report is the artifact</h3><p>The verification scan's HTML report is what auditors and certification bodies see; it is the evidence of record for the whole program.</p></div>
  </div>
</div></section>''')

# 17 — pilot compliance dashboard (merged from the plan deck)
S.append(f'''<section class="slide wide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>The verifier · 17</div>
  <h1>Pilot dashboard: 8 &rarr; 0, measured</h1>
  <p class="subtitle">MISRA C 2025 Rule 7.5 cleanup, demo pilot on <code>driftregion/iso14229</code>, measured 2026-11-04, C/C++test Standard 2026.1.3</p>
  <div class="grid4">
    <div class="card v"><div class="n">8 &rarr; 0</div><div class="l">violations, total (5 Rule 7.5 + 3 Rule 8.4); -100% after v1 + expert merge</div></div>
    <div class="card"><div class="n">1 / 1</div><div class="l">demo modules at zero findings, Parasoft-certified on 2026.1.3</div></div>
    <div class="card"><div class="n">11</div><div class="l">source-level candidates reconciled against the scan, divergence documented</div></div>
    <div class="card v"><div class="n">100%</div><div class="l">mandatory rules in scope, no deviations filed</div></div>
  </div>
  <div class="tablewrap"><table>
    <thead><tr><th>Per-file zero proof (demo module)</th><th class="num">Baseline</th><th class="num">Verification</th></tr></thead>
    <tbody>
      <tr><td><code>calibration_constants.h</code></td><td class="num">4</td><td class="num">0</td></tr>
      <tr><td><code>calibration_demo.c</code></td><td class="num">1</td><td class="num">0</td></tr>
    </tbody>
  </table></div>
  <div class="note">Verifier finding: on both 2025.2 and 2026.1.3, Rule 7.5 flags the suffix and non-literal forms; the negative-in-macro form is accepted by the scanner. The zero gate therefore covers the suffix and non-literal classes, while the v1 script also normalizes negatives as value-preserving cleanup. Dashboard adapted from the ESL ThreadX LoongArch64 compliance dashboard format.</div>
</div></section>''')

# 15 — Whole repo baseline
S.append(f'''<section class="slide prompt"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Scaling up · 18</div>
  <h1>The same loop on upstream code: 1,095 findings</h1>
  <p class="subtitle">Full amalgamation, 7,438 lines, no seed involved, MISRA C 2025 config, 2026.1.3</p>
''' + shot('parasoft_baseline_seed_top.png', 'Whole-repo baseline: 1,095 findings, 0 suppressed, 1,472 per 10,000 lines', ratio=RP, w=1000) + '''
  <div class="tablewrap"><table>
    <thead><tr><th>Rule</th><th class="num">Findings</th><th>Nature</th><th>Mechanical?</th></tr></thead>
    <tbody>
      <tr><td>Rule 15.5 (single point of exit)</td><td class="num">383</td><td>structural rewrites</td><td>no</td></tr>
      <tr><td>Rule 15.6 (bodies must be blocks)</td><td class="num">82</td><td><strong>all 82 are assert-expansion artifacts</strong></td><td>yes, one macro</td></tr>
      <tr><td>Dir 4.6 (stdint typedefs)</td><td class="num">68</td><td>type-word rewrites</td><td>yes</td></tr>
      <tr><td>Rules 14.4 / 12.3 / 21.8 / 2.2 / 11.11</td><td class="num">251</td><td>mixed; 12.3, 21.8, 2.2 are largely assert artifacts</td><td>partly</td></tr>
    </tbody>
  </table></div>
</div></section>''')

# 16 — assert experiments
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Experiments · 19</div>
  <h1>Three micro-scans to find the fix that actually zeroes 123 findings</h1>
  <p class="subtitle">All 82 Rule 15.6 and 41 Rule 21.8 findings trace to one macro: <code>#define UDS_ASSERT(x) assert(x)</code>, because glibc's assert expands to an unbraced <code>if</code></p>
  <div class="tablewrap"><table>
    <thead><tr><th>Variant</th><th>Macro</th><th class="num">15.6</th><th class="num">21.8</th><th>Verdict</th></tr></thead>
    <tbody>
      <tr><td>A (as shipped)</td><td><code>#define UDS_ASSERT(x) assert(x)</code></td><td class="num">2 / site</td><td class="num">1 / site</td><td>the 123-finding source</td></tr>
      <tr><td>B (wrap only)</td><td><code>do { assert(x); } while (0)</code></td><td class="num">2 / site</td><td class="num">1 / site</td><td>does not help: glibc's assert still leaks the unbraced if</td></tr>
      <tr><td>C (hook)</td><td><code>do { if (!(x)) { UDS_AssertFail(); } } while (0)</code></td><td class="num">0</td><td class="num">0</td><td><strong>clean</strong></td></tr>
      <tr><td>D (abort)</td><td>hook calling <code>abort()</code></td><td class="num">0</td><td class="num">1 / site</td><td>Rule 21.8 covers abort too: "The 'abort' library function should not be used"</td></tr>
    </tbody>
  </table></div>
  <div class="note">Each micro-variant was verified with its own Parasoft scan on a small fixture, because a full amalgamation scan costs 15-20 minutes: cheap experiments first, one expensive verification last. The final fix keeps a fault hook (an application-replaceable spin function), not abort, preserving fail-loud semantics the embedded way.</div>
</div></section>''')

# 17 — rule-assert
S.append(f'''<section class="slide prompt"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Batch fix 1 of 3 · 20</div>
  <h1><code>video/rule-assert</code>: one macro rewrite, 123 findings gone</h1>
  <p class="subtitle">Commit <code>2ed57bf9</code>, stackable and revertable; the header gained a <code>UDS_AssertFail</code> hook any application can override</p>
<div class="diagram">- #define UDS_ASSERT(x) assert(x)
+ #define UDS_ASSERT(x)  do {{ if (!(x)) {{ UDS_AssertFail(); }} }} while (0)
+ static void UDS_AssertFail(void) {{ for (;;) {{ }} }}  /* replace with your fault handler */</div>
''' + shot('tenant-assert-before.png', 'Before-state on the tenant: 58 UDS_ASSERT call sites on the demo branch; the fix needs no call-site changes', ratio=R, w=900) + '''
</div></section>''')

# 18 — dir-4-6
S.append(f'''<section class="slide wide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Batch fix 2 of 3 · 21</div>
  <h1>Branch <code>video/dir-4-6</code>: comment-aware type rewriting, 88 search hits to 17</h1>
  <p class="subtitle">Commit <code>2524ee36</code>, script <code>tools/dir46_typedefs.py</code>: int&rarr;int32_t, unsigned&rarr;uint32_t, short&rarr;int16_t, long&rarr;int64_t, with <code>long long</code>, comments, and strings handled</p>
  <div class="shotrow tall">
''' + shot('tenant-dir46-before.png', 'Before (demo branch): 88 bare-type hits in the amalgamation', ratio=R) + shot('tenant-dir46-after.png', 'After (video/dir-4-6): 17 hits, all in comments and build files; the verifier reports 0 Dir 4.6 findings', ratio=R) + '''
  </div>
  <div class="note">Compile-verified after the rewrite: type-preserving on targets where int is 32 bits and long is 64 bits.</div>
</div></section>''')

# 19 — rule-14-4
S.append(f'''<section class="slide wide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Batch fix 3 of 3 · 22</div>
  <h1>Branch <code>video/rule-14-4</code>: 34 implicit zero tests made explicit</h1>
  <p class="subtitle">Commits <code>3bbda370</code> + <code>7d1ce9ae</code>, script <code>tools/rule144_explicit_zero.py</code>; <code>!= 0</code> is value-preserving for integer, enum, and pointer operands (0 is a null pointer constant)</p>
<div class="diagram">if (ret)          ->  if (ret != 0)          while (link->busy)  ->  while (link->busy != 0)
UDS_ASSERT(src)   ->  UDS_ASSERT(src != 0)
/* left alone: */ if (a == b)   if (x && y)   while (p->next != NULL)</div>
  <div class="shotrow tall">
''' + shot('tenant-rule144-before.png', 'Before (video/dir-4-6): 36 bare if/while/UDS_ASSERT conditionals', ratio=R) + shot('tenant-rule144-after.png', 'After (video/rule-14-4): 1 hit, the macro definition line itself', ratio=R) + '''
  </div>
</div></section>''')

# 20 — verification 766 (report)
S.append(f'''<section class="slide prompt"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Verification · 23</div>
  <h1>The loop closes at repo scale: 1,095 &rarr; 766</h1>
  <p class="subtitle">One verification scan on the tip branch (<code>video/rule-14-4</code>), same config, 7,456 lines, 0 suppressed</p>
''' + shot('parasoft_verify_full_top.png', 'Verification report: 766 total findings, severity 2 down 467 to 246, severity 4 down 241 to 133, severity 1 unchanged at 4', ratio=RP, w=1434) + f'''
  <div class="grid3">
    <div class="card v"><div class="n">-329</div><div class="l">findings removed by three batch fixes, verified in one scan</div></div>
    <div class="card"><div class="n">5 classes at 0</div><div class="l">Rules 15.6, 21.8, 12.3, 2.2 and Dir 4.6 all reach zero</div></div>
    <div class="card v"><div class="n">9 left</div><div class="l">Rule 14.4 residuals routed to expert review, exactly like the seed exclusions</div></div>
  </div>
</div></section>''')

# 21 — full before/after table
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Verification · 24</div>
  <h1>Per-rule evidence: where the 329 findings went</h1>
  <p class="subtitle">Extracted from the Parasoft XML reports of both scans, not from the HTML rendering</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Rule</th><th class="num">Before</th><th class="num">After</th><th class="num">Delta</th><th>Why</th></tr></thead>
    <tbody>
      <tr><td>Rule 15.6 (assert artifact)</td><td class="num">82</td><td class="num">0</td><td class="num">-82</td><td>UDS_ASSERT block-form macro (slide 17)</td></tr>
      <tr><td>Dir 4.6 (stdint typedefs)</td><td class="num">68</td><td class="num">0</td><td class="num">-68</td><td>type rewrites (slide 18)</td></tr>
      <tr><td>Rule 21.8 (assert/abort)</td><td class="num">41</td><td class="num">0</td><td class="num">-41</td><td>no assert, no abort: hook instead</td></tr>
      <tr><td>Rule 12.3 + Rule 2.2 (assert artifacts)</td><td class="num">81</td><td class="num">0</td><td class="num">-81</td><td>side-effect and dead-code findings lived inside the assert expansion</td></tr>
      <tr><td>Rule 14.4 (explicit zero tests)</td><td class="num">43</td><td class="num">9</td><td class="num">-34</td><td>34 sites made explicit; 9 residuals to expert review</td></tr>
      <tr><td>Rule 11.11 (typedefs removed casts)</td><td class="num">45</td><td class="num">7</td><td class="num">-38</td><td>side effect of the Dir 4.6 typedefs</td></tr>
      <tr><td><strong>Total</strong></td><td class="num"><strong>1,095</strong></td><td class="num"><strong>766</strong></td><td class="num"><strong>-329</strong></td><td></td></tr>
    </tbody>
  </table></div>
  <div class="note">What remains is the honest part: Rule 15.5 single-exit (383) is a structural rewrite program, Rule 4.4 commented-out code (45) and Rule 5.2 shadowing (29) need human judgment. That is the next loop iteration, script v2 onwards.</div>
</div></section>''')

# 22 — revertability
S.append(f'''<section class="slide prompt"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Revertability · 25</div>
  <h1>One commit per branch: reversal is one command</h1>
  <p class="subtitle">No fix ever lands on a shared branch; the upstream repo is never touched</p>
<div class="diagram">misra-rule-7-5-seed   3d3f7ab9  pinned before-state (never moves)
       │
misra-rule-7-5-demo   0fc00476  v1 script + fixes     2c1f7403  expert fixes (pilot: 8 -> 0)
       │
video/rule-assert     2ed57bf9  assert macro fix      (-123 findings)
       │
video/dir-4-6         2524ee36  stdint typedefs       (-68 findings)
       │
video/rule-14-4       3bbda370  fix script            7d1ce9ae  explicit zero tests (-34)
revert one step: git revert 7d1ce9ae          one rule: git reset --hard 3bbda370 && git push --force-with-lease
delete the whole campaign: git push fork --delete video/rule-14-4</div>
''' + shot('gh-fork-branches.png', 'The fork branch list after the campaign: each branch independently revertable', ratio=R, w=1200) + '''
</div></section>''')

# 23 — agentic + connectors
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Agentic path · 26</div>
  <h1>Agentic Batch Changes: licensed on the tenant, quota-gated today</h1>
  <p class="subtitle">The 2026-11-02 Sourcegraph update (agentic batch changes + MCP connectors) mapped onto this program</p>
  <div class="grid2">
    <div class="card"><span class="tag">Verified on the tenant</span><h3>The full agent API exists</h3><p>GraphQL exposes <code>createBatchChangeAgent</code>, <code>createBatchChangeAgentThread</code>, <code>submitBatchChangeAgentThreadMessage</code>, and tool-approval mutations. The feature is licensed; a prepared agent prompt is ready to run.</p></div>
    <div class="card v"><span class="tag">Current blocker</span><h3>Deep Search quota</h3><p><code>createBatchChangeAgent</code> fails with <code>"Deep Search quota exceeded"</code>. Agent runs consume Deep Search quota, which the tenant plan has exhausted. Until it clears, the recorded demo uses local batch scripts + branch publishing.</p></div>
  </div>
  <div class="grid2">
    <div class="card"><span class="tag">Connectors (MCP)</span><h3>What they add to this loop</h3><p>The agent can pull CI state (Buildkite, GitHub checks) into its own loop, plus ticket and docs context. The human keeps the draft-first review gate.</p></div>
    <div class="card v"><span class="tag">What does not change</span><h3>Parasoft stays the evidence of record</h3><p>Whatever drives the edits (script, agent, or IDE), the decision point remains the Parasoft verification scan; Sourcegraph still owns find, fix-at-scale, and the hold-zero guard.</p></div>
  </div>
</div></section>''')

# 24 — hold zero + timeline
S.append('''<section class="slide tall"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Hold zero · 27</div>
  <h1>Holding zero: detect with Sourcegraph, enforce on the code host</h1>
  <p class="subtitle">Sourcegraph does not natively block PRs; it respects the code host's merge gates. The gate is therefore two parts: Sourcegraph detects, GitHub/GitLab enforces.</p>
  <div class="flow">
    <div class="step"><b>1</b><strong>PR guard as a required check</strong><span>A CI job runs the combined guard query per PR via the search API or src-cli and exits non-zero on any match; the code host registers it as a required status check. Proof 1 executed on the tenant: 0 on cleaned, 11 on seed, under 1s per query.</span></div>
    <div class="step"><b>2</b><strong>Parasoft in the pipeline</strong><span>Every merged change runs the verification scan; the report is the release evidence.</span></div>
    <div class="step"><b>3</b><strong>Code Monitor safety net</strong><span>Queries run over future code changes and notify by email, Slack, or webhook (open a ticket, trigger the re-scan), covering branches the PR gate does not.</span></div>
  </div>
  <div class="tablewrap"><table>
    <thead><tr><th>Week</th><th>Milestone</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>1</td><td>Pilot: seed module baseline 8, scripts v1, tenant queries, zero certified</td><td><strong>executed 2026-11-04/06, seed-to-zero under one day</strong></td></tr>
      <tr><td>2-3</td><td>Scale: whole-repo campaign, three mechanical classes zeroed (1,095 to 766)</td><td><strong>executed 2026-11-06</strong></td></tr>
      <tr><td>4+</td><td>Standing gate: guard query in CI, Parasoft scan in pipeline, Code Monitor live</td><td>design fixed, Proof 1 done; wiring scheduled</td></tr>
    </tbody>
  </table></div>
</div></section>''')

# 25 — Contact
S.append('''<section class="slide"><div class="inner">
  <div class="eyebrow"><span class="mark"></span>Thank you · 28</div>
  <h1>Run the same loop on your code base</h1>
  <p class="subtitle">With Sourcegraph Code Monitor you can review new violations as they appear, and Batch Changes reverts them just as fast: seed it, measure it with Parasoft, find it with Sourcegraph, fix it with a versioned script, verify zero, hold zero</p>
  <div class="brandrow">
    <div class="brandchip ps"><img src="../assets/parasoft-logo.png" alt="Parasoft"><span>Parasoft C/C++test</span></div>
    <div class="brandchip sg"><img src="../assets/SG-logo.png" alt="Sourcegraph"><span>Sourcegraph Cloud</span></div>
  </div>
  <div class="person-card">
    <img src="../assets/daniel-liezrowice.jpg" width="140" height="140" alt="Daniel Liezrowice">
    <div>
      <strong>Daniel Liezrowice</strong>
      <span>CTO, ESL - Engineering Software Lab</span>
      <p>ESL is an embedded software consultancy and Parasoft and Perforce partner in Israel for over 20 years. This demonstration used only open-source code, a Sourcegraph Cloud trial tenant, and Parasoft C/C++test Standard 2026.1.3.</p>
    </div>
  </div>
  <div class="contact">
    <img src="../assets/esl-logo.png" alt="ESL - Engineering Software Lab">
    <p><a href="https://eswlab.com/" target="_blank" rel="noopener">eswlab.com</a> · <a href="https://eswlab.com/contact-us/" target="_blank" rel="noopener">Contact ESL</a> · Watch the recorded demo (2 min 55 s): <a href="https://www.youtube.com/watch?v=ZNPqVLcTY6A" target="_blank" rel="noopener">youtube.com/watch?v=ZNPqVLcTY6A</a> &middot; Companion brief: <a href="https://zuwasi.github.io/Public-html-pages/parasoft-cuda-bridge/technical/" target="_blank" rel="noopener">Parasoft CUDA Bridge</a></p>
  </div>
  <div class="foot">All measurements from 3-7 November 2026. Sources: Parasoft C/C++test HTML/XML reports (1,095 / 766 / 8 / 0), the eswlab.sourcegraphcloud.com tenant (all query counts), and the git history of github.com/zuwasi/iso14229.</div>
</div></section>''')

BODY = '<main class="viewport" aria-label="MISRA C 2025 Rule 7.5 zero program presentation">\n<div id="track">\n' + '\n\n'.join(S) + '\n</div>\n</main>\n'

EXTRA_STYLE = '''<style>
.step span{color:#4a443a}
.slide{padding-top:calc(var(--top) + 12px);padding-bottom:50px}
h1{margin:8px 0 6px}
p.subtitle{margin-bottom:12px}
.brandrow{display:flex;gap:14px;margin:0 0 14px;flex-wrap:wrap;align-items:center}
.brandchip{display:flex;align-items:center;gap:10px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:7px 14px;box-shadow:0 1px 4px rgba(20,30,50,.06)}
.brandchip img{height:27px;width:auto;display:block}
.brandchip.sg{background:#0a0a0a;border-color:#0a0a0a}
.brandchip.sg img{height:22px}
.brandchip span{font-size:clamp(13px,1.2vw,16px);font-weight:600;color:var(--ink)}
.brandchip.sg span{color:#fff}
.cardlogo{float:right;height:26px;width:auto;margin:0 0 6px 10px}
.fchart{margin:8px 0 0}
.fchart svg{width:auto;max-width:100%;height:auto;max-height:518px;margin:0 auto;display:block}
p,li{line-height:1.42}
.diagram{line-height:1.42;font-size:clamp(11px,1.08vw,14.5px);padding:12px 18px;margin:10px 0 0}
table{font-size:clamp(13px,1.22vw,16px)}
th,td{padding:8px 12px}
.card{padding:12px 16px}
.card p,.card li{font-size:clamp(13px,1.18vw,16px);line-height:1.4}
.grid2,.grid3,.grid4{gap:16px;margin:10px 0}
.note{padding:10px 16px;margin:10px 0 0;font-size:clamp(13px,1.2vw,16px);line-height:1.42}
.n{font-size:clamp(24px,2.6vw,38px)}
.shotrow{margin-top:10px;gap:22px}
.foot{margin-top:12px;font-size:clamp(12px,1.05vw,14px)}
</style>'''
OUT = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<meta name="theme-color" content="#e2e5ea">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; base-uri 'none'; form-action 'none'; object-src 'none'; img-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; connect-src 'self' https://fonts.googleapis.com https://fonts.gstatic.com; script-src 'unsafe-inline'">
<meta name="description" content="ESL technical brief: the MISRA C:2025 Rule 7.5 zero program on driftregion/iso14229, a measured Sourcegraph + Parasoft closed loop, from an 8-finding seeded pilot to zero, then scaled to 1,095 whole-repo findings with three mechanical batch fixes.">
<title>MISRA C:2025 Rule 7.5 Zero Program | Sourcegraph + Parasoft | ESL</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
{style}
{EXTRA_STYLE}
</head>
<body>
<header class="topbar">
  <div class="brand">
    <a class="homebtn" href="#1" title="Back to slide 1" aria-label="Back to slide 1">&#127968;</a>
    <a href="https://eswlab.com/" target="_blank" rel="noopener"><img src="../assets/esl-logo.png" alt="ESL - Engineering Software Lab"></a>
    <span id="brand">MISRA C:2025 Rule 7.5 Zero Program · Sourcegraph + Parasoft</span>
  </div>
  <nav class="links" aria-label="Related links">
    <a href="https://eswlab.sourcegraphcloud.com/search" target="_blank" rel="noopener">eswlab tenant</a>
    <a href="https://eswlab.com/" target="_blank" rel="noopener">eswlab.com</a>
    <a href="https://eswlab.com/contact-us/" target="_blank" rel="noopener">Contact ESL</a>
  </nav>
</header>
{BODY}{tail}
{script}
</body>
</html>
'''

open('/mnt/c/Users/danie/Public-html-pages/misra-rule-7-5-zero-program/technical/index.html', 'w').write(OUT)
print('written', len(OUT), 'bytes,', len(S), 'slides')
