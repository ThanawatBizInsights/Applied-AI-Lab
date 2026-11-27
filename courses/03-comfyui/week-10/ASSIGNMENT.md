# Week 10 — Assignment (3 hours): Packaging-accurate product scenes

**Linked projects:** [Balena Roastery](../../../projects/balena/README.md), [Seoa Ryn](../../../projects/seoa/README.md)

## Brief
Build a ComfyUI workflow that places the approved Balena cold brew pouch in lifestyle scenes, with the mascot, so that the packaging exactly matches the reference (composited, not hallucinated).

## Deliverables
- Workflow JSON with documented nodes and masks
- Packaging accuracy checklist and results for 20 images
- Custom-node review notes for any third-party node used

## Acceptance criteria
- [ ] Packaging text, logo and colours match the approved reference in ≥ 90% of outputs
- [ ] Every third-party custom node reviewed before installation (source, licence, network access)
- [ ] Balena constraints still pass
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Packaging accuracy rate
- Identity-rubric score
- Manual retouch minutes per image

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- Visible seams after inpainting: feather the mask and lower the denoise strength.
- ControlNet ignored: check the preprocessor and the strength and start/end percentages.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
