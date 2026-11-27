# EXP-06 — Single-agent versus multi-agent performance

**Status:** DESIGN (not started) · **Weeks:** 18, 20 · **Projects:** [Little Snowy Owl Studio — Animal Pairs](../../../projects/animal-pairs/README.md), [Rusty App](../../../projects/rusty/README.md)

## 1. Research question
At an equal cost budget, does a multi-agent code-review system (planner, reviewer, tester) find more real issues than a single agent?

## 2. Hypothesis
H1: At equal token budget, the multi-agent system achieves higher finding recall with equal precision. H0: no gain at equal budget (gains come only from spending more).

## 3. Literature and references
- Yao, S. et al. (2023). *ReAct*. arXiv:2210.03629
- Wu, Q. et al. (2023). *AutoGen*. arXiv:2308.08155
- Jimenez, C. et al. (2024). *SWE-bench*. arXiv:2310.06770

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** Same 10 historical diffs; Same model; Same tools; 3 runs each.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
Single ReAct-style agent with the same tools and budget.

## 6. Variables
**Independent:**
- Architecture: single / multi-agent
- Budget: low / high

**Dependent:**
- Finding precision and recall vs learner's labels
- Tokens and cost
- Steps
- Task completion rate

## 7. Evaluation metrics
- Precision
- Recall
- Cost per review
- Recall per dollar

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
10 historical diffs from Animal Pairs/RustyKit (read-only local clones) with the learner's own reviews as ground truth.

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
