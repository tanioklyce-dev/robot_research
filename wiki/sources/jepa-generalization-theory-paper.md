---
title: "A Generalization Theory for JEPA-Based World Models (Cui, Zhang, Wen, Wang 2026)"
type: source
url: https://arxiv.org/abs/2606.27014
author: Jingyi Cui, Qi Zhang, Hongwei Wen, Yisen Wang (Peking University / Univ. Sydney)
published: 2026-06-25
ingested: 2026-07-26
local_path: raw/2606.27014.pdf
venue: arXiv preprint (cs.LG)
license: arXiv
format: pdf
tags: [jepa, world-model, generalization-theory, spectral-graph, co-occurrence-matrix, planning-regret, finite-sample-bound, latent-prediction, theory]
---

# A Generalization Theory for JEPA-Based World Models

## Summary

The **first generalization theory for [JEPA](../concepts/world-models/jepa.md)-based world models** — a Peking University theory paper (not [LeCun](../entities/yann-lecun.md)/coauthor) that answers "does a JEPA world model provably generalize to downstream planning?" It formulates JEPA pretraining as a **conditional spectral graph learning** problem, proves the JEPA objective is equivalent to a **low-rank factorization of an action-conditioned co-occurrence matrix**, then connects JEPA pretraining error to **downstream planning regret** to derive a **finite-sample generalization bound**. The bound exposes an inherent **approximation-vs-sample-error trade-off in the latent dimension**, giving the first theoretical account of when latent-predictive world models beat input-level (pixel-generative) ones. It slots directly beside the wiki's existing JEPA-theory results — [Balestriero's density-estimation result](../concepts/learning/spectral-theory-of-ssl.md) and the [Klindt/LeCun/Balestriero identifiability theorems](when-does-lejepa-learn-a-world-model-paper.md) — and shares their **spectral-graph** mathematical language.

## Key claims

- **Conditioned co-occurrence matrix:** the authors define a matrix of the co-occurrence probability of current and next state **conditioned on the action**, and show JEPA pretraining risk = matrix factorization of it (a *conditional* spectral graph formulation — the action-conditioned generalization of the [spectral view of SSL](../concepts/learning/spectral-theory-of-ssl.md)).
- **Pretraining error → planning regret:** they bound downstream action-planning regret (evaluated at the input level) in terms of the latent-space JEPA pretraining risk, yielding a finite-sample generalization bound for JEPA world models — the missing link, since planning happens in latent space but is judged on input-level tasks.
- **Latent-dimension trade-off:** the bound reveals an approximation-error (falls with larger latent dim) vs sample-error (rises with larger latent dim) tension, theoretically characterizing the advantage of **latent-** over **input-level** predictive models (and its limits).
- **Positioning vs prior theory:** prior JEPA theory studied the *static representation* setting (Littwin et al. 2024 on feature preference; Balestriero et al. 2025 on anti-collapse = implicit density estimation) or was parametric (Klindt et al. 2026 identifiability). This is the first to treat JEPA *as a world model* with provable downstream-planning guarantees.

## Entities mentioned

- [V-JEPA 2](../entities/v-jepa-2.md), [DINO-WM](../entities/dino-wm.md), [LeWorldModel](../entities/leworldmodel.md), [VL-JEPA](../entities/vl-jepa.md) — the empirical JEPA world models the theory covers.
- Authors: Jingyi Cui, Qi Zhang, Hongwei Wen, Yisen Wang (Peking Univ. State Key Lab of General AI; Univ. Sydney).

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the object of the theory.
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — the spectral-graph framing it extends to the action-conditioned world-model setting.
- [Identifiability](../concepts/world-models/identifiability.md) — the sibling formal result; this paper adds *generalization* to identifiability's *recoverability*.

## Open questions

- The bound is asymptotic/finite-sample theory — no empirical validation of the predicted latent-dimension sweet spot on a real JEPA world model.
- Does the action-conditioned co-occurrence formulation connect to the anti-collapse mechanisms taxonomy (SIGReg / inverse-dynamics), or is it agnostic to how collapse is prevented?
