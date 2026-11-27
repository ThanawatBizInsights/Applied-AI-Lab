# Week 18 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 18 materials"*.

## Planned checkpoints
1. Write a 60-line agent loop from scratch (no framework) with two tools and a step budget.
2. Rebuild it in LangGraph with a checkpointer and a human approval interrupt.
3. Point it at a read-only copy of the Animal Pairs Swift package to summarise test coverage.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Agent loops on the same tool: add the tool history to state and a repeated-call detector.
- Swift tests cannot run on Linux CI for UIKit code: run only the platform-independent package tests.
