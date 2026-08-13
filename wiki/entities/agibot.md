---
title: AGIBOT
type: entity
subtype: company
created: 2026-05-06
updated: 2026-08-13
sources: 10
tags: [agibot, china, embodied-ai, humanoid]
---

Shanghai-based embodied-AI and humanoid-robotics company (full name: AGIBOT Innovation (Shanghai) Technology Co., Ltd.). Maintains an open simulation stack including [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) and the world-model simulator [Genie Envisioner](genie-envisioner.md).

## What we know
- **Simulation stack**: launched [AGIBOT Genie Sim 3.0](agibot-genie-sim.md) open source at CES 2026 ([AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)).
- **World model**: maintains [Genie Envisioner](genie-envisioner.md) / GE-Sim2 ([AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md), [Genie Envisioner Paper](../sources/genie-envisioner-paper.md)).
- **Hardware**: humanoid robot lineup (introduced alongside Genie Sim 3.0 at CES 2026).
- **Open-source posture**: ships datasets and evaluation code on GitHub.
- **AgiBot World Colosseo / AGIBOT-Beta** (Bu et al., arXiv 2503.06669) is the **single largest component of [X-VLA](x-vla.md)'s pretraining mixture — 48.8% of 290 K episodes**, recorded at 30 Hz with head + wrist cameras on AGIBOT's own bimanual platform ([X-VLA paper](../sources/xvla-paper.md), Fig. 3). This is the wiki's clearest evidence of AGIBOT data flowing into a non-AGIBOT SOTA model: nearly half of what X-VLA learned about cross-embodiment manipulation came from AGIBOT hardware.

## Why it matters
One of the most active publishers of open embodied-AI infrastructure in 2026 — and a counterweight to the NVIDIA-centric Western stack.

## Related
- [X-VLA](x-vla.md) — trained 48.8% on AgiBot-Beta episodes.
- [AGIBOT Genie Sim 3.0](agibot-genie-sim.md), [Genie Envisioner](genie-envisioner.md) — flagship products.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — substrate Genie Sim runs on.
- [NVIDIA Cosmos](nvidia-cosmos.md) — underlying model for GE-Sim2.

## Mentioned in
- [X-VLA paper](../sources/xvla-paper.md)
- [AGIBOT Genie Sim 3.0 Announcement](../sources/agibot-genie-sim-3-announcement.md)
- [AGIBOT Genie Envisioner 2.0 Announcement](../sources/agibot-genie-envisioner-2-announcement.md)
- [Genie Envisioner Paper](../sources/genie-envisioner-paper.md)
- [CaP-X paper](../sources/cap-x-paper.md) — AgiBot G1 used for zero-shot real-world CaP-Agent0 demos alongside the [Franka Panda](franka-panda.md); required "single arm to bimanual control primitive modifications."
