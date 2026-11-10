---
title: "R²D²: Scaling Multimodal Robot Learning with NVIDIA Isaac Lab"
type: source
url: https://developer.nvidia.com/blog/r2d2-scaling-multimodal-robot-learning-with-nvidia-isaac-lab/
author: "Oyindamola Omotuyi (NVIDIA)"
published: 2026-02-10
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, isaac-lab, simulation, gpu-simulation, throughput, multimodal, sim-to-real, adopters]
ingested: 2026-11-10
---

# R²D²: Scaling Multimodal Robot Learning with NVIDIA Isaac Lab

## Summary

An overview and quick-start for [Isaac Lab](../entities/nvidia-isaac-lab.md): its modular configuration, sensors, throughput figures, a four-step train-and-deploy example for the Unitree H1, and named adopters.

> [!note] Vendor product post
> The throughput figures come with no hardware specification, so they can't be compared with other benchmarks.

## Key claims

- **Design.** Separate managers for observations, actions, rewards and events, procedural scene and terrain generation, and import from USD, URDF or MJCF. It offers actuator models, over 10 sensor types including tiled RTX cameras, and a built-in teleoperation stack.
- **Throughput.** **135,000 FPS** for H1 humanoid locomotion and **over 150,000 FPS** for Franka cabinet manipulation, maintained with RGB-D sensors across 4,096 environments. The GPU used isn't stated.
- **Libraries.** SKRL, RSL-RL, RL-Games, SB3 and Ray, through the Gymnasium interface. Policies export to ONNX or TorchScript.
- **Adopters.** Agility Robotics (Digit whole-body control), [Skild AI](../entities/skild-ai.md), FieldAI, the Robotics and AI Institute (Spot, Atlas and its UMV), and Under Control Robotics (Moby).

## Entities mentioned

- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md), [Skild AI](../entities/skild-ai.md), [Boston Dynamics](../entities/boston-dynamics.md)

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) — the deployment step.

## Open questions

- **On what GPU** were 135,000 and 150,000 FPS measured?
