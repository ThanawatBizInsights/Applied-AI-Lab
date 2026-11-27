# Week 06 — Assignment (3 hours): CheckKhum policy-wording RAG (public documents only)

**Linked projects:** [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md)

## Brief
Build a RAG pipeline over publicly available Thai motor and travel insurance wording, so CheckKhum staff can ask coverage questions and get answers with clause-level citations. No customer data.

## Deliverables
- Ingestion pipeline with document metadata (insurer, product, version, page)
- RAG `answer()` with citations and a refusal path
- A 40-question synthetic evaluation set with reference answers
- EXP-02 experiment plan filled in

## Acceptance criteria
- [ ] Every answer cites at least one source chunk, or refuses
- [ ] No document without a recorded public source URL is ingested
- [ ] Thai parsing issues documented with examples
- [ ] Pipeline runs end-to-end from a single command
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Answer correctness (human-graded, 40 questions)
- Citation precision
- Refusal accuracy on unanswerable questions

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Thai text from PDF is garbled: the PDF may use custom font encodings; try a different parser or OCR.
- Answers ignore context: put the context before the question and instruct the model to quote clause numbers.
- Chunks cut tables in half: use structure-aware chunking for tables.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
