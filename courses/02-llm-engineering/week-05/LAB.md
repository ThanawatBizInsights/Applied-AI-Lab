# Week 05 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 05 materials"*.

## Planned checkpoints
1. Embed 200 Billionslight product descriptions (public catalogue text) with two models.
2. Load them into local Supabase/pgvector; compare brute force with an HNSW index on latency and recall.
3. Write 30 labelled queries (Thai and English) and compute recall@5 for each model.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- `type vector does not exist`: run `create extension if not exists vector;`
- Dimension mismatch: the column dimension must equal the model's output size.
- Docker on Intel Mac is slow: give it ≥ 4 GB RAM or use a free hosted Supabase project.
