---
title: SAC (Soft Actor-Critic)
type: entity
subtype: method
created: 2026-07-05
updated: 2026-07-17
sources: 3
tags: [reinforcement-learning, off-policy-rl, maximum-entropy-rl, actor-critic, continuous-control, algorithm]
---

**SAC** (Soft Actor-Critic) — the off-policy, maximum-entropy actor-critic RL algorithm (Haarnoja, Zhou, Abbeel, [Levine](sergey-levine.md); ICML 2018). The default continuous-control algorithm of modern deep RL and the algorithmic root of the wiki's [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) lineage.

## The idea

SAC optimizes a **maximum-entropy** objective — expected reward *plus* policy entropy, weighted by a temperature α: the agent succeeds at the task while staying as stochastic as possible. This buys **exploration** (keeps sampling alternatives) and **robustness** (doesn't collapse to one mode prematurely). It pairs this with an **off-policy** replay-buffer update and a **stochastic** actor (vs. DDPG's deterministic policy), getting both sample efficiency and stability — famously **consistent across random seeds**, which is what makes it usable without per-task hyperparameter tuning ([SAC paper](../sources/sac-paper.md)).

Two papers define SAC. The **[original](../sources/sac-paper.md)** (ICML 2018) introduces the max-entropy actor-critic with separate soft **value**, soft **Q**, and **policy** networks; reparameterization-trick policy gradient; proven-convergent soft policy iteration. The **[Algorithms and Applications](../sources/sac-applications-paper.md)** follow-up (1812.05905) defines the *practical* SAC most code runs: it drops the V-network, uses **clipped double-Q**, and — the key delta — **automatically tunes the temperature α** by casting max-entropy RL as an entropy-*constrained* optimization whose dual variable is α, adjusted by gradient descent to hit a **target entropy** (typically `−dim(action space)`). That paper also gave SAC's first **real-robot** demonstrations: a Minitaur quadruped walking directly in the real world in ~2 hr, and a dexterous hand rotating a valve from images.

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

- [SAC paper](../sources/sac-paper.md) — original (ICML 2018).
- [SAC Applications paper](../sources/sac-applications-paper.md) — practical SAC (automatic α + real-robot demos).
- [RLPD paper](../sources/rlpd-paper.md) — base algorithm.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — inherited via RLPD (entropy-regularized actor with adaptive α).
- [USC table-tennis MARL project](../sources/usc-table-tennis-marl.md) — SAC was the best self-play algorithm (ELO 2352), beating PPO and MA-POCA in a [Unity ML-Agents](unity-ml-agents.md) ping-pong environment.

## Open questions / TBD

- Tuomas Haarnoja / Pieter Abbeel / Aurick Zhou / Abhishek Gupta — author pages not yet filed.
