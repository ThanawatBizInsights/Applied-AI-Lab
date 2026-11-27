# Week 04 — Tool calling, model routing, benchmarking and evaluation

Course 01 — AI Engineering Foundations · **10 hours** · Linked projects: [Balena Roastery](../../../projects/balena/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md), [Billionslight](../../../projects/billionslight/README.md)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 04 materials"*.

## Prerequisites
- Week 3 structured outputs
- API keys for at least two providers (approved budget)

## Time plan
| Activity | Hours | File |
|---|---:|---|
| Theoretical instruction | 2 | [`LECTURE.md`](LECTURE.md) |
| Guided laboratory | 2 | [`LAB.md`](LAB.md) |
| Independent project development | 3 | [`ASSIGNMENT.md`](ASSIGNMENT.md) |
| Research reading | 1 | [`RESEARCH_READING.md`](RESEARCH_READING.md) |
| Assessment | 1 | [`QUIZ.md`](QUIZ.md) |
| Documentation and reflection | 1 | [`REFLECTION.md`](REFLECTION.md) |
| **Total** | **10** | |

## Assignment at a glance
**Multi-model AI Gateway v0.1 (course main project)** — Build `shared/llm-gateway` v0.1: a Python package with a unified interface over at least two providers plus the fake provider, tool calling, routing rules, cost logging and a benchmark CLI. This becomes the first module of the capstone.

## Hardware and cost
Local CPU. Paid API calls for EXP-01: estimated USD 3–8 depending on models. Approval needed.

**Research strand:** this week contributes to [EXP-01](../../../research/experiments/README.md).

## Completion evidence (AGENTS.md §5)
- [ ] Assignment tests pass (`uv run pytest -m assignment courses/01-ai-foundations/week-04`)
- [ ] Acceptance criteria checked off in `ASSIGNMENT.md`
- [ ] Quiz score recorded in `PROGRESS.md`
- [ ] `REFLECTION.md` written in your own words
- [ ] Review saved in `reviews/`
- [ ] Study hours logged in `learning-journal/`
