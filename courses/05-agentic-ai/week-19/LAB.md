# Week 19 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 19 materials"*.

## Planned checkpoints
1. Build a minimal MCP server with one tool and one resource; connect it to a desktop client.
2. Expose Billionslight product search as an MCP tool with input schemas.
3. Write tests that call the server in-process.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- stdio server prints logs to stdout and breaks the protocol: log to stderr.
- Client does not see tools: check capability negotiation and server start command.
