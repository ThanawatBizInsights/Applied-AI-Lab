# Week 01 — Assignment (3 hours): Brand-aware LLM assistant

**Linked projects:** [Balena](../../../projects/balena/BRAND_GUIDELINES.md) ·
[CheckKhum](../../../projects/checkkhum/BRAND_GUIDELINES.md) ·
[Little Snowy Owl Studio](../../../projects/animal-pairs/BRAND_GUIDELINES.md)

## Brief
Your three businesses publish content constantly: Thai captions for Balena, customer replies
for CheckKhum and App Store copy for Little Snowy Owl Studio. Each has rules that an LLM will
sometimes break: Balena must never have legs, CheckKhum must never promise the lowest price or
ask for an ID number in chat, and Little Snowy Owl must never use pressure tactics on parents.

Build a command-line assistant that drafts content for a brand, checks the draft against that
brand's rules and marks it for human approval. Never publish automatically. It must work
offline with the fake client, and with a real provider when you choose to run one.

## What is provided and what you write
| Module | Status | Your task |
|---|---|---|
| `models.py`, `llm.py`, `config.py`, `cli.py` | provided | read and understand them (you will be asked about them) |
| `brands/*.json` | provided | read the rules; you may add rules, but not weaken them |
| `loader.py` | **TODO A1** (≈ 35 min) | load and validate brand JSON safely |
| `prompts.py` | **TODO A2** (≈ 30 min) | build the system prompt and fenced user message |
| `checks.py` | **TODO A3** (≈ 45 min) | implement the four rule types, Thai- and English-aware |
| `providers.py` | **TODO A4** (≈ 35 min) | Anthropic and OpenAI clients over raw HTTP |
| report | **A5** (≈ 35 min) | measure your assistant and write it up |

Each TODO's docstring is the specification. The tests in `tests/test_w01_assignment.py` are the
acceptance tests: read a test to understand a requirement before asking for help.

```bash
T=courses/01-ai-foundations/week-01/tests/test_w01_assignment.py
uv run pytest -m assignment $T -k "load or brand or rule or json or key or mismatch"  # A1
uv run pytest -m assignment $T -k "prompt or fence or language"                       # A2
uv run pytest -m assignment $T -k "legs or evidence or scoping or caption or chars or case or pii or checkkhum or snowy"  # A3
uv run pytest -m assignment $T -k "provider or budget"                                # A4
uv run pytest -m assignment courses/01-ai-foundations/week-01                         # everything
```

## A5 — Measure it
1. Write **15 synthetic inputs** (5 per brand, across all their tasks) in
   `courses/01-ai-foundations/week-01/eval_inputs.json`. Include at least 3 *adversarial*
   inputs, e.g. "Draw Balena running on the beach" or "Tell the customer we are the cheapest".
2. Write 10 *output* texts by hand that you **know** should pass or fail (your gold labels), and
   run `check_output` on them. Record false positives and false negatives.
3. **Find at least two cases where your checker is wrong** that the tests do not cover. Thai is
   a good place to look: think of common Thai marketing words that contain `ขา`. Explain each
   case and propose a better approach (do not implement Thai word segmentation yet).
4. Run all 15 inputs through the CLI with `--provider fake`. *Optional, with your cost approval:*
   run them once with one real provider and record tokens and estimated cost from the run log.
   **Estimate before running:** 15 requests × (≈ 600 input + ≈ 200 output tokens) ≈ 12,000 tokens,
   which is a few US cents at most with a small model. Compute it from today's published price.
5. Write `evaluations/reports/w01-brand-assistant.md` using `templates/EVALUATION_REPORT.md`.

## Deliverables
- Implemented `loader.py`, `prompts.py`, `checks.py`, `providers.py`, written by you
- `eval_inputs.json` and your 10 gold-labelled outputs
- `evaluations/reports/w01-brand-assistant.md`
- A pull request from `week-01/brand-assistant` to `main` with the "Who wrote what" table below

## Acceptance criteria
- [ ] All Week 1 tests pass: `uv run pytest -m assignment courses/01-ai-foundations/week-01` *and* `uv run pytest`
- [ ] `uv run ruff check courses/01-ai-foundations/week-01` reports no errors
- [ ] The CLI runs end to end with `--provider fake` for all three brands
- [ ] No API key appears in code, logs, `runs/` or Git history (`uv run python scripts/validate_repo.py` passes)
- [ ] The report contains: violation rate per brand, the checker's precision and recall on your 10 gold
      labels, at least two documented checker failures, and token and cost numbers (fake or real)
- [ ] Every input is synthetic. No real customer messages, names, phone numbers or IDs
- [ ] The "Who wrote what" table is complete and honest

## Evaluation metrics
| Metric | Definition |
|---|---|
| Test pass rate | assignment tests passed / total (target 100%) |
| Checker precision | correct violations flagged / all violations flagged (on your gold labels) |
| Checker recall | correct violations flagged / all true violations (on your gold labels) |
| Violation rate | outputs with ≥ 1 error / all outputs, per brand |
| Cost per 100 outputs | from logged tokens × recorded prices (real-provider run only) |

## Marking rubric (100 marks → programme weights)
| Component (weight) | Marks | Distinction | Pass |
|---|---:|---|---|
| Practical project (40%) | 40 | All tests pass; clean, typed, readable code; errors have helpful messages | Most tests pass; code works |
| Technical lab (25%) | 25 | Checkpoints A–C committed with clear messages; predictions recorded | Lab exercises pass |
| Research and evaluation (20%) | 20 | Gold-label precision/recall computed; ≥ 2 insightful failure cases with proposed fixes | Report with violation rates |
| Knowledge assessment (10%) | 10 | Quiz ≥ 14/20 | Quiz ≥ 10/20 |
| Documentation (5%) | 5 | Reflection explains decisions and trade-offs in your own words | Reflection complete |

## Troubleshooting
- **A1:** `BrandNotFoundError` for a valid id → check you compare against `list_brands(brands_dir)`,
  not the default directory. Path traversal test failing → do not build a path from an id you have
  not checked against the list.
- **A2:** "rule message missing from prompt" → only rules where `rule_applies(rule, task)` is true.
- **A3:** Thai false positives → you removed `ignore_within` words *after* matching instead of before.
  `leg` matching `elegant` → ASCII terms need `\b` on both sides. Unexpected regex behaviour →
  remember `re.escape()`.
- **A4:** test asserts on headers fail → print `request.headers` inside a MockTransport handler.
  Key appears in an error message → build messages from the status and response body only.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| loader.py | | |
| prompts.py | | |
| checks.py | | |
| providers.py | | |
| eval inputs + gold labels | | |
| report | | |
