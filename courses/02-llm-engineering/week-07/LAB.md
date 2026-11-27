# Week 07 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 07 materials"*.

## Planned checkpoints
1. Add Postgres full-text search (with a Thai segmentation step) alongside pgvector.
2. Implement RRF and measure recall@5 before and after.
3. Add a reranker and measure the latency cost.
4. Run EXP-02 on both CheckKhum and Billionslight question sets.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Full-text search finds nothing in Thai: Postgres has no Thai dictionary; pre-segment text and store tokens.
- Reranker too slow on CPU: rerank only the top 20 candidates.
