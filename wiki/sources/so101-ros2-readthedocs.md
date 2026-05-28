---
title: "so101_ros2 — A ROS 2 Bridge for LeRobot SO-101 (nimiCurtis/so101_ros2)"
type: source
url: https://so101-ros2.readthedocs.io/latest/
github: https://github.com/nimiCurtis/so101_ros2
license: MIT
author: nimiCurtis (Nimi Curtis, GitHub user)
created: 2025-06-12
last_pushed: 2025-12-13 (v0.1.1 release)
ingested: 2026-05-28
stars: 50
forks: 8
languages: Python 81.1% / C++ 13.5% / CMake 4.5% / Shell 0.9%
ros2_distro: Humble (required)
python: 3.10+
tags: [so101-ros2, nimicurtis, lerobot, ros2, humble, so-101, isaac-sim, vla, smolvla, pi05, ros2_control, hardware-interface, urdf, usd]
---

## Summary

**`nimiCurtis/so101_ros2`** — an **SO-101-hardware-specific** ROS 2 workspace + LeRobot bridge. **MIT-licensed**, 50 stars / 8 forks / Python 3.10+, ROS 2 **Humble**. Created Jun 12 2025; last release v0.1.1 on Dec 13 2025. Docs site: [so101-ros2.readthedocs.io](https://so101-ros2.readthedocs.io/latest/). The most opinionated of the three LeRobot↔ROS 2 bridges in this wiki — ships a **complete 8-package workspace** including URDF/USD, hardware interface, controllers, bringup launch files, teleop, and bag-recording. Adds **Isaac Sim 5.0+ integration** for sim-based teleoperation and VLA inference.

The thesis is the opposite of [lerobot-ros](lerobot-ros-github.md)'s "lightweight wrapper" stance: this is a **batteries-included reference implementation** for one specific robot. For SO-101 owners on Humble, it's the fastest path to a working IL pipeline.

## Topics: `imitation-learning, isaac-sim, lerobot, robot-learning, robotics, ros2, teleoperation, vla`

## Workspace — 8 packages

| Package | Role |
|---|---|
| `so101_description` | URDF + Xacro + meshes + **USD files** (for Isaac Sim) |
| `so101_hardware_interface` | ROS 2 control hardware interface for real SO-101 |
| `so101_controller` | ros2_control controllers + launch files |
| `so101_bringup` | System launch + configuration |
| `so101_ros2` | Core utilities |
| `so101_ros2_bridge` | **The LeRobot↔ROS 2 bridge nodes** (primary integration) |
| `so101_teleop` | Manual control / teleop utilities |
| `ros2_externals/` | Bundled external dependencies |

Plus a separate `so101_rosbag2lerobot_dataset` package for converting recorded rosbags to LeRobot dataset format.

## Pipeline (per readthedocs landing page navigation)

1. **Setup** — prerequisites, Python env, USB access, calibration, verification.
2. **Build so101_ros2** — bootstrap, LeRobot exposure, camera support.
3. **ROS 2 Control Architecture** — hardware interface + controller layout.
4. **Getting Started** — bridge / camera configuration, system launch.
5. **Imitation Learning** — teleoperation, demonstrations, training, deployment.

## Lerobot integration features (per GitHub README)

- **Real-time leader/follower teleoperation** via LeRobot API.
- **Camera pipelines**: V4L USB cameras + **Intel RealSense 2.0**.
- **Demonstration recording** via `system_data_recorder` for IL datasets.
- **ROS 2 → LeRobotDataset conversion** via separate `so101_rosbag2lerobot_dataset` package.
- **VLA model training / fine-tuning** integration with LeRobot.
- **Autonomous policy deployment** — **SmolVLA and π0.5 supported**.
- **Isaac Sim 5.0+** for virtual teleoperation + inference.
- **Joint state streaming** at configurable rates.

## Install pattern (verbatim from README)

Requires **two conda environments** (because Isaac Sim 5.0+ wants Python 3.11; LeRobot wants 3.10):

```bash
# Env 1 — lerobot_ros2 (Python 3.10)
conda create -n lerobot_ros2 python=3.10
conda activate lerobot_ros2
git clone https://github.com/nimiCurtis/lerobot.git    # author's own fork
cd lerobot
pip install -e ".[all]"

# Env 2 — lerobot_isaaclab (Python 3.11, optional)
# Separate due to Python version incompatibility with Env 1
```

ROS 2 workspace:

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone --recurse-submodules https://github.com/nimiCurtis/so101_ros2.git
./build.sh   # first-time initialization; exports to ~/.bashrc
```

> [!note] Two-env install + own LeRobot fork
> The install pattern (two conda envs + the author's [`nimiCurtis/lerobot`](https://github.com/nimiCurtis/lerobot) fork rather than upstream `huggingface/lerobot`) is a heavier operational footprint than [Rosetta](rosetta-github.md) (single env, upstream LeRobot) or [lerobot-ros](lerobot-ros-github.md) (single env, upstream LeRobot). The fork dependency is a maintenance risk — if upstream LeRobot moves, the fork can drift.

## Hardware assumptions

- Pre-assembled [SO-101](../entities/so-arm101.md) with calibrated motor IDs and baud rates.
- USB connection via auto-detected COM ports (`lerobot-find-port`).
- Both leader and follower arm configurations supported.
- Motor calibration JSON exported to a specified directory.

No support for SO-100, Koch-v1.1, or any other arm — by design.

## Comparison vs the other two LeRobot↔ROS 2 bridges

| Dimension | [so101_ros2](../entities/so101-ros2.md) (this) | [Rosetta](../entities/rosetta.md) | [lerobot-ros](../entities/lerobot-ros.md) |
|---|---|---|---|
| **Approach** | SO-101 reference workspace | YAML contract (generic) | Python sub-class (generic) |
| **Hardware coverage** | **SO-101 only** | any ROS 2 robot | any ros2_control / MoveIt arm |
| **Packages** | **8** (full workspace) | 5 | 2 |
| **Stars (May 2026)** | 50 | 76 | **194** |
| **ROS 2 distro** | **Humble** | distro-agnostic | **Jazzy only** |
| **License** | **MIT** | Apache-2.0 | not specified |
| **Sim** | **Isaac Sim 5.0+** | not specified | Gazebo (per quickstart) |
| **URDF / USD** | shipped (`so101_description`) | not in scope | not in scope |
| **Policies tested** | **SmolVLA + π0.5** | full LeRobot menu + π0.5 + GR00T + Wall-X + X-VLA (claimed) | not the focus |
| **Operational footprint** | 2 conda envs + author's LeRobot fork | 1 env + upstream LeRobot | 1 env + upstream LeRobot |

> [!note] Strategic positioning
> `so101_ros2` is the **SO-101 owner's preferred bridge if they want Isaac Sim** and don't mind the heavier install. [lerobot-ros](lerobot-ros-github.md) is the right choice for **any-arm generality on Jazzy**. [Rosetta](rosetta-github.md) is the right choice for **non-arm robots (mobile bases) or Humble platforms**.

## Maturity / risk profile

| Signal | Value |
|---|---|
| Stars / forks | 50 / 8 |
| Age | ~12 months (Jun 2025 → May 2026) |
| Last push | 2025-12-13 (v0.1.1 release; ~5 months old) |
| License | **MIT** ✓ |
| Maintainers | Solo author (`nimiCurtis`) |
| Documentation | **dedicated readthedocs site** — best-documented of the 3 |
| Author's other work | Maintains a personal LeRobot fork (`nimiCurtis/lerobot`) |

## Entities mentioned

- [LeRobot](../entities/lerobot.md) — upstream.
- [SO-ARM101](../entities/so-arm101.md) — target hardware.
- [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md) — integrated simulator.
- [SmolVLA](../entities/smolvla.md) / [π0](../entities/pi-zero.md) / [π0.5/0.6](../entities/pi-zero-6.md) — supported deployment policies.
- [Rosetta](../entities/rosetta.md) / [lerobot-ros](../entities/lerobot-ros.md) — sibling bridges.
- [ROS 2](../entities/ros2.md) — middleware substrate (Humble specifically).

## Open questions

- **Author's LeRobot fork divergence** — how out-of-date is `nimiCurtis/lerobot` vs `huggingface/lerobot`? What functionality does the fork add?
- **Hardware variants** — does it work on SO-100 (the predecessor) or only SO-101?
- **VLA deployment maturity** — README claims SmolVLA + π0.5 deployment works. Any blog posts / demos / benchmarks?
- **Bag→LeRobotDataset conversion robustness** — separate `so101_rosbag2lerobot_dataset` package. Schema compatibility with upstream `LeRobotDataset`?
- **Isaac Sim teleop loop performance** — the Isaac Sim integration is the unique value-add vs the other two bridges; what's the latency profile?
