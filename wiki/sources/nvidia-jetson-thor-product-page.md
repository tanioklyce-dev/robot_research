---
title: NVIDIA Jetson Thor product page
type: source
subtype: vendor-page
url: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
author: NVIDIA
published: 2025
ingested: 2026-05-16
tags: [jetson, thor, blackwell, physical-ai, robotics-compute]
---

# NVIDIA Jetson Thor product page

NVIDIA's official product page for the Jetson Thor edge-AI compute module — the Blackwell-generation successor to [Jetson Orin Nano](../entities/jetson-orin-nano.md) / AGX Orin, positioned as "the ultimate platform for physical AI and robotics."

## Summary

Jetson Thor ships in two SoM SKUs (T5000 and T4000) plus an AGX-style Developer Kit. Both modules use a Blackwell GPU with 5th-gen Tensor Cores, an ARM Neoverse-V3AE CPU, 256-bit LPDDR5X at 273 GB/s, and target the **40–130 W** envelope (T5000) / **40–70 W** envelope (T4000). NVIDIA's headline claim: **7.5× higher AI compute than AGX Orin, 3.5× better energy efficiency**.

## Key claims

### Jetson T5000 module — verbatim
| Spec | Value |
|---|---|
| GPU | 2560-core NVIDIA Blackwell architecture GPU with 5th-gen Tensor Cores |
| CPU | 14-core Arm Neoverse-V3AE 64-bit |
| Memory | 128 GB, 256-bit LPDDR5X |
| Memory bandwidth | 273 GB/s |
| AI performance | 2070 TFLOPS (FP4 — Sparse) |
| Power | 40 W – 130 W |

### Jetson T4000 module — verbatim
| Spec | Value |
|---|---|
| GPU | 1536-core NVIDIA Blackwell architecture GPU |
| CPU | 12-core Arm Neoverse-V3AE 64-bit |
| Memory | 64 GB, 256-bit LPDDR5X |
| Memory bandwidth | 273 GB/s |
| AI performance | 1200 TFLOPS (FP4 — Sparse) |
| Power | 40 W – 70 W |

### Software stack referenced
The page lists the full **NVIDIA Isaac** platform — [Isaac GR00T](../entities/nvidia-groot.md), Isaac ROS, [Isaac Sim](../entities/nvidia-isaac-sim.md), [Isaac Lab](../entities/nvidia-isaac-lab.md) — alongside NVIDIA Holoscan and the [JetPack SDK](../entities/jetpack.md). The page does **not** disclaim the well-known constraint that Isaac Sim itself cannot execute on Thor (no RT cores) — see [Isaac Sim and Isaac Lab on Jetson AGX Thor — RS DesignSpark](rs-designspark-isaac-sim-on-thor.md).

### Positioning
> "The ultimate platform for physical AI and robotics."

> "7.5× higher AI compute than NVIDIA AGX Orin, with 3.5× better energy efficiency."

Virtual Incision (surgical robotics) is the workload example NVIDIA features on the page.

## Entities mentioned
- [Jetson Thor](../entities/jetson-thor.md)
- [JetPack SDK](../entities/jetpack.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)
- [NVIDIA GR00T](../entities/nvidia-groot.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- Physical AI / on-robot inference vs off-robot training (see [Jetson Thor vs DGX Spark](../syntheses/platforms/jetson-thor-vs-dgx-spark.md)).

## Open questions
- T5000 vs T4000 pricing for production modules (page does not list).
- Detailed FP8 / INT8 / FP16 / FP32 throughput numbers beyond the FP4-sparse headline.
- Specific JetPack 7 versions and Isaac ROS GA dates supported at module ship.
