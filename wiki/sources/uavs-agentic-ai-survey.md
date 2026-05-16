---
title: "UAVs Meet Agentic AI: A Multidomain Survey of Autonomous Aerial Intelligence and Agentic UAVs"
type: source
url: https://arxiv.org/html/2506.08045v1
author: Ranjan Sapkota, Konstantinos I. Roumeliotis, Manoj Karkee
affiliations: Cornell University; University of the Peloponnese
published: 2025-06
ingested: 2026-05-09
tags: [uav, drone, agentic-ai, survey, edge-ai, vlm, swarm, precision-agriculture]
---

## Summary
Comprehensive multidomain survey defining **agentic UAVs** — autonomous aerial systems with "goal-driven behavior, contextual reasoning, and interactive autonomy." Establishes a four-layer architecture (Perception / Cognition / Control / Communication) and maps enabling technologies and open challenges across eight application domains. Cornell + University of the Peloponnese. arXiv 2506.08045.

## Key claims

### Agentic UAV definition
Agentic UAVs are distinguished from traditional UAVs by operating at **autonomy levels 4–5** (context-aware, minimal human oversight) vs. traditional systems at levels 1–2 (rule-based, operator-dependent). The defining capabilities: learned policies, multimodal sensor fusion, dynamic goal planning, onboard edge AI.

### Four-layer architecture ([concept page](../concepts/robotics/agentic-uavs.md))
1. **Perception** — multimodal sensing: RGB, thermal, LiDAR, hyperspectral
2. **Cognition** — RL, task decomposition, affordance reasoning, transformer attention for memory
3. **Control** — MPC + neural policy networks for trajectory execution
4. **Communication** — V2X protocols for swarm coordination

Mathematical formalism: `o_t = Φ(s_t)` — sensor inputs → semantic representations via neural encoders.

### Enabling technologies
- **Edge AI processors**: NVIDIA Jetson, Intel Movidius
- **VLMs**: Flamingo, LLaVA for natural-language instruction execution
- Multimodal sensor fusion; MDPs for mission planning

### Eight application domains
| Domain | Capability highlight |
|---|---|
| Precision agriculture | Real-time NDVI, adaptive spraying, autonomous replanning |
| Disaster response / SAR | SLAM + thermal survivor detection, swarm coordination |
| Environmental monitoring | Air/water quality, species tracking |
| Urban infrastructure | Autonomous defect classification, 3D structural mapping |
| Logistics | GPS-denied navigation, semantic landing zone detection |
| Defense / security | Perimeter surveillance, threat detection, multi-agent coordination |
| Wildlife conservation | Non-invasive tracking, anti-poaching |
| Construction / mining | BIM integration, stockpile volume monitoring |

### Key challenges
- Real-time inference latency constraint: τ_c < δ ≈ 100 ms
- GPS-denied navigation reliability
- Power vs. compute tradeoff on edge hardware
- Regulatory: airspace integration, decision transparency, safety certification

## Entities mentioned
- [NVIDIA](../entities/nvidia.md) — Jetson mentioned as edge AI processor
- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — concept page

## Open questions
- No specific benchmarks cited with performance numbers — survey-level only
- VLM integration maturity in real UAV deployments unclear
- Swarm coordination protocols: which V2X standards specifically?
