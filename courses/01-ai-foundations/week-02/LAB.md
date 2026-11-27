# Week 02 — Guided lab (2 hours)

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 02 materials"*.

## Planned checkpoints
1. Implement forward and backward passes of a 2-layer network in NumPy on a toy dataset; plot the loss curve.
2. Implement scaled dot-product attention in NumPy and check it against a hand calculation.
3. Use a Hugging Face tokenizer (CPU only, small download) to tokenise 20 Thai and 20 English Balena captions.
4. Compute tokens-per-character for each language and estimate API cost at published prices.

Each checkpoint will include: the commands, the expected output, a prediction question and a
commit message to use.

## Troubleshooting (known issues)
- Tokenizer download blocked or slow: set `HF_HUB_OFFLINE=1` after the first download; use small tokenizers only.
- NumPy shape errors in attention: print `.shape` after every step; Q·Kᵀ must be (seq, seq).
- Exploding loss: lower the learning rate by 10x; check that inputs are normalised.
