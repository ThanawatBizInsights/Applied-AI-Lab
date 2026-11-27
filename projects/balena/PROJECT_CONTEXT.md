# Balena Roastery — Project context

Status tags: **[VERIFIED]** read from the repository · **[USER-PROVIDED]** from the learner's
brief · **[PROPOSED]** learning work, not an existing feature · **[NEEDS CONFIRMATION]**.
Verified on 2026-11-27 by read-only inspection. No changes were made to any project repository.

## Repositories
| Repository | Visibility | Commit inspected | Last commit date |
|---|---|---|---|
| `ThanawatBizInsights/Balena` | public | `18bed5e` | 2026-10-15 |
| `ThanawatBizInsights/YoutubeCreator` | public | `737b8ca` | 2026-11-23 |

## [VERIFIED] What the repository shows
- `Balena` repo: a mobile-first Thai recipe page for **Balena Cold Brew Concentrate Original 500 mL**, opened from a LINE OA rich-menu button, with four recipes, each with a 14-second Remotion animation.
- `Balena` stack: React 19, TypeScript, Vite, Remotion Player 4.0.534, Playwright page checks, Vercel config. Includes an internal cost calculator with tests (`src/cost/calc.ts`).
- `YoutubeCreator/balena`: a reusable pipeline for Balena's Thai educational Reels: JSON episode configs, a content-hash cache for narration, an ElevenLabs TTS script (only generates missing lines), Whisper-based Thai alignment for QC, and an FFmpeg renderer. Source footage is kept out of Git.
- `YoutubeCreator/drink`: a Remotion composition for an iced-coffee how-to video, music-only.

## [USER-PROVIDED] Focus and constraints
- Focus: ComfyUI image and video generation; character LoRA; mascot identity consistency; product photography and packaging accuracy; automated Thai marketing content; Remotion and ElevenLabs integration; social media production automation.

## [PROPOSED] Role in this curriculum
- W1: brand-aware caption assistant (fake provider)
- W3: structured Thai post generator
- W9–11: parameter study, packaging composites, Balena LoRA
- W15: Balena Content Factory v0.1 with approval gate
- W22: Balena request flows end-to-end through the Studio OS

## [NEEDS CONFIRMATION]
- Full list of approved product SKUs and packaging reference files (where they are stored).
- Whether a ComfyUI or LoRA setup already exists outside GitHub.
- Social channels in scope (LINE OA, Facebook, Instagram, TikTok?).

## Decisions log
| Date | Decision | Why | Who |
|---|---|---|---|
| | | | |
