---
title: SERL
type: entity
subtype: method
created: 2026-07-05
updated: 2026-07-05
sources: 5
tags: [reinforcement-learning, real-world-rl, open-source, software-suite, reward-classifier, forward-backward, impedance-control]
---

**SERL** (Sample-Efficient Robotic reinforcement Learning) — an open-source software suite ([Luo](jianlan-luo.md), Hu, …, [Finn](chelsea-finn.md), Gupta, [Levine](sergey-levine.md); 2024) that makes [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) usable out of the box by packaging a tuned [RLPD](rlpd.md) implementation with reward-specification, auto-reset, and compliant-control components. The **direct predecessor of [HIL-SERL](../sources/hil-serl-paper.md)**.

## What's in the suite

- **Core RL** — a high-quality [RLPD](rlpd.md) implementation supporting image observations and demonstrations.
- **Reward specification** — image-compatible **binary success classifiers** and **VICE** (adversarial reward learning).
- **Auto-reset** — **forward-backward controllers**: a forward policy solves the task, a backward policy resets the environment, enabling reset-free training.
- **Control** — an **impedance controller** design for contact-rich learning on a widely-adopted manipulator ([Franka Panda](franka-panda.md)).

## Results

Learns image-based policies for **PCB-board insertion, cable routing, and object relocation in 25–50 minutes each**, at perfect/near-perfect success, with robustness under perturbation and emergent recovery behaviors — exceeding prior SOTA for comparable tasks ([SERL paper](../sources/serl-paper.md)).

## Position in the lineage

The wiki's real-world-RL systems form a clean ladder, all on the [RLPD](rlpd.md) core:

- **SERL** — demos only, single-arm precision tasks, out-of-the-box implementation.
- **[HIL-SERL](../sources/hil-serl-paper.md)** — adds *online human corrections*; unlocks dual-arm + dynamic tasks SERL doesn't attempt (100% in 1–2.5 hr).
- **[AutoSERL](../sources/autoserl-paper.md)** — *automates the human away* using one demonstration; matches HIL-SERL.

## Related

- [RLPD](rlpd.md) — the algorithm SERL wraps.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — SERL is its reference implementation.
- [Jianlan Luo](jianlan-luo.md) — co-first author; the SERL→HIL-SERL throughline.
- [Franka Panda](franka-panda.md) — target manipulator.
- [Imitation learning](../concepts/learning/imitation-learning.md) — SERL seeds on demos but optimizes RL.

## Mentioned in

- [SERL paper](../sources/serl-paper.md) — primary source.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — predecessor system; the demo-only baseline HIL-SERL improves on.
- [AutoSERL paper](../sources/autoserl-paper.md) — 20-demo SERL is a baseline AutoSERL beats from a single demo.

## Open questions / TBD

- Zheyuan Hu / Abhishek Gupta / Archit Sharma / Stefan Schaal — co-authors without entity pages yet.
