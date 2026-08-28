---
title: TD-MPC / TD-MPC2
type: entity
subtype: method
created: 2026-05-10
updated: 2026-08-27
sources: 11
tags: [td-mpc, td-mpc2, world-model, model-based-rl, mbrl, mpc, hansen, decoder-free, latent-prediction]
---

**TD-MPC / TD-MPC2** — model-based reinforcement learning family from Nicklas Hansen, Hao Su, and Xiaolong Wang (UC San Diego). Trains a **decoder-free implicit world model** in latent space and plans with **local trajectory optimization (Model Predictive Control)**, bootstrapped by a **TD-trained value function** that extends the effective horizon beyond the MPC window. Sits alongside [Dreamer](dreamer.md) as a default MBRL baseline in modern world-model literature.

## Family lineage

- **TD-MPC / TD-MPC1** — Hansen, Wang, Su (ICML 2022). Original temporal-difference + MPC formulation. **Primary paper now ingested** — see [TD-MPC Paper](../sources/td-mpc-paper.md).
- **TD-MPC2** — Hansen, Su, Wang (ICLR 2024). Scaling, robustness, single-hyperparameter generality, multi-task agent. See [TD-MPC2 Paper](../sources/td-mpc2-paper.md).

## TD-MPC1 mechanics (from the primary paper)

- **TOLD** (Task-Oriented Latent Dynamics): five deterministic MLPs — encoder, latent dynamics, reward, Q, policy — jointly trained with reward MSE + TD value loss + **latent-state consistency** (regress predicted latent onto an EMA target encoder's embedding; no decoder). Gradients BPTT through H=5-step latent rollouts ([TD-MPC Paper](../sources/td-mpc-paper.md) §4).
- **Planning**: MPPI with N=512 samples + 5% policy-guided rollouts; return = learned short-horizon reward + **γ^H·Q terminal value**; exploration via annealed sampling std.
- **Headlines**: first documented solve of DMControl Dog (A∈R³⁸); 92 tasks across DMControl + Meta-World; 16× faster wall-clock than LOOP; ~1.5M params on image tasks (up to 15× fewer than pixel-specialist baselines).
- **The JEPA-adjacent design point**: latent consistency onto an EMA teacher is a self-predictive representation — the same EMA/stop-grad anti-collapse family as JEPA, but grounded by reward/value instead of explicit regularization. This makes TD-MPC1 the earliest wiki-tracked robotics instance of decoder-free latent prediction (2022, pre-dating the JEPA-WM wave).

## Key capabilities (TD-MPC2)

- **104 online-RL tasks across 4 domains** with a single hyperparameter set ([Hansen et al. 2024](../sources/td-mpc2-paper.md)).
- **317M-parameter multi-task agent.** Single agent operates across 80 tasks, multiple embodiments, and varying action spaces; performance scales with model and data.
- **Decoder-free.** No pixel reconstruction loss — the latent world model is trained implicitly via dynamics + reward + value targets.
- **Architecture.** Implicit latent dynamics + TD-bootstrapped value + local MPC at action time.

## Why it's in this wiki

- **LeWM baseline column.** TD-MPC (and TD-MPC2 by extension) is one of the four world-model baselines in [LeWM](leworldmodel.md).
- **Closest MBRL relative to JEPA in the wiki.** Decoder-free latent dynamics + planning is structurally analogous to [LeWM](leworldmodel.md) and [DINO-WM](dino-wm.md). The differences (TD-bootstrapped value vs MPC-only; per-task RL fine-tune vs offline-trained generalist; collapse-prevention strategy) are the curriculum-relevant axes.
- **MBRL canon.** Required reading for curriculum [Module 8](../syntheses/curriculum/robot-learning-curriculum.md) (RL) and [Module 10](../syntheses/curriculum/robot-learning-curriculum.md) (world models).

## Position vs adjacent methods

| Method | Latent dynamics | Decodes to pixels? | Planning method | Value bootstrap? |
| --- | --- | --- | --- | --- |
| [DreamerV3](dreamer.md) | yes (RSSM) | yes | actor-critic in imagination | yes |
| **TD-MPC2** | yes | **no** | local trajectory MPC | yes |
| [LeWorldModel](leworldmodel.md) | yes | **no** | MPC | no |
| [DINO-WM](dino-wm.md) | yes (frozen DINOv2) | **no** | MPC | no |

## Related

- [Dreamer](dreamer.md) — sibling MBRL family with pixel reconstruction.
- [LeWorldModel](leworldmodel.md) — JEPA-style end-to-end latent WM baseline-vs-TD-MPC in the LeWM paper.
- [World model](../concepts/world-models/world-model.md) — umbrella concept.

## Mentioned in

- [TD-MPC Paper](../sources/td-mpc-paper.md) — **primary source (TD-MPC1)**
- [TD-MPC2 Paper](../sources/td-mpc2-paper.md)
- [LeWorldModel Paper](../sources/leworldmodel-paper.md) (as a baseline)
- [LeRobot ICLR 2026 paper](../sources/lerobot-iclr-2026-paper.md) — **the only model-based / world-model method natively integrated in LeRobot** (alongside HIL-SERL on the RL side). Notable for being the closest thing in LeRobot's current algorithm coverage to the wiki's broader world-model focus (Dreamer, V-JEPA-2, DINO-WM are not yet integrated).
- [Microduck — Pollen Robotics launch](../sources/pollen-robotics-microduck.md) — Referenced as one of [LeRobot](lerobot.md)'s existing RL implementations, raising the open question of why [Microduck](microduck.md) ships an independent mjlab/PPO stack instead.

## Open questions / TBD

- ~~TD-MPC1 paper as a separate source page~~ — filed 2026-07-04: [TD-MPC Paper](../sources/td-mpc-paper.md).
- **Author entity page for Nicklas Hansen** — would anchor the TD-MPC1 → TD-MPC2 lineage.
