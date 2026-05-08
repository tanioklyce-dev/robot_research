---
title: Habitat
type: entity
subtype: product
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [habitat, embodied-ai, simulator, meta-fair, navigation, manipulation]
---

**Habitat** — Meta FAIR's open-source **embodied-AI simulation platform** for navigation and manipulation in photorealistic 3D scenes. Runs at high frame rates on commodity GPUs and ships with large 3D-scene datasets (Replica, Matterport3D, HM3D). Habitat 2.0 (2021) added rigid-body dynamics and the Home Assistant Benchmark (HAB), which [[maniskill|ManiSkill]]-HAB later reimplemented at the low-level control layer.

## Position in this wiki
Habitat is a **legacy embodied-AI sim** referenced for context across multiple syntheses but not yet a primary training environment in any ingested source:

- **[[maniskill-hab-paper|ManiSkill-HAB Paper]]** — explicitly compares against Habitat 2.0 throughput (ManiSkill-HAB ~3× faster).
- **[[simulators-for-agentic-robotics-2026|Simulators landscape synthesis]]** — Habitat referenced as a mature point of comparison.
- **[[meta-fair|Meta FAIR]]** entity page — Habitat noted as adjacent embodied-AI sim suite.

## Why it matters
- **Predates the agentic-robotics wave but informed it.** Habitat was the embodied-AI workhorse before the [[robocasa|RoboCasa]] / [[maniskill|ManiSkill]] / [[nvidia-isaac-lab|Isaac Lab]] cohort.
- **Photorealistic 3D scene rendering at scale** — enables visual-navigation training that more physics-focused sims (MuJoCo, MJX) don't natively prioritize.
- **Meta-affiliated.** Sits in the same institutional context as the [[meta-fair|FAIR]] JEPA program but doesn't show up in the ingested JEPA papers — interesting absence.

## Related
- [[meta-fair|Meta FAIR]] — origin lab.
- [[maniskill|ManiSkill]] — competing/successor manipulation benchmark.
- [[robocasa|RoboCasa]] — newer household-manipulation benchmark.
- [[simulators-for-agentic-robotics-2026|Simulators for agentic robotics — 2026 landscape]] — landscape synthesis.

## Mentioned in
- [[maniskill-hab-paper|ManiSkill-HAB Paper]]

## Open questions / TBD
- Habitat 3.0+ status, current adoption — not in the wiki.
- Why Habitat doesn't show up in FAIR's own JEPA work (V-JEPA 2 / V-JEPA 2.1 / JEPA-WMs) despite shared institutional context — open question.
- Habitat papers (Savva et al. 2019; Szot et al. 2021 for HAB) not yet ingested.
