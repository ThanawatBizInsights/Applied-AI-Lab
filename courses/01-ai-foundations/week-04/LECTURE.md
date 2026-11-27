# Week 04 — Lecture (2 hours): Tool calling, model routing, benchmarking and evaluation

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 04 materials"*.

Principles before tools. Planned sequence:

1. Tool calling: function schemas, the request/response loop, parallel calls
2. Adapter pattern: one interface, many providers
3. Reliability: timeouts, exponential backoff, idempotency, rate limits
4. Routing strategies: static rules, cascades, LLM-as-router
5. Evaluation: exact match, rubric scoring, LLM-as-judge and its biases
6. Benchmark hygiene: held-out sets, contamination, variance and repeated runs

Each section will include: the core idea, a worked example linked to [Balena Roastery](../../../projects/balena/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md),
a "predict before you run" question and a common misconception.
