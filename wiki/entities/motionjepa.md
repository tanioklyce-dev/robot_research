---
title: MotionJEPA
type: entity
subtype: model
created: 2026-10-22
updated: 2026-10-22
sources: 2
tags: [motionjepa, disreg, jepa, slow-feature-collapse, anti-collapse, leworldmodel, label-free, balestriero, klindt]
---

# MotionJEPA

**MotionJEPA** is a [LeWorldModel](leworldmodel.md)-style action-conditioned [JEPA](../concepts/world-models/jepa.md) trained with **DISReg**, a label-free regulariser against [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md). A second ViT-Tiny embeds the pixel difference `o_{t+1} − o_t`, and a small head must predict that embedding from the pair of frame embeddings `(z_t, z_{t+1})`. An encoder that represents only the static scene cannot do that. Karmann, Li, … [Klindt](david-klindt.md), [Balestriero](randall-balestriero.md) et al. (Oxford, vivo, AMI Labs and others), arXiv 2609.23881, September 2026 ([paper](../sources/motionjepa-temporal-feature-collapse-paper.md)).

## Why it matters here

It is the **first label-free barrier** in the wiki shown to work against slow-feature collapse. The [hierarchical H-JEPA](h-jepa.md) paper, which has the same senior author and came out two weeks later without citing it, had concluded that only inverse dynamics, which needs action labels, works. The two are compatible. DISReg acts on the joint law of consecutive embeddings, which is what H-JEPA's theorem says a barrier must do. It narrows the claim to "only inverse dynamics has been shown on scene-diverse real data". See [the batch synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md).

## Results ([paper](../sources/motionjepa-temporal-feature-collapse-paper.md))

- **Synthetic games** (Pong / Dino / Golf, 3 seeds): it is the only method that keeps every feature group under 0.1 probe NMSE in the image embedding. LeWM keeps the score and the background. [SMWM](smwm.md) keeps only what the action moves.
- **LeWM's four benchmarks with a per-episode wood background**, CEM, 25-step mean success: **LeWM 20.4%, IDM 77.2%, MotionJEPA 81.8%, MotionJEPA + IDM 86.4%**. No seeds or spread are reported for the planning table.
- The world model itself is still action-conditioned. "Label-free" applies to the regulariser.

## Limits

Simulation only, with a **fixed camera**. Under a fixed camera the background subtracts out of the difference image exactly. With ego-motion, which a mobile manipulator has, the difference image is mostly scene. Whether DISReg still protects in that case is untested. Its λ weights (0.25 / 0.5 / 2) come with no stated origin. Code: github.com/mkarmann/motion-jepa (no license file).

## Related
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — barrier #4 on that page.
- [SMWM](smwm.md) — inverse dynamics with the action as target; DISReg replaces the target with visual change, and the two are complementary.
- [TDV](../sources/tdv-paper.md) — conditions prediction on the pixel difference; DISReg predicts its embedding instead.
- [Hamiltonian JEPA](hamiltonian-jepa.md) — a structural barrier, in the same batch.

## Mentioned in
- [MotionJEPA paper](../sources/motionjepa-temporal-feature-collapse-paper.md)
- [Predictive Closure paper](../sources/predictive-closure-jepa-feature-selection-paper.md) (cited)
- Synthesis: [What the latent throws away](../syntheses/world-models/jepa-dynamics-collapse-fixes.md)
