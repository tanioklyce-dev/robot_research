---
title: Physical Atari
type: entity
subtype: system
created: 2026-11-09
updated: 2026-11-09
sources: 1
tags: [physical-atari, real-world-rl, real-time-rl, atari, ale, keen-technologies, low-cost-hardware, open-hardware]
---

**Physical Atari** — an open test rig from [Keen Technologies](keen-technologies.md) for studying reinforcement learning in real time. A camera watches Atari on a small screen, and a three-servo robot called the Robotroller moves a real joystick ([paper](../sources/physical-atari-paper.md)).

## How it works

An [ALE](ale.md) game runs on a Raspberry Pi 5 at 60 FPS and doesn't wait for the agent. A separate computer sees the screen through a camera and sends one of 18 actions, which the servos carry out by moving to preset positions. [AprilTags](../concepts/robotics/apriltags.md) on the screen locate the game and encode the reward.

Screen-to-joystick response is about 165 ms, before any neural-network time.

## Results

- Learned six games in about 5.5 hours each, with 145 hours of runs and no intervention.
- A policy moved to a second, identically built robot did worse on all six games. On the two games tested, continued learning on the new body improved it.

The rig has clear limits as a proxy for robotics, and the "weeks" and "under $1,000" claims lack itemised support. Both are covered on the [source page](../sources/physical-atari-paper.md).

## Why it matters in this wiki

Most [real-world RL](../concepts/learning/real-world-robot-rl.md) in this wiki bought sample efficiency with demonstrations and human corrections. Physical Atari tests the plainer case of an agent learning alone on cheap hardware.

Its reliability notes are also useful in their own right. Plastic servo gears, plastic horns, loose screws and over-aggressive gains each failed under continuous duty, and [Dynamixel](dynamixel.md) users may meet the same problems.

## Availability

[Build guides and printable parts](https://keenagi.com/research/physical-atari/) are public, and the [code](https://github.com/Keen-Technologies/physical-atari-rlc) is Apache-2.0. Users supply their own Atari ROMs.

## Related

- [Keen Technologies](keen-technologies.md) · [ALE](ale.md) · [Dynamixel](dynamixel.md)
- [Real-world robotic RL](../concepts/learning/real-world-robot-rl.md) · [Atari RL lineage](../syntheses/rl/atari-rl-lineage.md)

## Mentioned in

- [Physical Atari paper](../sources/physical-atari-paper.md)
