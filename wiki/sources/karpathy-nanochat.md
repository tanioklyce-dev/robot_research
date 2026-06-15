---
title: "nanochat — Karpathy's full ChatGPT pipeline for ~$100 (GitHub repo, 2025)"
type: source
url: https://github.com/karpathy/nanochat
author: Andrej Karpathy
affiliation: independent / formerly OpenAI & Tesla
published: 2025-10-13 (initial commit / "original nanochat post"); active development through 2026
ingested: 2026-05-14
tags: [karpathy, nanochat, gpt, llm, transformer, pedagogy, github, reference-implementation, training-pipeline, speedrun, leaderboard]
github_stats: 53K stars, 7.2K forks (May 2026); active master branch
---

> [!note] Ingest depth
> Read the README in full (~200 lines). Repo metadata (file structure, leaderboard table, dtype-handling section, contributing notes) captured below; code itself (`nanochat/gpt.py`, `runs/speedrun.sh`, etc.) is the actual artifact.

## Summary

**nanochat** — "the simplest experimental harness for training LLMs." Single-GPU-node, minimal, hackable, end-to-end: **tokenization → pretraining → SFT → RL → evaluation → inference → chat UI**. Headline result: **train your own GPT-2 capability LLM (a 2019 $43,000 model) for $48 in ~2 hours on an 8XH100 spot instance** (~$15 on cheapest spot pricing). The repo is the modern successor to [nanoGPT](karpathy-nanogpt.md), which the README explicitly retired in November 2025 in favor of this one.

**The single complexity dial:** `--depth` (number of transformer layers). Everything else — width, head count, LR schedule, training horizon, weight decays — is computed automatically to be compute-optimal. GPT-2 capability lives around `--depth=24–26`. This is a deliberate pedagogical choice: it forces all candidate changes to the repo to be *principled* (must work across the depth sweep), not depth-specific hacks.

**Why it matters to this wiki.** nanochat is the **modern reference end-to-end LLM training pipeline** — the wiki's recommended companion to [nanoGPT](karpathy-nanogpt.md)'s `model.py` for [Curriculum Module 3](../syntheses/curriculum/curriculum-03-attention-and-transformers.md), and the substrate that [autoresearch](karpathy-autoresearch.md) (Karpathy's March 2026 agent-driven research project) iterates on. The fact that a GPT-2-capability model now costs ~$48 to reproduce is a wiki-relevant data point on its own: it pins the **"how reproducible is modern LLM training on consumer/prosumer compute?"** question with a concrete number.

## The Time-to-GPT-2 leaderboard (README, May 2026)

The repo maintains a public leaderboard for the wall-clock time required to beat OpenAI's 2019 GPT-2 (1.6B) CORE score (0.256525) on an 8XH100 node:

| # | Hours | val_bpb | CORE | Description | Date | Contributors |
|---|-------|---------|------|-------------|------|--------------|
| 0 | 168 | — | 0.2565 | Original OpenAI GPT-2 checkpoint | 2019 | OpenAI |
| 1 | 3.04 | 0.7483 | 0.2585 | d24 baseline | Jan 29 2026 | Karpathy |
| 2 | 2.91 | 0.7450 | 0.2578 | d26 slightly undertrained + fp8 | Feb 2 2026 | Karpathy |
| 3 | 2.76 | 0.7464 | 0.2602 | bump batch size to 1M tokens | Feb 5 2026 | Karpathy |
| 4 | 2.02 | 0.7185 | 0.2571 | NVIDIA ClimbMix dataset | Mar 4 2026 | ddudek + Karpathy |
| 5 | 1.80 | 0.7181 | 0.2690 | **autoresearch round 1** | Mar 9 2026 | Karpathy |
| 6 | 1.65 | 0.7180 | 0.2626 | **autoresearch round 2** | Mar 14 2026 | Karpathy |

**Rows 5 and 6 are the wiki-relevant entries**: improvements driven by Karpathy's [autoresearch](karpathy-autoresearch.md) project — an AI agent iterating on a simplified train.py overnight. Going from 2.02 → 1.65 hours (an 18% wall-clock improvement) over two rounds is **the first public empirical evidence that an AI coding agent can produce real, measurable improvements to a frontier ML training pipeline** — within nanochat's specific 8XH100 / 5-min-experiment budget. See the [autoresearch source page](karpathy-autoresearch.md) for the design.

## What's in the repo

```
nanochat/
├── gpt.py             # the GPT nn.Module — same family as nanoGPT's model.py
├── optim.py           # AdamW + Muon optimizer (single-GPU + distributed)
├── tokenizer.py       # BPE tokenizer wrapper (GPT-4 style)
├── dataloader.py      # tokenizing distributed dataloader
├── dataset.py         # pretraining data utilities
├── engine.py          # KV-cache inference
├── execution.py       # lets the LLM execute Python code as a tool
├── core_eval.py       # DCLM CORE benchmark
├── loss_eval.py       # bits-per-byte eval
├── checkpoint_manager.py
├── report.py
└── ui.html            # the chat web UI
runs/
├── speedrun.sh        # the canonical $100 train-and-chat pipeline (8XH100)
├── miniseries.sh      # train a compute-optimal model family across depths
├── scaling_laws.sh    # scaling experiments
└── runcpu.sh          # small example for CPU/MPS
scripts/
├── tok_train.py       # train tokenizer
├── base_train.py      # pretrain base model
├── chat_sft.py        # supervised fine-tuning
├── chat_rl.py         # reinforcement learning
├── chat_eval.py       # eval (CORE, GSM8K, ARC, MMLU, HumanEval, ...)
└── chat_web.py        # serve the chat web UI
tasks/                 # arc, gsm8k, humaneval, mmlu, smoltalk, spellingbee
```

The `runs/speedrun.sh` script is the **single entry point**: it runs the entire pipeline end-to-end on an 8XH100 node and produces a chat-able model in ~3 hours.

## Notable design choices

1. **One file per concern, no framework.** Same philosophy as nanoGPT. There are no factory functions, no config-object hierarchies, no plugin systems. Every script is ~hand-readable.
2. **The `--depth` knob.** A single integer sets the model size; all other hyperparameters derive from it via compute-optimal scaling laws. This is a structural commitment: changes to the repo have to be principled across the depth sweep, not handpicked for one size.
3. **Explicit precision via `COMPUTE_DTYPE`.** No `torch.amp.autocast`. Model weights stored fp32 (for optimizer precision); custom `Linear` casts to bf16 / fp16 / fp32 per hardware in the forward pass. Auto-detected on CUDA SM 80+ (bf16) vs SM <80 (fp32). `NANOCHAT_DTYPE` env var overrides.
4. **Covers RL.** `scripts/chat_rl.py` and the chat-eval suite (ARC, GSM8K, MMLU, HumanEval) bring the repo into RLHF / RLVR territory — a step beyond pretraining-only nanoGPT.
5. **AI-contribution disclosure policy.** "When submitting a PR, please declare any parts that had substantial LLM contribution and that you have not written or that you do not fully understand." Explicit norm-setting in a 2026 LLM-training repo.

## Hardware footprint

- **Reference:** 8XH100 80GB node, ~$24/hr at 2026 spot pricing → ~$48 for a 2-hour GPT-2-capable run, ~$15 on cheapest spot deals.
- **Also runs:** 8XA100 (slower), single GPU (8× slower; auto-falls-back to gradient accumulation), CPU/MPS via `runs/runcpu.sh` (intentionally tiny models for testing the pipeline).
- **VRAM:** 80GB default; for <80GB, tune `--device-batch-size` down from 32 → 16 → 8 → 4 → 2 → 1.

## Curriculum hookup

Recommended companion to [nanoGPT](karpathy-nanogpt.md) for **[Curriculum Module 3 — Sequence models, attention, transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)**:

- **Architecture:** read `nanochat/gpt.py` (or stick with nanoGPT's `model.py` if simpler is better).
- **End-to-end training pipeline:** read `runs/speedrun.sh` + the `scripts/base_train.py` it calls.
- **Modern optimizer (Muon):** read `nanochat/optim.py`. The wiki's optimizer coverage stops at AdamW (Module 1); Muon (Jordan et al. 2024) is the leaderboard-current optimizer worth reading once you're past AdamW.
- **RL stage:** `scripts/chat_rl.py` is the wiki's only ingested code reference for RLHF-class training; could anchor a future Module-8 deepening.

The repo also sets up [autoresearch](karpathy-autoresearch.md): "The training code in autoresearch is a simplified single-GPU implementation of nanochat." If a future curriculum module covers agent-driven research, nanochat is the substrate.

## What nanochat is *not*

- Not a production framework. There are no model factories, no flexible configs, no plugin architecture. "Accessibility is about overall cost but also about cognitive complexity."
- Not multimodal. Text-only. No vision, no audio. For VLA-class systems see the wiki's [VLA models](../concepts/learning/vla-models.md) concept page.
- Not state-of-the-art on raw capability. A $48 model trained in 2 hours is GPT-2-grade, "a bit like talking to a kindergartener." For frontier capability you need ~6 orders of magnitude more compute.
- Not designed for distributed training across nodes. Single-node only (1–8 GPUs).

## Entities mentioned

- **[Andrej Karpathy](../entities/andrej-karpathy.md)** — author.
- **Alec Radford** — credited in acknowledgements as "chief LLM whisperer."
- **HuggingFace** — fineweb + smoltalk datasets (acknowledged).
- **Lambda** — compute provider (acknowledged).
- **modded-nanoGPT** ([KellerJordan repo](https://github.com/KellerJordan/modded-nanogpt)) — gamified-leaderboard pretraining repo; explicit inspiration for nanochat's speedrun leaderboard.

## Concepts touched

- **[Transformer](../glossary.md#transformer)** — `nanochat/gpt.py`.
- **Tokenization (BPE)** — `tokenizer.py` + `tok_train.py`.
- **Compute-optimal scaling laws** — the `--depth` design rests on these.
- **RLHF / RLVR** — `chat_rl.py` + `tasks/`.
- **DCLM CORE benchmark** — `core_eval.py`. The metric the speedrun leaderboard tracks.
- **Muon optimizer** — `optim.py`; wiki currently has no other reference.

## Related sources

- [karpathy/nanoGPT](karpathy-nanogpt.md) — the deprecated predecessor; nanochat is the active successor.
- [karpathy/autoresearch](karpathy-autoresearch.md) — agent-driven research on a simplified version of nanochat's training code.
- [karpathy/micrograd](karpathy-micrograd.md) — same author; the autograd-from-scratch predecessor.
- [Vaswani et al. 2017 — Attention Is All You Need](attention-is-all-you-need.md) — architectural ancestor.

## Open questions / TBD

- **The Muon optimizer** (Jordan et al. 2024) is referenced in `nanochat/optim.py` but not yet a separate wiki source. Worth a stub if the curriculum extends to Module-1 optimizer coverage beyond AdamW.
- **DCLM CORE benchmark** is the leaderboard's measurement; not yet a wiki source page. Useful if a future synthesis covers "what does GPT-2-capability mean numerically?"
- **The autoresearch-driven rows (5 & 6 of the leaderboard)** are the most wiki-relevant entries here — see [the autoresearch source page](karpathy-autoresearch.md) for the deeper analysis.
