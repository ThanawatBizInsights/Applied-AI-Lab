# Week 01 — Starter code

```
starter-code/
├── brand_assistant/          # assignment package
│   ├── brands/*.json         # brand rules: Balena, CheckKhum, Little Snowy Owl Studio (provided)
│   ├── models.py             # dataclasses (provided)
│   ├── llm.py                # client interface, FakeLLMClient, RequestBudget (provided)
│   ├── config.py             # settings from .env, key masking (provided)
│   ├── cli.py, __main__.py   # command-line interface (provided)
│   ├── loader.py             # TODO A1
│   ├── prompts.py            # TODO A2
│   ├── checks.py             # TODO A3
│   └── providers.py          # TODO A4
└── w01_exercises/            # lab exercises 1–3 (TODOs) + data/sample_posts.json
```

Run the CLI from the repository root:

```bash
export PYTHONPATH=courses/01-ai-foundations/week-01/starter-code
uv run python -m brand_assistant brands
uv run python -m brand_assistant generate --brand balena --task caption --input "แนะนำ Cold Brew Original"
```

Until you implement the TODOs, `generate` exits with code 3 and a "Not implemented yet" message.
That is expected. Exit codes: 0 = passed checks, 2 = brand-rule errors, 3 = TODO not done,
4 = configuration error.

Every TODO's docstring is its specification; the tests in `../tests/` are its acceptance tests.
There are no solutions in this repository, on purpose.
