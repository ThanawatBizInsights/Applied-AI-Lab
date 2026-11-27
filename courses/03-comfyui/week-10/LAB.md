# Week 10 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 10 materials"*.

## Planned checkpoints
1. Generate Balena in 3 fixed poses using pose/edge ControlNet.
2. Use a reference adapter with Seoa Ryn reference images (owned or licensed) for a fashion shot.
3. Inpaint a product area and composite the approved packaging render instead of generating it.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Visible seams after inpainting: feather the mask and lower the denoise strength.
- ControlNet ignored: check the preprocessor and the strength and start/end percentages.
