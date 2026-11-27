# CLAUDE.md

**Read [`AGENTS.md`](AGENTS.md) first. It holds all the rules for this repository**, including
the four operating modes (Teaching, Build, Review, Research), the ChatGPT–Claude collaboration
protocol, the safety, privacy and cost rules, and what counts as evidence of completion.
This file adds only Claude Code-specific notes and must never contradict `AGENTS.md`.

## Start of every session

1. Read `AI_HANDOFF.md`, then `PROGRESS.md`, then the current week's `README.md`.
2. State the active mode. **Default: Teaching Mode.** Do not complete assignments for the learner.
3. Check the branch. Never commit to `main`.

## End of every meaningful session

1. Run `uv run pytest` (scaffold tests) and report the real result.
2. Run `uv run python scripts/validate_repo.py`.
3. Update `AI_HANDOFF.md` and, if relevant, `CHANGELOG.md`.

## Claude Code-specific notes

- Primary responsibilities: guided implementation, environment setup, Build Mode code
  generation, debugging, automated testing, repository maintenance, technical documentation.
- Do not review your own Build Mode code as if it were independent. Ask for a ChatGPT review
  and record the request in `AI_HANDOFF.md`.
- The learner's machine is an Intel MacBook. Commands you give must work on macOS (BSD tools,
  zsh) as well as in Linux CI.
- Never run paid API calls, cloud GPU jobs or `pip install` of GPU or large-model packages
  without explicit approval and a cost estimate.

## Useful commands

```bash
uv sync --extra dev                                         # install dependencies
uv run pytest                                               # scaffold and repository tests
uv run pytest -m assignment courses/01-ai-foundations/week-01   # learner's assignment tests
uv run python scripts/validate_repo.py                      # structure, hours, weights, links, secrets
```
