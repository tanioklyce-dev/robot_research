---
title: Jianlan Luo
type: entity
subtype: person
created: 2026-07-05
updated: 2026-07-05
sources: 1
tags: [person, uc-berkeley, reinforcement-learning, real-world-rl, manipulation]
---

**Jianlan Luo** — robot-learning researcher in [Sergey Levine](sergey-levine.md)'s lab at UC Berkeley EECS. Lead author on the **SERL → HIL-SERL** line of work that made **sample-efficient real-world reinforcement learning** for dexterous manipulation practical.

## Papers in this wiki

- **[HIL-SERL](../sources/hil-serl-paper.md)** (Luo, Xu, Wu, Levine — Oct 2024) — lead author. Human-in-the-loop real-world RL reaching 100% success on dexterous/dual-arm tasks in 1–2.5 hr. Maintained the main research codebase.

## Why it matters in this wiki

Luo is the throughline of the wiki's **[real-world robotic RL](../concepts/learning/real-world-robot-rl.md)** thread. The SERL (demo-only) → HIL-SERL (demo + online human corrections) progression, both Luo-led, is the concrete demonstration that RL can be trained *directly on physical robots* at superhuman reliability within practical wall-clock times — the counterpoint to the imitation-learning-dominated ([ACT](act.md) / [Diffusion Policy](diffusion-policy.md)) mainstream elsewhere in the wiki.

## Related

- [Sergey Levine](sergey-levine.md) — PhD/postdoc advisor and senior author on HIL-SERL.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the concept his work anchors.

## Mentioned in

- [HIL-SERL paper](../sources/hil-serl-paper.md) — lead author.

## Open questions / TBD

- **SERL** (Luo et al. 2024, the demo-only predecessor) and **RLPD** (Ball et al. 2023, the base algorithm) are referenced but not yet ingested as their own source pages.
- Luo's earlier cable-routing / assembly RL papers (Luo et al. 2019/2021/2023) are cited throughout HIL-SERL and would deepen the real-world-RL lineage.
