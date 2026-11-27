# Week 06 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 06 materials"*.

## Planned checkpoints
1. Parse 5 public Thai insurance documents (e.g. standard policy wording published by the regulator or insurers) and inspect the output.
2. Implement two chunkers and compare retrieval recall on 20 questions.
3. Build `answer(question)` that cites chunk IDs and refuses when retrieval confidence is low.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Thai text from PDF is garbled: the PDF may use custom font encodings; try a different parser or OCR.
- Answers ignore context: put the context before the question and instruct the model to quote clause numbers.
- Chunks cut tables in half: use structure-aware chunking for tables.
