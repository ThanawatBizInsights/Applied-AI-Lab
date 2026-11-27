# Week 19 — Model Context Protocol and custom MCP servers

Course 05 — Frontier AI and Agentic Systems · **10 hours** · Linked projects: [Billionslight](../../../projects/billionslight/README.md), [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 19 materials"*.

## Prerequisites
- Week 18
- Basic TypeScript reading (Python SDK is the default)

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
**Project-scoped MCP servers** — Build two MCP servers in `shared/mcp-servers/`: a Billionslight product-knowledge server (search, spec lookup, citation) and a Phonics Pond curriculum server (read-only access to curriculum JSON and the decodability checker). Each server can see only its own project's data.

## Hardware and cost
Local CPU. No paid services.

## Completion evidence (AGENTS.md §5)
- [ ] Assignment tests pass (`uv run pytest -m assignment courses/05-agentic-ai/week-19`)
- [ ] Acceptance criteria checked off in `ASSIGNMENT.md`
- [ ] Quiz score recorded in `PROGRESS.md`
- [ ] `REFLECTION.md` written in your own words
- [ ] Review saved in `reviews/`
- [ ] Study hours logged in `learning-journal/`
