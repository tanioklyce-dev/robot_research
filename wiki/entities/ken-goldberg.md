---
title: Ken Goldberg
type: entity
subtype: person
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [person, uc-berkeley, autolab, manipulation, grasping, code-as-policy]
---

**Ken Goldberg** — Professor at **UC Berkeley**, where he directs the **AUTOLab**. In this wiki he appears as **co-senior author (with [Jim Fan](jim-fan.md)) on both ingested code-as-policy papers**, making him the academic half of the Berkeley ↔ [NVIDIA GEAR](nvidia-gear.md) collaboration that produced them.

## Papers in this wiki
- **[CaP-X](../sources/cap-x-paper.md)** (ICML 2026) — co-senior author (†, equal advising with Linxi "Jim" Fan). The framework separating agent capability from human-designed API scaffolding.
- **[ASPIRE](../sources/aspire-paper.md)** (Jun 2026) — co-author. Continual skill discovery built on CaP-X.

## Why it matters in this wiki
The Berkeley AUTOLab contribution to this line is visible in its **grasping-and-manipulation framing**: both papers treat grasp planning, perception-to-grasp transforms, and grasp-failure recovery as first-class primitives the agent must compose, rather than as a solved black box. ASPIRE's skill library has an entire **object-level grasping** category, and its trace format records grasp candidates as inspectable evidence.

This is a different center of gravity from the wiki's other robot-learning labs — [GEAR](nvidia-gear.md) on foundation models and humanoids, [Physical Intelligence](physical-intelligence.md) on end-to-end VLAs — and it is part of why the code-as-policy line reasons in terms of *composable classical primitives* at all.

## Related
- [NVIDIA GEAR](nvidia-gear.md) — collaborating lab; [Jim Fan](jim-fan.md) is the co-senior author on both papers.
- [Letian (Max) Fu](letian-fu.md) — Berkeley first author on CaP-X.
- [CaP-X](cap-x.md) / [ASPIRE](aspire.md) — the systems.
- [Code as policy](../concepts/agents/code-as-policy.md) — the concept both papers advance.

## Mentioned in
- [CaP-X paper](../sources/cap-x-paper.md)
- [ASPIRE paper](../sources/aspire-paper.md)

## Open questions / TBD
- Goldberg's broader body of work (Dex-Net and the grasp-planning line) is not ingested; the wiki currently knows him only through these two 2026 papers.
