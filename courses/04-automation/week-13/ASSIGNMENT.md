# Week 13 — Assignment (3 hours): CheePao product research digest

**Linked projects:** [CheePao](../../../projects/cheepao/README.md)

## Brief
Build an n8n workflow that collects public product information for a chosen category, scores products against criteria, calls the LLM Gateway for a Thai comparison summary and saves a digest, so you can compare it with your manual process.

## Deliverables
- Workflow JSON in `shared/automation/n8n/cheepao/`
- Scoring criteria documented
- Time log: manual vs automated (EXP-08 baseline)

## Acceptance criteria
- [ ] Respects source terms of service and robots rules; uses official APIs or feeds where available
- [ ] No credentials in exported JSON (validator passes)
- [ ] Affiliate disclosure text included in any generated content
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Minutes saved per digest
- Digest error count (manual check)
- Cost per digest

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Data lost after restart: mount `/home/node/.n8n` to a volume.
- Expression returns undefined: check item pairing; use `$json` from the right node.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
