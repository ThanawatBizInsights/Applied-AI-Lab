# Week 22 — Assignment (3 hours): Personal AI Studio OS — integrated MVP

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [LumiTale Studio](../../../projects/lumitale/README.md), [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md)

## Brief
Integrate Gateway, Knowledge Engine, ComfyUI client, brand service and n8n behind the Studio API, so that one Balena content request flows end-to-end to an approval queue.

## Deliverables
- Job queue + status endpoints
- Brand/context service backed by `projects/*/BRAND_GUIDELINES.md` data
- Architecture diagram and updated ADRs

## Acceptance criteria
- [ ] End-to-end demo runs from one command using fake providers (offline)
- [ ] Each project's data and credentials isolated
- [ ] Every job has cost and provenance recorded
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- End-to-end success rate
- Cost per request
- Mean job time

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Jobs stuck in 'running': add heartbeats and timeouts; requeue on worker crash.
- Circular dependencies between services: n8n calls the API; the API never calls n8n synchronously.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
