# Week 12 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 12 materials"*.

## Planned checkpoints
1. Turn a 6-shot LumiTale storyboard into image-to-video clips.
2. Write a Python client that submits a workflow JSON to the ComfyUI API and waits for the result.
3. Batch-render 10 Phonics Pond illustration variants from a CSV manifest.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- WebSocket disconnects: poll `/history/{prompt_id}` as a fallback.
- Flicker between frames: reduce motion strength; use the same seed and LoRA weight.
