---
title: TD-MPC Paper — Temporal Difference Learning for Model Predictive Control (Hansen et al., ICML 2022)
type: source
url: https://arxiv.org/abs/2203.04955
project_page: https://nicklashansen.github.io/td-mpc
author: Nicklas Hansen, Xiaolong Wang*, Hao Su* (*equal contribution; UC San Diego)
published: 2022-03 (arXiv 2203.04955v2, 2022-07-19; ICML 2022, PMLR 162)
ingested: 2026-07-04
local_path: raw/TemporalDifferneceLearning_for_ModelPredictiveControl_2203.04955v2.pdf
sha256: b80e9fc9eaebfa43ad30641ebb0327346998e604cd7421ae44701ef373b501aa
format: pdf (19 pp. incl. appendices A–L)
tags: [td-mpc, told, model-based-rl, mpc, mppi, latent-world-model, decoder-free, dmcontrol, meta-world, ucsd]
---

## Summary

The original [TD-MPC](../entities/td-mpc.md) paper: a hybrid model-based/model-free framework combining short-horizon sampling MPC (MPPI-style) over a learned **Task-Oriented Latent Dynamics (TOLD)** model with a **TD-learned terminal value function** that extends the effective horizon beyond the planning window — model and value jointly learned. The key argument: modeling the full environment (state or pixel reconstruction) is wasteful because it captures task-irrelevant detail; TOLD models only what predicts reward, regularized by a modality-agnostic **latent-state consistency loss with no decoder**. Achieves superior sample efficiency over model-based and model-free baselines on 92 continuous-control tasks (DMControl + Meta-World), is the **first documented method to solve DMControl's 38-dimensional-action Dog tasks**, and closes the wall-clock gap between MBRL and model-free RL (16× faster than LOOP; matches SAC's time-to-solve). Direct predecessor of [TD-MPC2](td-mpc2-paper.md).

## Key claims

### TOLD model (§4, Eq. 6–11, Alg. 2)
- **Five deterministic MLP components** (no RNN, no probabilistic model): representation `z=h_θ(s)`; latent dynamics `d_θ(z,a)`; reward `R_θ(z,a)`; value `Q_θ(z,a)`; policy `π_θ(z)`.
- **Objective**: temporally weighted (λ=0.5) H-step sum of three losses — reward MSE (c₁=0.5) + TD value with slow EMA target net (c₂=0.1) + **latent state consistency** `‖d_θ(z,a) − h_θ⁻(s′)‖²` (c₃=2). Rollouts are recurrent in latent space (only the first observation is encoded); gradients backprop through time through the model — unlike prior work that decouples model learning from policy/value learning (Dreamer, LOOP).
- **π_θ** is a DDPG/SAC-style Q-maximizer used to (a) compute cheap TD targets (avoiding expensive planning-based targets à la POLO) and (b) guide planning. Alone it's worse than planning but sufficient for value learning.

### Planning (§3, Alg. 1)
- Adapted MPPI: N=512 sampled rollouts + 5% policy-guided; return estimate = short-term learned reward + **γ^H · Q at the horizon** (learned terminal value); top-k=64 elites refit time-dependent diagonal Gaussians; J=6 iterations; H=5; receding-horizon with warm start.
- **Exploration by planning**: sampling std floored at a linearly decayed ε (0.5→0.05); horizon annealed 1→H. Planning std decays as tasks are solved — inherent exploration/exploitation balance (App. E).

### Decoder-free vs reconstruction (§4, Table 3)
- Pixel prediction (PlaNet/Dreamer) forces modeling task-irrelevant detail (e.g. shading); the consistency loss regresses onto the target-encoder embedding instead, making the model **input-modality-agnostic** (demonstrated with proprioception + egocentric-camera fusion).
- Closest prior: MuZero/EfficientZero (reward/value-centric models) — but MCTS needs discrete actions and can't feasibly handle even A∈R⁶; TD-MPC scales to A∈R³⁸.
- Claim: **first to jointly learn model and value via TD-learning in continuous control** with a complete MPC framework.

### Results (92 tasks)
- **Humanoid (A∈R²¹) / Dog (A∈R³⁸)**: solved in ~1M env steps; **first documented result solving DMControl Dog**; large margins over SAC and over MPC with a ground-truth simulator.
- **15 state-based DMControl tasks @ 500k steps**: ≥ SAC/LOOP/MPC:sim throughout; biggest gains on complex dynamics (Quadruped, Acrobot).
- **Image-based DMControl 100k** (10 runs): e.g. Finger Spin 943±59 (best), Cup Catch 933±24; competitive with pixel-specialist baselines (DrQ, EfficientZero) with **up to 15× fewer parameters** (~1.5M total) and no image-specific tuning.
- **Meta-World v2**: 50 goal-conditioned manipulation tasks; far more sample-efficient than SAC on hard ones (Bin Picking, Hammer); **MT10 multi-task** single policy beats multi-task SAC.
- **Wall-time (RTX 3090)**: Walker Walk solved in 0.47 h vs LOOP 7.72 h (**16×**); matches SAC's time-to-solve while being far more sample-efficient. ~20 ms/decision step (50 Hz); inference planning budget can be halved with no performance drop.

### Ablations (§5, Fig. 10, App. A/D)
- Regularization variants: no-latent (state-space prediction), no-consistency (MuZero-like), reconstruction (Dreamer-style decoder), contrastive (SimSiam-style). Reconstruction and contrastive both beat no-regularization, but **latent consistency is the most consistent across tasks**.
- **Transfer** (App. A): finetuning Walk→Run converges much faster than scratch; freezing the encoder barely hurts (transferable features), freezing encoder *and* dynamics degrades substantially (dynamics encodes task-specific behavior) — the finding that motivates TD-MPC2's multi-task scaling.

## Entities mentioned

- [TD-MPC](../entities/td-mpc.md) — this is its primary source (TD-MPC1). Successor: [TD-MPC2 Paper](td-mpc2-paper.md).
- Authors: Nicklas Hansen, Xiaolong Wang, Hao Su (UC San Diego) — no entity pages yet.
- [dm_control / DMControl](../entities/dm-control.md), [Metaworld](../entities/metaworld.md) — benchmarks.
- Baselines/reference points: SAC, LOOP, [Dreamer](../entities/dreamer.md)/Dreamer-v2, PlaNet, MuZero, EfficientZero, CURL, DrQ/DrQ-v2, POLO.

## Concepts touched

- [Optimal control](../concepts/robotics/optimal-control.md) — MPC + learned terminal value is the textbook receding-horizon decomposition; the paper is the cleanest modern "OC over a learned model" instance.
- [World model](../concepts/world-models/world-model.md) — TOLD is the reward-centric corner of the WM design space (vs generative Dreamer, vs self-supervised JEPA).
- [Latent space](../concepts/world-models/latent-space.md) — latent-consistency regression onto an EMA target encoder is a **self-predictive representation** — the same anti-collapse family (EMA + stop-grad) catalogued in [Curriculum Module 4](../syntheses/curriculum/curriculum-04-self-supervised-learning.md), applied to dynamics learning a year before the JEPA-WM wave.
- Model-based RL — the MFRL/MBRL hybrid design ([Curriculum Module 8](../syntheses/curriculum/curriculum-08-rl-vocabulary.md), [Module 10](../syntheses/curriculum/curriculum-10-world-models.md)).

## Open questions

- The paper never mentions TD-MPC2 (predates it); the Conclusions anticipate "architectural innovations" — realized as SimNorm latents + discrete-regression heads in [TD-MPC2](td-mpc2-paper.md).
- Nicklas Hansen entity page — still pending (flagged on the [TD-MPC entity](../entities/td-mpc.md) too); would anchor the TD-MPC1→2 lineage.
- How TD-MPC's latent-consistency loss relates formally to JEPA's EMA-teacher prediction — a curriculum-worthy comparison (both are decoder-free latent prediction; TD-MPC adds reward/value grounding, JEPA adds explicit anti-collapse machinery).
