---
title: "Taking Flight with Dialogue: Natural Language Control for PX4-based Drone Agent (Lim et al. 2025)"
type: source
url: https://arxiv.org/html/2506.07509v1
author: Shoon Kit Lim, Melissa Jia Ying Chong, Jing Huey Khor, Ting Yang Ling
published: 2025-06-09
ingested: 2026-06-14
local_path: null
venue: arXiv cs.RO (2506.07509v1)
license: n/a (arXiv preprint; code repo separately licensed)
format: arXiv HTML paper
tags: [uav, drone, agentic-uavs, px4, ros2, ollama, local-llm, vlm, jetson-orin-nano, isaac-sim, natural-language-control, llm-agent]
---

## Summary

An **open-source agentic framework for natural-language control of a PX4 drone**, built entirely on **locally-hosted models via [Ollama](../entities/ollama.md)** — no closed/cloud APIs. A [ROS 2](../entities/ros2.md) wrapper serves an LLM (turns dialogue into discrete flight commands) and a VLM (binary scene checks for mission-relevant objects), feeding a path-planning node that emits low-level **[PX4](../entities/px4-autopilot.md)** actions. Evaluated in **[NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)** SITL and on a custom quadcopter with an onboard **[Jetson Orin Nano](../entities/jetson-orin-nano.md)**. This is the wiki's first **concrete, fully-onboard, local-LLM instance** of the [agentic-UAV](../concepts/robotics/agentic-uavs.md) pattern that [Sapkota et al.'s survey](uavs-agentic-ai-survey.md) describes in the abstract — and it stress-tests the survey's assumption that heavy onboard VLM inference is impractical (it runs, but mission success tops out at **40%**). Code: [github.com/limshoonkit/ros2-agent-ws](https://github.com/limshoonkit/ros2-agent-ws).

## Key claims

- **Motivation:** democratize NL drone control — SOTA UAV vision-language systems rely on closed-source models accessible only to well-resourced orgs; this framework is open-source + locally-hosted.
- **Architecture:**
  - **ROS 2 wrapper encapsulates Ollama** to serve interchangeable LLMs and VLMs.
  - **LLM → discrete motion commands** (`Turn` / `Move` with constrained parameters), conditioned on context + recent command history.
  - **VLM → binary object presence** (mission-relevant scene understanding), run concurrently.
  - **Path-planning node** converts a goal point + current pose into a collision-free trajectory using low-level PX4 flight actions.
  - No explicit tool-calling / multi-step agent loop beyond LLM context + command-history conditioning.
- **Models benchmarked (all local via Ollama):**
  - **LLMs (command generation):** Gemma3 4B, Qwen2.5 3B, Llama-3.2 3B, DeepSeek-LLM 7B.
  - **VLMs (scene understanding):** Gemma3 12B, Llama3.2-Vision 11B, LLaVA 1.6 7B.
- **Hardware (custom quad):** [Jetson Orin Nano](../entities/jetson-orin-nano.md) Dev Kit (companion computer) + **Pixhawk 6c Mini** flight controller + **ZED Mini** stereo camera (visual-inertial odometry); ~0.56 m frame.
- **Simulation:** **PX4 SITL in [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)** (rendering + physics) with preset environments (outdoor car park, co-working spaces, hospitals, warehouses, data centers). *(Notable: PX4's own docs name Gazebo as the official sim; this work uses Isaac Sim instead.)*
- **Results:**
  - Best **mission success rate 40%** (Gemma3 as both LLM and VLM).
  - **Valid command generation:** Gemma3, Qwen2.5, Llama-3.2 all **100%**; **DeepSeek-LLM only 38%**.
  - **VLM valid binary responses 97–100%** across families.
  - **Strong association** between proportion of valid navigation commands and mission completion — command-format reliability, not perception, is the bottleneck.
  - No quantitative latency metrics reported.
- **Open-source:** source code, model configs, and prompt templates at `github.com/limshoonkit/ros2-agent-ws`.

## Entities mentioned

- [PX4 Autopilot](../entities/px4-autopilot.md) — flight stack (Offboard mode driven over ROS 2)
- [ROS 2](../entities/ros2.md) — middleware; wraps Ollama and bridges to PX4
- [Ollama](../entities/ollama.md) — local model-serving runtime for all LLMs/VLMs
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) — onboard companion computer
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) — SITL rendering + physics
- Pixhawk 6c Mini (flight controller); ZED Mini (VIO camera) — not yet entity pages
- [Gemma 3](../entities/gemma3.md) — named model option.

## Concepts touched

- [Agentic UAVs](../concepts/robotics/agentic-uavs.md) — concrete, fully-onboard, open-source instance of the perception/cognition/control stack.
- [LLM-agent architecture](../concepts/agents/llm-agent-architecture.md) — an **LLM-agent (not VLA)** instance: NL → discrete command tokens + VLM checks, the same pattern the wiki tracks on ground robots.
- **Local-LLM edge robotics** — Ollama-served sub-8B models doing real (if modestly reliable) onboard control; command-format validity as the limiting factor.

## Open questions

- **Why 40%?** The paper blames invalid command generation, but without latency/path-optimality numbers it's hard to separate language failures from control/planning failures.
- **NED/ENU + RGB8 frame/encoding mismatches** are flagged as live bugs — how much of the 60% failure is plumbing vs. reasoning?
- Authors' affiliations are not stated on the abstract/HTML page.
- Future work targets a **single end-to-end VLA under 1B params for edge** — would that beat the decomposed LLM+VLM+planner pipeline here?
