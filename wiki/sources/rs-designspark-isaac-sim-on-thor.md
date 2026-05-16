---
title: Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor (RS DesignSpark)
type: source
subtype: vendor-explainer
url: https://www.rs-online.com/designspark/isaacsim-and-isaaclab-on-nvidia-jetson-agx-thor
author: RS Components / DesignSpark
published: 2025
ingested: 2026-05-16
tags: [jetson-thor, isaac-sim, isaac-lab, rt-cores, training-vs-inference]
---

# Isaac Sim and Isaac Lab on NVIDIA Jetson AGX Thor

A vendor-side explainer that articulates the **single most important architectural constraint** on Jetson Thor: it has no RT cores, therefore Isaac Sim / Isaac Lab cannot run on it — even headless. The article also lays out NVIDIA's prescribed train-on-workstation, deploy-on-Thor workflow.

## Summary

Jetson Thor inherits the Jetson-family GPU lineage and, like every prior Jetson, omits dedicated ray-tracing hardware. Isaac Sim's renderer is built on the RTX pipeline and **requires RT cores even in headless mode**. The recommended workflow: train policies on an RTX workstation or data-centre GPU (e.g. DGX Spark, RTX 4090/5090), deploy the trained policy to Thor for real-time on-robot execution and hardware-in-the-loop validation.

## Key claims — verbatim

### What Thor lacks
> "Jetson Thor and other Jetson SoCs do not incorporate dedicated raytracing hardware."

The platform requires "GPUs with dedicated ray tracing (RT) cores," which Thor does not have.

### Headless mode does not help
Headless execution "still relies on the RTX rendering pipeline and therefore requires GPUs with dedicated ray tracing (RT) cores."

Consequently: "Isaac Sim is not supported on Jetson Thor or other Jetson devices."

### Recommended workflow (verbatim)
- **Training phase**: "Reinforcement learning pipelines (e.g., with Isaac Lab and RSL-RL) are executed on RTX-capable workstations or data centre GPUs."
- **Deployment phase**: "Trained policies are deployed to Jetson Thor for real-time execution, edge inference, and hardware-in-the-loop (HIL) validation."

The article recommends [NVIDIA DGX Spark](../entities/dgx-spark.md) for the training workstation specifically because its Blackwell GPU **does** include 4th-gen RT cores.

### Not addressed
- Isaac ROS compatibility on Thor (covered separately by Isaac ROS 4.0 release notes — Isaac ROS *is* supported on Thor; the constraint is on the simulator, not the ROS GEMs).
- Whether any Isaac Lab components (e.g. policy evaluation, dataset replay) can run on Thor without the renderer.

## Entities mentioned
- [Jetson Thor](../entities/jetson-thor.md)
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)
- [NVIDIA DGX Spark](../entities/dgx-spark.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- RT cores as a categorical hardware capability (present on workstation Blackwell GPUs, absent on Jetson SoC GPUs even when the SoC GPU is also Blackwell).
- Sim-to-real workflow architecture: simulate-and-train off-robot, deploy on-robot.

## Open questions
- Does Newton physics (the new default engine in Isaac Lab 3.0) carry the same RT-core dependency, or only the renderer?
- If a future Jetson generation added RT cores, would Isaac Sim immediately be on-Jetson capable, or are other constraints (e.g. memory bandwidth, Omniverse Kit footprint) gating?
