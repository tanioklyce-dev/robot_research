---
title: RoboJEPA
type: entity
subtype: model
created: 2026-10-13
updated: 2026-10-13
sources: 1
tags: [robojepa, jepa, world-model, scaling-laws, v-jepa-2-1, meta-fair, cem, multi-embodiment, open-weights]
---

**RoboJEPA** is Meta FAIR's family of **action-conditioned latent world models (22M–8B)**, released October 2026. A predictor regresses next-step features of a **frozen V-JEPA 2.1-G** encoder and is trained on 23 datasets covering 12 embodiments. Planning uses CEM toward a single goal image. Its significance is the **first fitted, extrapolation-validated scaling law** for a robot world model ([paper](../sources/robojepa-scaling-robotic-latent-world-models-paper.md)). Checkpoints and code are released.

## Key facts
- **Law**: held-out 9-step rollout ℓ1 error on the compute frontier follows L = E + A·C^(α − γ ln C). Fit on 22M–2B, it predicts 4B and 8B within ~10⁻³. The irreducible error (~0.2 DROID, ~0.17 RoboCasa) is close, so the bottleneck is now data.
- **Capability thresholds** (RoboCasa, goal-image CEM): end-effector control ~10²⁰ FLOPs → holding an object ~3×10²⁰ → obstacle avoidance ~10²¹–10²² → object pushing ~10²².
- **Long horizon needs long-rollout training**: with 2-step rollouts there is no clean scaling on obstacle-reach; 10-step rollouts in the cooldown restore it.
- **Real Franka** (n=30): 8B Grasp 67% / Lift 50% / Pick and Place 27%. π0.5 gets 5% / 0% / **53%** with text goals. Pick and Place shows no size trend.
- **Encoder**: V-JEPA 2 as the frozen encoder led to predictor collapse at scale; V-JEPA 2.1 (much better dense features) did not.
- Planning takes several seconds per multi-step plan on multiple GPUs at 8B; not real time.

## Position in the landscape
The **frozen-encoder, scale-the-predictor** branch of the JEPA world-model line ([V-JEPA 2](v-jepa-2.md)-AC → [JEPA-WMs](jepa-wms.md) at 229M → RoboJEPA at 8B). It contrasts with the **end-to-end, small-model** branch ([LeWorldModel](leworldmodel.md), [H-JEPA](h-jepa.md)). See the comparison table on the [source page](../sources/robojepa-scaling-robotic-latent-world-models-paper.md#relation-to-the-h-jepa-paper-also-ingested-2026-10-13).

## Related
- [Three ways to scale a JEPA world model](../syntheses/world-models/three-ways-to-scale-a-jepa-world-model.md) — the synthesis comparing this with the other two autumn-2026 scaling bets.
- [Scaling laws](../concepts/learning/scaling-laws-vla.md) · [JEPA](../concepts/world-models/jepa.md) · [DROID](droid.md) · [RoboCasa](robocasa.md) · [Meta FAIR](meta-fair.md) · [Jeannette Bohg](jeannette-bohg.md)

## Mentioned in
- [RoboJEPA paper (Zholus et al., 2026)](../sources/robojepa-scaling-robotic-latent-world-models-paper.md)
