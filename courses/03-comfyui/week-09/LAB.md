# Week 09 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 09 materials"*.

## Planned checkpoints
1. Set up ComfyUI on a cloud GPU; build a text-to-image workflow without templates.
2. Run a 5×5 grid over CFG and steps with a fixed seed for a Balena scene.
3. Encode and decode a Balena reference image through the VAE and inspect the loss of detail.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Black images: VAE precision issue; try the fp32 VAE.
- Results differ with the same seed: check sampler determinism and GPU settings.
- Do not install ComfyUI with GPU dependencies on the Intel Mac.
