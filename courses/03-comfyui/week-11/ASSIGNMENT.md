# Week 11 — Assignment (3 hours): Character LoRA with measured identity consistency

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [Little Snowy Owl Studio — Animal Pairs](../../../projects/animal-pairs/README.md), [Seoa Ryn](../../../projects/seoa/README.md)

## Brief
Train one character LoRA (Balena, an Animal Pairs character, or Seoa Ryn) and run EXP-03 to measure identity consistency against a prompt-plus-reference baseline.

## Deliverables
- Dataset card and caption files (images stored outside Git if not yours to publish)
- Training config with pinned versions
- EXP-03 results and report

## Acceptance criteria
- [ ] LoRA weights not committed
- [ ] Baseline and LoRA conditions use the same prompts and seeds
- [ ] Similarity metric validated against human ratings on ≥ 30 images
- [ ] Licence and consent status recorded for every training image
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Mean identity similarity
- Rubric pass rate
- Constraint violation rate (e.g. legs)
- Training cost

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- LoRA copies backgrounds: increase dataset variety; caption the backgrounds.
- Identity drifts at low weights and burns at high weights: sweep the LoRA strength from 0.4 to 1.0.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
