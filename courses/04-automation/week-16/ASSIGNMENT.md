# Week 16 — Assignment (3 hours): CheckKhum renewal reminder and quotation-prep workflow (synthetic data)

**Linked projects:** [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md)

## Brief
Build a workflow that finds synthetic policies due for renewal, drafts a reminder and a quotation-preparation checklist with the Gateway, and queues them for staff approval. Nothing reaches a customer without approval.

## Deliverables
- Workflow JSON + Supabase tables for queue and audit log
- Failure-injection test script and results
- Runbook: what to do when the workflow fails

## Acceptance criteria
- [ ] 100% of outbound messages pass through approval (test proves it)
- [ ] Duplicate runs do not send duplicate reminders
- [ ] Audit log records who approved what and when
- [ ] Synthetic data only; generator script included
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Lost/duplicated jobs under failure injection (target 0)
- Mean time to recovery
- Staff minutes per renewal

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Approval links can be forwarded: sign them, expire them and bind them to a staff identity.
- Retry storms: cap attempts and add jitter.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
