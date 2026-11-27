# EXP-01 — Thai-language LLM accuracy and cost benchmarking

**Status:** DESIGN (not started) · **Weeks:** 3–4 · **Projects:** [Balena Roastery](../../../projects/balena/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md)

## 1. Research question
For Thai-language business tasks (caption writing, customer replies, technical Q&A), how do current frontier and small models compare in accuracy, brand-rule compliance, latency and cost?

## 2. Hypothesis
H1: A small model with a well-designed prompt reaches ≥ 90% of the best frontier model's accuracy on Thai customer-reply tasks at ≤ 20% of the cost. H0: the accuracy gap is larger than 10%.

## 3. Literature and references
- Zheng, L. et al. (2023). *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. arXiv:2306.05685
- Liang, P. et al. (2022). *Holistic Evaluation of Language Models (HELM)*. arXiv:2211.09110
- Pipatanakul, K. et al. (2023). *Typhoon: Thai Large Language Models*. arXiv:2312.13951

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** Same 60-item test set; Temperature fixed; 3 runs per item; Same date window.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
Best-scoring frontier model with the same prompt (upper bound), plus a fixed template response (lower bound).

## 6. Variables
**Independent:**
- Model (3–5 models across providers)
- Prompt version (v1, v2)

**Dependent:**
- Task accuracy (rubric 0–3)
- Brand-rule violations
- Latency (s)
- Cost per item (USD)
- Thai fluency rating (1–5)

## 7. Evaluation metrics
- Mean rubric score ± SD
- Violation rate
- p50/p95 latency
- USD per 100 items
- Inter-rater agreement (Cohen's κ) on a 20% double-scored sample

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
60 synthetic Thai items: 20 Balena captions, 20 CheckKhum customer replies (synthetic enquiries), 20 Billionslight technical questions with reference answers.

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
