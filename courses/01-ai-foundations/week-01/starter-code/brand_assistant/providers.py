"""Real provider clients over raw HTTP.   >>> YOU IMPLEMENT THIS <<<

Learning goal: understand what an "LLM API" actually is (an HTTPS POST with a JSON body
and an API key header) before using any SDK. Each provider wants the same intent in a
different wire format. Your job is to translate.

Rules:
- Call `self.budget.spend()` BEFORE sending each request.
- Never put the API key in an exception message, log line or return value.
- Map HTTP errors: 401/403 -> AuthError; 429 and 5xx -> RetryableError; other 4xx -> ProviderError.
  (Retrying is Week 4's topic. Here you only classify.)
- Tests inject an `httpx.MockTransport`, so they never touch the network or cost money.

Verify the current request format in each provider's official API reference before you make
a real call. Write down which page and date you used in your REFLECTION.md.
"""

from __future__ import annotations

import time  # noqa: F401

import httpx

from .llm import RequestBudget
from .models import LLMResponse, Message  # noqa: F401


class ProviderError(RuntimeError):
    def __init__(self, status: int, message: str):
        super().__init__(f"HTTP {status}: {message}")
        self.status = status


class AuthError(ProviderError):
    pass


class RetryableError(ProviderError):
    pass


class _BaseHTTPClient:
    provider = "base"

    def __init__(
        self,
        api_key: str,
        model: str,
        budget: RequestBudget,
        transport: httpx.BaseTransport | None = None,
        timeout: float = 30.0,
    ):
        self._api_key = api_key
        self.model = model
        self.budget = budget
        self._http = httpx.Client(transport=transport, timeout=timeout)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(model={self.model!r})"  # no key here, on purpose


class AnthropicClient(_BaseHTTPClient):
    """Anthropic Messages API.

    Request:  POST https://api.anthropic.com/v1/messages
              headers: x-api-key, anthropic-version: 2023-06-01, content-type: application/json
              body:    {"model", "max_tokens", "system", "messages": [{"role", "content"}]}
    Response: text in body["content"] (a list of blocks; join the "text" of blocks whose
              "type" is "text"); usage in body["usage"]["input_tokens"/"output_tokens"].
    """

    provider = "anthropic"
    URL = "https://api.anthropic.com/v1/messages"
    API_VERSION = "2023-06-01"

    def complete(self, system: str, messages: list[Message], max_tokens: int = 512) -> LLMResponse:
        raise NotImplementedError("TODO(W01-A4): implement AnthropicClient.complete")


class OpenAIClient(_BaseHTTPClient):
    """OpenAI Chat Completions API.

    Request:  POST https://api.openai.com/v1/chat/completions
              headers: Authorization: Bearer <key>, content-type: application/json
              body:    {"model", "max_tokens", "messages": [{"role": "system", ...}, ...]}
              Note: the system prompt is the FIRST message with role "system".
    Response: text in body["choices"][0]["message"]["content"];
              usage in body["usage"]["prompt_tokens"/"completion_tokens"].
    (OpenAI also offers a newer Responses API. Chat Completions is used here because its
    format is the most widely copied by other providers. Compare both in your reflection.)
    """

    provider = "openai"
    URL = "https://api.openai.com/v1/chat/completions"

    def complete(self, system: str, messages: list[Message], max_tokens: int = 512) -> LLMResponse:
        raise NotImplementedError("TODO(W01-A4): implement OpenAIClient.complete")
