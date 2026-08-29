---
title: VAE Paper — Auto-Encoding Variational Bayes (Kingma & Welling, ICLR 2014)
type: source
url: https://arxiv.org/abs/1312.6114
author: Diederik P. Kingma, Max Welling
affiliation: Machine Learning Group, Universiteit van Amsterdam
published: 2013-12-20 (arxiv v1); ICLR 2014; v11 2022-12-10
ingested: 2026-07-06
local_path: raw/VariationalAutoEncoder_1312.6114v11.pdf
sha256: bdcb63b79ed88f64f8ee2d43a721930d01dde5441a4dba20ecaa2342b34e017c
tags: [vae, variational-inference, generative-model, reparameterization-trick, elbo, sgvb, aevb, kingma, welling, foundational]
---

## Summary

**Auto-Encoding Variational Bayes** — Kingma & Welling (Universiteit van Amsterdam, ICLR 2014; the paper that introduced the **variational autoencoder**). Asks: how do we do efficient inference and learning in directed probabilistic models with continuous latent variables whose posterior is intractable, on large datasets? Two contributions: (1) the **SGVB (Stochastic Gradient Variational Bayes) estimator** — a reparameterization of the variational lower bound (ELBO) that yields a low-variance, differentiable Monte Carlo estimator optimizable with plain SGD; (2) the **AEVB (Auto-Encoding VB) algorithm** — for i.i.d. datasets with per-datapoint latents, fit a **recognition model** `q_φ(z|x)` (a *probabilistic encoder*) jointly with the generative model `p_θ(x|z)` (a *probabilistic decoder*), amortizing posterior inference into a single forward pass instead of per-datapoint MCMC. When the recognition model is a neural network, the result is the **variational auto-encoder**. Foundational for essentially all subsequent deep latent-variable modeling — the ELBO machinery reused by [DDPM](../entities/ddpm.md), the CVAE inside [ACT](../entities/act.md), the VQ-VAE tokenizers in [VQ-BeT](../entities/vq-bet.md), and the latent spaces diffusion models like Stable Diffusion operate in.

## Key claims

- **ELBO decomposition** (§2.2, eqs. 1–3): `log p_θ(x) = D_KL(q_φ(z|x) ‖ p_θ(z|x)) + L(θ,φ;x)`, so the lower bound `L` splits into `−D_KL(q_φ(z|x) ‖ p_θ(z)) + E_q[log p_θ(x|z)]` — a **prior-regularization term** plus an **expected reconstruction term**. This is the auto-encoder reading of variational inference.
- **The naïve estimator is unusable** (§2.2): the standard score-function (REINFORCE-style) Monte Carlo gradient `∇_φ E_q[f(z)]` "exhibits very high variance" — the reparameterization trick is the fix.
- **Reparameterization trick** (§2.3–2.4, eq. 4): rewrite `z ~ q_φ(z|x)` as a deterministic differentiable transform `z = g_φ(ε, x)` of parameter-free noise `ε ~ p(ε)` (Gaussian case: `z = μ + σε`), so gradients flow through the sampling step. Three recipes: tractable inverse CDF; location–scale families; composition of transforms.
- **Two SGVB estimators** (§2.3): generic `L̃^A` (eq. 6), and `L̃^B` (eq. 7) which integrates the KL term **analytically** (appendix B gives the closed-form Gaussian–Gaussian KL) so only the reconstruction term is sampled — typically lower variance. With minibatch size `M = 100`, **one sample per datapoint (`L = 1`) suffices** (eq. 8).
- **The VAE instantiation** (§3, eq. 10): prior `p(z) = N(0, I)`; encoder MLP outputs `(μ, σ)` of a diagonal-Gaussian posterior; decoder MLP is Bernoulli (binary data) or Gaussian (continuous data). Resulting per-datapoint objective: `½ Σ_j (1 + log σ_j² − μ_j² − σ_j²) + (1/L) Σ_l log p_θ(x|z^(l))`.
- **Experiments** (§5, figs. 2–3): MNIST + Frey Face vs the **wake-sleep algorithm** (Hinton et al. 1995 — the only prior online method for this model class) — AEVB "converged considerably faster and reached a better solution in all experiments"; also beats Monte Carlo EM (HMC-based) on estimated marginal likelihood, and unlike MCEM it scales to the full dataset. **More latent dimensions did not cause overfitting**, credited to the KL term's regularizing effect (tested N_z up to 200).
- **Built-in regularization**: unlike denoising/contractive/sparse autoencoders, the SGVB objective's regularizer is **dictated by the variational bound** — no nuisance regularization hyperparameter (§4).
- **Appendix F**: full VB variant that also does variational inference over the *global parameters* θ (reparameterized hyperprior) — stated but not experimentally evaluated.

## Positioning vs prior work (§4)

- **Wake-sleep** (Hinton, Dayan, Frey, Neal 1995) — also uses a recognition model, but optimizes two objectives that don't correspond to a bound on the marginal likelihood; same per-datapoint cost as AEVB; does handle discrete latents (AEVB as presented doesn't).
- **Concurrent work**: Rezende, Mohamed & Wierstra 2014 (DeepMind, "stochastic backpropagation" / deep latent Gaussian models) independently arrived at the same reparameterization connection — the two papers are jointly credited for the VAE.
- **PCA link**: linear-Gaussian special case recovers PCA as ML solution (Roweis 1998).
- **Predictive sparse decomposition** (Kavukcuoglu, Ranzato, [LeCun](../entities/yann-lecun.md) 2008) — encoder–decoder architecture the authors say they "drew some inspiration" from.

## Why it matters in this wiki

- **The ELBO substrate of diffusion** — [DDPM](../entities/ddpm.md)'s training objective is a weighted variational bound; [curriculum Module 5](../syntheses/curriculum/curriculum-05-generative-models.md) derives DDPM starting from exactly this paper's ELBO, and its anchor exercise (Module 12) is the `L_simple` derivation from the variational bound.
- **CVAE inside [ACT](../entities/act.md)** — ACT trains its action-chunking policy as a conditional VAE (the "VAE-style action distribution model" flagged on the ACT entity page).
- **VQ-VAE lineage** — [VQ-BeT](../entities/vq-bet.md)'s residual VQ-VAE action tokenizer and the video tokenizers in generative world models descend from the VAE via discrete-latent variants.
- **Latent-space diffusion** — Stable Diffusion is "VAE encoder + DDPM in latent space" ([Module 5 family map](../syntheses/curriculum/curriculum-05-generative-models.md)); a VAE defines the [learned latent space](../concepts/world-models/latent-space.md) the diffusion runs in.
- **The reparameterization trick escaped the VAE** — it's now generic ML infrastructure (covered as such in [Blondel & Roulet's differentiable-programming textbook](blondel-roulet-differentiable-programming.md), ch. 12, alongside REINFORCE and Gumbel tricks).

## Entities mentioned

- [DDPM](../entities/ddpm.md) — downstream; reuses the variational-bound machinery.
- [ACT](../entities/act.md) — downstream; conditional-VAE policy.
- [VQ-BeT](../entities/vq-bet.md) — downstream; residual VQ-VAE tokenizer.
- [Yann LeCun](../entities/yann-lecun.md) — PSD (Kavukcuoglu, Ranzato, LeCun 2008) cited as encoder–decoder inspiration.
- [Geoffrey Hinton](../entities/geoffrey-hinton.md) — wake-sleep (the positioning baseline) and the DBM recognition-model precursor.

## Concepts touched

- [Variational autoencoder](../concepts/learning/variational-autoencoder.md) — the concept this paper defines.
- [Learned latent space](../concepts/world-models/latent-space.md) — the VAE is the canonical *probabilistic* learned latent space (explicit prior + sampling story).
- [Energy-based models](../concepts/learning/energy-based-models.md) — sibling family in the generative-model design space (explicit amortized density vs unnormalized energy).

## Open questions / TBD

- ~~**Rezende et al. 2014** (arxiv 1401.4082, stochastic backpropagation / DLGM) — the co-credited concurrent paper; not a source page yet.~~ **Filed 2026-07-06**: [Stochastic Backpropagation Paper](stochastic-backpropagation-paper.md).
- ~~**Wake-sleep** (Hinton et al. 1995) — historical predecessor; not a source page.~~ **Filed 2026-07-06**: [Wake-Sleep Paper](wake-sleep-paper.md).
- ~~**β-VAE / disentanglement line** (Higgins et al. 2017) — the KL-weighting knob downstream work turns; not in the wiki.~~ **Filed 2026-07-06**: [β-VAE Paper](beta-vae-paper.md).
- **Diederik Kingma** — also the Adam optimizer (Kingma & Ba 2014); entity page on demand if more Kingma-line work surfaces.
- The v11 PDF (2022) is a lightly-corrected arxiv revision of the 2013 paper, not a content update — treated here as the 2013/ICLR-2014 work.
