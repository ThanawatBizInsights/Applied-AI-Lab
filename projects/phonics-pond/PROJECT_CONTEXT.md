# Little Snowy Owl Studio — Phonics Pond — Project context

Status tags: **[VERIFIED]** read from the repository · **[USER-PROVIDED]** from the learner's
brief · **[PROPOSED]** learning work, not an existing feature · **[NEEDS CONFIRMATION]**.
Verified on 2026-11-27 by read-only inspection. No changes were made to any project repository.

## Repositories
| Repository | Visibility | Commit inspected | Last commit date |
|---|---|---|---|
| `ThanawatBizInsights/phonics` | public | `3b51495` | 2026-11-25 |

## [VERIFIED] What the repository shows
- An Xcode project `PhonicsPond` with app, unit-test and UI-test targets.
- Curriculum data in `Resources/Content/curriculum.json` and `lesson_level1.json`.
- `tools/validate_content.py` checks without Xcode that every reading word's graphemes are taught at or before its level, that sentence tokens are readable or introduced tricky words, that the audio IDs match the manifest, and that referenced artwork exists.
- Other tools: `build_curriculum.py`, `build_storybooks.py`, `build_audio_manifest.py`, `audio_review.py`; an audio generation log is kept in `docs/audio-review/`.

## [USER-PROVIDED] Focus and constraints
- Focus: AI-assisted educational content development; systematic phonics curriculum validation; storybook generation; decodable word verification; character consistency; automated illustration and audio production; educational content evaluation.
- Constraint: preserve the offline, child-friendly nature of the app. AI supports development and never interacts with children directly.

## [PROPOSED] Role in this curriculum
- W12: batch illustration variants from a manifest
- W17: LLM reviewer alongside validate_content.py
- W19: read-only curriculum MCP server
- W20: guardrails that block non-decodable words

## [NEEDS CONFIRMATION]
- Which phonics programme or scope-and-sequence the curriculum follows.
- Target age range and market (UK, US, Thailand?).

## Decisions log
| Date | Decision | Why | Who |
|---|---|---|---|
| | | | |
