---
title: Variational autoencoder (VAE)
type: concept
created: 2026-07-06
updated: 2026-07-09
sources: 10
tags: [vae, generative-model, variational-inference, elbo, reparameterization-trick, latent-variable, kingma, foundational]
---

A **variational autoencoder (VAE)** is an autoencoder with a *probabilistic* latent space: the encoder outputs a distribution `q_φ(z|x)` (not a point), a prior `p(z) = N(0, I)` is imposed on the latent, and the training loss is the **negative ELBO** — an expected reconstruction term plus a KL term pulling the posterior toward the prior ([VAE Paper](../../sources/vae-paper.md)). Because the prior is explicit, a trained VAE is a true generative model: sample `z ~ p(z)`, decode. The technical move that makes it trainable is the **reparameterization trick** — write `z = μ_φ(x) + σ_φ(x) ⊙ ε` with `ε ~ N(0, I)`, so the sampling step is differentiable and plain SGD works where score-function estimators are too high-variance ([VAE Paper](../../sources/vae-paper.md)).

Introduced by Kingma & Welling 2013 (concurrently with [Rezende, Mohamed & Wierstra 2014](../../sources/stochastic-backpropagation-paper.md) at DeepMind), it was the first practical recipe for **amortized variational inference** with neural networks: one encoder forward pass replaces per-datapoint iterative inference (MCMC, mean-field updates). The recognition-model idea itself is older — the [wake-sleep algorithm](../../sources/wake-sleep-paper.md) (Hinton et al. 1995) trained a bottom-up recognition network and top-down generative network jointly, but with two inconsistent objectives; the VAE's contribution was a single correct bound both networks descend together.

## Key references

- **[VAE Paper — Auto-Encoding Variational Bayes](../../sources/vae-paper.md)** (Kingma & Welling, ICLR 2014) — the defining paper: SGVB estimator, AEVB algorithm, reparameterization trick, closed-form Gaussian KL.
- **[Stochastic Backpropagation Paper](../../sources/stochastic-backpropagation-paper.md)** (Rezende, Mohamed, Wierstra, ICML 2014) — the co-credited concurrent paper: DLGMs, Gaussian gradient identities, O(1)-vs-O(K) variance argument against REINFORCE, rank-1 structured posteriors, amortized-inference framing.
- **[Wake-Sleep Paper](../../sources/wake-sleep-paper.md)** (Hinton, Dayan, Frey, Neal, *Science* 1995) — the predecessor: recognition + generative networks, MDL/free-energy objective, Helmholtz machine; its two flaws (fantasy-trained recognition weights, wrong-direction KL) are what the VAE fixed.
- **[β-VAE Paper](../../sources/beta-vae-paper.md)** (Higgins et al., ICLR 2017) — weight the KL term by β > 1 to trade reconstruction fidelity for **disentangled** latents; introduced the standard disentanglement metric; the KL-weighting knob used in downstream CVAE/VAE components.
- **[DDPM Paper](../../sources/ddpm-paper.md)** (Ho et al., NeurIPS 2020) — diffusion models are trained on a weighted variational bound; [curriculum Module 5](../../syntheses/curriculum/curriculum-05-generative-models.md) derives DDPM *from* the VAE (a diffusion model can be read as a hierarchical VAE with a fixed encoder).
- **[The Elements of Differentiable Programming](../../sources/blondel-roulet-differentiable-programming.md)** (Blondel & Roulet, ch. 12) — the reparameterization trick as generic ML infrastructure, alongside REINFORCE and Gumbel tricks.
- **[Robot Learning: A Tutorial](../../sources/lerobot-robot-learning-tutorial.md)** (LeRobot) — introduces VAEs (with diffusion and flow matching) as the generative preliminaries to imitation learning.

## Where VAEs show up in robot learning

VAEs are rarely the headline model anymore, but they persist as **components**:

- **Conditional VAE as policy** — [ACT](../../entities/act.md) (Zhao et al. 2023) trains its action-chunking transformer as a CVAE: a latent "style" variable absorbs the multimodality of human demonstrations ([LeRobot ICLR 2026 paper](../../sources/lerobot-iclr-2026-paper.md) cites Kingma & Welling as the substrate).
- **Discrete-latent variants (VQ-VAE)** — [VQ-BeT](../../entities/vq-bet.md)'s residual VQ-VAE action tokenizer ([VQ-BeT Paper](../../sources/vq-bet-paper.md)); video tokenizers in generative world models.
- **Latent-diffusion stacks** — Stable Diffusion is "VAE encoder + DDPM in latent space" ([Module 5](../../syntheses/curriculum/curriculum-05-generative-models.md) family map); the VAE supplies the compressed [latent space](../world-models/latent-space.md) the diffusion runs in.

## Related concepts

- [Learned latent space](../world-models/latent-space.md) — the VAE is the canonical *probabilistic* learned latent space: explicit prior, KL-shaped geometry, sampling story.
- [Energy-based models](energy-based-models.md) — sibling family: VAE keeps an explicit (amortized, variational) density; EBMs go unnormalized.
- [Flow matching](flow-matching.md) — modern continuous-action heads ([π0](../../entities/pi-zero.md)-line) that displaced VAE/diffusion heads in 2025+ VLAs.
- [Imitation learning](imitation-learning.md) — CVAE (ACT) is one of the standard answers to demonstration multimodality, alongside diffusion and tokenization.

## Current state

As a standalone image generator the VAE is superseded (blurry Gaussian-decoder samples — the weakness that motivated diffusion; see [Module 5](../../syntheses/curriculum/curriculum-05-generative-models.md)). As *infrastructure* it is everywhere: the ELBO is the training objective of diffusion, the reparameterization trick is the default low-variance gradient estimator for stochastic layers, and VAE/VQ-VAE compressors sit inside latent-diffusion image models, video world models, and action tokenizers. In this wiki's robot-learning lineage its two live descendants are the **CVAE in [ACT](../../entities/act.md)** and the **residual VQ-VAE in [VQ-BeT](../../entities/vq-bet.md)**.

## Mentioned in

- [VAE Paper — Auto-Encoding Variational Bayes](../../sources/vae-paper.md) — primary source.
- [Stochastic Backpropagation Paper](../../sources/stochastic-backpropagation-paper.md) — co-defining paper.
- [Wake-Sleep Paper](../../sources/wake-sleep-paper.md) — predecessor.
- [β-VAE Paper](../../sources/beta-vae-paper.md) — disentanglement extension.
- [DDPM Paper](../../sources/ddpm-paper.md) — variational-bound training objective.
- [VQ-BeT Paper](../../sources/vq-bet-paper.md) — residual VQ-VAE tokenizer.
- [Robot Learning: A Tutorial (LeRobot)](../../sources/lerobot-robot-learning-tutorial.md) — generative-models chapter.
- [LeRobot ICLR 2026 Paper](../../sources/lerobot-iclr-2026-paper.md) — cites Kingma & Welling 2022 (VAE) in its reference set.
- [The Elements of Differentiable Programming](../../sources/blondel-roulet-differentiable-programming.md) — reparameterization trick (ch. 12).
- [World Models (Ha & Schmidhuber, 2018)](../../sources/world-models-paper.md) — the V model: a canonical VAE application (frame compression for a world model).
