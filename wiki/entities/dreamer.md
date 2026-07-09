---
title: Dreamer / DreamerV3
type: entity
subtype: method
created: 2026-05-10
updated: 2026-07-09
sources: 8
tags: [dreamer, dreamer-v3, world-model, model-based-rl, mbrl, hafner, generative-wm]
---

**Dreamer / DreamerV3** — model-based reinforcement learning (MBRL) family from Danijar Hafner and collaborators (DeepMind / Toronto / collaborators). Trains a recurrent latent dynamics model as a **generative world model** and trains an actor-critic in **imagination** (i.e. on rollouts produced by the world model rather than the environment). DreamerV3 (Hafner et al. 2023) is the latest standard and the version cited as a baseline in modern world-model literature.

## Family lineage

- **[PlaNet](../sources/planet-paper.md)** (Hafner et al. 2019) — recurrent latent dynamics (RSSM) with CEM planning (no actor-critic); ~200× sample-efficiency vs A3C.
- **Dreamer / DreamerV1** (Hafner et al. 2020) — actor-critic in imagination on top of PlaNet's RSSM.
- **DreamerV2** (Hafner et al. 2021) — Atari-class scaling; discrete latent.
- **DreamerV3** (Hafner et al. 2023) — single-config generality across 150+ tasks; first algorithm to mine Minecraft diamonds without human data or curricula. See [DreamerV3 Paper](../sources/dreamer-v3-paper.md).
- **[DayDreamer](../sources/daydreamer-paper.md)** (Wu, Escontrela, Hafner et al. 2022) — Dreamer on **4 physical robots, online, no simulator**: A1 quadruped walks in 1 hour from scratch; UR5/XArm visual pick-place. The real-robot existence proof for the family.

## Key capabilities (DreamerV3)

- **Single hyperparameter set across 150+ tasks.** Continuous + discrete actions, visual + low-dim inputs, 2D + 3D worlds, varying reward sparsity ([Hafner et al. 2023 abstract](../sources/dreamer-v3-paper.md)).
- **Minecraft diamond from scratch.** No human data, no curricula. Long-held MBRL benchmark milestone.
- **Architecture.** Recurrent latent dynamics core (RSSM-line) + reconstruction-based world model + actor-critic trained in imagination.
- **Stability tricks.** Symlog squashing, two-hot reward representation, percentile-based normalization — the "robustness via normalization, balancing, and transformations" claim in the abstract. Exact list to be confirmed against PDF.

## Why it's in this wiki

- **LeWM baseline column.** Dreamer / DreamerV3 is one of the four world-model baselines [LeWM](leworldmodel.md) compares against.
- **Generative-WM family exemplar.** Predicts environment state and reward — opposite end of the world-model design axis from [JEPA](../concepts/world-models/jepa.md), which sidesteps generation entirely.
- **MBRL canon.** Required vocabulary for curriculum [Module 8](../syntheses/curriculum/robot-learning-curriculum.md) (RL) and [Module 10](../syntheses/curriculum/robot-learning-curriculum.md) (world models).

## Position vs adjacent methods

| Method | Latent dynamics | Decodes to pixels? | Planning method | Value bootstrap? |
| --- | --- | --- | --- | --- |
| **DreamerV3** | yes (RSSM) | yes | actor-critic in imagination | yes |
| [TD-MPC2](td-mpc.md) | yes | **no** (decoder-free) | local trajectory MPC | yes |
| [LeWorldModel](leworldmodel.md) | yes | **no** | MPC | no (no explicit value) |
| [DINO-WM](dino-wm.md) | yes (frozen DINOv2) | **no** | MPC | no |

## Related

- [TD-MPC](td-mpc.md) — sibling decoder-free MBRL family.
- [LeWorldModel](leworldmodel.md) — JEPA-style end-to-end latent WM baseline-vs-Dreamer in the LeWM paper.
- [World model](../concepts/world-models/world-model.md) — umbrella concept.

## Downstream (2025–26 ingests)

- **[S5WM](../sources/s5wm-paper.md)** (UZH RPG, 2025) — replaces the RSSM with a parallelizable **S5 state-space model**: up to 10× faster WM training / 4× overall at equal sample efficiency; flown on real racing quadrotors. Attacks the *wall-clock* cost of the Dreamer recipe.
- **[EAWM / EADream](../sources/eawm-paper.md)** (ICLR 2026) — adds an **event-segmentation prediction objective** on top of Dreamer-class backbones: +10–45% across Atari 100K / Craftax / DMC(-GB2), SOTA. Attacks the *representation objective* (events, not pixels).

## Mentioned in

- [DreamerV3 Paper](../sources/dreamer-v3-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md) (as a baseline)
- [S5WM paper](../sources/s5wm-paper.md) — RSSM→SSM swap
- [EAWM paper](../sources/eawm-paper.md) — event-aware objective on Dreamer backbones
- [PlaNet paper](../sources/planet-paper.md) — lineage origin
- [DayDreamer paper](../sources/daydreamer-paper.md) — real-robot deployment

## Open questions / TBD

- ~~Author entity page for Danijar Hafner~~ — created 2026-07-09 ([danijar-hafner](danijar-hafner.md)).
- ~~PlaNet as separate source page~~ — [ingested 2026-07-09](../sources/planet-paper.md). Dreamer V1/V2 remain lineage-table-only (V3 suffices as baseline reference).
