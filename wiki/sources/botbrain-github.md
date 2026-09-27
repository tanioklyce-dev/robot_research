---
title: "BotBrain Open Source (botbotrobotics/BotBrain) — GitHub README"
type: source
url: https://github.com/botbotrobotics/BotBrain
fetch_url: https://raw.githubusercontent.com/botbotrobotics/BotBrain/main/README.md
local_path: raw/2026-09-27-botbrain-github-readme.md
sha256: 4d4d452308a3c3e1e52c8e465827b2869112e524954d9751532611222bdc35c9
author: BotBot (botbotrobotics; Brazil)
published: 2026-01-22
ingested: 2026-09-27
venue: GitHub repository (homepage botbot.bot)
format: "repository README + GitHub API metadata + bot_rosa package README/manifest/llm.py spot-check"
github_stats: "360 stars, 100 forks, MIT, TypeScript-majority; created 2026-01-22, last commit 2026-05-18 (captured 2026-09-27); no GitHub releases"
tags: [botbrain, botbot, ros2, humble, jetson, orin-nano, realsense, nav2, rtab-map, slam, teleoperation, web-ui, fleet, quadruped, humanoid, unitree-go2, unitree-g1, rosa, llm-agent, open-hardware, 3d-printing, mit]
---

# BotBrain Open Source (BBOSS)

## Summary

**BotBrain** — tagline *"One Brain, any Bot"* — is an MIT-licensed, **bolt-on autonomy kit for legged (and wheeled) ROS 2 robots**: a **3D-printable snap-fit enclosure** holding an NVIDIA Jetson and **two Intel RealSense D435i** cameras, a **ROS 2 Humble** workspace (RTAB-Map SLAM, [Nav2](../entities/nav2.md) navigation, lifecycle/state-machine orchestration, YOLO detection, per-robot drivers), and a **Next.js 15 / React 19 web dashboard** for teleoperation, mapping, missions, health monitoring and multi-robot fleets. Officially supported robots are the **[Unitree Go2](../entities/unitree-go2.md) / Go2-W**, **[Unitree G1](../entities/unitree-g1.md)** (upper-body pose control and FSM transitions) and **DirectDrive Tita** biped, with a documented path for custom robots. Built by **BotBot**, a Brazilian company that sells an IP67 **BotBrain Pro** with payloads and service; the open edition is the on-ramp. Its demo claim is **one hour of autonomous office patrols** (video). It is the wiki's clearest instance of the **"brain box" pattern** — perception + SLAM + navigation + fleet UI as a product that sits *on top of* a vendor's locomotion stack rather than replacing it.

## Key claims

### Hardware

- Designed around **Intel RealSense D435i** (×2, front/rear) and the **NVIDIA Jetson** line.
- *"Officially supported boards: Jetson Nano, Jetson Orin Nano (support for AGX and Thor coming soon)"*; *"some heavy AI modules require Orin AGX."* (The Requirements table says "Nano, Orin Nano, or AGX series" — slightly looser than the headline.)
- 3D-printable enclosure (STL/STEP/3MF) with robot-specific adapters for Go2, G1 and Tita; *"Get your robot running with BotBrain in less than 30 minutes."* Parts: PLA, Jetson, 2× D435i, a voltage converter.

### Software stack

| Layer | Contents |
|---|---|
| OS | **JetPack 6.2 (Ubuntu 22.04)** recommended; Docker + Compose; `install.sh` sets up autostart |
| ROS 2 | **Humble** — `bot_bringup`, `bot_localization` (**RTAB-Map**, single or dual D435i), `bot_navigation` (**Nav2**), `bot_state_machine`, `bot_yolo` (YOLOv8/v11, TensorRT), `bot_rosa`, `bot_jetson_stats`, `bot_description`, per-robot `go2_pkg` / `g1_pkg` / `tita_pkg`, `joystick-bot` |
| Frontend | Next.js 15, React 19, TypeScript; talks to the robot via **rosbridge** (WebSocket, port 9090); **Supabase** for auth and storage (user must create their own project) |

### Features (README list)

- **Navigation**: RTAB-Map visual SLAM, Nav2 path planning with dynamic obstacle avoidance and recovery, multi-waypoint **missions/patrols**, click-to-navigate, map management.
- **Orchestration and safety**: coordinated lifecycle startup/shutdown; state machine; **6-level priority velocity arbitration (joystick > nav > AI)** via `twist_mux`; dead-man switch; e-stop sequence.
- **Control surfaces**: CockPit page, drag-and-drop custom dashboards, virtual joysticks, PS5/Xbox gamepads, WASD; speed profiles (*"Beginner, Normal and Insane mode"*).
- **Video**: multi-camera H.264/H.265 streaming, in-browser recording, URDF-based 3D view with laser-scan and path overlay.
- **Monitoring**: Jetson stats (JetPack version, power mode, per-rail power, thermals, fans), CPU/GPU/RAM, storage.
- **Fleet**: simultaneous multi-robot connections, fleet-wide commands, audit logging with CSV export, usage heatmaps.

### AI

- Marked **"(Coming Soon)"** as a section: YOLOv8/v11 detection and a searchable detection history.
- **ROSA natural-language control** — the `bot_rosa` package wraps NASA JPL's **ROSA** agent (LangChain-based; verified: `nasa-jpl/rosa`, Apache-2.0) with robot-specific tools loaded dynamically from each robot package. The shipped `llm.py` defaults to **OpenAI `gpt-4o`** (an Ollama path is commented out); `robot_config.yaml` takes an `openai_api_key`. The AI sits at the **lowest** priority in velocity arbitration.

### Safety posture

Explicit: *"Use a physical E-stop — Never rely solely on software stops"*; test in simulation first; keep clear during initial testing; full disclaimer of liability.

## Entities mentioned

- [BotBrain](../entities/botbrain.md) (new) · [Unitree Go2](../entities/unitree-go2.md) · [Unitree G1](../entities/unitree-g1.md) · [Nav2](../entities/nav2.md) · [RTAB-Map](../entities/rtab-map.md) · [ROS 2](../entities/ros2.md) · [Jetson Orin Nano](../entities/jetson-orin-nano.md) · [Unitree](../entities/unitree.md)
- Not given pages: BotBot (the company), DirectDrive Tita, NASA JPL ROSA, Intel RealSense D435i, Supabase.

## Concepts touched

- [Agent hardware abstraction](../concepts/agents/agent-hardware-abstraction.md) — ROSA-on-ROS 2 with per-robot tool sets, and an LLM placed *below* joystick and Nav2 in command arbitration.
- [LLM agent architecture](../concepts/agents/llm-agent-architecture.md) — a cloud LLM (GPT-4o) steering a robot through ROS tools.

## Open questions

- **Is it maintained?** Last commit 2026-05-18, no releases, 100 forks. Four months quiet at capture. The Pro product may be where development went.
- **Humble / JetPack 6.2 pin.** That is the Isaac ROS 3.2 / Ubuntu 22.04 world. Moving to JetPack 7.2 (and [Isaac ROS](../entities/isaac-ros.md) 4.6/5.0 on Jazzy/Lyrical) is a distro migration the README does not mention; Thor support is "coming soon."
- **How well does it hold up on a non-Unitree robot?** Every supported platform ships its own locomotion controller exposing `cmd_vel`; the "any Bot" claim is really "any bot with a velocity interface."
- **What does the one-hour patrol demo measure?** A video, no interventions count, no navigation success rate.
- **Supabase dependency** — the dashboard needs a user-owned cloud project for auth and storage; there is no fully offline mode documented.
