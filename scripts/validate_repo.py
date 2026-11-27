#!/usr/bin/env python3
"""Validate the Applied AI Lab repository. Exit code 0 = all checks pass, 1 = failures.

    uv run python scripts/validate_repo.py          # human-readable report
    uv run python scripts/validate_repo.py --quiet  # failures only

Checks: required files · 24 week folders with the weekly structure · 10 project workspaces ·
curriculum hours = 240 · assessment weights = 100% (and identical in CURRICULUM and PROGRESS) ·
internal Markdown links · consistency of the shared AI instructions · AI_HANDOFF sections ·
experiment templates · secrets · personal data · large or forbidden files.

A line containing the marker `secret-scan: allow` is skipped by the secret scan (use only for
deliberately fake teaching examples, and say so on the line).
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_ROOT = ["README.md", "AGENTS.md", "CLAUDE.md", "CURRICULUM.md", "PROGRESS.md", "ARCHITECTURE.md",
                 "RESEARCH.md", "ROADMAP.md", "CHANGELOG.md", "SECURITY.md", "CONTRIBUTING.md", "AI_HANDOFF.md",
                 ".gitignore", ".env.example", "pyproject.toml"]
REQUIRED_DIRS = ["courses", "projects", "shared/llm-gateway", "shared/knowledge-engine", "shared/comfyui-workflows",
                 "shared/automation", "shared/mcp-servers", "shared/utilities", "research/literature-review",
                 "research/research-questions", "research/experiments", "research/findings", "evaluations/datasets",
                 "evaluations/benchmarks", "evaluations/metrics", "evaluations/reports", "learning-journal",
                 "resources", "templates", "tests", "scripts", "capstone", "portfolio"]
COURSE_WEEKS = {"01-ai-foundations": range(1, 5), "02-llm-engineering": range(5, 9), "03-comfyui": range(9, 13),
                "04-automation": range(13, 17), "05-agentic-ai": range(17, 21),
                "06-platform-engineering": range(21, 25)}
WEEK_FILES = ["README.md", "LEARNING_OBJECTIVES.md", "LECTURE.md", "LAB.md", "ASSIGNMENT.md",
              "RESEARCH_READING.md", "QUIZ.md", "REFLECTION.md", "RESOURCES.md"]
WEEK_DIRS = ["starter-code", "tests"]
PROJECTS = ["balena", "animal-pairs", "phonics-pond", "billionslight", "checkkhum", "iris-family", "rusty",
            "lumitale", "seoa", "cheepao"]
PROJECT_FILES = ["README.md", "PROJECT_CONTEXT.md", "LEARNING_GOALS.md", "BRAND_GUIDELINES.md", "TECH_STACK.md",
                 "ROADMAP.md", "EXPERIMENTS.md", "EVALUATION.md"]
EXPERIMENT_SECTIONS = ["Research question", "Hypothesis", "Literature and references", "Experimental design",
                       "Baseline", "Variables", "Evaluation metrics", "Model and software versions",
                       "Dataset description", "Results", "Limitations", "Reproducibility instructions", "Conclusions"]
HANDOFF_SECTIONS = ["Current learning module", "Current assignment", "Learning objectives", "Completed work",
                    "Files changed", "Architectural decisions", "Test results", "Outstanding issues",
                    "Questions requiring ChatGPT review", "Recommended next steps"]
EXPECTED_WEIGHTS = {"Practical projects": 40, "Technical laboratories": 25, "Research and evaluation": 20,
                    "Knowledge assessments": 10, "Documentation": 5}

FORBIDDEN_EXT = {".safetensors", ".ckpt", ".pt", ".pth", ".bin", ".gguf", ".onnx", ".mp4", ".mov", ".m4v",
                 ".avi", ".mkv", ".wav", ".mp3", ".m4a", ".flac", ".pem", ".key", ".p12", ".sqlite", ".db"}
MAX_BYTES = 5 * 1024 * 1024
TEXT_EXT = {".md", ".py", ".json", ".csv", ".toml", ".txt", ".yml", ".yaml", ".ini", ".cfg", ".sh", ".ts",
            ".tsx", ".js", ".mjs", ".sql", ".example", ".env", ""}
TOKEN_PATTERNS = {
    "OpenAI/Anthropic-style key": re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}"),
    "Private key block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
}
ASSIGNMENT = re.compile(r"(?:key|token|secret|password)\w*\s*[=:]\s*['\"]?([^'\"\s,)]{16,})", re.IGNORECASE)
ASSIGNMENT_EXT = {".env", ".example", ".toml", ".ini", ".cfg", ".yml", ".yaml", ".txt", ".md", ".json", ""}
PLACEHOLDER = re.compile(r"^(replace-|your[-_]|<|\$|\{|example|placeholder|xxx|changeme|http)", re.IGNORECASE)
EMAIL = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
EMAIL_ALLOW = re.compile(r"(noreply@anthropic\.com|@example\.(com|org)|@users\.noreply\.github\.com)$", re.IGNORECASE)
THAI_ID_FORMATTED = re.compile(r"\b\d-\d{4}-\d{5}-\d{2}-\d\b")
ALLOW_MARKER = "secret-scan: allow"


@dataclass
class Check:
    name: str
    problems: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.problems


def repo_files(root: Path) -> list[Path]:
    """Files that are tracked or would be committed (respects .gitignore)."""
    try:
        out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                             cwd=root, capture_output=True, check=True).stdout.decode()
        files = [root / f for f in out.split("\0") if f]
    except (OSError, subprocess.CalledProcessError):
        skip = {".git", ".venv", "node_modules", "__pycache__", ".pytest_cache", ".ruff_cache"}
        files = [p for p in root.rglob("*") if p.is_file() and not skip & set(p.relative_to(root).parts)]
    return [f for f in files if f.is_file()]


def _md_table_rows(text: str, header_startswith: str) -> list[list[str]]:
    """Rows (as cell lists) of the first Markdown table whose header starts with the given text."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip("| ").startswith(header_startswith):
            rows = []
            for row in lines[i + 2:]:
                if not row.strip().startswith("|"):
                    break
                rows.append([c.strip() for c in row.strip().strip("|").split("|")])
            return rows
    return []


def check_structure(root: Path) -> list[Check]:
    c1 = Check("Required root files and directories")
    c1.problems += [f"missing {f}" for f in REQUIRED_ROOT if not (root / f).is_file()]
    c1.problems += [f"missing directory {d}/" for d in REQUIRED_DIRS if not (root / d).is_dir()]

    c2 = Check("24 weekly directories with the weekly structure")
    weeks_found = sorted(p.name for p in (root / "courses").glob("*/week-*") if p.is_dir())
    if len(weeks_found) != 24:
        c2.problems.append(f"expected 24 week directories, found {len(weeks_found)}")
    for course, weeks in COURSE_WEEKS.items():
        if not (root / "courses" / course / "README.md").is_file():
            c2.problems.append(f"missing courses/{course}/README.md")
        for n in weeks:
            d = root / "courses" / course / f"week-{n:02d}"
            c2.problems += [f"{d.relative_to(root)}/{f} missing" for f in WEEK_FILES if not (d / f).is_file()]
            c2.problems += [f"{d.relative_to(root)}/{x}/ missing" for x in WEEK_DIRS if not (d / x).is_dir()]

    c3 = Check("10 project workspaces with context files")
    for p in PROJECTS:
        d = root / "projects" / p
        c3.problems += [f"projects/{p}/{f} missing" for f in PROJECT_FILES if not (d / f).is_file()]

    c4 = Check("Week 1 complete materials and starter code")
    w1 = root / "courses/01-ai-foundations/week-01"
    for f in WEEK_FILES:
        if (w1 / f).is_file() and "Status: OUTLINE" in (w1 / f).read_text(encoding="utf-8"):
            c4.problems.append(f"week-01/{f} is still an outline")
    for f in ["starter-code/brand_assistant/cli.py", "starter-code/w01_exercises/ex01_json_thai.py",
              "tests/test_w01_scaffold.py", "tests/test_w01_assignment.py"]:
        if not (w1 / f).is_file():
            c4.problems.append(f"week-01/{f} missing")
    return [c1, c2, c3, c4]


def check_curriculum(root: Path) -> list[Check]:
    text = (root / "CURRICULUM.md").read_text(encoding="utf-8")
    c1 = Check("Curriculum hours total 240 (24 × 10)")
    rows = [r for r in _md_table_rows(text, "Week | Course") if r and r[0].isdigit()]
    hours = [int(r[-1]) for r in rows]
    if len(rows) != 24:
        c1.problems.append(f"programme table has {len(rows)} week rows, expected 24")
    if sum(hours) != 240:
        c1.problems.append(f"programme hours sum to {sum(hours)}, expected 240")
    if any(h != 10 for h in hours):
        c1.problems.append("every week should be 10 hours")
    split = [r for r in _md_table_rows(text, "Activity | Hours") if r and r[1].isdigit()]
    if sum(int(r[1]) for r in split) != 10:
        c1.problems.append("weekly time model does not sum to 10 hours")

    c2 = Check("Assessment weighting totals 100% and matches PROGRESS.md")
    for fname, header in (("CURRICULUM.md", "Component | Weight"), ("PROGRESS.md", "Component | Weight")):
        rows = _md_table_rows((root / fname).read_text(encoding="utf-8"), header)
        weights = {r[0]: int(r[1].rstrip("%")) for r in rows if r and r[1].rstrip("%").isdigit()}
        if weights != EXPECTED_WEIGHTS:
            c2.problems.append(f"{fname}: weights {weights} differ from {EXPECTED_WEIGHTS}")
        if sum(weights.values()) != 100:
            c2.problems.append(f"{fname}: weights sum to {sum(weights.values())}")
    return [c1, c2]


LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def check_links(root: Path, files: list[Path]) -> Check:
    c = Check("Internal documentation links resolve")
    for f in files:
        if f.suffix != ".md":
            continue
        in_code = False
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for target in LINK.findall(re.sub(r"`[^`]*`", "", line)):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                path = (f.parent / target.split("#")[0]).resolve()
                if not path.exists():
                    c.problems.append(f"{f.relative_to(root)}:{n} → {target}")
    return c


def check_instructions(root: Path) -> list[Check]:
    c1 = Check("Shared AI instructions are consistent")
    agents = (root / "AGENTS.md").read_text(encoding="utf-8")
    claude = (root / "CLAUDE.md").read_text(encoding="utf-8")
    for mode in ("Teaching Mode", "Build Mode", "Review Mode", "Research Mode"):
        if mode not in agents:
            c1.problems.append(f"AGENTS.md does not define {mode}")
    if "AGENTS.md" not in claude:
        c1.problems.append("CLAUDE.md does not reference AGENTS.md")
    if "Teaching Mode" not in claude:
        c1.problems.append("CLAUDE.md does not state the default Teaching Mode")
    for phrase in ("AI_HANDOFF.md", "Intel MacBook", "synthetic", "cost estimate"):
        if phrase.lower() not in agents.lower():
            c1.problems.append(f"AGENTS.md is missing the rule about '{phrase}'")
    if re.search(r"(?i)build mode is (the )?default", claude + agents):
        c1.problems.append("an instruction file claims Build Mode is the default")

    c2 = Check("AI_HANDOFF.md has all required sections")
    handoff = (root / "AI_HANDOFF.md").read_text(encoding="utf-8") if (root / "AI_HANDOFF.md").exists() else ""
    c2.problems += [f"missing section '{s}'" for s in HANDOFF_SECTIONS if s.lower() not in handoff.lower()]
    return [c1, c2]


def check_experiments(root: Path) -> Check:
    c = Check("8 experiment templates with all required sections and result files")
    dirs = sorted(p for p in (root / "research/experiments").glob("EXP-*") if p.is_dir())
    if len(dirs) < 8:
        c.problems.append(f"expected ≥ 8 experiments, found {len(dirs)}")
    for d in dirs:
        exp = d / "EXPERIMENT.md"
        if not exp.is_file():
            c.problems.append(f"{d.name}/EXPERIMENT.md missing")
            continue
        text = exp.read_text(encoding="utf-8")
        c.problems += [f"{d.name}: section '{s}' missing" for s in EXPERIMENT_SECTIONS if s not in text]
        csv_file, json_file = d / "results.csv", d / "results.json"
        if not csv_file.is_file() or not csv_file.read_text(encoding="utf-8").strip():
            c.problems.append(f"{d.name}/results.csv missing or empty")
        try:
            json.loads(json_file.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            c.problems.append(f"{d.name}/results.json missing or invalid")
    return c


def check_sensitive(root: Path, files: list[Path]) -> list[Check]:
    secrets, personal, large = (Check("No secrets or credentials"), Check("No personal data (emails, ID numbers)"),
                                Check("No large or forbidden files (weights, media, keys, databases)"))
    for f in files:
        rel = f.relative_to(root)
        if f.name == ".env" or (f.name.startswith(".env.") and f.name != ".env.example"):
            secrets.problems.append(f"{rel}: environment file must not be committed")
        if f.suffix.lower() in FORBIDDEN_EXT:
            large.problems.append(f"{rel}: forbidden file type")
        if f.stat().st_size > MAX_BYTES:
            large.problems.append(f"{rel}: {f.stat().st_size // 1024} KB > 5 MB")
        if f.suffix.lower() not in TEXT_EXT or f.stat().st_size > MAX_BYTES or rel.name == "uv.lock":
            continue
        try:
            lines = f.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(lines, 1):
            if ALLOW_MARKER in line:
                continue
            for label, pat in TOKEN_PATTERNS.items():
                if pat.search(line):
                    secrets.problems.append(f"{rel}:{n}: looks like a {label}")
            if f.suffix.lower() in ASSIGNMENT_EXT or f.name.startswith(".env"):
                m = ASSIGNMENT.search(line)
                if m and not PLACEHOLDER.match(m.group(1)):
                    secrets.problems.append(f"{rel}:{n}: credential-like assignment")
            for email in EMAIL.findall(line):
                if not EMAIL_ALLOW.search(email):
                    personal.problems.append(f"{rel}:{n}: email address")
            if THAI_ID_FORMATTED.search(line):
                personal.problems.append(f"{rel}:{n}: formatted Thai national ID number")
    return [secrets, personal, large]


def run_checks(root: Path = ROOT) -> list[Check]:
    files = repo_files(root)
    checks: list[Check] = []
    checks += check_structure(root)
    checks += check_curriculum(root)
    checks.append(check_links(root, files))
    checks += check_instructions(root)
    checks.append(check_experiments(root))
    checks += check_sensitive(root, files)
    return checks


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate the Applied AI Lab repository.")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    checks = run_checks()
    for c in checks:
        if c.ok and not args.quiet:
            print(f"PASS  {c.name}")
        elif not c.ok:
            print(f"FAIL  {c.name}")
            for p in c.problems[:25]:
                print(f"        - {p}")
            if len(c.problems) > 25:
                print(f"        … and {len(c.problems) - 25} more")
    failed = sum(not c.ok for c in checks)
    print(f"\n{len(checks) - failed}/{len(checks)} checks passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
