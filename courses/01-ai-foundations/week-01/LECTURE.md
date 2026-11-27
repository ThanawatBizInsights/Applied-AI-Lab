# Week 01 — Lecture (2 hours)

**How to use this lecture.** Read one section at a time. When you see **🔮 Predict**, write
your answer in `REFLECTION.md` *before* reading on or running anything. Wrong predictions are
useful: they show exactly where your mental model differs from reality.

| § | Topic | Time |
|---|---|---:|
| 1 | Reproducible Python environments | 20 min |
| 2 | Git from the inside | 25 min |
| 3 | HTTP: what an API call really is | 25 min |
| 4 | JSON, Unicode and Thai text | 20 min |
| 5 | Secrets and configuration | 10 min |
| 6 | Anatomy of a brand-aware LLM application | 20 min |

---

## 1. Reproducible Python environments

### 1.1 The problem
A Python program depends on three things that differ between machines: the **interpreter**
(3.11 or 3.13?), the **installed packages** and their versions, and the **operating system and
CPU** (Intel x86_64 vs Apple Silicon arm64, macOS vs Linux). "It works on my machine" means one
of these differs.

### 1.2 What `import` actually does
When you write `import httpx`, Python searches the directories in `sys.path` in order. One of
them is a `site-packages` directory belonging to the *interpreter that is running*. If you
installed httpx into a different interpreter's `site-packages`, the import fails, even though
"it is installed".

> 🔮 **Predict:** you run `pip install httpx` and then `python3 -c "import httpx"` fails.
> Give two possible reasons.

### 1.3 Virtual environments
A virtual environment is just a directory (`.venv/`) containing a link to an interpreter and
its own empty `site-packages`. Activating it puts its `bin/` first on your `PATH`. Each project
then has its own packages, so upgrading one project cannot break another.

### 1.4 Declared vs locked dependencies
- `pyproject.toml` **declares** what the project needs: `httpx>=0.27`. That is a range.
- `uv.lock` **locks** the exact versions (and hashes) that were resolved: `httpx==0.28.1`.
  Commit the lockfile. Anyone who runs `uv sync` gets the same versions.

Without a lockfile, two installs a month apart can resolve different versions. That is a
reproducibility failure, and for experiments (Research Mode) a validity failure too.

### 1.5 Why `uv`
`uv` replaces `pip`, `venv`, `pip-tools` and `pyenv` with one fast tool: it installs Python
versions, creates `.venv`, resolves and locks dependencies, and runs commands inside the
environment (`uv run pytest`). The principles above apply whatever tool you use. `uv` just
makes the correct workflow the easy one.

### 1.6 Intel Mac realities
- Many AI packages publish pre-built **wheels** per platform. Some have stopped publishing
  wheels for macOS x86_64 (PyTorch is the important example: check its install page for the
  last version that supports Intel Macs). Without a wheel, pip tries to compile from source,
  which often fails.
- There is no CUDA on a Mac, and Intel Macs have no Apple-Silicon GPU acceleration (MPS) either.
  Diffusion, video generation and fine-tuning therefore run on cloud GPUs in this programme.
- Rule (from `AGENTS.md`): check compatibility and get approval before installing large or
  GPU packages locally.

**Misconception:** "Use `sudo pip install` when it fails." Never. It writes into the system
Python and can break macOS tools. The fix is always the right environment.

---

## 2. Git from the inside

### 2.1 Git stores snapshots, not diffs
Git is a **content-addressed object store**. Every object is named by the hash of its content:

| Object | Contains |
|---|---|
| **blob** | the bytes of one file (no name) |
| **tree** | a directory listing: names → blob or tree hashes |
| **commit** | a pointer to one tree (the full snapshot) + parent commit(s) + author + message |

Change one byte of a file and you get a new blob, a new tree above it and a new commit. The
unchanged files reuse their existing blobs, which is why snapshots are cheap.

### 2.2 Branches are just pointers
A branch is a tiny file containing one commit hash. `HEAD` points to the branch you are on.
Committing creates a new commit whose parent is the current one, and moves the branch pointer
forward. Commits form a **directed acyclic graph** (DAG); merges are commits with two parents.

> 🔮 **Predict:** how many bytes is the file `.git/refs/heads/main`? (Lab B checks this.)

### 2.3 The three places your work lives
Working directory → (`git add`) → **index/staging area** → (`git commit`) → repository →
(`git push`) → remote (GitHub). `git status` tells you what differs between these places.

### 2.4 Why a committed secret is a disaster
Because commits are immutable snapshots chained by hashes, deleting a key in a *later*
commit does not remove it from history: the old blob is still there, and on a public
repository it may already have been scraped by bots within minutes. **The only safe response
to a leaked key is to revoke and rotate it at the provider**, and then clean the history.
This is why `.gitignore` covers `.env` and why `scripts/validate_repo.py` scans for keys.

### 2.5 The workflow you use in this programme
`main` is protected. Work on a branch (`week-01/brand-assistant`), commit small logical steps,
push and open a pull request (PR). The PR is where ChatGPT or Claude reviews your work
(Review Mode), and where your evidence of learning accumulates.

---

## 3. HTTP: what an API call really is

### 3.1 The request/response model
HTTP is a text protocol in which a client sends a **request** and a server sends back a
**response**. Each exchange is independent (**stateless**). Any "conversation memory" must be
sent again by the client every time, which is exactly why LLM chat APIs make you resend the
whole message history.

A real LLM request, written out:

```http
POST /v1/messages HTTP/1.1
Host: api.anthropic.com
x-api-key: <your key>
anthropic-version: 2023-06-01
content-type: application/json

{"model": "<model id>", "max_tokens": 200, "system": "You write for Balena Roastery…",
 "messages": [{"role": "user", "content": "<user_input>\nCold Brew Original\n</user_input>"}]}
```

and the response:

```http
HTTP/1.1 200 OK
content-type: application/json

{"content": [{"type": "text", "text": "…"}], "usage": {"input_tokens": 182, "output_tokens": 64}, …}
```

That is all an "AI API" is: an HTTPS POST with a JSON body and a key in a header. SDKs only
wrap this. Week 1 makes you write it by hand, so the SDKs hold no mystery later.

### 3.2 Methods and idempotency
- `GET` reads, `POST` creates or performs an action, `PUT` replaces, `DELETE` removes.
- An operation is **idempotent** if doing it twice has the same effect as doing it once.
  GET, PUT and DELETE are meant to be idempotent; POST usually is not. A generation request
  is a POST: retrying it costs money again and may return a different answer.

> 🔮 **Predict:** why does an LLM completion use POST and not GET, even though you are
> "getting" text?

### 3.3 Status codes
| Range | Meaning | LLM-API examples | What your code does |
|---|---|---|---|
| 2xx | success | 200 OK | parse the body |
| 4xx | **your** request is wrong | 400 bad JSON, 401 bad key, 403 not allowed, 404 wrong URL, 429 too many requests | fix it; 429 → wait and retry |
| 5xx | **the server** failed | 500, 503 overloaded | retry later, with backoff |

Only some failures are worth retrying (408, 429, 5xx). Retrying a 400 just repeats the same
mistake. Retrying a 401 can get a key locked. Exercise 2 makes you encode this.

### 3.4 Headers, authentication and TLS
Headers carry metadata: content type, API version and authentication. Providers authenticate
with either `Authorization: Bearer <key>` (OpenAI style) or a custom header such as
`x-api-key` (Anthropic) or `x-goog-api-key` (Gemini). HTTPS (TLS) encrypts all of this in
transit. Your key is still exposed if you log the headers.

### 3.5 Timeouts and rate limits
Networks fail. A request without a timeout can hang forever. Always set one: httpx's default
is 5 seconds, which is too short for long generations, so the starter code uses 30 seconds.
Providers enforce rate limits (requests and tokens per minute) and answer 429 when you exceed
them. Week 4 adds retries with exponential backoff. This week you only *classify* errors.

---

## 4. JSON, Unicode and Thai text

### 4.1 JSON's data model
JSON has exactly six types: object, array, string, number, `true`/`false`, `null`. It has no
dates, no comments, no tuples and no distinction between integer and float. Dates travel as
ISO 8601 strings (`"2026-12-01T09:00:00+07:00"`), and the receiver must parse and validate them.

### 4.2 Unicode vs UTF-8
A **code point** is a number assigned to a character (`ก` is U+0E01). **UTF-8** is a way
of encoding code points as bytes: ASCII characters take 1 byte, and Thai characters take
**3 bytes**. So `len("กาแฟ") == 4` characters, but 12 bytes on disk and on the wire.

> 🔮 **Predict:** what does `json.dumps({"t": "กาแฟ"})` print? (Exercise 1 checks this.)

By default Python's `json.dumps` escapes non-ASCII characters as `ก…`. That is valid
JSON but unreadable in files and diffs. Use `ensure_ascii=False` and always read and write
files with `encoding="utf-8"`. Never rely on the platform default.

### 4.3 What a "character" is in Thai
Thai stacks vowels and tone marks on consonants: `กำ` is one visible unit made of two code
points, and `ที่` is three. `len()` counts code points, not what a reader sees. Character
limits therefore need care: App Store limits, LINE message limits and your `max_chars` rule
may count differently. Week 2 shows how tokenizers see the same text.

### 4.4 Thai has no spaces between words
`ท้องลายขาว` ("striped white belly") contains the substring `ขา` ("leg"). Searching Thai text
for a forbidden word with a plain substring match gives **false positives**. English has a
milder version: `leg` is inside `elegant`, which is why ASCII terms are matched on word
boundaries. Word segmentation for Thai (e.g. with PyThaiNLP) arrives in Weeks 5–7. This week
you use an explicit `ignore_within` list, and measure where it still fails.

### 4.5 Validate at the boundary
Data from files, users, webhooks and models is **untrusted**. Parse and validate it once, where
it enters your system, and convert it to typed objects (`BrandProfile`). The rest of the code
can then trust it. A clear error at load time ("rule r9: unknown type 'vibes'") is far cheaper
than a confusing failure three functions later. JSON Schema is the standard language for these
rules; you use it with pydantic in Week 3.

---

## 5. Secrets and configuration

- Configuration that differs between machines (keys, model IDs, limits) lives in **environment
  variables**, not in code. `.env` holds your values and is git-ignored; `.env.example` documents
  every variable with placeholders and *is* committed.
- **Fail fast:** check configuration at start-up and give a clear message ("ANTHROPIC_API_KEY is
  still a placeholder"), not a confusing 401 later.
- **Never print secrets.** `Settings.__repr__` in `config.py` masks the key, so even
  `print(settings)` is safe. Read that code.
- **Budgets are a security control.** A loop bug that sends 10,000 requests is a cost incident.
  `RequestBudget` stops a run after `LLM_MAX_REQUESTS_PER_RUN` requests.

> 🔮 **Predict:** list three places a key can leak *without* being committed to Git.

---

## 6. Anatomy of a brand-aware LLM application

```
brands/*.json ──► loader ──► BrandProfile ──► prompts.build_messages ──► (system, messages)
   (data)        (validate)    (typed)                                         │
                                                                               ▼
                                         LLMClient.complete()  ◄── FakeLLMClient | AnthropicClient | OpenAIClient
                                                                               │
                                                                               ▼
                         checks.check_output(text, brand, task) ──► CheckResult ──► PENDING_HUMAN_APPROVAL
                                                                               │
                                                                               ▼
                                                                  runs/<date>.jsonl (evidence)
```

Four design decisions, and why:

1. **Brand rules are data, not code.** Rules live in JSON, so a new brand (Billionslight,
   Seoa Ryn) needs a file, not a code change. That is the start of the capstone's brand
   management service.
2. **One client interface, many providers.** `prompts.py` and `checks.py` never import a
   provider. You can develop offline with the fake client and swap providers by configuration.
   This is the **adapter pattern**, and it becomes the Week 4 Gateway.
3. **Instructions and input are separated.** Stable instructions go in the system prompt.
   Untrusted input is fenced in `<user_input>` tags in the user message. This does not make
   prompt injection impossible, but it is the necessary first step (Week 3).
4. **Never trust model output.** Deterministic checks run on every output, and everything waits
   for **human approval**. A model can and will write "Balena wiggles her little legs". The
   check is cheap; a published mistake is expensive.

**Cost model.** You pay per token, input and output priced separately (output usually costs
several times more). Cost of a request = input tokens × input price + output tokens × output
price. The system prompt is resent with *every* request, so a long brand guide costs money on
every call. Week 2 measures that precisely for Thai.

> 🔮 **Predict:** your Balena system prompt is 400 tokens, the input 30 and the output 120.
> Which part dominates the cost at typical prices: input or output? Check with
> `estimate_cost_usd()` using today's price for any small model, and note the date and source.

---

### Key terms
virtual environment · lockfile · wheel · blob/tree/commit · branch pointer · stateless ·
idempotent · status code families · bearer token · UTF-8 · code point · validation boundary ·
adapter pattern · prompt injection · human-in-the-loop
