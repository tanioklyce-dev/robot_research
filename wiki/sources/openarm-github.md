---
title: "OpenArm GitHub (enactic/OpenArm) — README and repository family"
type: source
url: https://github.com/enactic/OpenArm
local_path: raw/2026-09-13-openarm-github-readme.md
sha256: f558aa83d81fd35061d5add981dd7e16b35b5d89618d3ad7400f8c5f74218bb2
author: "Enactic, Inc."
published: 2024-09-29
venue: "GitHub; the umbrella repo carries the docs site and issues, code lives in sibling repos"
format: repository README + API metadata
github_stats: "3,038 stars, 350 forks, 16 open issues, Apache-2.0, created 2024-09-29, pushed 2026-09-09 (captured 2026-09-13)"
latest_release: "1.1 (2025-10-31) on this repo; openarm_hardware 2.0.0 (2026-09-09)"
tags: [openarm, enactic, github, open-hardware, ros2, dora, isaac-lab, mujoco, cern-ohl, apache-2]
ingested: 2026-09-13
---

# OpenArm GitHub (enactic/OpenArm)

## Summary

The umbrella repository for [OpenArm](../entities/openarm.md): a README, code of conduct, and the Docusaurus source of [docs.openarm.dev](openarm-docs.md); the code and CAD are spread across sibling repos. Description: *"A fully open-source humanoid arm for physical AI research and deployment in contact-rich environments."* **3,038 stars and 350 forks** on 2026-09-13 for a repo created 2024-09-29 — the CAD repo alone has 515 — which puts it in the same public-attention band as the wiki's other open low-cost arms and well above any other 7-DOF open design here. Topics tagged: bilateral teleoperation, force feedback, gravity compensation, Genesis, MuJoCo, MoveIt 2, ROS 2, imitation and reinforcement learning.

The README states the positioning and the price: *"human-scale proportions, safety and compliance, and practical payloads. At $6,500 USD for a complete bimanual system…"* and introduces the **OpenArm Cell** as *"a standardized environment with unified background, lighting, and camera placement"* so that *"research performed using OpenArm can be reproduced around the world in consistent evaluation conditions."*

## Repository family (README table, stars at capture)

| Repo | License | Stars | Content |
|---|---|---|---|
| openarm_hardware | **CERN-OHL-S-2.0** | 515 | STL, STEP, Fusion 360; releases 1.0.0 (2025-07-23) → 1.1.0 (2025-11-19) → **2.0.0 (2026-09-09)** |
| openarm_description | Apache-2.0 | 44 | URDF/xacro |
| openarm_can | Apache-2.0 | 64 | CAN control library |
| openarm_ros2 | Apache-2.0 | 114 | ROS 2 packages (last push 2026-06-29) |
| openarm_teleop | Apache-2.0 | 45 | unilateral + bilateral teleop |
| openarm_isaac_lab | Apache-2.0 | 115 | Isaac Lab environments (last push 2026-02-18) |
| openarm_mujoco | Apache-2.0 | 59 | MJCF assets |
| openarm_dataset | Apache-2.0 | — | dataset format, recorder, Python API |
| dora-openarm | Apache-2.0 | — | Dora nodes for collection, inference, teleop |

Releases on the umbrella repo: 0.1 (2025-02-19), 0.2 (2025-04-04), 0.3 (2025-05-08), 1.1 *"OpenArm 01: Release No.2"* (2025-10-31). The Enactic GitHub organization (created 2025-05-16, location Japan) has 51 public repos, including the `dora-openarm-*` node family and the Damiao datasheet site.

## Why it matters in this wiki

- The **hardware is strong-copyleft (CERN-OHL-S)** while the software is permissive — the same split as [SO-ARM101](../entities/so-arm101.md)'s ecosystem, and the reason a manufacturer directory rather than a single vendor is the distribution model.
- The star count is a rough proxy for the design having become the default open 7-DOF arm above the SO-101 tier, which is what the [UME](../entities/ume.md) and [Yuri](../entities/yuri.md) sightings suggested.
- Activity is uneven: the Isaac Lab repo has not been pushed since February 2026 while hardware and MuJoCo moved this month.

## Entities mentioned

[OpenArm](../entities/openarm.md) · [Enactic](../entities/enactic.md) · [WowRobo](../entities/wowrobo.md) · [Damiao](../entities/damiao.md) · [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) · [MuJoCo](../entities/mujoco.md)

## Concepts touched

[Imitation learning](../concepts/learning/imitation-learning.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions

- Genesis is a topic tag; no Genesis assets are listed in the README or docs.
- Contributor count and commit velocity per repo — not pulled.
