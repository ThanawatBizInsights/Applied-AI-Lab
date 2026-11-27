# EXP-05 — Phonics curriculum compliance

**Status:** DESIGN (not started) · **Weeks:** 17, 20 · **Projects:** [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md)

## 1. Research question
Can an LLM reviewer, combined with the existing rule-based validator, detect phonics-curriculum violations in draft storybooks more completely than the validator alone, without too many false alarms?

## 2. Hypothesis
H1: Validator + LLM reviewer increases recall of seeded violations by ≥ 15 percentage points over the validator alone, at precision ≥ 0.8. H0: no recall gain, or precision < 0.8.

## 3. Literature and references
- Castles, A., Rastle, K. & Nation, K. (2018). *Ending the Reading Wars*. Psychological Science in the Public Interest 19(1)
- Ehri, L. C. (2005). *Learning to Read Words: Theory, Findings, and Issues*. Scientific Studies of Reading 9(2)

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** 30 synthetic draft pages with known seeded errors (non-decodable words, unintroduced tricky words, illustration mismatches); Expert labels by the learner.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
`tools/validate_content.py` alone (deterministic rules).

## 6. Variables
**Independent:**
- Checker: validator only / LLM only / validator + LLM
- Model: reasoning vs non-reasoning

**Dependent:**
- Recall of seeded violations
- Precision
- Cost per storybook
- Review minutes saved

## 7. Evaluation metrics
- Precision
- Recall
- F1
- Cost per page
- Violation types missed

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
Synthetic draft pages only. No child data. Nothing generated here ships without human review.

Use `templates/DATASET_CARD.md` for the dataset card.

## 10. Cost estimate (approve before running)
| Item | Quantity | Unit price (from provider page, date) | Estimate |
|---|---|---|---|
| | | | |

## 11. Results
Raw results: [`results.csv`](results.csv) (one row per observation). Summary: [`results.json`](results.json).

_Not yet run._

## 12. Limitations and threats to validity
_Fill in after the run: sample size, synthetic-data bias, grader bias, model version drift._

## 13. Reproducibility instructions
```bash
# Fill in: exact commands, seeds, config files, environment
```

## 14. Conclusions
_Only conclusions the data supports. State what the experiment does NOT show._
