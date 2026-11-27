"""Configuration from environment variables. PROVIDED.

Principle: configuration that differs between machines (keys, model IDs, limits) lives in the
environment, never in code (the "Twelve-Factor App" rule). `.env` is git-ignored;
`.env.example` documents every variable with placeholders.
"""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass

PLACEHOLDER_PREFIXES = ("replace-me", "replace-with", "your-", "sk-xxx")


class ConfigError(RuntimeError):
    pass


def mask(value: str) -> str:
    """Return a safe display form of a secret: only the last 4 characters are visible."""
    return "****" if len(value) <= 8 else f"****{value[-4:]}"


def _is_placeholder(value: str) -> bool:
    return not value.strip() or value.strip().lower().startswith(PLACEHOLDER_PREFIXES)


@dataclass(frozen=True)
class Settings:
    provider: str
    api_key: str | None
    model: str | None
    max_requests: int

    def __repr__(self) -> str:  # never print a raw key, even by accident
        key = mask(self.api_key) if self.api_key else None
        return (
            f"Settings(provider={self.provider!r}, api_key={key!r}, "
            f"model={self.model!r}, max_requests={self.max_requests})"
        )


def load_settings(env: Mapping[str, str] | None = None, provider: str | None = None) -> Settings:
    """Read settings. Loads `.env` (if python-dotenv is installed) when `env` is not given."""
    if env is None:
        try:
            from dotenv import load_dotenv

            load_dotenv()
        except ImportError:
            pass
        env = os.environ
    provider = (provider or env.get("LLM_PROVIDER", "fake")).lower()
    max_requests = int(env.get("LLM_MAX_REQUESTS_PER_RUN", "20"))
    if provider == "fake":
        return Settings("fake", None, "fake-1", max_requests)
    prefix = {"openai": "OPENAI", "anthropic": "ANTHROPIC", "gemini": "GEMINI"}.get(provider)
    if prefix is None:
        raise ConfigError(f"Unknown LLM_PROVIDER {provider!r}. Use fake, openai, anthropic or gemini.")
    key, model = env.get(f"{prefix}_API_KEY", ""), env.get(f"{prefix}_MODEL", "")
    if _is_placeholder(key):
        raise ConfigError(f"{prefix}_API_KEY is missing or still a placeholder. Set it in .env (never commit it).")
    if _is_placeholder(model):
        raise ConfigError(f"{prefix}_MODEL is missing. Look up a current model ID in the provider's docs.")
    return Settings(provider, key, model, max_requests)
