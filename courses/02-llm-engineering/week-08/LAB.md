# Week 08 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 08 materials"*.

## Planned checkpoints
1. Prepare 300–500 synthetic instruction pairs for Billionslight technical Q&A (style and format, not facts).
2. Run a QLoRA fine-tune of a small open model on a cloud GPU notebook.
3. Compare base, fine-tuned and base+RAG on the Week 7 evaluation set.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Out of memory: reduce sequence length or batch size; enable gradient checkpointing.
- bitsandbytes does not run on Intel Mac: do all training on the cloud GPU, never locally.
- Loss falls but answers get worse: overfitting; evaluate on held-out data every N steps.
