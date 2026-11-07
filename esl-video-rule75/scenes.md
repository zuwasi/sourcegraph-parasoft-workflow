# Demo storyboard: The Rule 7.5 Zero Program - Sourcegraph finds, Parasoft decides

Single source of truth for the whole video (see the esl-demo-video skill's SKILL.md):
the narration column drives the voice, the voice timing drives the subtitles, and this file
plus `transcript.md` are the .md deliverables at the end. Voice: `en-GB-RyanNeural`.

Demo project: `zuwasi/iso14229` (fork of driftregion/iso14229, upstream never touched).
Every number on screen was measured; every recording is the real eswlab tenant, the real
GitHub fork, or the real Parasoft C/C++test reports.

| # | Headline (what you'll see) | Action recorded on screen | What it achieves | Narration (read by the voice) | Target sec |
|---|----------------------------|---------------------------|------------------|-------------------------------|------------|
| 01 | Title | Title card | Sets the goal | The Rule 7.5 Zero Program. Sourcegraph finds, Parasoft decides. In about three minutes, we take a real C code base from one thousand and ninety five MISRA C 2025 findings to a verified, revertable zero. | 12 |
| 02 | The problem | ESL slide | Frame the problem | iso14229 is a real open source diagnostic protocol stack. About seven and a half thousand lines of C. A full MISRA C 2025 scan reports one thousand and ninety five findings, and every one of them needs a decision. Nobody clicks through a thousand rows by hand. | 15 |
| 03 | Find: one query, all candidates | Live Sourcegraph query on the eswlab tenant, seed branch | Locate every Rule 7.5 candidate | The pilot starts with one rule. MISRA C 2025 Rule 7.5 bans suffixes and minus signs inside INT N C macros. One Sourcegraph query finds every candidate in the seed module. Eleven results, in about a tenth of a second. | 15 |
| 04 | Fix: a versioned script | GitHub file view of tools/rule75_v1.py on the fork | Show the fix is repeatable | The fix is a versioned script, not a one off patch. Two value preserving transforms: strip the suffix, and move the minus sign outside the macro. Two edge cases are excluded and routed to an expert. The values are identical before and after. | 16 |
| 05 | Prove the fix: zero results | Live Sourcegraph query on the demo branch | Search proves the fix | After the fix, the same guard query returns zero. Even the script's own documentation cannot fool the search. | 10 |
| 06 | Parasoft decides | Parasoft verification report, seed module | Judge, not guess | Parasoft C/C++test is the judge. The seed verification scan reports zero findings left, while the baseline had eight. Search found the sites; Parasoft decided. | 13 |
| 07 | Scale up: the whole repository | Parasoft baseline report, whole repository | Show the real numbers | Now scale up. The whole repository, no seed involved. One thousand and ninety five findings. The biggest mechanical classes are assert macro artifacts, implicit integer tests, and missing unsigned suffixes. | 14 |
| 08 | One commit per branch | GitHub fork branch list | Show revertability | Each fix is one commit on its own stacked branch. The assert macro rewrite removes one hundred and twenty three findings. Unsigned typedefs remove sixty eight. Explicit comparisons remove thirty four. Reversing any step is one git command. | 16 |
| 09 | One scan confirms it | Parasoft verification report, whole repository | Prove the total | One verification scan confirms it. One thousand and ninety five becomes seven hundred and sixty six. Three hundred and twenty nine findings removed by mechanical rewrites, and five rule classes now sit at zero. | 14 |
| 10 | Holding zero | ESL slide | Keep it at zero | Holding zero. Sourcegraph detects, and the code host enforces. The same query runs on every pull request in under a second. Parasoft runs in the pipeline. Code Monitor watches for regressions. | 15 |
| 11 | End | End card | Close | The Rule 7.5 Zero Program, by Engineering Software Lab. Thank you for watching. | 7 |

Rules: one idea per scene, short spoken sentences, narration roughly as long as the recording
(trim happens in phase 4, never stretch).
