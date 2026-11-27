# Week 15 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 15 materials"*.

## Planned checkpoints
1. Study the existing Balena reels pipeline (hash cache, ElevenLabs TTS, FFmpeg) in the YoutubeCreator repo, read-only.
2. Create a Remotion composition that takes caption JSON as props.
3. Wire n8n: script → Gateway → ElevenLabs (cached) → ComfyUI → Remotion render → approval queue.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Remotion render is slow on the Intel Mac: render drafts at lower resolution; use concurrency 2.
- Thai words mispronounced: use a pronunciation dictionary or phonetic respelling in the script.
