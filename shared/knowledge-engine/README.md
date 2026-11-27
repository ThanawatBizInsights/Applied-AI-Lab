# Knowledge Engine (RAG)

**Status:** not started. Built in **Weeks 5–7** for CheckKhum (public policy wording) and
Billionslight (public datasheets).

Planned: ingestion with metadata → chunking → embeddings in Supabase pgvector → hybrid retrieval
(BM25 + dense, RRF) → reranking → answers with clause-level citations and a refusal path.
Project isolation via separate schemas or RLS. Evaluated in EXP-02.
