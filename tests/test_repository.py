"""Repository-level validation as tests (runs in `uv run pytest`)."""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("validate_repo", ROOT / "scripts" / "validate_repo.py")
validate_repo = importlib.util.module_from_spec(spec)
sys.modules["validate_repo"] = validate_repo  # needed so @dataclass can resolve its module
spec.loader.exec_module(validate_repo)

CHECKS = validate_repo.run_checks(ROOT)


@pytest.mark.parametrize("check", CHECKS, ids=[c.name for c in CHECKS])
def test_repository_check(check):
    assert check.ok, "\n".join(check.problems)


def test_secret_scanner_catches_a_key(tmp_path):
    """The scanner itself must work: plant a fake key in a temporary repo copy."""
    fake = "sk-" + "Zq9" * 9
    (tmp_path / "leak.md").write_text(f"OPENAI_API_KEY={fake}\n", encoding="utf-8")
    secrets = validate_repo.check_sensitive(tmp_path, [tmp_path / "leak.md"])[0]
    assert not secrets.ok


def test_placeholders_are_not_flagged(tmp_path):
    (tmp_path / "x.md").write_text("OPENAI_API_KEY=replace-me-with-a-real-key\n", encoding="utf-8")
    assert validate_repo.check_sensitive(tmp_path, [tmp_path / "x.md"])[0].ok


def test_email_detection(tmp_path):
    address = "someone" + "@" + "gmail.com"  # assembled at runtime so this file passes its own scan
    (tmp_path / "x.md").write_text(f"contact: {address}\n", encoding="utf-8")
    assert not validate_repo.check_sensitive(tmp_path, [tmp_path / "x.md"])[1].ok
