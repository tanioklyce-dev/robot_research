---
title: Sim-to-real transfer
type: concept
created: 2026-05-06
updated: 2026-07-04
sources: 17
tags: [sim-to-real, domain-gap, rl, simulation]
---

**Sim-to-real transfer** is the practice of training a robot policy in simulation and deploying it on a physical robot with little or no fine-tuning. The "reality gap" — differences between sim physics, sensor noise, lighting, dynamics — is the central obstacle.

## Why it matters
Real-robot data collection is slow and expensive. Simulation gives unlimited cheap training time. The whole agentic-robotics stack assumes that policies trained in simulators (Isaac Lab, MuJoCo Playground, Genesis, Genie Sim) will generalize to real robots — so the quality of sim-to-real determines whether simulation investment pays off.

## Historical lineage
The problem predates the deep-learning era under the name **simulation bias**: [Kober, Bagnell & Peters 2013](../../sources/kober-rl-robotics-survey-2013.md) (§6) describe policies exploiting model errors as "analogous to overfitting," note that direct sim-to-real transfer had been demonstrated in only a handful of cases, and catalogue the mitigation that became domain randomization — **artificial noise injection** (Jakobi et al. 1995; Atkeson 1998). Their observation that transfer works better for *self-stabilizing* tasks still explains much of the locomotion-vs-manipulation transfer asymmetry.

## Common techniques
- **Domain randomization** — randomize physics, textures, lighting, friction in sim so the policy learns invariances.
- **Domain adaptation** — fine-tune on a small amount of real data after sim training.
- **High-fidelity rendering** — use photorealistic renderers (Omniverse RTX, Madrona) so vision-based policies see realistic input.
- **High-frequency physics** — match real-robot control rates (e.g. [AGIBOT Genie Sim 3.0](../../entities/agibot-genie-sim.md)'s 1,000 Hz physics).
- **Vision pretraining on real images** — augment sim data with real video to anchor representations.

## Quantified gap (2025)

The [Stanford HAI AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) provides the clearest independent measurement of the gap:

| Setting | Benchmark | Top result |
|---|---|---|
| Controlled simulation (short-horizon) | RLBench | **89.4%** (EquAct, Jan 2026) |
| Real household environments (long-horizon) | [BEHAVIOR-1K](../../entities/behavior-benchmark.md) full task success | **12.4%** (2025 Challenge winner) |

The 89.4% vs. 12.4% contrast is the canonical sim-to-real gap for household manipulation as of 2025. RLBench tests 18 short-horizon tasks in a controlled simulator; BEHAVIOR-1K's 1,000 tasks come from surveys of what households actually want robots to do.

## Notable claims
- [MuJoCo Playground](../../entities/mujoco-playground.md) demonstrates **zero-shot** transfer from both state and pixel inputs across quadrupeds, humanoids, hands, and arms ([MuJoCo Playground Paper](../../sources/mujoco-playground-paper.md)).
- Tesla Optimus combines sim-to-real with imitation from human teleoperated/wearable-camera video.

## Related
- [VLA models](vla-models.md) — the typical policy class undergoing sim-to-real.
- [World-model simulators](../world-models/world-model-simulators.md) — sidesteps sim-to-real partially by training inside a learned model of reality.

## Mentioned in
- [Kober, Bagnell & Peters 2013 — RL in Robotics Survey](../../sources/kober-rl-robotics-survey-2013.md) — simulation bias, noise injection, self-stabilizing transfer.
- [MuJoCo Playground Paper](../../sources/mujoco-playground-paper.md)
- [NVIDIA Newton Contact-Rich Manipulation Blog](../../sources/nvidia-newton-contact-rich-manipulation-blog.md)
- [RoboCasa365 Paper](../../sources/robocasa365-paper.md)
- [V-JEPA 2 Paper](../../sources/v-jepa-2-paper.md)
- [Stanford HAI — AI Index Report 2026](../../sources/stanford-hai-ai-index-2026.md) — the 12.4% [BEHAVIOR-1K](../../entities/behavior-benchmark.md) challenge figure.
- [BEHAVIOR-1K Paper](../../sources/behavior-1k-paper.md) — the hard, long-horizon end of the gap; end-to-end RL 0.0, real-robot 0–22% ([OmniGibson](../../entities/omnigibson.md) sim).
