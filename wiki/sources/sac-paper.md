---
title: "SAC — Soft Actor-Critic: Off-Policy Maximum Entropy Deep RL with a Stochastic Actor (Haarnoja et al. 2018)"
type: source
url: https://arxiv.org/abs/1801.01290
author: Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, Sergey Levine
published: 2018-01
ingested: 2026-07-05
local_path: raw/RL_SoftActorCritic_1801.01290v2.pdf
venue: ICML 2018 (PMLR 80)
format: pdf
tags: [reinforcement-learning, off-policy-rl, maximum-entropy-rl, actor-critic, continuous-control, sample-efficiency, uc-berkeley, algorithm]
---

**SAC** (Soft Actor-Critic) is the off-policy, maximum-entropy actor-critic algorithm (Haarnoja, Zhou, [Abbeel](../entities/sergey-levine.md), [Levine](../entities/sergey-levine.md); ICML 2018, UC Berkeley) that became the default continuous-control workhorse of modern deep RL — and the algorithm the wiki's entire [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) lineage ([RLPD](../entities/rlpd.md) → [SERL](../entities/serl.md) → [HIL-SERL](hil-serl-paper.md)) is built on top of.

## Summary

SAC targets the two failure modes that kept model-free deep RL out of real-world use: **high sample complexity** and **brittle, seed-sensitive convergence**. Its answer is the **maximum-entropy RL** objective — the actor maximizes expected reward *and* policy entropy, i.e. "succeed at the task while acting as randomly as possible." Combining that objective with an off-policy actor-critic formulation (replay buffer for sample efficiency; a stable stochastic actor rather than the deterministic-policy-gradient of DDPG) yields state-of-the-art results on continuous-control benchmarks with markedly better stability across random seeds than prior off-policy methods.

## Key claims

- **Maximum-entropy objective.** SAC maximizes `E[Σ_t r(s_t,a_t) + α·H(π(·|s_t))]` — reward augmented by an entropy term weighted by a **temperature α**. Entropy maximization improves **exploration** (the policy keeps trying alternatives) and **robustness** (it doesn't commit prematurely to a single mode), and captures multiple near-optimal behaviors.
- **Off-policy + stochastic actor = efficiency *and* stability.** Prior on-policy max-entropy methods (e.g. TRPO/PPO-style) are stable but sample-inefficient; prior off-policy max-entropy methods (soft Q-learning) required complex approximate inference. SAC gets both: a replay-buffer off-policy update with a tractable stable stochastic actor.
- **Architecture — soft policy iteration made practical.** The original formulation uses **three function approximators**: a soft **state-value** network V, a **soft Q-function**, and a **stochastic policy** π (a Gaussian whose mean/variance are network outputs). It alternates soft policy *evaluation* and soft policy *improvement*, which the paper proves converges in the tabular case. The policy is optimized with the **reparameterization trick** for a lower-variance gradient. (The later practical SAC drops the separate V-network and adds **clipped double-Q** and **automatic temperature tuning** — see the [Algorithms and Applications follow-up](sac-applications-paper.md), arXiv 1812.05905.)
- **Results — SOTA continuous control, seed-stable.** Outperforms DDPG, PPO, TD3, and soft Q-learning on MuJoCo continuous-control benchmarks, including the hard **21-action-dimension Humanoid** where DDPG typically fails. Crucially, SAC achieves **very similar performance across different random seeds** — the reliability property that makes it usable without per-task hyperparameter babysitting.

## Entities mentioned

- [Sergey Levine](../entities/sergey-levine.md) — senior author (UC Berkeley); SAC is the algorithmic root of his lab's later real-world-RL systems.
- [SAC](../entities/sac.md) — the algorithm entity.
- [RLPD](../entities/rlpd.md) — the SAC-based recipe that carries SAC into real-robot learning.

## Concepts touched

- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — SAC is the base algorithm under RLPD/SERL/HIL-SERL; its off-policy sample efficiency is *why* real-world RL is feasible at all.
- Curriculum [Module 8 — RL vocabulary](../syntheses/curriculum/curriculum-08-rl-vocabulary.md) — SAC is the canonical off-policy, entropy-regularized actor-critic in the vocabulary.

## Open questions

- **This paper predates the "practical" SAC.** The version most systems actually run (no V-network, clipped double-Q, learned α) is the [Algorithms and Applications follow-up](sac-applications-paper.md) (1812.05905), now also ingested.
- **Tuomas Haarnoja / Pieter Abbeel / Aurick Zhou** — authors without entity pages yet; Abbeel in particular recurs across the RL and robot-learning literature ([DDPM](../entities/ddpm.md) co-author Abbeel is the same person).
