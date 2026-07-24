---
title: Gazebo
type: entity
subtype: software-framework
created: 2026-05-28
updated: 2026-05-28
sources: 7
tags: [gazebo, gz-sim, ignition, simulator, ros2, open-source, urdf, sdf, open-robotics]
---

**Gazebo** — the **canonical open-source ROS simulator**. Originated at the University of Southern California (2002), shepherded through Willow Garage / OSRF (Open Source Robotics Foundation), and **rebranded twice**: classic **Gazebo** (Gazebo 1–11, ROS 1 era) → **Ignition** (Citadel through Garden, mid-2010s through 2022) → **Gazebo** again (Gazebo Harmonic and later, 2023+ — re-adoption of the original name). Maintained by Open Robotics. The default sim target for ROS 2 robots and the open-source counterpart to NVIDIA's [Isaac Sim](nvidia-isaac-sim.md).

## Why it matters in this wiki

- **The default sim for ROS 2-based robots** in this wiki:
  - [TurtleBot 4](turtlebot.md) — Gazebo-Garden / Harmonic in Clearpath docs ([source](../sources/clearpath-turtlebot-4.md)).
  - [Stretch](stretch.md) docs reference Gazebo as one of two simulators ("ROS 2 + Python + MuJoCo/Gazebo," [source](../sources/hello-robot-stretch-docs.md)).
  - [ROSOrin](rosorin.md) — bundled Gazebo curriculum.
  - [lerobot-ros](lerobot-ros.md) quickstart uses Gazebo for the simulated SO-101 ([source](../sources/lerobot-ros-github.md)).
  - [PX4 Autopilot](px4-autopilot.md) UAV simulation ([source](../sources/px4-docs-main.md)).

## Position vs Isaac Sim and other simulators

| Simulator | Stewardship | Strengths | Weaknesses for wiki use cases |
|---|---|---|---|
| **Gazebo** | Open Robotics (open-source, Apache-2.0) | Native ROS 2 integration; ubiquitous; lightweight; URDF/SDF native | Lower-fidelity contact + rendering than Isaac Sim |
| **[NVIDIA Isaac Sim](nvidia-isaac-sim.md)** | NVIDIA (proprietary) | PhysX + RTX rendering; massive parallelism via [Isaac Lab](nvidia-isaac-lab.md); USD-native | Requires NVIDIA GPU; closed ecosystem; doesn't run on [Jetson Thor](jetson-thor.md) (no RT cores) |
| **[MuJoCo](mujoco.md)** | DeepMind (open-source) | Best contact physics for manipulation research | No native ROS bridge; smaller robot model library |

[so101_ros2](so101-ros2.md) uses **Isaac Sim 5.0+** instead of Gazebo, which is unusual for a ROS 2-native project — most prefer Gazebo for ease of integration.

## Confusing naming history

- **Gazebo 1–11** — original C++ stack; deprecated 2025.
- **Ignition Citadel / Edifice / Fortress / Garden** — rebranded; same project, new internals.
- **Gazebo Harmonic / Ionic / Jetty / Kilted** — name reverted to "Gazebo" in 2023; current naming (annual releases, like ROS 2).

Per ROS 2 distribution pairing: **Gazebo Harmonic** is bundled with **ROS 2 Jazzy / Humble**, **Gazebo Fortress** was the prior pairing.

## Related

- [ROS 2](ros2.md) — primary middleware substrate.
- [NVIDIA Isaac Sim](nvidia-isaac-sim.md) — proprietary alternative; higher fidelity but heavier.
- [MuJoCo](mujoco.md) — physics engine; not a full simulator stack.
- [TurtleBot](turtlebot.md), [Stretch](stretch.md), [ROSOrin](rosorin.md), [lerobot-ros](lerobot-ros.md), [PX4 Autopilot](px4-autopilot.md) — all use Gazebo somewhere in their sim story.

## Mentioned in

- [Clearpath TurtleBot 4 product page](../sources/clearpath-turtlebot-4.md)
- [Hello Robot Stretch Documentation](../sources/hello-robot-stretch-docs.md)
- [Hiwonder ROSOrin docs](../sources/hiwonder-rosorin-docs.md)
- [lerobot-ros GitHub](../sources/lerobot-ros-github.md) — Gazebo for the simulated SO-101 quickstart.
- [so101_ros2 readthedocs](../sources/so101-ros2-readthedocs.md) — mentions Gazebo for context; project uses Isaac Sim instead.
- [PX4 docs](../sources/px4-docs-main.md) — Gazebo Garden / Harmonic as the UAV-simulation default.

## Open questions / TBD

- **Direct ingest of [gazebosim.org](https://gazebosim.org/) docs** would let us nail down the current release roadmap and ROS 2-distro pairings precisely.
- **Open Robotics / OSRF** as an organization entity — currently no page despite Open Robotics shepherding both ROS 2 and Gazebo.
- **Gazebo Harmonic + ROS 2 Jazzy on Jetson** — performance characteristics for in-the-loop training? Not surfaced from current sources.
