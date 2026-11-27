"""Exercise 3 — Secrets and configuration (≈ 20 min).

Concepts (LECTURE.md §5): environment variables, .env vs .env.example, masking, fail fast.

Predict first:
  P1. If you `print(settings)` and settings holds an API key, where could that key end up?
  P2. Why is failing at start-up better than failing on the first API call?
"""

from __future__ import annotations

from collections.abc import Mapping


class MissingSecretError(RuntimeError):
    pass


def mask_secret(value: str) -> str:
    """Show only the last 4 characters: "sk-abcdef123456" -> "****3456".

    Values of 8 characters or fewer are fully hidden: "****".
    """
    raise NotImplementedError("TODO(W01-E3a)")


def require_env(name: str, env: Mapping[str, str]) -> str:
    """Return env[name], or raise MissingSecretError if it is missing, empty, or a placeholder
    (starts with "replace-me" or "replace-with", case-insensitive).

    The error message must name the variable and say to set it in .env.
    It must never include the value itself.
    """
    raise NotImplementedError("TODO(W01-E3b)")


def find_secrets_in_text(text: str) -> list[str]:
    """Return a list of suspicious lines (1-based "line <n>") that look like committed secrets.

    Flag a line if it matches any of these, case-insensitively:
    - an assignment to a name containing KEY, TOKEN, SECRET or PASSWORD whose value is at
      least 16 characters and is not a placeholder (e.g. OPENAI_API_KEY=sk-live-abc...);
    - a string starting with "sk-" followed by 20+ letters, digits, "-" or "_".
    This is a simplified version of what scripts/validate_repo.py does for the whole repo.

    Hint: re.search(r"(key|token|secret|password)\\w*\\s*[=:]\\s*['\\"]?([^'\\"\\s]{16,})", line, re.I)
    """
    raise NotImplementedError("TODO(W01-E3c)")
