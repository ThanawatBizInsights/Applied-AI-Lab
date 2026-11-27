# Week 21 — Assignment (3 hours): Personal AI Studio OS — API service MVP

**Linked projects:** [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md), [Balena Roastery](../../../projects/balena/README.md)

## Brief
Create `capstone/studio-api`: a FastAPI service exposing the Gateway and Knowledge Engine with project-scoped auth, containerised, with CI running tests on every push.

## Deliverables
- FastAPI app, Dockerfile, docker-compose for local dev
- GitHub Actions workflow running tests
- Deployment plan (staging only) awaiting approval

## Acceptance criteria
- [ ] No secrets baked into images; config from environment
- [ ] Project A's key cannot read project B's data (tests)
- [ ] OpenAPI schema generated and documented
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Image size
- p95 latency (local)
- Test coverage
- Auth test pass rate

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Docker image is huge: multi-stage build; slim base; no build tools in the final stage.
- Async endpoint blocks: you are calling a sync client inside `async def`.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
