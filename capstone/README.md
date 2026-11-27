# Capstone — Personal AI Studio OS

**Status:** not started. Architecture: [`ARCHITECTURE.md`](../ARCHITECTURE.md).

The capstone starts as a **small, working MVP** and grows course by course. It is not built
during setup.

| Stage | Week | Scope |
|---|---|---|
| Seed | 1 | brand-aware assistant (`courses/01-ai-foundations/week-01/starter-code`) |
| Components | 4–19 | Gateway, Knowledge Engine, ComfyUI client, automations, MCP servers in `shared/` |
| MVP | 21 | `studio-api/`: FastAPI + auth + Docker exposing Gateway and Knowledge Engine |
| Integrated | 22 | jobs, brand/context service, n8n and MCP integration |
| Hardened | 23 | threat model, observability, cost optimisation |
| Demonstrated | 24 | `DEMO.md`, recording (private), portfolio case studies |

Non-negotiables: per-project data isolation · human approval before anything external · cost
and usage logged for every call · offline fake mode for demos and CI.
