---
title: "What Drives Success in Physical Planning with JEPA-WMs? (Terver et al., TMLR 05/2026)"
type: source
url: https://openreview.net/forum?id=cHZn5Gdh8e
arxiv: https://arxiv.org/abs/2512.24497
code: https://github.com/facebookresearch/jepa-wms
dataset: https://huggingface.co/datasets/facebook/jepa-wms
local_path: raw/7271_What_Drives_Success_in_Ph.pdf
sha256: ea9e100174702a25ab6512021c7e9d314a79df19f75f1c6ee9312e1cb9a48e4b
author: Basile Terver, Tsung-Yen Yang, Jean Ponce, Adrien Bardes, Yann LeCun
affiliations: Meta FAIR (Terver, Yang, Bardes) + Inria Paris (Terver) + ENS/PSL & NYU (Ponce) + NYU (LeCun)
published: 2025-12-30 (arxiv preprint)
revised: 2026-05 (TMLR final version)
ingested: 2026-05-07 (preprint); 2026-05-25 (TMLR full-paper deepening)
tags: [jepa, world-model, jepa-wms, robocasa, metaworld, droid, franka, fair, meta-fair, adaln, rope, dinov2, dinov3, cem, mpc, design-choices]
---

## Summary

**Final TMLR-published version (05/2026)** of the FAIR JEPA-WMs paper, now ingested in full (55 pp) — supersedes the prior arxiv-abstract-level ingest. Confirmed authors and affiliations: **Basile Terver** (Meta FAIR + Inria Paris), **Tsung-Yen Yang** (Meta FAIR), **Jean Ponce** (ENS/PSL + NYU), **Adrien Bardes** (Meta FAIR), **Yann LeCun** (NYU).

The paper's contribution is **not a novel algorithm** — the authors are explicit that "JEPA-WM" is a *unified recipe formalization* of an existing family (PLDM, DINO-WM, V-JEPA-2-AC, EB-JEPA), with the dynamics learned purely through a predictive loss in embedding space, no reconstruction / reward / value / policy heads. The contribution is **a systematic ablation across 7 design axes** producing an empirically-recommended recipe that outperforms both DINO-WM and V-JEPA-2-AC on every evaluated environment (Maze, Wall, Push-T, Metaworld-Reach/Reach-Wall, Robocasa-Reach/Place, DROID).

## Key claims

### The recommended recipe (Table 1, paper p. 5)

| Component | Simulated nav (Wall, Maze, Push-T, Metaworld) | Real-world manipulation (DROID, Robocasa) |
|---|---|---|
| **Visual encoder** | DINOv2-S | **DINOv3-L** |
| **Predictor arch** | **AdaLN + RoPE** | **AdaLN + RoPE** |
| **Predictor depth** | 6 | **12** |
| **Rollout-loss steps (training)** | 2-step | **6-step** |
| **Context length W** | 3 | **5** |
| **Proprioception** | ✓ | ✓ (when aligned with target embodiment; off for DROID→Robocasa zero-shot) |
| **Planner** | CEM with L₂ embedding distance | CEM with L₂ embedding distance |

### Head-to-head results (Table 2, paper p. 12)

Numbers are planning success / Action Score; **bold = best**. Standard error in parens.

| Model | Maze | Wall | Push-T | MW-R | MW-RW | Rc-R | Rc-Pl | DROID |
|---|---|---|---|---|---|---|---|---|
| DINO-WM | 81.6 (3.4) | 64.1 (4.6) | 66.0 (4.7) | 44.8 (8.9) | 35.1 (9.4) | 19.1 (13.4) | 21.7 (7.2) | 39.4 (2.1) |
| V-JEPA-2-AC | — | — | — | — | — | 16.2 (8.3) | 33.1 (7.2) | 42.9 (2.5) |
| **Ours** | **83.9 (2.3)** | **78.8 (3.9)** | **70.2 (2.8)** | **58.2 (9.3)** | **41.6 (10.0)** | **25.4 (16.6)** | **30.7 (8.0)** | **48.2 (1.8)** |

> V-JEPA-2-AC numbers come from the authors' retrained model with a "rollout-loss bug fix" (paper §C); not the public checkpoint. V-JEPA-2-AC was not run on the simulated 2D nav tasks.

### Design-axis findings (§5.2)

1. **Planner — CEM-L₂ wins overall.** Gradient-based planners (Adam, GD) excel only on smooth-cost Metaworld and fail on 2D nav + contact-rich manipulation (local minima). On real-world DROID/Robocasa, CEM and NG (Nevergrad NGOpt wizard) tie — **NG matches CEM with zero hyperparameter tuning**, useful when moving to a new task/dataset. **L₂ consistently beats L₁** for the planning cost across all setups.

2. **Multi-step rollout loss — 2-step helps sim, 6-step helps DROID.** Pure teacher-forcing (1-step) is suboptimal; 2-step improves on simulated environments then degrades for k > 2. On DROID, the optimum shifts to **k = 6** because the model's effective Lipschitz constant Λ_K dominates over the per-step error δ_K when horizons get long. The multistep loss acts as data augmentation against compounding error (analogous to scheduled sampling).

3. **Proprioception — always helps when modality is aligned.** Visual embeddings encode appearance + coarse layout; proprioception encodes precise joint positions / end-effector coords. Without it, Metaworld policies "reach the vicinity of the goal but oscillate, unable to resolve the remaining distance from vision alone." Excluded from DROID→Robocasa zero-shot because proprio spaces aren't aligned.

4. **Context length W.** **Wp ≤ W must hold** (planning context can't exceed training context). Optimal W ≈ 3 on simulated, **W = 5 on DROID** (more complex dynamics need longer context for velocity / object-state inference). W > 5 degrades because larger W reduces unique training slices.

5. **Encoder — DINO ≫ V-JEPA.** DINO (image, fine object segmentation) outperforms V-JEPA / V-JEPA-2 (video, coarser segmentation) as a frozen backbone. Authors' explanation: "distinct objects occupy distinct spatial tokens with sharp boundaries, so that object motion translates into localized, sparse token changes that the predictor can learn efficiently." DINOv3 clearly wins only on photorealistic envs (DROID, Robocasa); DINOv2 ties or beats DINOv3 on synthetic envs.

6. **Predictor architecture — AdaLN+RoPE best on average, but task-dependent.** Compared sincos+ftcond / RoPE+ftcond / RoPE+seqcond / AdaLN+RoPE / AdaLN-zero+RoPE. AdaLN's per-block conditioning prevents action-information vanishing through layers. AdaLN-zero (the Peebles & Xie DiT variant) underperforms AdaLN on the highest-signal environments (DROID, PushT, Maze).

7. **Model scaling — pays off only on real-world data.** Increasing encoder size (ViT-S → ViT-B → ViT-L) and predictor depth (3 → 6 → 9 → 12) **does not help on simulated envs** (saturation at ViT-S, depth ≈ 6 or as low as 3 on Wall/Maze). On DROID, scaling yields **consistent positive gains on both axes**. Practical guideline: scale only when env dynamics are genuinely complex.

8. **Data scaling.** Performance climbs with data on all envs. Authors' best model outperforms DINO-WM most clearly on the least-saturated datasets (DROID, Wall).

### Architectural framing

The paper is the **first cohesive formalization of JEPA-WM as a recipe** (Equations 1–4):

- `z_t = E_{ϕ,θ}(o_t)` — frozen visual encoder + optional learned shallow proprio encoder
- Loss: `L = MSE(P_θ(E_{ϕ,θ}(o_{t-w:t}), A_θ(a_{t-w:t})), E_{ϕ,θ}(o_{t+1}))`
- Planning: minimize `L^p_α(o_t, a_{t:t+H-1}, o_g) = (L_vis + α·L_prop)(F_{ϕ,θ}(o_t, a_{t:t+H-1}), E_{ϕ,θ}(o_g))` over action sequences

Distinguishes JEPA-WMs from **MuZero / PlaNet / Dreamer-class** models — JEPA-WMs have **no reconstruction, reward, value, or policy heads**, only the embedding-space predictive loss.

### Open limitations (paper §6 conclusion)

- **Deterministic predictor** — MSE learns conditional mean of potentially multi-modal futures. Mitigated in current benchmarks by deterministic dynamics + latent abstraction of task-irrelevant variability + closed-loop MPC. For environments with aleatoric uncertainty, JEPA-WMs would need **latent variable injection (LeCun 2022) or diffusion in latent space**.
- **Frozen encoder** — paper focuses on the predictor; concurrent work explores lightweight adaptation (bisimulation encoders, sparse autoencoders on features, decoupling dynamics-relevant from dynamics-irrelevant representations) as complementary directions.
- The proposed "optimum" is per-task-category. There is no single recipe that wins everywhere — sim and real have different best designs.

## Entities mentioned
- [Meta FAIR](../entities/meta-fair.md) — primary affiliation (Terver, Yang, Bardes).
- [JEPA-WMs](../entities/jepa-wms.md) — model family this paper formalizes.
- [V-JEPA 2](../entities/v-jepa-2.md) — baseline (V-JEPA-2-AC variant); same FAIR group's prior work.
- [DINO-WM](../entities/dino-wm.md) — baseline (Zhou et al., NYU + FAIR, Nov 2024).
- [DINOv2](../entities/dinov2.md) — frozen feature substrate for simulated envs.
- [DINOv3](../entities/dinov3.md) — frozen substrate for real-world DROID/Robocasa.
- [RoboCasa](../entities/robocasa.md) — Rc-R/Rc-Pl manipulation eval.
- [DROID](../entities/droid.md) — real Franka dataset (training + eval).
- [Metaworld](../entities/metaworld.md) — MW-R/MW-RW eval.
- [PushT](../entities/pusht.md) — Push-T 2D pushing eval.
- [PointMaze](../entities/pointmaze.md) — Maze eval.
- [Franka Panda](../entities/franka-panda.md) — real-robot eval platform.
- [PLDM](../entities/pldm.md) — prior JEPA-WM end-to-end variant; both predictor and encoder learned.
- [Dreamer](../entities/dreamer.md) — explicitly contrasted (has reconstruction / reward / value heads).
- [TD-MPC](../entities/td-mpc.md) — contrasted (decoder-free MBRL with TD-bootstrapped value).
- [Yann LeCun](../entities/yann-lecun.md) — senior author.
- [Adrien Bardes](../entities/adrien-bardes.md) — senior author.
- [Basile Terver](../entities/basile-terver.md) — first author.
- [Jean Ponce](../entities/jean-ponce.md) — ENS/PSL + NYU senior author.

## Concepts touched
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — paper's defining architecture family; this ingest deepens the JEPA concept page with the design-axis lessons.
- [World model](../concepts/world-models/world-model.md) — physical-planning-with-world-model focus.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — latent-prediction paradigm.
- [Learned latent space](../concepts/world-models/latent-space.md) — frozen DINOv2/v3 patch features as the latent; predictor is the only learned piece.
- [Optimal control](../concepts/robotics/optimal-control.md) — CEM + MPC planning loop closes the control side.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — same paper trains on DROID and evaluates zero-shot on Robocasa.

## Open questions

- **Genie 3 / Cosmos-class generative video WMs** vs the JEPA-WM "no reconstruction" recipe — paper notes them but does not compare directly. The deterministic-predictor limitation is the obvious place where generative-video models might exceed JEPA-WM.
- **Stochastic JEPA-WM extensions** — paper points to latent variable injection (LeCun 2022) or diffusion in latent space as the path forward but doesn't implement either.
- **Encoder co-training (PLDM, EB-JEPA)** vs the frozen-encoder recipe — paper claims frozen DINO ≫ V-JEPA but doesn't run the co-trained recipe through the same ablation.
- **AdaLN's task-dependence** — the architecture choice swings the most across envs; the paper notes the per-task pattern without offering a unifying explanation.
- **Lipschitz / compounding-error analysis is informal** — §C / Remark 1 quantify the accuracy-robustness tradeoff intuitively; a tighter theoretical bound is left open.

## Why this matters (revised)

The TMLR-version ingest changes the wiki's read of this paper in three ways:

1. **The "JEPA into heavy sim" framing remains correct** — RoboCasa is the first heavy-sim entry from the FAIR JEPA line, and this paper drives the [revised "JEPA + sim" synthesis](../syntheses/world-models/why-jepa-research-skips-the-simulator-stack.md). Nothing in the full paper undercuts that read.
2. **The architectural lessons are now load-bearing for the broader JEPA concept page.** AdaLN+RoPE > sincos / sequence conditioning; DINO ≫ V-JEPA as frozen backbone; 2-step rollout ≈ scheduled sampling; CEM-L₂ as the default planner. These are the first published systematic ablations of these axes for JEPA-style world models, and they should now anchor the [JEPA concept page](../concepts/world-models/jepa.md).
3. **The "fair beat us in robotics" framing is now defensible** — Ours > V-JEPA-2-AC on every evaluated env where both ran (Rc-R, Rc-Pl, DROID), and Ours > DINO-WM on every env. This makes JEPA-WMs the **new strongest published JEPA-style robot-planning baseline** as of mid-2026.
