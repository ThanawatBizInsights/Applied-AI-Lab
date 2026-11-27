"""Exercise 2 — HTTP from first principles (≈ 45 min). No network, no API key, no cost.

Concepts (LECTURE.md §3): request line, headers, body, status codes, authentication.
You build requests as objects and test them against `httpx.MockTransport`, which plays the
role of the server. This is exactly how providers.py is tested in the assignment.

Predict first:
  P1. Which HTTP method creates a chat completion, and why not GET?
  P2. Which status code means "your key is wrong", and which means "slow down"?
  P3. Is it safe to automatically retry a request that returned 400? A 503?
"""

from __future__ import annotations

import httpx  # noqa: F401


def build_chat_request(
    provider: str, api_key: str, model: str, system: str, user: str, max_tokens: int = 256
) -> httpx.Request:
    """Return an httpx.Request (do not send it) for one chat call.

    provider "anthropic": POST https://api.anthropic.com/v1/messages
        headers x-api-key, anthropic-version "2023-06-01"; body has model, max_tokens,
        system and messages=[{"role": "user", "content": user}].
    provider "openai": POST https://api.openai.com/v1/chat/completions
        header Authorization "Bearer <key>"; body has model, max_tokens and
        messages=[{"role": "system", ...}, {"role": "user", ...}].
    Any other provider -> ValueError.

    Hint: httpx.Request("POST", url, headers=..., json=body)
    """
    raise NotImplementedError("TODO(W01-E2a)")


def classify_status(status: int) -> str:
    """Map an HTTP status code to one of: "ok", "auth_error", "retry", "client_error".

    2xx -> ok · 401, 403 -> auth_error · 408, 429, 5xx -> retry · other 4xx -> client_error.
    Anything else (1xx, 3xx) -> ValueError.
    """
    raise NotImplementedError("TODO(W01-E2b)")


def send_and_extract(request: httpx.Request, provider: str, transport: httpx.BaseTransport) -> dict:
    """Send `request` through `transport` and return {"text", "input_tokens", "output_tokens"}.

    Use `with httpx.Client(transport=transport) as client: response = client.send(request)`.
    If classify_status(response.status_code) is not "ok", raise RuntimeError with the
    status category and code, but NOT the request headers (they contain the key).
    Extract fields as described in brand_assistant/providers.py docstrings.
    """
    raise NotImplementedError("TODO(W01-E2c)")
