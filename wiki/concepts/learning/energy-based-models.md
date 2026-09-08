---
title: Energy-based models (EBMs)
type: concept
created: 2026-05-17
updated: 2026-09-07
sources: 12
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

## The five distinctions the lecture notes draw that this page did not

Added on ingesting **[Dawid & LeCun's Les Houches lecture notes](../../sources/dawid-lecun-lvebm-lecture-notes.md)** (2023), which are the derivation behind the [2022 position paper](../../sources/lecun2022-path-towards-ami.md) and the most careful EBM exposition in this wiki.

**1. The energy is for inference. The loss is for training. They are different functions.**

> The energy function is **not** the objective function to minimize within the learning! The energy is used only for inference.

Training sculpts an energy landscape; the thing you descend is a loss whose job is to make observed configurations lower than unobserved ones. The degenerate case where they coincide is the **Hopfield network** (`L(y_train, w) = F_w(y_train)`, Hebbian update) — and its known pathology, **spurious minima**, is what having no contrastive term costs you. That is representation collapse's 1982 ancestor.

**2. Maximum likelihood is a contrastive method.** Substituting Gibbs–Boltzmann into the negative log-likelihood gives `L_NLL = F_w(x,y) + (1/β) log ∫ dy′ exp[−β F_w(x,y′)]` — push the data's energy down, push everything's energy up, gradient of the second term approximable by Monte Carlo. Its failure mode is named: it wants *"an infinitely deep and infinitely narrow canyon"* at the data manifold, hence the need for a prior or weight limits.

This matters for how the wiki frames the autoregressive-vs-JEPA argument. Likelihood training is not a *different paradigm* from contrastive learning; in energy terms it is **a contrastive method with a particularly expensive negative-sampling scheme**.

**3. Collapse is the price of multimodality, not a defect of joint embedding.**

| Architecture | Can collapse? | Can be multimodal? |
|---|---|---|
| Deterministic regression, `F = ‖y − Net(x)‖` | **no** | **no** |
| Joint embedding, `F = D(s_x, s_y)` | **yes** | yes |
| Latent-variable generative | yes | yes |
| Autoencoder | yes (identity function) | yes |

> **Every model that can be multimodal, i.e., have multiple predictions for a single input, is susceptible to collapse.**

**4. Regularized training = bounding the *volume* of the low-energy region**, and that single idea unifies a shelf of classical methods as `L = D(y, Dec(Enc(y))) + R(Enc(y))`: PCA (low rank), autoencoder (bottleneck), k-means (discreteness), Gaussian mixtures, sparse coding (explicit `λ‖z‖₁`). Score matching is the third route — flatten the gradient and sharpen the curvature at data points.

**5. The stated reason the field abandoned contrastive methods** is scaling, and it is asserted rather than proved: generating contrastive points has *"bad (even exponential!) scaling with the data dimension"*, making them *"unlikely to lead to autonomous intelligence of the future."* This claim is the hinge of the whole JEPA design argument and deserves to be held as a hypothesis — [SimCLR](../../sources/simclr-paper.md) and [MoCo](../../sources/moco-v3-paper.md) did scale.

> [!note] What is lost by giving up probability, stated by its advocates
> Two costs the notes are explicit about: uncertainty becomes hard to reason about, and **energies are uncalibrated** — measured in arbitrary units, so *"combining two separately trained EBMs is not straightforward."* The design consequence is that the architecture must avoid passing outputs between separately trained components. There is also a technical objection to normalizing even when you can: per-state normalization introduces the **label bias problem**, so *"it is hurtful to normalize those scores."*

## Prehistory: the anti-collapse ladder is forty years older than the wiki records

| Year | Model | Energy | Anti-collapse device |
|---|---|---|---|
| 1982 | **Hopfield network** | `F(y) = −Σ y_i w_ij y_j` | **none** — loss *is* the energy; spurious minima follow |
| 1983 | **Boltzmann machine** | adds hidden units `z` | **contrastive term**, MCMC-sampled: positive and negative phases |
| 1983 | Restricted BM | `w^yy = w^zz = 0` | same, cheaper sampling |

Both are explicitly spin-glass/Ising constructions, and the Boltzmann machine is *"the first introduction of hidden units"* — i.e. the first latent variables. [The anti-collapse lineage](../../syntheses/world-models/ssl-anti-collapse-lineage.md) begins its table in 2018; the shape of the problem and the shape of the fix are both much older.

### The spin glass returns — as a model of the loss, not the network (2015), and as an objective (2017)

Thirty years after Hopfield, the same mathematics comes back in LeCun's orbit twice, with the object changed each time — now filed from the primaries:

| Year | Paper | What the spin glass / Gibbs machinery models | What it buys |
|---|---|---|---|
| 2015 | [The Loss Surfaces of Multilayer Networks](../../sources/choromanska2015-loss-surfaces-multilayer-networks.md) | **the training loss** of a ReLU network, as an *H*-spin spherical spin-glass Hamiltonian (under decoupling assumptions the authors call "possibly unrealistic") | low-index critical points sit in a **band just above the global minimum**; bad minima vanish exponentially with size; the global minimum is unreachable and overfits |
| 2017 | [Entropy-SGD](../../sources/chaudhari2017-entropy-sgd.md) | **a Gibbs distribution over weights** focused near the current iterate; its log-partition function — the **local free entropy** — becomes the objective | optimization biased toward **wide valleys**, which is where SGD's minima already sit (~94% near-zero Hessian eigenvalues) |

The 2017 move is the one that belongs on this page: **free energy used as a training objective**. The Les Houches principle above — regularized EBM training *bounds the volume of the low-energy region* — is stated about the energy over *inputs*; Entropy-SGD applies the same idea to the energy over *weights*, measuring that volume locally and climbing it. And it raises the question [loss-landscape geometry](loss-landscape-geometry.md) files: on a joint-embedding loss the widest low-energy valley is the collapsed one, so the anti-collapse devices in this page's prehistory table are changing *which minima exist*, not which the optimizer finds.

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
- [Dawid & LeCun 2023 — Introduction to Latent Variable Energy-Based Models](../../sources/dawid-lecun-lvebm-lecture-notes.md) — the Les Houches lectures; the source for the five distinctions and the prehistory above.
- [JEPA Through the Eyes of a Physicist (Fajmanova, 2026)](../../sources/jepa-vs-physics-moudrkat.md) — an outside reading of the same material; useful for the coarse-graining framing, wrong on the collapse mechanism.
- [The Loss Surfaces of Multilayer Networks (2015)](../../sources/choromanska2015-loss-surfaces-multilayer-networks.md) — the spin glass as a model of the *training loss*; the bridge from the Hopfield/Boltzmann prehistory to modern training.
- [Entropy-SGD (2017)](../../sources/chaudhari2017-entropy-sgd.md) — free energy over weights as a training objective; the optimizer-side twin of the volume-bounding principle.
- [LeCun & Xing debate (2026)](../../sources/lecun-xing-jepa-glp-debate-2026.md) — LeCun's live account of why he stopped predicting pixels [135:42–137:44]: distributions over video clips cannot be normalised, EBMs are the weaker substitute, and diffusion models carry *"zero guarantee"* against mode collapse.

## Open questions / TBD

- **Training procedures used by Kona** — not surfaced in materials ingested so far. The interview summary says "energy minimization" and "non-autoregressive" but doesn't specify whether training uses score matching, contrastive loss, denoising, or something else.
- **Hinton's products-of-experts (2000) and contrastive divergence** enter the wiki by citation only, through [Bengio et al. 2003](../../sources/bengio2003-neural-probabilistic-language-model.md) §5.1. The tech report is not ingested, and it is the shared ancestor of both the Bengio and LeCun branches above.
- **Empirical reproducibility** of the cost-vs-LLM claims for EBMs — the IBC paper found EBMs hard to scale beyond PushT; Kona's claimed Sudoku-at-$4 hasn't been independently corroborated in this wiki.
