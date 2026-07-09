---
title: NVIDIA and Hugging Face Bring New Models and Frameworks to LeRobot (NVIDIA blog)
type: source
url: https://blogs.nvidia.com/blog/hugging-face-lerobot-models-frameworks-open-robotics/
author: Sasa Docca (NVIDIA)
published: 2026-07-06
ingested: 2026-07-08
format: web (corporate blog)
tags: [nvidia, hugging-face, lerobot, gr00t, cosmos, isaac-teleop, isaac-lab-arena, envhub, reachy-2, jetson-thor, open-source, partnership]
---

# NVIDIA and Hugging Face Bring New Models and Frameworks to LeRobot (NVIDIA blog)

## Summary

NVIDIA's corporate-blog umbrella announcement of the NVIDIA ↔ [Hugging Face](../entities/hugging-face.md) [LeRobot](../entities/lerobot.md) partnership — published 2026-07-06, the day before the more technical [HF blog](nvidia-isaac-teleop-gr00t17-lerobot-blog.md) this wiki ingested first. Framing: connect "NVIDIA's 3 million robotics developers with Hugging Face's 16 million AI builders" through shared models, datasets, and standardized workflows. Beyond the two items the HF blog detailed ([GR00T](../entities/nvidia-groot.md) 1.7 in LeRobot, [Isaac Teleop](../entities/nvidia-isaac-teleop.md)), this post adds three integrations the wiki hadn't recorded: **[Cosmos 3](../entities/nvidia-cosmos.md) coming to LeRobot "soon"**, **Isaac Lab-Arena environments registrable in the LeRobot Environment Hub (EnvHub)**, and **[Jetson Thor](../entities/jetson-thor.md) integration with [Reachy 2](../entities/reachy.md)** for VLA deployment on open-source humanoids.

## Key claims

- **GR00T 1.7 in LeRobot** — branded here "the first open and commercially viable robot foundation model" (the [HF blog](nvidia-isaac-teleop-gr00t17-lerobot-blog.md) says "latest"); post-train/deploy through LeRobot workflows with "benchmarked performance."
- **[Isaac Teleop](../entities/nvidia-isaac-teleop.md)** — open-source data-collection framework; "high-quality human demonstrations from external devices using standardized, interoperable formats."
- **[Cosmos 3](../entities/nvidia-cosmos.md) → LeRobot, "soon"** — the frontier world model will "generate and augment robotics data, simulate scenarios and support policy development when real-world data is limited or too expensive to collect." No date, no scope details.
- **Isaac Lab-Arena ↔ LeRobot EnvHub** — developers "prototype complex simulation environments, register them in LeRobot EnvHub and seamlessly use them within the LeRobot ecosystem to train and evaluate generalist robot policies such as GR00T, Pi and SmolVLA." First wiki sighting of **EnvHub** as a named LeRobot component.
- **[Jetson Thor](../entities/jetson-thor.md) + [Reachy 2](../entities/reachy.md)** — Thor integration with LeRobot's Reachy 2 "to support deployment of VLA models on open source humanoid robots." One sentence; no technical detail.
- **Dataset scale claim** — NVIDIA's open physical-AI data: "largest open source physical AI dataset," 15M+ downloads, **350,000+ real and simulated trajectories, 57 million grasps** (no formal dataset name given).
- **Community scale** — 3M NVIDIA robotics developers; 16M Hugging Face AI builders.
- Quote (Thomas Wolf, HF cofounder & chief science officer): "Open source is how a field turns advanced research into something people can study, adapt and build on."

> [!note] Relation to the HF blog (2026-07-07)
> Same announcement wave, different altitude: this corporate post is the breadth view (five integrations, ecosystem stats); the [HF blog](nvidia-isaac-teleop-gr00t17-lerobot-blog.md) is the depth view (install commands, LIBERO numbers, fine-tune recipe). The "first" vs "latest" open-commercial-VLA phrasing difference is marketing drift, not a factual conflict.

## Entities mentioned

- [LeRobot](../entities/lerobot.md), [Hugging Face](../entities/hugging-face.md), [NVIDIA](../entities/nvidia.md)
- [NVIDIA GR00T](../entities/nvidia-groot.md) 1.7, [NVIDIA Isaac Teleop](../entities/nvidia-isaac-teleop.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md) 3
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md), [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md) (Lab-Arena)
- [Jetson Thor](../entities/jetson-thor.md), [Reachy 2](../entities/reachy.md) ([Pollen Robotics](../entities/pollen-robotics.md))
- π ([Physical Intelligence](../entities/physical-intelligence.md)), [SmolVLA](../entities/smolvla.md) — named as EnvHub-evaluable policies

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — open VLA deploy path (Thor + Reachy 2).
- [World models](../concepts/world-models/world-model.md) — Cosmos 3 as data generator/augmenter for policy training.

## Open questions

- **Cosmos 3-in-LeRobot**: timeline, which variant (Nano 16B? Edge 4B?), and what the integration surface is (data-gen API? policy type like `groot`?).
- **LeRobot EnvHub** — new named component; scope/docs not yet ingested (relation to the ICLR paper's sim-eval story?).
- **Isaac Lab-Arena** details — only a one-line description existed in the wiki before this ([Isaac Lab](../entities/nvidia-isaac-lab.md)); the developer page (developer.nvidia.com/isaac/lab-arena) is a candidate ingest.
- **Thor + Reachy 2** — what the "integration" concretely is (a reference image? carrier support? a LeRobot plugin?).
- Which HF dataset(s) the 350k-trajectory / 57M-grasp claim refers to (likely the GR00T/PhysicalAI collections; unnamed in the post).
