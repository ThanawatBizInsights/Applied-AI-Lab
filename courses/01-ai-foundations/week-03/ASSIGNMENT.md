# Week 03 — Assignment (3 hours): Structured Thai content generator with prompt versioning

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [Billionslight](../../../projects/billionslight/README.md)

## Brief
Extend the Week 1 brand assistant so it returns validated JSON for Balena social posts and Billionslight product explainers, with prompts stored as versioned files and an evaluation script that compares prompt versions.

## Deliverables
- `prompts/<brand>/<task>/v1.md`, `v2.md` …
- pydantic models and a validate-and-retry loop (max 2 retries)
- `eval_prompts.py` that prints a comparison table

## Acceptance criteria
- [ ] ≥ 95% of outputs parse against the schema on a 20-item set
- [ ] Brand rule violations counted automatically and reported per prompt version
- [ ] Image-input path works for at least one product photo (public or own)
- [ ] Cost per run printed from token usage
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Schema validity rate
- Brand-rule violation rate
- Mean cost per output
- Human rating (1–5) on 10 samples

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Model wraps JSON in Markdown fences: strip them before parsing, then fix the prompt.
- Thai text turns into `\u0e01` escapes: use `ensure_ascii=False` when writing JSON.
- Image too large: resize to ≤ 1568 px on the long side before sending.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
