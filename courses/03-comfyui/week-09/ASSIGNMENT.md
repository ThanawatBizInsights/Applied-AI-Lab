# Week 09 — Assignment (3 hours): Balena generation parameter study

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md)

## Brief
Run a controlled study of how sampler, steps and CFG affect Balena mascot fidelity (round whale body, no legs, coffee cup, water splash, white striped belly, pink cheeks), scored against a written rubric.

## Deliverables
- Workflow JSON in `shared/comfyui-workflows/balena/` (no output images committed)
- Rubric-scored results CSV
- Short report with 1 contact sheet (≤ 1 MB, deliberately added)

## Acceptance criteria
- [ ] Every image reproducible from the recorded settings
- [ ] Rubric covers all six Balena identity constraints
- [ ] Leg-presence failure rate reported for each setting
- [ ] Checkpoint licence recorded
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Identity-rubric score (0–6)
- Leg-violation rate
- Seconds per image
- GPU cost per 100 images

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Black images: VAE precision issue; try the fp32 VAE.
- Results differ with the same seed: check sampler determinism and GPU settings.
- Do not install ComfyUI with GPU dependencies on the Intel Mac.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
