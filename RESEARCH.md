# RESEARCH — Research and evaluation strand (20% of the grade)

The learner's strength is research. This strand turns it into **AI evaluation practice**: every
claim about a model, prompt or workflow must come from a reproducible experiment on stated data.

## Principles (from `AGENTS.md` §1.4)
1. Question → falsifiable hypothesis → baseline → design → **pre-register** (commit the design before running).
2. Fix and record versions: model ID, date, prompt version, seed, software versions.
3. Repeat runs (≥ 3 for stochastic systems); report spread, not a single number.
4. Combine quantitative metrics with qualitative analysis (error categories, examples).
5. State limitations and threats to validity. Say what the result does **not** show.
6. Cite only sources you have actually read and verified. Label preprints.
7. Synthetic or public data only for sensitive domains (insurance, health, children).
8. Estimate cost and get approval before any paid run.

## Experiments
| ID | Title | Weeks | Design |
|---|---|---|---|
| EXP-01 | Thai-language LLM accuracy and cost benchmarking | 3–4 | [design](research/experiments/EXP-01-thai-llm-benchmark/EXPERIMENT.md) |
| EXP-02 | RAG versus standard LLM responses | 6–7 | [design](research/experiments/EXP-02-rag-vs-llm/EXPERIMENT.md) |
| EXP-03 | Character identity consistency with and without LoRA | 11–12 | [design](research/experiments/EXP-03-identity-lora/EXPERIMENT.md) |
| EXP-04 | Manual versus automated content production | 15–16 | [design](research/experiments/EXP-04-manual-vs-automated/EXPERIMENT.md) |
| EXP-05 | Phonics curriculum compliance | 17, 20 | [design](research/experiments/EXP-05-phonics-compliance/EXPERIMENT.md) |
| EXP-06 | Single-agent versus multi-agent performance | 18, 20 | [design](research/experiments/EXP-06-single-vs-multi-agent/EXPERIMENT.md) |
| EXP-07 | Privacy-preserving AI personalisation | 20 | [design](research/experiments/EXP-07-privacy-personalisation/EXPERIMENT.md) |
| EXP-08 | AI adoption and productivity improvements in SMEs | 13–24 | [design](research/experiments/EXP-08-sme-adoption-productivity/EXPERIMENT.md) |

Each folder has `EXPERIMENT.md` (all required sections), `results.csv` (header row: one row per
observation) and `results.json` (summary).

## Where things go
| Folder | Contents |
|---|---|
| `research/literature-review/` | `LITERATURE_LOG.md`, one line per source read, plus notes |
| `research/research-questions/` | open questions that may become experiments |
| `research/experiments/` | experiment designs, raw results, analysis notebooks |
| `research/findings/` | short, evidence-linked findings (one file per finding) |
| `evaluations/` | reusable datasets, benchmark harnesses, metric definitions, reports |

## Link to the learner's background
EXP-08 extends the learner's MSc research on how data companies position themselves as AI
enablers: it studies, from the adopter's side, which AI workflows small businesses actually keep
using, with the TAM/UTAUT constructs and a mixed-methods design.
