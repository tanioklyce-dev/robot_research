---
title: "Neural Networks: Zero to Hero — Karpathy's from-scratch lecture series (YouTube, 2022–2024)"
type: source
url: https://karpathy.ai/zero-to-hero.html
author: Andrej Karpathy
published: 2022-08-16 (first lecture) — 2024-06-09 (latest)
ingested: 2026-07-09
format: video lecture series (10 videos, ~19.5 h total) + Jupyter notebooks + exercises
license: MIT (companion repo karpathy/nn-zero-to-hero)
tags: [karpathy, pedagogy, backprop, mlp, batchnorm, transformers, gpt, tokenizer, lectures, zero-to-hero]
---

> [!note] Ingest depth
> Ingested from the [course page](https://karpathy.ai/zero-to-hero.html), the [companion GitHub repo](https://github.com/karpathy/nn-zero-to-hero) (23.4K stars, MIT, Jupyter notebooks + exercises per lecture), and the [YouTube playlist](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) metadata (titles, durations, upload dates verified via yt-dlp). The videos themselves were not watched for this ingest; per-lecture descriptions come from Karpathy's own summaries.

## Summary

**Neural Networks: Zero to Hero** is Karpathy's free lecture series building neural networks **from scratch, in code** — starting from a scalar autograd engine ([micrograd](karpathy-micrograd.md)) and ending at a full reproduction of GPT-2 (124M). The through-line is Karpathy's pedagogical stance that *language models are the best vehicle for learning deep learning*: the same character-level name-generator task ("makemore") is solved five times with progressively better machinery (bigram counts → MLP → activation-statistics-aware MLP with BatchNorm → manually-backpropagated MLP → WaveNet-style hierarchy), then scaled to a real transformer, tokenizer, and GPT-2 training run. Each lecture is live-coded end to end with nothing imported that hasn't been built or explained; the companion repo ships the notebooks and per-lecture exercises. Prerequisites: Python and "a vague recollection of calculus."

## The lectures

| # | Lecture | Date | Length |
|---|---------|------|--------|
| 1 | The spelled-out intro to neural networks and backpropagation: **building micrograd** | 2022-08-16 | 2h25m |
| 2 | The spelled-out intro to language modeling: **building makemore** (bigrams, PyTorch tensors, NLL loss) | 2022-09-07 | 1h57m |
| 3 | makemore Part 2: **MLP** (train/dev/test splits, learning-rate tuning, over/underfitting) | 2022-09-12 | 1h15m |
| 4 | makemore Part 3: **Activations & Gradients, BatchNorm** (forward/backward-pass statistics, why init matters) | 2022-10-04 | 1h55m |
| 5 | makemore Part 4: **Becoming a Backprop Ninja** (manual backprop through a 2-layer MLP + BatchNorm + CE, no autograd) | 2022-10-11 | 1h55m |
| 6 | makemore Part 5: **Building a WaveNet** (deeper hierarchical/convolutional architecture) | 2022-11-21 | 0h56m |
| 7 | **Let's build GPT: from scratch, in code, spelled out** (decoder-only transformer per "Attention is All You Need") | 2023-01-17 | 1h56m |
| 8 | **State of GPT** (Microsoft Build talk — the GPT training pipeline: pretrain → SFT → RLHF; not a build-along) | 2023-05-25 | 0h42m |
| 9 | **Let's build the GPT Tokenizer** (byte-pair encoding; why tokenization causes so many LLM pathologies; → minBPE repo) | 2024-02-20 | 2h13m |
| 10 | **Let's reproduce GPT-2 (124M)** (full training run: architecture, mixed precision, flash attention, distributed data-parallel, hyperparameters per GPT-2/GPT-3 papers; → [build-nanogpt] / [nanoGPT](karpathy-nanogpt.md) lineage) | 2024-06-09 | 4h01m |

Total ≈ 19.5 hours. Lectures 1–7 + 9–10 are live-coding builds; lecture 8 is a conference talk giving the systems-level view.

## Key claims / pedagogical arc

- **Backprop before frameworks.** Lecture 1 builds reverse-mode autodiff on scalars from nothing ("assumes only basic Python and a vague recollection of calculus") — the position that you don't understand `.backward()` until you've written it. Lecture 5 doubles down: having *learned* autograd, you throw it away and backprop through cross-entropy, BatchNorm, and matrix multiplies by hand, because "backprop is a leaky abstraction" — bugs like dead ReLUs and vanishing gradients are invisible unless you can read gradient flow.
- **One task, escalating machinery.** The makemore sequence (lectures 2–6) holds the task fixed (character-level names) and swaps the model, which isolates *what each architectural idea buys you* — the same design used by this wiki's own curriculum (fixed anchor exercises, escalating modules).
- **Activation/gradient statistics as first-class diagnostics** (lecture 4): watching histograms of activations, gradients, and update-to-weight ratios during training, and why BatchNorm made deep nets trainable — the practitioner skills behind [Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md) §5's normalization coverage and its "diagnose a stuck training run" goal.
- **Tokenization is where LLM weirdness lives** (lecture 9): a catalog of LLM failure modes (spelling, arithmetic, non-English handling) traced to BPE tokenization rather than the architecture.
- **Frontier-adjacent reproducibility** (lecture 10): GPT-2 (124M) reproduced in ~1 hour / ~$10 of cloud compute by 2024 — the same "modern ML on accessible compute" thread as [nanochat](karpathy-nanochat.md)'s $48-$100 ChatGPT pipeline.

## Curriculum hookup

This series is the closest existing external companion to the wiki's [robot-learning curriculum](../syntheses/curriculum/robot-learning-curriculum.md) Tier-1 modules:

- **[Module 1 — Neural networks and training](../syntheses/curriculum/curriculum-01-neural-networks.md)**: lectures 1–5 cover the module's §1–§5 almost exactly (neuron/MLP → loss → backprop/SGD → overfitting and train/dev/test hygiene → BatchNorm). Lecture 1 *is* the video form of the [micrograd](karpathy-micrograd.md) exit-ramp; lecture 5 is the video form of the [Kevin Clark gradient notes](clark-computing-nn-gradients.md) (manual vectorized backprop). Watch 1 → do micrograd; watch 5 → do Clark.
- **[Module 3 — Sequence models, attention, transformers](../syntheses/curriculum/curriculum-03-attention-and-transformers.md)**: lectures 7, 9, 10 are the build-along path to a trained GPT — the video companion to [nanoGPT](karpathy-nanogpt.md)/[nanochat](karpathy-nanochat.md).
- Lecture 6 (WaveNet) previews hierarchical/dilated-convolution ideas adjacent to [Module 2](../syntheses/curriculum/curriculum-02-cnns.md).

**Where it does NOT overlap:** nothing on robotics, control, RL, world models, or SSL/JEPA (Modules 4+) — it's a pure "how neural nets and LLMs actually work" foundation. Robot-specific material still has no Karpathy-quality equivalent.

## Entities mentioned

- **[Andrej Karpathy](../entities/andrej-karpathy.md)** — sole author/instructor.

## Concepts touched

- Backpropagation / reverse-mode autodiff (lectures 1, 5).
- MLPs, activation functions, initialization, BatchNorm (lectures 3–4) — [Module 1](../syntheses/curriculum/curriculum-01-neural-networks.md) §1/§5 territory.
- Language modeling, cross-entropy/NLL loss, train/dev/test methodology (lecture 2–3).
- Transformers / attention, tokenization (BPE), GPT-2/GPT-3 training practice (lectures 7, 9, 10) — Module 3 territory.

## Related sources

- [karpathy/micrograd](karpathy-micrograd.md) — the artifact lecture 1 builds.
- [karpathy/nanoGPT](karpathy-nanogpt.md) — the lineage lecture 10's build-nanogpt sits in.
- [karpathy/nanochat](karpathy-nanochat.md) — the modern end-to-end successor.
- [Kevin Clark — Computing NN Gradients](clark-computing-nn-gradients.md) — written companion to lecture 5.
- [Welch Labs — The Perceptron](welchlabs-perceptron.md) — the 20-min popular-level orientation before this; Zero to Hero is the do-the-work version.
- [fast.ai — Practical Deep Learning for Coders](fastai-practical-deep-learning.md) — the *library-first* onboarding ramp; Zero to Hero is the *from-scratch* complement (fast.ai teaches you to drive, Karpathy teaches you to build the engine).

## Open questions / TBD

- The series stops at mid-2024; Karpathy's later long-form videos ("[1hr Talk] Intro to LLMs", "Deep Dive into LLMs like ChatGPT", 2024–2025) are outside this playlist and would be a separate ingest if the wiki needs LLM-landscape (rather than build-from-scratch) coverage.
- Per-lecture caption-level ingest (via the yt-dlp workflow) is possible if any single lecture becomes load-bearing for a curriculum module — most likely candidates: lecture 4 (activation statistics) for the planned "common training pathologies" reference page.
