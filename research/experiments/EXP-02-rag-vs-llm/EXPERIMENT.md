# EXP-02 — RAG versus standard LLM responses

**Status:** DESIGN (not started) · **Weeks:** 6–7 · **Projects:** [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md)

## 1. Research question
Does retrieval-augmented generation over verified documents improve correctness and reduce unsupported claims compared with the same model answering without retrieval?

## 2. Hypothesis
H1: RAG increases correctness by ≥ 20 percentage points and reduces unsupported claims by ≥ 50% on document-specific questions. H0: no meaningful difference.

## 3. Literature and references
- Lewis, P. et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. arXiv:2005.11401
- Es, S. et al. (2023). *RAGAS*. arXiv:2309.15217
- Liu, N. F. et al. (2023). *Lost in the Middle*. arXiv:2307.03172

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** Same model version; Same questions; Fixed temperature; Same graders, blinded to condition.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
Same model and prompt without retrieved context ('closed-book').

## 6. Variables
**Independent:**
- Condition: closed-book / dense RAG / hybrid RAG + reranker

**Dependent:**
- Correctness (human-graded)
- Unsupported-claim count
- Citation precision
- Refusal accuracy on unanswerable questions
- Cost and latency

## 7. Evaluation metrics
- Correctness rate
- Unsupported claims per answer
- Citation precision
- Refusal accuracy
- Paired difference with bootstrap 95% CI

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
40 CheckKhum questions over public Thai policy wording + 40 Billionslight questions over public datasheets; 20% unanswerable by design.

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
