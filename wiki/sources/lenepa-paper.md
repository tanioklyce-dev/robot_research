---
title: "LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning (Chemeris, Jin, Balestriero 2026)"
type: source
url: https://arxiv.org/abs/2607.00958
author: Alexander Chemeris, Ming Jin, Randall Balestriero (Langotime / Griffith / Brown)
published: 2026-07-01
ingested: 2026-07-26
local_path: raw/2607.00958.pdf
venue: arXiv preprint (MILETS 2026 workshop)
license: arXiv
format: pdf
tags: [lenepa, time-series, self-supervised, jepa, sigreg, no-augmentation, next-latent-prediction, frozen-probe, balestriero, lejepa]
---

# LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning

## Summary

**LeNEPA** ("Latent Euclidean Next-Embedding Prediction Architecture") extends the **"Le-" family** of [Randall Balestriero](../entities/randall-balestriero.md) — [LeJEPA](lejepa-paper.md), [LeWorldModel](../entities/leworldmodel.md) — into **time-series representation learning**. It is a **no-augmentation next-latent-token prediction** objective with a causal backbone that replaces the stop-gradient/EMA stabilization of vanilla NEPA-style JEPAs with **[SIGReg](../entities/leworldmodel.md)-based isotropy regularization** (the LeJEPA anti-collapse term), computing the predictive loss in a lightweight projected space that is discarded at evaluation. Its practical thesis: time-series SSL is dangerously sensitive to augmentation/view choices that encode domain-specific invariances, so an augmentation-free recipe that survives being **reused unchanged across signal families** is more useful infrastructure than a heavily-tuned benchmark winner. Not a [LeCun](../entities/yann-lecun.md) paper.

## Key claims

- **The problem — fixed-recipe fragility:** augmentation choice alone can swing time-series accuracy by up to 32 points; JEPA recipes tuned for one domain (e.g. ECG masking) degrade when reused unchanged on another. LeNEPA is framed as a **fixed-recipe stress test**, not a fully-tuned SOTA comparison.
- **Method:** no-augmentation next-embedding prediction + causal backbone + **SIGReg** isotropy regularization (isotropic-Gaussian embedding target, inherited from [LeJEPA](lejepa-paper.md)) instead of stop-gradient/EMA; predictive loss in a discarded projected space.
- **Results (frozen-probe, fixed-horizon):**
  - On **PTB-XL** (ECG) and **Diag** (synthetic diagnostic corpus): an ECG-tuned JEPA is strong in-domain on PTB-XL but weaker when reused unchanged on Diag; **LeNEPA preserves frozen-probe gains on both** with the same config.
  - **Faster early representation acquisition:** reaches 80% of its final AUROC/AUPRC gain in 2–5k updates vs 5–10k for the JEPA readout.
  - **External check (CauKer-pretrained LeNEPA):** 77.65% mean UCR-128 Random-Forest accuracy — within 1.16 pts of Mantis, within 0.24 pts of MOMENT (77.89%), single-seed best-checkpoint.
- **Takeaway:** no-augmentation latent prediction is a viable **low-retuning** time-series SSL recipe. Code: `github.com/langotime/lenepa-milets-2026`.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — co-author; SIGReg is his.
- [LeNEPA](../entities/lenepa.md) — the method.
- [LeWorldModel](../entities/leworldmodel.md) — SIGReg's home model; the "Le-" sibling.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — next-latent prediction; SIGReg anti-collapse.
- [Spectral theory of SSL](../concepts/learning/spectral-theory-of-ssl.md) — the Balestriero SSL-theory line LeNEPA's design descends from.

## Open questions

- Single-seed external UCR-128 result; the paper explicitly disclaims tuned-SOTA comparison. How does LeNEPA fare under full per-dataset tuning against Mantis/MOMENT?
- Does SIGReg's isotropy assumption hold for strongly non-stationary/periodic time series the way it does for image embeddings?
