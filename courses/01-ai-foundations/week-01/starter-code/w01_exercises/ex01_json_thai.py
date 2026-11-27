"""Exercise 1 — JSON, Unicode and validation (≈ 30 min).

Concepts (LECTURE.md §4): JSON's data model, UTF-8, `ensure_ascii`, validating at the boundary.

Predict first (write your answers in REFLECTION.md):
  P1. How many bytes does "กาแฟ" take in UTF-8? How many characters does len() report?
  P2. What does json.dumps({"t": "กาแฟ"}) print by default?
  P3. Which posts in data/sample_posts.json are invalid, and why?
"""

from __future__ import annotations

import json  # noqa: F401
from datetime import datetime  # noqa: F401
from pathlib import Path

DATA = Path(__file__).parent / "data" / "sample_posts.json"
REQUIRED = {"id": str, "brand": str, "channel": str, "text": str, "hashtags": list, "scheduled": str}
CHANNELS = {"line_oa", "facebook", "instagram", "tiktok", "youtube"}


def utf8_stats(text: str) -> dict[str, int]:
    """Return {"chars": <len(text)>, "utf8_bytes": <bytes when UTF-8 encoded>}.

    >>> utf8_stats("abc")
    {'chars': 3, 'utf8_bytes': 3}
    """
    raise NotImplementedError("TODO(W01-E1a)")


def to_json(obj: object) -> str:
    """Serialise to JSON so that Thai stays readable (no \\u0e01 escapes), indented by 2 spaces."""
    raise NotImplementedError("TODO(W01-E1b)")


def load_posts(path: Path = DATA) -> list[dict]:
    """Load the list of posts from a UTF-8 JSON file. Raise ValueError if the top level is not a list."""
    raise NotImplementedError("TODO(W01-E1c)")


def validate_post(post: dict) -> list[str]:
    """Return a list of human-readable error strings ([] means valid).

    Check that:
    - every key in REQUIRED exists and has the right type
      (error text: "missing key: <key>" or "wrong type for <key>: expected <type name>");
    - `channel` is one of CHANNELS ("unknown channel: <value>");
    - `text` is not empty after stripping whitespace ("empty text");
    - `scheduled` parses with datetime.fromisoformat() and includes a timezone
      ("invalid scheduled time" or "scheduled time has no timezone").
    Only check a key's value if the key exists with the right type.
    """
    raise NotImplementedError("TODO(W01-E1d)")
