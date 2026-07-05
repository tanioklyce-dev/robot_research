---
title: Sergey Levine
type: entity
subtype: person
created: 2026-05-08
updated: 2026-07-05
sources: 9
tags: [person, uc-berkeley, robot-learning, rl, real-world-rl, droid, metaworld]
---

**Sergey Levine** — Associate Professor at UC Berkeley EECS. Robot-learning and reinforcement-learning researcher; one of the most prolific senior figures in the field across the 2015–2026 window. In this wiki, **senior across the [real-world robotic RL](../concepts/learning/real-world-robot-rl.md) lineage** ([SAC](../sources/sac-paper.md) → [RLPD](../sources/rlpd-paper.md) → [SERL](../sources/serl-paper.md) → [HIL-SERL](../sources/hil-serl-paper.md)), plus **[DROID](droid.md)** and co-senior on **[Metaworld](metaworld.md)**.

## Papers in this wiki
- **[SAC](../sources/sac-paper.md)** (Haarnoja, Zhou, Abbeel, Levine — ICML 2018) — senior author. Soft Actor-Critic, the max-entropy off-policy algorithm at the algorithmic root of the whole real-world-RL line.
- **[RLPD](../sources/rlpd-paper.md)** (Ball, Smith, Kostrikov, Levine — ICML 2023) — senior author. The SAC-based recipe (symmetric sampling + LayerNorm + ensembles) that carries SAC into real-robot learning.
- **[SERL](../sources/serl-paper.md)** (Luo, Hu, …, Finn, Gupta, Levine — Jan 2024) — senior author. Open-source real-world-RL suite; HIL-SERL's predecessor.
- **[HIL-SERL](../sources/hil-serl-paper.md)** (Luo, Xu, Wu, Levine — Oct 2024) — senior author. Human-in-the-loop real-world RL; 100% success on dexterous/dual-arm manipulation in 1–2.5 hr.
- **[DROID](droid.md)** (Khazatsky, Pertsch, …, Finn, Levine — Apr 2024) — senior author on the 13-institution real-robot teleoperation dataset.
- **[Metaworld](metaworld.md)** (Yu, Quillen, Levine, Finn — CoRL 2019) — co-senior on the 50-task meta-RL benchmark.

## Why it matters in this wiki
Levine's appearances split two ways. **Infrastructure papers** — DROID (the canonical real-robot dataset) and Metaworld (the canonical meta-RL benchmark) — underpin the JEPA-for-robotics literature (V-JEPA 2, JEPA-WMs) and the broader RL/world-model literature. **Method papers** — the [SAC](../sources/sac-paper.md) → [RLPD](../sources/rlpd-paper.md) → [SERL](../sources/serl-paper.md) → [HIL-SERL](../sources/hil-serl-paper.md) lineage — are the wiki's anchor for [real-world robotic RL](../concepts/learning/real-world-robot-rl.md): RL trained directly on hardware to superhuman reliability, the counterpoint to the imitation-learning mainstream. Levine is senior author on all four, from the 2018 algorithmic root to the 2024 dexterous-manipulation system.

Adjacent papers from Levine's group not yet ingested but commonly referenced: SAC, RT-1, RT-2, Octo, OpenVLA — multiple of these would deepen the wiki's coverage of the model-based-RL and VLA threads.

## Related
- UC Berkeley EECS — affiliation.
- [Jianlan Luo](jianlan-luo.md) — HIL-SERL lead author, Levine-lab.
- [DROID](droid.md) / [Metaworld](metaworld.md) — infrastructure papers in this wiki.
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) — the concept HIL-SERL anchors.
- [Chelsea Finn](chelsea-finn.md) — frequent collaborator (Stanford); also senior on both DROID and Metaworld.
- [Karl Pertsch](karl-pertsch.md) — DROID co-lead.

## Mentioned in
- [SAC paper](../sources/sac-paper.md) — senior author.
- [RLPD paper](../sources/rlpd-paper.md) — senior author.
- [SERL paper](../sources/serl-paper.md) — senior author.
- [HIL-SERL paper](../sources/hil-serl-paper.md) — senior author.
- DROID project page (linked via [DROID](droid.md) entity)
- Metaworld project page (linked via [Metaworld](metaworld.md) entity)

## Open questions / TBD
- DROID paper (arxiv 2403.12945) and Metaworld paper (arxiv 1910.10897) still worth filing to anchor those citations directly.
- **AutoSERL** (Liu et al. 2026) extends the SERL line but is *not* a Levine paper — first external group to build on the ladder.
- Octo / OpenVLA / RT-1 papers — Levine-affiliated; not yet ingested.
