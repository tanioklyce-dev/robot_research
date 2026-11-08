---
title: Robot platforms — comparison
type: synthesis
created: 2026-05-08
updated: 2026-11-08
tags: [robots, hardware, comparison, list, manipulators, mobile-robots, aloha, mobile-aloha, xlerobot, lekiwi, yuri, bimanual, humanoids, unitree-g1, agile-one-sn, fauna-sprout, tiago-pro, nori-a3, home-robots, quadrupeds]
---

# Robot platforms — comparison

A reference list of robot platforms with entity pages in this wiki, organized by tier and type, with comparison axes and "what each is used for in the wiki." Intended as a quick-lookup page when a paper says "we evaluate on X" and you want to know how X relates to other platforms ingested here. Refreshed 2026-11-08. For what to buy for a home, see [Household robots compared](household-robots-comparison.md).

## At a glance

| Robot                          | Tier        | Type                  | Compute                   | Arm DOF           | Mobility       | Primary use here                                                                         |
| ------------------------------ | ----------- | --------------------- | ------------------------- | ----------------- | -------------- | ---------------------------------------------------------------------------------------- |
| [Franka Panda](../../entities/franka-panda.md) | Research    | Tabletop manipulator  | External GPU              | 7                 | None           | DROID, V-JEPA 2, V-JEPA 2.1, JEPA-WMs, RUM cross-embodiment. The default real-robot arm. |
| [xArm 7](../../entities/xarm-7.md)             | Commercial  | Tabletop manipulator  | External                  | 7                 | None           | RUM cross-embodiment transfer target (~10pt drop vs Stretch).                            |
| [Stretch](../../entities/stretch.md)           | Research    | Mobile manipulator    | Onboard (Intel NUC; optional Jetson Orin NX on Stretch 4) | Telescoping + 3-axis wrist | Holonomic on Stretch 4; diff-drive before | RUM zero-shot generalist policies; stretch_ai LLM agent (Stretch 3). **Stretch 4: $29,950, shipping.** |
| [Mobile ALOHA](../../entities/aloha.md)        | Research    | Bimanual mobile manip | Onboard (laptop + RTX 3070 Ti) | 2× 6 (ViperX 300) | Diff-drive (AgileX Tracer) | ACT + Diffusion Policy + VINN benchmarking on bimanual mobile manip; whole-body teleop; $32k. |
| [Yuri](../../entities/yuri.md) ([Sensori](../../entities/sensori-robotics.md)) | Research    | Bimanual manip (Desktop / Mobile) | Onboard (Jetson AGX Orin 64 GB) | 2× 7 (OpenArm+) | None (Desktop) / wheeled OpenBase (Mobile) | Integrated Physical-AI data-collection rig; bilateral force-feedback teleop out-of-box; LeRobot recording; GR00T/π0/X-VLA/SmolVLA support. Quote-only price. |
| [OpenArm](../../entities/openarm.md) ([Enactic](../../entities/enactic.md)) | Research    | Bimanual manip (tabletop) | External PC (CAN-FD)     | 2× 7 (+ gripper)  | None (FAQ: no mobile base planned) | **$6,500 bimanual** open-hardware 7-DOF QDD arm (4.1 kg nominal payload); bilateral force-feedback teleop; Cell evaluation enclosure; the upstream of Yuri's OpenArm+ and UME's test arm. |
| [Unitree G1](../../entities/unitree-g1.md) (EDU / EDU+) | Research    | Bipedal humanoid      | Onboard (not specified on its page here; the [GR00T E2E workflow](../../sources/nvidia-gr00t-e2e-workflow-docs.md) deploys via Jetson Thor) | 23–29 joints by config; 3-finger 7-DoF hand in dexterous configs | Legs | **De-facto whole-body-control benchmark** (SONIC, MotionBricks, BumbleBee); GR00T's main humanoid target; [HIW-500](../../entities/hiw-500.md) home teleop data; from $13.5K without SDK; EDU by quote. |
| [Agile ONE SN](../../entities/agile-one-sn.md) ([Agile Robots](../../entities/agile-robots.md)) | Research (**announced, early 2027**) | Bipedal humanoid (reference platform) | Onboard (Jetson Thor 128 GB + Intel i3 N305) | 31 body DoF + 2× 20-DoF tactile hands (71 total) | Legs | **NVIDIA's reference humanoid**: GR00T 1.7 + GR00T WBC preinstalled; URDF/USD for Isaac Sim/Lab. Price unannounced; weight 43 vs 40 kg ⚠. |
| [Fauna Sprout](../../entities/fauna-robotics.md) ([Fauna Robotics](../../entities/fauna-robotics.md)) | Research    | Bipedal humanoid (developer platform) | Onboard (Jetson AGX Orin 64 GB) | 29 DoF total (6 per arm) | Legs | 107 cm / 22.7 kg soft-shelled developer humanoid; whole-body teleop; "Request Robot," about $50k by press reports; Fauna is now an Amazon company. Not yet used in any ingested paper. |
| [TIAGo Pro](../../sources/pal-tiago-pro-product-page.md) ([PAL Robotics](../../entities/tiago.md)) | Research    | Bimanual mobile manip | Onboard (not stated on page) | 2× 7 (single-arm option) | Wheeled | Current-generation TIAGo; 3 kg per arm; ROS 2; quote-only. |
| [Reachy 2](../../entities/reachy.md) ([Pollen](../../entities/pollen-robotics.md)) | Research    | Bimanual mobile manip | Onboard CPU | 2× 7 | Omni base option | Open-source; VR teleoperation; about 3 kg per arm. |
| [YOR](../../entities/yor.md) | Research    | Bimanual mobile manip | Onboard (Jetson AGX Orin or Thor) | 2× 6 (AgileX PiPER) | Omnidirectional swerve, telescopic lift | Open source, about $9,250 in parts; 1.5 kg per arm; one proof-of-concept task. |
| [TidyBot++](../../entities/tidybot-plus-plus.md) | Research    | Holonomic base (arm of choice) | Onboard mini PC | Kinova Gen3 in reference build | Holonomic powered casters | Open source, $5–6k before arm; six imitation-learning tasks in a real apartment. |
| [Galbot G1](../../entities/galbot.md) | Commercial  | Bimanual mobile manip | Onboard (Jetson AGX Orin 64 GB) | 2× 7 | Omnidirectional, lifting torso | Retail and warehouse deployment claims in China; 5 kg per arm; no published price. |
| [Unitree G1-D](../../sources/unitree-g1-product-page.md) | Research    | Bimanual mobile manip (data collection) | Not stated on page | 2× 7 | Wheeled, 1-DOF column | Unitree's wheeled data-collection platform with training tooling; quote-only. |
| [Unitree H2](../../entities/unitree-h2.md) | Research    | Full-size bipedal humanoid | 2070 TOPS option (vendor) | 2× 7 | Legs | $29,900 without SDK or hands; EDU by quote; listed as unavailable on 2026-11-08. |
| [Unitree R1](../../entities/unitree-r1.md) | Educational / research | Small bipedal humanoid | Not stated here | 4–5 per arm | Legs | From $4,900; R1 EDU $10,500 is the version with secondary development. |
| [XLeRobot](../../entities/xlerobot.md)         | Educational | Bimanual mobile manip | External PC (or onboard [Jetson Orin Nano](../../entities/jetson-orin-nano.md)) | 2× (5+1) SO-101 + 2-DoF neck | Holonomic (LeKiwi omni) | **Cheapest bimanual mobile manipulator** ($660 tethered → $1.3k untethered); LeRobot/SO-101; onboard-Jetson untethered build + on-edge VLA benchmarks ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)). |
| [LeKiwi](../../entities/lekiwi.md) ([SIGRobotics-UIUC](../../entities/sigrobotics-uiuc.md)) | Educational | Mobile manipulator    | Onboard [Raspberry Pi 5](../../entities/raspberry-pi-5.md), heavy compute on a laptop over Wi-Fi (Jetson Orin Nano swap documented) | 5+1 ([SO-101](../../entities/so-arm101.md)) | Holonomic (3-wheel Kiwi omni) | **The LeRobot ecosystem's standard mobile manipulator**: ~€230 in the [LeRobot paper](../../sources/lerobot-iclr-2026-paper.md); Apache-2.0, 3D-printed, Seeed kits. The base under [XLeRobot](../../entities/xlerobot.md); prize hardware in 22 of 30 [hackathon](../../sources/lerobot-worldwide-hackathon-2025-winners.md) placings; an embodiment in [LeHome](../../sources/lehome-benchmark-paper.md). |
| [ROSOrin Pro](../../entities/rosorin-pro.md)   | Educational | Mobile manipulator    | Jetson Orin Nano          | 6 (HX-12H servos) | Diff/Ackermann | OpenClaw LLM-agent (via Hiwonder's openclaw_controller ROS 2 bridge); LeWM-feasibility candidate.                                |
| [ROSOrin](../../entities/rosorin.md)           | Educational | Mobile robot (no arm) | Jetson Orin Nano          | 0                 | Diff/Ackermann | LLM-agent curriculum (cloud + offline).                                                  |
| [TurtleBot](../../entities/turtlebot.md)       | Educational | Mobile robot (no arm) | Raspberry Pi (gen 4)      | 0                 | Diff-drive     | Reference / comparison point — not used directly in any wiki source.                     |
| [NORI A3](../../entities/nori-a3.md) | Home / prosumer | Bimanual mobile manip | [Raspberry Pi 5](../../entities/raspberry-pi-5.md) + laptop | 2× 7+1 | Wheeled, lift | **$1,688**; shipping in batches by press reports; no depth sensor or published results. |
| [Flourish 1](../../entities/flourish-1.md) | Home / consumer | Bimanual mobile manip | Raspberry Pi + cloud | DOF unpublished | Six wheels, lift | **$3,555**, 50 units, December 2026; owner teaches by phone; 1.5 kg limit. |
| [Sourccey](../../entities/sourccey.md) | Home / developer | Bimanual mobile manip | Raspberry Pi 5 | 2× 5+1 | Mecanum, lift | Open source; launch November 2026, ship December; price unpublished. |
| [Weave Isaac 1](../../entities/weave-robotics.md) | Home / consumer | Bimanual mobile manip | Not stated | 2× 6 | Wheeled, collapsible torso | **$7,999** or $449/mo; pre-order; teleoperation-assisted; no SDK. |
| [SwitchBot onero H1](../../entities/switchbot-onero-h1.md) | Home / consumer | Bimanual mobile manip | Not stated | Not on listing | Wheeled | **$9,999**; listed as unavailable. |
| [Sunday Memo](../../entities/sunday-robotics.md) | Home (beta) | Bimanual mobile manip | Onboard (unspecified) | 2× 7 | Wheeled | Not for sale; beta "late 2026"; strongest dishwasher demonstration. |
| [UniX AI Panther](../../entities/unix-ai-panther.md) | Commercial / home | Bimanual mobile manip | Not stated | 2× 8 | 4WS + 4WD, 80 cm lift | Vendor claims household deployment; no price. |
| [Roborock Saros Z70](../../entities/roborock-saros-z70.md) | Consumer | Robot vacuum with arm | Onboard | 5-axis arm, 300 g | Wheeled | Shipping; good vacuum, unreliable autonomous arm. |
| [Unitree Go2](../../entities/unitree-go2.md) / As2 | Educational / research | Quadruped | Onboard | 0 | Legs | Go2 from $1,600; As2 Air $3,100 ([store](../../sources/unitree-h2-r1-product-pages.md)). |
| [Spot](../../entities/spot.md) | Commercial | Quadruped | Onboard | Optional arm | Legs | Heavy-tier inspection and research platform. |

## By tier

### Research-grade ($10k–$30k+)
- **[Franka Panda](../../entities/franka-panda.md)** (UFactory's commercial tier sits adjacent). 7-DOF torque-controlled arm, 1 kHz FCI control. Standard real-robot platform across the JEPA / VLA / DROID literature. Used in V-JEPA 2 (zero-shot pick-and-place), V-JEPA 2.1 (real-Franka grasping +20pt), JEPA-WMs (Franka unroll decode), RUM (transferred to via custom mount), DROID (single embodiment for entire dataset).
- **[xArm 7](../../entities/xarm-7.md)** (UFactory). Commercial alternative to Franka. Same 7-DOF tabletop class. Appears in this wiki only as RUM's cross-embodiment transfer target — but a useful data point for how BC policies generalize across hardware (~10pt drop).
- **[Stretch](../../entities/stretch.md)** (Hello Robot; Stretch 4 launched 2026-05-12). Mobile manipulation: telescoping arm + omnidirectional holonomic base + dual hemispherical 3D LiDAR + Luxonis OAK cameras on Stretch 4 (RealSense on earlier generations). **Stretch 3 is sold out; `stretch_ai` still [documents only Stretch 3](../../sources/stretch-ai-github-readme.md).** Anchor of the NYU + Hello Robot research line ([RUM](../../entities/robot-utility-models.md), [stretch_ai](../../entities/stretch-ai.md) LLM agent, [Dobb·E](../../entities/dobb-e.md)). The de-facto research-tier single-arm mobile manipulator for academic work in 2024–2026.
- **[Mobile ALOHA](../../entities/aloha.md)** (Stanford; Fu, Zhao, Finn 2024). Bimanual mobile manipulator with whole-body teleoperation. 4× [ViperX 300](../../entities/viperx-300.md) (2 leaders + 2 followers) + AgileX Tracer base + 3 webcams + RTX 3070 Ti laptop = **$32k**. Comparable in budget to a single Franka arm, ~6× cheaper than PR2/TIAGo. Anchors the [ACT](../../entities/act.md) + co-training-with-static-data IL pattern.
- **[TIAGo Pro](../../sources/pal-tiago-pro-product-page.md)** ([PAL Robotics](../../entities/tiago.md)). Two 7-DoF arms at 3 kg each on ROS 2, quote-only. **[Reachy 2](../../entities/reachy.md)** is the open-source option in the same bimanual class, with about 3 kg per arm.
- **[YOR](../../entities/yor.md)** (NYU-led; 2026) and **[TidyBot++](../../entities/tidybot-plus-plus.md)** (Princeton and Stanford; 2024). Open-source builds well below Mobile ALOHA's cost. YOR is two 6-DoF arms on a swerve base with a lift, for about $9,250 ([paper](../../sources/yor-paper.md)). TidyBot++ is a $5–6k holonomic base that takes an arm of your choice, and has the better published household results ([paper](../../sources/tidybot-plus-plus-paper.md)).
- **[Yuri](../../entities/yuri.md)** ([Sensori Robotics](../../entities/sensori-robotics.md), Southlake TX; 2026). **Integrated, supported** bimanual Physical-AI rig: 2× 7-DOF backdrivable **OpenArm+** arms + RealSense head + Jetson AGX Orin 64 GB, in Desktop (benchtop) or Mobile (wheeled **OpenBase**) form. Its differentiators are **out-of-the-box bilateral force-feedback teleoperation** (OpenLeader arms + Quest 3), a day-one [LeRobot](../../entities/lerobot.md)-recording + VLA-eval stack (GR00T / π0 / X-VLA / SmolVLA), and US-based support — "a complete robot, not a box of parts." Arms/base released as open hardware (OpenArm+ / OpenBase). Price is quote-only but the spec places it in the **research tier**, adjacent to Mobile ALOHA. The bimanual counterpart to Sensori's integrator role vs. the self-assembled [LeRobot](../../entities/lerobot.md) kits.

- **Research humanoids.** These are the humanoids a lab can actually get. The closed, industrial and educational humanoids are in the [Humanoid platforms survey](humanoid-platforms-survey.md).
  - **[Unitree G1](../../entities/unitree-g1.md)** (from $13.5K without SDK; EDU by quote). The whole-body-control benchmark robot and GR00T's main humanoid target. Unlike the arms and mobile manipulators above, its value here is **locomotion and whole-body control**. Its manipulation results are still thin: 3-finger hands, and no published UnifoLM success rates.
  - **[Unitree H2](../../entities/unitree-h2.md)** ($29,900 without SDK or hands; EDU by quote) and **[Unitree R1](../../entities/unitree-r1.md)** (from $4,900; EDU $10,500). Both follow the G1 pattern: the listed price excludes secondary development ([Unitree](../../sources/unitree-h2-r1-product-pages.md)).
  - **[Agile ONE SN](../../entities/agile-one-sn.md)** (announced 2026-10-21, due early 2027, unpriced). The first humanoid sold with GR00T 1.7 and whole-body control as the **factory default**. It has 20-DoF tactile hands and a 128 GB Jetson Thor. It is listed here because it is sold as an R&D platform, but it cannot be bought yet ([Agile release](../../sources/agile-robots-agile-one-sn-launch.md), [NVIDIA release](../../sources/nvidia-isaac-platform-gtc-berlin-2026.md)).
  - **[Fauna Sprout](../../entities/fauna-robotics.md)** ("Request Robot"; about $50k by press reports). A smaller, softer developer humanoid on a Jetson AGX Orin. Specs come only from the vendor [product page](../../sources/fauna-robotics-sprout.md).

### Educational (sub-$1k–$5k)
- **[XLeRobot](../../entities/xlerobot.md)** (open-source, LeRobot ecosystem). **Bimanual** mobile manipulator: 2× [SO-101](../../entities/so-arm101.md) arms (5+1 DoF each) + 2-DoF neck on a [LeKiwi](../../entities/lekiwi.md) holonomic omni base; 90% 3D-printed; **$660 tethered** (external PC) up to **~$1.3k untethered** with onboard [Jetson Orin Nano](../../entities/jetson-orin-nano.md). The educational-tier analog to [Mobile ALOHA](../../entities/aloha.md) at ~1/25th the cost — the wiki's **cheapest bimanual mobile manipulator**. The [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) build adds onboard compute, a Tri-Bus power topology, and the wiki's first on-edge VLA latency numbers; see [Jetson onboard compute for XLeRobot](jetson-onboard-compute-xlerobot.md).
- **[LeKiwi](../../entities/lekiwi.md)** ([SIGRobotics-UIUC](../../entities/sigrobotics-uiuc.md); kits from [Seeed Studio](../../entities/seeed-studio.md)). A single-arm mobile manipulator: one [SO-101](../../entities/so-arm101.md) on a 3-wheel holonomic Kiwi base driven by STS3215 servos, with a [Raspberry Pi 5](../../entities/raspberry-pi-5.md) onboard. Apache-2.0 and 3D-printed. It is the **cheapest mobile manipulator in the wiki**, listed at ~€230 in the [LeRobot paper](../../sources/lerobot-iclr-2026-paper.md), and the platform [LeRobot](../../entities/lerobot.md) treats as its standard mobile robot. It ranks below XLeRobot, which is two of its arms on the same base, and far below [Stretch](../../entities/stretch.md) in reach, lift and sturdiness. The Pi cannot run a policy, so a laptop does the inference unless you swap in a Jetson Orin Nano ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)). Payload and reliability are unmeasured.
- **[ROSOrin Pro](../../entities/rosorin-pro.md)** (Hiwonder). 6-DOF arm + mobile base + Jetson Orin Nano. Ships upstream [OpenClaw](../../entities/openclaw.md) as the LLM-agent brain plus Hiwonder's [`openclaw_controller`](../../entities/openclaw-controller.md) ROS 2 bridge module that wires it to the robot. Closest educational-tier analog to Stretch + stretch_ai, but with a real arm (vs Stretch's telescoping single-DOF arm).
- **[ROSOrin](../../entities/rosorin.md)** (Hiwonder). No-arm sibling of ROSOrin Pro. Mobile robot only; Jetson Orin Nano + cloud/offline LLM-agent curriculum.
- **[TurtleBot](../../entities/turtlebot.md)** (multiple vendors per generation; current: Open Robotics / Clearpath). Reference educational mobile robot since 2010. Lacks the agentic-AI bundling that ROSOrin / ROSOrin Pro now ship.

### Home and consumer robots ($1k–$10k)

*Added 2026-11-08.* A new tier of wheeled two-arm robots sold for homes: [NORI A3](../../entities/nori-a3.md), [Flourish 1](../../entities/flourish-1.md), [Sourccey](../../entities/sourccey.md), [Weave Isaac 1](../../entities/weave-robotics.md) and [SwitchBot onero H1](../../entities/switchbot-onero-h1.md), with [Sunday Memo](../../entities/sunday-robotics.md) in beta. Nearly all are pre-order, and none has published independent results. They are evaluated in [Household robots compared](household-robots-comparison.md).

## By function

### Tabletop manipulators (no mobility)
[Franka Panda](../../entities/franka-panda.md), [xArm 7](../../entities/xarm-7.md).

### Mobile manipulators (arm + mobility)
**Single-arm:** [Stretch](../../entities/stretch.md) (research; Stretch 4 current), [ROSOrin Pro](../../entities/rosorin-pro.md) and [LeKiwi](../../entities/lekiwi.md) (educational).
**Bimanual:** [Mobile ALOHA](../../entities/aloha.md) (research, $32k) and [XLeRobot](../../entities/xlerobot.md) (educational, $660–1.3k) — the two ingested bimanual *mobile* manipulators, ~25× apart in cost; plus [Yuri](../../entities/yuri.md) (Sensori; Desktop is bimanual tabletop, Mobile adds a wheeled base), the integrated force-feedback-teleop research-tier option. Also [TIAGo Pro](../../sources/pal-tiago-pro-product-page.md), [Reachy 2](../../entities/reachy.md), [YOR](../../entities/yor.md), [Galaxea R1](../../entities/galaxea-r1.md) and [G1-D](../../sources/unitree-g1-product-page.md) at research tier, [Galbot G1](../../entities/galbot.md) commercially, and the home tier above.

### Humanoids (legs + arms)
[Unitree G1](../../entities/unitree-g1.md) (research, buyable), [Unitree H2](../../entities/unitree-h2.md) and [R1](../../entities/unitree-r1.md) (research and educational), [Fauna Sprout](../../entities/fauna-robotics.md) (research, quote), [Agile ONE SN](../../entities/agile-one-sn.md) (research, announced). The wheeled research humanoids, [Galaxea R1](../../entities/galaxea-r1.md) and [Reachy 2](../../entities/reachy.md), are bimanual mobile manipulators in function. Their details are in the [survey](humanoid-platforms-survey.md#wheeled-humanoids--the-counterargument-tier-walden).

### Quadrupeds
[Unitree Go2](../../entities/unitree-go2.md), [Go1](../../entities/unitree-go1.md), [A1](../../entities/unitree-a1.md), [Spot](../../entities/spot.md).

### Mobile robots without arms
[ROSOrin](../../entities/rosorin.md), [TurtleBot](../../entities/turtlebot.md).

## Cross-tier observations

### "Research-grade" vs "educational" is a real boundary
- **Repeatability and torque** — Franka's 1 kHz torque control + research-grade servos vs ROSOrin Pro's HX-12H educational bus servos. Affects what kinds of policies can transfer cleanly. The RUM cross-embodiment story (~10pt drop, Stretch → xArm 7) is across two *commercial* arms; transferring to educational arms is a much larger gap.
- **Data availability** — every research-tier robot above has at least one large public dataset attached ([DROID](../../entities/droid.md) for Franka, [RUM](../../entities/robot-utility-models.md) for Stretch). Educational-tier robots don't yet.
- **Software stack maturity** — Franka has libfranka + frankx + ROS bindings + every major sim ([MuJoCo](../../entities/mujoco.md), [Isaac Sim](../../entities/nvidia-isaac-sim.md), Pinocchio). ROSOrin Pro has Hiwonder's stack + ROS 2 + Gazebo. Both functional; the research-tier ecosystems are deeper.

### Educational tier is converging on "Jetson + LLM agent + ROS 2"
The [ROSOrin](../../entities/rosorin.md) / [ROSOrin Pro](../../entities/rosorin-pro.md) / [OpenClaw](../../entities/openclaw.md) stack represents a generational update of the [TurtleBot](../../entities/turtlebot.md) educational role: same target audience (CS / robotics students learning ROS), but with **Jetson Orin Nano compute (~10× the Raspberry Pi)** and a **bundled agentic-AI / LLM-agent curriculum** that TurtleBot doesn't have. The interesting question is whether TurtleBot 5 (or whichever follows) will close that gap, or whether Hiwonder's lineage takes over the educational niche entirely.

### Research-tier mobile manipulation = Stretch (single-arm) or Mobile ALOHA (bimanual)
Historically two options in this wiki: **[Hello Robot Stretch](../../entities/stretch.md)** for single-arm + telescoping reach, and **[Mobile ALOHA](../../entities/aloha.md)** for bimanual + whole-body teleop. Commercial bimanual options now exist as well, listed under research tier. ROSOrin Pro (single-arm) and **[XLeRobot](../../entities/xlerobot.md) (bimanual)** are the educational-tier alternatives; [Spot](../../entities/spot.md) is the heavy-tier quadruped alternative, and production [Atlas](../../entities/atlas.md) is committed to Hyundai and DeepMind through 2026. When an academic paper says "real-robot mobile manipulation," **Stretch is implied for single-arm work, Mobile ALOHA for bimanual**. Both ship onboard compute and sit in the academic budget band (about $30–32k for Stretch 4 and Mobile ALOHA).

> [!note] The educational-tier bimanual gap is now filled
> Until XLeRobot, bimanual mobile manipulation in this wiki meant **Mobile ALOHA at $32k** — research-tier only. [XLeRobot](../../entities/xlerobot.md) brings the same form factor (dual arms + mobile base) to **$660–1.3k** via 3D printing + [LeRobot](../../entities/lerobot.md)-ecosystem [SO-101](../../entities/so-arm101.md) arms, with an onboard-Jetson untethered path ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md)). The open question is capability: XLeRobot's 1 kg/arm payload + ~40 cm reach + hobby servos are a real step down from ViperX-300-class hardware — the cost collapse is genuine, the capability parity is not.

### Tabletop manipulation = Franka, with xArm 7 as second option
Same pattern — when a paper says "real-robot manipulation" without further qualification, **Franka is implied**. xArm 7 appears as a transfer target rather than a primary platform.

**Added 2026-09-13 — the open 7-DOF tier has a name.** [OpenArm](../../entities/openarm.md) sits between the SO-101 (~$120 arm) and the Franka (~$30k) at $6,500 bimanual with a 4.1 kg nominal payload, and both [Yuri](../../entities/yuri.md) and [UME](../../entities/ume.md)'s test rig derive from it.

## What's missing from this wiki

Worth flagging robot platforms that show up in adjacent literature but don't have entity pages here yet:

- ~~**Boston Dynamics Spot** — quadruped reference platform (no entity page).~~ **Filed** as [Spot](../../entities/spot.md) (2026-05-09) alongside [Atlas](../../entities/atlas.md); [Unitree Go2](../../entities/unitree-go2.md) filed 2026-07-27 as the cheap-tier counterpart. Quadrupeds remain the **thinnest-sourced** platform tier here — neither entity is grounded in a primary technical source (Spot comes from a vendor blog, Go2 from an [Anthropic policy article](../../sources/anthropic-project-fetch-robot-dog.md) that never even names the model). Ingested navigation papers do use quadrupeds, notably [Go1](../../entities/unitree-go1.md), and [A1](../../entities/unitree-a1.md) anchors learned locomotion.
- **Pi (Physical Intelligence) hardware** — already in known gaps as needing a primary source.
- ~~**ALOHA / ViperX bimanual setup** — Stanford bimanual teleop platform; referenced indirectly via Chelsea Finn but no entity page.~~ **Filed 2026-05-25** as [ALOHA / Mobile ALOHA](../../entities/aloha.md) + [ViperX 300](../../entities/viperx-300.md) entities via the [Mobile ALOHA paper](../../sources/mobile-aloha-paper.md) ingest.
- **xArm 6** (UFactory's 6-DOF cousin to xArm 7) — sometimes cited as a cheaper alternative.
- **UR5 / UR10 / UR16** (Universal Robots) — collaborative arms common in industrial settings; not yet appearing in our literature.
- **Humanoids beyond the research tier** — the closed, industrial and educational humanoids are in the [Humanoid platforms survey](humanoid-platforms-survey.md), which covers 23 platforms. The research humanoids are now in the tables above.

## Sources used in this synthesis

- Per-platform entity pages: [Franka Panda](../../entities/franka-panda.md), [xArm 7](../../entities/xarm-7.md), [Stretch](../../entities/stretch.md), [Mobile ALOHA](../../entities/aloha.md), [XLeRobot](../../entities/xlerobot.md), [ROSOrin Pro](../../entities/rosorin-pro.md), [ROSOrin](../../entities/rosorin.md), [TurtleBot](../../entities/turtlebot.md), [LeKiwi](../../entities/lekiwi.md), [Unitree G1](../../entities/unitree-g1.md), [Agile ONE SN](../../entities/agile-one-sn.md), [Fauna Robotics](../../entities/fauna-robotics.md).
- [Agile Robots launches Agile ONE SN](../../sources/agile-robots-agile-one-sn-launch.md) · [NVIDIA advances Isaac platform (GTC Berlin)](../../sources/nvidia-isaac-platform-gtc-berlin-2026.md) · [Fauna Sprout product page](../../sources/fauna-robotics-sprout.md).
- **Added 2026-11-08:** [Unitree H2 and R1](../../sources/unitree-h2-r1-product-pages.md) · [Unitree G1 and G1-D](../../sources/unitree-g1-product-page.md) · [TIAGo Pro](../../sources/pal-tiago-pro-product-page.md) · [Stretch 4 launch](../../sources/hello-robot-stretch-4-launch.md) · [stretch_ai README](../../sources/stretch-ai-github-readme.md) · [Roborock Saros Z70](../../sources/roborock-saros-z70.md) · home-tier entity pages linked above.
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — XLeRobot untethered build (cost, DoF, payload, onboard compute).
- Companion source pages: [RUM Paper](../../sources/robot-utility-models-paper.md) (cross-embodiment data), [DROID](../../entities/droid.md) entity (Franka data scale), [ROSOrin Pro User Manual](../../sources/hiwonder-rosorin-pro-user-manual.md) (educational-tier specs).

## Related

- [index.md](../../index.md) — Robot platforms section (the live list).
- [LeWM on ROSOrin Pro — feasibility analysis](../projects/lewm-on-rosorin-pro-feasibility.md) — uses the research-vs-educational tier distinction extensively.
- [Household robots compared](household-robots-comparison.md) — what to buy for research and for a home.
- [LLM-agent architecture across stacks](../agents/llm-agent-architecture-across-stacks.md) — compares stretch_ai (Stretch) vs ROSOrin (cloud/offline) vs OpenClaw (ROSOrin Pro).
- [Sim-heavy vs real-data paths](../simulators/sim-heavy-vs-real-data-paths.md) — anchors the "what robot underpins each path" question.

## Open questions / TBD

> [!note] Tier boundary in cross-embodiment transfer
> RUM measures Stretch → xArm 7 (~10pt drop). The research-tier-to-educational-tier drop is **not measured anywhere in this wiki**. Whether a Stretch-trained policy transfers to ROSOrin Pro is the obvious next question; nobody has published on it yet.

> [!note] Humanoid scope
> Added 2026-10-23. Only the **research humanoids a lab can get** are listed here: the G1, Sprout, and Agile ONE SN, which is announced. The closed-development, industrial, educational and paper-embodiment humanoids are in the [Humanoid platforms survey](humanoid-platforms-survey.md), which covers 23 platforms. The page's research-vs-educational comparison axes (repeatability and torque, attached datasets, stack maturity) favour the G1 on datasets and stack maturity. Agile ONE SN has neither yet.
