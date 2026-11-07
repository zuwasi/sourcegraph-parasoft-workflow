---
name: esl-demo-video
description: Produce a narrated, subtitled demo video in the Engineering Software Lab (ESL) brand for any product or project (web app, desktop app, IDE extension, CLI tool, embedded or hardware setup, service, or concept walkthrough). Records the real product, adds ESL title and end cards, ESL concept slides, the ESL logo and www.eswlab.com, a neural voiceover, burned-in subtitles, a YouTube cover picture and a Markdown transcript. Use when asked for an ESL demo video, screencast, walkthrough, tutorial video or YouTube video.
---

# ESL demo video

A repeatable way to make a 1-3 minute, 1920x1080 narrated demo video for **any** ESL project.
The subject changes; the method, the identity and the tools stay the same:

storyboard → voice → real recording per scene → cuts and masks → build → quality check → deliver

Output: `output/<name>.mp4` (H.264/AAC, burned-in subtitles), `output/youtube-thumbnail.jpg`
(1280x720), `transcript.md`, plus the editable storyboard and config. `SKILL_DIR` below is
the folder that contains this file.

## Principles

1. **Show the real thing.** Every result on screen happened: real app, real data from a
   demo account or sample project, real edits, real output. Never mock results, draw fake UI
   states, or invent numbers. If a step cannot be recorded, use an honest ESL slide instead.
2. **Narration is the spine.** Write the storyboard first. The voice fixes each scene's
   length; the recording is cut to the voice, never stretched or sped up.
3. **One idea per scene.** 8 to 12 scenes, 5 to 15 seconds each, about 150 spoken words
   per minute. Short sentences, plain words, no dashes.
4. **Every claim is true and visible.** Check technical claims against the product's own
   documentation, and state honest limits on screen (for example "host code coverage only;
   kernels are not instrumented"). Prefer a precise claim to an impressive one.
5. **Readable on a phone.** Zoom the UI (about 150%), hide the mouse pointer, hold 2 to 3 s
   after each change, keep key content above the bottom 150 px where subtitles sit.
6. **Private by default.** Record only the app region. Hide chat or AI panes, notifications,
   other tabs and windows. Mask user names, avatars, e-mail addresses, tokens, customer data.
7. **ESL identity, every time.** Title card, end card and slides come from the brand kit,
   unchanged. Do not hand-draw cards.
8. **Local until asked.** Do not upload, publish or push unless the user asks.

## ESL identity (do not change without approval)

- Logo `assets/esl-logo.jpeg`, always placed with multiply blending (`esl_brand.logo`) so its
  white background takes the card color. Never as a white box.
- Logo colors: blue `#4c9bf5`, amber `#fbb20f`. Text: headline `#172d3b`, accent `#2f7fd8`
  (taglines, website), muted `#415763`. Card background cream `#f6f3ea`. Blue and amber
  stripe on the left edge of every card.
- `www.eswlab.com` on the title card, the end card (large), every slide and the cover picture.
- Name: "Engineering Software Lab" (ESL). Contact: sales@eswlab.com.
- Fonts: Segoe UI (falls back to Arial or DejaVu Sans). Subtitles: Segoe UI 36, white on a
  dark box, bottom centre.
- Default voice `en-GB-RyanNeural`. Others: `en-US-AndrewNeural`, `en-US-AvaNeural`,
  `he-IL-AvriNeural`, `he-IL-HilaNeural` (list all with `edge-tts --list-voices`).

## Requirements

Python 3 with `pillow` and `edge-tts` (`pip install pillow edge-tts`), and `ffmpeg`/`ffprobe`
on PATH. For web recordings also `pip install playwright` and `python -m playwright install chromium`.

## Workflow

### 0. Plan with the user

Agree on: audience (customer, partner, internal), the one outcome the viewer should
remember, the product version, what may be shown (demo data, no customer data), voice and
language, and target length. Pick a pattern:

| Pattern | Scene outline |
|---|---|
| Problem to solution | title, the pain (slide), starting state, 2-4 steps, proven result, end |
| Find, fix, verify (tools for analysis, testing, security) | title, project, run tool, findings, fix, rerun clean, extra evidence (tests, report), end |
| Feature walkthrough | title, context, one scene per feature (3-5), summary slide, end |
| Before and after | title, old way (recording or slide), new way, side-by-side result or numbers, end |
| Setup or install tutorial | title, prerequisites slide, each install step, first successful run, end |
| Architecture or concept | title, 3-6 slides with diagrams or screenshots, one live proof scene, end |

### 1. Storyboard (`scenes.md`)

Copy `SKILL_DIR/templates/*` into a new project folder and create `clips/`. Fill the table:
headline, action on screen, what it achieves, narration, target seconds. Scene 01 is the
title card; the last scene is the end card ("<Product>, by Engineering Software Lab. Thank you
for watching."). Keep the column headers; the build reads the column whose header starts
with "Narration". Fill `video.json`: output name, voice, card, slide and cover text.

### 2. Voice and subtitles

```powershell
python SKILL_DIR\scripts\build.py --project . voices          # all scenes
python SKILL_DIR\scripts\build.py --project . voices 04 07    # redo some
```

Listen to every mp3. Fix mispronounced names with `spoken` pairs in `video.json`
(written text, how to say it), for example `["C/C++test", "C, C plus plus test"]`,
`["GPU", "G P U"]`, `["eswlab", "E S W lab"]`. The voice reads the spoken form; subtitles keep
the written form. Now each scene's length is known.

### 3. Scene visuals, one per scene

Each scene is one of:

- **Recording**: `clips/sceneNN.mp4`, `.webm`, `.mov`, `.mkv` or `.avi`, any size (fitted to
  1920x1080 without distortion). Record at least 1 s longer than the narration.
- **Still**: `clips/sceneNN.png` or `.jpg`, shown for the length of the narration.
  Good for a final report, a diagram, a photo of hardware.
- **ESL slide**: listed under `slides` in `video.json` (kicker, 1-2 headline lines, up to
  5 bullets); generated by the build. Use for context, problems, summaries, honest limits.
- **Title and end cards**: generated from `title_card` and `end_card`.

Capture recipes, by target:

| Target | How to record | Notes |
|---|---|---|
| Web app | `examples/web-playwright/recorder.py` (Playwright, 1920x1080, CSS zoom 150%, event log) | Fresh browser profile, demo account; `page.screenshot(full_page=True)` for stills |
| Windows desktop app or IDE | `ffmpeg -f gdigrab` on the app window region, driven by UI Automation; `examples/visual-studio/` | DPI aware: on 150% DPI place the window at 2560x1440 physical and scale to 1920x1080 |
| Terminal or CLI | Record the terminal window region with gdigrab (font 20 pt or more, 120x34), or asciinema then `agg` to gif, then ffmpeg to mp4 | Type commands with pauses; clear secrets from history and environment |
| macOS / Linux desktop | `ffmpeg -f avfoundation` (macOS) or `-f x11grab` (Linux) on the window region | Same rules for region, zoom, pointer |
| Android device | `scrcpy --record sceneNN.mp4` | Do Not Disturb on, demo account |
| Hardware, lab bench, board | Phone or camera video, landscape, tripod, steady light | Pair with a screen recording of the host tool in the next scene |
| Slides or diagrams | ESL `slides`, or a still exported from the diagram tool | No other branding on ESL slides |

Recording rules:

- Automate the actions (Playwright, UI Automation, DTE, scripted shell) so takes repeat
  exactly, and log every action with seconds since recording start (`events.tsv`). The
  timings drive the cuts. Grab a proof screenshot per scene and look at it before moving on.
- Start 2-3 s before the action, hold 2-3 s after each state change. Record long waits
  (builds, scans) in full and cut them later.
- Hide the pointer (`-draw_mouse 0`) or move it deliberately; never leave it over content.
- Stop the recording before closing the app, so the desktop never appears.
- Leave unrelated warnings visible (do not hide reality); explain them with a note if they
  could confuse.

### 4. Cuts, masks and notes (`edits.json`)

Per scene, all optional:

- `start`: skip the first seconds.
- `segments`: `[[from, to], ...]` of the clip to keep, in order; removes waits.
- `masks`: `[{"x","y","w","h","color","from","to"}]` boxes on the 1920x1080 frame over
  personal data. Global masks (for example an avatar in every frame) go in `video.json`
  `masks`, with `except` listing card and slide scenes.
- `notes`: `[{"text","from","to"}]` a small caption at the top of the frame.
- `fade_out`: true on the last recorded scene.

### 5. Build

```powershell
python SKILL_DIR\scripts\build.py --project . all
```

This renders the cards and slides, fits every clip to 1920x1080, burns subtitles, masks and
notes, trims each scene to its narration, normalizes loudness to -16 LUFS, joins the scenes,
and writes the cover picture, `output/scene-durations.json` and `transcript.md`. A scene with
less video than narration stops the build: record a longer take or keep more segments.
Rebuild one scene with `build.py --project . scenes 06`, then `build.py --project . concat`.

### 6. Quality check (required before reporting)

- `ffprobe` the result: 1920x1080, h264 and aac, yuv420p, expected duration, under 50 MB.
- Extract one frame per scene (by time, with `ffmpeg -ss <t>`) and look at each: text
  readable, subtitles not covering key content, masks in place, no personal data, no
  desktop or unrelated windows, cards and slides with logo and website.
- Read `transcript.md` against the screen: every sentence matches what is shown.
- Watch it once at 1x and once muted (the subtitles must carry it). Ask the user to watch it
  before publishing. Report the checks you did and did not do.

### 7. Deliver

Give absolute paths to the video, cover picture and transcript. For YouTube, the user uploads
at https://www.youtube.com/upload and sets the cover under Details, Thumbnail (phone
verification at https://www.youtube.com/verify may be needed). Suggested description end:
`Learn more: https://www.eswlab.com` and `Contact: sales@eswlab.com`. If the video goes into a
repository, keep raw clips only if asked; they are large and may show unmasked data.

## Files

| Path | Purpose |
|---|---|
| `assets/esl-logo.jpeg` | Official ESL logo |
| `scripts/esl_brand.py` | Colors, fonts, logo blending, title card, end card, slide, cover picture |
| `scripts/build.py` | `voices`, `cards`, `scenes`, `concat`, `thumbnail`, `all` |
| `scripts/make_voice.py` | edge-tts mp3 + srt for one scene (forces IPv4, retries 5 times) |
| `templates/` | Starting `scenes.md`, `video.json`, `edits.json` |
| `examples/web-playwright/` | Browser recorder, sample app and a complete small demo (title, slide, recording, still, end) |
| `examples/visual-studio/` | Windows desktop and IDE automation and region recording (PowerShell) |
| `examples/parasoft-cuda-bridge/` | An approved 2:10 customer demo: storyboard, config and cuts |
