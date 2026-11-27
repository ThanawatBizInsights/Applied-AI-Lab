"""Command-line interface. PROVIDED — it wires your modules together.

Examples (run from the repository root):
    uv run python -m brand_assistant brands
    uv run python -m brand_assistant generate --brand balena --task caption \\
        --input "แนะนำ Cold Brew Original 500 mL สำหรับหน้าร้อน"
    uv run python -m brand_assistant generate --brand checkkhum --task customer_reply \\
        --input "สวัสดีค่ะ อยากทราบว่าประกันชั้น 1 คุ้มครองน้ำท่วมไหมคะ" --provider anthropic

(`python -m` needs the starter-code folder on the path. The commands in LAB.md show how.)

Every run is appended to runs/<date>.jsonl (git-ignored), so you can analyse results later.
Outputs of brands with approval_required are marked PENDING_HUMAN_APPROVAL: nothing is ever
published by this tool.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from dataclasses import asdict
from pathlib import Path

from .config import ConfigError, load_settings
from .llm import FakeLLMClient, RequestBudget, estimate_cost_usd
from .loader import list_brands, load_brand
from .models import LLMResponse


def make_client(provider: str | None):
    """Build a client from environment settings. Fake needs no key and costs nothing."""
    settings = load_settings(provider=provider)
    budget = RequestBudget(settings.max_requests)
    if settings.provider == "fake":
        return FakeLLMClient()
    from . import providers

    cls = {"anthropic": providers.AnthropicClient, "openai": providers.OpenAIClient}.get(settings.provider)
    if cls is None:
        raise ConfigError(f"Provider {settings.provider!r} is not implemented yet (Gemini is a stretch goal).")
    return cls(api_key=settings.api_key, model=settings.model, budget=budget)


def _record(run: dict, runs_dir: Path) -> Path:
    runs_dir.mkdir(parents=True, exist_ok=True)
    path = runs_dir / f"{dt.date.today().isoformat()}.jsonl"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(run, ensure_ascii=False) + "\n")
    return path


def cmd_generate(args: argparse.Namespace) -> int:
    from .checks import check_output
    from .prompts import build_messages

    brand = load_brand(args.brand)
    system, messages = build_messages(brand, args.task, args.input)
    client = make_client(args.provider)
    response: LLMResponse = client.complete(system, messages, max_tokens=args.max_tokens)
    result = check_output(response.text, brand, args.task)
    cost = None
    if args.price_in is not None and args.price_out is not None:
        cost = round(estimate_cost_usd(response.input_tokens, response.output_tokens, args.price_in, args.price_out), 6)
    run = {
        "timestamp": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "brand": brand.id,
        "task": args.task,
        "input": args.input,
        "output": response.text,
        "provider": response.provider,
        "model": response.model,
        "input_tokens": response.input_tokens,
        "output_tokens": response.output_tokens,
        "latency_s": round(response.latency_s, 3),
        "estimated_cost_usd": cost,
        "checks_passed": result.passed,
        "violations": [asdict(v) for v in result.violations],
        "status": "PENDING_HUMAN_APPROVAL" if brand.approval_required else "DRAFT",
    }
    print(json.dumps(run, ensure_ascii=False, indent=2))
    if not args.no_record:
        _record(run, Path(args.runs_dir))
    return 0 if result.passed else 2


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="brand_assistant", description="Brand-aware LLM assistant (Week 1)")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("brands", help="list available brands")
    gen = sub.add_parser("generate", help="generate and check one output")
    gen.add_argument("--brand", required=True)
    gen.add_argument("--task", required=True)
    gen.add_argument("--input", required=True)
    gen.add_argument("--provider", default=None, help="fake | anthropic | openai (default: LLM_PROVIDER)")
    gen.add_argument("--max-tokens", type=int, default=512)
    gen.add_argument("--price-in", type=float, default=None, help="USD per million input tokens")
    gen.add_argument("--price-out", type=float, default=None, help="USD per million output tokens")
    gen.add_argument("--runs-dir", default="runs")
    gen.add_argument("--no-record", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command == "brands":
            print("\n".join(list_brands()))
            return 0
        return cmd_generate(args)
    except NotImplementedError as exc:
        print(f"Not implemented yet: {exc}\nThis is expected until you finish the assignment.", file=sys.stderr)
        return 3
    except ConfigError as exc:
        print(f"Configuration error: {exc}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
