---
title: LeJEPA Paper — Provable and Scalable Self-Supervised Learning Without the Heuristics (Balestriero & LeCun, 2025)
type: source
url: https://arxiv.org/abs/2511.08544
author: Randall Balestriero, Yann LeCun
affiliation: Brown University (Balestriero); NYU / Meta FAIR (LeCun)
published: 2025-11-11 (v1); 2025-11-14 (v3)
ingested: 2026-05-10
created: 2026-05-10
updated: 2026-05-10
tags: [lejepa, sigreg, jepa, ssl, anti-collapse, isotropic-gaussian, balestriero, lecun, foundational, sketched-regularization]
---

> [!note] Ingest depth
> This source page is **based on the arxiv abstract page only** (PDF not in `raw/`). The technical formulations of SIGReg + the Cramér–Wold + Epps–Pulley details are derived in the paper body — [Module 12](../syntheses/curriculum-12-lewm-deep-dive.md)'s SIGReg derivation re-derives them from the LeWM paper's exposition. Drop the PDF in `raw/` for a deeper ingest.

## Summary

**LeJEPA** — Balestriero & LeCun, Brown + NYU/FAIR (November 2025). The **foundational paper for SIGReg** ([Sketched Isotropic Gaussian Regularizer](../glossary.md#sigreg)). LeJEPA is positioned as both a *theory* of JEPAs and an *instantiation* of that theory in a "lean, scalable, and theoretically grounded training objective."

The headline contribution: **identify isotropic Gaussian as the optimal distribution for JEPA embeddings** (the distribution that minimizes downstream prediction risk under the JEPA framework), then propose **SIGReg** as the regularizer that enforces this distributional shape. The combination — JEPA's predictive loss + SIGReg — is **LeJEPA**.

**Headline empirical result:** ImageNet-1k pretraining with linear evaluation on a frozen ViT-H/14 backbone reaches **79% top-1**, validated across "10+ datasets, 60+ architectures." Demonstrates the LeJEPA recipe is competitive with mainstream SSL methods while removing the heuristics those methods need (stop-gradient, teacher-student, EMA target encoders).

LeJEPA is the **methodological precursor to [LeWM](../entities/leworldmodel.md)** ([Maes et al. 2026](leworldmodel-paper.md)). LeWM is essentially "LeJEPA applied to the offline-RL / world-model setting": same SIGReg, same single hyperparameter, but conditioned on actions and used for MPC against a learned predictor.

## Abstract (verbatim opener)

> "Learning manipulable representations of the world and its dynamics is central to AI. Joint-Embedding Predictive Architectures (JEPAs) offer a promising blueprint, but lack of practical guidance and theory has led to ad-hoc R&D. We present a comprehensive theory of JEPAs and instantiate it in LeJEPA, a lean, scalable, and theoretically grounded training objective."

## Key claims

### Theoretical contribution

- **Isotropic Gaussian is optimal for JEPA embeddings.** The paper proves that an isotropic Gaussian latent distribution minimizes downstream prediction risk under the JEPA framework. This is the formal justification for the "Gaussian-shaped latent" target SIGReg enforces.
- **A theory of JEPAs.** The paper claims to provide "a comprehensive theory of JEPAs" — formal grounding for the architectural choices that prior end-to-end JEPA work made empirically.

### Method (LeJEPA = JEPA loss + SIGReg)

- **Predictive objective** (the JEPA loss): same as standard JEPA — predict next-embedding from current.
- **SIGReg** ([Sketched Isotropic Gaussian Regularizer](../glossary.md#sigreg)): random unit-norm projections + univariate normality test (Epps–Pulley) + average across projections, justified by Cramér–Wold. Backprop through the test statistic.
- **Total loss:** `L = L_JEPA + λ · SIGReg`. Single trade-off hyperparameter `λ`.
- **Linear time and memory complexity** in batch size and feature dimension — SIGReg is cheap.
- **Heuristics-free.** No stop-gradient. No teacher-student / EMA target encoder. No image augmentations specific to the SSL setup. The whole training procedure is "just gradient descent on this two-term loss."

### Empirical claims

- **Stability across hyper-parameters, architectures, and scale.** Validated on 10+ datasets and 60+ architectures.
- **ViT-H/14 ImageNet-1k linear-eval: 79%.** Frozen backbone after LeJEPA pretraining; competitive with mainstream SSL methods.
- The validation breadth ("10+ datasets, 60+ architectures") is unusually wide for a methodology paper — suggests the recipe is *robust* across regimes rather than hand-tuned to a single benchmark.

## How LeJEPA relates to LeWM

[LeWM](leworldmodel-paper.md) (Maes et al. 2026) takes the LeJEPA recipe and applies it to action-conditioned world modeling for offline RL:

- **Same loss structure.** `L = L_pred + λ · SIGReg(Z)` — directly inherited from LeJEPA.
- **Same Sketched Isotropic Gaussian formulation.** Random unit-norm projections + Epps–Pulley + Cramér–Wold.
- **What LeWM adds:** action conditioning in the predictor (causal AR transformer with AdaLN action input), a planning protocol (CEM-MPC against the learned dynamics), and the four-environment robotics-relevant evaluation suite (PushT, Reacher, OGBench-Cube, Two-Room).
- **Citation pattern.** LeWM cites this paper as ref [25]; the SIGReg derivation in LeWM §3 is essentially a recap of LeJEPA's central regularizer applied to the action-conditioned setting.

The relationship is the same as VICReg → V-JEPA: a paper introduces an anti-collapse regularizer in a pure-SSL setting, and a successor paper uses the same regularizer for world modeling with actions.

## Why it matters in this wiki

- **The foundational reference for SIGReg.** Previously cited from [Module 12](../syntheses/curriculum-12-lewm-deep-dive.md) as "Balestriero 2025" without further specification; now properly filed as a primary source.
- **The "single hyperparameter" and "heuristics-free" claims** that LeWM inherits originate here. LeWM is the *application* of LeJEPA to offline RL; LeJEPA is the *general* methodology paper.
- **Validation breadth (10+ datasets, 60+ architectures)** is what makes LeWM's "single hyperparameter" claim credible. Without LeJEPA's broad validation, LeWM's four-environment benchmark could be hand-tuned. With LeJEPA's results in hand, the LeWM result is more naturally read as a confirmation that the LeJEPA recipe holds in the action-conditioned setting too.

## Entities mentioned

- [LeWorldModel](../entities/leworldmodel.md) — the action-conditioned application of this paper's methodology.
- [Yann LeCun](../entities/yann-lecun.md) — co-author.
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — the architecture family this paper provides theory for.

## Concepts touched

- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — LeJEPA is "JEPA done correctly."
- [Self-Supervised Learning](../glossary.md#ssl) — LeJEPA is positioned as a heuristics-free SSL method.
- [Learned latent space](../concepts/latent-space.md) — the isotropic-Gaussian-target framing.

## Open questions / TBD

- **Full PDF ingest** — abstract-level only. The actual SIGReg derivation, the proof that isotropic Gaussian is optimal, and the full ablation tables would deepen this page substantially.
- **Empirical comparison vs DINOv2 / V-JEPA 2** at matched compute — the abstract reports 79% on ViT-H/14 but doesn't give a head-to-head against the canonical SSL baselines at the same scale. Worth surfacing on PDF re-ingest.
- **Author entity page for Randall Balestriero** — a co-author on multiple JEPA-line papers in this wiki ([PLDM (2025)](pldm-paper.md), this paper, [LeWM](leworldmodel-paper.md)). Could anchor the SIGReg-line research thread.
- **Theoretical-claims verification** — the "isotropic Gaussian is optimal" claim has formal scope conditions in the paper. Worth restating these precisely once the PDF is ingested, since [Module 12](../syntheses/curriculum-12-lewm-deep-dive.md)'s SIGReg derivation currently presents the result without those conditions.
