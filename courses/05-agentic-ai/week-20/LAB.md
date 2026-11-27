# Week 20 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 20 materials"*.

## Planned checkpoints
1. Turn the Week 18 agent into a planner + reviewer + tester team; compare with the single agent.
2. Add guardrails: refuse medical advice in Rusty contexts; block non-decodable words in Phonics drafts.
3. Build a Rusty recommendation prototype on synthetic activity data that keeps personal data on-device.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Multi-agent costs explode: share state and cap rounds; compare at equal budgets.
- Guardrail false positives: measure them; tune on a held-out set, not the test set.
