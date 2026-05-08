---
title: ROSOrin
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 2
tags: [rosorin, hiwonder, jetson-orin-nano, education, mobile-robot, llm-agent]
---

Educational mobile robot kit from [Hiwonder](hiwonder.md) built around a Jetson Orin Nano. Differential-drive (with Ackermann variant available); **no manipulator arm**. Designed as a teaching platform for ROS 2, Gazebo simulation, and agentic-AI applications.

## Hardware
- Compute: Jetson Orin Nano (also supports Jetson Nano, Jetson Orin NX, Raspberry Pi 5).
- Motion: differential-drive or Ackermann chassis; STM32 motor controller.
- Sensors: Aurora Depth Camera, monocular USB camera, LiDAR, 6-microphone circular array, IMU.
- Voice module: WonderEcho Pro with custom wake word "hello hiwonder."

## Software stack
- ROS 2 **Humble**.
- Workflow runs in an Ubuntu VM via VMware Workstation.
- Standard ROS 2 / Nav2 / Gazebo / RViz pipeline for SLAM + autonomous navigation.
- Vision: OpenCV + YOLOv11 + TensorRT for object detection (curriculum chapter 7).

## Agentic-AI curriculum
- **Cloud LLMs**: GPT-4o, GPT-4o-mini, [Qwen-plus-latest](qwen.md); StepFun multimodal as Chinese-language fallback.
- **Cloud speech**: Whisper-1, gpt-4o-transcribe, OpenAI TTS (tts-1, tts-1-hd, gpt-4o-mini-tts).
- **Offline stack**: [Ollama](ollama.md) running [qwen3:1.7b](qwen.md), plus sherpa-onnx for ASR + TTS (matcha-icefall, VITS).
- **Embodied AI** (chapter 10.3): same JSON tool-call pattern as [stretch_ai](stretch-ai.md) — LLM emits `{action: [...], response: ...}`, executor dispatches skill calls via `eval(f'self.{a}')`. Demos: real-time detection, vision tracking, smart home assistant.

## Why it matters
Concrete evidence that the **[LLM-agent architecture pattern](../concepts/llm-agent-architecture.md)** has reached the educational tier — a kit you can buy for a classroom now ships with both cloud and offline LLM-driven agent workflows. ROSOrin's `eval`-on-action-strings approach is a signal that the pattern is settling into a standard recipe across vendors.

## Related
- [Hiwonder](hiwonder.md) — vendor.
- [ROSOrin Pro](rosorin-pro.md) — manipulation-capable sibling kit (adds 6-DOF arm + [OpenClaw](openclaw.md) LLM-agent framework).
- [Stretch](stretch.md) — research-tier counterpart from [Hello Robot](hello-robot.md).
- [Ollama](ollama.md) / [Qwen](qwen.md) — local LLM stack used in chapter 10.5.
- [LLM-agent architecture](../concepts/llm-agent-architecture.md) — design pattern the curriculum implements.

## Mentioned in
- [Hiwonder ROSOrin Documentation](../sources/hiwonder-rosorin-docs.md)
- [Hiwonder ROSOrin Pro User Manual](../sources/hiwonder-rosorin-pro-user-manual.md)
