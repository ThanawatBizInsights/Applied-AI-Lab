# Week 01 — Python development environment, Git, APIs and JSON

Course 01 — AI Engineering Foundations · **10 hours** · **Status: complete materials**
Linked projects: [Balena](../../../projects/balena/README.md),
[CheckKhum](../../../projects/checkkhum/README.md),
[Little Snowy Owl Studio](../../../projects/animal-pairs/README.md)

## Why this week matters
Every later week (RAG, ComfyUI automation, agents, MCP, the capstone) is built from the same
four parts: a reproducible Python environment, version control, HTTP APIs and JSON. If these
are solid, later problems are about AI. If they are shaky, later problems are about the
plumbing, and they are much harder to debug.

You finish the week with a **brand-aware LLM assistant**. It turns a brand profile (rules
such as "Balena never has legs") into prompts, calls a model, checks the output against the
rules and queues it for human approval. It works offline at zero cost, and with a real
provider when you approve the spend. In Week 4 it grows into the Multi-model AI Gateway.

## Time plan
| # | Activity | Hours | File |
|---|---|---:|---|
| 1 | Lecture: environments, Git internals, HTTP, JSON, secrets, LLM app anatomy | 2 | [LECTURE.md](LECTURE.md) |
| 2 | Guided lab: set up the Mac, Git drills, exercises 1–3 | 2 | [LAB.md](LAB.md) |
| 3 | Assignment: brand-aware LLM assistant | 3 | [ASSIGNMENT.md](ASSIGNMENT.md) |
| 4 | Research reading | 1 | [RESEARCH_READING.md](RESEARCH_READING.md) |
| 5 | Knowledge check (20 marks) | 1 | [QUIZ.md](QUIZ.md) |
| 6 | Reflection and journal | 1 | [REFLECTION.md](REFLECTION.md) |
| | **Total** | **10** | |

Suggested order: Lecture §1–2 → Lab Parts A–B → Lecture §3–6 → Lab Part C → Assignment →
Reading → Quiz → Reflection.

## Prerequisites
- An Intel MacBook with macOS, admin rights and about 2 GB free disk space. No GPU needed.
- A GitHub account with access to this repository.
- Python experience (functions, classes, dicts, exceptions). No prior HTTP or Git internals needed.
- **No API key is required.** A real-provider run is optional and needs your cost approval.

## Files
```
week-01/
├── starter-code/
│   ├── brand_assistant/      # the assignment package (TODOs in loader, prompts, checks, providers)
│   └── w01_exercises/        # guided lab exercises 1–3
├── tests/
│   ├── test_w01_scaffold.py    # checks provided code: must pass before you start
│   ├── test_w01_exercises.py   # lab exercises      (marked "assignment")
│   └── test_w01_assignment.py  # assignment         (marked "assignment")
└── reviews/                  # reviews of your submission (ChatGPT or self-review)
```

## Completion evidence (AGENTS.md §5)
- [ ] `uv run pytest -m assignment courses/01-ai-foundations/week-01` → all pass, with code **you** wrote
- [ ] `evaluations/reports/w01-brand-assistant.md` written
- [ ] Acceptance criteria ticked in `ASSIGNMENT.md`
- [ ] Quiz score in `PROGRESS.md`
- [ ] `REFLECTION.md` completed in your own words
- [ ] Review saved in `reviews/`
- [ ] Hours logged in `learning-journal/`
