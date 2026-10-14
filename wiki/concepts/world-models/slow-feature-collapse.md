---
title: Slow-feature collapse
type: concept
created: 2026-10-13
updated: 2026-10-13
sources: 3
tags: [slow-feature-collapse, jepa, anti-collapse, sigreg, inverse-dynamics, pldm, droid, world-model, representation-learning]
---

# Slow-feature collapse

**Slow-feature collapse** is the failure in which a predictive world model's encoder represents only what is **constant within an episode**: the scene, the camera, the lighting. It discards the agent it is supposed to model. The prediction loss goes to zero, because the predictor learns the identity map, and no "collapse" alarm fires, because the embeddings still vary *across* episodes and so look healthy to a distribution-level regulariser. The model knows *which room it is in* and nothing about the arm.

It is the temporal counterpart of ordinary representation collapse, where every input maps to one point. Ordinary collapse is what [SIGReg](sigreg.md), VICReg and EMA teachers prevent. Slow-feature collapse **passes all of them**.

## Key references
- [Sobal et al. 2022, "JEPAs focus on slow features"](../../sources/sobal2022-jepa-slow-features-paper.md): the empirical discovery. A **fixed** distractor (constant within an episode, varying across episodes) is fatal; a **changing** one is harmless; VICReg doesn't fix it; inverse dynamics recovers the controllable dot.
- [PLDM](../../sources/pldm-paper.md) (2025): an inverse-dynamics term in the anti-collapse mix, motivated by the 2022 result.
- [H-JEPA paper](../../sources/h-jepa-hierarchical-world-models-paper.md) (2026, App. L): the **theory**, and the failure on real data (DROID).

## The theory (H-JEPA App. L)
- **Three kinds of content** in a sequence: *background* (constant within an episode, readable from one frame), *foreground* (action-driven, partly stochastic), and *distractors* (moving, action-independent).
- **No marginal regulariser can exclude it** (Prop. 1). An encoder that maps the background to any target distribution, Gaussian included, satisfies SIGReg exactly and has zero prediction error. Variance/covariance penalties, whitening, entropy terms and SIGReg all look only at the distribution of single embeddings, so none can tell this encoder from a good one.
- **It is an optimum** (Thm. 1). Any feature carrying unpredictable motion costs prediction error; the background costs nothing. Among zero-loss solutions, training's implicit bias picked the collapse in every SIGReg-only run.
- **Barriers, ranked:**
  1. SIGReg with time **in the sample axis** ("pooled"): a real but small penalty. With time **in the group axis** (per-timestep), zero. Every SIGReg-only DROID run collapsed regardless of λ.
  2. **Time repulsion** (reward latent change, no labels): keeps the predictor off the identity, but never beat the do-nothing baseline. There is no usable weight window when the foreground is itself ~50% unpredictable.
  3. **Inverse dynamics** (regress the action from consecutive latents): an **Ω(1) floor**. A collapsed encoder cannot predict actions, so it pays at least the action variance. **This is the only barrier that works, and it needs action labels.**
- **The theory explains Sobal 2022's three results**: fixed noise is background and becomes the collapse target; changing noise is a distractor and gets shed; IDM recovers the controlled dot but not the stationary one.

## When it bites
**When the scene changes between episodes.** On DROID, 75% of latent variance is between episodes; on OGBench Cube (fixed camera, one scene) it is 28%. Single-scene simulators (Push-T, PointMaze, AntMaze) make the background a point mass, so SIGReg alone suffices there. **That is why the wiki's simulation results never showed this failure.**

## Related concepts
- [SIGReg](sigreg.md) — necessary for rank, provably insufficient against this.
- [JEPA](jepa.md) — "Common training challenges" and the H-JEPA section.
- [World-model evaluation](world-model-evaluation.md) — a collapsed model can have low prediction loss and a healthy-looking embedding distribution. **Measure action sensitivity** (how much the rollout changes when actions are swapped) or within-episode variance share, not loss.

## Current state (2026-10)
A theory now matches the 2022 observation, and the practical answer is unchanged: **use action labels**. For a home robot, whose scenes vary by construction, this means LeWM-style training on teleop or play data with logged actions, **not** passive video, unless a label-free barrier that acts across time is found. The H-JEPA authors list action-free extension as open, and their one attempt (time repulsion) failed.

## Mentioned in
- [H-JEPA paper](../../sources/h-jepa-hierarchical-world-models-paper.md)
- [Sobal et al. 2022](../../sources/sobal2022-jepa-slow-features-paper.md)
- [PLDM paper](../../sources/pldm-paper.md)
