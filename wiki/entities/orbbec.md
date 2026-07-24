---
title: Orbbec (Gemini2)
type: entity
subtype: hardware-vendor
created: 2026-06-13
updated: 2026-06-13
sources: 2
tags: [orbbec, rgb-d, depth-camera, perception, sensor, realsense-alternative]
---

**Orbbec** — depth-camera vendor; its **Gemini2** is an RGB-D camera used as the depth source in NVIDIA/Seeed robot-perception demos. In this wiki, the Orbbec Gemini2 is the assumed sensor for the Seeed [nvblox](nvblox.md) 3D-mapping recipe ([Seeed jetson-examples nvblox README](../sources/seeed-jetson-examples-nvblox.md)).

## Why it matters here

Orbbec is a practical **alternative to the Intel RealSense** line for RGB-D / depth sensing on Jetson robots. Upstream NVIDIA Isaac ROS nvblox examples often assume RealSense; the Seeed recipe instead targets the **Gemini2** (or compatible Orbbec RGB-D device). Relevant to the wiki's depth-camera discussion in [XLeRobot low-light camera options](../syntheses/projects/xlerobot-camera-options-low-light.md).

## Related

- [Isaac ROS NVBlox (nvblox)](nvblox.md) — consumes Gemini2 depth.
- [Seeed Studio](seeed-studio.md) — distributes the recipe + hardware.

## Mentioned in

- [Seeed jetson-examples — nvblox recipe (README)](../sources/seeed-jetson-examples-nvblox.md)
