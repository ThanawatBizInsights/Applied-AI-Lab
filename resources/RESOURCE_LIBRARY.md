# Resource library

**Verification status (read this first).** Links were checked on **2026-11-27** from the setup
environment, whose network blocked most external sites. Only four pages actually loaded; they
are marked ✔. Everything else is marked **"Not yet verified"**: the URL is the well-known
official address, but nobody has confirmed it loads or that the course is still available. When
you first open one, replace "Not yet verified" with ✔ and the date. Never record a resource as
verified without opening it.

Study times are approximate planning figures, not publisher claims. Difficulty: B = beginner,
I = intermediate, A = advanced (relative to this programme).

## Courses and learning paths
| Title | Author / organisation | URL | Module(s) | Diff. | Est. time | Why it is relevant | Verified |
|---|---|---|---|:-:|---|---|---|
| Hugging Face Learn (LLM, Diffusion, Agents courses) | Hugging Face | https://huggingface.co/learn | W2, W5, W8, W9, W18 | I | 4–8 h per course (selected chapters) | Free, hands-on, maintained by the library authors | Not yet verified |
| Neural Networks: Zero to Hero | Andrej Karpathy | https://karpathy.ai/zero-to-hero.html | W2 | I–A | 4 h (micrograd + makemore part 1); full series much longer | Builds backprop and a transformer from scratch, the best principles-first source | Not yet verified |
| OpenAI Cookbook | OpenAI | https://cookbook.openai.com/ | W3, W4, W6 | I | per example, 0.5–1 h | Worked examples for structured outputs, tool calling, RAG | Not yet verified |
| Anthropic Academy | Anthropic | https://www.anthropic.com/learn | W3, W4, W18, W19 | B–I | 2–6 h (selected courses) | Courses on the Claude API, prompting, tool use and MCP | Redirect observed 2026-11-27 (308 → academy.claude.com); destination not loaded |
| Full Stack Deep Learning — LLM Bootcamp | FSDL | https://fullstackdeeplearning.com/llm-bootcamp/ | W4, W21, W23 | I | 3–5 h (selected lectures) | Shipping LLM applications: evaluation, deployment, ops (check how current the material is) | Not yet verified |

## Official documentation
| Title | Organisation | URL | Module(s) | Diff. | Est. time | Why it is relevant | Verified |
|---|---|---|---|:-:|---|---|---|
| uv documentation | Astral | https://docs.astral.sh/uv/ | W1 | B | 1 h | Environment and lockfile tool used throughout | Not yet verified |
| Pro Git (2nd ed.) | Chacon & Straub | https://git-scm.com/book/en/v2 | W1 | B–I | 2 h (ch. 2–3, 10) | Git internals and workflow | Not yet verified |
| An overview of HTTP | MDN Web Docs (Mozilla) | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | W1, W14 | B | 0.5 h | Request/response model, methods, status codes | Not yet verified |
| Creating your first schema | JSON Schema | https://json-schema.org/learn/getting-started-step-by-step | W1, W3 | B | 0.5 h | Standard for validating JSON | ✔ 2026-11-27 |
| HTTPX documentation | Encode | https://www.python-httpx.org/ | W1, W4 | B | 0.5 h | HTTP client and MockTransport used in tests | Not yet verified |
| pytest documentation | pytest-dev | https://docs.pytest.org/en/stable/ | all | B | 1 h | Testing framework | Not yet verified |
| Pydantic documentation | Pydantic | https://docs.pydantic.dev/latest/ | W3, W21 | I | 1 h | Typed validation and structured outputs | Not yet verified |
| OpenAI API documentation | OpenAI | https://platform.openai.com/docs | W1, W3, W4 | I | per topic | Request formats, function calling, model list and pricing | Not yet verified |
| Claude API documentation | Anthropic | https://docs.anthropic.com/ | W1, W3, W4, W17 | I | per topic | Messages API, tool use, extended thinking, prompt caching | Not yet verified |
| Gemini API documentation | Google | https://ai.google.dev/gemini-api/docs | W3, W4 | I | per topic | Multimodal inputs, function calling | Not yet verified |
| Building effective agents | Anthropic (Schluntz & Zhang) | https://www.anthropic.com/engineering/building-effective-agents | W4, W18 | I | 0.5 h | Workflows vs agents; when to keep it simple. The page notes that the tooling has since evolved | ✔ 2026-11-27 |
| PyTorch tutorials | PyTorch Foundation | https://pytorch.org/tutorials/ | W2, W8 | I | 2 h | Tensors, autograd, training loops (check Intel-Mac wheel support before installing) | Not yet verified |
| ComfyUI documentation | Comfy Org | https://docs.comfy.org/ | W9–W12 | I | 3 h | Nodes, workflows, server API | Not yet verified |
| ComfyUI repository | Comfy Org (originally comfyanonymous) | https://github.com/comfyanonymous/ComfyUI | W9–W12 | I | 1 h | Source, API examples, install notes; the repository now lives under the Comfy-Org owner | ✔ 2026-11-27 |
| n8n documentation | n8n | https://docs.n8n.io/ | W13–W16 | B–I | 3 h | Triggers, expressions, credentials, error workflows | Not yet verified |
| Model Context Protocol | MCP project | https://modelcontextprotocol.io/ | W19, W22 | I | 2 h | Specification, SDKs, security model | Not yet verified |
| Supabase AI & Vectors | Supabase | https://supabase.com/docs/guides/ai | W5–W7, W14 | I | 2 h | pgvector on Supabase, hybrid search, RLS | Not yet verified |
| pgvector | pgvector project | https://github.com/pgvector/pgvector | W5 | I | 1 h | Vector types, distance operators, HNSW/IVFFlat indexes | ✔ 2026-11-27 |
| FastAPI documentation | S. Ramírez | https://fastapi.tiangolo.com/ | W21 | I | 2 h | Typed APIs, dependency injection, OpenAPI | Not yet verified |
| Docker — Get started | Docker | https://docs.docker.com/get-started/ | W13, W21 | B | 1.5 h | Containers, images, Compose | Not yet verified |
| LangGraph documentation | LangChain | https://langchain-ai.github.io/langgraph/ | W18, W20 | I | 2 h | Stateful agent graphs, checkpoints, interrupts | Not yet verified |
| Remotion documentation | Remotion | https://www.remotion.dev/docs/ | W15 | I | 2 h | Programmatic video (already used in Balena and Billionslight) | Not yet verified |
| ElevenLabs documentation | ElevenLabs | https://elevenlabs.io/docs | W15 | B | 1 h | TTS, voices, music; check licensing for commercial use | Not yet verified |
| OWASP Top 10 for LLM Applications | OWASP GenAI Security Project | https://genai.owasp.org/llm-top-10/ | W19, W23 | I | 1 h | Standard LLM threat list | Not yet verified |

## Explanations and references
| Title | Author | URL | Module(s) | Diff. | Est. time | Why it is relevant | Verified |
|---|---|---|---|:-:|---|---|---|
| Neural Networks (video series) | 3Blue1Brown (G. Sanderson) | https://www.3blue1brown.com/topics/neural-networks | W2 | B | 2 h | Visual intuition for gradient descent, backprop, attention | Not yet verified |
| The Illustrated Transformer | J. Alammar | https://jalammar.github.io/illustrated-transformer/ | W2 | B–I | 1 h | Step-by-step attention diagrams | Not yet verified |
| Speech and Language Processing (3rd ed. draft) | D. Jurafsky & J. H. Martin | https://web.stanford.edu/~jurafsky/slp3/ | W2, W5, W7 | I | per chapter | Authoritative textbook: tokenisation, embeddings, IR | Not yet verified |

## Papers
Papers cited in the curriculum are listed in each week's `RESEARCH_READING.md` and each
experiment's `EXPERIMENT.md`, with full citations (authors, year, venue, arXiv ID). Record each
one you read in `research/literature-review/LITERATURE_LOG.md`, and check whether arXiv
preprints have a peer-reviewed version.
