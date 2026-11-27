# Week 20 — Assignment (3 hours): Rusty privacy-preserving personalisation engine + agent evaluation

**Linked projects:** [Rusty App](../../../projects/rusty/README.md), [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md)

## Brief
Build a recommendation prototype for Rusty's supportive messages using synthetic activity data, where the model sees only minimised, aggregated features. Run EXP-06 and EXP-07 and report the results.

## Deliverables
- Synthetic data generator + personalisation prototype
- Guardrail test suite (medical-advice refusals, tone, data minimisation)
- EXP-06 and EXP-07 reports

## Acceptance criteria
- [ ] No real health data; no diagnostic or medical recommendations (tests enforce it)
- [ ] Feature minimisation documented: what is sent, what stays on device
- [ ] Multi-agent vs single-agent compared on the same tasks and budget
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Personalisation quality rating
- Data fields sent off-device
- Guardrail pass rate
- Task success and cost (EXP-06)

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Multi-agent costs explode: share state and cap rounds; compare at equal budgets.
- Guardrail false positives: measure them; tune on a held-out set, not the test set.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
