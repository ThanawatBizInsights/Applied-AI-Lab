# Week 23 — Assignment (3 hours): Hardening and cost report

**Linked projects:** [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md), [Balena Roastery](../../../projects/balena/README.md)

## Brief
Produce a security and cost hardening release of the Studio OS: threat model, red-team results, fixes, observability dashboards and a measured cost-optimisation report.

## Deliverables
- `SECURITY.md` threat model section updated
- Red-team test suite in `tests/` and results report
- Cost report with before/after numbers

## Acceptance criteria
- [ ] All OWASP LLM Top 10 items assessed (applicable or not, with reasons)
- [ ] No secrets or personal data in logs (automated check)
- [ ] Cost savings measured on the same workload, not estimated
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Red-team attack success rate (before/after)
- Cost per 100 requests (before/after)
- Evaluation regression pass rate

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Logs contain prompts with personal data: redact at the logging layer, not at each call site.
- Cache returns stale answers: include model, prompt version and data version in the key.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
