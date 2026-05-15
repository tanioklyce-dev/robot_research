---
title: NVIDIA GEAR Lab — Publications
type: source
url: https://research.nvidia.com/labs/gear/publications/
author: NVIDIA Research — GEAR Lab
published: continuously updated (extracted 2026-05-15)
ingested: 2026-05-15
tags: [nvidia, gear, embodied-ai, humanoids, world-models, vla, foundation-models, sim-to-real]
---

## Summary
The publications page for **NVIDIA GEAR** — Generalist Embodied Agent Research, co-led by [Jim Fan](../entities/jim-fan.md) and [Yuke Zhu](../entities/yuke-zhu.md). Built on Next.js as a single-page app; the publication list is hard-coded into the JS bundle. **32 unique publications** listed at extraction time, spanning Nov 2022 (MineDojo) through Aug 2026 (MotionBricks SIGGRAPH). Five papers are featured as Highlights at the top.

GEAR's research portfolio cleanly maps to four lab-stated focus areas:
1. **Multimodal foundation models** — VIMA, Prismer, Voyager, MineDojo.
2. **General-purpose robots** — GR00T N1, HOVER, SONIC, CHIP, ASAP, VIRAL, Doorman.
3. **Foundation agents** — Voyager, AMAGO, NitroGen, MineDojo.
4. **Simulation & synthetic data** — Isaac Lab, RoboCasa, MimicGen, DreamGen, MimicPlay, Sim-and-Real Co-Training, DrEureka, Eureka.

## Lab leadership
- **Jim Fan** — Director of Robotics, Distinguished Scientist; co-founded GEAR with Yuke Zhu in Feb 2024; also co-leads Project GR00T.
- **[Yuke Zhu](../entities/yuke-zhu.md)** — Director and Distinguished Research Scientist at NVIDIA; Associate Professor at UT Austin.

## Publications (chronological, newest first)

### Highlighted (top of page)
1. **DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos** — ICML 2026 (Spotlight). [arXiv 2602.06949](https://arxiv.org/abs/2602.06949) · [project](https://dreamdojo-world.github.io/) — **Ingested 2026-05-15**: see [DreamDojo Paper](dreamdojo-paper.md). Foundation generative-video world model trained on **44,711 hr** of egocentric human video (DreamDojo-HV — 96× more skills + 2,000× more scenes than the prior largest WM-pretraining corpus). Uses **continuous latent actions** as a self-supervised proxy for unlabeled video; built on Cosmos-Predict2.5 (2B + 14B variants). Self-Forcing distillation → **10.81 FPS** real-time autoregressive. The destination paper of the **Dream* triplet** (DreamGen → DreamZero → DreamDojo). New entities: [Fourier GR-1](../entities/fourier-gr-1.md), [Joel Jang](../entities/joel-jang.md).
2. **EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data** — arXiv 2602.16710 (Feb 2026). [paper](https://arxiv.org/abs/2602.16710) · [project](https://research.nvidia.com/labs/gear/egoscale/) — **Ingested 2026-05-15**: see [EgoScale Paper](egoscale-paper.md). Reports the first published VLA pretraining scaling law (`L = 0.024 − 0.003·ln(D)`, R² = 0.9983) on 20,854 hr of egocentric human video — the same corpus that underlies [GR00T N1.7](../entities/nvidia-groot.md). Seeded a new [Scaling laws — VLAs and human data](../concepts/scaling-laws-vla.md) concept page.
3. **DreamZero: World Action Models are Zero-shot Policies** — arXiv 2602.15922 (Feb 2026). [paper](https://arxiv.org/abs/2602.15922) · [project](https://dreamzero0.github.io/)
4. **SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control** — arXiv 2511.07820 (Nov 2025). [paper](https://arxiv.org/abs/2511.07820) · [project](https://nvlabs.github.io/GEAR-SONIC/) — Authors include Tingwu Wang, Olivier Dionne, Davis Rempe, Ye Yuan, Zhengyi Luo, Xue Bin Peng, Yuke Zhu.
5. **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** — arXiv 2503.14734 (Mar 2025). [paper](https://arxiv.org/abs/2503.14734) · [product page](https://developer.nvidia.com/isaac/gr00t) — Authors: Soroush Nasiriany, Abhiram Maddukuri*, Lance Zhang*, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, Yuke Zhu. Already cited via the [NVIDIA GR00T entity](../entities/nvidia-groot.md).

### 2026 venues (newest)
6. **MotionBricks: Scalable Real-Time Motions with Modular Latent Generative Model and Smart Primitives** — SIGGRAPH 2026 (Aug). [arXiv 2604.24833](https://arxiv.org/abs/2604.24833) · [project](https://nvlabs.github.io/motionbricks/)
7. **CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation** — ICML 2026 (Oral). [arXiv 2603.22435](https://arxiv.org/abs/2603.22435) · [project](https://capgym.github.io/)
8. **NitroGen: An Open Foundation Model for Generalist Gaming Agents** — CVPR 2026 (Oral). [arXiv 2601.02427](https://arxiv.org/abs/2601.02427) · [project](https://nitrogen.minedojo.org/) — Successor to MineDojo; "open foundation model for gaming agents".
9. **Opening the Sim-to-Real Door for Humanoid Pixel-to-Action Policy Transfer** ("Doorman") — CVPR 2026. [arXiv 2512.01061](https://arxiv.org/abs/2512.01061) · [project](https://doorman-humanoid.github.io/)
10. **VIRAL: Visual Sim-to-Real at Scale for Humanoid Loco-Manipulation** — CVPR 2026. [arXiv 2511.15200](https://arxiv.org/abs/2511.15200) · [project](https://viral-humanoid.github.io/)
11. **SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning** — ICRA 2026. [arXiv 2505.22626](https://arxiv.org/abs/2505.22626) · [project](https://ut-austin-rpl.github.io/SCIZOR/)
12. **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** — ICLR 2026. [arXiv 2511.00091](https://arxiv.org/abs/2511.00091) · [project](https://www.wenlixiao.com/self-improve-VLA-PLD)

### 2025 venues
13. **CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation** — arXiv 2512.14689 (Dec 2025). [paper](https://arxiv.org/abs/2512.14689) · [project](https://nvlabs.github.io/CHIP/)
14. **Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning** — arXiv 2511.04831 (Nov 2025). [paper](https://arxiv.org/abs/2511.04831) · [docs](https://isaac-sim.github.io/IsaacLab/main/index.html) — The canonical [Isaac Lab](../entities/nvidia-isaac-lab.md) reference paper.
15. **World Simulation with Video Foundation Models for Physical AI** — arXiv 2511.00062 (Oct 2025). [paper](https://arxiv.org/abs/2511.00062) · [project](https://research.nvidia.com/publication/2025-09_world-simulation-video-foundation-models-physical-ai)
16. **DreamGen: Unlocking Generalization in Robot Learning through Video World Models** — CoRL 2025 (Sep). [arXiv 2505.12705](https://arxiv.org/abs/2505.12705) · [project](https://research.nvidia.com/labs/gear/dreamgen/)
17. **FLARE: Robot Learning with Implicit World Modeling** — CoRL 2025. [arXiv 2505.15659](https://arxiv.org/abs/2505.15659) · [project](https://research.nvidia.com/labs/gear/flare/)
18. **Sim-to-Real Reinforcement Learning for Vision-Based Dexterous Manipulation on Humanoids** — CoRL 2025. [arXiv 2502.20396](https://arxiv.org/abs/2502.20396) · [project](https://toruowo.github.io/recipe/)
19. **ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills** — RSS 2025 (Jun). [arXiv 2502.01143](https://arxiv.org/abs/2502.01143) · [project](https://agile.human2humanoid.com/)
20. **Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation** — RSS 2025. [arXiv 2503.24361](https://arxiv.org/abs/2503.24361) · [project](https://co-training.github.io/)
21. **HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots** — ICRA 2025 (May). [arXiv 2410.21229](https://arxiv.org/abs/2410.21229) · [project](https://hover-versatile-humanoid.github.io/)
22. **Emergent Active Perception and Dexterity of Simulated Humanoids from Visual Reinforcement Learning** — arXiv 2505.12278 (May 2025). [paper](https://arxiv.org/abs/2505.12278) · [project](https://www.zhengyiluo.com/PDC-Site/)

### 2024 venues
23. **DrEureka: Language Model Guided Sim-To-Real Transfer** — RSS 2024 (Jul). [arXiv 2406.01967](https://arxiv.org/abs/2406.01967) · [project](https://eureka-research.github.io/dr-eureka/) — Awards: "Top 10 NVIDIA Research Highlights of 2023".
24. **RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots** — RSS 2024. [arXiv 2406.02523](https://arxiv.org/abs/2406.02523) · [project](https://robocasa.ai/) — Already cited via the [RoboCasa entity](../entities/robocasa.md). Awards: "Top 10 NVIDIA Research Highlights of 2023".
25. **Eureka: Human-Level Reward Design via Coding Large Language Models** — ICLR 2024 (May). [arXiv 2310.12931](https://arxiv.org/abs/2310.12931) · [project](https://eureka-research.github.io/) — Awards: "Top 10 NVIDIA Research Highlights of 2023".
26. **AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents** — ICLR 2024 (Spotlight). [arXiv 2310.09971](https://arxiv.org/abs/2310.09971) · [project](https://ut-austin-rpl.github.io/amago/)
27. **Prismer: A Vision-Language Model with Multi-Task Experts** — TMLR 2024. [arXiv 2303.02506](https://arxiv.org/abs/2303.02506) · [project](https://shikun.io/projects/prismer)
28. **Voyager: An Open-Ended Embodied Agent with Large Language Models** — TMLR 2024 (Mar). [arXiv 2305.16291](https://arxiv.org/abs/2305.16291) · [project](https://voyager.minedojo.org/) — Awards: "Best Paper Award Finalist".

### 2022–2023 venues (foundational)
29. **MimicPlay: Long-Horizon Imitation Learning by Watching Human Play** — CoRL 2023 (Nov). [arXiv 2302.12422](https://arxiv.org/abs/2302.12422) · [project](https://mimic-play.github.io/) — Award: "Best Paper Award Finalist".
30. **MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations** — CoRL 2023. [arXiv 2310.17596](https://arxiv.org/abs/2310.17596) · [project](https://mimicgen.github.io/) — Award: "Outstanding Paper Award". Underlies [MimicGen entity](../entities/mimicgen.md).
31. **VIMA: General Robot Manipulation with Multimodal Prompts** — ICML 2023 (Jul). [arXiv 2210.03094](https://arxiv.org/abs/2210.03094) · [project](https://vimalabs.github.io/) — Award: "Outstanding Paper Award".
32. **MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge** — NeurIPS 2022 (Nov). [arXiv 2206.08853](https://arxiv.org/abs/2206.08853) · [project](https://minedojo.org/) — Award: "Outstanding Paper Award". Jim Fan's signature pre-GEAR work.

## Lineage observations
- **The GR00T pillar.** GR00T N1 (Mar 2025) is the foundation-model anchor; SONIC (Nov 2025), CHIP (Dec 2025), HOVER (May 2025), ASAP (Jun 2025), Doorman (CVPR 2026), VIRAL (CVPR 2026) are the surrounding humanoid whole-body / sim-to-real family.
- **The Dream* world-model pillar (2025–2026).** DreamGen → DreamZero → DreamDojo is a clean three-paper progression from "video WM as data generator" to "world-action model as zero-shot policy" to "WM trained on large-scale human video". This is GEAR's bet on world-model-driven generalization, parallel to (and competing with) the FAIR JEPA program already heavily covered in the wiki.
- **The Eureka / DrEureka pillar (2023–2024).** LLM-as-reward-designer; one of the cleanest "LLM in the loop of sim-to-real" results. NVIDIA promoted both as top-10 research highlights.
- **The data / sim infrastructure pillar.** Isaac Lab (Nov 2025 paper), RoboCasa, MimicGen, MimicPlay, SCIZOR, Sim-and-Real Co-Training, EgoScale — half of the lab's output is *infrastructure for training other models*.
- **The agent pillar.** MineDojo → Voyager → AMAGO → NitroGen — Jim Fan's open-ended-agent line, now extended into "open foundation model for gaming agents" with NitroGen.

## Entities mentioned
- [NVIDIA](../entities/nvidia.md)
- [NVIDIA GEAR](../entities/nvidia-gear.md) — newly created with this ingest.
- [Jim Fan](../entities/jim-fan.md) — newly created with this ingest.
- [Yuke Zhu](../entities/yuke-zhu.md)
- [NVIDIA GR00T](../entities/nvidia-groot.md) (GR00T N1 paper)
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) (Isaac Lab 2025 paper)
- [RoboCasa](../entities/robocasa.md) (RoboCasa 2024 paper)
- [MimicGen](../entities/mimicgen.md) (MimicGen 2023 paper)

## Concepts touched
- Foundation models for embodied agents (VLA + humanoid whole-body control + open-ended agents)
- Sim-to-real transfer (ASAP, DrEureka, VIRAL, Doorman, Sim-and-Real Co-Training, dexterous-manipulation recipe)
- Video world models for robot learning (DreamGen / DreamZero / DreamDojo / FLARE / World Simulation paper)
- Synthetic-data generation (MimicGen, RoboCasa, EgoScale, SCIZOR)

## Open questions / candidates for individual ingest
The following are the highest-priority follow-up paper ingests, in rough order of payoff for the wiki's existing coverage:
- **DreamGen / DreamZero / DreamDojo (2025–2026)** — the GEAR world-model triplet; would substantially deepen the wiki's [world-model](../concepts/world-model.md) and [world-model-simulators](../concepts/world-model-simulators.md) coverage and provide a clean NVIDIA-side counterpoint to the FAIR JEPA program.
- **FLARE (CoRL 2025)** — "implicit world modeling" sits next to the JEPA / latent-WM family; potential cross-link with [LeWorldModel](leworldmodel-paper.md) / [DINO-WM](dino-wm-paper.md).
- **HOVER + SONIC + ASAP + Doorman + VIRAL** — the humanoid whole-body / pixel-to-action / sim-to-real cluster; a single synthesis page covering "GEAR's 2025–2026 humanoid stack" would be high-value.
- **Eureka + DrEureka (2023–2024)** — most-cited GEAR papers; LLM-as-reward-designer would seed a `concepts/llm-reward-design.md` hub.
- **MineDojo / Voyager / NitroGen** — Jim Fan's open-ended-agent line; would seed a `concepts/open-ended-agents.md` hub and an embodied-agents-in-Minecraft thread distinct from the wiki's robotics-only focus.
- **Isaac Lab paper (Nov 2025)** — primary reference for the [Isaac Lab](../entities/nvidia-isaac-lab.md) entity; currently sourced only from blog posts.
- **EgoScale / SCIZOR** — egocentric-video data scaling and self-supervised data curation; both nearby to [DROID](../entities/droid.md) and the imitation-learning thread.
- **Author-graph follow-up**: Tingwu Wang, Davis Rempe, Zhengyi Luo, Xue Bin Peng (SONIC), Soroush Nasiriany, Ajay Mandlekar (GR00T N1) all warrant entity stubs once their papers are individually ingested.
