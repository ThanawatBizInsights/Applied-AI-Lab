# shared/ — Reusable components

Components built during the course and later integrated into the capstone. Each starts empty
and is created in the week shown; nothing here is production code for any project.

| Component | Built in | Becomes |
|---|---|---|
| [`llm-gateway/`](llm-gateway/README.md) | W1 seed (brand assistant), W4 v0.1 | Central LLM Gateway |
| [`knowledge-engine/`](knowledge-engine/README.md) | W5–7 | Knowledge and RAG Engine |
| [`comfyui-workflows/`](comfyui-workflows/README.md) | W9–12 | Visual Production Engine |
| [`automation/`](automation/README.md) | W13–16 | n8n Automation Engine, Video pipeline |
| [`mcp-servers/`](mcp-servers/README.md) | W19 | MCP Integration Layer |
| [`utilities/`](utilities/README.md) | as needed | shared helpers (logging, cost, Thai text) |

Rules: every component has a fake/offline mode, tests that run without network, and a README
with its interface, limitations and the ADR that introduced it.
