# Sourcegraph + Parasoft: MISRA C 2025 Rule 7.5 Zero Program

The working material for the ESL zero-program demonstration on `driftregion/iso14229`:
Sourcegraph finds, Parasoft decides, versioned scripts fix at scale, everything revertable.

## Published artifacts (public)

| Artifact | URL |
|---|---|
| Technical brief, 28 slides | https://zuwasi.github.io/Public-html-pages/misra-rule-7-5-zero-program/technical/index.html |
| Demo video (2:47, narrated, subtitled) | https://www.youtube.com/watch?v=StzLdcFgW-E |
| YouTube thumbnail | `esl-video-rule75/output/youtube-thumbnail.jpg` |
| Transcript | `esl-video-rule75/transcript.md` |
| Demo repository (public fork) | https://github.com/zuwasi/iso14229 |

The old plan deck (`misra-rule-7-5-sourcegraph-plan`) was retired on 2026-11-07; its
workflow slide (slide 4), Parasoft-in-the-loop slide (9), and pilot dashboard (10) were
merged into the technical brief as slides 3, 16 and 17. Git history of the
Public-html-pages repository preserves the original.

## Layout

| Path | What it is |
|---|---|
| `iso14229/` | The demo repository clone (own git, remote = the GitHub fork). **Gitignored here**: it is its own repository. Branches: `misra-rule-7-5-seed`, `misra-rule-7-5-demo`, `video/rule-assert`, `video/dir-4-6`, `video/rule-14-4` |
| `esl-video-rule75/` | The ESL demo video project (storyboard, config, voice mp3/srt, clips, output) |
| `deck/` | The generator for the published technical brief (`build_deck.py`) plus the overflow checker and screenshot helpers |
| `docs/` | The esl-demo-video skill reference and project notes |

## Measured results (all verified)

- Seed pilot: 8 violations -> 0 (Parasoft C/C++test 2026.1.3, `builtin://MISRA C 2025`, gcc_12-64; same verdict on 2025.2)
- Whole repository: 1,095 -> 766 (-329) in one verification scan
- Rules 15.6 (82->0), 21.8 (41->0), Dir 4.6 (68->0), 12.3, 2.2 at zero; Rule 14.4 43->9, residuals to expert review
- Guard query: `repo:zuwasi/iso14229@BRANCH fork:yes lang:C patternType:regexp (INT32_C|INT64_C|UINT32_C|UINT64_C)\(\s*(-\s*[0-9]+[uUlL]*|0[xX][0-9a-fA-F]+\s*[uUlL]+|[0-9]+\s*[uUlL]+|[A-Za-z_][A-Za-z0-9_]*)\s*\)`

## Rebuild commands

Deck (writes the published HTML):
```
python3 deck/build_deck.py   # expects the reference template pieces under /tmp; see script header
node deck/check_deck.js      # per-slide overflow check at 1600x900
```

Video:
```
python3 /path/to/esl-demo-video/scripts/build.py --project esl-video-rule75 all
```

## Gotchas that cost real time

- The DTP license server has `start_deactivated=true`: after a server restart, re-activate it in the legacy `/pst` console.
- After a Windows reboot the three Parasoft services must be started (elevated `net start`) before `cpptestcli` licenses.
- A full-amalgamation scan takes 15-20 minutes regardless of file count (Flow Analysis + Global phases dominate).
- Sourcegraph: `fork:yes` is mandatory for forked repos; `patternType:regexp` is opt-in; Zoekt cannot use negated character classes.
- Branch refresh on the tenant: GraphQL `refreshRepository(repository:"UmVwb3NpdG9yeToxODk=")`, then wait for the mirror sync.

## Secrets

None in this repository. The Sourcegraph token and the DTP connection settings
(`cpptest_local.properties`) live outside it, in the Amp thread workspace `.amp/in/`.
