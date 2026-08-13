---
title: XLeRobot
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-08-13
sources: 16
tags: [xlerobot, mobile-manipulator, dual-arm, lerobot, lekiwi, so-arm101, low-cost, household-robot, embodied-ai, sourccey]
---

**Open-source hardware:** [github.com/Vector-Wangel/XLeRobot](https://github.com/Vector-Wangel/XLeRobot) (Apache 2.0). Docs: [xlerobot.readthedocs.io](https://xlerobot.readthedocs.io).

**XLeRobot** — $660 household **dual-arm mobile manipulator** built by [Gaotian "Vector" Wang](vector-wang.md). Composes two [SO-ARM101](so-arm101.md) arms (~40 cm reach each) onto a [LeKiwi](lekiwi.md)-class wheeled base, with optional cameras and Raspberry Pi compute. 90% 3D-printed. Apache 2.0. Version 0.3.0 released August 30, 2025. Project tagline: *"Bring Embodied AI to Every Family Around the World" at a price cheaper than an iPhone*.

## Specs

- **Arms**: 2× [SO-ARM101](so-arm101.md), each ~40 cm reach, 600–1000 g payload
- **Base**: wheeled mobile platform inspired by [LeKiwi](lekiwi.md) / Bambot (2-wheel, mecanum, and 3× omni-wheel variants documented). **Note:** an owner build in the [fleet framework](../syntheses/projects/fleet-agentic-framework.md) uses the **2-wheel differential** variant (non-holonomic — turn-then-approach, no sideways strafe), *not* the LeKiwi 3-wheel omni base the intro implies; photo there.
- **Actuators**: **17× Feetech STS3215** servos at 12 V (same family as SO-100/SO-101) — per-servo ~30 mA idle / ~180 mA no-load running / **2.7 A stall** ([RobotShop STS3215](https://www.robotshop.com/products/feetech-12v-30kgcm-magnetic-encoding-servo-sts3215))
- **Mass**: ~12 kg (intentionally adult-liftable)
- **Vertical workspace**: 0.5 m – 1.25 m (fixed-height torso, no lift)
- **Reach from cart edge**: ~0.36 m
- **Power**: 288 Wh LiFePO4 Anker SOLIX C300, **10+ hr** runtime (stock; *no high-power compute*). The official [BOM](https://xlerobot.readthedocs.io/en/latest/hardware/getting_started/material.html) lists the **C300 DC Power Bank (A1726, $179.99)** — **2.8 kg**, DC-only (no AC outlet, hard-capped 300 W, no surge) but **with a 12 V/10 A car outlet + 3 USB-C (2×140 W + 1×100 W)**, so it serves both robot rails on its own ([Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md) runs its Tri-Bus on it: arms on the car outlet, wheels/neck + Jetson on USB-C). For a Thor build this analysis opts for the **C300 Portable Power Station (A1722, ~$200, 4.1 kg)** — same rails **+ 2× AC 300 W / 600 W surge + AC outlet** — for transient headroom, not necessity. Comparison + the C1000 alternative: [Anker C300 DC vs C300 vs C1000](../syntheses/platforms/anker-portable-power-stations.md). Adding an [AGX Thor](jetson-thor.md) collapses runtime to **~1.4–2.5 hr** and requires a second voltage rail (12 V motors + 28 V/PD Thor) — see [XLeRobot + Thor power budget](../syntheses/projects/xlerobot-thor-power-budget.md).
- **3D-printed**: 90% of mechanical parts (tested on BambuLab A1 / PLA; PETG, PLA-CF, Tough PLA also supported)
- **Assembly time**: **2–4 hr from scratch; 1–2 hr with pre-assembled SO101 arms** (8 high-level steps)
- **Optional sensors**: RGB camera, stereo RGB (+$30), **RealSense D415 RGBD depth** (+$220). For **low-light / cluttered** operation the **D435i** (global shutter, wider FOV, IMU) is a better swap than the stock D415, though it needs a mount tweak (different housing: D435i 90×25×25 mm vs D415 99×20×23 mm — the press-fit shell won't fit as-printed) — see [XLeRobot camera options for low-light + clutter](../syntheses/projects/xlerobot-camera-options-low-light.md).
- **Compute model**: **PC-does-inference, Pi-relays-WiFi** — the optional Raspberry Pi 4/5 (+$79) is positioned as a *data-relay*, not the inference host. Heavy policy inference runs on a user PC, optionally via LeRobot's async policy server on port 8080. Onboard alternatives: a CUDA path ([Jetson Orin Nano/NX](../syntheses/platforms/jetson-onboard-compute-xlerobot.md), which runs the LeRobot policies as-is) or an NPU path ([Raspberry Pi AI HAT+ 2 / Hailo-10H](../sources/raspberry-pi-ai-hat-plus-2.md) on a [Pi 5](raspberry-pi-5.md) — good for an onboard LLM/VLM agent layer + vision, but **does not** run ACT/Diffusion/SmolVLA policies; see [Hailo](hailo.md)).
- **Form factor**: IKEA RÅSKOG cart serves as the torso/base in the developer kit

## Pricing

- **Basic configuration**: $660 USD (~€680, ¥3999 CN, ₹87,000 IN)
- **Developer assembly kit**: $579 worldwide (excludes battery + IKEA cart)
- **Taobao**: ¥3,699

## Software

XLeRobot is **explicitly a multi-stack reference platform** — the docs walk five distinct on-robot software workflows rather than committing to one.

- **Framework**: **[LeRobot](lerobot.md)** (Hugging Face); install via `pip install -e .` on top of the LeRobot install
- **Simulation**: **[ManiSkill](maniskill.md) 3.0** — scenes include `ReplicaCAD_SceneManipulation-v1`, AI2-THOR, RoboCasa Kitchen, `OpenCabinetDrawer-v1`
- **Teleop**: keyboard, **Xbox**, **Switch Joycon**, **VR (Quest 3 → ManiSkill via WebSocket-over-HTTPS)**. Real-robot VR is **"coming soon"** as of v0.3.0 — only sim VR works today.
- **VLA / policy options (three of them)**:
  - **ACT** (Action Chunking Transformer) — LeRobot's default VLA; example uses 50 single-arm episodes
  - **π0.5** via an **OpenPI fork** with bimanual SO-101 training support; ships with the `bimanual-toy-box-cleanup` HF dataset
  - **SmolVLA** (`lerobot/smolvla_base`) — 12-D bimanual action space padded to 32-D during training; ~20 demos for drawer / pick-place / **zipper** tasks; **80k steps = ~1 hr 45 min on an A100**
- **RL**: official XLeRobot RL "coming soon"; meanwhile the docs point users to `lerobot-sim2real` (Stone Tao, ManiSkill-PPO) and HuggingFace's HIL-SERL tutorial
- **LLM agent**: a **LangChain-style stack** with **Google Gemini 3 Flash** default; tool library is **RoboCrew** (factory functions like `create_move_forward()`, `look_around()`, a VLA-calling manipulation tool); voice wakeword "hey robot"; demos include approach-a-human, grab-notebook-and-deliver

## Capabilities & limitations (per the docs)

**Claimed capabilities**: household chores, indoor tasks, plant care, delivery, manipulation roughly comparable to $30k+ commercial bimanual robots.

**Acknowledged limitations**:
- Fixed height — no lifting platform (cf. [Stretch](stretch.md)'s lift mechanism)
- Workspace smaller than Aloha-class
- No in-hand dexterity
- Payload <1 kg
- No dynamic motion

**Safety positioning**: low-torque motors deliberately chosen to limit harm potential — a tradeoff that makes the platform plausible for household deployment.

## Contributors

- **Creator**: [Vector Wang](vector-wang.md) (Gaotian Wang)
- **RL sim2real**: Zhuoyi Lu
- **Documentation**: Nicole Yue
- **Simulation assets**: Yuesong Wang

## Why it matters in this wiki

XLeRobot is the **cheapest dual-arm mobile manipulator** documented in this wiki. It compresses a research-grade configuration into a ~$660 BOM by aggressively reusing existing open-hardware lineage:

- Arm = [SO-ARM101](so-arm101.md) (The Robot Studio, open-source)
- Base = [LeKiwi](lekiwi.md)-class (SIGRobotics-UIUC)
- Software = [LeRobot](lerobot.md) (Hugging Face)
- Sim = [ManiSkill](maniskill.md) (Hillbot lineage)

This composition pattern — **buy-no-new-IP, glue together with 3D-printed brackets and Apache-2.0 software** — is becoming the dominant cost-reduction strategy in the affordable-manipulation space, and XLeRobot is one of its clearest expressions.

> [!note] The commercial answer to the same problem
> **[Sourccey](sourccey.md)** ([Vulcan Robotics](vulcan-robotics.md), Aug 2026) converges on nearly the same component list — FeeTech servos, Raspberry Pi 5, ~90% 3D-printed, dual 5-DOF arms, LeRobot — from the product side rather than the community side. It adds a **vertical lift**, **standard LiDAR**, an **onboard touchscreen**, **Oculus Quest IK teleop**, and **[X-VLA](x-vla.md) laundry-folding policies preinstalled**; it gives up **half the battery energy** (~120 Wh vs 288 Wh), **all of the reproducibility** (no BOM, wiring, URDF, or STLs published), a **permissive hardware license** (CERN-OHL-S-2.0 vs Apache 2.0), and any published price. Full comparison: **[Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md)**. Useful counterpoint to [Stretch](stretch.md) (~$20k, integrated single-arm with lift), the [Reachy 2](reachy.md) (~$50k, dual-arm with integrated AI compute), and [Fauna Sprout](fauna-robotics.md) (humanoid developer platform).

## Related

- [Vector Wang](vector-wang.md) — creator
- [LeKiwi](lekiwi.md) — base lineage
- [SO-ARM101](so-arm101.md) — arm
- [LeRobot](lerobot.md) — software
- [ManiSkill](maniskill.md) — sim
- [Stretch](stretch.md) — adjacent (single-arm, integrated, ~30× more expensive)
- [Mobile ALOHA](aloha.md) — the research-tier bimanual-mobile counterpart (~25× the cost)
- [Robot platforms — comparison](../syntheses/platforms/robot-platforms-comparison.md) — where XLeRobot sits by tier/type (educational bimanual mobile manipulator)
- [Reachy 2](reachy.md) — adjacent (dual-arm, professional)
- [V-JEPA 2](v-jepa-2.md) — **the docs' Related Works section cites V-JEPA 2 under "Task Planning"** — a direct intersection with the wiki's JEPA / world-model thread.

## In the wild — hackathon traction (Oct 2025)

XLeRobot was the **dominant dual-arm platform** at the [October 2025 Seeed × NVIDIA × Hugging Face Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md), placing in winning teams on both sites:

- **U.S. site champion — [SIGRobotics-UIUC](sigrobotics-uiuc.md) matcha-making bot** — bimanual XLeRobot + [GR00T N1.5](nvidia-groot.md) fine-tune via NVIDIA Brev + Jetson Thor deployment.
- **China site 2nd runner-up — "Mate XLeRobot"** (Ryan, Isaac, Qi, KAHO, Bubbles) — **hardware-modded XLeRobot variant with a vertical lift-rail**, which directly addresses the fixed-height workspace limitation in the stock spec. First wiki-documented end-user hardware modification of the platform.

These are the strongest external signals to date that the $660 BOM holds up when stacked against more expensive arms (FashionStar StarAI) in a competitive setting.

## Downstream projects

- **[Cutting the Cord](../sources/cutting-the-cord-untethered-xlerobot.md)** ([Nikolaus Correll](nikolaus-correll.md) lab, CU Boulder, 2026) — the first measured **untethered, onboard-GPU XLeRobot** (<$1,300 / $1,202 BOM). Adds embedded [Jetson Orin Nano](jetson-orin-nano.md) compute, a **Tri-Bus power topology** that isolates the Jetson from motor voltage transients (fixing a 12.2 V→0.3 V brownout on the stock shared bus), a stiffer "High-Shell" 4-wall print topology (1 kg/arm payload, 98.7 % grasp success), and onboard SLAM/IK/VR-teleop. Provides the wiki's first on-edge VLA latency numbers and grounds the [Jetson onboard-compute comparison](../syntheses/platforms/jetson-onboard-compute-xlerobot.md). It runs its Tri-Bus on the **C300 DC ($159.99)** — confirming that the DC bank has a **12 V/10 A car outlet + 3 USB-C (2×140 W + 1×100 W)** and serves both robot rails on its own (arms on the car outlet; wheels/neck + Jetson on USB-C). See [Anker C300 DC vs C300 vs C1000](../syntheses/platforms/anker-portable-power-stations.md).
- **[Grievous](grievous.md)** ([source](../sources/grievous-github.md)) — Alex Koven's in-progress "cheap, human-like, fully-autonomous testbed" explicitly building on Mobile ALOHA + XLeRobot + [LeRobot](lerobot.md). First wiki-tracked attempt to combine XLeRobot's cost-reduction strategy with [Mobile ALOHA](aloha.md)'s bimanual-mobile design.

## Mentioned in

- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Cutting the Cord (Shaw et al., 2026)](../sources/cutting-the-cord-untethered-xlerobot.md) — untethered onboard-Jetson evolution.
- [Jetson onboard compute for XLeRobot](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) — Orin Nano vs AGX Orin vs Thor.
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)
- [Grievous GitHub](../sources/grievous-github.md) — design ancestor.
- [Sourccey vs XLeRobot](../syntheses/platforms/sourccey-vs-xlerobot.md) — head-to-head with the commercial convergent design.

## Open questions / TBD

- Real-world task-success numbers vs. published household-manipulation benchmarks (RoboCasa365, BEHAVIOR-1K, OK-Robot dataset). Currently qualitative claims only.
- Reproducibility for a non-expert assembler: 4-hour estimate is generous; does the price hold including the inevitable 3D-print failures?
- The "comparable to $30k+ commercial bimanual robots" claim deserves scrutiny — payload and workspace numbers suggest it's narrower than that comparison implies.
