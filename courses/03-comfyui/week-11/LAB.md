# Week 11 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 11 materials"*.

## Planned checkpoints
1. Prepare a 20–40 image Balena dataset with captions that never mention legs.
2. Train a LoRA on a cloud GPU; save checkpoints at 3 step counts.
3. Score 50 images per checkpoint with DINOv2 similarity and the Balena rubric.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- LoRA copies backgrounds: increase dataset variety; caption the backgrounds.
- Identity drifts at low weights and burns at high weights: sweep the LoRA strength from 0.4 to 1.0.
