---
title: Multi-agent reinforcement learning (MARL)
type: concept
created: 2026-07-17
updated: 2026-07-17
sources: 1
tags: [reinforcement-learning, multi-agent-rl, self-play, markov-game, ctde, maddpg, ma-poca]
---

# Multi-agent reinforcement learning (MARL)

**Multi-agent reinforcement learning (MARL)** studies RL when **more than one learning agent** shares an environment — cooperative, competitive, or mixed. It generalizes the single-agent [MDP](../../syntheses/curriculum/curriculum-08-rl-vocabulary.md) to a **Markov Game** (a.k.a. stochastic game): `<S, N, {Aᵢ}, {Rᵢ}, {Oᵢ}, ρ, λ, Z>`, where the transition and reward now depend on the **joint** action of all N agents and each agent may see only a local observation `oᵢ`.

## Definition

The core difficulty is that, from any one agent's view, the environment is **non-stationary** — the other agents are *also* updating their policies, so the dynamics shift underneath the learner. This breaks the single-agent convergence guarantees: value-based methods can fail to reach a stationary Nash equilibrium in general-sum games, and even whether equilibrium is the *right* success criterion is contested ([Zhang, Yang & Başar survey, cited in the USC project](../../sources/usc-table-tennis-marl.md)). Two further pressures: **scalability** — the joint action space grows exponentially in N — and **sample inefficiency** — MARL routinely needs millions of interactions even for simple games.

## Information structures / training paradigms

- **Independent Learning (IL)** — each agent treats the others as part of the environment and runs single-agent RL. Simplest, but hits the non-stationarity problem head-on; various methods (e.g. lenient learning, learned communication) try to stabilize it. *(Note: "IL" here means Independent Learning, not [imitation learning](imitation-learning.md).)*
- **Centralized Training, Decentralized Execution (CTDE)** — agents train with access to global/joint information (e.g. a centralized critic) but execute using only their own local observations. **MADDPG** (multi-agent actor-critic; Lowe et al. 2017) is the canonical instance: each agent keeps its own critic `Qᵢ` over the *joint* action to update a decentralized policy. Unity's **MA-POCA** (MultiAgent POsthumous Credit Assignment) is a CTDE trainer with a shared "coach" critic that also handles agents being added/removed mid-episode.
- **Self-play** — agents improve by playing copies/past versions of themselves, with a rating such as **ELO** tracking relative strength. This is the mechanism behind the AlphaGo/AlphaStar lineage and is the default competitive-training loop in [Unity ML-Agents](../../entities/unity-ml-agents.md).

## Cooperation spectrum

MARL problems are **fully cooperative**, **fully competitive** (zero-sum), or **mixed**. Many real games — including table tennis, where a foul is not exactly the opponent's gain — are **not strictly zero-sum**, motivating mixed methods rather than pure adversarial training.

## Key references

- [Learning to play Table Tennis using Multi-agent RL (USC project)](../../sources/usc-table-tennis-marl.md) — a hands-on self-play MARL example in [Unity ML-Agents](../../entities/unity-ml-agents.md); compares IL-style self-play (PPO / SAC) vs. CTDE (MA-POCA), with ELO fitness and reward/bat-size curricula.

## Related concepts

- [Reinforcement-learning vocabulary (Module 8)](../../syntheses/curriculum/curriculum-08-rl-vocabulary.md) — single-agent MDP / PPO / SAC / DQN / actor-critic that MARL builds on.
- [Real-world robotic RL](real-world-robot-rl.md) — the single-agent, real-hardware side of the RL stack.
- [Swarm intelligence](../robotics/swarm-intelligence.md) — a distinct many-agent paradigm (emergent collective behavior from simple local rules) worth contrasting with learned MARL.

## Mentioned in

- [Learning to play Table Tennis using Multi-agent RL (USC project)](../../sources/usc-table-tennis-marl.md)
