---
title: "RoboJEPA: Scaling Robotic Latent World Models (Zholus et al., Meta FAIR, 2026)"
type: source
url: https://arxiv.org/abs/2610.10515
local_path: raw/2610.10515v1.pdf
sha256: 78a0772ca15fd68f7970c3c6f66f3abfa89d12ff1ef345af5c5b699278d5794c
author: Artem Zholus, Nicolas Beltran-Velez, Jianhao Yuan, Sarath Chandar, Tushar Nagarajan, Daniel Severo, Koustuv Sinha, Michal Drozdzal, Adriana Romero Soriano, Jeannette Bohg, Nicolas Ballas, Mahmoud Assran
published: 2026-10-07
ingested: 2026-10-13
venue: arXiv (cs.AI), v1
format: "paper, 73 pp (15 main + appendices A–K). FAIR at Meta, with Mila / Chandar Lab / Polytechnique Montréal. Checkpoints (22M–8B), training and robot-deployment code released (facebookresearch/robo_jepa)."
tags: [robojepa, jepa, world-model, scaling-laws, v-jepa-2-1, v-jepa-2, action-conditioned, cem, droid, robocasa, multi-embodiment, open-x-embodiment, agibot-world, lerobot, so-101, pi0-fast, pi-zero-5, meta-fair, bohg, assran, ballas]
---

# RoboJEPA: Scaling Robotic Latent World Models (Zholus et al., Meta FAIR, 2026)

## Summary

RoboJEPA is a family of **action-conditioned latent world models from 22M to 8B parameters**. It is the V-JEPA 2-AC recipe scaled up: a **frozen V-JEPA 2.1-G encoder**, and a predictor transformer that regresses the next frame's patch features with an ℓ1 loss, trained on **23 public datasets covering 12 embodiments and 26 action spaces**. That is 2.87M episodes, 15,022 video hours, and 6,692 hours with actions. The contribution is a **scaling law**. On held-out data (real DROID scenes and simulated RoboCasa kitchens), 9-step rollout error on the compute-optimal frontier follows a **second-order power law** L(C) = E + A·C^(α − γ ln C). It was fit on 22M–2B models and **extrapolated to 4B and 8B** with errors of 0.6 and 1.4 ×10⁻³, about 2–3× better than a plain power law. Downstream **goal-image CEM planning** in RoboCasa also improves with compute, and capabilities appear **at distinct compute thresholds in a fixed order**: end-effector control (~10²⁰ FLOPs), then moving while holding an object (~3×10²⁰), then avoiding static obstacles (~10²¹–10²²), then pushing objects (~10²² FLOPs). Long-horizon tasks only scale predictably after training on **10-step autoregressive rollouts** during the cooldown. On a real Franka with a single goal image and no fine-tuning, Grasp success rises from 30% (22M) to **67% (8B)** over 30 episodes per cell. π0.5 still wins Pick and Place (53% vs 27%) and scores 0% on Object Lift. The authors claim the first scaling laws for multi-embodiment robotic world models on real data, and the largest JEPA predictor trained to date.

## Key claims

**Model and recipe (§2, App. A)**
- Predictor: a ViT with a frame-causal mask, local attention over the last 8 timesteps, 4-axis RoPE (t, h, w, view), per-view learned bias, per-embodiment linear action/state encoders, QK-norm (*"of particular importance for training stability when scaling"*), and LayerNorm on the output. Proprioception is integrated (s₍t+1₎ = s_t + a_t), not predicted.
- Loss = ½ teacher-forced ℓ1 + ½ **autoregressive-rollout ℓ1** from a shorter prefix (KV-cached), to fight exposure bias. K = 2 by default; **K = 10 in the "long-horizon" cooldown**, together with 480×640 inputs.
- Training uses a WSD-style schedule: one flat-LR run, then cooldowns branched from intermediate checkpoints, so one run yields many compute points. Compute ranges from 2×10¹⁹ to 9.5×10²² FLOPs, on H100 nodes (the 1B run used 32 × 8 H100s).
- **Encoder choice (App. K):** the project started on the **V-JEPA 2** encoder, and *"the predictor often collapsed beyond a certain model size, despite the frozen encoder,"* while larger datasets caused instability or divergence. V-JEPA 2.1 scaled cleanly. The two encoders are equal on classification but far apart on **dense** tasks (ADE20K 24.4 → 47.9 mIoU, NYUv2 depth RMSE 0.642 → 0.307), and V-JEPA 2.1 is *worse* on IntPhys2 (66.0 → 58.8). The authors' hypothesis: **dense feature quality matters more for scaling a robot world model than "physical understanding" features.** The table is restated from other papers, not a controlled ablation.

**Data (Table 1)**: DROID 92k episodes · Roboset 73k · RoboMIND 35.3k · **LeRobot (SO-101) 21.5k** · RoboCasa365 32k (sim) · 1X 23.5k · **AgiBot World 167.5k (8,036 video h)** · 9 Open-X datasets 2.43M. Several epochs are run over this fixed corpus.

**Scaling law (§3.1)**
- DROID holdout: L = 0.217 + 7.1×10⁻¹⁸·C^(1.815 − 0.0220 ln C). RoboCasa: L = 0.171 + 2.7×10⁻¹⁶·C^(1.640 − 0.0198 ln C).
- Second-order law vs plain power law vs BNSL vs UNSL, selected on 4B/8B extrapolation (Table 2). The two best forms agree on the **irreducible error (~0.2 DROID, ~0.17 RoboCasa)**. In the authors' words, RoboJEPA is *"close to saturation"* at the current data budget. **No single model size stays on the frontier throughout.**
- The long-horizon (K=10) cooldown is more efficient beyond ~10²¹ FLOPs and **lowers the fitted irreducible error** (0.194 → 0.185), which the authors read as less accumulated error.

**Downstream planning (§3.2–3.3)**: CEM, receding horizon, a single goal image, no subgoals, fixed hyperparameters (H = 5, 4,096 samples per iteration, 15/10 iterations), and planning distributed across several GPUs (*"several seconds"* per multi-step plan for 8B; not real time). More than 50,000 evaluation episodes across two platforms.
- Greedy tasks (pose reach, reach while holding an object) improve smoothly and saturate early.
- **Obstacle-reach under short-horizon training: no clean frontier.** A 300M model beats a 1B model. After K=10 training it scales cleanly: below 300M, models stall at ~0.3 reward (stuck on the wrong side of the obstacle); the skill appears around 10²¹ FLOPs and saturates around 10²².
- **Object push: zero success for every model below ~10²² FLOPs**, then all sizes begin to succeed. That points to compute, not size. Peak success is ~0.5.

**Real robot (§3.4, App. G, Table 12)**: Franka/DROID setup with exterior and wrist cameras. **30 episodes per model per task** for RoboJEPA and 50 per VLA. Each episode is scored manually, and goal images are staged by executing a predefined motion.

| Model | Grasp | Object Lift | Pick & Place |
|---|---|---|---|
| π0-FAST (text, DROID-finetuned) | 22% | 12% | 40% |
| π0.5 (text, DROID-finetuned) | 5% | **0%** | **53%** |
| RoboJEPA-22M (goal image) | 30% | 2% | 17% |
| RoboJEPA-1B | 50% | 24% | 10% |
| RoboJEPA-2B | 43% | 40% | 31% |
| RoboJEPA-4B | 60% | 30% | 21% |
| RoboJEPA-8B | **67%** | **50%** | 27% |

- Qualitatively, only models of **2B or more keep the gripper closed after grasping**; smaller ones drop the object. Larger models recover from mistakes more reliably.
- **Decoder**: a diffusion decoder from V-JEPA 2.1 features to Cosmos tokens (CV4x8x8) for visualisation. It also *generates* the frames between the world model's 4-frame-skip predictions. A DROID-finetuned 8B model imagines all three views at 720p.

**Limitations (§5, authors')**: the encoder is frozen, so the law describes a dynamics model on a fixed representation; the fits are near **data saturation**, so more and more diverse interaction data is needed, not just parameters; no text; actions are sampled uniformly with no policy proposal.

## Reading it critically

> [!warning] The real-robot table does not support "improves with model size" on every task
> At **n = 30**, a 95% interval on a 50% rate is about ±18 points. Grasp's trend (30% → 67%) and Object Lift's (2% → 50%) survive that. **Pick and Place does not**: 17 / 13 / 10 / 17 / 10 / 31 / 21 / 27% across sizes is flat within noise, and the 1B model is the worst. Pick and Place is also the only task where the text-conditioned VLAs **beat every RoboJEPA size** (π0.5 53%, π0-FAST 40%). The paper describes the VLAs as degrading on the *other* tasks, which is accurate, but the clean scaling trend is in two of three tasks. Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), report it that way.

- **The VLA comparison is not like-for-like, and the paper says so**: text vs goal image, DROID-finetuned vs a pretraining mixture that contains DROID. A staged goal image carries far more task information than "lift the cup". π0.5's 0% on Object Lift is plausibly a language-grounding failure (the authors suggest "lift" is rare in DROID), not a manipulation one.
- **What the law predicts is imagination error, not success.** The downstream evidence is a correlation between the two in simulation, plus capability thresholds. Thresholds are the opposite of smooth extrapolation: object pushing is 0% until 10²² FLOPs. A loss law tells you *when to expect* a capability only after you have seen it emerge.
- **Saturation is the most decision-relevant line in the paper.** An irreducible error of ~0.2 reached at 8B on a 2.87M-episode corpus means the bottleneck is now **data**, matching every robotics scaling-law page in the wiki.
- **The "VLA comparison" sits beside a clean finding**: the planner is task-agnostic. One set of CEM hyperparameters covers all tasks and model sizes, with no fine-tuning. That is the [world-model-as-policy](../concepts/world-models/world-model.md) claim with real numbers behind it.

## Relation to the H-JEPA paper, also ingested 2026-10-13

These are the two LeCun-lineage world-model papers of the same week, and they take **opposite bets on the encoder**:

| | [RoboJEPA](../entities/robojepa.md) (FAIR) | [H-JEPA](../entities/h-jepa.md) (NYU / AMI) |
|---|---|---|
| Encoder | **frozen** V-JEPA 2.1-G (internet-video pretrained) | **trained end to end** from pixels (LeWM, ViT-Tiny/S) |
| Predictor scale | 22M–**8B** | small; scales in *depth of hierarchy* |
| Data | 2.87M episodes, 12 embodiments | single datasets (DROID alone for real data) |
| Anti-collapse | none needed (encoder fixed), though V-JEPA 2 predictors collapsed at scale | SIGReg + **inverse dynamics** (required on DROID) |
| Planner | CEM, single goal, no subgoals | gradient descent, hierarchical subgoals |
| Real robot | **closed loop**, 3 tasks, n=30 | offline only |
| DROID baseline | — | V-JEPA 2-AC: lowest fidelity at the highest planner compute |

H-JEPA's [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) result does not apply to RoboJEPA in the same form: a frozen encoder cannot learn to discard the arm. RoboJEPA's encoder anecdote is a different instability, in the predictor at scale.

## Entities mentioned
- [RoboJEPA](../entities/robojepa.md) · [V-JEPA 2](../entities/v-jepa-2.md) · [Meta FAIR](../entities/meta-fair.md) · [Jeannette Bohg](../entities/jeannette-bohg.md)
- Data: [DROID](../entities/droid.md) · [RoboCasa](../entities/robocasa.md) · [RoboMIND](../entities/robomind.md) · [Open X-Embodiment](../entities/open-x-embodiment.md) · [AgiBot](../entities/agibot.md) · [LeRobot](../entities/lerobot.md) / [SO-ARM101](../entities/so-arm101.md) · [1X NEO](../entities/1x-neo.md)
- Baselines: [π0](../entities/pi-zero.md) (π0-FAST) · [π0.5](../entities/pi-zero-5.md) · [JEPA-WMs](../entities/jepa-wms.md) · [DINO-WM](../entities/dino-wm.md) · [NVIDIA Cosmos](../entities/nvidia-cosmos.md) (decoder tokenizer)

## Concepts touched
- [Scaling laws](../concepts/learning/scaling-laws-vla.md) — the first fitted, extrapolation-validated law for a robot world model.
- [JEPA](../concepts/world-models/jepa.md) · [World model](../concepts/world-models/world-model.md)

## Open questions
- Does the law hold when the encoder is trained too (the authors' first limitation), and does V-JEPA 2's collapse-at-scale recur?
- What is the data-scaling half? With saturation near, how many more episodes, and from which embodiments, buy the next 0.01 of error?
- Pick and Place at n ≥ 100 per size. Is the flat trend real?
- Latency on robot-side hardware. Several seconds of multi-GPU CEM per plan on a cluster puts the 8B model off any onboard tier.
- Planning with a policy proposal instead of uniform sampling, the obvious hybrid with a VLA.
