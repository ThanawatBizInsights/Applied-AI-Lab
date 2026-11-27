# ROADMAP — How this repository grows

## Principle: progressive expansion
Full materials are written **one week ahead of the learner**, not all at once. That keeps them
specific to what the learner actually did, and avoids hundreds of pages of shallow content.

| Trigger | Action | Who |
|---|---|---|
| Learner submits Week N | Review Week N (Review Mode), update `PROGRESS.md` and `AI_HANDOFF.md` | ChatGPT (review), learner |
| Review accepted | Expand Week N+1: full `LECTURE.md`, `LAB.md`, `QUIZ.md`, starter code and tests | ChatGPT drafts the content, Claude Code writes the code and tests |
| End of a course | Course retrospective; adjust later weeks to the knowledge gaps found | learner + ChatGPT |
| New project information | Update `projects/<slug>/PROJECT_CONTEXT.md` with status tags | either assistant |

Expansion checklist for a week: principles before tools · predict-before-run prompts ·
starter code with TODOs (no solutions) · assignment tests marked `assignment` that pass against a
private reference solution that is never committed · troubleshooting table · real, verified
readings · cost estimate for any paid step.

## Milestones
| Milestone | When | Definition of done |
|---|---|---|
| M0 Repository setup | Setup | This PR merged after review |
| M1 Gateway v0.1 | End of W4 | `shared/llm-gateway` with tests; EXP-01 report |
| M2 Knowledge Engine v0.1 | End of W7 | Hybrid RAG with citations; EXP-02 report |
| M3 Visual pipeline | End of W12 | ComfyUI client + batch; EXP-03 report |
| M4 Automation with approvals | End of W16 | Content Factory + CheckKhum renewals; EXP-04 |
| M5 Agents and MCP | End of W20 | MCP servers, agent evals; EXP-05/06/07 |
| M6 Studio OS MVP + portfolio | End of W24 | Demo, 3 case studies, EXP-08 paper |

## Backlog (not scheduled)
- GitHub Actions workflow running `pytest` and `validate_repo.py` on every PR (planned for W21; can be earlier if wanted).
- Branch protection on `main` (needs the learner to enable it in GitHub settings).
- Gemini provider in the Week 1 assistant (stretch goal).
- Thai word segmentation for the brand checker (W5–7).
