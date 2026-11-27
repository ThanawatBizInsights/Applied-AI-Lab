# EXP-07 — Privacy-preserving AI personalisation

**Status:** DESIGN (not started) · **Weeks:** 20 · **Projects:** [Rusty App](../../../projects/rusty/README.md)

## 1. Research question
How much personalisation quality is lost when the model receives only minimised, aggregated features instead of detailed activity history?

## 2. Hypothesis
H1: Aggregated features keep ≥ 90% of the perceived quality of detailed-history personalisation while sending ≥ 80% fewer data fields off-device. H0: quality loss > 10%.

## 3. Literature and references
- Dwork, C. & Roth, A. (2014). *The Algorithmic Foundations of Differential Privacy*
- McMahan, B. et al. (2017). *Communication-Efficient Learning of Deep Networks from Decentralized Data*. arXiv:1602.05629

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** Same synthetic personas (20); Same model; Blind rating.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
Detailed synthetic activity history sent to the model (an upper bound used only with synthetic data).

## 6. Variables
**Independent:**
- Data exposure: detailed / aggregated / on-device rules only

**Dependent:**
- Message appropriateness rating
- Personalisation relevance rating
- Data fields sent
- Guardrail violations

## 7. Evaluation metrics
- Mean ratings
- Fields sent per request
- Guardrail violation rate (target 0)

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
Synthetic personas and activity data from a seeded generator. No real health data. No medical advice.

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
