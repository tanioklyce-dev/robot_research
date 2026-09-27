---
title: BotBrain (BotBot)
type: entity
subtype: software-framework
created: 2026-09-27
updated: 2026-09-27
sources: 1
tags: [botbrain, botbot, ros2, humble, jetson, realsense, nav2, rtab-map, teleoperation, web-ui, fleet, quadruped, humanoid, unitree-go2, unitree-g1, rosa, open-hardware, mit]
---

**BotBrain** — an MIT-licensed, open-source **bolt-on "brain box"** for legged and wheeled [ROS 2](ros2.md) robots from **BotBot**, a Brazilian robotics company: a 3D-printed enclosure with a Jetson and two RealSense D435i cameras, a ROS 2 Humble autonomy stack (RTAB-Map + [Nav2](nav2.md)), and a browser dashboard for teleop, missions and fleets ([BotBrain GitHub](../sources/botbrain-github.md)).

## What it is

| Layer | Contents |
|---|---|
| Hardware | Snap-fit PLA enclosure; NVIDIA Jetson (**Nano / Orin Nano** official; AGX and Thor "coming soon"); **2× Intel RealSense D435i**; robot-specific mounts |
| Robot stack | ROS 2 **Humble** on **JetPack 6.2**, Dockerized; [RTAB-Map](rtab-map.md) visual SLAM, [Nav2](nav2.md), lifecycle state machine, `twist_mux` priority arbitration, YOLO (TensorRT), per-robot drivers |
| UI | Next.js 15 / React 19 dashboard over rosbridge; Supabase auth; cockpit, custom layouts, missions, health, fleet, audit log |
| Language | `bot_rosa` — NASA JPL's ROSA agent (LangChain) with per-robot tools; defaults to OpenAI GPT-4o |

**Supported robots**: [Unitree Go2](unitree-go2.md) / Go2-W, [Unitree G1](unitree-g1.md), DirectDrive Tita; custom robots via a documented package template.

## Why it is interesting

- **It fills the layer between the locomotion controller and the task.** Unitree ships walking; BotBrain adds seeing, mapping, going places and a fleet UI. That is the same seam [AgenticROS](agenticros.md) targets from the agent side, and the one the wiki's [fleet framework](../syntheses/projects/fleet-agentic-framework.md) analysis sits in. BotBrain takes a conventional stack (SLAM + Nav2 + web UI) and gets the packaging right: hardware, installer and dashboard in one repo.
- **The LLM goes at the bottom of the priority ladder.** Velocity arbitration is *joystick > nav > AI*, behind a dead-man switch and e-stop. It is a simple, legible answer to the [guardrails](../syntheses/agents/guardrails-for-robot-agents.md) question: the language model can suggest motion and can never override a human or the planner.
- **Open-core business model.** The open edition leads to **BotBrain Pro**: IP67, thermal/IR and 30× zoom payloads, LoRa, 4G/5G, service contracts. It is the security-patrol quadruped market, entered from the software side.

## Limits (as of 2026-09-27)

- **Pinned to the old stack**: ROS 2 Humble / Ubuntu 22.04 / JetPack 6.2 — the [Isaac ROS](isaac-ros.md) 3.2 era. No Jazzy/Lyrical or JetPack 7.2 path documented.
- **Quiet repo**: last commit 2026-05-18; no releases.
- **No learned policies**: navigation is classical. There is no VLA, no manipulation, no data recording for learning.
- **"Any bot" means any bot that already exposes a velocity interface.**

## Related

- [AgenticROS](agenticros.md) — agent↔ROS 2 bridge; complementary layer.
- [Nav2](nav2.md) · [RTAB-Map](rtab-map.md) — the autonomy core.
- [Unitree Go2](unitree-go2.md) · [Unitree G1](unitree-g1.md) — the primary targets.

## Mentioned in

- [BotBrain GitHub](../sources/botbrain-github.md) — primary source.
