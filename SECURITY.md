# SECURITY — Security, privacy and data policy

## 1. Repository visibility
This repository is meant to be **private**. ⚠️ At setup (2026-11-27) GitHub reported it as
**public**. Until the owner changes it (GitHub → Settings → General → Danger Zone → Change
visibility), treat everything committed here as public: no personal details, no private
project information, no unreleased business data.

## 2. Never commit
| Category | Examples | Where it goes instead |
|---|---|---|
| Secrets | API keys, tokens, passwords, service-role keys, signing certificates | `.env` (git-ignored); provider dashboards |
| Customer data | CheckKhum policies, quotes, names, phone numbers, ID numbers, LINE chats | Nowhere in this lab; use synthetic data |
| Children's data | Iris's Family footage, faces, names, schools, locations | Stays in its private storage; metadata only |
| Health data | Real Apple Health exports, mood entries | Nowhere; Rusty experiments use synthetic data |
| Large files | model weights, LoRAs, datasets > 5 MB, rendered video/audio | Hugging Face Hub (private), cloud storage |
| Unlicensed media | images you do not own or have no licence for | Do not use |

`.gitignore` blocks the common cases. `scripts/validate_repo.py` scans for key patterns, large
files and forbidden file types, and runs in the test suite.

## 3. If a secret is committed
1. **Revoke and rotate the key at the provider immediately.** Deleting the file is not enough:
   the key stays in Git history, and public repositories are scanned by bots within minutes.
2. Check the provider's usage logs for misuse.
3. Remove it from history (`git filter-repo`), force-push, and ask collaborators to re-clone.
4. Record the incident and the lesson in `learning-journal/`.

## 4. Data rules by project
- **CheckKhum:** synthetic or public policy documents only. No real customer records, ever.
- **Iris's Family:** no private footage or personal information in Git, logs or LLM prompts;
  automation handles metadata only.
- **Rusty:** synthetic activity and health data only; no diagnostic or medical recommendations.
- **Little Snowy Owl (Animal Pairs, Phonics Pond):** AI supports development only; it never
  interacts with children; the apps stay offline and child-friendly.
- **Seoa Ryn, LumiTale:** no likeness of a real person without documented consent.
- **CheePao:** respect platform terms; disclose affiliate links; no fake reviews.

## 5. Third-party code and models
Before installing a ComfyUI custom node, n8n community node or MCP server, review its source,
maintainer, licence, requested permissions and network access, and record the review in the
relevant week folder. Record model licences and commercial-use restrictions in the project's
`TECH_STACK.md` before commercial use.

## 6. Cost controls
No paid API calls, subscriptions or cloud resources without approval and a written estimate. The
Week 1 client enforces `LLM_MAX_REQUESTS_PER_RUN`. Set spend limits in every provider dashboard.

## 7. Production
Nothing in this repository deploys to production. Any production deployment of any project
needs explicit human approval. Protect `main` with branch protection rules.

## 8. Threat model
Expanded in Week 23 (OWASP Top 10 for LLM Applications, STRIDE).
