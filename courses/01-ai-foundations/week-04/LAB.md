# Week 04 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 04 materials"*.

## Planned checkpoints
1. Implement a `currency_convert` and `product_lookup` tool and run a tool-calling loop on one provider.
2. Write adapters for two providers behind one `Gateway.complete()` interface.
3. Run the EXP-01 test set across 3+ models, 3 runs each; save results as CSV.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- 429 rate limit: back off with jitter; lower concurrency to 1 during benchmarks.
- Different providers return different usage fields: normalise them in each adapter, not in the caller.
- Benchmark results vary between runs: run ≥ 3 times and report spread, not a single number.
