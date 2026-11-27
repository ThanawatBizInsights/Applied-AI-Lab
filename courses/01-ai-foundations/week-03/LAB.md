# Week 03 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 03 materials"*.

## Planned checkpoints
1. Write three versions of the Balena caption prompt; score 10 outputs each against the brand checks from Week 1.
2. Define a JSON Schema for a caption (`headline_th`, `body_th`, `hashtags`, `cta`) and validate model outputs with pydantic.
3. Send a packaging photo and ask for a structured description; compare it with the approved product reference.
4. Start EXP-01: build a 30-item Thai test set (synthetic) with expected answers.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Model wraps JSON in Markdown fences: strip them before parsing, then fix the prompt.
- Thai text turns into `\u0e01` escapes: use `ensure_ascii=False` when writing JSON.
- Image too large: resize to ≤ 1568 px on the long side before sending.
