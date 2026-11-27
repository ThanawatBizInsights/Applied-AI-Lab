# Week 23 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 23 materials"*.

## Planned checkpoints
1. Run a prompt-injection red-team against the CheckKhum RAG endpoint (synthetic data).
2. Add OpenTelemetry tracing around Gateway calls.
3. Add semantic or exact caching and measure the cost reduction on a replayed workload.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Logs contain prompts with personal data: redact at the logging layer, not at each call site.
- Cache returns stale answers: include model, prompt version and data version in the key.
