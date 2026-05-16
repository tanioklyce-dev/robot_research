---
title: roboRIO
type: entity
created: 2026-05-08
updated: 2026-05-08
sources: 2
tags: [frc, controller, ni, roborio, embedded]
---

# roboRIO

The mandatory robot controller for [FIRST Robotics Competition](first-robotics-competition.md), manufactured by National Instruments (NI). Available in two generations: roboRIO 1 and roboRIO 2.

## Specifications

| Feature | roboRIO 1 | roboRIO 2 |
|---------|----------|----------|
| Processor | Xilinx Zynq-7020 (dual-core ARM Cortex-A9 + FPGA) | Same architecture, improved |
| OS | NI Linux Real-Time | NI Linux Real-Time |
| Ports | PWM (10), DIO (10), Analog In (4), Relay (4), CAN, I2C, SPI, USB, MXP, RSL | Similar + Ethernet improvements |
| Programming | WPILib (Java, C++, LabVIEW); Python via RobotPy | Same |

## FRC role

- **R710**: Every FRC robot must use exactly one roboRIO as its primary controller ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), §8.7).
- Communicates with the FMS via FRC Radio (pre-configured at events) over the FMS network.
- Controls all motor controllers (via CAN bus or PWM), pneumatic controllers (PCM/PH), sensors, and custom circuits.
- Robot code cannot be deployed while connected to FMS ([FRC 2026 Game Manual](../sources/frc-2026-game-manual.md), §5.12).
- Supports co-processors (Raspberry Pi, Jetson, Orange Pi) for vision processing — these connect via Ethernet or USB but cannot directly control actuators without routing through the roboRIO.

## Software ecosystem

- **WPILib**: Open-source FRC framework providing motor control, sensor reading, autonomous command scheduling, and driver station communication.
- **NetworkTables**: Publish/subscribe protocol for robot-to-dashboard and robot-to-coprocessor communication.
- **PathPlanner / Choreo**: Third-party autonomous trajectory planning tools that generate paths followed by the roboRIO.
- **PhotonVision / Limelight**: Vision coprocessor software that detects [AprilTags](../concepts/robotics/apriltags.md) and feeds pose estimates to the roboRIO for autonomous localization.

## Comparison to research-robotics controllers

| Controller | Context | Architecture | Key difference |
|-----------|---------|-------------|----------------|
| **roboRIO** | FRC | ARM Cortex-A9 + FPGA, NI Linux RT | Hard-real-time motor control; tightly regulated by FRC rules |
| Jetson Orin Nano | [ROSOrin](rosorin.md) | ARM + GPU, Ubuntu + ROS 2 | GPU for ML inference; no real-time motor FPGA |
| Raspberry Pi 5 | [Stretch](stretch.md) driver | ARM, Ubuntu + ROS 2 | General Linux; soft-real-time |

The roboRIO's FPGA provides deterministic real-time control (important for 10ms control loops during competition), but its compute is modest by ML standards. FRC teams offload vision and ML workloads to coprocessors.

## Mentioned in
- [FRC 2026 Game Manual](../sources/frc-2026-game-manual.md) (R710, §8.7)
