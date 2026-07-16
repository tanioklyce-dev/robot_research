---
title: "NVIDIA GR00T End-to-End Workflow (Physical AI course docs)"
type: source
url: https://docs.nvidia.com/learning/physical-ai/gr00t-e2e-workflow/latest/index.html
author: NVIDIA
published: 2026 (rolling docs)
ingested: 2026-07-15
format: documentation / course
tags: [groot, nvidia, unitree-g1, jetson-thor, isaac-lab-arena, isaac-teleop, agile, lerobot, isaac-ros, sim-to-real, teleoperation, deployment, pick-and-place]
---

# NVIDIA GR00T End-to-End Workflow (Physical AI course docs)

## Summary

NVIDIA's **end-to-end course/workflow** for developing and deploying a humanoid manipulation policy with **[GR00T](../entities/nvidia-groot.md)** on the **[Unitree G1](../entities/unitree-g1.md)**. It walks the full loop — **teleoperation → data collection → policy fine-tuning → evaluation → deployment** — down **two independent paths**: a **simulation path** (entirely in **Isaac Lab-Arena**, ~3–6 h) and a **real-robot path** (physical data collection + deployment via **[Jetson Thor](../entities/jetson-thor.md)**, ~3–6 h). Target task: **tabletop pick-and-place** (active balance + apple grasp + place on plate — perception, grasping, and whole-body coordination in one). This is the concrete first-party recipe behind the [pinball-playing-robot project](../syntheses/projects/pinball-playing-robot.md)'s GR00T plan, which links to it directly.

## Key claims

**Software stack (named components)**
- **Isaac Lab-Arena** — the simulation environment for the sim path.
- **[Isaac Teleop](../entities/nvidia-isaac-teleop.md)** — teleoperation system, "with **AGILE**" (i.e. the [WBC-AGILE](wbc-agile-github.md) whole-body-control engine underneath the teleop/loco layer).
- **[GR00T 1.7](../entities/nvidia-groot.md)** — the VLA used for post-training.
- **[LeRobot](../entities/lerobot.md)** — dataset format for training.
- **[Isaac ROS](../entities/isaac-ros.md)** — real-robot integration.

**Data formats**: collect via teleoperation in **HDF5 (sim) or MCAP (real)**, then convert to **LeRobot format** for GR00T post-training.

**Hardware**: [Unitree G1](../entities/unitree-g1.md) robot; [Jetson Thor](../entities/jetson-thor.md) for real-robot deployment; Isaac Lab-Arena for sim.

**Structure (navigation)**
- **Getting Started** — Concepts, Agents, Prerequisites.
- **Simulation Workflow** — seven subsections (setup → evaluation).
- **Real Robot Workflow** — nine subsections, **including safety and deployment**.
- **Conclusion & Resources**.

## Entities mentioned

- [NVIDIA GR00T](../entities/nvidia-groot.md) (1.7), [Unitree G1](../entities/unitree-g1.md), [Jetson Thor](../entities/jetson-thor.md), [Isaac Teleop](../entities/nvidia-isaac-teleop.md), [Isaac ROS](../entities/isaac-ros.md), [LeRobot](../entities/lerobot.md), [Isaac Lab](../entities/nvidia-isaac-lab.md) (Arena).

## Concepts touched

- Sim-vs-real **two-path** teleop→train→deploy loop; [whole-body control](../concepts/robotics/whole-body-control.md) (via Isaac Teleop + AGILE); [VLA models](../concepts/learning/vla-models.md) post-training.

## Open questions

- The docs pair GR00T-VLA manipulation with an AGILE whole-body/loco layer under teleop — how tightly is [WBC-AGILE](wbc-agile-github.md) wired into Isaac Teleop vs. a separate install?
- Safety guidance is a listed subsection but not detailed here (the [pinball project](../syntheses/projects/pinball-playing-robot.md) notes sim-validation + e-stop + classical-control fallback as the working answer).
