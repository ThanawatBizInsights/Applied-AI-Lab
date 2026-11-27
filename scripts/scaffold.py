#!/usr/bin/env python3
"""Create week outlines (2–24), course READMEs, project workspaces and experiment templates.

Safe to re-run: it NEVER overwrites an existing file (prints "skip" instead). To regenerate a
file, delete it first and review the diff before committing.

    uv run python scripts/scaffold.py            # create missing files
    uv run python scripts/scaffold.py --dry-run  # list what would be created
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from data_experiments import EXPERIMENTS  # noqa: E402
from data_projects import PROJECTS, VERIFIED_ON  # noqa: E402
from data_weeks import COURSES, WEEKS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TIME_SPLIT = [("Theoretical instruction", 2, "LECTURE.md"), ("Guided laboratory", 2, "LAB.md"),
              ("Independent project development", 3, "ASSIGNMENT.md"), ("Research reading", 1, "RESEARCH_READING.md"),
              ("Assessment", 1, "QUIZ.md"), ("Documentation and reflection", 1, "REFLECTION.md")]
WEEK_FILES = ["README.md", "LEARNING_OBJECTIVES.md", "LECTURE.md", "LAB.md", "ASSIGNMENT.md",
              "RESEARCH_READING.md", "QUIZ.md", "REFLECTION.md", "RESOURCES.md"]
PROJECT_FILES = ["README.md", "PROJECT_CONTEXT.md", "LEARNING_GOALS.md", "BRAND_GUIDELINES.md",
                 "TECH_STACK.md", "ROADMAP.md", "EXPERIMENTS.md", "EVALUATION.md"]
OUTLINE_BANNER = ("> **Status: OUTLINE.** Full materials are written when you finish the previous week "
                  "(see `ROADMAP.md`). Ask Claude or ChatGPT: *\"Expand week {n:02d} materials\"*.\n")

created: list[Path] = []
skipped: list[Path] = []
DRY = False


def write(path: Path, text: str) -> None:
    if path.exists():
        skipped.append(path)
        return
    created.append(path)
    if DRY:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullets(items, prefix="- ") -> str:
    return "\n".join(f"{prefix}{i}" for i in items)


def numbered(items) -> str:
    return "\n".join(f"{k}. {i}" for k, i in enumerate(items, 1))


def week_dir(w) -> Path:
    return ROOT / "courses" / w["course"] / f"week-{w['n']:02d}"


def project_title(slug: str) -> str:
    return next(p["name"] for p in PROJECTS if p["slug"] == slug)


def project_links(slugs, depth="../../../") -> str:
    return ", ".join(f"[{project_title(s)}]({depth}projects/{s}/README.md)" for s in slugs)


# --------------------------------------------------------------------------- weeks
def render_week(w) -> None:
    d, n, a = week_dir(w), w["n"], w["assignment"]
    banner = OUTLINE_BANNER.format(n=n)
    exp = (f"\n**Research strand:** this week contributes to "
           f"[{w['experiment']}](../../../research/experiments/README.md).\n") if w["experiment"] else ""
    time_table = "\n".join(f"| {name} | {h} | [`{f}`]({f}) |" for name, h, f in TIME_SPLIT)

    write(d / "README.md", f"""# Week {n:02d} — {w['title']}

{COURSES[w['course']]} · **10 hours** · Linked projects: {project_links(a['projects'])}

{banner}
## Prerequisites
{bullets(w['prereq'])}

## Time plan
| Activity | Hours | File |
|---|---:|---|
{time_table}
| **Total** | **10** | |

## Assignment at a glance
**{a['title']}** — {a['brief']}

## Hardware and cost
{w['hardware']}
{exp}
## Completion evidence (AGENTS.md §5)
- [ ] Assignment tests pass (`uv run pytest -m assignment courses/{w['course']}/week-{n:02d}`)
- [ ] Acceptance criteria checked off in `ASSIGNMENT.md`
- [ ] Quiz score recorded in `PROGRESS.md`
- [ ] `REFLECTION.md` written in your own words
- [ ] Review saved in `reviews/`
- [ ] Study hours logged in `learning-journal/`
""")

    write(d / "LEARNING_OBJECTIVES.md", f"""# Week {n:02d} — Learning objectives

By the end of this week you should be able to:

{numbered(w['objectives'])}

## Competencies affected (see `PROGRESS.md`)
Evidence from this week can raise competencies by **at most one level**, and only with a linked
commit, test or report.
""")

    write(d / "LECTURE.md", f"""# Week {n:02d} — Lecture (2 hours): {w['title']}

{banner}
Principles before tools. Planned sequence:

{numbered(w['principles'])}

Each section will include: the core idea, a worked example linked to {project_links(a['projects'])},
a "predict before you run" question and a common misconception.
""")

    write(d / "LAB.md", f"""# Week {n:02d} — Guided lab (2 hours)

{banner}
## Planned checkpoints
{numbered(w['lab'])}

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
{bullets(w['troubleshoot'])}
""")

    write(d / "ASSIGNMENT.md", f"""# Week {n:02d} — Assignment (3 hours): {a['title']}

**Linked projects:** {project_links(a['projects'])}

## Brief
{a['brief']}

## Deliverables
{bullets(a['deliverables'])}

## Acceptance criteria
{bullets(a['criteria'], '- [ ] ')}
- [ ] No secrets, customer data, private footage or children's data committed (`scripts/validate_repo.py` passes)
- [ ] "Who wrote what" table completed below

## Evaluation metrics
{bullets(a['metrics'])}

## Marking rubric (maps to programme weights)
| Component | Weight | Distinction (≥ 70%) looks like |
|---|---:|---|
| Practical project | 40% | All acceptance criteria met; clean, tested, documented code |
| Technical lab | 25% | All lab checkpoints committed with working output |
| Research and evaluation | 20% | Metrics measured (not estimated), limitations stated |
| Knowledge assessment | 10% | Quiz ≥ 70% |
| Documentation | 5% | Reflection explains decisions in your own words |

## Troubleshooting
{bullets(w['troubleshoot'])}

## Submission
| Item | Link / commit | Who wrote it (me / AI-reviewed / AI-generated) |
|---|---|---|
| | | |
""")

    readings = "\n".join(f"| {c} | {why} | ☐ |" for c, why in w["readings"])
    write(d / "RESEARCH_READING.md", f"""# Week {n:02d} — Research reading (1 hour)

| Reading | Why it matters this week | Read |
|---|---|:-:|
{readings}

For each reading, note in `REFLECTION.md`: the main claim, the evidence, one limitation, and
one way it changes what you build. Links are verified when the week is expanded.
""")

    write(d / "QUIZ.md", f"""# Week {n:02d} — Knowledge check (1 hour)

{banner}
Planned topics (questions are written when the week is expanded, so they reflect what you
actually studied):

{bullets(w['quiz'])}

Format: 10 questions (multiple choice, short answer and one "explain this code"), marked out
of 20. Record your score in `PROGRESS.md`.
""")

    write(d / "REFLECTION.md", f"""# Week {n:02d} — Reflection (1 hour)

Write in your own words. AI may ask you questions about this; it must not write it for you.

## Prompts
{numbered(w['reflection'] + ['Explain your implementation as if to a colleague: structure, key decisions, what you would change.', 'What did AI generate, what did you write, and what did you learn by doing it yourself?'])}

## My reflection
_Write here._

## Hours spent
| Activity | Planned | Actual |
|---|---:|---:|
| Lecture | 2 | |
| Lab | 2 | |
| Assignment | 3 | |
| Reading | 1 | |
| Quiz | 1 | |
| Reflection | 1 | |
""")

    write(d / "RESOURCES.md", f"""# Week {n:02d} — Resources

Details (URL, difficulty, time, verification date) are in
[`resources/RESOURCE_LIBRARY.md`](../../../resources/RESOURCE_LIBRARY.md).

{bullets(w['resources'])}
""")

    write(d / "starter-code" / "README.md", f"""# Week {n:02d} — Starter code

Created when the week is expanded. It will contain skeleton modules with `TODO` markers and
docstrings that describe the expected behaviour. It will not contain solutions.
""")
    write(d / "tests" / "README.md", f"""# Week {n:02d} — Tests

Created when the week is expanded. Tests for your own work are marked `@pytest.mark.assignment`
and run with:

```bash
uv run pytest -m assignment courses/{w['course']}/week-{n:02d}
```
""")


def render_course_readmes() -> None:
    for slug, title in COURSES.items():
        weeks = [w for w in WEEKS if w["course"] == slug]
        rows = []
        if slug == "01-ai-foundations":
            rows.append("| [01](week-01/README.md) | Python development environment, Git, APIs and JSON | **Complete materials** |")
        rows += [f"| [{w['n']:02d}](week-{w['n']:02d}/README.md) | {w['title']} | Outline |" for w in weeks]
        mains = {
            "01-ai-foundations": "Multi-model AI Gateway (`shared/llm-gateway/`)",
            "02-llm-engineering": "CheckKhum Insurance Intelligence and Billionslight Product Intelligence (`shared/knowledge-engine/`)",
            "03-comfyui": "Balena, Animal Pairs, Phonics Pond, Seoa Ryn and LumiTale Studio (`shared/comfyui-workflows/`)",
            "04-automation": "Balena Content Factory, Iris's Family Video Studio, CheePao Affiliate Intelligence and CheckKhum Customer Operations (`shared/automation/`)",
            "05-agentic-ai": "Phonics Pond Educational AI, Rusty Personalisation Engine and AI Software Development Agent (`shared/mcp-servers/`)",
            "06-platform-engineering": "Personal AI Studio OS (`capstone/`)",
        }[slug]
        write(ROOT / "courses" / slug / "README.md", f"""# {title}

**Main project:** {mains}

| Week | Topic | Materials |
|---|---|---|
{chr(10).join(rows)}

Each week is 10 hours: 2 lecture, 2 lab, 3 assignment, 1 reading, 1 quiz, 1 reflection.
Course grade = average of week grades, using the weights in [`CURRICULUM.md`](../../CURRICULUM.md#5-assessment).
""")


# --------------------------------------------------------------------------- projects
def render_project(p) -> None:
    d = ROOT / "projects" / p["slug"]
    if p["repo"]:
        repo_rows = "\n".join(f"| `{r}` | {vis} | `{sha}` | {date} |" for r, vis, sha, date in p["repo"])
        repo_table = f"| Repository | Visibility | Commit inspected | Last commit date |\n|---|---|---|---|\n{repo_rows}"
    else:
        repo_table = "_No GitHub repository found for this project. This folder is a learning workspace only._"
    ws_note = "\n> This is a **learning workspace only**: no production code for this project exists in this lab.\n" if p.get("learning_workspace_only") else ""
    b = p["brand"]
    weeks = ", ".join(f"W{n:02d}" for n in p["weeks"])

    write(d / "README.md", f"""# {p['name']} — learning workspace
{ws_note}
Everything this lab knows about **{p['name']}**, and how the curriculum uses it.

| File | Contents |
|---|---|
| [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) | Verified facts, user-provided facts, open questions |
| [LEARNING_GOALS.md](LEARNING_GOALS.md) | What you learn through this project, by week |
| [BRAND_GUIDELINES.md](BRAND_GUIDELINES.md) | Rules that AI outputs must follow |
| [TECH_STACK.md](TECH_STACK.md) | Verified and proposed technology, licences |
| [ROADMAP.md](ROADMAP.md) | Proposed learning milestones |
| [EXPERIMENTS.md](EXPERIMENTS.md) | Experiments that use this project |
| [EVALUATION.md](EVALUATION.md) | Metrics and how they are measured |

**Curriculum weeks:** {weeks}. **Experiments:** {', '.join(p['experiments'])}.

Code and data for exercises go in subfolders created during the relevant week. Use synthetic
or public data only.
""")

    write(d / "PROJECT_CONTEXT.md", f"""# {p['name']} — Project context

Status tags: **[VERIFIED]** read from the repository · **[USER-PROVIDED]** from the learner's
brief · **[PROPOSED]** learning work, not an existing feature · **[NEEDS CONFIRMATION]**.
Verified on {VERIFIED_ON} by read-only inspection. No changes were made to any project repository.

## Repositories
{repo_table}

## [VERIFIED] What the repository shows
{bullets(p['verified'])}

## [USER-PROVIDED] Focus and constraints
{bullets(p['user'])}

## [PROPOSED] Role in this curriculum
{bullets(p['roadmap'])}

## [NEEDS CONFIRMATION]
{bullets(p['confirm'])}

## Decisions log
| Date | Decision | Why | Who |
|---|---|---|---|
| | | | |
""")

    write(d / "LEARNING_GOALS.md", f"""# {p['name']} — Learning goals

Weeks where this project is the main or a supporting example: **{weeks}**.

{bullets([f'**{r.split(":")[0]}** —{r.split(":", 1)[1]}' if ':' in r else r for r in p['roadmap']])}

## Personal goals (fill in)
- What do I want this project to gain from the programme?
- Which skill do I most want to prove with it in my portfolio?
""")

    write(d / "BRAND_GUIDELINES.md", f"""# {p['name']} — Brand guidelines for AI outputs

{b['summary']}

## Must
{bullets(b['must'])}

## Never
{bullets(b['never'])}

## Voice
{b['voice']}

## Languages
{b['languages']}

## How these rules are enforced
- Encoded as machine-checkable rules where possible (see Week 1 `brand_assistant/brands/*.json`
  for Balena, CheckKhum and Little Snowy Owl).
- Visual rules are scored with a rubric in `EVALUATION.md`.
- A human approves anything published.

_Source: learner's brief [USER-PROVIDED], plus repository facts where noted in PROJECT_CONTEXT.md._
""")

    write(d / "TECH_STACK.md", f"""# {p['name']} — Technology stack

## [VERIFIED] From the repository
{bullets(p['stack_verified']) if p['stack_verified'] else '_Nothing verified (no repository or empty repository)._'}

## [PROPOSED] Added during the curriculum
{bullets(p['stack_proposed'])}

## Model and asset licences
Record **before** using any output commercially.

| Model / dataset / asset | Licence | Commercial use allowed? | Restrictions | Checked on |
|---|---|---|---|---|
| | | | | |
""")

    write(d / "ROADMAP.md", f"""# {p['name']} — Learning roadmap [PROPOSED]

{bullets(p['roadmap'], '- [ ] ')}

These are learning milestones in this lab. They do not change the production project unless
you decide so and record the decision in `PROJECT_CONTEXT.md`.
""")

    write(d / "EXPERIMENTS.md", f"""# {p['name']} — Experiments

| ID | Experiment | Where |
|---|---|---|
""" + "\n".join(
        f"| {e['id']} | {e['title']} | [research/experiments/{e['id']}-{e['slug']}](../../research/experiments/{e['id']}-{e['slug']}/EXPERIMENT.md) |"
        for e in EXPERIMENTS if e["id"] in p["experiments"]) + """

Add project-specific experiments here with the next free ID (EXP-09 onwards).
""")

    write(d / "EVALUATION.md", f"""# {p['name']} — Evaluation

## Metrics
| Metric | How it is measured | Target | Latest result | Evidence |
|---|---|---|---|---|
""" + "\n".join(f"| {m} | _define in the week that introduces it_ | _set before measuring_ | — | — |" for m in p["metrics"]) + """

Rules: set targets **before** measuring; report the model version, date and sample size with
every result; never report a single run as a final result.
""")


# --------------------------------------------------------------------------- experiments
def render_experiment(e) -> None:
    d = ROOT / "research" / "experiments" / f"{e['id']}-{e['slug']}"
    write(d / "EXPERIMENT.md", f"""# {e['id']} — {e['title']}

**Status:** DESIGN (not started) · **Weeks:** {e['weeks']} · **Projects:** {project_links(e['projects'], '../../../')}

## 1. Research question
{e['rq']}

## 2. Hypothesis
{e['hypothesis']}

## 3. Literature and references
{bullets(e['references'])}

_Verify each reference before citing it in a report. Add what you read in `research/literature-review/`._

## 4. Experimental design
- **Design:** controlled comparison; conditions are run on the same items in randomised order.
- **Controls:** {'; '.join(e['controls'])}.
- **Pre-registration:** fill in sections 1–7 and commit them **before** collecting results.

## 5. Baseline
{e['baseline']}

## 6. Variables
**Independent:**
{bullets(e['iv'])}

**Dependent:**
{bullets(e['dv'])}

## 7. Evaluation metrics
{bullets(e['metrics'])}

## 8. Model and software versions
| Component | Version / ID | Date used |
|---|---|---|
| | | |

## 9. Dataset description
{e['dataset']}

Use `templates/DATASET_CARD.md` for the dataset card.

## 10. Cost estimate (approve before running)
| Item | Quantity | Unit price (from provider page, date) | Estimate |
|---|---|---|---|
| | | | |

## 11. Results
Raw results: [`results.csv`](results.csv) (one row per observation). Summary: [`results.json`](results.json).

_Not yet run._

## 12. Limitations and threats to validity
_Fill in after the run: sample size, synthetic-data bias, grader bias, model version drift._

## 13. Reproducibility instructions
```bash
# Fill in: exact commands, seeds, config files, environment
```

## 14. Conclusions
_Only conclusions the data supports. State what the experiment does NOT show._
""")
    buf = io.StringIO()
    csv.writer(buf).writerow(e["columns"])
    write(d / "results.csv", buf.getvalue())
    summary = {"experiment_id": e["id"], "status": "design", "run_date": None, "n_items": None,
               "models": [], "conditions": {}, "metrics": {m: None for m in e["dv"]},
               "hypothesis_supported": None, "notes": ""}
    write(d / "results.json", json.dumps(summary, indent=2, ensure_ascii=False))


def main() -> int:
    global DRY
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    DRY = ap.parse_args().dry_run
    render_course_readmes()
    for w in WEEKS:
        render_week(w)
    for p in PROJECTS:
        render_project(p)
    for e in EXPERIMENTS:
        render_experiment(e)
    print(f"{'would create' if DRY else 'created'}: {len(created)} files; skipped (already exist): {len(skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
