---
title: XLeRobot Documentation
type: source
url: https://xlerobot.readthedocs.io/en/latest/
github: https://github.com/Vector-Wangel/XLeRobot
author: Gaotian "Vector" Wang (creator) + contributors
published: 2025-08 (v0.3.0)
ingested: 2026-05-10
re-ingested: 2026-05-11 (deeper crawl — Hardware / Simulation / Software / Demos / Related Works subpages)
tags: [low-cost-robotics, mobile-manipulator, dual-arm, lerobot, lekiwi, so-arm101, embodied-ai, open-source]
---

## Summary

**XLeRobot** is a $660 household dual-arm mobile manipulator designed to "bring embodied AI to every family." Built by Gaotian "Vector" Wang as a composition on top of the [LeRobot](../entities/lerobot.md) ecosystem: two [SO-ARM101](../entities/so-arm101.md) arms (~40 cm reach each) mounted on a [LeKiwi](../entities/lekiwi.md) holonomic base, with optional Raspberry Pi compute and RGB / RealSense depth cameras. 90% 3D-printed; under 4 hours assembly. Version 0.3.0 released August 30, 2025; documentation site is the canonical entry point. License: Apache 2.0.

The project's explicit positioning is *cheaper than an iPhone*, with capabilities the project says compare to $30,000+ commercial bimanual robots — albeit with sharp limitations (fixed height, low payload, no dexterous in-hand manipulation).

## Key claims

- **Hardware stack**:
  - Two SO-ARM101 arms, ~40 cm reach, 600–1000 g payload per arm
  - LeKiwi-class wheeled mobile base
  - 90% 3D-printed
  - Optional: RGB camera, stereo RGB, RealSense RGBD depth, Raspberry Pi
  - Assembly time: < 4 hours
- **Pricing**: $660 USD basic / ~€680 EU / ¥3999 CN / ₹87,000 IN. Developer assembly kit $579 worldwide (excluding battery and IKEA cart used as base). Taobao ¥3,699.
- **Software**: built on [LeRobot](../entities/lerobot.md) (Hugging Face). Multiple control interfaces: keyboard, Xbox controller, Switch Joycon, VR (Quest 3). ManiSkill simulation with URDF support. Imitation-learning + reinforcement-learning environments.
- **Capabilities claimed**: household chores, indoor tasks, plant care, delivery, manipulation roughly competitive with $30k+ commercial robots.
- **Limitations acknowledged**: fixed height (no lift platform), workspace smaller than Aloha-class, no in-hand dexterity, payload <1 kg, no dynamic motion.
- **Safety positioning**: low-torque motors limit physical harm potential — a deliberate design tradeoff for a household platform.
- **Community & ecosystem**: hardware tutorials on YouTube and Bilibili; active Discord; Embodied AI hackathon participation.
- **Lineage**: explicitly builds on [LeRobot](../entities/lerobot.md), [SO-100/SO-101](../entities/so-arm101.md) (The Robot Studio), [LeKiwi](../entities/lekiwi.md) (SIGRobotics-UIUC), and Bambot (Qian Tim).

## Entities mentioned

- [XLeRobot](../entities/xlerobot.md) — the project itself
- [Vector Wang](../entities/vector-wang.md) — creator (Gaotian Wang)
- [LeRobot](../entities/lerobot.md) — software framework
- [LeKiwi](../entities/lekiwi.md) — mobile base
- [SO-ARM101](../entities/so-arm101.md) — arm platform
- [The Robot Studio](../entities/the-robot-studio.md) — SO-ARM creators (referenced via SO-ARM101)
- [Hugging Face](../entities/hugging-face.md) — LeRobot maintainer
- [ManiSkill](../entities/maniskill.md) — simulation environment supported

## Concepts touched

- [Imitation learning](../concepts/imitation-learning.md) — primary learning paradigm
- [Assistive robotics](../concepts/assistive-robotics.md) — household manipulation tasks; positioned in the same affordable-platform space as [Stretch](../entities/stretch.md), [ROSOrin Pro](../entities/rosorin-pro.md), and similar
- [Sim-to-real transfer](../concepts/sim-to-real-transfer.md) — ManiSkill sim → real, RL sim2real (Zhuoyi Lu)

## Open questions

- Real-world performance data: the docs describe capabilities qualitatively but lack benchmark numbers. How does XLeRobot perform on standard household-manipulation benchmarks (e.g., RoboCasa365, BEHAVIOR-1K) where Stretch / OK-Robot / RUM have published numbers?
- Reliability and reproducibility: the $660 figure is striking, but does it hold for an end-user assembler, including failure recovery for 3D-printed parts?
- Comparison to [Stretch](../entities/stretch.md) (~$20k) as an assistive platform — XLeRobot is dual-arm and ~30× cheaper, but lacks Stretch's lift, sturdier mobile base, and integrated stack maturity. Specific tradeoffs deserve a synthesis.

---

## Deeper crawl — 2026-05-11

The 2026-05-10 ingest above covered the landing page. This section adds detail from the docs' five subsections (Hardware / Simulation / Software / Demos / Related Works).

### Hardware (`hardware/`)

**Architecture intent.** Computing is offloaded to a user-supplied PC; the optional Raspberry Pi is positioned as a **WiFi relay** for sensor / actuator data, not as the inference host. This is the explicit design choice that lets the BOM stay near $660 — the platform never has to ship with a Jetson-class compute module.

**Physical specs (`hardware_intro/`):**
- **Mass**: ~12 kg (intentionally adult-liftable)
- **Vertical workspace**: 0.5 m – 1.25 m above ground (fixed-height torso; no lift)
- **Reach from cart edge**: ~0.36 m (workspace constraint vs. Aloha-class)
- **Power**: Anker SOLIX C300 power station — 288 Wh, 300 W max output, 280 W max charge (~1 hr to full), **10+ hr** normal-operation runtime; supplies dual 12 V arms + base + Pi at ~180 W draw
- **Actuators**: **17× Feetech STS3215 servos at 12 V** — the same servo family used by SO-100/SO-101 (cf. [SO-ARM101](../entities/so-arm101.md))

**BOM (`getting_started/material.html`).** Detailed parts list with regional pricing (US / EU / CN / IN). Standout line items:
- 17× STS3215 servos @ $14 each (US) = $238
- IKEA RÅSKOG cart: $39.99
- Anker SOLIX C300: $179.99
- 3× 4" omni wheels: $9.99 each
- 2× motor control boards: $10.55 each
- Logitech C920 head cam: $66; 2× hand cams: $12.98 each
- Optional Raspberry Pi 5: $60; RealSense D415: $272; stereo dual-eye cam: $30 upgrade

**3D-printing (`getting_started/3d.html`).** Tested on **BambuLab A1 with PLA Matte Black**. Alternative materials documented: PETG HF, PLA CF, Tough PLA. Recommends drying PLA at 45 °C for 8 hr in humid environments. STL + STEP files at `github.com/Vector-Wangel/XLeRobot/tree/main/hardware`.

**Assembly (`getting_started/assemble.html`).** 8 high-level steps:
1. Build two SO101 arms (motors indexed 1–6)
2. Configure motors via Bambot software
3. Assemble wheel base with omni wheels + extended wiring
4. Mount LeKiwi base under the IKEA cart
5. Assemble arm bases + head
6. Wiring + cable management (USB-C → DC for 12 V, USB-C → USB-C to charging station)
7. Clamp arms onto cart corners
8. Optional shells/sleeves

Assembly time: **2–4 hrs from scratch, 1–2 hrs with pre-assembled SO101 arms**. Detection should report **9 motors total** across two control boards (`/dev/ttyACM0`, `/dev/ttyACM1`).

Two-wheel and mecanum-wheel variants exist as `assemble_2wheel.html` and `assemble_mecanum.html`.

### Simulation (`simulation/`)

- **Simulator**: **[ManiSkill](../entities/maniskill.md) 3.0** (only — no MuJoCo / PyBullet path documented)
- **Scenes supported**: `ReplicaCAD_SceneManipulation-v1` (default), AI2-THOR, RoboCasa Kitchen counter scenes, `OpenCabinetDrawer-v1`. Notable: the docs explicitly link the [RoboCasa](../entities/robocasa.md) bench, which closes the loop with the wiki's existing JEPA/world-model coverage.
- **Asset layout**: URDF + meshes at `simulation/Maniskill/agents/robots`, `/assets/robots`, `/envs/scenes` in the repo — users copy them into their ManiSkill installation.
- **VR teleop (`vr_sim.html`)**: a custom **VRMonitor service** runs a WebSocket-over-HTTPS server that streams Quest 3 controller poses to ManiSkill. The exchange object is a `ControlGoal` (arm designation, 3D target position, wrist angle, gripper state, trigger / thumbstick metadata). Mappings: triggers = grippers; thumbsticks = base translate / rotate. Programmatic access: `from mani_skill.examples.vr_monitor import VRMonitor`. **Real-robot VR teleop is "coming soon"**; only simulation VR is functional today.

### Software (`software/`)

Five distinct on-robot software workflows are documented — XLeRobot is explicitly a **multi-stack reference platform**, not a single-policy product.

**1. Install (`install.html`).** `pip install -e .` workflow on top of the official [LeRobot](../entities/lerobot.md) install. The doc punts most environment details to LeRobot's installation guide.

**2. SO-100/SO-101 examples (`SO101.html`).** Four example scripts in increasing complexity:
- `0_so100_keyboard_joint_control.py` — joint-space
- `1_so100_keyboard_ee_control.py` — end-effector control
- `2_dual_so100_keyboard_ee_control.py` — dual-arm
- `3_so100_yolo_ee_control.py` — YOLO-vision-driven EE control

**3. Teleop (`XLeRobot_teleop.html`).** Four input modalities (keyboard, Xbox, Switch Joy-Con, VR). Real-robot VR is **"coming soon"** as of v0.3.0 — only sim works today. Bring-up requires `sudo chmod 666 /dev/ttyACM{0,1}` + `python lerobot/find_port.py`, with the same 9-motor expectation flagged in Assembly.

**4. RL (`RL.html`).** Mostly a *placeholder*: the page says "the official code for complete XLeRobot RL is coming soon" and **redirects users to two adjacent stacks**:
- [`lerobot-sim2real`](https://github.com/StoneT2000/lerobot-sim2real) by Stone Tao (ManiSkill-based PPO)
- HuggingFace official HIL-SERL tutorial (single SO-101 arm)

**5. LLM agent (`LLM_agent.html`).** A LangChain-style LLM-agent stack:
- **LLM**: defaults to **Google Gemini 3 Flash** (`google_genai:gemini-3-flash-preview`); any LangChain-compatible model works.
- **Tool library**: **RoboCrew** — factory functions like `create_move_forward()`, `look_around()`, plus a manipulation tool that calls a VLA policy. Tools are passed to an `LLMAgent` at construction.
- **Voice**: configurable wakeword (default **"hey robot"**); voice-commanded autonomous navigation is one of the demonstrated examples.
- **Demos shown**: approach-a-human, grab-notebook-and-deliver, voice-commanded navigation.
- **Compute model**: lightweight tools can run on Pi or laptop; VLA-inference tool runs on an **external GPU** via LeRobot's async policy server on port 8080.

**6. VLA / behavior-cloning options (three of them):**

- **ACT (`VLA_ACT.html`)** — LeRobot's ACT (Action Chunking Transformer) as the canonical VLA baseline. Example uses **50 episodes** of single-arm data; training command deferred to LeRobot's tutorial. Inference can run on Raspberry Pi (`record.py --teleop.type=xlerobot_vr`) or on a remote GPU server.
- **π0.5 (`VLA_pi05.html`)** — A bimanual VLA via an **OpenPI fork** with added "training support for bimanual SO-101 configuration." Released alongside the **`bimanual-toy-box-cleanup`** dataset on Hugging Face. No success-rate numbers published in the docs.
- **SmolVLA (`VLA_smol.html`)** — `lerobot/smolvla_base` checkpoint adapted to XLeRobot's **12-D action space (6 joints × 2 arms)**; actions are padded to 32-D during training and cropped to 12-D at inference. Tasks shown: drawer manipulation, pick-and-place, fine-motor **zipper control** — learned from **~20 demonstrations**. Compute: ~**1 hr 45 min on an NVIDIA A100 for an 80k-step checkpoint**. Apple Silicon supported via `--policy.device=mps`.

**7. Raspberry Pi setup (`raspberry_pi_setup.html`).** Pi 4 or newer; standard Pi Imager flow (32 GB+ SD card); WiFi + VNC + SSH for headless ops. The Pi's role is *on-robot relay*, not heavy compute.

### Demos (`demos/`)

Gallery of community and project demos — qualitative, no benchmark numbers:
- **Astera Institute / BrainBot** — "big brain with XLeRobot" (Hackster.io)
- **Makermods** — community implementation (makermods.ai)
- VR control (sim + real); autonomous RL; YOLO-based object tracking
- Dynamics demo by Mitchell Chen
- "First demo v0.1.0" historical clip
- Hackathon context: **Seeed Embodied AI Worldwide Hackathon**

### Related works (`relatedworks/`)

The docs list a curated set of adjacent projects organized by sub-discipline. Notably XLeRobot **explicitly cites [V-JEPA 2](../entities/v-jepa-2.md)** under "Task Planning" — a direct intersection with this wiki's JEPA / world-model coverage.

- **Perception**: DRAWER, CoTracker3
- **Task planning**: [**V-JEPA 2**](../entities/v-jepa-2.md) (intersection with this wiki's JEPA line)
- **Motion control**: HIL-SERL (Human-in-the-Loop SERL); "Caging in Time"
- **Tactile / dexterous hands**: 3D-ViTac (Velostat visuo-tactile), eFlesh (magnetic touch sensing), **BACH Hand** ("Belt-Augmented Compliant Hand," Yuan Shen Li — `yuanshenli.com/bach.html`)
- **Simulation & benchmarking**: [**ManiSkill 3.0**](../entities/maniskill.md), **RoboTwin 2.0** (bimanual benchmark)
- **Dev tools**: BamBot (web control panel), Model Context Protocol (MCP), Hunyuan3D-2 (3D reconstruction), `lerobot-sim2real`

These are framed as "interesting, meaningful work" the project draws from or aspires to — not direct dependencies.

## New entities / concepts surfaced (not yet in wiki)

- **HIL-SERL** — Human-in-the-Loop SERL; the RL workflow XLeRobot defers to for now. Candidate concept page if the assistive-RL thread expands.
- **RoboCrew** — the LangChain-tool-factory library underpinning XLeRobot's LLM agent. Candidate entity page if/when the LLM-agent thread deepens.
- **OpenPI** — the π0/π0.5 implementation fork XLeRobot uses for bimanual training. Already adjacent to [π0 paper](pi-zero-paper.md); a future ingest of OpenPI itself would close the loop.
- **`bimanual-toy-box-cleanup`** dataset (HF) — first XLeRobot-native VLA dataset.
- **STS3215 servo** — the universal Feetech actuator across the SO-100 / SO-101 / XLeRobot stack; not yet broken out as its own entity.
- **BACH Hand**, **3D-ViTac**, **eFlesh** — tactile-and-dexterity work XLeRobot cites; candidates if the wiki ever opens a tactile / dexterous-hand thread.
