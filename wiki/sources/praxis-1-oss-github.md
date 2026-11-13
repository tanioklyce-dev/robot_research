---
title: "runwayml/praxis-1-oss — Praxis-1 inference and fine-tuning code (GitHub README)"
type: source
url: https://github.com/runwayml/praxis-1-oss
fetch_url: https://raw.githubusercontent.com/runwayml/praxis-1-oss/main/README.md
local_path: raw/2026-11-11-praxis-1-oss-readme.md
sha256: 5e021f501d5b4925c5e131368e37ab9fca7e3ca5f1a8c10f7a1ecb2b9211fc60
author: Runway
published: 2026-11-11
venue: GitHub repository (Apache-2.0)
format: README (1,332 lines)
license: Apache-2.0
tags: [praxis-1, runway, open-weights, apache-2, nvfp4, jetson-thor, rtx-5090, h100, b200, so-101, lerobot, droid, yam, lora, policy-server, websocket, mujoco]
ingested: 2026-11-12
---

## Summary

**The deployment facts for [Praxis-1](../entities/praxis-1.md), which are more conservative than the launch post.** The repository holds PyTorch inference code, a WebSocket policy server, a MuJoCo simulation of the DROID setup, and fine-tuning instructions (full fine-tune of `praxis-1-base`, and LoRA on `praxis-1-droid`). Released checkpoints: `praxis-1-droid`, `praxis-1-yam`, `praxis-1-so101`, an **NVFP4 version of each**, and the base mid-trained model. The quick start needs **one CUDA GPU with at least 80 GB, the CUDA 13.0 driver and Python 3.12**. It installs pinned torch 2.13, flash-attn-4 and a compiled `causal-conv1d`, and downloads the Wan2.2 VAE and Qwen3.5-2B separately. A fresh clone took **17 minutes to first numbers** on an H100.

## Key claims

- **Memory and GPUs.** In bf16 the policy is **54.4 GB**. NVFP4 on the routed experts brings it to **17.5 GB**, or **about 23.5 GB** including the text encoder (4.6 GB) and VAE (1.4 GB). *"A 32 GB RTX 5090 **should fit (the peak is not measured yet)** and a 24 GB GPU does not."* The text encoder must sit on the policy GPU.
- **Precision by architecture.** H100 runs **bf16 only**, and an NVFP4 request raises an error there. NVFP4 is supported on SM100/SM103 (B200, B300), SM120 (RTX 5090) and **SM110 (Jetson Thor)**. Thor has its own NVFP4 backend and a set of Thor-only kernel options, which shows real engineering on that part. No Thor latency figure appears in the sections read.
- **Latency on one H100**, DROID checkpoint, synthetic inputs, server-side p50: **about 500 ms per call** with video CFG 4 and about 344 ms with guidance off. The first call of a process takes **35 s** while kernels compile. **A robot client against a hosted server saw a median of 1.1–1.4 s per call** in RoboLab runs. The README warns that real camera frames may give different times, because MoE routing depends on the tokens.
- **Determinism.** Kernel optimizations are documented as bit-identical to the reference path where stated. For example, commands were bit-identical with and without the last-step video decoder across 90 calls.
- **SO-100/SO-101 setup.** The SO-101 checkpoint uses a 6-D joint-space head (5 joints in radians relative to the start of the chunk, plus absolute gripper 0..1) at 15 Hz. It takes one or two cameras, each fit to 416×416 tiles, so a 640×480 camera gives a 288×416 tile. It follows LeRobot 0.7 `SOFollower` conventions with `use_degrees=True`. Server config is `configs/serve_so101.yaml` and the on-robot client is `demo/so101/so101_client.py`. **The robot does not run the model**: the arm is a client of a GPU server.

> [!note] What "runs on Jetson Thor" means here
> The code has a dedicated SM110 path, so the launch post's Thor claim is not just marketing. But the README states its latency numbers for H100 only. A 128 GB Thor holds the bf16 model in memory. Whether it can serve a 1.6 s chunk in under 1.6 s is not stated in the sections read. Measure it with `python -m praxis.serve.latency` before planning around on-robot inference.

## Entities mentioned

[Runway](../entities/runway.md) · [Praxis-1](../entities/praxis-1.md) · [Jetson Thor](../entities/jetson-thor.md) · [LeRobot](../entities/lerobot.md) · [DROID](../entities/droid.md) · [YAM](../entities/yam.md) · [Qwen](../entities/qwen.md)

## Concepts touched

[World-action model](../concepts/world-models/world-action-model.md) · [Mixture of experts](../concepts/learning/mixture-of-experts.md)

## Open questions

- Thor latency per call in bf16 and in NVFP4.
- Peak memory on RTX 5090. The README says it is unmeasured.
- Fine-tuning hardware for LoRA is "one 80 GB GPU". There is no path stated for smaller cards.
