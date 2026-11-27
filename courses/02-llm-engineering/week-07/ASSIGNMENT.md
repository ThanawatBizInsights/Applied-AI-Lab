# Week 07 — Assignment (3 hours): Knowledge Engine v0.1 with EXP-02 report (course main project)

**Linked projects:** [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md)

## Brief
Package the RAG work into `shared/knowledge-engine` v0.1 with hybrid retrieval, reranking, citations and per-project data isolation, then complete EXP-02.

## Deliverables
- `shared/knowledge-engine/` package with a project-scoped index
- EXP-02 report in `evaluations/reports/`
- Row-level security or separate schemas showing project isolation

## Acceptance criteria
- [ ] Hybrid retrieval improves recall@5 over dense-only, or the report explains why not
- [ ] Faithfulness measured with a stated method, and the judge spot-checked by hand (≥ 20 items)
- [ ] CheckKhum and Billionslight data cannot be retrieved across projects (test proves it)
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- recall@5
- Faithfulness
- Citation accuracy
- Latency added by the reranker
- RAG vs no-RAG correctness delta

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Full-text search finds nothing in Thai: Postgres has no Thai dictionary; pre-segment text and store tokens.
- Reranker too slow on CPU: rerank only the top 20 candidates.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
