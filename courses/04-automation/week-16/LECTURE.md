# Week 16 — Lecture (2 hours): Error handling, queues, retries, logging and human approvals

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 16 materials"*.

Principles before tools. Planned sequence:

1. Failure modes: transient vs permanent errors
2. Retries with backoff; idempotency keys; exactly-once is a myth
3. Queues and dead-letter handling
4. Human approval patterns: approve, edit, reject; audit logs
5. Observability for automations: run IDs, structured logs, SLOs

Each section will include: the core idea, a worked example linked to [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md),
a "predict before you run" question and a common misconception.
