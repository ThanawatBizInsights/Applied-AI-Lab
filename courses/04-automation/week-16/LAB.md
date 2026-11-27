# Week 16 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 16 materials"*.

## Planned checkpoints
1. Add an error workflow in n8n that records failures in Supabase and sends an alert.
2. Build an approval step (for example via LINE or email) with a signed approve/reject link.
3. Simulate failures (timeouts, 500s, bad data) and confirm that nothing is lost or duplicated.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Approval links can be forwarded: sign them, expire them and bind them to a staff identity.
- Retry storms: cap attempts and add jitter.
