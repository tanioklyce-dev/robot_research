---
title: jetson-containers
type: entity
subtype: software-framework
created: 2026-06-13
updated: 2026-06-13
sources: 2
tags: [jetson, nvidia, docker, edge-ai, jetson-containers, dustynv, infrastructure, lerobot]
---

# jetson-containers

**jetson-containers** — an open-source framework (originated by **Dustin Franklin**, NVIDIA) for **building and running Docker container images on NVIDIA Jetson** (aarch64 / L4T) hardware. It maintains a large catalog of prebuilt, dependency-resolved containers (PyTorch, CUDA, TensorRT, LLM/VLM stacks, robot-learning stacks) published under the **`dustynv/*`** namespace on Docker Hub, and ships helper scripts — notably **`autotag`** (selects the correct image tag for the host's JetPack/L4T version) and **`run.sh`** (wraps `docker run` with the right device, display, and volume flags for Jetson). It is the de-facto deployment substrate behind the **NVIDIA Jetson AI Lab** tutorials.

## Why it matters in this wiki

It is the **operational answer to "the aarch64 dependency problem"** for edge robot-learning: pulling a `dustynv/*` image sidesteps building CUDA/PyTorch/TensorRT-aligned wheels for ARM by hand. In this wiki it appears as the deployment mechanism for the [NVIDIA Jetson AI Lab LeRobot tutorial](../sources/nvidia-jetson-ai-lab-lerobot.md), which runs **[LeRobot](lerobot.md)** on Jetson via the `dustynv/lerobot` container + `autotag`. It is infrastructure, not a robot — relevant wherever the wiki discusses getting a learning stack onto [Jetson Orin Nano](jetson-orin-nano.md) / AGX Orin / Orin NX silicon.

## Key facts

- **Image registry:** `dustynv/*` on Docker Hub (e.g. `dustynv/lerobot`).
- **Helpers:** `autotag <name>` resolves a host-appropriate tag; `run.sh` wraps `docker run` with Jetson-appropriate device/volume/display flags (used as `./run.sh … $(./autotag lerobot)`).
- **Versioning:** images are pinned to L4T / JetPack lines (the LeRobot tutorial targets JetPack 6 GA = L4T r36.3 and JetPack 6.1 = r36.4).
- **Scope:** broad catalog beyond LeRobot — LLM/VLM serving, vision, ROS, etc. (only the LeRobot container is ingested so far).
- **Maintainer:** Dustin Franklin (NVIDIA); the same lineage behind the Jetson AI Lab documentation site.

## Related

- [jetson-examples](jetson-examples.md) — Seeed's one-command `reComputer run` recipe catalog built on top of jetson-containers.
- [LeRobot](lerobot.md) — packaged as `dustynv/lerobot`.
- [Jetson Orin Nano](jetson-orin-nano.md) — typical target module.
- [NVIDIA](nvidia.md) — sponsor / publisher of Jetson AI Lab.
- [NVIDIA Brev](nvidia-brev.md) — adjacent NVIDIA "get-a-stack-running-fast" tooling, but cloud-GPU rather than edge-container.

## Open questions

- Current maintenance state and whether the `dustynv/lerobot` image tracks upstream LeRobot's post-refactor CLI (the ingested tutorial is archived). See [source page](../sources/nvidia-jetson-ai-lab-lerobot.md) open questions.

## Mentioned in

- [NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived tutorial)](../sources/nvidia-jetson-ai-lab-lerobot.md) — uses `dustynv/lerobot` + `autotag` to run LeRobot on Jetson.
- [Seeed jetson-examples (repo + reComputer runner)](../sources/seeed-jetson-examples.md) — `reComputer run` recipes wrap jetson-containers images.
