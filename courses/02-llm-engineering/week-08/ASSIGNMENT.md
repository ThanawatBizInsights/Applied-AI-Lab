# Week 08 — Assignment (3 hours): When does fine-tuning help? Billionslight technical answer style

**Linked projects:** [Billionslight](../../../projects/billionslight/README.md)

## Brief
Fine-tune a small open model to answer in Billionslight's technical support format, and show with evidence whether it beats prompting and RAG on correctness, format compliance and cost.

## Deliverables
- Dataset card (`evaluations/datasets/`) following Datasheets for Datasets
- Training notebook or script with pinned versions and seed
- Comparison report with a recommendation

## Acceptance criteria
- [ ] Adapter weights are NOT committed (stored on Hugging Face Hub, private)
- [ ] Base model licence recorded in `projects/billionslight/TECH_STACK.md`
- [ ] Held-out set never seen during training
- [ ] Total GPU cost reported against the approved estimate
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Format compliance rate
- Technical correctness
- Inference cost per 1k answers
- GPU training cost

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Out of memory: reduce sequence length or batch size; enable gradient checkpointing.
- bitsandbytes does not run on Intel Mac: do all training on the cloud GPU, never locally.
- Loss falls but answers get worse: overfitting; evaluate on held-out data every N steps.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
