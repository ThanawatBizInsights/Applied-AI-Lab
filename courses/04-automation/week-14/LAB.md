# Week 14 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 14 materials"*.

## Planned checkpoints
1. Create a webhook endpoint in n8n and verify an HMAC signature.
2. Connect Google Drive with the narrowest scope that works.
3. Write a synthetic CheckKhum enquiry into a local Supabase table protected by RLS.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- OAuth redirect mismatch: the callback URL must match exactly, including the trailing slash.
- RLS blocks inserts: the policy needs `with check`, not only `using`.
