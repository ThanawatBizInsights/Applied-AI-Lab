# Week 05 — Assignment (3 hours): Billionslight semantic product search

**Linked projects:** [Billionslight](../../../projects/billionslight/README.md)

## Brief
Build a semantic search service over public Billionslight-style solar and electrical product data (inverters, panels, batteries, breakers) in pgvector, with an evaluation script and a model-choice report.

## Deliverables
- SQL migration for the `products` and `product_chunks` tables with a vector index
- Ingestion script and `search(query, k)` function
- Evaluation report: recall@5 and MRR for two embedding models

## Acceptance criteria
- [ ] Only public or synthetic product data; source of every record recorded
- [ ] Index type and parameters justified in writing
- [ ] Thai queries evaluated separately from English queries
- [ ] Search latency reported for 1k and 10k rows (synthetic scale-up)
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- recall@5
- MRR
- p95 query latency (ms)
- Embedding cost per 1k documents

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- `type vector does not exist`: run `create extension if not exists vector;`
- Dimension mismatch: the column dimension must equal the model's output size.
- Docker on Intel Mac is slow: give it ≥ 4 GB RAM or use a free hosted Supabase project.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
