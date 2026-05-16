---
title: Hiwonder ROSOrin Documentation
type: source
url: https://docs.hiwonder.com/projects/ROSOrin/en/jetson-orin-nano-version/
author: Hiwonder
published: 2024-2025
ingested: 2026-05-07
tags: [hiwonder, rosorin, jetson-orin-nano, ros2, education, gazebo, ollama, qwen]
---

## Summary
Sphinx documentation site for [Hiwonder](../entities/hiwonder.md)'s **[ROSOrin](../entities/rosorin.md)** educational robot kit on a [Jetson Orin Nano](../entities/jetson-orin-nano.md) compute platform. Covers the full curriculum: hardware setup, ROS 2 (Humble) basics, mapping/navigation, perception (OpenCV + YOLOv11 + TensorRT), Gazebo simulation, and "Large AI Model Courses" with both cloud (GPT-4o, [Qwen](../entities/qwen.md), StepFun) and offline ([Ollama](../entities/ollama.md) + [Qwen](../entities/qwen.md) + sherpa-onnx) flavors. The Embodied AI section uses the same JSON tool-call [LLM-agent pattern](../concepts/agents/llm-agent-architecture.md) as [stretch_ai](../entities/stretch-ai.md).

## Key claims

### Hardware
- Mobile differential-drive base (Ackermann variant available); **no manipulator arm**.
- Compute: Jetson Orin Nano (also supports Jetson Nano, Jetson Orin NX, Raspberry Pi 5).
- Sensors: Aurora Depth Camera, monocular USB camera, LiDAR, 6-microphone circular array, IMU.
- Voice module: WonderEcho Pro with custom-flashed wake word "hello hiwonder."

### Software stack
- ROS 2 **Humble** (`ros-humble-urdf`, `ros-humble-xacro`).
- STM32 microcontroller for motor control.
- Workflow runs in an Ubuntu VM via VMware Workstation (per chapter 9.1).
- ROS packages live under `/home/ubuntu/ros2_ws/src/robot_gazebo/`.

### Chapter 9 — Gazebo simulation
- URDF/xacro models with sensor plugins for LiDAR + IMU.
- Two world files: `worlds.launch.py` (basic) and `room_worlds.launch.py` (mapped environment for SLAM/nav).
- Workflow:
  - `ros2 launch robot_gazebo worlds.launch.py` — launch sim
  - `ros2 launch robot_gazebo slam.launch.py` — start SLAM
  - `ros2 run robot_gazebo teleop_key_control` — teleop while mapping
  - `ros2 run nav2_map_server map_saver_cli` — save map
  - `ros2 launch robot_gazebo navigation.launch.py map:=map_01` — Nav2 with saved map
- Standard ROS 2 / Gazebo + Nav2 + RViz "2D Pose Estimate" / "2D Nav Goal" workflow.
- **Gazebo version not explicitly stated** in visible content (likely Gazebo Classic given the ROS 2 Humble pairing, but unconfirmed).

### Chapter 10 — Large AI Model Courses

**Cloud-based (10.1–10.4):**
- LLMs: **GPT-4o**, **GPT-4o-mini**, **gpt-4o-transcribe** (ASR), **Whisper-1**, **Qwen-plus-latest**.
- TTS: **tts-1**, **tts-1-hd**, **gpt-4o-mini-tts** (voices: nova, shimmer, echo, onyx, fable, alloy, ash, sage, coral).
- VLM: GPT-4V via OpenAI API; **StepFun's `stepfun_vllm_model`** when `ASR_LANGUAGE=Chinese` (Chinese-language fallback path).
- API providers: OpenAI direct + OpenRouter.
- API setup requires registering, getting a key, and charging tokens via Billing.

**Offline (10.5):**
- LLM runtime: **[Ollama](../entities/ollama.md)** (`ollama serve` starts the local server).
- Local LLM model: **`qwen3:1.7b`** (small enough for Jetson Orin Nano).
- Speech stack: **sherpa-onnx** with CUDA acceleration (`provider="cuda"`).
- Offline TTS models: **`matcha-icefall-zh-baker`** (Chinese), **`vits-ljs`** (English VITS).
- Tasks demonstrated: speech-to-text, text-to-speech, LLM Q&A, semantic understanding (NLU), emotion perception, voice-controlled movement, autonomous line following, color tracking — all **on-device**.
- Client class pattern: `client = speech.OllamaAPI(ollama_host)` → `client.llm_origin(...)` / `client.llm_multi_turn(...)`.

### Embodied AI (10.3) — LLM-agent pattern
Same architecture as [stretch_ai](../entities/stretch-ai.md):
- LLM is given a goal + tool-call schema.
- LLM emits structured JSON: `{action: [...], response: "..."}`.
- Executor invokes skill methods named in `action` array via `eval(f'self.{a}')` — **Python `eval` on LLM output**, security-questionable but typical for educational demos.
- Skills include `move(...)`, `vision(query)`, plus chassis motion control. The `vision` method routes to either OpenAI VLM or StepFun VLM based on language.
- Demos covered: real-time detection, vision tracking, smart home assistant.

### Other notable chapters
- Chapter 6: color recognition, QR code detection, autonomous patrolling.
- Chapter 7 (ROS+ML): MediaPipe for human-robot interaction, **YOLOv11 + TensorRT** for object detection (with optional model training), traffic-sign training, autonomous-driving applications.
- Chapter 8: voice interaction (WonderEcho Pro install + 6-mic configuration).

## Entities mentioned
- [Hiwonder](../entities/hiwonder.md)
- [ROSOrin](../entities/rosorin.md)
- [Ollama](../entities/ollama.md)
- [Qwen](../entities/qwen.md)
- [stretch_ai](../entities/stretch-ai.md) — referenced for the parallel LLM-agent pattern.

## Concepts touched
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — same JSON tool-call pattern as stretch_ai, here extended to a fully offline variant via Ollama + sherpa-onnx.
- Mobile robotics (no entity for the concept yet — bare text).

## Open questions
- Specific Gazebo version — Classic vs. Garden vs. Harmonic? Docs never say.
- Is the simulation a digital twin of the physical ROSOrin, or generic differential-drive?
- Privacy: cloud demos send video/audio to OpenAI / OpenRouter — no discussion in docs.
- StepFun deserves its own coverage — Chinese multimodal AI provider, not stubbed yet.
- No VLA work surfaced — Embodied AI is strictly LLM-agent, not VLA. Confirms the bifurcation already noted in the synthesis.
