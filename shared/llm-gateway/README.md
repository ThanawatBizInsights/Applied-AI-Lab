# LLM Gateway

**Status:** not started. Built in **Week 4** (Course 01 main project), from the Week 1
`brand_assistant` client interface.

## Planned interface (v0.1)
```python
gateway.complete(task="caption", project="balena", system=..., messages=..., route="cheapest-acceptable")
# -> LLMResponse(text, provider, model, input_tokens, output_tokens, latency_s, cost_usd, route_reason)
```
## Requirements (from Week 4 ASSIGNMENT.md)
- Adapters for ≥ 2 providers + fake; tool calling; routing rules; JSONL usage log
- Offline tests; no key ever logged; per-run request and cost budgets
