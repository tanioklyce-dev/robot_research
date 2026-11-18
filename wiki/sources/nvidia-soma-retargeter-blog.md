---
title: "Adapt Human Motion for Robots with NVIDIA SOMA Retargeter (NVIDIA blog)"
type: source
url: https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/
fetch_url: https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/
video_url: https://fb.watch/KYOMuecQOe/
local_path: raw/2026-11-17-nvidia-blog-soma-retargeter.md
sha256: 41c7cc8e207f918673a6af5b93c53730126feb14828f9216ee886898fc9aa5ec
author: John Malaska (NVIDIA)
published: 2026-11-13
ingested: 2026-11-17
venue: NVIDIA Technical Blog
license: "tool: Apache-2.0 (github.com/NVIDIA/soma-retargeter)"
format: "vendor tutorial post. Text captured via curl with article extraction; figures and GIFs described from their captions, not captured. Reached from a 9-second NVIDIA Robotics Facebook video (posted 2026-11-17, no captions, caption text only) that links here; the video itself carries no information beyond its caption."
tags: [soma-retargeter, soma-x, motion-retargeting, humanoid, nvidia, newton, warp, inverse-kinematics, bones-seed, gem-x, kimodo, motionbricks, gear-sonic, protomotions, unitree-g1, unitree-h2, booster-t1, agibot, microduck, vendor-source]
---

# Adapt Human Motion for Robots with NVIDIA SOMA Retargeter

> [!note] What was ingested
> The user supplied a Facebook share link. It resolves to a 9-second NVIDIA Robotics clip whose only content is a three-sentence caption ("NVIDIA SOMA Retargeter maps human motion to different humanoid robots, accounting for their proportions, joint structures and range of motion...") and a link to this post. Under the wiki's primary-source rule the post is the source; the clip is recorded as `video_url`.

## Summary

A tutorial for **SOMA Retargeter**, NVIDIA's open-source (Apache-2.0) tool for turning human motion into joint trajectories for a specific humanoid. The input is a BVH animation on the **SOMA** skeleton, a shared human-body representation from NVIDIA's SOMA-X project; the output is a CSV of root pose and joint angles per frame. In between, the tool scales the human targets to the robot's proportions, solves inverse kinematics with [Newton](../entities/newton-physics-engine.md) on Warp, and applies corrections such as foot-plant stabilisation. The v0.2 release ships configurations for five humanoids. The post's larger point is the pipeline it sits in: motion from capture, video reconstruction or generative models, all on the SOMA skeleton, retargeted per robot, then converted into motion libraries for tracking-policy training in [SONIC](../entities/gear-sonic.md) or ProtoMotions. The post gives no quantitative results.

## Key claims

### What the tool does
- "A robot cannot simply copy the same joint motion from a human. Its proportions, joint structure, and range of motion are different."
- **Input**: "a Biovision Hierarchy (BVH) animation on the SOMA base skeleton." Representing all sources on that skeleton "gives the retargeter a consistent input."
- **Pipeline** (Figure 1): scale motion targets to the robot, solve inverse kinematics, apply joint limits and "planted-foot stabilization," save as CSV containing "the robot's root position, orientation, and joint angles for each frame."
- **Solver**: IK from Newton, built with NVIDIA Warp. "When a robot cannot match every target at once, IK weights determine which body parts take priority."
- **Output role**: the CSV describes "the desired movement for a downstream learning or control system." It is a reference, not a controller.

### Robots supported in v0.2
Reference configurations and retargeted examples for [Unitree G1](../entities/unitree-g1.md), [Unitree H2](../entities/unitree-h2.md), [Booster T1](../entities/booster-t1.md), and two [AgiBot](../entities/agibot.md) humanoids (X2 Ultra and A3T3), with sample motions from the BONES-SEED dataset.

### Tools for a new or poorly fitting robot
- **Robot Configurator**: load a robot description, align human and robot reference poses, set scale, map skeleton to body parts. Figure 3 shows why alignment matters: with an unaligned reference pose, a one-handed wave on Booster T1 comes out with both arms held outward; after alignment it is a one-handed wave. "Both panels use the same input motion and IK settings."
- **IK weight optimizer** (experimental): tunes per-body-part weights by retargeting "a small set of motions representative of the robot's intended tasks" and "checking how closely and smoothly the robot follows the targets."
- **Foot-plant correction**: "Sliding feet can introduce conflicting targets for a downstream motion-tracking policy: the reference foot moves while the intended action calls for planted contact." Adjusts foot motion over detected contact intervals.
- **Headless batch retargeting** for whole collections once a configuration is settled.

### Where the motion comes from
- **Motion capture**: BONES-SEED (the dataset SONIC released).
- **Video reconstruction**: GEM-X "reconstructs whole-body 3D human motion from a single video using the SOMA body model," with a demo connecting video to G1 retargeting.
- **Generation**: Kimodo (from text and pose constraints) and ARDY (adds interactive steering), both generating on the SOMA skeleton; and [MotionBricks](motionbricks-paper.md).

### Where the motion goes
- **SONIC**: its training workflow "includes a SOMA CSV converter for G1" into SONIC's motion-library format.
- **ProtoMotions**: "another framework for physics-based motion tracking."
- "In either case, the input representation and policy need to match the target robot."
- **MotionBricks**: its G1 model "was trained in part on BONES-SEED motions adapted to G1 with SOMA Retargeter" and was demonstrated on a physical G1 with SONIC executing.
- **MicroDuck** (Figure 4): "human motion from Bones was adapted for the robot and used to train a controller for each clip in physics simulation," shown in Isaac Lab and Newton. Simulation only, one controller per clip.

## Reading it critically

- **No numbers.** No tracking error, no comparison with other retargeters (such as the GMR + PyRoki pipeline the [SONIC paper](sonic-paper.md) reports using for its own 611 hours), no timing, no failure rate. The post shows that the tool works on examples; it does not show how well.
- **It is kinematic.** The output satisfies scaled pose targets, joint limits and a foot-contact heuristic. Balance, dynamics and actuator limits are left to the downstream tracking policy and to simulation, which the post says plainly. The [SimToolReal](simtoolreal-paper.md) result is a reminder of where purely kinematic retargeting ends: for dexterous tool use it reached 8.1% and established no stable grasp.
- **The SONIC link is to the repository, not the paper.** Whether SONIC's published results used SOMA Retargeter or the GMR + PyRoki pipeline the paper describes is not stated; the converter in the SONIC repository suggests SOMA is at least the supported path now.
- **The value is the shared skeleton.** With capture data, single-video reconstruction and two text-to-motion generators all emitting the same skeleton, one configuration per robot turns every source into usable references. That standardisation is the actual product, and it ties the pipeline to NVIDIA's own body model.

## Entities mentioned
- [NVIDIA](../entities/nvidia.md) · [Newton physics engine](../entities/newton-physics-engine.md) · [GEAR-SONIC](../entities/gear-sonic.md) · [MicroDuck](../entities/microduck.md) · [NVIDIA Isaac Lab](../entities/nvidia-isaac-lab.md)
- Robots: [Unitree G1](../entities/unitree-g1.md) · [Unitree H2](../entities/unitree-h2.md) · [Booster T1](../entities/booster-t1.md) · [AgiBot](../entities/agibot.md) (X2 Ultra, A3T3)
- No entity pages: SOMA-X, BONES-SEED / Bones, GEM-X, Kimodo, ARDY, ProtoMotions, NVIDIA Warp

## Concepts touched
- [Motion retargeting](../concepts/robotics/motion-retargeting.md) (new page)
- [Whole-body control](../concepts/robotics/whole-body-control.md): reference motions for tracking policies
- [Cross-embodiment](../concepts/learning/cross-embodiment.md): one human motion, five robot bodies

## Open questions
- Retargeting quality on any metric, and against GMR or other public retargeters. The [repository](soma-retargeter-github.md) names GMR and PyRoki as the work it builds on, and still reports no comparison.
- Which retargeter produced SONIC's published training set.
- ~~Whether the tool handles hands~~ — answered by the [repository](soma-retargeter-github.md): "High-DOF hands are not supported yet."
- What it takes to configure a non-humanoid such as MicroDuck, which is not among the five reference configurations.

## Related sources
- [NVIDIA/soma-retargeter v0.2.0 (GitHub)](soma-retargeter-github.md): the primary for the pipeline, its limits and its licences.
- [SONIC paper](sonic-paper.md): BONES-SEED, and the tracking policy the CSVs feed.
- [MotionBricks paper](motionbricks-paper.md): generative motion trained partly on SOMA-retargeted data.
- [Using AI agents to teach Microduck to walk in simulation](nvidia-microduck-ai-agents-sim-blog.md) · [Microduck with Isaac Lab 3.0](hf-nvidia-microduck-isaac-lab-sim-to-real.md): the MicroDuck simulation work referenced in Figure 4.
