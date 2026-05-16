---
title: Navid Azizan
type: entity
subtype: person
created: 2026-05-09
updated: 2026-05-09
sources: 2
tags: [person, mit, control-theory, meta-learning, learning-for-control, drone]
---

**Navid Azizan** — Esther and Harold E. Edgerton Assistant Professor, MIT Department of Mechanical Engineering; affiliated with IDSS and LIDS. Research focus: learning-based control, optimization, and decision-making for robotic and autonomous systems. Notable for the **SDRE / SDC factorization** line (ICML 2023) and the **meta-learning + mirror descent** adaptive drone control work (2025).

## Papers in this wiki

- **[Learning Control-Oriented Dynamical Structure from Data](../sources/learning-control-oriented-dynamical-structure.md)** (Richards, Slotine, Azizan, Pavone — ICML 2023) — co-author. Proposes SD-LQR: semi-supervised learning of SDC factorizations for SDRE-based nonlinear trajectory tracking. Outperforms CCM and naïve LQR in data-scarce regimes.

- **[MIT Drone Adaptive Control](../sources/mit-drone-adaptive-control.md)** (Tang, Sun, Azizan — 2025) — senior author. Meta-learning + automatic mirror-descent selection for drone trajectory tracking under wind disturbances; 50% less tracking error than baselines; 15 min training data.

## Research thread
Both papers share a theme: **learning to control nonlinear systems under data scarcity and environmental uncertainty**, without assuming known disturbance structure or full system models. The 2023 paper targets the model-learning problem (what structure to learn); the 2025 paper targets the disturbance-rejection problem (how to adapt at runtime).

## Related
- MIT Mechanical Engineering / IDSS / LIDS — affiliation
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — domain context for drone work

## Mentioned in
- [Learning Control-Oriented Dynamical Structure from Data](../sources/learning-control-oriented-dynamical-structure.md)
- [MIT Drone Adaptive Control](../sources/mit-drone-adaptive-control.md)
