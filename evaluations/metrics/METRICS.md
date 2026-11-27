# Metric definitions

Define a metric once, here, and link to it from reports.

| Metric | Definition | Range | Used in |
|---|---|---|---|
| Violation rate | outputs with ≥ 1 error-severity brand violation ÷ all outputs | 0–1 (lower is better) | W1, W3, W9 |
| Checker precision | true violations flagged ÷ all flagged | 0–1 | W1 |
| Checker recall | true violations flagged ÷ all true violations | 0–1 | W1 |
| Schema validity rate | outputs parsing against the JSON Schema ÷ all outputs | 0–1 | W3 |
| Cost per 100 requests | Σ(input tokens × input price + output tokens × output price) ÷ requests × 100 | USD | W1, W4 |
| p50 / p95 latency | median / 95th percentile request time | seconds | W4, W21 |
| recall@k | relevant items in the top k ÷ all relevant items | 0–1 | W5, W7 |
| MRR | mean of 1 / rank of the first relevant result | 0–1 | W5, W7 |
| Faithfulness | claims supported by the retrieved context ÷ all claims | 0–1 | W7 |
| Citation precision | correct citations ÷ all citations | 0–1 | W6, W7 |
| Identity similarity | cosine similarity of image embeddings to the reference set | −1–1 | W11 |
| Cohen's κ | agreement between two raters, corrected for chance | −1–1 | EXP-01, EXP-03 |

Always report n, the model version and the date. For stochastic systems, report mean ± SD over ≥ 3 runs.
