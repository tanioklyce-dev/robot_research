---
title: XLeRobot
type: entity
subtype: robot
created: 2026-05-10
updated: 2026-05-11
sources: 2
tags: [xlerobot, mobile-manipulator, dual-arm, lerobot, lekiwi, so-arm101, low-cost, household-robot, embodied-ai]
---

**XLeRobot** — $660 household **dual-arm mobile manipulator** built by [Gaotian "Vector" Wang](vector-wang.md). Composes two [SO-ARM101](so-arm101.md) arms (~40 cm reach each) onto a [LeKiwi](lekiwi.md)-class wheeled base, with optional cameras and Raspberry Pi compute. 90% 3D-printed. Apache 2.0. Version 0.3.0 released August 30, 2025. Project tagline: *"Bring Embodied AI to Every Family Around the World" at a price cheaper than an iPhone*.

Repository: [github.com/Vector-Wangel/XLeRobot](https://github.com/Vector-Wangel/XLeRobot). Docs: [xlerobot.readthedocs.io](https://xlerobot.readthedocs.io).

## Specs

- **Arms**: 2× [SO-ARM101](so-arm101.md), each ~40 cm reach, 600–1000 g payload
- **Base**: wheeled mobile platform inspired by [LeKiwi](lekiwi.md) / Bambot (2-wheel, mecanum, and 3× omni-wheel variants documented)
- **Actuators**: **17× Feetech STS3215** servos at 12 V (same family as SO-100/SO-101)
- **Mass**: ~12 kg (intentionally adult-liftable)
- **Vertical workspace**: 0.5 m – 1.25 m (fixed-height torso, no lift)
- **Reach from cart edge**: ~0.36 m
- **Power**: Anker SOLIX C300 power station — 288 Wh, 300 W max output, 280 W max charge (~1 hr to full), **10+ hr** runtime
- **3D-printed**: 90% of mechanical parts (tested on BambuLab A1 / PLA; PETG, PLA-CF, Tough PLA also supported)
- **Assembly time**: **2–4 hr from scratch; 1–2 hr with pre-assembled SO101 arms** (8 high-level steps)
- **Optional sensors**: RGB camera, stereo RGB (+$30), **RealSense D415 RGBD depth** (+$220)
- **Compute model**: **PC-does-inference, Pi-relays-WiFi** — the optional Raspberry Pi 4/5 (+$79) is positioned as a *data-relay*, not the inference host. Heavy policy inference runs on a user PC, optionally via LeRobot's async policy server on port 8080.
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

This composition pattern — **buy-no-new-IP, glue together with 3D-printed brackets and Apache-2.0 software** — is becoming the dominant cost-reduction strategy in the affordable-manipulation space, and XLeRobot is one of its clearest expressions. Useful counterpoint to [Stretch](stretch.md) (~$20k, integrated single-arm with lift), the [Reachy 2](reachy.md) (~$50k, dual-arm with integrated AI compute), and [Fauna Sprout](fauna-robotics.md) (humanoid developer platform).

## Related

- [Vector Wang](vector-wang.md) — creator
- [LeKiwi](lekiwi.md) — base lineage
- [SO-ARM101](so-arm101.md) — arm
- [LeRobot](lerobot.md) — software
- [ManiSkill](maniskill.md) — sim
- [Stretch](stretch.md) — adjacent (single-arm, integrated, ~30× more expensive)
- [Reachy 2](reachy.md) — adjacent (dual-arm, professional)
- [V-JEPA 2](v-jepa-2.md) — **the docs' Related Works section cites V-JEPA 2 under "Task Planning"** — a direct intersection with the wiki's JEPA / world-model thread.

## In the wild — hackathon traction (Oct 2025)

XLeRobot was the **dominant dual-arm platform** at the [October 2025 Seeed × NVIDIA × Hugging Face Embodied AI Hackathon](../sources/seeed-embodied-ai-hackathon-2025-recap.md), placing in winning teams on both sites:

- **U.S. site champion — [SIGRobotics-UIUC](sigrobotics-uiuc.md) matcha-making bot** — bimanual XLeRobot + [GR00T N1.5](nvidia-groot.md) fine-tune via NVIDIA Brev + Jetson Thor deployment.
- **China site 2nd runner-up — "Mate XLeRobot"** (Ryan, Isaac, Qi, KAHO, Bubbles) — **hardware-modded XLeRobot variant with a vertical lift-rail**, which directly addresses the fixed-height workspace limitation in the stock spec. First wiki-documented end-user hardware modification of the platform.

These are the strongest external signals to date that the $660 BOM holds up when stacked against more expensive arms (FashionStar StarAI) in a competitive setting.

## Mentioned in

- [XLeRobot Documentation](../sources/xlerobot-docs.md)
- [Seeed × NVIDIA × HF Embodied AI Hackathon 2025 Recap](../sources/seeed-embodied-ai-hackathon-2025-recap.md)

## Open questions / TBD

- Real-world task-success numbers vs. published household-manipulation benchmarks (RoboCasa365, BEHAVIOR-1K, OK-Robot dataset). Currently qualitative claims only.
- Reproducibility for a non-expert assembler: 4-hour estimate is generous; does the price hold including the inevitable 3D-print failures?
- The "comparable to $30k+ commercial bimanual robots" claim deserves scrutiny — payload and workspace numbers suggest it's narrower than that comparison implies.
