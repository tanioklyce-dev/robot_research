---
title: "lerobot-ros — Lightweight ROS 2 wrapper for LeRobot (ycheng517/lerobot-ros GitHub)"
type: source
url: https://github.com/ycheng517/lerobot-ros
license: not specified in repo metadata
author: ycheng517 (GitHub user)
created: 2025-07-27
last_pushed: 2025-11-06
ingested: 2026-05-28
stars: 194
forks: 28
languages: Python 100%
ros2_distro: Jazzy (only tested)
tags: [lerobot-ros, lerobot, ros2, jazzy, ros2_control, moveit, moveit-servo, joint-trajectory-controller, position-controllers, gripper-action-controller, so-101, gamepad-teleop, keyboard-teleop]
---

## Summary

**`ycheng517/lerobot-ros`** — a **generic Python-class-based** ROS 2 wrapper for [LeRobot](../entities/lerobot.md). Tagline: "lightweight interface for controlling ROS-based robotic arms using LeRobot." **194 stars / 28 forks / 3 open issues** as of May 2026 — the **most-starred LeRobot↔ROS 2 bridge** in the wiki, ~2.5× the star count of [Rosetta](rosetta-github.md) (76) and ~4× of [so101-ros2](so101-ros2-readthedocs.md) (50). Python 100%; ROS 2 **Jazzy only** ("This repo is only tested on Jazzy"); no license listed in repo metadata.

The thesis: any robot arm with a [ros2_control](https://control.ros.org/) or [MoveIt 2](../entities/moveit.md) interface can be made a LeRobot platform by **sub-classing `ROS2Robot` and `ROS2Config`** with the right joint names, control mode, and limits. The architecture is the orthogonal alternative to [Rosetta](rosetta-github.md)'s YAML-contract approach — **Python sub-class vs declarative YAML**.

## Topics: `embodied-ai, lerobot, robotic-arm, robotics, ros2`. Description: *"Lightweight interface for controlling ROS-based robotic arms using LeRobot."*

## Architecture — 2 packages, no monolith

- `lerobot_robot_ros/` — the LeRobot Robot plugin (`ROS2Robot` class + `ROS2Config` dataclass).
- `lerobot_teleoperator_devices/` — gamepad teleoperator (6-DoF end-effector) + keyboard teleoperator (joint position).

Compare to [Rosetta](rosetta-github.md)'s 5 packages and [so101_ros2](so101-ros2-readthedocs.md)'s 8 packages — `lerobot-ros` is **the minimalist of the three**.

## Three supported control modes

Per README, robot config selects via `action_type`:

| Mode | `action_type` | ros2_control / MoveIt component | Use case |
|---|---|---|---|
| **Joint position** | `JOINT_POSITION` | `position_controllers/JointGroupPositionController` + `joint_state_broadcaster` | Direct joint targets; the cheapest mode |
| **Joint trajectory** | `JOINT_TRAJECTORY` | `joint_trajectory_controller/JointTrajectoryController` + `joint_state_broadcaster` | Smooth trajectory execution |
| **End-effector velocity** | `CARTESIAN_VELOCITY` | `moveit_servo` + `joint_trajectory_controller` + `joint_state_broadcaster` | Cartesian-space control; needs MoveIt 2 |

Gripper modes (`gripper_action_type`):
- **Trajectory** — `JointTrajectoryController` publishing to `/gripper_controller/joint_trajectory`.
- **Action** — `GripperActionController` sending action goals to `/gripper_controller/gripper_cmd` (with feedback on whether the gripper reached its target).

## How you integrate a new robot

Two-file delta (README "Code Changes to Lerobot-ros"):

```python
# robot.py: a pass-through class to satisfy LeRobot device discovery
class MyRobot(ROS2Robot):
    pass

# config.py: declare joint names, gripper, limits
@RobotConfig.register_subclass("my_ros2_robot")
@dataclass
class MyRobotConfig(ROS2Config):
    action_type: ActionType = ActionType.JOINT_POSITION
    ros2_interface: ROS2InterfaceConfig = field(
        default_factory=lambda: ROS2InterfaceConfig(
            base_link="base_link",
            arm_joint_names=["joint_1", "joint_2", ..., "joint_6"],
            gripper_joint_name="gripper_joint",
            gripper_open_position=0.0,
            gripper_close_position=1.0,
            max_linear_velocity=0.05,  # m/s
            max_angular_velocity=0.25,  # rad/s
        )
    )
```

That's it. Once `MyRobot` is registered, it's invokable via `lerobot-teleoperate --robot.type=my_ros2_robot ...`.

## Quickstart (SO-101 simulated)

Requires **ROS 2 Jazzy + Python 3.12** (must match for `rclpy`). Workspace setup:

```bash
conda create -y -n lerobot-ros python=3.12
conda activate lerobot-ros
conda install -c conda-forge libstdcxx-ng -y   # rclpy needs GLIBCXX_3.4.30
source /opt/ros/jazzy/setup.sh

git clone https://github.com/ycheng517/lerobot-ros
cd lerobot-ros
pip install -e lerobot_robot_ros lerobot_teleoperator_devices
```

Simulated SO-101 setup uses [Gazebo](../entities/gazebo.md) — see [Pavankv92/lerobot_ws](https://github.com/Pavankv92/lerobot_ws). Then 3 terminals:

```bash
# Terminal 1 — Gazebo sim
ros2 launch lerobot_description so101_gazebo.launch.py

# Terminal 2 — controllers + MoveIt
ros2 launch lerobot_controller so101_controller.launch.py && \
  ros2 launch lerobot_moveit so101_moveit.launch.py

# Terminal 3 — LeRobot with keyboard teleop into the ROS 2 SO-101
lerobot-teleoperate \
  --robot.type=so101_ros \
  --robot.id=my_awesome_follower_arm \
  --teleop.type=keyboard_joint \
  --teleop.id=my_awesome_leader_arm \
  --display_data=true
```

"Once you have teleoperation working, you can use all standard LeRobot features as usual."

## Comparison vs the other two LeRobot↔ROS 2 bridges in this wiki

| Dimension | [lerobot-ros](../entities/lerobot-ros.md) (this) | [Rosetta](../entities/rosetta.md) | [so101_ros2](../entities/so101-ros2.md) |
|---|---|---|---|
| **Approach** | Python sub-class | YAML contract | SO-101 hardware-specific workspace |
| **Generality** | Generic (any ros2_control / MoveIt arm) | Generic (any ROS 2 topic shape) | SO-101-only |
| **Lines to add a new robot** | ~30 (one class + one dataclass) | ~50 (one YAML) | N/A (hardware-specific) |
| **Stars (May 2026)** | **194** | 76 | 50 |
| **ROS 2 distro** | **Jazzy only** | distribution-agnostic (likely Humble + Jazzy) | **Humble only** |
| **Control modes** | joint pos / joint traj / EE velocity (MoveIt Servo) | declarative — any topic shape | depends on shipped `so101_controller` |
| **Teleop** | gamepad (6-DoF EE) + keyboard (joints) shipped | keyboard + experimental teleop plugin | shipped `so101_teleop` |
| **Architecture stance** | "lightweight wrapper" | "5-step pipeline" | "complete workspace + bringup" |
| **Sim integration** | Gazebo (per quickstart) | not specified | **Isaac Sim 5.0+** |
| **License** | not specified | Apache-2.0 | MIT |

> [!note] Distribution split is operationally load-bearing
> If you're on a **Humble** robot (ROSOrin Pro, TurtleBot 4, TurtleBot 3), `lerobot-ros` is **not directly usable** without porting to Humble. [Rosetta](rosetta-github.md) is the safer cross-distro bet for these platforms.

## Maturity / risk profile

| Signal | Value |
|---|---|
| Stars / forks | 194 / 28 (**highest of the 3 LeRobot↔ROS 2 bridges**) |
| Age | ~10 months (Jul 2025 → May 2026) |
| Open issues | 3 |
| Last push | 2025-11-06 (~6 months ago) |
| Maintainers | Solo author (`ycheng517`) |
| License | **Not specified** — this is a blocker for any redistribution use |
| Author signal | Also maintains [ycheng517/ar4_ros_driver](https://github.com/ycheng517/ar4_ros_driver) (a real-robot ROS 2 driver) — referenced from the README as an example of `moveit_servo` usage |

**Caveat**: last push 6 months ago — less active than Rosetta (last push days ago) and so101_ros2 (last push Dec 2025). Star count is high but momentum may be slowing.

## Entities mentioned

- [LeRobot](../entities/lerobot.md) — upstream framework.
- [SO-ARM101](../entities/so-arm101.md) — quickstart reference robot.
- [Rosetta](../entities/rosetta.md) / [so101_ros2](../entities/so101-ros2.md) — sibling bridges.
- [ROS 2](../entities/ros2.md) — middleware substrate.

## Open questions

- **No license** — would block redistribution; should be raised with the author.
- **Maintenance momentum** — last push 6 months old. Is this a stable plateau or an abandoned project?
- **Multi-camera support** — README focuses on arm control; multi-camera dataset capture (the [`so101.yaml` Rosetta contract](rosetta-github.md) handles 3 cameras out-of-the-box) is not explicitly addressed.
- **Mobile-base support** — `lerobot-ros` is explicitly *arm-focused*. For a mobile manipulator (ROSOrin Pro, [LeKiwi](../entities/lekiwi.md)), [Rosetta](rosetta-github.md) (with its TurtleBot3 contract) is the more natural fit.
- **Backport to Humble** — what's the engineering lift? `rclpy` differences between Jazzy and Humble are usually small; might be a few-day port.
