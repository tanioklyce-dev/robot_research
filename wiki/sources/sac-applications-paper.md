---
title: "SAC Applications — Soft Actor-Critic Algorithms and Applications (Haarnoja et al. 2018/2019)"
type: source
url: https://arxiv.org/abs/1812.05905
author: Tuomas Haarnoja, Aurick Zhou, Kristian Hartikainen, George Tucker, Sehoon Ha, Jie Tan, Vikash Kumar, Henry Zhu, Abhishek Gupta, Pieter Abbeel, Sergey Levine
published: 2018-12
ingested: 2026-07-05
local_path: raw/RL_SAC_AlgorithmsApplications_1812.05905v2.pdf
sha256: 30df4c4ff7c878aa2938ecaf651eb5cc05dc224eb0e3b5bcc8981dbf30d7a9bd
venue: arXiv 1812.05905 (v2)
format: pdf
tags: [reinforcement-learning, off-policy-rl, maximum-entropy-rl, actor-critic, automatic-temperature, real-world-rl, quadruped, dexterous-manipulation, algorithm]
---

**The "practical SAC."** This is the follow-up to the [original SAC paper](sac-paper.md) (Haarnoja et al. ICML 2018) that turns [Soft Actor-Critic](../entities/sac.md) into the version people actually deploy: it adds **automatic temperature (α) tuning** via a constrained-entropy dual formulation, removing SAC's most annoying per-task hyperparameter, and demonstrates SAC learning **directly on real robots** — quadruped locomotion and dexterous-hand manipulation from images. When [RLPD](../entities/rlpd.md) / [SERL](../entities/serl.md) / [HIL-SERL](hil-serl-paper.md) say "SAC with adaptively-adjusted entropy weight α," this is the paper they mean.

## Summary

The original SAC works but requires hand-tuning the temperature α (the reward-vs-entropy trade-off), and a bad α "can drastically degrade performance." This paper reframes max-entropy RL as a **constrained** optimization — maximize return subject to a minimum average-entropy target — and shows the dual of that problem yields the standard soft actor-critic updates *plus* a gradient update for the dual variable, which *is* the temperature. So α is learned automatically to hit a target entropy. The paper also folds in the by-then-standard practical modifications (clipped double-Q, dropping the separate value network) and — the headline of the "Applications" half — proves the whole thing works on physical hardware: a Minitaur quadruped learning to walk **directly in the real world in ~2 hours** with no simulation, and a D'Claw dexterous hand rotating a valve **from raw images**.

## Key claims

- **Automatic temperature tuning (§5, the main delta).** Recast max-entropy RL as maximizing return subject to an entropy constraint `E[−log π(a|s)] ≥ H̄`. Strong duality gives soft-actor-critic updates plus a dual-variable update; the dual variable plays the role of α. α is then adjusted by gradient descent to match the **target entropy** `H̄` (a single, interpretable, task-scale-robust knob — commonly set to `−dim(action space)`). This removes the brittle manual α tuning of the original SAC.
- **The "practical SAC" architecture.** Together with the automatic α, this version drops the separate soft **value** network of the original (bootstrapping the value from the Q-functions instead) and uses **clipped double-Q** to curb overestimation — the configuration inherited by essentially all downstream SAC-based systems, including [RLPD](../entities/rlpd.md).
- **Real-world quadruped locomotion (§7.2).** A **Minitaur** (8 direct-drive actuators, motor encoders + IMU) learns underactuated walking on flat terrain **directly in the real world, ~2 hours of training, no simulation**, and the learned gait generalizes to unseen terrain/perturbations. An early, concrete proof that model-free RL can be trained on real hardware in practical time.
- **Real-world dexterous manipulation.** A dexterous hand (D'Claw-class) learns a valve-rotation task **from image observations** on real hardware — one of the first image-based real-robot RL manipulation results, and a direct ancestor of the [SERL](../entities/serl.md)/HIL-SERL image-based-RL line.
- **SOTA sample efficiency + asymptotic performance, seed-stable.** Outperforms prior on- and off-policy methods on benchmark tasks in both sample efficiency and final performance, and (SAC's signature) achieves similar performance across random seeds. "SAC is a promising candidate for learning in real-world robotics tasks" — a thesis the later Berkeley real-world-RL papers cash out.

## Entities mentioned

- [SAC](../entities/sac.md) — this paper defines the practical/deployed form of the algorithm entity.
- [Sergey Levine](../entities/sergey-levine.md) — senior author (UC Berkeley); Abhishek Gupta and Pieter Abbeel also co-author (Gupta later co-authors [SERL](../entities/serl.md)).
- [RLPD](../entities/rlpd.md) — the SAC-based recipe that inherits automatic-α SAC.

## Concepts touched

- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the Minitaur / dexterous-hand results are the earliest real-robot points on the wiki's RL lineage, predating SERL by ~5 years.
- Curriculum [Module 8 — RL vocabulary](../syntheses/curriculum/curriculum-08-rl-vocabulary.md) — SAC's temperature/entropy machinery.

## Open questions

- **Target-entropy choice.** The method replaces tuning α with choosing the target entropy H̄; the paper's `−dim(A)` heuristic works but the sensitivity to H̄ on contact-rich manipulation isn't deeply characterized here.
- **Author entity pages.** George Tucker / Jie Tan / Sehoon Ha / Vikash Kumar / Tuomas Haarnoja / Pieter Abbeel / Abhishek Gupta — the Google-Brain-robotics + Berkeley author cluster; none filed yet (Gupta recurs in [SERL](../entities/serl.md)).
