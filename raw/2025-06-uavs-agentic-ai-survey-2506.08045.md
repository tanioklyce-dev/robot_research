---
source_url: https://arxiv.org/html/2506.08045v1
collected: 2026-05-09
published: 2025-06 (submitted)
author: Ranjan Sapkota, Konstantinos I. Roumeliotis, Manoj Karkee
affiliation: Cornell University (Biological and Environmental Engineering); University of the Peloponnese (Informatics and Telecommunications)
arxiv: 2506.08045
---

# UAVs Meet Agentic AI: A Multidomain Survey of Autonomous Aerial Intelligence and Agentic UAVs

## Abstract
Comprehensive synthesis of agentic UAVs — autonomous aerial systems integrating "perception, decision-making, memory, and collaborative planning" to operate adaptively in complex environments. Covers seven+ application domains.

## Definition of agentic UAVs
Distinguishes from traditional UAVs by "goal-driven behavior, contextual reasoning, and interactive autonomy."

## Four-layer architecture
1. **Perception**: Multimodal sensing (RGB, thermal, LiDAR, hyperspectral)
2. **Cognition**: Reinforcement learning, task decomposition, affordance reasoning
3. **Control**: MPC and neural policy networks for trajectory execution
4. **Communication**: V2X protocols for swarm coordination

## Key enabling technologies
- Edge AI processors: NVIDIA Jetson, Intel Movidius
- Multimodal sensor fusion
- Vision-Language Models (Flamingo, LLaVA) for natural-language instruction execution

## Application domains (8)
| Domain | Key capabilities |
|---|---|
| Precision agriculture | Real-time crop health, adaptive spraying, seeding |
| Disaster response / SAR | SLAM, thermal survivor detection, swarm coordination |
| Environmental monitoring | Ecosystem surveillance, air/water quality |
| Urban infrastructure | Bridge/facade inspection, defect classification, 3D mapping |
| Logistics | GPS-denied navigation, semantic landing zone detection |
| Defense / security | Perimeter surveillance, threat detection, multi-agent |
| Wildlife conservation | Non-invasive tracking, anti-poaching, habitat mapping |
| Construction / mining | BIM integration, autonomous surveying, stockpile monitoring |

## Traditional vs. agentic comparison (15 dimensions)
- Traditional: rule-based, single modality, static waypoints, operator-dependent, Levels 1–2 autonomy
- Agentic: learned policies, multimodal fusion, dynamic goal planning, minimal human oversight, Levels 4–5

## Mathematical formalism
o_t = Φ(s_t): sensor inputs → semantic representations via neural encoders

## Technical challenges
- Power/compute tradeoff on edge hardware
- Real-time inference latency (τ_c < δ ≈ 100ms)
- GPS-denied navigation reliability
- Sensor fusion scalability
- Regulatory: airspace integration, decision transparency, safety certification, data privacy

## Future directions
1. Self-evolving aerial ecosystems with continuous learning
2. UAV + IoT + ground robot + cloud integration
3. Sustainable/equitable deployment
4. Standardized multi-agent communication protocols

## Case study
Wheat field chlorosis detection: traditional UAV executes fixed path + post-flight analysis; agentic UAV performs real-time NDVI analysis, detects stress zones, replans routes, issues irrigation commands autonomously.
