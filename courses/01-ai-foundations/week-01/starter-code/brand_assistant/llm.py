"""LLM client interface, a fake offline client and a request budget. PROVIDED.

Design decision (read LECTURE.md §6): every provider is hidden behind one small interface,
`LLMClient.complete()`. The rest of the program never knows which provider it talks to.
That lets you (1) develop and test offline with `FakeLLMClient`, at zero cost, and
(2) add providers later without touching prompts.py or checks.py. In Week 4 this grows
into the Multi-model AI Gateway.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from typing import Protocol

from .models import LLMResponse, Message


class BudgetExceededError(RuntimeError):
    """Raised before a request would exceed the per-run request budget."""


class LLMClient(Protocol):
    provider: str
    model: str

    def complete(self, system: str, messages: list[Message], max_tokens: int = 512) -> LLMResponse:
        """Send one request and return the model's text plus usage information."""
        ...


@dataclass
class RequestBudget:
    """A hard safety rail against runaway loops that would cost money.

    Call `spend()` immediately BEFORE every real network request.
    """

    max_requests: int
    used: int = 0

    def spend(self) -> None:
        if self.used >= self.max_requests:
            raise BudgetExceededError(
                f"Request budget of {self.max_requests} reached. "
                "Raise LLM_MAX_REQUESTS_PER_RUN in .env only if you have approved the cost."
            )
        self.used += 1


def approx_tokens(text: str) -> int:
    """Very rough token estimate: UTF-8 bytes / 4.

    This is deliberately naive. Thai characters take 3 bytes each in UTF-8, so this badly
    overestimates Thai. In Week 2 you replace it with a real tokenizer and measure the error.
    """
    return max(1, len(text.encode("utf-8")) // 4)


@dataclass
class FakeLLMClient:
    """Deterministic offline client for development and tests. Costs nothing.

    - `responses` maps a substring of the last user message to a canned reply.
    - Otherwise `default` is returned, or a generic placeholder that says how long the
      request was (it never echoes the prompt, so its output is predictable in tests).
    - Every call is recorded in `calls` so tests can inspect what was sent.
    """

    responses: dict[str, str] = field(default_factory=dict)
    default: str | None = None
    model: str = "fake-1"
    provider: str = "fake"
    calls: list[dict] = field(default_factory=list)

    def complete(self, system: str, messages: list[Message], max_tokens: int = 512) -> LLMResponse:
        start = time.perf_counter()
        last_user = next((m.content for m in reversed(messages) if m.role == "user"), "")
        text = next((reply for key, reply in self.responses.items() if key in last_user), None)
        if text is None:
            text = self.default or f"[fake response to a {len(last_user)}-character request]"
        self.calls.append({"system": system, "messages": list(messages), "max_tokens": max_tokens})
        return LLMResponse(
            text=text,
            provider=self.provider,
            model=self.model,
            input_tokens=approx_tokens(system) + sum(approx_tokens(m.content) for m in messages),
            output_tokens=approx_tokens(text),
            latency_s=time.perf_counter() - start,
        )


def estimate_cost_usd(
    input_tokens: int, output_tokens: int, usd_per_mtok_in: float, usd_per_mtok_out: float
) -> float:
    """Cost of one request given prices in USD per million tokens.

    Take prices from the provider's official pricing page and record them, with the date,
    in evaluations/benchmarks/model-registry.csv. Prices change; never hard-code them.
    """
    return input_tokens / 1_000_000 * usd_per_mtok_in + output_tokens / 1_000_000 * usd_per_mtok_out
