"""Check model output against brand rules.   >>> YOU IMPLEMENT THIS <<<

Learning goal: never trust model output. Deterministic checks are cheap, fast and
explainable. They catch the obvious failures before a human reviewer spends time.

They are also imperfect, and Thai makes that visible: Thai is written without spaces between
words, so "ขา" (leg) appears inside "ขาว" (white) and "ขาย" (sell). English has the same
problem in a different form: "leg" is inside "elegant". Your implementation must handle both.
"""

from __future__ import annotations

import re  # noqa: F401

from .models import BrandProfile, CheckResult, Rule, Violation  # noqa: F401


def rule_applies(rule: Rule, task: str | None) -> bool:
    """True if the rule applies to `task`. PROVIDED.

    A rule with an empty `applies_to` applies to every task. When `task` is None,
    only rules that apply to every task are used.
    """
    if not rule.applies_to:
        return True
    return task is not None and task in rule.applies_to


def check_output(text: str, brand: BrandProfile, task: str | None = None) -> CheckResult:
    """Return every violation of the rules that apply to `task`.

    Matching rules (the tests check each one):
    - All term matching is case-insensitive.
    - forbidden_terms:
        * First remove every `ignore_within` string from the text (case-insensitively).
        * A term made only of ASCII characters matches on word boundaries (regex \\b):
          "leg" matches "a leg" but not "elegant" or "legs" ("legs" is listed as its own term).
        * Any other term (e.g. Thai) matches as a plain substring.
        * At most ONE violation per rule; evidence = the first term found (in the order the
          terms are listed in the rule).
    - required_any: one violation if none of the terms appears as a substring;
      evidence = "none of: " + the terms joined by ", ".
    - forbidden_regex: one violation if any pattern matches. evidence = "pattern <index>"
      (NEVER the matched text: it could be a real ID number or phone number).
    - max_chars: one violation if len(text) > value; evidence = "<length> > <value>".
    - Violations keep the order of the rules in the brand file.

    Hint 1: re.escape() the term before putting it in a regex.
    Hint 2: str.isascii() tells you whether a term is ASCII-only.
    Hint 3: re.sub(re.escape(word), " ", text, flags=re.IGNORECASE) removes ignore words.
    """
    raise NotImplementedError("TODO(W01-A3): implement check_output — see the docstring")
