# Week 02 — Lecture (2 hours): Neural networks, transformers, tokenisation and inference

> **Status: OUTLINE.** Full materials are written when you finish the previous week (see `ROADMAP.md`). Ask Claude or ChatGPT: *"Expand week 02 materials"*.

Principles before tools. Planned sequence:

1. From linear regression to a neuron: weights, bias, activation, loss
2. Backpropagation as the chain rule; gradient descent; learning rate
3. Embeddings: turning tokens into vectors
4. Self-attention step by step on a 3-token example
5. The transformer block: attention, MLP, residuals, layer norm
6. Tokenisation: bytes, BPE merges, why Thai (no spaces between words) tokenises differently
7. Inference: logits → probabilities → sampling; KV cache; prefill vs decode

Each section will include: the core idea, a worked example linked to [Balena Roastery](../../../projects/balena/README.md), [CheckKhum (เช็กคุ้ม)](../../../projects/checkkhum/README.md),
a "predict before you run" question and a common misconception.
