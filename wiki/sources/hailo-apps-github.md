---
title: "hailo-apps (hailo-ai/hailo-apps GitHub)"
type: source
url: https://github.com/hailo-ai/hailo-apps
author: Hailo (hailo-ai)
published: 2026-04-13
ingested: 2026-06-07
tags: [hailo, edge-ai, npu, llm, vlm, gstreamer, hailort, raspberry-pi, xlerobot, software]
license: MIT
format: github repo
---

# hailo-apps (hailo-ai/hailo-apps)

## Summary

[Hailo](../entities/hailo.md)'s official application repository: **"High-performance AI applications for Hailo accelerators, including GStreamer pipelines, GenAI assistants, and standalone C++/Python apps."** It is the software the [Raspberry Pi AI HAT+ 2](raspberry-pi-ai-hat-plus-2.md) product page points to for generative-AI workloads, and the practical on-device starting point for both the vision (Hailo-8/8L) and GenAI (Hailo-10H) lines. **MIT-licensed**; 412★ / 143 forks; latest release **26.03.1 (2026-04-13)**; Python 67.7% / C++ 25.3%.

## Key claims

- **Supported accelerators**: **Hailo-8, Hailo-8L, Hailo-10H** — one repo spans both the vision-CNN chips and the GenAI chip.
- **Supported platforms**: **Raspberry Pi 5**, Ubuntu (x86_64), and **Windows** (Windows support new in v26.03.0).
- **30+ ready-to-run applications**, in three categories:
  | Category | Purpose | Path |
  |---|---|---|
  | **GenAI Apps** | "LLM/VLM/speech workflows on **Hailo-10H**" | `hailo_apps/python/gen_ai_apps/` |
  | **Pipeline Apps** | Real-time camera / RTSP / video processing | `hailo_apps/python/pipeline_apps/` |
  | **Standalone Apps** | Minimal HailoRT-only apps (learning / minimal installs) | `hailo_apps/python/standalone_apps/` + `hailo_apps/cpp/` |
- **Vision examples**: object detection, pose estimation, instance segmentation, depth estimation, tiling. **YOLO26 model support** new in v26.03.0.
- **GenAI examples**: a **Voice2Action** demo (v26.03.0) and an AI-generated "Easter Eggs" game. The page does **not** name specific LLMs/VLMs (no Llama/Qwen called out).
- **CLI entrypoints** (after `source setup_env.sh`): `hailo-detect-simple`, `hailo-pose`, `hailo-seg`, `hailo-depth`, `hailo-tiling`.
- **Software stack / deps**:
  - Core: **HailoRT PCIe driver (.deb)**, **HailoRT (.deb)**, **HailoRT Python binding (.whl)**.
  - Optional (for GStreamer pipelines): **TAPPAS Core (.deb)** + its Python binding. Standalone and GenAI apps can skip TAPPAS via `--no-tappas-required`.
- **Install**:
  ```bash
  git clone https://github.com/hailo-ai/hailo-apps.git
  cd hailo-apps
  sudo ./install.sh
  source setup_env.sh
  ```
- **"AI-Powered Development" (Beta)**: an agent feature — **"Just describe your idea and the agent builds, validates, and runs it for you,"** supporting VLM / LLM / pipeline / standalone app types; the "Easter Eggs" game is cited as "built autonomously by AI." (Does **not** name Claude/agents/skill files on the page.)

> [!note] Not on the page
> Specific supported LLM/VLM model names, Python/OS version floors, tokens/sec, and the model-download mechanism (Hailo Model Zoo → HEF) are not stated in the README excerpt. The GenAI apps are explicitly **Hailo-10H-only**.

## Relevance to this wiki — XLeRobot

This repo is the concrete answer to "what runs on the [AI HAT+ 2](raspberry-pi-ai-hat-plus-2.md) on a Pi 5." For an [XLeRobot](../entities/xlerobot.md) Pi-5 host it supplies, out of the box:
- **Onboard vision** (detection/pose/seg/depth) that can ground the robot's LLM-agent perception tools.
- An **onboard LLM/VLM/speech layer** (`gen_ai_apps`, Hailo-10H) — a local alternative to XLeRobot's stock cloud Gemini agent.

It does **not** provide a way to run LeRobot control policies (ACT/Diffusion/SmolVLA/π0.5) — those aren't Hailo apps; see [Hailo](../entities/hailo.md) and the [NPU-vs-Jetson synthesis](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md).

## Entities mentioned
- [Hailo](../entities/hailo.md) — repo author / accelerator vendor.
- [Raspberry Pi 5](../entities/raspberry-pi-5.md) — primary edge platform.
- [XLeRobot](../entities/xlerobot.md) — candidate deployment platform.

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — onboard LLM/VLM/Voice2Action; the agent "build-validate-run" dev feature.
- [VLA models](../concepts/learning/vla-models.md) — what this stack does *not* run (robot control policies).

## Open questions
- Which LLMs/VLMs ship in `gen_ai_apps`, and at what tokens/sec on the Hailo-10H?
- Does Voice2Action's "action" layer expose a tool/function-call interface usable as a robot agent backend?
- What harness does "AI-Powered Development" use under the hood (cf. the AI-first FRC workflows in [Team 4414](team-4414-hightide-2026-binder.md) / [Team 254](team-254-ai-in-frc-presentation.md))?
