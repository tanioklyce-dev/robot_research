---
title: JEPA-WMs
type: entity
subtype: model
created: 2026-05-07
updated: 2026-05-25
sources: 5
tags: [jepa-wms, jepa, world-model, fair, meta-fair, robocasa, metaworld, droid, lecun, bardes, ponce, adaln, rope, dinov3, cem, cc-by-nc]
---

**JEPA-WMs** — a family of [JEPA](../concepts/world-models/jepa.md)-style world models for physical planning, formalized by [FAIR](meta-fair.md) in [Terver et al. (TMLR 05/2026)](../sources/jepa-wms-paper.md) ("What Drives Success in Physical Planning with Joint-Embedding Predictive World Models?"). Authors: **Basile Terver** (Meta FAIR + Inria), **Tsung-Yen Yang** (Meta FAIR), **Jean Ponce** (ENS/PSL + NYU), **Adrien Bardes** (Meta FAIR), **Yann LeCun** (NYU).

The paper's contribution is **not a novel algorithm but a unified recipe + systematic ablation** across 7 design axes, producing a per-task-category optimum that beats [DINO-WM](dino-wm.md) and [V-JEPA-2-AC](v-jepa-2.md) on every evaluated environment.

## Definition (paper formalization)

A "JEPA-WM" is a world model that learns dynamics through a **purely embedding-space predictive loss**, with **no reconstruction, no reward head, no value/policy head**. This distinguishes it from MuZero / PlaNet / Dreamer-class models. The encoder may be frozen (DINO-WM, V-JEPA-2-AC, this paper's recipe) or co-trained (PLDM, EB-JEPA).

- `z_t = E_{ϕ,θ}(o_t)` — frozen visual encoder + optional shallow proprio encoder
- Loss: `L = MSE(P_θ(E_{ϕ,θ}(o_{t-w:t}), A_θ(a_{t-w:t})), E_{ϕ,θ}(o_{t+1}))`
- Planning: minimize `(L_vis + α·L_prop)(F_{ϕ,θ}(o_t, a_{t:t+H-1}), E_{ϕ,θ}(o_g))` over action sequences, with closed-loop MPC

## The recommended recipe ([paper](../sources/jepa-wms-paper.md) Table 1)

| Component | Simulated nav | Real manipulation (DROID, Robocasa) |
|---|---|---|
| Visual encoder | DINOv2-S | **DINOv3-L** |
| Predictor arch | **AdaLN + RoPE** | **AdaLN + RoPE** |
| Predictor depth | 6 | **12** |
| Rollout-loss steps | 2-step | **6-step** |
| Context length W | 3 | 5 |
| Proprioception | ✓ | ✓ (off only when embodiment-misaligned, e.g. DROID→Robocasa) |
| Planner | CEM with L₂ embedding distance | CEM with L₂ embedding distance |

## Head-to-head results ([paper](../sources/jepa-wms-paper.md) Table 2)

Planning success / Action Score — **bold = best**:

| Model | Maze | Wall | Push-T | MW-R | MW-RW | Rc-R | Rc-Pl | DROID |
|---|---|---|---|---|---|---|---|---|
| DINO-WM | 81.6 | 64.1 | 66.0 | 44.8 | 35.1 | 19.1 | 21.7 | 39.4 |
| V-JEPA-2-AC | — | — | — | — | — | 16.2 | 33.1 | 42.9 |
| **Ours** | **83.9** | **78.8** | **70.2** | **58.2** | **41.6** | **25.4** | **30.7** | **48.2** |

V-JEPA-2-AC numbers are the authors' retraining with a "rollout-loss bug fix" (paper §C), not the public checkpoint. V-JEPA-2-AC was not run on the simulated 2D nav tasks.

## Key design-axis findings

1. **DINO ≫ V-JEPA** as frozen backbone for control (DINO's fine object segmentation matters).
2. **AdaLN+RoPE > sincos / sequence conditioning** on average, but task-dependent.
3. **Multi-step rollout loss helps** — k=2 in sim, **k=6 on DROID** (compounding-error Lipschitz term dominates at long horizons).
4. **Proprioception always helps** when embodiments align.
5. **Context length W=3 in sim, W=5 on DROID**; planning context must be ≤ training context.
6. **CEM-L₂ best overall planner**; NG (Nevergrad NGOpt) ties on real-world manipulation with **zero hyperparameter tuning** — useful when moving to a new task.
7. **Scaling encoder + predictor depth helps only on real-world DROID**, saturates on simulated benches.
8. **L₂ > L₁ for the planning cost**, consistently.

## Environments and datasets

From the official `facebookresearch/jepa-wms` README:

- **42 Metaworld tasks** (100 episodes each); evaluated subset = Reach + Reach-Wall.
- **Push-T, PointMaze, Wall** — classic 2D / 3D control benches.
- **[RoboCasa](robocasa.md) kitchen manipulation** — Reach + Place; the heavy-sim entry.
- **[DROID](droid.md)** dataset (raw stereo HD 8.7 TB; non-stereo HD 5.6 TB) — training + offline planning eval on a real Franka.
- **Franka** robot trajectories with "unroll decode evaluation" (16 in-lab videos).
- Optional video pretraining: Kinetics-400, Kinetics-710, Something-Something-v2, HowTo100M.

Pretrained weights ship per environment.

## Open limitations (paper §6)

- **Deterministic predictor** — MSE learns the conditional mean of multi-modal futures. Future direction: latent variable injection (LeCun 2022) or diffusion in latent space.
- **Frozen encoder bias** — paper studies predictor design with a frozen encoder; co-trained encoder variants (PLDM, EB-JEPA) not directly compared in the ablations.
- **No single recipe wins everywhere** — sim and real have different best designs.

## Why it matters

JEPA-WMs is the load-bearing source for the [revised "JEPA + sim" synthesis](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md). It is also the **current strongest published JEPA-style robot-planning baseline** (mid-2026), beating both DINO-WM and V-JEPA-2-AC on every evaluated environment.

## Related
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — architecture family; updated with this paper's design lessons.
- [V-JEPA 2](v-jepa-2.md) — predecessor + baseline.
- [DINO-WM](dino-wm.md) — baseline.
- [PLDM](pldm.md) — encoder-co-trained JEPA-WM contrast.
- [RoboCasa](robocasa.md) — heavy-sim manipulation benchmark.
- [DROID](droid.md) — real Franka dataset.
- [DINOv3](dinov3.md) — recommended encoder for photorealistic envs.
- [Meta FAIR](meta-fair.md) — primary lab.
- [Why JEPA research skips the simulator stack](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md) — revised synthesis citing this paper as the contradicting evidence.

## Code
- Repo: https://github.com/facebookresearch/jepa-wms — see [JEPA-WMs GitHub source page](../sources/jepa-wms-github.md) for full reproducibility recipe.
- Model checkpoints: https://huggingface.co/facebook/jepa-wms (5 JEPA-WMs + 5 DINO-WM baselines + 2 V-JEPA-2-AC baselines + 4 VM2M decoder heads).
- Dataset: https://huggingface.co/datasets/facebook/jepa-wms
- OpenReview: https://openreview.net/forum?id=cHZn5Gdh8e
- **License: CC-BY-NC 4.0** — non-commercial; constrains downstream Stretch / ROSOrin Pro project use to research and personal scope.

## Mentioned in
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
- [JEPA-WMs GitHub](../sources/jepa-wms-github.md)
