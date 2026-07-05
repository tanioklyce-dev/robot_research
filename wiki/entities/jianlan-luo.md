---
title: Jianlan Luo
type: entity
subtype: person
created: 2026-07-05
updated: 2026-07-05
sources: 2
tags: [person, uc-berkeley, reinforcement-learning, real-world-rl, manipulation]
---

**Jianlan Luo** — robot-learning researcher in [Sergey Levine](sergey-levine.md)'s lab at UC Berkeley EECS. Lead author on the **[SERL](../sources/serl-paper.md) → [HIL-SERL](../sources/hil-serl-paper.md)** line of work that made **sample-efficient real-world reinforcement learning** for dexterous manipulation practical.

## Papers in this wiki

- **[SERL](../sources/serl-paper.md)** (Luo, Hu, …, Finn, Gupta, Levine — Jan 2024) — co-first author. Open-source real-world-RL suite ([RLPD](../entities/rlpd.md) + reward classifier + auto-reset + impedance control); 25–50 min/policy.
- **[HIL-SERL](../sources/hil-serl-paper.md)** (Luo, Xu, Wu, Levine — Oct 2024) — lead author. SERL + online human corrections; 100% success on dexterous/dual-arm tasks in 1–2.5 hr. Maintained the main research codebase.

## Why it matters in this wiki

Luo is the throughline of the wiki's **[real-world robotic RL](../concepts/learning/real-world-robot-rl.md)** thread. The SERL (demo-only) → HIL-SERL (demo + online human corrections) progression, both Luo-led, is the concrete demonstration that RL can be trained *directly on physical robots* at superhuman reliability within practical wall-clock times — the counterpoint to the imitation-learning-dominated ([ACT](act.md) / [Diffusion Policy](diffusion-policy.md)) mainstream elsewhere in the wiki.

## Related

- [Sergey Levine](sergey-levine.md) — advisor and senior author on SERL + HIL-SERL.
- [SERL](../entities/serl.md) / [RLPD](../entities/rlpd.md) — the suite he co-authored and the algorithm it wraps.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the concept his work anchors.

## Mentioned in

- [SERL paper](../sources/serl-paper.md) — co-first author.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — lead author.
- [AutoSERL paper](../sources/autoserl-paper.md) — his SERL/HIL-SERL are the baselines it extends.

## Open questions / TBD

- Luo's earlier cable-routing / assembly RL papers (Luo et al. 2019/2021/2023) are cited throughout HIL-SERL and would deepen the real-world-RL lineage.
