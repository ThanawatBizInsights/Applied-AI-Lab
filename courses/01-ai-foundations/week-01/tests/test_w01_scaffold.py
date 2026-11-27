"""Scaffold tests: these check the PROVIDED code and data and must pass before you start.

Run: uv run pytest courses/01-ai-foundations/week-01
"""

import json
from pathlib import Path

import pytest
from brand_assistant.cli import main
from brand_assistant.config import ConfigError, load_settings, mask
from brand_assistant.llm import BudgetExceededError, FakeLLMClient, RequestBudget, approx_tokens, estimate_cost_usd
from brand_assistant.loader import BRANDS_DIR, REQUIRED_KEYS, list_brands
from brand_assistant.models import RULE_TYPES, CheckResult, Message, Violation

EXPECTED_BRANDS = ["balena", "checkkhum", "little_snowy_owl"]


def test_three_brands_available():
    assert list_brands() == EXPECTED_BRANDS


@pytest.mark.parametrize("brand_id", EXPECTED_BRANDS)
def test_brand_files_are_valid_json_with_required_keys(brand_id):
    data = json.loads((BRANDS_DIR / f"{brand_id}.json").read_text(encoding="utf-8"))
    assert data["id"] == brand_id
    for key in REQUIRED_KEYS:
        assert key in data, key
    for rule in data["rules"]:
        assert rule["type"] in RULE_TYPES
        assert rule["severity"] in ("error", "warning")
    for task in {t for r in data["rules"] for t in r.get("applies_to", [])}:
        assert task in data["tasks"], f"rule applies to unknown task {task}"


def test_balena_never_has_legs_rule_exists():
    data = json.loads((BRANDS_DIR / "balena.json").read_text(encoding="utf-8"))
    no_legs = next(r for r in data["rules"] if r["id"] == "no-legs")
    assert no_legs["severity"] == "error"
    assert "legs" in data["mascot"]["must_not_have"]


def test_fake_client_is_deterministic_and_records_calls():
    client = FakeLLMClient(responses={"cold brew": "สั่งทาง LINE ได้เลย"})
    msgs = [Message("user", "write about cold brew")]
    first = client.complete("sys", msgs)
    second = client.complete("sys", msgs)
    assert first.text == second.text == "สั่งทาง LINE ได้เลย"
    assert first.provider == "fake"
    assert len(client.calls) == 2


def test_approx_tokens_overestimates_thai_bytes():
    # Thai characters are 3 bytes in UTF-8, so the naive estimate is higher for Thai.
    assert approx_tokens("กาแฟ" * 10) > approx_tokens("coffee" * 7)


def test_budget_blocks_extra_requests():
    budget = RequestBudget(max_requests=2)
    budget.spend()
    budget.spend()
    with pytest.raises(BudgetExceededError):
        budget.spend()


def test_cost_estimate():
    assert estimate_cost_usd(1_000_000, 500_000, 1.0, 4.0) == pytest.approx(3.0)


def test_check_result_passes_with_warnings_only():
    result = CheckResult([Violation("x", "warning", "m", "e")])
    assert result.passed and not result.errors


def test_settings_never_expose_key():
    s = load_settings({"LLM_PROVIDER": "anthropic", "ANTHROPIC_API_KEY": "k" * 30 + "WXYZ", "ANTHROPIC_MODEL": "m"})
    assert "kkkk" not in repr(s) and repr(s).count("WXYZ") == 1
    assert mask("short") == "****"


def test_placeholder_key_is_rejected():
    with pytest.raises(ConfigError):
        load_settings({"LLM_PROVIDER": "openai", "OPENAI_API_KEY": "replace-me", "OPENAI_MODEL": "m"})


def test_fake_provider_needs_no_key():
    assert load_settings({"LLM_PROVIDER": "fake"}).api_key is None


def test_cli_lists_brands(capsys):
    assert main(["brands"]) == 0
    assert capsys.readouterr().out.split() == EXPECTED_BRANDS


def test_cli_reports_unfinished_todos_gracefully(tmp_path):
    # Until the assignment is done, `generate` exits with code 3 instead of a traceback.
    code = main(["generate", "--brand", "balena", "--task", "caption", "--input", "x",
                 "--provider", "fake", "--runs-dir", str(tmp_path)])
    assert code in (0, 2, 3)


def test_sample_posts_file_is_valid_json():
    path = Path(__file__).resolve().parent.parent / "starter-code" / "w01_exercises" / "data" / "sample_posts.json"
    assert len(json.loads(path.read_text(encoding="utf-8"))) == 4
