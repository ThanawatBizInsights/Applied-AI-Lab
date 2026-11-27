# Week 12 — Video generation, upscaling, batch processing and ComfyUI API

Course 03 — ComfyUI and Generative Media Engineering · **10 hours** · Linked projects: [LumiTale Studio](../../../projects/lumitale/README.md), [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md), [Balena Roastery](../../../projects/balena/README.md)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 12 materials"*.

## Prerequisites
- Week 11 LoRA
- Python HTTP and WebSocket basics (Week 1)

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
**ComfyUI batch client and storyboard-to-video pipeline (course main project)** — Build `shared/comfyui-workflows/client` (a Python ComfyUI API client) and a manifest-driven batch pipeline that turns a storyboard JSON into consistent images and short clips, logging cost and settings per asset.

## Hardware and cost
Cloud GPU (≈ 5–8 hours). Video is expensive: estimated USD 8–20. Approval needed.

**Research strand:** this week contributes to [EXP-03](../../../research/experiments/README.md).

## Completion evidence (AGENTS.md §5)
- [ ] Assignment tests pass (`uv run pytest -m assignment courses/03-comfyui/week-12`)
- [ ] Acceptance criteria checked off in `ASSIGNMENT.md`
- [ ] Quiz score recorded in `PROGRESS.md`
- [ ] `REFLECTION.md` written in your own words
- [ ] Review saved in `reviews/`
- [ ] Study hours logged in `learning-journal/`
