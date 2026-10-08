---
title: "Meet Flourish One, the Raspberry Pi-powered humanoid built for busy parents (The Robot Report)"
type: source
url: https://www.therobotreport.com/meet-flourish-one-raspberry-pi-powered-humanoid-built-busy-parents/
local_path: raw/2026-09-29-therobotreport-flourish-one.md
sha256: 654285631b3f608aa7f449895d304ce6af2711dff48d1d8c92962a9b5048db6a
author: Mike Oitzman (The Robot Report)
published: 2026-09-29
ingested: 2026-10-07
venue: The Robot Report (trade press)
format: "launch-day article (~750 words) built on an interview with the founder"
tags: [flourish, flourish-1, home-robot, mobile-manipulator, raspberry-pi, cloud-inference, phone-teleop, imu, lidar, wrist-camera, trade-press, secondary]
---

# Meet Flourish One, the Raspberry Pi-powered humanoid built for busy parents

> [!note] The only hardware source
> [Flourish's own site](flourish-robots-website.md) publishes no compute, sensor or base specification. This article is where the **Raspberry Pi, six-wheel base, base-mounted lidar and per-gripper wrist cameras** come from. All of it is founder-stated. Its payload conversion is wrong; see below.

## Summary

Trade-press launch profile of [Flourish 1](../entities/flourish-1.md), based on an interview with founder [Antoine Marcel](../entities/flourish-robots.md). The founder's thesis is that **homes are too idiosyncratic for a generalist model**, so Flourish fine-tunes **per task, per home** from the owner's own demonstrations, with training and higher-level inference on **cloud GPUs**. The robot itself carries only a **Raspberry Pi**, to hold the BOM down: *"If we were to put an NVIDIA GPU in the robot, it would immediately double the cost."* Teaching uses the **phone's IMU**: you move the phone as if doing the task and the arms mirror it.

## Key claims
- Company **"founded in January of this year"** (2026). It *"straddl[es] San Francisco and Paris."* The first 50 units are **hand-built by a tiny team**.
- Thesis, in the founder's words: *"The way I tidy my apartment is not the same as you do in your house. You're going to show it for 30 minutes how to water your plants… We're going to fine-tune an AI model for that."*
- Hardware: **six-wheel mobile base** "for stability"; **two arms**; **two-fingered grippers, each with a wrist-mounted camera**; **small lidar on the base near the floor** for obstacle detection; battery designed for **12 hours of arm operation**.
- Payload: *"Each of the two arms has a payload capacity of 1.5 kg (4 lb.)"*. 1.5 kg is **3.3 lb**, as the company's site says. Why 1.5 kg: *"in homes, the majority of tasks don't need a huge payload."*
- Limits: not waterproof, *"won't do any dishes or wash the dog"*; limited dexterity; good for tidying, trash and wiping, not intricate assembly.
- Compute: **"powered by a Raspberry Pi"** (model unstated). Cloud GPUs train the skill models and run inference for higher-level behaviours, so the robot *"will require a network connection for 'thinking'"*, or owners can run the workloads on their own computers.
- Teaching: an app in development uses **the smartphone's IMUs** for teaching and teleoperation. *"you just take your phone, move your phone, and it will move the arms. We don't need any more other hardware."*
- Price **$3,555**; hopes to ship **before Christmas**.

## Contradictions with other sources

> [!warning] Contradiction — payload per arm, or in total
> This article says **1.5 kg per arm**. The [company site](flourish-robots-website.md) gives a single **3.3 lb (1.5 kg)** payload and *"nothing over 1.5 kg"*. *Interesting Engineering* says **3.3 lb total**. The primary supports only "objects up to 1.5 kg".

> [!note] "Humanoid"
> The headline calls it a humanoid. It is a **wheeled dual-arm mobile manipulator** with a lift, in the same class as [XLeRobot](../entities/xlerobot.md), [Sourccey](../entities/sourccey.md) and [NORI A3](../entities/nori-a3.md). Flourish's own pages never use the word. CNET and Forbes repeat it.

## Entities mentioned
- [Flourish Robots](../entities/flourish-robots.md) · [Flourish 1](../entities/flourish-1.md)
- [Raspberry Pi 5](../entities/raspberry-pi-5.md): the article says only "Raspberry Pi". The Pi 5 entity page is the closest match, not a confirmed model.
- [NVIDIA](../entities/nvidia.md), named only as the GPU the robot avoids carrying.

## Concepts touched
- [Imitation learning](../concepts/learning/imitation-learning.md): per-home fine-tuning from owner demonstrations.
- [Onboard robot service architecture](../concepts/robotics/onboard-robot-service-architecture.md): a thin onboard computer with cloud "thinking".
- [Heterogeneous edge SoC](../concepts/robotics/heterogeneous-edge-soc.md): the cost argument against onboard GPUs.

## Open questions
- Phone-IMU teleop gives a 6-DoF pose stream for one hand. How does one phone drive **two** arms plus a base and a lift? One arm at a time?
- IMU-only pose tracking drifts within seconds. Does the app fuse the phone camera (visual-inertial odometry, as ARKit/ARCore do), or does the arm follow orientation only?
- Which Raspberry Pi? A Pi 5 can host the controllers and stream cameras but cannot run a VLA ([Sourccey](../entities/sourccey.md), [NORI A3](../entities/nori-a3.md)).
