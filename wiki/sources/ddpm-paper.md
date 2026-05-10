---
title: DDPM Paper — Denoising Diffusion Probabilistic Models (Ho et al., NeurIPS 2020)
type: source
url: https://arxiv.org/abs/2006.11239
author: Jonathan Ho, Ajay Jain, Pieter Abbeel
affiliation: UC Berkeley (Abbeel lab)
published: 2020-06-19 (arxiv v1); 2020-12-16 (v2); NeurIPS 2020
ingested: 2026-05-09
created: 2026-05-09
updated: 2026-05-09
tags: [ddpm, diffusion-model, generative-model, score-matching, langevin-dynamics, ho-2020, abbeel-lab, foundational]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (paper PDF not in `raw/`). Substantive technical claims are cross-cited from [Diffusion Policy Paper](diffusion-policy-paper.md), which builds directly on DDPM mechanics. To deepen this page, drop the DDPM PDF in `raw/` and re-ingest.

## Summary

**Denoising Diffusion Probabilistic Models** (DDPM) — Ho, Jain, Abbeel (UC Berkeley, NeurIPS 2020). The foundational paper that established **diffusion models** as a competitive generative-model class. Trains a network to predict the noise added at each step of a forward Markov noising process; samples by iteratively denoising from Gaussian noise. The crucial theoretical contribution is connecting **diffusion probabilistic models with denoising score matching and Langevin dynamics**, which yields a simple weighted variational bound training objective. Achieved state-of-the-art image generation on CIFAR-10 (FID 3.17, IS 9.46) and competitive results on 256×256 LSUN. Substrate for almost all subsequent diffusion-model work, including image generation (Stable Diffusion, DALL-E), video generation, **and robot action diffusion** ([Diffusion Policy](../entities/diffusion-policy.md)).

## Abstract (verbatim opener)

> "We present high quality image synthesis results using diffusion probabilistic models, a class of latent variable models inspired by considerations from nonequilibrium thermodynamics."

## Key claims

- **Theoretical link**: novel connection between diffusion probabilistic models and **denoising score matching** with **Langevin dynamics** sampling. This unifies two previously separate threads in generative modeling.
- **Simple training objective**: a **weighted variational bound** — predict the noise added at each forward step; minimize MSE against ground-truth noise. No adversarial training needed.
- **Progressive lossy decompression**: the sampling chain can be interpreted as a generalization of autoregressive decoding.
- **Headline image-generation numbers**: CIFAR-10 IS 9.46, FID 3.17 (state-of-the-art at publication); 256×256 LSUN comparable to ProgressiveGAN.

## Mechanics (cross-cited from Diffusion Policy paper)

From [Diffusion Policy Paper](diffusion-policy-paper.md) §II (which gives a compact DDPM tutorial):

- **Forward process**: gradually add Gaussian noise to data over `K` steps until pure noise. Defined by a fixed noise schedule `β_k`.
- **Reverse process**: a learned neural network `ε_θ(x_k, k)` predicts the noise that was added; the reverse step subtracts that prediction (with appropriate scaling) and adds fresh small Gaussian noise.
- **Training loss**: `L = MSE(ε_k, ε_θ(x_0 + ε_k, k))` — predict the noise from a noisy sample at step `k`.
- **Sampling**: start from `x_K ~ N(0, I)`, iterate `K` denoising steps to recover `x_0`.

### How [Diffusion Policy](../entities/diffusion-policy.md) adapts DDPM

Two modifications:
1. Output `x` is a **robot action sequence**, not an image.
2. The denoising process is **conditioned on observations** `O_t`: model `p(A_t | O_t)`, not the joint `p(A_t, O_t)`.

The training and sampling structure are otherwise identical to DDPM, including the square-cosine noise schedule (from iDDPM, Nichol & Dhariwal 2021) which Diffusion Policy adopts.

## Downstream lineage

DDPM's most relevant descendants for this wiki:
- **DDIM** (Song, Meng, Ermon, ICLR 2021, arxiv 2010.02502) — non-Markovian sampling that decouples training-step count from inference-step count. Diffusion Policy uses DDIM at inference (10 steps for 100-step-trained model) for real-time control.
- **iDDPM / Improved DDPM** (Nichol & Dhariwal, ICML 2021) — better noise schedule (square cosine), used by Diffusion Policy.
- **Score-based generative modeling** (Song & Ermon, NeurIPS 2019; Song et al., ICLR 2021) — alternative formulation of the same underlying mathematics.
- **Latent-space diffusion** (Stable Diffusion, Rombach et al., CVPR 2022) — diffusion in a learned latent space rather than pixel space.
- **Diffusion-as-policy in robotics** — [Diffusion Policy](../entities/diffusion-policy.md) (Chi et al., RSS 2023); Diffuser/trajectory-diffusion (Janner et al., ICML 2022); IDQL (Hansen-Estruch et al., 2023).

## Why it matters in this wiki

- **Substrate of [Diffusion Policy](../entities/diffusion-policy.md)** — Diffusion Policy is *DDPM applied to action sequences with observation conditioning*. Without DDPM, Diffusion Policy is not a research direction.
- **Substrate of generative-video world models** — [NVIDIA Cosmos](../entities/nvidia-cosmos.md), [Genie Envisioner](../entities/genie-envisioner.md), Sora, etc. all build on diffusion-model foundations established here.
- **Reference point for the JEPA argument** — JEPA's whole pitch ("don't predict pixels; predict in latent space") is a counter-position to the diffusion-pixel-prediction approach DDPM established. So DDPM is implicitly the *thing JEPA is positioned against* in [V-JEPA 2](../entities/v-jepa-2.md), [LeWM](../entities/leworldmodel.md), etc.

## Entities mentioned

- [DDPM](../entities/ddpm.md) — the method/model class.
- [Diffusion Policy](../entities/diffusion-policy.md) — direct robotics adaptation.

## Concepts touched

- [World model](../concepts/world-model.md) — generative-video world models trace to DDPM.
- [Imitation learning](../concepts/imitation-learning.md) — Diffusion Policy's BC formulation builds on DDPM.

## Open questions / TBD

- **Full paper not yet ingested** — abstract-level only. The U-Net architecture details, exact loss derivation, and ablations would deepen this page.
- **DDIM not yet a source page** — Song, Meng, Ermon (ICLR 2021, arxiv 2010.02502); Diffusion Policy uses it at inference.
- **iDDPM not yet a source page** — Nichol & Dhariwal (ICML 2021); Diffusion Policy uses its square-cosine schedule.
- **Score-based formulation** (Song & Ermon) — alternative formulation; could become its own source.
- **Author entity pages** — Pieter Abbeel (Berkeley) is a major figure; could become an entity if more Abbeel-line work surfaces. Jonathan Ho is now at Google. Ajay Jain has moved on as well.
