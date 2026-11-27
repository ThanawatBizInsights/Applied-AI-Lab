# Week 01 — Guided lab (2 hours)

Commands are for **macOS (zsh) on an Intel MacBook**. Run everything from the repository root
unless stated otherwise. Each checkpoint ends with a commit, which is your lab evidence (25% of
the grade).

| Part | Topic | Time |
|---|---|---:|
| A | Environment setup | 30 min |
| B | Git drills | 30 min |
| C | Exercises 1–3 (JSON, HTTP, secrets) | 55 min |
| D | Optional: one real API call (needs approval) | 5 min |

---

## Part A — Environment setup (30 min)

**A1. Check the machine.**
```bash
uname -m            # expect x86_64 on an Intel Mac
sw_vers -productVersion
xcode-select -p || xcode-select --install   # command-line tools (git, compilers)
```

**A2. Install uv** (once). Choose one method and record which in your journal:
```bash
brew install uv
```
or the official installer from the uv documentation (read the script before running it):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then:
```bash
uv --version
```

**A3. Clone the repository and create your branch.**
```bash
git clone https://github.com/ThanawatBizInsights/Applied-AI-Lab.git
cd Applied-AI-Lab
git switch -c week-01/brand-assistant
```
(If the setup pull request is not merged yet, start from it: `git switch setup/ai-learning-academy`,
then create your branch from there.)

**A4. Create the environment from the lockfile.**
```bash
uv python install 3.12
uv sync --extra dev
uv run python -c "import sys; print(sys.executable, sys.version)"
```
> 🔮 Predict: which directory does `sys.executable` point to? Why does that matter?

**A5. Run the scaffold tests.** All must pass before you start.
```bash
uv run pytest
```
Expected: every collected test passes, plus a number of `deselected` tests: those are *your*
assignment tests, which only run with `-m assignment`.

**A6. Configure secrets safely.**
```bash
cp .env.example .env
git check-ignore -v .env   # must print the .gitignore rule that ignores it
```
Leave `LLM_PROVIDER=fake`. You do not need a key this week.

✅ **Checkpoint A:** `git commit --allow-empty -m "Lab A: environment ready (uv <version>, Python <version>)"`

---

## Part B — Git drills (30 min)

**B1. See the object model for yourself.**
```bash
git log --oneline -3
git cat-file -t HEAD           # → commit
git cat-file -p HEAD           # tree hash, parent, author, message
git cat-file -p 'HEAD^{tree}' | head   # names → blob/tree hashes
wc -c .git/HEAD
cat .git/HEAD                  # HEAD points to your branch
```
> 🔮 Before running `wc -c`: how many bytes do you expect in a branch file? Then check
> `git rev-parse --git-path refs/heads/week-01/brand-assistant` after your first commit.

**B2. Prove that a snapshot reuses unchanged files.**
Add a line to `learning-journal/README.md`, commit, then compare the trees of the two commits:
```bash
git diff-tree -r HEAD~1 HEAD   # only the changed blob appears
```

**B3. Practise a safe merge conflict.**
```bash
git switch -c drill/conflict
echo "Balena is a round whale." > learning-journal/drill.md && git add . && git commit -m "drill: A"
git switch week-01/brand-assistant
echo "Balena is a short whale." > learning-journal/drill.md && git add . && git commit -m "drill: B"
git merge drill/conflict       # conflict! open the file, keep "short, round", then:
git add learning-journal/drill.md && git commit -m "drill: resolve conflict"
git branch -d drill/conflict
```

**B4. The secret drill (no real secret).**
```bash
echo "OPENAI_API_KEY=sk-not-a-real-key-just-a-drill-0000" > drill.env   # secret-scan: allow (fake drill value)
git status                     # is drill.env ignored? (.env.* is ignored, but is this name?)
```
> 🔮 Predict first, then check. If it is *not* ignored, do **not** commit it. Delete it, and
> write in your reflection what would have happened to a real key on a public repository.
> Then run `uv run python scripts/validate_repo.py` to see the repository's secret scan.

✅ **Checkpoint B:** `git rm learning-journal/drill.md && git commit -m "Lab B: Git drills done"`

---

## Part C — Exercises (55 min)

Open `courses/01-ai-foundations/week-01/starter-code/w01_exercises/`. Each file starts with
**🔮 Predict** questions: answer them in `REFLECTION.md` first. Then implement the TODOs and
run that exercise's tests:

```bash
T=courses/01-ai-foundations/week-01/tests/test_w01_exercises.py
uv run pytest -m assignment $T -k "utf8 or json or posts or validate"      # Exercise 1
uv run pytest -m assignment $T -k "request or status or extract"           # Exercise 2
uv run pytest -m assignment $T -k "mask or require_env or find_secrets"    # Exercise 3
```

| Exercise | You learn | Stuck? Hint ladder |
|---|---|---|
| 1 `ex01_json_thai.py` (15 min) | UTF-8 vs characters, `ensure_ascii`, boundary validation | ① Lecture §4 ② `str.encode`, `json.dumps(…, ensure_ascii=False, indent=2)` ③ check types *before* values |
| 2 `ex02_http.py` (25 min) | Wire formats of two providers; status classes; mock servers | ① Lecture §3 ② `httpx.Request("POST", url, headers=…, json=…)` ③ `json.loads(req.content)` shows what you built |
| 3 `ex03_secrets.py` (15 min) | Masking, fail-fast config, secret scanning | ① Lecture §5 ② compare with `brand_assistant/config.py` ③ test one regex at a time in a Python shell |

Ask an AI assistant for hints in **Teaching Mode** (it will go step by step, per `AGENTS.md`).
Record in the "Who wrote what" table if any code came from AI.

✅ **Checkpoint C:** one commit per exercise, e.g. `git commit -m "Lab C1: JSON and UTF-8 exercise" --trailer "AI-Assisted: none"`

---

## Part D — Optional: one real API call (5 min, needs your approval)

**Cost estimate:** one request of about 50 input and 50 output tokens costs a small fraction
of one US cent with any small model. Look up the current price and model ID on the provider's
official pricing and models pages, and write both, with the date, in
`evaluations/benchmarks/model-registry.csv`.

Put your key in `.env` (never in the command line history), then:
```bash
set -a; source .env; set +a
curl -s https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d "{\"model\": \"$ANTHROPIC_MODEL\", \"max_tokens\": 50,
       \"messages\": [{\"role\": \"user\", \"content\": \"ทักทายสั้นๆ เป็นภาษาไทย\"}]}"
```
Compare the response with the JSON you parsed in Exercise 2. What fields did you not expect?

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `uv: command not found` | shell not reloaded | open a new terminal, or `source ~/.zshrc` |
| `ModuleNotFoundError: brand_assistant` when using `python -m` | starter code not on the path | prefix with `PYTHONPATH=courses/01-ai-foundations/week-01/starter-code` |
| Tests say `deselected` and nothing runs | you forgot `-m assignment` | add `-m assignment` |
| Thai shows as `???` or boxes in the terminal | terminal font or locale | `echo $LANG` should be a UTF-8 locale such as `en_US.UTF-8` |
| `SSL: CERTIFICATE_VERIFY_FAILED` | corporate proxy or outdated certificates | update macOS certificates; never disable TLS verification |
| `401` from the provider | wrong or placeholder key | check `.env`; regenerate the key if unsure |
| `429` | rate limit | wait; you are not meant to loop this week |
| `git push` rejected | branch protection or no upstream | `git push -u origin week-01/brand-assistant`, then open a PR |
| You committed a key | — | **revoke the key at the provider first**, then ask for help cleaning history |
