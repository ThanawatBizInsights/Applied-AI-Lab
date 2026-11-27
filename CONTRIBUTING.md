# CONTRIBUTING — Workflow for the learner and AI assistants

## Branches
| Branch | Purpose |
|---|---|
| `main` | protected; changes only through reviewed pull requests |
| `setup/*` | repository setup and maintenance |
| `week-XX/<topic>` | learner's work for a week, e.g. `week-01/brand-assistant` |
| `exp/<id>-<topic>` | experiments, e.g. `exp/EXP-01-thai-benchmark` |
| `review/<week>` | review documents only |

## Weekly flow
1. `git switch main && git pull && git switch -c week-XX/<topic>`
2. Work through the week; commit small, logical steps.
3. `uv run pytest`, `uv run pytest -m assignment courses/<course>/week-XX`, `uv run ruff check .`,
   `uv run python scripts/validate_repo.py`
4. Push and open a pull request. Fill in the "Who wrote what" table.
5. Ask for a review (ChatGPT in Review Mode, or self-review with `templates/REVIEW_TEMPLATE.md`).
6. Address feedback, update `PROGRESS.md`, merge.

## Commit messages
```
Implement Thai-aware forbidden-term matching

Remove ignore_within words before matching so ขาว and ขาย do not trigger
the no-legs rule. ASCII terms use word boundaries.

AI-Assisted: none
```
Trailers: `AI-Assisted: none | reviewed | generated` (see `AGENTS.md` §4).

## Code standards
- Python 3.11+, type hints, docstrings on public functions, `ruff` clean.
- Tests with `pytest`; anything that would call a network service uses a fake or `httpx.MockTransport`.
- No secrets, personal data or large binaries (see `SECURITY.md`).

## Adding a week's full materials
Follow the checklist in `ROADMAP.md`. Never commit solutions to assignments.
