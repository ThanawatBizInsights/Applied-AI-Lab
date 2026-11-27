# Week 12 — Assignment (3 hours): ComfyUI batch client and storyboard-to-video pipeline (course main project)

**Linked projects:** [LumiTale Studio](../../../projects/lumitale/README.md), [Little Snowy Owl Studio — Phonics Pond](../../../projects/phonics-pond/README.md), [Balena Roastery](../../../projects/balena/README.md)

## Brief
Build `shared/comfyui-workflows/client` (a Python ComfyUI API client) and a manifest-driven batch pipeline that turns a storyboard JSON into consistent images and short clips, logging cost and settings per asset.

## Deliverables
- Python client with tests (mocked HTTP)
- Manifest schema and one example storyboard
- Run report: success rate, time and cost per asset

## Acceptance criteria
- [ ] Re-running a manifest skips completed assets (idempotent)
- [ ] Every output has a sidecar JSON with workflow hash, seed and model versions
- [ ] Phonics Pond assets are child-appropriate and reviewed by a human before use
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
- Batch success rate
- Cost per finished second of video
- Temporal consistency rating (1–5)

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
- WebSocket disconnects: poll `/history/{prompt_id}` as a fallback.
- Flicker between frames: reduce motion strength; use the same seed and LoRA weight.

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
