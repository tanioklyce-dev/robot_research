---
title: Stochastic Backpropagation Paper — Stochastic Backpropagation and Approximate Inference in Deep Generative Models (Rezende, Mohamed, Wierstra, ICML 2014)
type: source
url: https://arxiv.org/abs/1401.4082
author: Danilo J. Rezende, Shakir Mohamed, Daan Wierstra
affiliation: Google DeepMind, London
venue: ICML 2014
published: 2014-01-16 (arxiv v1); v3 2014-05-30
ingested: 2026-07-06
local_path: raw/stochasticBackpropagation_1401.4082v3.pdf
sha256: 3d88eb87269ec43576ce172cdbaccdbdb5573f590d7bf2604b83012383d34bc7
tags: [dlgm, stochastic-backpropagation, variational-inference, recognition-model, amortized-inference, reparameterization, deepmind, rezende, foundational]
---

## Summary

**Stochastic Backpropagation and Approximate Inference in Deep Generative Models** — Rezende, Mohamed, Wierstra (Google DeepMind, ICML 2014). The paper co-credited with [Kingma & Welling](vae-paper.md) for the VAE: developed **simultaneously and independently** (each cites the other as concurrent — §3.2 here, [RMW14] there). Introduces **deep latent Gaussian models (DLGMs)** — directed generative models with Gaussian latent variables at every layer — plus **stochastic backpropagation**: rules for pushing gradients through stochastic variables, derived two ways: (1) **Gaussian gradient identities** (Bonnet 1964 for the mean, Price 1958 for the covariance) and (2) the **location-scale co-ordinate transformation** `z = μ + Rε` (the reparameterization trick). A neural **recognition model** `q(ξ|v)` is trained jointly with the generative model on a variational free-energy objective, giving **amortized inference** (the paper introduces that term into this literature, citing Gershman & Goodman 2014): one bottom-up pass replaces per-datapoint iterative inference. Beats [wake-sleep](wake-sleep-paper.md) and factor analysis on binarized MNIST and demonstrates imputation, visualization, and sampling on MNIST/NORB/CIFAR-10/Frey/SVHN.

## Key claims

- **DLGM construction** (§2, eqs. 1–6): layers of latents `h_l = T_l(h_{l+1}) + G_l ξ_l` with MLPs `T_l` and mutually independent Gaussian `ξ_l`; generalizes factor analysis (linear `T`), non-linear factor analysis, and non-linear Gaussian belief networks (Frey & Hinton 1999) as special cases.
- **Gaussian backpropagation (GBP)** (§3.1, eqs. 7–9): `∇_μ E[f] = E[∇_ξ f]` (Bonnet) and `∇_C E[f] = ½E[∇²f]` (Price) give unbiased gradient estimates; the general rule needs the Hessian (`O(K³)`), so the practical estimator uses the transformation form.
- **Reparameterization, independently derived** (§3.2, eq. 10): any distribution expressible as a smooth invertible transform of a base distribution admits stochastic backprop; Gaussian case `y = μ + Rε`, `C = RRᵀ` — the same trick as [Kingma & Welling's](vae-paper.md) `g_φ(ε, x)`, framed via location-scale families and co-ordinate transformations.
- **Variance argument vs REINFORCE** (§6, appendix D): score-function/REINFORCE estimator variance scales `O(K)` in the latent dimension; GBP variance is bounded by a constant `O(1)` — the crisp quantitative version of Kingma & Welling's "exhibits very high variance" remark.
- **Free-energy objective** (§4.1, eqs. 11–13): `F(V) = D_KL[q(ξ)‖p(ξ)] − E_q[log p(V|ξ)]` with analytic Gaussian KL; recognition model is a DAG of Gaussians whose means/covariances are deep networks. Explicit **amortised inference** framing: shared statistical strength across datapoints, faster convergence, one-pass test-time inference.
- **Rank-1-corrected covariance** (§4.3, eqs. 19–21): parameterize the posterior precision as `C⁻¹ = D + uuᵀ` (diagonal + rank-1) — trace, log-det, sampling, and gradients all in `O(K)` per layer, capturing one principal direction of posterior correlation that a diagonal posterior misses. A structured-posterior refinement the Kingma & Welling paper doesn't have.
- **Results** (§5, table 1): binarized MNIST test negative log-likelihood **86.60 nats (rank-one) / 87.30 (diagonal)** vs wake-sleep 91.3 and factor analysis 106.0; competitive with NADE/EoNADE/DBN-class models. Posterior visualizations show the recognition model concentrating on true-posterior mass (fig. 2). Fantasy samples on MNIST, NORB, CIFAR-10 patches, Frey faces; **missing-data imputation** on SVHN/MNIST/Frey under MAR (60–80% missing) and NMAR (occluded square) via a Markov-chain procedure (appendix F).
- **Denoising autoencoders reinterpreted** (§6): the DAE objective corresponds to variational inference with a stochastic encoder — but here the "corruption" and regularizer are *derived* from the variational principle and give a strict bound on the marginal likelihood.
- **Wake-sleep critique** (§6): "it fails to optimise a single consistent objective function and there is thus no guarantee that optimising it leads to a decrease in the free energy" — the same diagnosis as [Kingma & Welling §4](vae-paper.md).
- Optimization used **RMSprop** (Hinton's Coursera heuristic) — vs Adagrad in Kingma & Welling.

## VAE paper vs this paper — the two halves of one idea

> [!note] Same discovery, different emphases
> Kingma & Welling ([VAE Paper](vae-paper.md)) foreground the **estimator** (SGVB, two variants) and the auto-encoder reading; Rezende et al. foreground the **model class** (deep, multi-layer latent hierarchies), the **variance theory** (O(1) vs O(K)), and **structured posteriors** (rank-1 covariance). Both introduce a jointly-trained recognition model, both integrate the Gaussian KL analytically, both benchmark against [wake-sleep](wake-sleep-paper.md) on MNIST/Frey. The literature credits the VAE to both papers jointly.

## Entities mentioned

- [Geoffrey Hinton](../entities/geoffrey-hinton.md) — wake-sleep baseline; NLGBN (Frey & Hinton 1999) special case; RMSprop optimizer.

## Concepts touched

- [Variational autoencoder](../concepts/learning/variational-autoencoder.md) — co-defining paper.
- [Learned latent space](../concepts/world-models/latent-space.md) — 2D MNIST embeddings for visualization (fig. 3b); hierarchical Gaussian latents.

## Open questions / TBD

- **Danilo Rezende / Shakir Mohamed** — both went on to major DeepMind generative-modeling lines (normalizing flows, Rezende & Mohamed 2015); Shakir Mohamed is also an author of [β-VAE](beta-vae-paper.md). Entity pages on demand.
- **Normalizing flows** (Rezende & Mohamed, ICML 2015) — the direct successor for richer posteriors than rank-1 Gaussian; not in the wiki.
