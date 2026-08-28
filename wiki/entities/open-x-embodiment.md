---
title: Open X-Embodiment (OXE)
type: entity
subtype: dataset
created: 2026-05-25
updated: 2026-08-27
sources: 25
tags: [open-x-embodiment, oxe, dataset, cross-embodiment, robot-data, rt-x, levine, finn]
status: stub
---

> [!note] Stub entity
> Filed 2026-05-25 during lint (15 mentions across 9 wiki files). Primary source — O'Neill et al. 2024 ([arXiv 2310.08864](https://arxiv.org/abs/2310.08864), "Open X-Embodiment: Robotic Learning Datasets and RT-X Models") — **not yet ingested**; deepen when filed.

**Open X-Embodiment (OXE)** — the **largest open cross-embodiment robot-learning dataset** to date. Aggregated by a 35+-institution consortium ("Open X-Embodiment Collaboration") and released alongside the **RT-X** generalist policies (Oct 2023; revised through 2024). Standardized format across **22 robot embodiments and ~500 skills**, totaling **~1M+ trajectories** at original release; subsequent expansions push higher. The de-facto open pretraining corpus for cross-embodiment VLA work.

## What we know via the wiki's existing references

- **Standardized embodiment-tagged format**: each trajectory carries its robot embodiment tag so policies can be trained jointly across hardware.
- **Used as a training-data component by**:
  - [π0](pi-zero.md) (10,000 hr in-house teleop + **OXE** + DROID + Bridge).
  - [π0.7](pi07.md), [π*0.6](pistar06.md) (heterogeneous data mixture including OXE).
  - [Octo](octo.md) (trained from scratch on OXE; ~800K trajectories from this corpus).
  - [OpenVLA](openvla.md) (cross-embodiment-pretrained on OXE).
  - [GR00T N1](nvidia-groot.md) — OXE constituents (RT-1 338.4 h, Bridge-v2 111.1 h, Language Table 195.7 h, [DROID](droid.md) 428.3 h, MUTEX, RoboSet, Plex) form part of the 3,288.8 h real-robot layer of its data pyramid ([GR00T N1 Paper](../sources/groot-n1-paper.md)).
- **Includes [DROID](droid.md)** as one of its constituent datasets — the wiki's primary OXE-component entity.
- **Successor lineage**: OXE → RT-X → DROID → larger open robot corpora. OXE is the umbrella; DROID is the single-embodiment standardized Franka subset most commonly used.

## Why it matters in this wiki

- **The pretraining corpus for almost every cross-embodiment VLA** the wiki tracks. Filing closes 15 mentions across 9 files and converts the "trained on OXE" mention into an entity link.
- **The umbrella relationship** with [DROID](droid.md) is worth being explicit about: the wiki has had DROID filed for a while; OXE was the more frequently referenced parent.

## Related

- [DROID](droid.md) — constituent single-embodiment dataset; the Franka-Panda subset.
- [π0](pi-zero.md), [π0.7](pi07.md), [π*0.6](pistar06.md), [Octo](octo.md), [OpenVLA](openvla.md) — VLAs trained on OXE.
- [Sergey Levine](sergey-levine.md), [Chelsea Finn](chelsea-finn.md), [Karl Pertsch](karl-pertsch.md) — co-organizers.
- [VLA models](../concepts/learning/vla-models.md) — broader concept.

## Code & data

- Project page: https://robotics-transformer-x.github.io
- Paper: https://arxiv.org/abs/2310.08864
- Hosted on Google Cloud Storage (links from project page).

## Open questions

- **Primary source not yet ingested.** When the O'Neill et al. paper lands, deepen with: full embodiment list, skill taxonomy, license, and the RT-1-X / RT-2-X model results.
- **RT-1, RT-2, RT-X** — generalist policies bundled with OXE; not directly ingested as entities.
- **Open X-Embodiment v2** — referenced in 2025 papers; expanded corpus.
- **Bridge** dataset — co-cited with OXE in π0's training mix; also not ingested.

## Mentioned in

- [A Careful Examination of Large Behavior Models for Multitask Dexterous Manipulation (TRI LBM paper)](../sources/tri-lbm-paper.md)
- [awesome-physical-ai (GitHub curated list)](../sources/awesome-physical-ai-github.md)
- [DreamGen — Unlocking Generalization in Robot Learning through Video World Models (paper)](../sources/dreamgen-paper.md)
- [DROID — A Large-Scale In-The-Wild Robot Manipulation Dataset (paper)](../sources/droid-paper.md)
- [Fine-Tuning Vision-Language-Action Models — Optimizing Speed and Success (OpenVLA-OFT, Kim et al. 2025)](../sources/openvla-oft-paper.md)
- [FLARE — Robot Learning with Implicit World Modeling (paper)](../sources/flare-paper.md)
- [Flexion Reflect v0 — Towards Generalizable Robot Autonomy (Nov 2025)](../sources/flexion-reflect-v0.md)
- [From Demonstrations to Safe Deployment: Path-Consistent Safety Filtering for Diffusion Policies (PACS)](../sources/pacs-paper.md)
- [Gemini Robotics 1.5 — Pushing the Frontier of Generalist Robots with Embodied Reasoning, Thinking, and Motion Transfer (tech report)](../sources/gemini-robotics-1-5-report.md)
- [GR00T N1 — An Open Foundation Model for Generalist Humanoid Robots (paper)](../sources/groot-n1-paper.md)
- [GR00T N1.5 — Research Page (NVIDIA GEAR)](../sources/groot-n1_5.md)
- [HAI Issue Brief — The World Model and Spatial Intelligence Era: Governing AI Beyond Language](../sources/hai-world-model-spatial-intelligence-brief.md)
- [Isaac-GR00T GitHub (NVIDIA/Isaac-GR00T)](../sources/isaac-gr00t-github.md)
- [LeRobot: An Open-Source Library for End-to-End Robot Learning (Cadene et al., ICLR 2026)](../sources/lerobot-iclr-2026-paper.md)
- [MolmoAct: Action Reasoning Models that can Reason in Space](../sources/molmoact-paper.md)
- [Reinforcement Learning in Robotics — A Survey (Kober, Bagnell & Peters, IJRR 2013)](../sources/kober-rl-robotics-survey-2013.md)
- [RoboMIND: Benchmark on Multi-embodiment Intelligence Normative Data for Robot Manipulation (Wu, Hou, Liu, Che, Ju et al., Dec 2024)](../sources/robomind-paper.md)
- [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation (Chen et al., Jun 2025)](../sources/robotwin2-paper.md)
- [RT-1: Robotics Transformer for Real-World Control at Scale](../sources/rt-1-paper.md)
- [RT-H: Action Hierarchies Using Language](../sources/rt-h-paper.md)
- [Safe, Task-Consistent Manipulation with Operational Space Control Barrier Functions (OSCBF)](../sources/oscbf-paper.md)
- [The State of Robot Motion Generation (Bekris et al., 2024)](../sources/state-of-robot-motion-generation-2024.md)
- [π0 Paper — A Vision-Language-Action Flow Model for General Robot Control (Black et al., Physical Intelligence, 2024)](../sources/pi-zero-paper.md)
- [π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities (Physical Intelligence, 2025)](../sources/pi07-paper.md)
- [Introducing Index (Figure AI)](../sources/figure-index-announcement.md) — Scale anchor: OXE's ~1,150 h share of the [TRI LBM](../sources/tri-lbm-paper.md) mix against [Index](figure-index.md)'s claimed daily ingest.
