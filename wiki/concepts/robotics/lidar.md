---
title: LiDAR in robots
type: concept
created: 2026-11-16
updated: 2026-11-16
sources: 19
tags: [lidar, 2d-lidar, 3d-lidar, time-of-flight, slam, nav2, localization, range-sensing, safety-sensor, verification, privacy, sensor-bom, rplidar, hesai, livox, unitree-l1, camera-only]
---

# LiDAR in robots

## Definition

**LiDAR** (light detection and ranging) measures distance by timing laser pulses, returning a set of range points rather than an image. Robots in this wiki carry two kinds:

- **2D scanning LiDAR**: a single rotating beam sweeping a plane around the robot, typically 360° at 5–13 Hz with about 12 m range. It is cheap, and it is the standard input for floor-plan SLAM and [Nav2](../../entities/nav2.md) navigation.
- **3D LiDAR**: many beams or a scanning pattern covering a volume, for terrain, people and obstacles at height. Hemispherical units on [Stretch 4](../../entities/stretch.md) and humanoids, and the Unitree L-series and Livox units on quadrupeds and lawnmowers.

The two are different products serving different questions: *where am I on the floor plan* (2D) against *what is around me in 3D* (3D).

## What the wiki's robots carry

| Robot | LiDAR | Use | Source |
|---|---|---|---|
| [TurtleBot 4](../../entities/turtlebot.md) | RPLIDAR-A1, 2D | ROS 2 education, SLAM | [Clearpath](../../sources/clearpath-turtlebot-4.md) |
| [ROSOrin Pro](../../entities/rosorin-pro.md) | COIN-D6, 2D: 360°, 12 m (black objects), 9.5–10.5 Hz, 0.9° | the finished Nav2 + SLAM stack | [user manual](../../sources/hiwonder-rosorin-pro-user-manual.md) |
| [Sourccey](../../entities/sourccey.md) | 2D 360°, 5–13 Hz, 12 m at 70% reflectivity, 8,000 samples/s | LiDAR SLAM | [Vulcan site](../../sources/vulcan-robotics-sourccey-site.md) |
| [NORI A3](../../entities/nori-a3.md) | 2D, 12 m, 8–12 Hz, 0.72° at 10 Hz | home navigation | [product site](../../sources/nori-robotics-site.md) |
| [LeKiwi](../../entities/lekiwi.md) (one build) | RPLidar A1, 2D | SLAM mode alongside vision-only mode | [build write-up](../../sources/alfredang-lerobot-lekiwi-chatgpt.md) |
| [Stretch 4](../../entities/stretch.md) | **dual Hesai J128**, 3D hemispherical | navigation and the active-safety layer | [datasheet](../../sources/hello-robot-stretch-4-datasheet.md) |
| [Agile ONE SN](../../entities/agile-one-sn.md) | 3D, at the waist | humanoid perception | [launch](../../sources/agile-robots-agile-one-sn-launch.md) |
| [Galbot G1](../../sources/galbot-g1-product-page.md), [Galaxea R1](../../entities/galaxea-r1.md) | 3D / 360° (R1: optional second) | mobile manipulation | [Galbot](../../sources/galbot-g1-product-page.md), [R1 guide](../../sources/galaxea-r1-user-guide.md) |
| [Unitree R1](../../sources/unitree-h2-r1-product-pages.md) | Livox MID360 on the top variant | humanoid | [product pages](../../sources/unitree-h2-r1-product-pages.md) |
| [TidyBot++ flywheel rig](../../sources/robot-powered-data-flywheels-paper.md) | Unitree L2, base-mounted | mobile manipulation | [paper](../../sources/robot-powered-data-flywheels-paper.md) |
| [Zeroth M1](../../entities/zeroth-m1.md) | LDS LiDAR + iTOF | home companion, $2,499 | [product page](../../sources/zeroth-m1-product-page.md) |

> [!warning] "LiDAR" on a spec sheet can mean an 8×8 ToF chip
> [Microduck](../../entities/microduck.md) was reported as having "LiDAR". Pollen's own press kit says *"compact LiDAR, an **8×8 time-of-flight matrix**"*, which is 64 depth zones and not a scanning LiDAR at all ([launch page](../../sources/pollen-robotics-microduck.md); the [secondary that propagated it](../../sources/explainx-gemma-4-open-duck-mini.md)). Read the range, the angular resolution and the scan rate, not the word.

## Four jobs it does in this wiki

**1. Navigation and mapping.** 2D LiDAR plus Nav2 is the "solved" navigation layer. When a synthesis says *"navigation is solved by Nav2 + LiDAR SLAM"*, this is what is meant ([Nav2](../../entities/nav2.md); [LeRobot on ROSOrin Pro](../../syntheses/projects/lerobot-on-rosorin-pro.md)). [RTAB-Map](../../entities/rtab-map.md) takes LiDAR as one of its inputs, and [DimOS](../../entities/dimos.md) streams LiDAR frames into a voxel map and spatial memory ([DimOS as a home-AI substrate](../../syntheses/agents/dimos-as-home-ai-substrate.md)). For the wiki's own builds, a ~$100 2D LiDAR beside the RGB-D camera is the recommended fallback once navigation robustness becomes the bottleneck ([XLeRobot bring-up](../../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md)).

**2. A low-dimensional safety sensor you can verify.** [FEARL](../../sources/fearl-verifiable-foundation-models-robot-safety-paper.md) routes a foundation-model policy's output through a tiny MLP that also sees an **11-ray LiDAR scan**. Safety properties are written over the rays (*"if any front ray is under 0.2 m, never move forward"*) and certified by a neural-network verifier for every context the VLA could emit ([safety filters](safety-filters.md), [semantic safety](../safety/semantic-safety.md)). A camera image is far too high-dimensional to verify over; a handful of range rays is not. That makes LiDAR the natural sensor for certified safety layers under learned policies.

**3. A privacy-preserving alternative to cameras.** One bathing-assistance system in the [contact-rich safety survey](../../sources/safe-learning-contact-rich-survey.md) *deliberately downgrades its vision system to LiDAR for ethical reasons* (§3.2.4). Range points show where a body is without showing the body, which matters for [assistive](assistive-robotics.md) and in-home robots. The caveat is that LiDAR is still data: Unitree's G1 publishes audio, video and LiDAR on unencrypted local DDS topics anyone on the network segment can read ([attack-vectors paper](../../sources/cai-humanoid-robots-attack-vectors-paper.md); [robot security](robot-security.md)).

**4. A line item that has commoditized.** A $2,499 home device now carries LDS LiDAR, iTOF, a camera and a 3-mic array ([consumer value chain](../../syntheses/society/consumer-robotics-value-chain.md)), and 2D LiDAR ships in sub-$1k kits (Sourccey, ROSOrin).

## The camera-only counter-position

Several lines in the wiki deliberately do without it:

- **Visual navigation policies** map camera frames and a goal to waypoints *"with no map, LiDAR, or explicit localization"* ([visual navigation policies](visual-navigation-policies.md)). ViNT names *"cannot … ingest LiDAR"* as a limitation ([ViNT](../../sources/vint-paper.md)).
- **Real-to-sim capture without a scanner:** Niantic and NVIDIA reconstruct a space at metric scale from *"a few minutes of video from an off-the-shelf 360° camera… no LiDAR, tripod stations, or specialized capture workflow"* ([Niantic × Flexion](../../sources/niantic-flexion-nvidia-sim2real.md)).
- [Foundation Robotics](../../entities/foundation-robotics.md) is reported (not on its own page) to use camera-only perception and explicitly reject LiDAR.

> [!note] How to read the split
> The camera-only argument is about *what the learned policy consumes*. The LiDAR argument is about *what the classical stack and the safety layer need*. They are not really in conflict: [Stretch 4](../../entities/stretch.md) carries 3D LiDAR for navigation and safety while its learned policies use cameras. The live question is whether learned navigation becomes good enough to drop the classical layer, and with it the cheapest verifiable safety signal.

## Related concepts

- [Visual relocalization and mapping](visual-relocalization-and-mapping.md) — the camera-based half of localization
- [Visual navigation policies](visual-navigation-policies.md) — the learned, LiDAR-free alternative
- [Safety filters](safety-filters.md) — LiDAR rays as the verifiable input
- [Robot security](robot-security.md) — sensor streams on unencrypted buses
- [Assistive robotics](assistive-robotics.md) — privacy-preserving sensing in the home
- [Tactile sensing](tactile-sensing.md) — the other sensor class this wiki tracks

## Current state

2D LiDAR is a solved, commoditized component: about 12 m, 5–13 Hz, under $100 at the hobby end, and the default for SLAM under Nav2. 3D LiDAR is standard on 2026 humanoids and premium mobile manipulators. In this wiki its most distinctive use is not mapping but **verification**: a few range rays are the input on which a certified safety layer under a VLA has actually been demonstrated. Whether learned camera-only navigation displaces it depends less on navigation quality than on what replaces that verifiable signal.

## Mentioned in

> [!note] Curated list — about 35 source pages mention LiDAR; the ones below shaped this page.

- [FEARL](../../sources/fearl-verifiable-foundation-models-robot-safety-paper.md) — LiDAR rays as the verified safety input under a foundation-model policy
- [Safe learning for contact-rich tasks (survey)](../../sources/safe-learning-contact-rich-survey.md) — LiDAR chosen over vision for ethical reasons
- [Stretch 4 datasheet](../../sources/hello-robot-stretch-4-datasheet.md) — dual Hesai J128
- [ROSOrin Pro user manual](../../sources/hiwonder-rosorin-pro-user-manual.md), [Vulcan / Sourccey](../../sources/vulcan-robotics-sourccey-site.md), [NORI](../../sources/nori-robotics-site.md), [TurtleBot 4](../../sources/clearpath-turtlebot-4.md) — 2D LiDAR specs at the low end
- [Pollen Microduck launch](../../sources/pollen-robotics-microduck.md) — the ToF-marketed-as-LiDAR case
- [CAI attack vectors](../../sources/cai-humanoid-robots-attack-vectors-paper.md) — LiDAR on unencrypted DDS
- [Niantic × Flexion](../../sources/niantic-flexion-nvidia-sim2real.md), [ViNT](../../sources/vint-paper.md) — the camera-only side
