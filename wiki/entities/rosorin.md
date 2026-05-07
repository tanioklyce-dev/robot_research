---
title: ROSOrin
type: entity
subtype: product
created: 2026-05-07
updated: 2026-05-07
sources: 1
tags: [rosorin, hiwonder, jetson-orin-nano, education, mobile-robot, llm-agent]
---

Educational mobile robot kit from [[hiwonder|Hiwonder]] built around a Jetson Orin Nano. Differential-drive (with Ackermann variant available); **no manipulator arm**. Designed as a teaching platform for ROS 2, Gazebo simulation, and agentic-AI applications.

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
- **Cloud LLMs**: GPT-4o, GPT-4o-mini, [[qwen|Qwen-plus-latest]]; StepFun multimodal as Chinese-language fallback.
- **Cloud speech**: Whisper-1, gpt-4o-transcribe, OpenAI TTS (tts-1, tts-1-hd, gpt-4o-mini-tts).
- **Offline stack**: [[ollama|Ollama]] running [[qwen|qwen3:1.7b]], plus sherpa-onnx for ASR + TTS (matcha-icefall, VITS).
- **Embodied AI** (chapter 10.3): same JSON tool-call pattern as [[stretch-ai|stretch_ai]] — LLM emits `{action: [...], response: ...}`, executor dispatches skill calls via `eval(f'self.{a}')`. Demos: real-time detection, vision tracking, smart home assistant.

## Why it matters
Concrete evidence that the **[[llm-agent-architecture|LLM-agent architecture pattern]]** has reached the educational tier — a kit you can buy for a classroom now ships with both cloud and offline LLM-driven agent workflows. ROSOrin's `eval`-on-action-strings approach is a signal that the pattern is settling into a standard recipe across vendors.

## Related
- [[hiwonder|Hiwonder]] — vendor.
- [[stretch|Stretch]] — research-tier counterpart from [[hello-robot|Hello Robot]].
- [[ollama|Ollama]] / [[qwen|Qwen]] — local LLM stack used in chapter 10.5.
- [[llm-agent-architecture|LLM-agent architecture]] — design pattern the curriculum implements.

## Mentioned in
- [[hiwonder-rosorin-docs|Hiwonder ROSOrin Documentation]]
