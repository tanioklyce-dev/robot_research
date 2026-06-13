---
title: NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived tutorial)
type: source
url: https://www.jetson-ai-lab.com/archive/lerobot.html
author: NVIDIA Jetson AI Lab (Dustin Franklin / jetson-containers project)
published: 2024
ingested: 2026-06-13
tags: [lerobot, jetson, jetson-containers, dustynv, act, koch, docker, edge-ai, onboard-compute, tutorial, archived]
format: web-tutorial
---

# NVIDIA Jetson AI Lab — HuggingFace LeRobot (archived tutorial)

## Summary

A NVIDIA **Jetson AI Lab** tutorial for running Hugging Face **[LeRobot](../entities/lerobot.md)** in a prebuilt Docker container (`dustynv/lerobot`) deployed through the **[jetson-containers](../entities/jetson-containers.md)** framework, on Jetson Orin-class hardware. It walks the canonical LeRobot loop — motor configuration → teleoperation → dataset recording → **[ACT](../entities/act.md)** policy training → on-robot evaluation → dataset visualization — entirely **onboard a Jetson**, with the [Koch v1.1](../entities/lerobot.md) low-cost dual-arm kit as the primary robot. The page is now in the `/archive/` path and **marked deprecated / no longer maintained**; its commands target the **pre-refactor LeRobot CLI** (`lerobot/scripts/control_robot.py`, Hydra-style `train.py policy=act_koch_real`), which upstream LeRobot has since replaced with `lerobot-record` / `lerobot-train` entry points. Treat it as the **historical NVIDIA-blessed "LeRobot-in-a-container-on-Jetson" recipe**, not a current install guide.

## Why it matters in this wiki

This is the wiki's first **NVIDIA-official containerized path to run LeRobot *on* a Jetson** (training + inference), distinct from the two onboard/integration stories already ingested:

- **[Cutting the Cord](cutting-the-cord-untethered-xlerobot.md)** — measures LeRobot *policies* running untethered on an Orin Nano (ACT 27.8 Hz, etc.) but builds its own stack; it doesn't use the `dustynv/lerobot` container.
- **LeRobot ↔ ROS 2 bridges** ([Rosetta](../entities/rosetta.md) / [lerobot-ros](../entities/lerobot-ros.md) / [so101-ros2](../entities/so101-ros2.md)) — bolt LeRobot onto ROS 2 robots; orthogonal to "get LeRobot itself running on edge silicon."

It answers a narrow, practical question — *"how do I get the full LeRobot teleop→train→eval loop running on a Jetson without fighting CUDA/PyTorch/aarch64 dependency hell?"* — with the answer **"pull `dustynv/lerobot`."** The Docker-container approach is the load-bearing idea; the specific LeRobot CLI it wraps is stale.

## Key claims

- **Container:** `dustynv/lerobot`, deployed via `jetson-containers` + the `autotag` helper that selects the right tag for the host's L4T/JetPack. Bundled in-container: **JupyterLab** (port 8888) with the official LeRobot real-robot notebooks, **Rerun.io** for dataset playback, and **PulseAudio + Speech Dispatcher** for TTS audio.
- **Target hardware:** Jetson **AGX Orin 64 GB / 32 GB**, **Orin NX 16 GB**, and **Orin Nano 8 GB** (8 GB called out with caveats — it's the tight tier).
- **Software baseline:** **JetPack 6 GA (L4T r36.3)** or **JetPack 6.1 (L4T r36.4)**. (Predates the JetPack 6.2.x / R36.5 line the wiki's other Jetson sources track — another staleness marker.)
- **Storage:** NVMe SSD "highly recommended" — ≥16.5 GB for the container image, >2 GB for models; **swap raised to 8 GB**.
- **Primary robot:** **Koch v1.1** — low-cost dual-arm (leader/follower) kit using ROBOTIS [Dynamixel](../entities/dynamixel.md) servos. Also references **[ALOHA](../entities/aloha.md)** (Trossen bimanual) and the **PushT** simulation environment.
- **Device plumbing:** udev rules pin fixed names `/dev/ttyACM_kochleader` and `/dev/ttyACM_kochfollower`; PulseAudio configured `auth-anonymous=1`; optional CSI-camera path via `v4l2loopback` with `--csi2webcam` run-flags (e.g. `--csi-capture-res='1640x1232@30' --csi-output-res='640x480@30'`).
- **Default policy = ACT.** Training invoked as (pre-refactor Hydra CLI):
  `python lerobot/scripts/train.py dataset_repo_id=${HF_USER}/koch_test policy=act_koch_real env=koch_real device=cuda wandb.enable=true`
- **Recording / eval** go through `lerobot/scripts/control_robot.py record …` (with `--robot-path lerobot/configs/robot/koch.yaml`, `--fps 30`, warmup/episode/reset timing, `--num-episodes`); eval re-runs `record` with `-p <checkpoint>`.
- **Distributed training across machines:** datasets and checkpoints can be moved between multiple Jetsons or a PC via `scp` — record on the robot's Jetson, train on a beefier box, copy the checkpoint back to deploy. A simple precursor to LeRobot's later first-class async remote-inference stack.
- **Camera guidance:** top-mounted + front-facing as defaults; wrist-mounted cameras flagged as worth experimenting with.

## Entities mentioned

- [LeRobot](../entities/lerobot.md) — the framework being containerized.
- [jetson-containers](../entities/jetson-containers.md) — the deployment framework + `dustynv/*` image registry (new entity).
- [ACT](../entities/act.md) — the default policy trained in the tutorial.
- [ALOHA](../entities/aloha.md) — referenced bimanual platform.
- [Dynamixel](../entities/dynamixel.md) — Koch v1.1 servos.
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) — the entry-tier target (8 GB, with caveats).
- [Hugging Face](../entities/hugging-face.md) — LeRobot maintainer; dataset/model hub used by the recipe.
- [NVIDIA](../entities/nvidia.md) — publisher (Jetson AI Lab).

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — the teleop→record→train→eval loop.
- Onboard / edge inference — running the full loop on Jetson silicon (links to the [Jetson onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md)).

## Open questions

- **Is there a maintained successor?** The page is archived; NVIDIA may have folded LeRobot guidance into newer Jetson AI Lab / GR00T material. Not yet ingested.
- **Does `dustynv/lerobot` track current upstream LeRobot** (the `lerobot-record`/`lerobot-train` CLI, SmolVLA/π0 support), or is it frozen at the Koch/ACT-era API shown here? The container registry state is unverified.
- **Orin Nano 8 GB "caveats"** — the page doesn't quantify them; [Cutting the Cord](cutting-the-cord-untethered-xlerobot.md) later supplies the real onboard-Orin-Nano latency numbers for ACT/Diffusion/SmolVLA.
