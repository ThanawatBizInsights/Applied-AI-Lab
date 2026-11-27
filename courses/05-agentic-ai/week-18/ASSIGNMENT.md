# Week 18 — Assignment (3 hours): AI Software Development Agent v0.1 (code-review assistant)

**Linked projects:** [Little Snowy Owl Studio — Animal Pairs](../../../projects/animal-pairs/README.md), [Rusty App](../../../projects/rusty/README.md)

## Brief
Build an agent that reads a pull-request diff from a local clone of Animal Pairs or Rusty, runs the Swift package tests where possible, and writes a structured review. It proposes changes but never pushes.

## Deliverables
- Agent code with tools: read_file, list_files, run_tests (sandboxed), write_review
- 10 historical diffs with your own reviews as ground truth
- EXP-06 baseline run (single agent)

## Acceptance criteria
- [ ] Agent has no write access to any production repository
- [ ] Step and cost budgets enforced; runs stop cleanly
- [ ] Review findings scored against your labels
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Finding precision/recall vs your reviews
- Steps per review
- Cost per review

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Agent loops on the same tool: add the tool history to state and a repeated-call detector.
- Swift tests cannot run on Linux CI for UIKit code: run only the platform-independent package tests.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
