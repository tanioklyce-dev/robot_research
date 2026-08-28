---
title: Lerrel Pinto
type: entity
subtype: person
created: 2026-05-08
updated: 2026-08-26
sources: 9
tags: [person, nyu, robot-learning, manipulation, foundation-models, dino-wm, rum]
---

**Lerrel Pinto** — Assistant Professor at NYU CS. Robot-learning + manipulation + foundation-models researcher. In this wiki, **co-senior on [DINO-WM](../sources/dino-wm-paper.md)** (with [LeCun](yann-lecun.md)) and a co-author on [Robot Utility Models](../sources/robot-utility-models-website.md) — both NYU-anchored projects with [Meta FAIR](meta-fair.md) collaborators.

## Papers in this wiki
- **[DINO-WM](../sources/dino-wm-paper.md)** (Zhou, Pan, LeCun, Pinto — Nov 2024) — co-senior with LeCun. NYU side of the collaboration.
- **[Robot Utility Models](../sources/robot-utility-models-website.md)** (Etukuru, Shafiullah, …, Pinto — Sep 2024) — co-author.
- **[OK-Robot](../entities/ok-robot.md)** (Liu, Orru, Vakil, Paxton, Shafiullah, Pinto — Jan 2024) — co-senior with Shafiullah. Zero-shot pick-and-drop in 10 NYC homes; 58.5% success; 1.8× over OVMM baseline.
- **[BET Paper](../sources/bet-paper.md)** (Shafiullah, Cui, Altanzaya, Pinto — NeurIPS 2022) — **senior author**. Pinto's earliest paper in the wiki; established multi-modal-BC-via-action-discretization as a problem statement; direct ancestor of [VQ-BeT](vq-bet.md) and the broader Pinto-line BC trajectory.

## Why it matters in this wiki
Pinto sits at the intersection of two things this wiki tracks closely:
1. **JEPA-adjacent world modeling** (DINO-WM uses frozen DINOv2 features + learned predictor; lightweight benches; one of the comparison baselines for [LeWM](leworldmodel.md) and [JEPA-WMs](jepa-wms.md)).
2. **Real-robot generalist policies** (RUM's Stretch-only training corpus + zero-shot xArm 7 transfer is the canonical "data philosophy" alternative to the [DROID](droid.md)-anchored line).

If a future ingest brings in a Pinto-led paper that bridges those two — e.g. a NYU-line world model trained on RUM-style data — it would be load-bearing for this wiki.

## Related
- NYU CS — affiliation.
- [DINO-WM](dino-wm.md) / [Robot Utility Models](robot-utility-models.md) / [Dobb·E](dobb-e.md) — primary papers (Pinto co-senior on Dobb·E + RUM with [Mahi Shafiullah](mahi-shafiullah.md) as lead).
- [Mahi Shafiullah](mahi-shafiullah.md) — likely PhD advisee (lead author on Dobb·E + RUM).
- [Meta FAIR](meta-fair.md) — frequent collaborator (LeCun on DINO-WM, multiple co-authors on RUM).
- [Yann LeCun](yann-lecun.md) — DINO-WM co-senior.

## Mentioned in
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [OK-Robot Project Page](../sources/ok-robot-project-page.md)
- [BET Paper](../sources/bet-paper.md)

## Open questions / TBD
- Full publication trajectory (manipulation + foundation-model line) — not directly cited.
- Lab name / group at NYU — not surfaced.
- [Patch Policy paper](../sources/patch-policy-paper.md) — senior author with [Yann LeCun](yann-lecun.md); dense patch tokens via a block-causal mask, beating a fine-tuned 7.6B [OpenVLA-OFT](openvla.md) in-domain with 51M parameters at 10.99 ms.
