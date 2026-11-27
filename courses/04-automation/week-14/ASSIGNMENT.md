# Week 14 — Assignment (3 hours): Footage organiser and enquiry intake

**Linked projects:** [Iris's Family](../../../projects/iris-family/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md)

## Brief
Build two workflows: (1) an Iris's Family footage organiser that files new Drive uploads by date and type and writes metadata only (no footage leaves Drive, nothing goes to Git); (2) a CheckKhum synthetic enquiry intake from webhook to Supabase with validation.

## Deliverables
- Two workflow JSON exports (scrubbed)
- Supabase migration with RLS policies
- Threat model notes: what data each workflow can access

## Acceptance criteria
- [ ] Drive scope is the narrowest that works; justified in writing
- [ ] No children's footage, names or locations in logs, Git or LLM prompts
- [ ] Webhook rejects unsigned or replayed requests (tested)
- [ ] Only synthetic enquiries used
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Files organised correctly (%)
- Rejected bad requests (%)
- Minutes saved per week

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- OAuth redirect mismatch: the callback URL must match exactly, including the trailing slash.
- RLS blocks inserts: the policy needs `with check`, not only `using`.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
