# Week 01 — Learning objectives

By the end of the week you can:

| # | Objective | Evidence | Competency |
|---|---|---|---|
| 1 | Explain what a virtual environment, a lockfile and `pyproject.toml` each solve, and set up a reproducible project with `uv` on an Intel Mac. | Lab A; `uv.lock` in Git; quiz Q1–2 | Python environments |
| 2 | Explain Git's object model (blob, tree, commit, branch pointer) and use a branch-and-pull-request workflow without committing secrets. | Lab B; your branch and PR | Git and GitHub |
| 3 | Read and write an HTTP request and response by hand, classify status codes and explain idempotency, timeouts and authentication headers. | Exercise 2; quiz Q4–6 | HTTP and APIs |
| 4 | Handle JSON with Thai text correctly (UTF-8, `ensure_ascii`), and validate untrusted JSON at the system boundary. | Exercise 1; loader (A1) | JSON and data validation |
| 5 | Manage secrets through environment variables, mask them in output and respond correctly to a leaked key. | Exercise 3; `config.py` reading | Security basics |
| 6 | Build an LLM application with a provider-independent interface, a separated system/user prompt, deterministic output checks and a human approval state. | Assignment A1–A5 | LLM application design |
| 7 | Measure a simple LLM application (violation rates, tokens, estimated cost) and explain the limitations of keyword-based checks, especially for Thai. | `w01-brand-assistant.md` report | Evaluation |

## Not the goal this week
- Choosing the "best" model (Week 4, EXP-01).
- Tokenisation details (Week 2). The token counts this week are rough on purpose.
- Prompt engineering technique (Week 3).
