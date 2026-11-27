# Week 22 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 22 materials"*.

## Planned checkpoints
1. Add `POST /v1/jobs/image` that queues a ComfyUI job and returns a job ID.
2. Have n8n call the Studio API instead of providers directly.
3. Expose `list_projects`, `get_brand_rules` and `search_knowledge` via an MCP server.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Jobs stuck in 'running': add heartbeats and timeouts; requeue on worker crash.
- Circular dependencies between services: n8n calls the API; the API never calls n8n synchronously.
