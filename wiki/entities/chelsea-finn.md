---
title: Chelsea Finn
type: entity
subtype: person
created: 2026-05-08
updated: 2026-07-05
sources: 19
tags: [person, stanford, meta-learning, robot-learning, droid, metaworld, aloha, mobile-aloha]
---

**Chelsea Finn** — Assistant Professor at Stanford CS. Meta-learning + robot-learning researcher; introduced MAML (Model-Agnostic Meta-Learning) in 2017. In this wiki, **co-senior on [Metaworld](metaworld.md)** and **senior on [DROID](droid.md)**.

## Papers in this wiki
- **[Mobile ALOHA](../sources/mobile-aloha-paper.md)** (Fu, Zhao, Finn — Jan 2024) — senior author on the bimanual mobile-manipulation system. Brings the **[ALOHA](aloha.md) / [ACT](act.md) lineage** into the wiki. Co-leads [Zipeng Fu](zipeng-fu.md) and [Tony Z. Zhao](tony-zhao.md) are Finn's students.
- **[Metaworld](metaworld.md)** (Yu, Quillen, Levine, Finn — CoRL 2019) — co-senior on the 50-task meta-RL benchmark; the meta-learning framing is largely Finn's research lineage applied to robot manipulation.
- **[DROID](droid.md)** (Khazatsky, Pertsch, …, Finn, Levine — Apr 2024) — senior author on the 13-institution real-robot teleoperation dataset.
- **[SERL](../sources/serl-paper.md)** (Luo, Hu, …, Finn, Gupta, Levine — Jan 2024) — co-author on the open-source [real-world RL](../concepts/learning/real-world-robot-rl.md) suite; the RL-side counterpart to her imitation-heavy ALOHA work.

## Why it matters in this wiki
Three infrastructure papers from three angles: **Metaworld** (sim, meta-RL framing) and **DROID** (real, scene-diversity framing) both shared with [Levine](sergey-levine.md); plus **Mobile ALOHA** (open hardware + co-training pattern) on the bimanual-mobile-manipulation front. The Stanford-Berkeley-multi-institution axis these papers represent is the closest thing to a "standard reference setup" across the robot-learning literature ingested here.

Finn-affiliated work not yet directly ingested but commonly referenced: original ALOHA paper (Zhao et al. RSS 2023; covered here only via Mobile ALOHA's bibliography), Octo (generalist policy), various meta-learning + few-shot imitation work.

## Related
- Stanford CS — affiliation.
- [Metaworld](metaworld.md) / [DROID](droid.md) — primary papers in this wiki.
- [Sergey Levine](sergey-levine.md) — frequent collaborator (Berkeley); shared senior authorship on both ingested papers.
- [Karl Pertsch](karl-pertsch.md) — DROID co-lead (with Khazatsky).

## Mentioned in
- [Mobile ALOHA Paper](../sources/mobile-aloha-paper.md) — senior author.
- [SERL paper](../sources/serl-paper.md) — co-author.
- DROID project page (linked via [DROID](droid.md) entity)
- Metaworld project page (linked via [Metaworld](metaworld.md) entity)

## Open questions / TBD
- Original ALOHA paper (Zhao et al. RSS 2023) + Octo — Finn-affiliated; not yet directly ingested (ALOHA covered transitively via [Mobile ALOHA](../sources/mobile-aloha-paper.md)).
- Lab/group name at Stanford — not surfaced.

## The control-centric evaluation thread

Finn is the throughline of the wiki's world-model *evaluation* record, three years before it became a field:

- **[VP²](../sources/vp2-paper.md)** (Tian, Finn & Wu, ICLR 2023) — the founding result that perceptual metrics mis-rank video predictors for control, with the correlation's sign task-dependent. Everything in the 2026 [WorldArena](worldarena.md) cluster rediscovers this at scale.
- **[Ctrl-World](ctrl-world.md)** (Guo, Shi, Chen & Finn, 2025) — her group's action-conditioned world model, later measured as the **best policy evaluator** in WorldArena (r = 0.986 against simulator ranking).

Co-author Jiajun Wu went on to co-author WorldScore and the [HAI policy brief](../sources/hai-world-model-spatial-intelligence-brief.md) that told policymakers no adequate world-model benchmark exists.

## Mentioned in (additional)

- [VP² — A Control-Centric Benchmark for Video Prediction](../sources/vp2-paper.md)
