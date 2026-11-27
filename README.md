# Applied AI Lab — Applied AI Engineering Academy

A private, project-based, 24-week self-study programme (240 hours) for becoming an independent
**Applied AI Engineer and AI Solutions Architect**. Every lesson is tied to real projects:
Balena Roastery, Little Snowy Owl Studio (Animal Pairs, Phonics Pond), Billionslight,
CheckKhum, Iris's Family, Rusty, LumiTale Studio, Seoa Ryn and CheePao.

> **Teaching first.** AI assistants in this repository explain, hint and review. They do not
> complete assignments for the learner. See [`AGENTS.md`](AGENTS.md).

## Start here
| If you are… | Read |
|---|---|
| the learner, starting out | [`CURRICULUM.md`](CURRICULUM.md) → [Week 1](courses/01-ai-foundations/week-01/README.md) → [`PROGRESS.md`](PROGRESS.md) |
| an AI assistant (Claude, ChatGPT, other) | [`AGENTS.md`](AGENTS.md) → [`AI_HANDOFF.md`](AI_HANDOFF.md) → current week |
| a reviewer | [`AGENTS.md` §1.3 Review Mode](AGENTS.md) → [`templates/REVIEW_TEMPLATE.md`](templates/REVIEW_TEMPLATE.md) |

## Programme
| Course | Weeks | Main project |
|---|---|---|
| [01 AI Engineering Foundations](courses/01-ai-foundations/README.md) | 1–4 | Multi-model AI Gateway |
| [02 LLM and Knowledge Engineering](courses/02-llm-engineering/README.md) | 5–8 | CheckKhum and Billionslight intelligence (RAG) |
| [03 ComfyUI and Generative Media Engineering](courses/03-comfyui/README.md) | 9–12 | Balena, Animal Pairs, Phonics Pond, Seoa Ryn, LumiTale |
| [04 Intelligent Business Automation](courses/04-automation/README.md) | 13–16 | Content Factory, Video Studio, Affiliate Intelligence, Customer Ops |
| [05 Frontier AI and Agentic Systems](courses/05-agentic-ai/README.md) | 17–20 | Phonics Pond AI, Rusty personalisation, Dev Agent |
| [06 AI Platform Engineering](courses/06-platform-engineering/README.md) | 21–24 | Personal AI Studio OS (capstone) |

## Repository map
```
AGENTS.md / CLAUDE.md     rules for AI assistants (teaching, build, review, research modes)
AI_HANDOFF.md             shared context between ChatGPT and Claude (updated every session)
CURRICULUM.md             programme, hours, assessment · PROGRESS.md  tracker and competencies
ARCHITECTURE.md           capstone architecture and ADRs · RESEARCH.md  research strand
courses/                  6 courses, 24 weekly folders (Week 1 complete, 2–24 outlined)
projects/                 10 project workspaces: context, brand rules, stack, roadmap, evaluation
shared/                   reusable components built during the course (gateway, RAG, ComfyUI…)
research/                 literature, questions, 8 experiment designs (EXP-01…08), findings
evaluations/              datasets, benchmarks, metrics, reports
templates/                week, experiment, review, journal, dataset and report templates
scripts/                  scaffold and repository validation · tests/  repository tests
capstone/ portfolio/      Personal AI Studio OS and final portfolio
```

## Quick start (Intel MacBook)
```bash
brew install uv
```
```bash
uv sync --extra dev
```
```bash
uv run pytest
```
```bash
uv run python scripts/validate_repo.py
```
No API key is needed for Week 1 (`LLM_PROVIDER=fake`). Copy `.env.example` to `.env` only when a
week asks for a provider, and only after approving the estimated cost.

## Ground rules
- No secrets, customer records, children's footage or real health data in Git ([`SECURITY.md`](SECURITY.md)).
- No paid API calls, subscriptions or cloud GPUs without approval and a cost estimate.
- Heavy GPU work (diffusion, video, LoRA training) runs on cloud GPUs, not the Intel Mac.
- Work on branches; `main` changes only through reviewed pull requests ([`CONTRIBUTING.md`](CONTRIBUTING.md)).
