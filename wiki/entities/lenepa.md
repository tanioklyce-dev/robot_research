---
title: LeNEPA
type: entity
subtype: method
created: 2026-07-26
updated: 2026-07-26
sources: 1
tags: [lenepa, time-series, self-supervised, jepa, sigreg, no-augmentation, next-latent-prediction, balestriero, lejepa]
---

# LeNEPA

**LeNEPA** ("Latent Euclidean Next-Embedding Prediction Architecture") ([Chemeris, Jin, Balestriero 2026](../sources/lenepa-paper.md), arXiv 2607.00958) is a **no-augmentation, next-latent-prediction SSL recipe for time series** — the extension of [Randall Balestriero](randall-balestriero.md)'s **"Le-" family** ([LeJEPA](../sources/lejepa-paper.md), [LeWorldModel](leworldmodel.md)) beyond images/video/pixels into sequential signals.

## Why it matters in this wiki

LeNEPA shows the **SIGReg anti-collapse idea generalizing across modalities**: the same isotropic-Gaussian regularizer that replaces stop-gradient/EMA in [LeJEPA](../sources/lejepa-paper.md) is here dropped into a causal time-series encoder, replacing the augmentation-and-EMA machinery that makes time-series SSL notoriously recipe-fragile. It is the wiki's first time-series entry in the otherwise vision/robotics JEPA thread, and evidence that the [spectral/SIGReg SSL theory](../concepts/learning/spectral-theory-of-ssl.md) is a portable recipe, not an image-specific trick. Not a [LeCun](yann-lecun.md) paper.

## Method

No-augmentation next-embedding prediction + causal backbone + **SIGReg** isotropy regularization (isotropic-Gaussian embedding target) instead of stop-gradient/EMA; predictive loss computed in a lightweight projected space discarded at evaluation. Framed as a **fixed-recipe stress test** — how a recipe behaves when reused unchanged across signal families — rather than a tuned-SOTA comparison.

## Reported numbers

- Frozen-probe on **PTB-XL** (ECG) + **Diag**: preserves gains on both under a fixed config, where an ECG-tuned JEPA degrades off-domain; reaches 80% of its final AUROC/AUPRC gain in 2–5k updates (vs 5–10k for the JEPA readout).
- **UCR-128** (CauKer-pretrained, single-seed best-checkpoint): 77.65% RF accuracy — within 0.24 pts of MOMENT (77.89%), 1.16 pts of Mantis.

## Related

- [Randall Balestriero](randall-balestriero.md) — co-author; SIGReg is his.
- [LeWorldModel](leworldmodel.md) / [LeJEPA](../sources/lejepa-paper.md) — the "Le-" siblings LeNEPA descends from.
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — the theory underlying the SIGReg design.
- [JEPA](../concepts/world-models/jepa.md) — the next-latent-prediction family.

## Mentioned in

- [LeNEPA paper (Chemeris, Jin, Balestriero 2026)](../sources/lenepa-paper.md) — the primary source.
