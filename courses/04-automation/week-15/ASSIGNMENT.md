# Week 15 — Assignment (3 hours): Balena Content Factory v0.1 (course main project)

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [Iris's Family](../../../projects/iris-family/README.md)

## Brief
Build an automated pipeline that turns one approved Thai script into a vertical Balena reel draft (images, narration, captions, music bed), stopping at a human approval step before anything is published.

## Deliverables
- n8n workflow + Remotion composition + pipeline README
- Content-hash cache for TTS and images
- EXP-04 results: time, cost and quality vs your manual process

## Acceptance criteria
- [ ] Nothing is published automatically; approval step is mandatory
- [ ] Re-running with the same script costs zero new TTS credits
- [ ] Balena brand checks run on every generated image
- [ ] No rendered videos committed to Git
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Production minutes per reel
- Cost per reel
- Brand-check pass rate
- Human quality rating

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Remotion render is slow on the Intel Mac: render drafts at lower resolution; use concurrency 2.
- Thai words mispronounced: use a pronunciation dictionary or phonetic respelling in the script.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
