# Week 13 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 13 materials"*.

## Planned checkpoints
1. Run n8n with Docker Compose and a mounted volume.
2. Build a schedule-triggered workflow that fetches public product data and normalises it.
3. Export the workflow JSON and check that no credentials are in it.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Data lost after restart: mount `/home/node/.n8n` to a volume.
- Expression returns undefined: check item pairing; use `$json` from the right node.
