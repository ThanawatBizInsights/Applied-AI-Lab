"""Lab exercise tests — they fail until you implement w01_exercises/*.py.

Run: uv run pytest -m assignment courses/01-ai-foundations/week-01/tests/test_w01_exercises.py
"""

import json

import httpx
import pytest
from w01_exercises import ex01_json_thai as ex1
from w01_exercises import ex02_http as ex2
from w01_exercises import ex03_secrets as ex3

pytestmark = pytest.mark.assignment


# ---------------------------------------------------------------- Exercise 1
def test_utf8_stats_thai():
    assert ex1.utf8_stats("กาแฟ") == {"chars": 4, "utf8_bytes": 12}


def test_to_json_keeps_thai_readable():
    out = ex1.to_json({"t": "กาแฟ"})
    assert "กาแฟ" in out and "\\u0e" not in out
    assert json.loads(out) == {"t": "กาแฟ"}
    assert "\n  " in out  # indented by 2


def test_load_posts():
    posts = ex1.load_posts()
    assert [p["id"] for p in posts] == ["post-001", "post-002", "post-003", "post-004"]


def test_load_posts_rejects_non_list(tmp_path):
    p = tmp_path / "x.json"
    p.write_text('{"a": 1}', encoding="utf-8")
    with pytest.raises(ValueError):
        ex1.load_posts(p)


def test_validate_posts():
    posts = {p["id"]: p for p in ex1.load_posts()}
    assert ex1.validate_post(posts["post-001"]) == []
    assert ex1.validate_post(posts["post-002"]) == []
    assert ex1.validate_post(posts["post-003"]) == ["wrong type for hashtags: expected list"]
    errors = ex1.validate_post(posts["post-004"])
    assert "missing key: text" in errors
    assert "invalid scheduled time" in errors


def test_validate_timezone_and_channel():
    post = {"id": "x", "brand": "b", "channel": "myspace", "text": "  ", "hashtags": [],
            "scheduled": "2026-12-01T09:00:00"}
    errors = ex1.validate_post(post)
    assert set(errors) == {"unknown channel: myspace", "empty text", "scheduled time has no timezone"}


# ---------------------------------------------------------------- Exercise 2
def test_anthropic_request_shape():
    req = ex2.build_chat_request("anthropic", "KEY123", "m1", "be kind", "hello", 100)
    assert req.method == "POST"
    assert str(req.url) == "https://api.anthropic.com/v1/messages"
    assert req.headers["x-api-key"] == "KEY123"
    assert req.headers["anthropic-version"] == "2023-06-01"
    body = json.loads(req.content)
    assert body == {"model": "m1", "max_tokens": 100, "system": "be kind",
                    "messages": [{"role": "user", "content": "hello"}]}


def test_openai_request_shape():
    req = ex2.build_chat_request("openai", "KEY123", "m1", "be kind", "hello", 100)
    assert str(req.url) == "https://api.openai.com/v1/chat/completions"
    assert req.headers["authorization"] == "Bearer KEY123"
    body = json.loads(req.content)
    assert body["messages"][0] == {"role": "system", "content": "be kind"}
    assert body["messages"][1] == {"role": "user", "content": "hello"}


def test_unknown_provider():
    with pytest.raises(ValueError):
        ex2.build_chat_request("nope", "k", "m", "s", "u")


@pytest.mark.parametrize("code,expected", [(200, "ok"), (201, "ok"), (401, "auth_error"), (403, "auth_error"),
                                           (408, "retry"), (429, "retry"), (500, "retry"), (503, "retry"),
                                           (400, "client_error"), (404, "client_error")])
def test_classify_status(code, expected):
    assert ex2.classify_status(code) == expected


def test_classify_status_rejects_redirects():
    with pytest.raises(ValueError):
        ex2.classify_status(302)


def test_send_and_extract_anthropic():
    def handler(request):
        return httpx.Response(200, json={"content": [{"type": "text", "text": "สวัสดี"}],
                                         "usage": {"input_tokens": 12, "output_tokens": 5}})
    req = ex2.build_chat_request("anthropic", "KEY", "m", "s", "u")
    out = ex2.send_and_extract(req, "anthropic", httpx.MockTransport(handler))
    assert out == {"text": "สวัสดี", "input_tokens": 12, "output_tokens": 5}


def test_send_and_extract_openai():
    def handler(request):
        return httpx.Response(200, json={"choices": [{"message": {"role": "assistant", "content": "hi"}}],
                                         "usage": {"prompt_tokens": 7, "completion_tokens": 1}})
    req = ex2.build_chat_request("openai", "KEY", "m", "s", "u")
    expected = {"text": "hi", "input_tokens": 7, "output_tokens": 1}
    assert ex2.send_and_extract(req, "openai", httpx.MockTransport(handler)) == expected


def test_send_and_extract_error_hides_key():
    req = ex2.build_chat_request("openai", "SUPERSECRETKEY", "m", "s", "u")
    with pytest.raises(RuntimeError) as err:
        ex2.send_and_extract(req, "openai", httpx.MockTransport(lambda r: httpx.Response(401, json={})))
    assert "401" in str(err.value) and "SUPERSECRETKEY" not in str(err.value)


# ---------------------------------------------------------------- Exercise 3
def test_mask_secret():
    assert ex3.mask_secret("sk-abcdef123456") == "****3456"
    assert ex3.mask_secret("12345678") == "****"


@pytest.mark.parametrize("value", [None, "", "   ", "replace-me", "Replace-With-model-id"])
def test_require_env_rejects_missing_or_placeholder(value):
    env = {} if value is None else {"X_KEY": value}
    with pytest.raises(ex3.MissingSecretError) as err:
        ex3.require_env("X_KEY", env)
    assert "X_KEY" in str(err.value) and ".env" in str(err.value)


def test_require_env_returns_value():
    assert ex3.require_env("X_KEY", {"X_KEY": "real-value-123"}) == "real-value-123"


def test_find_secrets_in_text():
    fake_key = "sk-" + "a1B2" * 6  # built at runtime so no secret-looking literal is committed
    text = "\n".join([
        "OPENAI_API_KEY=replace-me",                 # placeholder: fine
        f"ANTHROPIC_API_KEY={'x' * 10}{'Q' * 10}",   # line 2: flagged
        "name = 'Balena'",                           # fine
        f"client = make('{fake_key}')",              # line 4: flagged
    ])
    assert ex3.find_secrets_in_text(text) == ["line 2", "line 4"]
