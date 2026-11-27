# Week 02 — Assignment (3 hours): Thai token economics report for Balena captions

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md)

## Brief
Build a small CLI that takes a CSV of Thai/English marketing texts, tokenises them with at least three tokenisers (for example GPT-style BPE, a SentencePiece model and a Thai-specific model), and produces a cost and context-budget report.

## Deliverables
- `starter-code/token_report.py` (learner-written) with a `--input` CSV option
- `evaluations/reports/w02-thai-token-economics.md` with a table and one chart
- At least 3 unit tests covering the counting and cost functions

## Acceptance criteria
- [ ] Runs offline after the first tokenizer download; no API keys needed
- [ ] Reports tokens per character and estimated cost per 1,000 captions for each tokenizer
- [ ] Explains in your own words *why* Thai costs differ (cites the lecture or a paper)
- [ ] Uses 40+ texts, all synthetic or already-public marketing copy
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Tokens per character (Thai vs English)
- Estimated USD per 1,000 captions
- Share of the context window used by a 500-word brand guide

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Tokenizer download blocked or slow: set `HF_HUB_OFFLINE=1` after the first download; use small tokenizers only.
- NumPy shape errors in attention: print `.shape` after every step; Q·Kᵀ must be (seq, seq).
- Exploding loss: lower the learning rate by 10x; check that inputs are normalised.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
