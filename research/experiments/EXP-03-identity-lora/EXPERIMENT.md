# EXP-03 — Character identity consistency with and without LoRA

**Status:** DESIGN (not started) · **Weeks:** 11–12 · **Projects:** [Balena Roastery](../../../projects/balena/README.md), [Little Snowy Owl Studio — Animal Pairs](../../../projects/animal-pairs/README.md), [Seoa Ryn](../../../projects/seoa/README.md), [LumiTale Studio](../../../projects/lumitale/README.md)

## 1. Research question
How much does a character LoRA improve identity consistency and constraint compliance compared with prompt-plus-reference conditioning alone?

## 2. Hypothesis
H1: The LoRA condition raises mean identity similarity and the rubric pass rate, and halves constraint violations (e.g. Balena with legs). H0: no improvement over reference conditioning.

## 3. Literature and references
- Hu, E. et al. (2021). *LoRA*. arXiv:2106.09685
- Ruiz, N. et al. (2023). *DreamBooth*. arXiv:2208.12242
- Ye, H. et al. (2023). *IP-Adapter*. arXiv:2308.06721
- Oquab, M. et al. (2023). *DINOv2*. arXiv:2304.07193

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** Same prompts (30) and seeds (5 each); Same sampler/steps/CFG; Pinned checkpoint hash.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
Same base checkpoint with prompt + reference-image conditioning (no LoRA).

## 6. Variables
**Independent:**
- Condition: prompt only / prompt + reference / LoRA / LoRA + reference
- LoRA strength (0.6, 0.8, 1.0)

**Dependent:**
- Identity similarity (DINOv2 or face-embedding cosine)
- Rubric pass rate
- Constraint violation rate
- Prompt adherence
- GPU seconds per image

## 7. Evaluation metrics
- Mean similarity ± SD
- Rubric pass rate
- Violation rate
- Correlation between metric and human ratings (Spearman ρ)

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
Owned or licensed reference images only; prompts covering 10 scenes × 3 poses. Generated images are stored outside Git; only metrics are committed.

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
