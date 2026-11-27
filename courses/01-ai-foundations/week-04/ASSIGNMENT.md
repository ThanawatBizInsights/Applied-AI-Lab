# Week 04 — Assignment (3 hours): Multi-model AI Gateway v0.1 (course main project)

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md)

## Brief
Build `shared/llm-gateway` v0.1: a Python package with a unified interface over at least two providers plus the fake provider, tool calling, routing rules, cost logging and a benchmark CLI. This becomes the first module of the capstone.

## Deliverables
- `shared/llm-gateway/` package with adapters, router, usage log (JSONL)
- Benchmark CLI and EXP-01 results in `research/experiments/EXP-01-thai-llm-benchmark/`
- ADR in `ARCHITECTURE.md` explaining the gateway interface

## Acceptance criteria
- [ ] All tests pass offline using the fake provider (no network in CI)
- [ ] Every request logs provider, model, tokens, latency and estimated cost
- [ ] Router chooses a model by rule and the choice is explained in the log
- [ ] EXP-01 report states model versions, dates, n, mean and spread for each metric
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Accuracy on the Thai test set
- USD per 100 requests
- p50/p95 latency
- Tool-call success rate

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- 429 rate limit: back off with jitter; lower concurrency to 1 during benchmarks.
- Different providers return different usage fields: normalise them in each adapter, not in the caller.
- Benchmark results vary between runs: run ≥ 3 times and report spread, not a single number.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
