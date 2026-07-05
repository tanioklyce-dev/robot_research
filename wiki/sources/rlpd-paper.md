---
title: "RLPD — Efficient Online Reinforcement Learning with Offline Data (Ball et al. 2023)"
type: source
url: https://arxiv.org/abs/2302.02948
author: Philip J. Ball, Laura Smith, Ilya Kostrikov, Sergey Levine
published: 2023-02
ingested: 2026-07-05
local_path: raw/RL_2302.02948v4.pdf
venue: ICML 2023 (PMLR 202)
format: pdf
tags: [reinforcement-learning, off-policy-rl, offline-data, sample-efficiency, sac, layernorm, real-world-rl, algorithm]
---

**RLPD** (Reinforcement Learning with Prior Data) is the off-policy actor-critic algorithm that underpins the entire [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) lineage in this wiki ([SERL](serl-paper.md) → [HIL-SERL](hil-serl-paper.md) → [AutoSERL](autoserl-paper.md)). Its thesis: you do **not** need offline-RL pretraining or explicit imitation regularizers to exploit prior data online — a standard off-policy method ([SAC](../concepts/learning/real-world-robot-rl.md)) plus a *minimal* set of design choices matches or beats far more complex methods, with **~2.5× improvement** across competitive benchmarks and no extra compute. Code: [github.com/ikostrikov/rlpd](https://github.com/ikostrikov/rlpd).

## Summary

The paper asks whether existing off-policy RL can simply *include* offline data (expert demos or sub-optimal exploratory trajectories) while learning online, without the machinery — pretraining, distribution-shift constraints, imitation terms — that prior methods bolt on. The answer is yes, provided three design choices are made carefully. RLPD is not a new algorithm so much as a **recipe** over SAC, and its lasting importance in this wiki is as the *engine* that SERL/HIL-SERL/AutoSERL wrap with robot-specific reward, reset, and control machinery.

## Key claims

- **Design choice 1 — Symmetric sampling (50/50).** Each training batch is drawn half from the offline (prior-data) buffer and half from the online replay buffer. Dead simple, no hyperparameter, works across a wide range of domains. This is the mechanism [HIL-SERL](hil-serl-paper.md)'s "sample equally from demo and RL buffers" refers to.
- **Design choice 2 — LayerNorm bounds value over-extrapolation.** Adding **Layer Normalization** to the critic implicitly bounds Q-values on out-of-distribution actions, preventing the catastrophic value divergence that otherwise wrecks off-policy learning with offline data (esp. sparse-reward / low-data / high-dim regimes). The paper gives a novel geometric argument (LayerNorm bounds the norm of intermediate representations → bounds extrapolation). Without it, "SAC + Offline Data" diverges; with it, training is stable.
- **Design choice 3 — Large critic ensembles + Clipped Double Q + high UTD.** Random-subset ensembling (à la REDQ/DroQ) with Clipped Double Q-Learning, run at a high **update-to-data (UTD)** ratio, extracts more learning signal per environment step — the sample-efficiency lever.
- **Result — ~2.5× over prior SOTA.** On D4RL AntMaze, Adroit, Franka Kitchen and other benchmarks (10 seeds), RLPD reaches reliable state-of-the-art, sometimes 2.5× better than IQL+finetuning and other offline-to-online methods, with no additional computational overhead. Runs on standard SAC infrastructure.
- **Environment-sensitivity caveat.** The paper documents that "best" design choices in recent RL literature are environment-sensitive — environments that look similar can require opposite choices — and recommends a practitioner workflow rather than a fixed config.
- **Data-agnostic.** The recipe works whether the prior data is a handful of expert demonstrations or a large volume of sub-optimal exploratory trajectories.

## Entities mentioned

- [Sergey Levine](../entities/sergey-levine.md) — senior author (UC Berkeley); the algorithm anchoring his lab's real-world-RL systems line.
- [RLPD](../entities/rlpd.md) — the algorithm entity.

## Concepts touched

- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — RLPD is the base algorithm of the whole recipe.
- [Imitation learning](../concepts/learning/imitation-learning.md) — RLPD's deliberate contrast: it uses demos as *data*, not as an imitation objective, which is why it can surpass the demonstrator.

## Open questions

- **This paper is benchmark-only.** RLPD's evaluation is in simulation (D4RL et al.); its real-robot impact is demonstrated downstream in [SERL](serl-paper.md) / [HIL-SERL](hil-serl-paper.md), not here.
- **Ilya Kostrikov / Philip Ball / Laura Smith** — co-authors without entity pages yet; Kostrikov in particular recurs across the modern off-policy-RL literature.
