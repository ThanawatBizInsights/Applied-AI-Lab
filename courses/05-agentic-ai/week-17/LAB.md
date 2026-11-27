# Week 17 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 17 materials"*.

## Planned checkpoints
1. Compare a reasoning and a non-reasoning model on 20 decodability questions (is this word decodable at level N?).
2. Use a vision model to check Phonics Pond illustrations against a written scene spec.
3. Read two current model cards and list claims you could and could not verify.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- The LLM invents phonics rules: give it the curriculum JSON as context and require it to cite the level.
- Reasoning model too slow or expensive: use it only on pages the rule checker cannot decide.
