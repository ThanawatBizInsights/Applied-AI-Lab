# Week 21 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 21 materials"*.

## Planned checkpoints
1. Build `POST /v1/complete` and `POST /v1/search` with pydantic models and streaming.
2. Write a multi-stage Dockerfile and run it locally.
3. Add API-key auth with project scopes and tests that prove isolation.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Docker image is huge: multi-stage build; slim base; no build tools in the final stage.
- Async endpoint blocks: you are calling a sync client inside `async def`.
