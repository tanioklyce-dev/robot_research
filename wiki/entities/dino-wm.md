---
title: DINO-WM
type: entity
subtype: model
created: 2026-05-07
updated: 2026-07-26
sources: 22
tags: [dino-wm, dinov2, world-model, jepa-adjacent, lecun, pinto, nyu, meta-fair]
---

**DINO-WM** — "World Models on Pre-trained Visual Features enable Zero-shot Planning." From [FAIR](meta-fair.md) (LeCun) and NYU (Lerrel Pinto), introduced in [Zhou et al. (Nov 2024)](../sources/dino-wm-paper.md). Models visual dynamics in **DINOv2 patch-feature space** with a frozen pretrained encoder + learned predictor — JEPA-adjacent (predicts in latent space) but **not strictly JEPA** (encoder frozen, not co-trained).

## Approach
- Frozen DINOv2 encoder produces patch features.
- Learned dynamics model predicts next-step features given action.
- **Zero-shot planning** via action-sequence optimization against observational goals.
- "Without expert demonstrations, reward modeling, or pre-learned inverse models" (paper abstract).

## Environments
Six core environments per the project page (https://dino-wm.github.io/):

- **PushT** — 2D pushing benchmark.
- **Wall** — navigation in walled environments.
- **PointMaze** — point-mass maze navigation.
- **Rope** — deformable rope manipulation.
- **Granular** — multi-particle / granular media.
- **Reacher** — joint-space reaching.

Plus eval variants: **WallRandom, PushObj, GranularRandom, DM Control Reacher**, and **CLEVRER** (unconditioned world modeling).

> [!note] Physics engine
> Secondary research identifies underlying physics as **[MuJoCo](mujoco.md) 2.1**. Project page does not state this; treat as wiki-internal claim until confirmed against paper body.

## Why it matters
- **Lightweight-sim JEPA-adjacent baseline.** Cited as a baseline in both [LeWM](../sources/leworldmodel-paper.md) and [JEPA-WMs (Terver et al.)](../sources/jepa-wms-paper.md) — meaning DINO-WM is the comparison every later JEPA-style robotics paper has to beat.
- **Different design point from LeWM.** DINO-WM uses a frozen pretrained DINOv2 encoder; LeWM trains the encoder end-to-end with SIGReg. The two stake out the "frozen pretrained" vs "end-to-end" axis of the JEPA-style world-model design space.
- **Beaten by JEPA-WMs on every evaluated env** ([Terver et al., TMLR 05/2026](../sources/jepa-wms-paper.md), Table 2): Maze 83.9 vs 81.6, Wall **78.8 vs 64.1**, Push-T 70.2 vs 66.0, MW-R **58.2 vs 44.8**, MW-RW 41.6 vs 35.1, Rc-R 25.4 vs 19.1, Rc-Pl 30.7 vs 21.7, DROID 48.2 vs 39.4. The JEPA-WMs recipe (AdaLN+RoPE predictor + 2-step rollout + proprioception + CEM-L₂ planner; DINOv3-L for photorealistic envs) is the **first published systematic improvement** on the DINO-WM baseline.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — JEPA-adjacent architecture.
- [Learned latent space](../concepts/world-models/latent-space.md) — DINO-WM models dynamics in *frozen DINOv2 patch-feature space*; the latent is inherited, not learned.
- [DINO-world](dino-world.md) — sibling DINOv2-feature world-model line from FAIR (Baldassarre et al. 2025).
- [LeWorldModel](leworldmodel.md) — end-to-end JEPA contrast.
- [V-JEPA 2](v-jepa-2.md) — full JEPA contrast.
- [Meta FAIR](meta-fair.md) — co-affiliation.
- [MuJoCo](mujoco.md) — likely physics backend.

## Mentioned in
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md) — cites DINO-WM as baseline
- [LeWorldModel GitHub](../sources/lewm-github.md) — DINO-WM listed as baseline
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md) — cites DINO-WM as baseline
- [DINO-world Paper](../sources/dino-world-paper.md) — sibling DINOv2-feature world-model line
- [VLA-JEPA Paper](../sources/vla-jepa-paper.md) — DINO-WM as comparator
- [HWM — Hierarchical Planning with Latent World Models](../sources/hwm-paper.md) — DINO-WM is the **Push-T base** that HWM's two-level planning wraps (17%→61% at d=75)
- [stable-worldmodel paper (Maes et al., 2026)](../sources/stable-worldmodel-paper.md) — implemented as a baseline in the `swm` platform; benchmarked under controlled visual/physical perturbation (quadratic decay under distractors).
- [WorldDP paper (Goswami et al., 2026)](../sources/worlddp-paper.md) — DINO-WM as a baseline (its raw-DINOv2-patch state is exactly what WorldDP's object-centric encoding is argued to improve on); single-stage, scores 0 on multi-stage tasks.
- [Sensorimotor World Models paper (Ivashkov et al., 2026)](../sources/sensorimotor-world-models-paper.md) — DINO-WM cited as the "freeze the encoder" point in the anti-collapse design space.

## A caution from the 2026 probe studies

DINO-WM builds its world model on a **frozen image-SSL encoder**. Under a shared inverse-dynamics probe, that class of encoder is the weakest measured: Web-DINO reaches only **0.16** action R² and SigLIP 2 **0.17**, clustered with pixel-reconstruction encoders and far below video-pretrained backbones (V-JEPA 2 at 0.85, VideoMAE at 0.75). A λ sweep across five orders of magnitude leaves them in a 0.1-wide band — "the limitation is representational rather than optimization-related," and image-SSL encoders produce **negative rotation R²** even after action supervision ([action-relevant latents](../sources/action-relevant-latents-paper.md)).

> [!warning] Contradiction — the second study disagrees
> [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md) evaluates Web-DINO as the latent space of a diffusion world model on real Bridge V2 data and finds it **strong**: IDM Pearson r = 0.820 against V-JEPA 2.1's 0.829, best encoder-latent success-classifier accuracy (0.906), and comfortably ahead of every reconstruction encoder. It groups Web-DINO *with* V-JEPA as "semantic."
>
> So the two 2026 studies disagree precisely about whether DINO-class frozen features are an adequate control substrate. Candidate explanations — Pearson r vs R², spatial patch latents vs mean-pooled features, real vs simulated data, aggregate vs per-DoF — are laid out in the [source page](../sources/latent-space-robotic-world-models-paper.md#contradiction-with-the-snu-probe-study). Unresolved, and it is the single most consequential open question for this page's design choice.

> [!note] What this does and doesn't say
> It does **not** say DINO-WM plans badly — DINO-WM's own results beat DreamerV3 and TD-MPC2 on goal-conditioned planning, and the probe measures representation quality, not closed-loop success. What it says is that the *encoder choice* is a measurable constraint, and that "frozen DINOv2 features" and "V-JEPA latent prediction" are not interchangeable substrates even though the wiki files both under [JEPA](../concepts/world-models/jepa.md)-adjacent. The paper is explicit: "the data does not support grouping V-JEPA with image-only semantic SSL methods."

## Mentioned in (additional)

- [What Makes Video World Model Latents Action-Relevant](../sources/action-relevant-latents-paper.md)
- [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md) — the counter-evidence: Web-DINO latents nearly match V-JEPA as a world-model substrate.
