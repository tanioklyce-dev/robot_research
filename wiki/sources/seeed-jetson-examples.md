---
title: Seeed jetson-examples (repo + reComputer runner)
type: source
url: https://github.com/Seeed-Projects/jetson-examples
author: Seeed Studio (Seeed-Projects)
published: 2024-06-24
ingested: 2026-06-14
local_path: null
venue: GitHub (Seeed-Projects/jetson-examples)
license: MIT
format: GitHub repository (README + per-recipe scripts)
tags: [seeed-studio, jetson, recomputer, jetson-containers, docker, edge-ai, llm, vlm, vision, robotics, one-command-deploy]
---

## Summary

**`jetson-examples`** is Seeed Studio's open-source (MIT) catalog of **one-line deployments** for vision-AI and generative-AI models on NVIDIA Jetson. After `pip3 install jetson-examples`, a single command — **`reComputer run <example>`** — pulls/builds the right Docker container for the host's JetPack/L4T and launches a working demo (LLM chat, VLM, object detection, depth, pose, image/audio generation, ROS, 3D mapping). It is the "buy-the-carrier, run-one-command" front door to the Jetson AI software stack, sitting **on top of [jetson-containers](../entities/jetson-containers.md)** and optimized for Seeed's [reComputer](../entities/seeed-studio.md) J-series boxes. 264★ / 40 forks; created 2024-06-24, actively maintained (last push 2026-06-11). The [nvblox recipe](seeed-jetson-examples-nvblox.md) is ingested separately as a sub-recipe deep-dive.

## Key claims

- **Install / run / clean:**
  ```sh
  pip3 install jetson-examples            # or: pip3 install jetson-examples --upgrade
  reComputer run <example>                # download/build container + launch demo
  reComputer clean <example>              # tear down
  ```
- **Mechanism:** each `<example>` is a directory under `reComputer/scripts/<name>/` with a setup/launch script that wraps the heavy container plumbing. The runner is the entity [`reComputer`](../entities/jetson-examples.md); the heavy lifting (image selection/build for aarch64 + CUDA/TensorRT alignment) leans on **[jetson-containers](../entities/jetson-containers.md)** (`dustynv/*` images, `autotag`).
- **Hardware target:** NVIDIA Jetson (Orin family especially), packaged commercially as Seeed **reComputer** carriers. JetPack coverage spans **JetPack 4.6 → 7.1** depending on the recipe.
- **License:** MIT. **Contribution bounty:** Seeed advertises a **$250 cash bonus** for accepted new examples (`edgeai@seeed.cc` / PR).

### Recipe catalog (37 examples, by category)

> Names below are the literal `reComputer/scripts/<dir>` recipe slugs as of 2026-06-11.

- **LLM serving / chat:** `llama3`, `llama3.2`, `gemma4`, `qwen3.5-4b`, `qwen3.6-35b`, `nemotron-3-nano`, `gpt-oss`, `Sheared-LLaMA-2.7B-ShareGPT`, `ollama`, `text-generation-webui`
- **LLM fine-tuning:** `llama-factory`
- **VLM / multimodal:** `llava`, `llava-v1.5-7b`, `llava-v1.6-vicuna-7b`, `live-llava`, `live-vlm-webui`
- **Object detection / vision:** `ultralytics-yolo`, `yolo11`, `yolo26`, `yolov10`, `yolov8-rail-inspection` (applied), `nanoowl` (open-vocabulary/zero-shot detection), `nanodb` (vector DB for semantic image/video search)
- **Monocular depth:** `depth-anything`, `depth-anything-v2`, `depth-anything-v3`
- **Pose estimation:** `MoveNet-Lightning`, `MoveNet-Thunder`, `MoveNetJS`
- **Image generation:** `comfyui`, `stable-diffusion-webui`
- **Audio:** `whisper` (ASR), `parler-tts` (TTS), `audiocraft` (music/audio generation)
- **Robotics / 3D:** `ros1-jp6` (ROS1 Noetic containerized on JetPack 6), `nvblox` ([Isaac ROS](../entities/nvblox.md) GPU 3D mapping — see [dedicated recipe page](seeed-jetson-examples-nvblox.md))
- **Other:** `deep-live-cam` (real-time face swap)

## Entities mentioned

- [jetson-examples / reComputer runner](../entities/jetson-examples.md) (this repo's tool)
- [Seeed Studio](../entities/seeed-studio.md) — publisher; reComputer hardware
- [jetson-containers](../entities/jetson-containers.md) — underlying container framework
- [Isaac ROS NVBlox](../entities/nvblox.md) / [Isaac ROS](../entities/isaac-ros.md) — `nvblox` recipe
- [Orbbec](../entities/orbbec.md) — RGB-D camera used by the `nvblox` demo
- [JetPack](../entities/jetpack.md) — version-pinned per recipe
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) / [Jetson Thor](../entities/jetson-thor.md) — Jetson family context
- [Ollama](../entities/ollama.md) — one of the LLM-serving recipes
- [Ultralytics YOLO](../entities/ultralytics-yolo.md) — upstream of the `ultralytics-yolo` / `yolo11` / `yolo26` / `yolov10` recipes

## Concepts touched

- **One-command edge-AI deployment** — abstracting Docker + JetPack/L4T + CUDA/TensorRT version-matching behind `reComputer run`, the consumer-friendly layer above [jetson-containers](../entities/jetson-containers.md).
- **The aarch64 dependency problem** — why a curated container catalog matters on Jetson (no pip-installing CUDA-aligned wheels by hand).
- Breadth of the on-device model menu: LLMs/VLMs, detection/depth/pose, gen-AI (image/audio), and robotics (ROS1, 3D mapping) all runnable on a single Orin box.

## Open questions

- Which recipes are realistic on **Orin Nano 8 GB** vs needing **NX 16 GB / AGX**? `qwen3.6-35b` and `nemotron-3-nano` (30B-class) imply large-memory tiers; the README doesn't publish a per-recipe RAM/tier matrix.
- How tightly are recipes pinned to specific `dustynv/*` tags, and how stale do they get as upstream models churn (e.g. is `llama3` current)?
- Is `ros1-jp6` (ROS1 Noetic) a bridge for legacy stacks only, or does Seeed maintain a ROS 2 path elsewhere?
