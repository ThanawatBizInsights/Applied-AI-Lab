# CheckKhum (เช็กคุ้ม) — Project context

Status tags: **[VERIFIED]** read from the repository · **[USER-PROVIDED]** from the learner's
brief · **[PROPOSED]** learning work, not an existing feature · **[NEEDS CONFIRMATION]**.
Verified on 2026-11-27 by read-only inspection. No changes were made to any project repository.

## Repositories
| Repository | Visibility | Commit inspected | Last commit date |
|---|---|---|---|
| `ThanawatBizInsights/checkkhum` | public | `224c0fa` | 2026-10-10 |

## [VERIFIED] What the repository shows
- Website for เช็กคุ้ม (CheckKhum) Car & Travel Insurance: quotation pages for car, EV, compulsory (พ.ร.บ.) and travel insurance, a customer portal and a demo staff area.
- Stack: Next.js 16, React 19, TypeScript, Tailwind CSS v4, zod, Supabase (Auth plus SQL migrations), LINE LIFF/LINE Login, Vercel config.
- Supabase migrations cover core tables, audit and automation, access control, enquiry intake, CRM workflow, a renewal job, the customer portal, LINE login and LINE OA chat.
- No pgvector or embedding tables were found in the migrations. RAG is new work.

## [USER-PROVIDED] Focus and constraints
- Focus: Thai insurance document intelligence; RAG with verified policy sources; Supabase and pgvector; policy comparison; quotation preparation; CRM and renewal automation; human approval workflows.
- Constraint: never use confidential customer records. Use synthetic or publicly available data only.

## [PROPOSED] Role in this curriculum
- W1: compliant Thai reply drafts (fake provider)
- W6–7: policy-wording RAG and EXP-02
- W16: renewal workflow with approvals
- W23: red-team and hardening

## [NEEDS CONFIRMATION]
- Which insurers' public policy wordings may be used as RAG sources.
- Licensing/regulatory constraints on giving coverage advice (staff-only tool?).

## Decisions log
| Date | Decision | Why | Who |
|---|---|---|---|
| | | | |
