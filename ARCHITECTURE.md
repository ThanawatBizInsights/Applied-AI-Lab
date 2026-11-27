# ARCHITECTURE — Personal AI Studio OS (capstone)

**Status:** proposed target architecture. Nothing below is built yet except the Week 1 brand
assistant, which is the seed of the Gateway and the Brand service. Components are built one
course at a time and integrated in Course 06. **Do not build the whole platform up front.**

## 1. Context
One person runs several small businesses and creative studios. Each needs LLM text, retrieval
over its own documents, images or video, automation and human approval. All share one
engineering platform, but **each project's data, credentials and permissions stay isolated**.

## 2. Components
```
                         ┌───────────────────────── Studio API (FastAPI, W21) ─────────────────────────┐
  n8n Automation (W13–16)│  auth & project scopes · jobs · cost & usage · approvals · audit log         │
  ───────────────────────►                                                                              │
  MCP clients (W19, W22) │ ┌──────────────┐ ┌──────────────────┐ ┌───────────────┐ ┌─────────────────┐ │
  ───────────────────────► │ LLM Gateway  │ │ Knowledge Engine │ │ Visual Engine │ │ Video Engine    │ │
                         │ │ (W1→W4)      │ │ RAG (W5–7)       │ │ ComfyUI (W9–12)│ │ Remotion+TTS(W15)│ │
                         │ └──────┬───────┘ └────────┬─────────┘ └──────┬────────┘ └────────┬────────┘ │
                         │        │   Brand & Project Context service (W1 seed → W22)        │          │
                         │        │   Evaluation & benchmarking (W4, W7, W20, W23)            │          │
                         └────────┼──────────────────┼──────────────────┼──────────────────────┼──────────┘
                                  ▼                  ▼                  ▼                      ▼
                         OpenAI / Anthropic /   Supabase Postgres   Cloud GPU (ComfyUI)    ElevenLabs,
                         Gemini / open models   + pgvector (per-     — approval needed      Remotion render
                                                project schemas/RLS)
```

| Component | Lives in | Built in | First version |
|---|---|---|---|
| LLM Gateway | `shared/llm-gateway/` | W1 seed, W4 v0.1 | unified client, routing, usage log |
| Brand & Project Context | `projects/*/BRAND_GUIDELINES.md` + brand JSON | W1 seed, W22 service | rules as data |
| Knowledge Engine | `shared/knowledge-engine/` | W5–7 | hybrid RAG with citations |
| Visual Production Engine | `shared/comfyui-workflows/` | W9–12 | ComfyUI API client + manifests |
| Video Production Engine | `shared/automation/` + Remotion | W15 | script → narration → render draft |
| Automation Engine | `shared/automation/n8n/` | W13–16 | workflows with approvals |
| MCP Integration Layer | `shared/mcp-servers/` | W19 | read-only project servers |
| Human approval system | Studio API + n8n | W16, W22 | approve/edit/reject + audit |
| Cost and usage monitoring | Gateway usage log → dashboard | W4, W23 | JSONL → Postgres |
| Evaluation and benchmarking | `evaluations/` | W4 onwards | harness + reports |
| Research and experiment management | `research/` | W1 onwards | experiment templates |

## 3. Cross-cutting principles
1. **Isolation by project:** separate schemas or RLS policies, separate keys and separate MCP
   servers. A request for Balena can never read CheckKhum data.
2. **Human approval before anything external** (publishing, customer messages).
3. **Everything measured:** every model call logs provider, model, tokens, latency and cost.
4. **Offline-testable:** each component has a fake mode so CI runs with no network or cost.
5. **Provenance:** every generated asset records its model, version, seed, prompt and workflow hash.
6. **Licences recorded** before commercial use (per project `TECH_STACK.md`).

## 4. Architecture Decision Records (ADRs)
Add one ADR per significant decision using the format below. Keep them short.

### ADR-001 — One repository for learning and shared components
- **Status:** accepted (setup, 2026-11-27)
- **Context:** the learner needs one place where ChatGPT and Claude can see all context.
- **Decision:** this repository holds curriculum, research, shared components and the capstone.
  Production project code stays in each project's own repository, read-only from here.
- **Consequences:** simple handoff; shared components must later be extracted or packaged if a
  production project adopts them.

### ADR-002 — Provider-independent client interface from Week 1
- **Status:** accepted (setup, 2026-11-27)
- **Context:** the programme uses OpenAI, Anthropic, Gemini and open models; tests must run offline.
- **Decision:** all model calls go through `LLMClient.complete()`; a `FakeLLMClient` is the default.
- **Consequences:** zero-cost development and CI; provider-specific features need explicit
  extension points (Week 4).

### ADR-003 — Brand rules as data
- **Status:** accepted (setup, 2026-11-27)
- **Decision:** brand constraints are JSON rule files validated at load time, not code.
- **Consequences:** new projects need no code changes; rule types are limited to what the
  checker implements (extend deliberately).

<!-- ADR template
### ADR-NNN — Title
- **Status:** proposed | accepted | superseded by ADR-XXX
- **Context:**
- **Decision:**
- **Alternatives considered:**
- **Consequences:**
-->
