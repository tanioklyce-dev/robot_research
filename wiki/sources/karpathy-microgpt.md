---
title: "microGPT — train and inference a GPT in 243 lines of dependency-free Python"
type: source
url: http://karpathy.github.io/2026/02/12/microgpt/
author: Andrej Karpathy
affiliation: independent / formerly OpenAI & Tesla
published: 2026-02-11 (release) / 2026-02-12 (blog post)
ingested: 2026-07-27
code: https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95
tags: [karpathy, microgpt, gpt, transformer, autograd, pedagogy, reference-implementation, minimal, curriculum]
---

> [!note] Ingest route
> Surfaced via a secondary article ([Sumit Pandey, *Towards Deep Learning*, 2026-02-15](https://www.towardsdeeplearning.com/andrej-karpathy-just-built-an-entire-gpt-in-243-lines-of-python-7d66cfdfa301), member-only) and then ingested from **Karpathy's own blog post and gist** rather than the secondary. The artifact is the gist; the blog post is the walkthrough.

## Summary

Karpathy's **microGPT** is a single dependency-free Python file that trains *and* runs a GPT end to end — dataset download, tokenizer, a hand-rolled scalar autograd engine, a GPT-2-shaped transformer, Adam, the training loop, and autoregressive sampling. His framing: this is **"the *full* algorithmic content of what is needed. Everything else is just for efficiency. I cannot simplify this any further."** He calls it an "art project" and "the culmination of multiple projects" — the terminus of the `micrograd` → `makemore` → `nanoGPT` → `nanochat` line, run in the opposite direction from `nanochat`: not *how cheaply can you build a real ChatGPT*, but **how little code contains the entire idea**.

## What's in the file

| Component | Detail |
|---|---|
| **Imports** | Standard library only — `os`, `math`, `random`, `argparse`. **No PyTorch, no NumPy.** |
| **Dataset** | ~**32,000 names**, one per line, downloaded from a URL at runtime |
| **Tokenizer** | Character-level — 26 lowercase letters + 1 BOS token = **vocab 27** |
| **Autograd** | A `Value` class building a computation graph and backpropagating through it (~40 lines, per third-party walkthroughs) — `micrograd` reincarnated inside the file |
| **Architecture** | Single-layer GPT, multi-head attention, **4 heads**, **16 embedding dims**, **block size 16** |
| **Optimizer** | **Adam** with linear learning-rate decay |
| **Training** | **1,000 steps**, ~**1 minute on a MacBook** (CPU) |
| **Inference** | Autoregressive sampling with temperature |
| **Model size** | **4,192 parameters** |
| **Loss** | ~**3.3** (uniform-random baseline) → ~**2.37** |
| **Output** | Plausible novel names — *"kamon," "karai," "yeran," "anna"* |

**Deliberately omitted:** batching, GPU acceleration, real (sub-word) tokenization, deeper/wider architectures, post-training, deployment. Everything in that list is characterized as efficiency or product concern, not algorithm.

> [!warning] Line-count discrepancy
> **243 lines** is the figure Karpathy states in his own release announcement and the one all coverage uses; it is in this page's title for that reason. One reading of the blog post renders it as a "200-line script." The gist is the authority and was not line-counted directly during ingest. Treat 243 as the citable number and the difference as unresolved (plausibly whitespace/comments, or a post-release edit).

## Why it matters

**It isolates the algorithm from the infrastructure.** Every other reference implementation in this wiki still delegates something essential to a framework — `nanoGPT`'s `model.py` is clean but sits on PyTorch's autograd and CUDA. microGPT delegates nothing: the backward pass is in the file. For anyone whose mental model of "what a transformer *is*" has a PyTorch-shaped hole in it, this is the artifact that fills it.

**It is a scale statement as much as a code statement.** 4,192 parameters, one layer, 16 embedding dims, a minute on a laptop CPU, and it still learns the statistical structure of English names well enough to generate new plausible ones. The distance from here to a frontier model is entirely **scale, data, and engineering** — the algorithmic content is what's in the file. That is the pedagogical claim, and stating it this concretely is the contribution.

**Placement in the Karpathy line.** [micrograd](karpathy-micrograd.md) taught backprop; [nanoGPT](karpathy-nanogpt.md) taught the architecture; [nanochat](karpathy-nanochat.md) taught the full pipeline at ~$100; **microGPT collapses all three into one file** at the cost of every practical concern. See [Andrej Karpathy](../entities/andrej-karpathy.md).

## Entities mentioned

- [Andrej Karpathy](../entities/andrej-karpathy.md) — author.

## Concepts touched

- Transformers / attention — see [curriculum module 3](../syntheses/curriculum/curriculum-03-attention-and-transformers.md).
- Backpropagation and autograd — see [curriculum module 1](../syntheses/curriculum/curriculum-01-neural-networks.md).

## Open questions

- **Exact line count** — see the warning above; resolvable by reading the gist directly.
- **Is the attention causal and is it single-head-per-block or genuinely multi-head?** Reported as 4 heads at 16 dims; the head-dim arithmetic and masking details were not verified from source.
- **The secondary article is paywalled** and adds nothing beyond the primary; filed as the ingest route only, not as a separate source page.
