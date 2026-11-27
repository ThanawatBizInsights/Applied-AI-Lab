# Week 17 — Assignment (3 hours): Phonics content validator assistant (development-side only)

**Linked projects:** [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md), [Billionslight](../../../projects/billionslight/README.md)

## Brief
Combine Phonics Pond's existing rule-based validator (`tools/validate_content.py`) with an LLM reviewer that flags non-decodable words, unintroduced tricky words and illustration mismatches in draft storybooks. The deterministic validator stays the authority; the LLM only adds suggestions.

## Deliverables
- Reviewer script that runs offline on stored drafts
- EXP-05 plan and a first run on 30 synthetic draft pages
- Report comparing rule-based vs LLM findings

## Acceptance criteria
- [ ] AI never generates content that ships to children without human review
- [ ] Rule-based checker remains the source of truth; disagreements are logged
- [ ] Precision and recall of LLM flags measured against expert (your) labels
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Flag precision
- Flag recall
- Cost per storybook
- Reasoning-model cost premium

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- The LLM invents phonics rules: give it the curriculum JSON as context and require it to cite the level.
- Reasoning model too slow or expensive: use it only on pages the rule checker cannot decide.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
