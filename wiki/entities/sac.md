---
title: SAC (Soft Actor-Critic)
type: entity
subtype: method
created: 2026-07-05
updated: 2026-07-05
sources: 1
tags: [reinforcement-learning, off-policy-rl, maximum-entropy-rl, actor-critic, continuous-control, algorithm]
---

**SAC** (Soft Actor-Critic) — the off-policy, maximum-entropy actor-critic RL algorithm (Haarnoja, Zhou, Abbeel, [Levine](sergey-levine.md); ICML 2018). The default continuous-control algorithm of modern deep RL and the algorithmic root of the wiki's [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) lineage.

## The idea

SAC optimizes a **maximum-entropy** objective — expected reward *plus* policy entropy, weighted by a temperature α: the agent succeeds at the task while staying as stochastic as possible. This buys **exploration** (keeps sampling alternatives) and **robustness** (doesn't collapse to one mode prematurely). It pairs this with an **off-policy** replay-buffer update and a **stochastic** actor (vs. DDPG's deterministic policy), getting both sample efficiency and stability — famously **consistent across random seeds**, which is what makes it usable without per-task hyperparameter tuning ([SAC paper](../sources/sac-paper.md)).

Original formulation: separate soft **value**, soft **Q**, and **policy** networks; reparameterization-trick policy gradient; proven-convergent soft policy iteration. The practical SAC most code runs (clipped double-Q, no V-network, **automatically-tuned temperature α**) comes from the follow-up (Haarnoja et al. 2018b, arXiv 1812.05905).

## Why it matters in this wiki

SAC is the base layer the whole real-world-RL stack stands on:

- **[RLPD](rlpd.md)** is explicitly "based on SAC" — it adds symmetric sampling + critic LayerNorm + ensembles on top.
- **[SERL](serl.md)** / **[HIL-SERL](../sources/hil-serl-paper.md)** / **[AutoSERL](../sources/autoserl-paper.md)** all inherit SAC through RLPD; the "entropy-regularized actor loss with adaptive α" in HIL-SERL is SAC's.
- It's the canonical off-policy actor-critic in curriculum [Module 8](../syntheses/curriculum/curriculum-08-rl-vocabulary.md) and recurs as a baseline across the wiki's RL sources ([TD-MPC](td-mpc.md), TD-MPC2, [BEHAVIOR-1K](../sources/behavior-1k-paper.md), LeRobot).

## Related

- [RLPD](rlpd.md) — the SAC-based recipe that carries it to real robots.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the concept SAC anchors algorithmically.
- [Sergey Levine](sergey-levine.md) — senior author.
- [Diffusion Policy](diffusion-policy.md) — the imitation-side counterpart; SAC is the model-free-RL-side root.

## Mentioned in

- [SAC paper](../sources/sac-paper.md) — primary source.
- [RLPD paper](../sources/rlpd-paper.md) — base algorithm.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — inherited via RLPD (entropy-regularized actor).

## Open questions / TBD

- The practical **1812.05905** SAC (automatic temperature tuning) is what systems actually run; not yet a separate source page.
- Tuomas Haarnoja / Pieter Abbeel / Aurick Zhou — author pages not yet filed.
