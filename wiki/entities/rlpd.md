---
title: RLPD
type: entity
subtype: method
created: 2026-07-05
updated: 2026-07-05
sources: 6
tags: [reinforcement-learning, off-policy-rl, sac, layernorm, offline-data, sample-efficiency, algorithm]
---

**RLPD** (Reinforcement Learning with Prior Data) — an off-policy actor-critic RL recipe (Ball, Smith, Kostrikov, [Levine](sergey-levine.md); ICML 2023) that incorporates offline data (demos or sub-optimal trajectories) into online learning using standard **[SAC](sac.md)** plus three minimal design choices, **without** offline pretraining or imitation regularizers. It is the **base algorithm** of the wiki's [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) lineage.

## The three design choices

1. **Symmetric sampling** — each training batch is 50% offline-buffer / 50% online-buffer. No hyperparameter to tune.
2. **LayerNorm in the critic** — implicitly bounds Q-value over-extrapolation on out-of-distribution actions, which is what stops off-policy-with-offline-data from diverging (especially under sparse reward / low data / high dimension).
3. **Large critic ensembles + Clipped Double Q + high UTD ratio** — the sample-efficiency lever; more learning signal extracted per real environment step.

Net: **~2.5× improvement** over prior offline-to-online methods (e.g. IQL+finetuning) across D4RL AntMaze / Adroit / Franka Kitchen and other benchmarks, at no extra compute ([RLPD paper](../sources/rlpd-paper.md)).

## Why it matters in this wiki

RLPD is the engine every downstream real-world-RL *system* in the wiki wraps:

- **[SERL](serl.md)** ([paper](../sources/serl-paper.md)) — packages RLPD with reward/reset/control machinery for out-of-the-box real-robot learning.
- **[HIL-SERL](../sources/hil-serl-paper.md)** — SERL + online human corrections; RLPD's symmetric sampling is literally the "sample equally from demo and RL buffers" step.
- **[AutoSERL](../sources/autoserl-paper.md)** — replaces the human with one-demo-derived automated interventions on the same RLPD core.

When any of these papers says "off-policy update," "sample from both buffers," or "bounded value function," that is RLPD.

## Related

- [SAC](sac.md) — the max-entropy off-policy actor-critic RLPD is built on.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the concept RLPD anchors algorithmically.
- [SERL](serl.md) — first real-robot system built on it.
- [Sergey Levine](sergey-levine.md) — senior author.
- [Diffusion Policy](diffusion-policy.md) — the imitation-side counterpart; RLPD is the RL-side engine.

## Mentioned in

- [RLPD paper](../sources/rlpd-paper.md) — primary source.
- [SERL paper](../sources/serl-paper.md) — core algorithm.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — base algorithm.
- [AutoSERL paper](../sources/autoserl-paper.md) — base algorithm.

## Open questions / TBD

- Ilya Kostrikov / Philip Ball / Laura Smith — authors without entity pages yet.
