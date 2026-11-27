"""Load and validate brand profiles from brands/*.json.   >>> YOU IMPLEMENT THIS <<<

Learning goal: JSON is untrusted input. Parse it, validate it, and convert it into typed
objects at the boundary, so the rest of the program can trust its data.
"""

from __future__ import annotations

from pathlib import Path

from .models import RULE_TYPES, BrandProfile, Mascot, Rule  # noqa: F401  (you will need these)

BRANDS_DIR = Path(__file__).parent / "brands"

#: Keys every brand file must contain.
REQUIRED_KEYS = ("id", "name", "language", "audience", "voice", "products", "tasks", "rules")


class BrandNotFoundError(LookupError):
    """No brand file exists for the requested id."""


class BrandValidationError(ValueError):
    """A brand file exists but its content is invalid."""


def list_brands(brands_dir: Path = BRANDS_DIR) -> list[str]:
    """Return the ids of all available brands, sorted. PROVIDED."""
    return sorted(p.stem for p in brands_dir.glob("*.json"))


def load_brand(brand_id: str, brands_dir: Path = BRANDS_DIR) -> BrandProfile:
    """Read `<brands_dir>/<brand_id>.json` and return a validated BrandProfile.

    Requirements (the assignment tests check each one):
    1. Unknown brand id -> raise BrandNotFoundError naming the id and listing available brands.
       Do not let a user-supplied id escape the brands directory (e.g. "../secrets").
    2. Read the file as UTF-8 (Thai text!). Invalid JSON -> BrandValidationError
       whose message includes the file name.
    3. Any key from REQUIRED_KEYS missing -> BrandValidationError naming the missing key(s).
    4. The `id` inside the file must equal `brand_id`.
    5. Every rule must have a `type` in RULE_TYPES, plus `id`, `severity` ("error" or
       "warning") and `message`. Otherwise -> BrandValidationError naming the rule id.
    6. A `max_chars` rule needs an integer `value`; a `forbidden_regex` rule needs `patterns`;
       the other rule types need `terms`.
    7. Convert JSON lists to tuples (the dataclasses are frozen and expect tuples).
       `mascot` may be null -> None. `approval_required` defaults to True.
    8. Ignore keys that start with "_" (e.g. "_sources" is documentation).

    Hint 1: json.loads(path.read_text(encoding="utf-8"))
    Hint 2: write a small helper `_parse_rule(raw: dict) -> Rule`.
    """
    raise NotImplementedError("TODO(W01-A1): implement load_brand — see the docstring")
