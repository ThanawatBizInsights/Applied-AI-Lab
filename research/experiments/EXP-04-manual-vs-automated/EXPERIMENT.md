# EXP-04 — Manual versus automated content production

**Status:** DESIGN (not started) · **Weeks:** 15–16 · **Projects:** [Balena Roastery](../../../projects/balena/README.md), [Iris's Family](../../../projects/iris-family/README.md), [CheePao](../../../projects/cheepao/README.md)

## 1. Research question
Does the automated content pipeline reduce production time and cost per asset without lowering quality, once review and correction time are included?

## 2. Hypothesis
H1: Total time per reel falls by ≥ 50% with equal or better quality ratings. H0: time savings disappear once review and fixes are counted, or quality drops.

## 3. Literature and references
- Brynjolfsson, E., Li, D. & Raymond, L. (2023). *Generative AI at Work*. NBER WP 31161
- Noy, S. & Zhang, W. (2023). *Experimental evidence on the productivity effects of generative AI*. Science 381(6654)

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** Same 6–10 briefs; Alternate order to reduce learning effects; Blind quality rating.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
Learner's current manual process, timed on the same briefs.

## 6. Variables
**Independent:**
- Production method: manual / automated + human review

**Dependent:**
- Total minutes (creation + review + fixes)
- Direct cost (API, GPU, credits)
- Quality rating (blind, 1–5)
- Brand-check pass rate
- Revisions needed

## 7. Evaluation metrics
- Median minutes per asset
- Cost per asset
- Mean blind quality rating
- Wilcoxon signed-rank test on paired times

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
6–10 Balena reel briefs (and optional CheePao digests). No private footage of children.

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
