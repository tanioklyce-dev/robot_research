---
title: NVIDIA GEAR Lab
type: entity
subtype: research-lab
created: 2026-05-15
updated: 2026-05-15
sources: 2
tags: [nvidia, gear, embodied-ai, humanoids, foundation-models, world-models]
---

**G**eneralist **E**mbodied **A**gent **R**esearch — NVIDIA Research lab founded Feb 2024 and co-led by [Jim Fan](jim-fan.md) and [Yuke Zhu](yuke-zhu.md). Stated mission: "build foundation models for embodied agents in virtual and physical worlds." Houses NVIDIA's [GR00T](nvidia-groot.md) program and is the in-house source of much of the [Isaac Lab](nvidia-isaac-lab.md) / [RoboCasa](robocasa.md) / [MimicGen](mimicgen.md) lineage.

## Four research pillars (lab-stated)
1. **Multimodal foundation models** — LLMs, vision-language models, world models.
2. **General-purpose robots** — locomotion + dexterous manipulation.
3. **Foundation agents** — large action models that bootstrap across games/sims.
4. **Simulation & synthetic data** infrastructure.

## Output snapshot (32 unique publications, 2022–2026)
Mapped to the four pillars and visible in the [GEAR publications list](../sources/nvidia-gear-publications.md):

- **GR00T pillar (humanoid whole-body)** — GR00T N1 (foundation), SONIC, CHIP, HOVER, ASAP, Doorman, VIRAL, Sim-to-Real Vision-Based Dexterous Manipulation.
- **Dream* world-model pillar** — DreamGen (CoRL 2025) → DreamZero → DreamDojo (ICML 2026 spotlight); FLARE (implicit WM); World Simulation with Video FMs paper.
- **Eureka pillar** — Eureka (ICLR 2024), DrEureka (RSS 2024) — LLM-as-reward-designer.
- **Open-ended agents pillar** — MineDojo (NeurIPS 2022 outstanding) → Voyager (TMLR 2024) → AMAGO → NitroGen (CVPR 2026 oral).
- **Sim / synthetic-data infrastructure** — Isaac Lab paper (Nov 2025), RoboCasa (RSS 2024), MimicGen (CoRL 2023 outstanding), MimicPlay, EgoScale, SCIZOR, Sim-and-Real Co-Training.
- **Manipulation / agents** — VIMA (ICML 2023 outstanding), Prismer (TMLR 2024), CaP-X (ICML 2026 oral), Self-Improving VLA via Residual RL (ICLR 2026).

## Position in the wiki
GEAR is **the in-house research source** of essentially every NVIDIA-product entity already in the wiki:
- [GR00T](nvidia-groot.md) — direct.
- [Isaac Lab](nvidia-isaac-lab.md), [Isaac Sim](nvidia-isaac-sim.md) — used as the simulation substrate for nearly all GEAR papers; the Nov 2025 Isaac Lab arXiv paper is GEAR-authored.
- [RoboCasa](robocasa.md), [MimicGen](mimicgen.md) — both authored under Yuke Zhu at NVIDIA / UT Austin.
- [Newton physics engine](newton-physics-engine.md), [NVIDIA Cosmos](nvidia-cosmos.md) — adjacent product groups consumed by GEAR's world-model and humanoid lines.

## Awards (selected)
- "Top 10 NVIDIA Research Highlights of 2023" — Eureka, DrEureka, RoboCasa, GR00T N1.
- Outstanding Paper Awards — MineDojo (NeurIPS 2022), VIMA (ICML 2023), MimicGen (CoRL 2023).
- Spotlight / Oral — DreamDojo (ICML 2026 spotlight), AMAGO (ICLR 2024 spotlight), CaP-X (ICML 2026 oral), NitroGen (CVPR 2026 oral).

## Related
- [NVIDIA](nvidia.md) — parent.
- [Jim Fan](jim-fan.md), [Yuke Zhu](yuke-zhu.md) — co-leads.
- [NVIDIA GR00T](nvidia-groot.md), [NVIDIA Isaac Lab](nvidia-isaac-lab.md), [RoboCasa](robocasa.md), [MimicGen](mimicgen.md) — outputs.

## Mentioned in
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md)
- [EgoScale Paper](../sources/egoscale-paper.md)
