---
title: Energy-based models (EBMs)
type: concept
created: 2026-05-17
updated: 2026-08-30
sources: 7
tags: [ebm, energy-based-model, bengio, infonce, jepa, ibc, lecun, kona, latent-variable, constraint-satisfaction]
---

**Energy-based models (EBMs)** are a model family that learns a scalar **energy function** `E_θ(x, y)` over an input `x` and a candidate output (or completion) `y`, such that **low energy ↔ compatible / valid `(x, y)` pair**. Inference is **minimizing `E_θ(x, y)` over `y`** (or searching for a low-energy `y`), rather than directly sampling from an autoregressive distribution.

Contrast with the dominant alternatives:

| Family | Models | Inference |
| --- | --- | --- |
| **Autoregressive** | GPT-style LLMs, autoregressive VLAs | Sample `y_t` from `P(y_t | y_<t, x)`, token by token |
| **Latent-variable diffusion / flow** | DDPM, [Diffusion Policy](../../entities/diffusion-policy.md), [π0](../../sources/pi-zero-paper.md) flow-matching head | Iteratively denoise / flow toward valid `y` |
| **Energy-based (implicit)** | [IBC](../../entities/ibc.md), [Kona](../../entities/kona.md), JEPA training objectives | Find `argmin_y E_θ(x, y)` (often via optimization, MCMC, or amortized sampling) |

Diffusion / flow models can themselves be derived as a particular family of EBMs with a specific score-based training procedure — the boundary is not sharp.

## Why EBMs in this wiki

The wiki has three quite-different modern EBM applications, all downstream of [Yann LeCun](../../entities/yann-lecun.md)'s long-running advocacy of energy-based learning as an alternative to maximum-likelihood / autoregressive training — plus one much older construction that is **not** his:

1. **EBM for imitation learning** — [IBC (Florence et al., CoRL 2021)](../../sources/ibc-paper.md). Train `E_θ(obs, action)` so the demonstration action is the energy minimum; at inference, sample candidate actions and pick `argmin E`. Trained with InfoNCE (contrastive) loss requiring negative samples — the practical pain point that motivated [Diffusion Policy](../../entities/diffusion-policy.md) to switch to denoising.
2. **EBM as a training story for predictive representation learning** — the framing LeCun gives to JEPA in his **[2022 "A Path Towards Autonomous Machine Intelligence" paper](../../sources/lecun2022-path-towards-ami.md)**. JEPA's joint-embedding-predict-in-latent-space architecture is presented as a particular EBM: low energy means "predictor output matches target encoder output." The anti-collapse regularizers — [VICReg](../../sources/vicreg-paper.md), [SIGReg](../../sources/lejepa-paper.md), [DINO](../../entities/dinov2.md)-style EMA — are the practical machinery that keeps that EBM well-conditioned.
3. **EBM for reasoning / constraint satisfaction** — [Kona](../../entities/kona.md), the proprietary EBRM from [Logical Intelligence](../../entities/logical-intelligence.md). Non-autoregressive; operates in abstract vector space; natural language as I/O only. Productized in the [Aleph](../../entities/aleph.md) orchestration layer.

> [!note] Provenance correction — the wiki's earliest EBM is Bengio's
> §5.1 of **[Bengio et al. 2003, *A Neural Probabilistic Language Model*](../../sources/bengio2003-neural-probabilistic-language-model.md)** builds an **energy-minimization variant** of the neural LM: give the *output* word a feature vector too, and have the network emit a scalar `E(w_{t−n+1}, …, w_t) = v · tanh(d + Hx) + Σ_i b_{w_{t−i}}`, low for likely subsequences, normalized over candidate `w_t` to recover a conditional probability. Framed explicitly on [Hinton](../../entities/geoffrey-hinton.md)'s products of experts (2000) — hidden units *are* the experts — and as an extension of maximum-entropy models in which the basis functions are learned jointly rather than greedily selected.
>
> Two things it establishes that the LeCun-line framing above does not:
> - **The tractability boundary is the factorization, not the energy.** Because the sequence probability is decomposed into per-element conditionals, the gradient is exact — no contrastive divergence, unlike products-of-HMMs where experts view the whole sequence. This is the cleanest statement in the wiki of *when* an EBM is cheap to train.
> - **A concrete payoff from the output-side embedding**: out-of-vocabulary words get a probability, by initializing the unseen word's feature vector as a probability-weighted convex combination of the words that could have appeared in that context.
>
> The wiki's EBM thread has until now read as a LeCun research program. It is older and wider than that, and this is the counterexample. See also [distributed representations](distributed-representations.md).

## Key references in this wiki

- **[LeCun 2022 — A Path Towards Autonomous Machine Intelligence](../../sources/lecun2022-path-towards-ami.md)** — the conceptual anchor. Frames JEPA, the configurable world model, and intrinsic-cost training all as EBM-flavored constructions.
- **[IBC Paper (Florence et al., CoRL 2021)](../../sources/ibc-paper.md)** — first EBM-for-policy result in this wiki; introduced [PushT](../../entities/pusht.md); ancestor of [Diffusion Policy](../../entities/diffusion-policy.md).
- **[Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video, 2026-05)](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)** — first commercialized EBM-for-reasoning surface in this wiki ([Kona](../../entities/kona.md) + [Aleph](../../entities/aleph.md)).
- **[Welch Labs — LeCun's $1B Bet Against LLMs](../../sources/welchlabs-lecun-1b-bet-against-llms.md)** — popular explainer; covers the EBM ↔ JEPA ↔ "intelligence is a cake" arc.
- **[Kona EBMs page — Logical Intelligence (2026-05-14)](../../sources/2026-05-14-logical-intelligence-kona-ebms-page.md)** — first vendor-authored EBM-for-reasoning positioning page in the wiki. Verbatim framing: "It does not predict likely outcomes. It enforces constraints." / "Certainty, Not Probability." Marketing-light on tech but useful for citing how a commercial EBM player describes its own value proposition.

## Why LeCun pushes EBMs

A recurring framing across his work: the maximum-likelihood / autoregressive objective is **a poor fit when the output is high-dimensional, multimodal, or continuous** — because it forces a tractable normalization (softmax over a vocabulary or pixelwise Gaussian) that doesn't match the real distribution. EBMs sidestep the normalization by only modeling **unnormalized relative compatibility** between `x` and `y`. The trade is that **training is harder** (need negative samples, score matching, or contrastive surrogates) and **inference is harder** (need optimization over `y`, not a single forward pass).

This is the long thread connecting the [1993 Siamese signature-verification paper](../../sources/bromley1993-siamese-signature-verification.md) → contrastive SSL ([Barlow Twins](../../sources/barlow-twins-paper.md), [VICReg](../../sources/vicreg-paper.md)) → [JEPA](../world-models/jepa.md) → [Kona](../../entities/kona.md). Same underlying commitment, different applications and training-side machinery at each step.

## Related concepts

- [Joint-Embedding Predictive Architecture](../world-models/jepa.md) — JEPA is a particular EBM family for predictive representation learning.
- [Diffusion Policy](../../entities/diffusion-policy.md) and [DDPM](../../sources/ddpm-paper.md) — score-based / denoising models, derivable as a sub-family of EBMs.
- [IBC](../../entities/ibc.md) — first EBM-for-policy in this wiki.
- [Variational autoencoder](variational-autoencoder.md) — the explicit-density sibling: amortized variational inference ([VAE Paper](../../sources/vae-paper.md)) where EBMs go unnormalized.
- [Formal verification](formal-verification.md) — what EBM-style reasoning models like [Kona](../../entities/kona.md) are positioned to slot underneath.

## Mentioned in

- [LeCun 2022 — A Path Towards Autonomous Machine Intelligence](../../sources/lecun2022-path-towards-ami.md)
- [IBC Paper](../../sources/ibc-paper.md)
- [Aleph and Energy-Based Models: The AI That Refuses to Bullshit (video)](../../sources/2026-05-aleph-ebm-refuses-bullshit-video.md)
- [Welch Labs — LeCun's $1B Bet Against LLMs](../../sources/welchlabs-lecun-1b-bet-against-llms.md)
- [Kona: Energy-Based Models (EBMs) for AI Reasoning — Logical Intelligence page](../../sources/2026-05-14-logical-intelligence-kona-ebms-page.md)
- [Bengio et al. 2003 — A Neural Probabilistic Language Model](../../sources/bengio2003-neural-probabilistic-language-model.md) — §5.1 energy-minimization variant; the earliest EBM construction in the wiki.

## Open questions / TBD

- **Training procedures used by Kona** — not surfaced in materials ingested so far. The interview summary says "energy minimization" and "non-autoregressive" but doesn't specify whether training uses score matching, contrastive loss, denoising, or something else.
- **Hinton's products-of-experts (2000) and contrastive divergence** enter the wiki by citation only, through [Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md) §5.1. The tech report is not ingested, and it is the shared ancestor of both the Bengio and LeCun branches above.
- **Empirical reproducibility** of the cost-vs-LLM claims for EBMs — the IBC paper found EBMs hard to scale beyond PushT; Kona's claimed Sudoku-at-$4 hasn't been independently corroborated in this wiki.
