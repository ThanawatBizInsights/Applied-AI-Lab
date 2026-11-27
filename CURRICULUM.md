# Curriculum — Applied AI Engineering Academy

A 24-week, project-based programme: **10 hours per week, 240 hours in total**. Every practical
task is tied to at least one of the learner's real projects. Principles come before frameworks.

- Status of materials: **Week 1 is complete.** Weeks 2–24 have outlines, prerequisites,
  objectives, assignments and assessment criteria. Each week's full lecture, lab, quiz and
  starter code are written **when the learner reaches the previous week** (see `ROADMAP.md`).
- Rules for AI assistants: [`AGENTS.md`](AGENTS.md). Progress tracker: [`PROGRESS.md`](PROGRESS.md).

---

## 1. Learner profile and adaptation

**Profile** (provided by the learner, kept general because this repository is public): MSc in
Information Systems with first-class honours and a research award; a dissertation on how data
companies position themselves as AI enablers (go-to-market); experience with Python, R,
Tableau, Excel, quantitative and qualitative research, business strategy, application
development and AI-assisted content production. Runs several live products (see `projects/`).

**How the curriculum adapts**

| Strength | How it is used |
|---|---|
| Research methods and analysis | Research Mode, experiment design and evaluation carry 20% of the grade. Experiments are real studies on real projects. |
| Python and data analysis | No beginner programming exercises. Python work goes straight to engineering practice: packaging, typing, testing, HTTP. |
| Business strategy and GTM | Every course ends with cost, value and adoption analysis (EXP-08: SME productivity). |
| Live products | Assignments improve real projects instead of toy datasets. |

**Likely gaps (to be confirmed by the Week 1 diagnostic and early reviews)**

| Gap | Where it is addressed |
|---|---|
| Software engineering practice: tests, packaging, type hints, Git workflow | Weeks 1, 4, 21, 23 |
| HTTP, APIs, authentication, async I/O | Weeks 1, 14, 21 |
| Linear algebra and probability behind neural networks | Weeks 2, 5, 9 (just enough, applied) |
| PyTorch and model internals | Weeks 2, 8, 11 |
| SQL depth: Postgres, indexes, pgvector, row-level security | Weeks 5, 7, 14 |
| Containers, deployment, observability | Weeks 21–23 |
| TypeScript (Remotion, MCP servers, n8n Code nodes) | Weeks 15, 19 (targeted, not a full course) |
| Swift/SwiftUI internals | Not taught as a language course. AI-assisted QA of the SwiftUI apps appears in Weeks 4, 18 and 20. |

---

## 2. Weekly time model (10 hours)

| Activity | Hours | File |
|---|---:|---|
| Theoretical instruction | 2 | `LECTURE.md` |
| Guided laboratory | 2 | `LAB.md` |
| Independent project development | 3 | `ASSIGNMENT.md` |
| Research reading | 1 | `RESEARCH_READING.md` |
| Assessment | 1 | `QUIZ.md` |
| Documentation and reflection | 1 | `REFLECTION.md` |
| **Total per week** | **10** | |

---

## 3. Programme overview

| Week | Course | Topic | Main project link | Hours |
|---:|---|---|---|---:|
| 01 | 01 Foundations | Python environment, Git, APIs and JSON | Balena, CheckKhum, Little Snowy Owl | 10 |
| 02 | 01 Foundations | Neural networks, transformers, tokenisation and inference | Balena (Thai tokenisation) | 10 |
| 03 | 01 Foundations | Prompt engineering, structured outputs and multimodal inputs | Balena, Billionslight | 10 |
| 04 | 01 Foundations | Tool calling, model routing, benchmarking and evaluation | Multi-model AI Gateway | 10 |
| 05 | 02 LLM Engineering | Embeddings, vector databases and semantic search | Billionslight | 10 |
| 06 | 02 LLM Engineering | Document processing, chunking and RAG | CheckKhum | 10 |
| 07 | 02 LLM Engineering | Hybrid retrieval, reranking, citations and evaluation | CheckKhum, Billionslight | 10 |
| 08 | 02 LLM Engineering | Fine-tuning, LoRA, QLoRA and quantisation | Billionslight | 10 |
| 09 | 03 ComfyUI | Diffusion models, latent space, checkpoints, samplers and VAE | Balena | 10 |
| 10 | 03 ComfyUI | ControlNet, reference conditioning, inpainting and masking | Balena, Seoa Ryn | 10 |
| 11 | 03 ComfyUI | Character datasets, LoRA training and identity consistency | Balena, Animal Pairs, Seoa Ryn | 10 |
| 12 | 03 ComfyUI | Video generation, upscaling, batch processing and ComfyUI API | LumiTale, Phonics Pond | 10 |
| 13 | 04 Automation | n8n fundamentals, triggers and expressions | CheePao | 10 |
| 14 | 04 Automation | APIs, webhooks, OAuth, Supabase and Google Drive | CheckKhum, Iris's Family | 10 |
| 15 | 04 Automation | ComfyUI, Remotion and ElevenLabs integration | Balena Content Factory | 10 |
| 16 | 04 Automation | Error handling, queues, retries, logging and human approvals | CheckKhum Customer Operations | 10 |
| 17 | 05 Agentic AI | Frontier models, reasoning and multimodal intelligence | Phonics Pond, Billionslight | 10 |
| 18 | 05 Agentic AI | Agent architecture, memory, state and tool use | AI Software Development Agent | 10 |
| 19 | 05 Agentic AI | Model Context Protocol and custom MCP servers | Billionslight, Phonics Pond | 10 |
| 20 | 05 Agentic AI | Multi-agent orchestration, evaluation and guardrails | Phonics Pond, Rusty | 10 |
| 21 | 06 Platform | FastAPI, Docker, authentication and deployment | Personal AI Studio OS | 10 |
| 22 | 06 Platform | Integration of LLMs, ComfyUI, n8n and MCP | Personal AI Studio OS | 10 |
| 23 | 06 Platform | Security, observability, testing and cost optimisation | Personal AI Studio OS | 10 |
| 24 | 06 Platform | Portfolio documentation and capstone demonstration | Personal AI Studio OS | 10 |
| | | | **Total** | **240** |

---

## 4. Courses

### Course 01 — AI Engineering Foundations (Weeks 1–4)
[`courses/01-ai-foundations/`](courses/01-ai-foundations/README.md) ·
**Main project: Multi-model AI Gateway** (`shared/llm-gateway/`). One Python interface over
OpenAI, Anthropic and Gemini, with structured outputs, tool calling, routing by cost and
quality, and a benchmark harness. It is the first component of the capstone.

### Course 02 — LLM and Knowledge Engineering (Weeks 5–8)
[`courses/02-llm-engineering/`](courses/02-llm-engineering/README.md) ·
**Main projects: CheckKhum Insurance Intelligence and Billionslight Product Intelligence**
(`shared/knowledge-engine/`). Thai-language RAG over **public or synthetic** policy wording
and solar product datasheets, with Supabase and pgvector, hybrid retrieval, citations and a
measured comparison of RAG against a plain LLM (EXP-02).

### Course 03 — ComfyUI and Generative Media Engineering (Weeks 9–12)
[`courses/03-comfyui/`](courses/03-comfyui/README.md) ·
**Main projects: Balena, Animal Pairs, Phonics Pond, Seoa Ryn and LumiTale Studio**
(`shared/comfyui-workflows/`). Diffusion from first principles, then controllable,
identity-consistent generation (EXP-03) on cloud GPUs. Includes brand-rule checks such as
"Balena never has legs".

### Course 04 — Intelligent Business Automation (Weeks 13–16)
[`courses/04-automation/`](courses/04-automation/README.md) ·
**Main projects: Balena Content Factory, Iris's Family Video Studio, CheePao Affiliate
Intelligence and CheckKhum Customer Operations** (`shared/automation/`). n8n workflows with
webhooks, OAuth, queues, retries and human approval steps (EXP-04: manual vs automated).

### Course 05 — Frontier AI and Agentic Systems (Weeks 17–20)
[`courses/05-agentic-ai/`](courses/05-agentic-ai/README.md) ·
**Main projects: Phonics Pond Educational AI, Rusty Personalisation Engine and an AI Software
Development Agent** (`shared/mcp-servers/`). Agent loops, memory, MCP servers, multi-agent
orchestration and guardrails (EXP-05, EXP-06, EXP-07). AI stays on the development side and
never talks to children.

### Course 06 — AI Platform Engineering (Weeks 21–24)
[`courses/06-platform-engineering/`](courses/06-platform-engineering/README.md) ·
**Main project: Personal AI Studio OS** (`capstone/`). FastAPI, Docker, authentication,
integration of the earlier components, security, observability, cost control and the final
portfolio demonstration.

---

## 5. Assessment

| Component | Weight | Evidence |
|---|---:|---|
| Practical projects | 40% | Weekly `ASSIGNMENT.md` deliverables and course main projects |
| Technical laboratories | 25% | `LAB.md` checkpoints completed and committed |
| Research and evaluation | 20% | Experiments in `research/experiments/`, reports in `evaluations/reports/` |
| Knowledge assessments | 10% | `QUIZ.md` scores |
| Documentation | 5% | `REFLECTION.md`, `learning-journal/`, README quality |
| **Total** | **100%** | |

Each assignment has its own rubric that maps onto these weights. Grade bands: **Distinction**
≥ 70%, **Merit** 60–69%, **Pass** 50–59% (aligned with Irish and UK postgraduate conventions).
Competency levels 0–5 are tracked separately in `PROGRESS.md` and rise only with evidence.

## 6. Research strand

Eight experiments run through the programme. Templates are in `research/experiments/`.

| ID | Topic | Weeks |
|---|---|---|
| EXP-01 | Thai-language LLM accuracy and cost benchmarking | 3–4 |
| EXP-02 | RAG vs standard LLM responses | 6–7 |
| EXP-03 | Character identity consistency with and without LoRA | 11–12 |
| EXP-04 | Manual vs automated content production | 15–16 |
| EXP-05 | Phonics curriculum compliance | 17, 20 |
| EXP-06 | Single-agent vs multi-agent performance | 18, 20 |
| EXP-07 | Privacy-preserving AI personalisation | 20 |
| EXP-08 | AI adoption and productivity improvements in SMEs | 13–24 (longitudinal) |
