---
title: "nanoGPT — Karpathy's minimal GPT training repo (GitHub repo, 2022; deprecated Nov 2025)"
type: source
url: https://github.com/karpathy/nanoGPT
author: Andrej Karpathy
affiliation: independent / formerly OpenAI & Tesla
published: 2022-12-28 (initial commit)
ingested: 2026-05-14
created: 2026-05-14
updated: 2026-05-14
tags: [karpathy, nanogpt, gpt, transformer, pedagogy, github, reference-implementation, deprecated]
github_stats: 58K stars, 10K forks (May 2026); officially deprecated 2025-11
---

> [!note] Ingest depth
> Read the README only (~150 lines). The repo's code (`model.py` ~300 lines, `train.py` ~300 lines, plus configs and data prep) is the actual artifact; the README is the entry point.

> [!warning] Officially deprecated
> Per the README header: "**Update Nov 2025**: nanoGPT has a new and improved cousin called [nanochat](https://github.com/karpathy/nanochat). It is very likely you meant to use/find nanochat instead. nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity." For *training new models* in 2026 use [nanochat](karpathy-nanochat.md). For *understanding the transformer architecture as a clean reference implementation*, nanoGPT's `model.py` is still the wiki's recommended read — it's simpler and the deprecation doesn't change that the code is correct.

## Summary

**nanoGPT** — "The simplest, fastest repository for training/finetuning medium-sized GPTs." A rewrite of Karpathy's earlier `minGPT` that prioritizes "teeth over education": `train.py` reproduces GPT-2 (124M) on OpenWebText in ~4 days on a single 8XA100 40GB node. Two files matter: **`model.py` is a ~300-line GPT model definition**, and **`train.py` is a ~300-line training loop**. The model can optionally load OpenAI's GPT-2 weights.

**Why it matters to this wiki.** `model.py` is the **canonical clean reference implementation of a decoder-only transformer** — the de-facto "read this to understand transformers in code" pointer in the field. The repo is the recommended exit-ramp at the bottom of [Curriculum Module 3](../syntheses/curriculum-03-attention-and-transformers.md) for *architecture*; for *training pipelines* in 2026 use the successor [nanochat](karpathy-nanochat.md).

## What's in the repo

- **`model.py`** (~300 lines) — `GPT` class. Encapsulates token + position embedding, a stack of transformer blocks (LN → causal self-attn → residual → LN → MLP → residual), a final LN + LM head. Tied embedding-and-output weights. Causal masking implemented via a registered triangular buffer. Optional loading of OpenAI GPT-2 weights.
- **`train.py`** (~300 lines) — distributed-data-parallel training loop (DDP); AdamW; LR warmup + cosine decay; gradient accumulation; mixed precision (`bf16` by default); `torch.compile`; periodic eval + checkpoint.
- **`sample.py`** — text generation from a trained or pretrained checkpoint.
- **`config/`** — Hydra-free Python-file configs: `train_shakespeare_char.py` (3-minute baby GPT on Shakespeare), `train_gpt2.py` (4-day GPT-2 124M on OpenWebText), `finetune_shakespeare.py`, etc.
- **`bench.py`** — training-loop benchmarking minus the bookkeeping.

## Hardware footprint

| Setup | Approx. time | Approx. result |
|---|---|---|
| Single GPU, char-level Shakespeare (`train_shakespeare_char.py`) | 3 minutes on A100 | val loss ~1.47; coherent Shakespeare-shaped output |
| MacBook CPU, char-level Shakespeare, small overrides | ~3 minutes | val loss ~1.88; rougher output |
| MPS on Apple Silicon | 2-3× faster than CPU | (intermediate) |
| 8XA100 40GB, GPT-2 124M on OpenWebText | ~4 days | val loss ~2.85 (matches finetuned-on-OWT GPT-2) |

The pedagogical strength is that the **same `train.py` works across all four** — just different configs.

## Why deprecated, but still useful

The README's Nov 2025 update directs new users to [nanochat](karpathy-nanochat.md), which is a structural superset (tokenizer + pretrain + SFT + RL + chat UI; "Time-to-GPT-2" speedrun leaderboard; one-knob complexity dial via `--depth`). For *training new models* there's no reason to use nanoGPT in 2026.

But for the wiki's curriculum purpose — **a clean transformer reference implementation that you read top-to-bottom** — nanoGPT's `model.py` is still the right call:

- nanoGPT is **simpler** (no tokenizer training, no SFT, no chat UI, no leaderboard machinery).
- nanoGPT's `model.py` is **standalone** (~300 lines + standard PyTorch); nanochat's `nanochat/gpt.py` is similar in spirit but lives alongside ~20 other files.
- The transformer architecture in both repos is **basically the same** — once you understand nanoGPT's `model.py`, you understand the architecture nanochat uses too.

If you want both pedagogy *and* state-of-the-art training, read nanoGPT's `model.py` for the architecture and nanochat's `runs/speedrun.sh` for the modern training pipeline.

## Curriculum hookup

Recommended reading for **[Curriculum Module 3 — Sequence models, attention, transformers](../syntheses/curriculum-03-attention-and-transformers.md)**, alongside the **[Attention Is All You Need paper](attention-is-all-you-need.md)** ingest. Specifically:

- Module 3 §3 (self-attention) → `CausalSelfAttention` class in `model.py`.
- Module 3 §5 (positional encoding) → learned `nn.Embedding(block_size, n_embd)` in `model.py` (nanoGPT uses learned positions, not sinusoidal — the paper showed they perform comparably).
- Module 3 §6 (transformer block) → `Block` class.
- Module 3 §7 (causal masking) → the registered triangular buffer in `CausalSelfAttention`.

The repo also acts as the **practical answer to "now what?"** at the end of Module 3 — having understood the paper, you can clone this repo, train a Shakespeare baby GPT on whatever hardware you have, and have a working transformer within an hour.

## Entities mentioned

- **[Andrej Karpathy](../entities/andrej-karpathy.md)** — sole author.

## Concepts touched

- **[Transformer](../glossary.md#transformer)** — clean code reference.
- **Decoder-only / autoregressive language models.**
- **Causal masking.**
- **Distributed Data Parallel (DDP) training.**
- **`torch.compile` + bf16 mixed precision** — practical tricks the curriculum mentions but doesn't show in code.

## Related sources

- [Vaswani et al. 2017 — Attention Is All You Need](attention-is-all-you-need.md) — the paper this code implements.
- [karpathy/nanochat](karpathy-nanochat.md) — the deprecation target / spiritual successor.
- [karpathy/micrograd](karpathy-micrograd.md) — same author, scalar autograd predecessor.
- [karpathy/autoresearch](karpathy-autoresearch.md) — same author, agent-driven research on a simplified nanochat.

## Open questions / TBD

- Whether to recommend the `master` branch or a specific tagged commit for the curriculum exercise. The repo is no longer actively maintained, so the current state should be stable, but check for breakage with newer PyTorch versions.
