"""Data models shared by every module. PROVIDED — read, do not change the field names.

Why dataclasses and not plain dicts? A dict accepts any key, so a typo such as
`brand["lanugage"]` fails late, deep inside your code. A frozen dataclass fails at
construction time, documents the shape of the data and can be type-checked.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Severity = Literal["error", "warning"]
Role = Literal["user", "assistant"]

#: The only rule types a brand file may use. loader.py must reject anything else.
RULE_TYPES: tuple[str, ...] = ("forbidden_terms", "required_any", "forbidden_regex", "max_chars")


@dataclass(frozen=True)
class Rule:
    """One machine-checkable brand rule (see brands/*.json for examples).

    - forbidden_terms: violation if any term appears (see checks.py for matching rules).
    - required_any:    violation if none of the terms appears.
    - forbidden_regex: violation if any regex pattern matches.
    - max_chars:       violation if the text is longer than `value` characters.
    `applies_to` lists task names; an empty tuple means the rule applies to every task.
    """

    id: str
    type: str
    severity: Severity
    message: str
    terms: tuple[str, ...] = ()
    patterns: tuple[str, ...] = ()
    ignore_within: tuple[str, ...] = ()
    value: int | None = None
    applies_to: tuple[str, ...] = ()


@dataclass(frozen=True)
class Mascot:
    name: str
    description: str
    must_have: tuple[str, ...] = ()
    must_not_have: tuple[str, ...] = ()


@dataclass(frozen=True)
class BrandProfile:
    id: str
    name: str
    language: str  # ISO 639-1 code: "th" or "en"
    audience: str
    voice: str
    products: tuple[str, ...]
    tasks: dict[str, str]
    rules: tuple[Rule, ...]
    mascot: Mascot | None = None
    approval_required: bool = True


@dataclass(frozen=True)
class Message:
    role: Role
    content: str


@dataclass(frozen=True)
class LLMResponse:
    text: str
    provider: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_s: float


@dataclass(frozen=True)
class Violation:
    rule_id: str
    severity: Severity
    message: str
    evidence: str  # what triggered the rule; must never contain personal data


@dataclass
class CheckResult:
    violations: list[Violation] = field(default_factory=list)

    @property
    def errors(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == "error"]

    @property
    def warnings(self) -> list[Violation]:
        return [v for v in self.violations if v.severity == "warning"]

    @property
    def passed(self) -> bool:
        """True when there are no error-severity violations (warnings are allowed)."""
        return not self.errors
