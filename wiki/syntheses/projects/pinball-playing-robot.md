---
title: Pinball-playing robot — project scoping
type: synthesis
created: 2026-07-15
updated: 2026-07-21
source_notes: raw/project_notes_on_robots_from_claude.txt
tags: [pinball, xlerobot, jetson-thor, dgx-spark, gr00t, so-arm101, solenoid, reflex-control, global-shutter-camera, physical-ai, project]
---

# Pinball-playing robot — project scoping

Scoping notes for a physical-AI project: a mobile robot that **navigates a showroom, approaches a pinball machine, starts a game, and learns to play** — built on the wiki's [XLeRobot](../../entities/xlerobot.md) base + [Jetson Thor](../../entities/jetson-thor.md) compute stack. Captured from the user's own design conversation (`raw/project_notes_on_robots_from_claude.txt`); this page is the durable, cross-linked version. It is **project scoping, not a validated build** — everything below is a design hypothesis to test.

## The core reframe: decompose by timescale

"Learn to play pinball" is **two problems at very different clock rates**, and only one is a VLA job:

- **Slow / semantic (~10 Hz) → keep on [GR00T](../../entities/nvidia-groot.md).** Showroom navigation, recognizing + approaching a machine, positioning at the cabinet, finding and pressing start, strategy ("cradle the ball," "go for that ramp"). [GR00T N1.7](../../entities/nvidia-groot.md) on Thor runs ~10 Hz — well-suited to all of this.
- **Reflex / control (100+ Hz) → a separate dedicated loop.** Actual flipper play is a reflex problem: a ball crosses the flipper zone in tens of milliseconds, so a 10 Hz (100 ms) policy loop **cannot see-decide-act inside the window**. This needs a high-FPS playfield camera + a lightweight ball tracker + a fast timing controller. GR00T owns strategy and posture; the fast loop owns the flip. **Trying to make one end-to-end VLA do both is the most likely way the project stalls.**

This split also resolves the camera tension: the **playfield/ball-tracking camera feeds the fast loop only** (high framerate, out of the VLM backbone), while just 1–2 cameras feed GR00T for nav/manipulation — keeping GR00T's rate healthy.

## Actuation: decouple positioning from the press

The [SO-ARM101](../../entities/so-arm101.md) arms are 5-DOF hobby-servo (STS3215); fine for *positioning* but too slow/soft for reflex flipper presses. Design principle: **the arm parks a fast end-effector on the flipper button and holds; the effector fires in milliseconds.**

- **Effector of choice: a short-stroke push-solenoid** per flipper button. Coil pull-in ~5–15 ms; MOSFET switching sub-ms → single-digit-to-low-teens ms actuation, ~an order of magnitude faster than jabbing an STS3215.
  - Drive with a logic-level MOSFET + flyback diode, gated from an MCU.
  - **Separate power rail** from Thor (inrush spikes off the compute supply) — convenient given the project already runs a ~24 V battery domain (see [XLeRobot Thor power budget](xlerobot-thor-power-budget.md)).
  - **Peak-and-hold current** for cradling (hold a flipper up without cooking the coil) — the same dual-wind/PWM trick real machines use.
- **Electrical bypass is off-limits**: tapping the leaf switch (sub-ms) works but means splicing into **Stern's showroom demo units** — treat as the latency benchmark only, not a legal option. Assume **non-invasive physical presses**.
- **Servo finger** (~20–40 ms) is the middle option — OK for the start button, marginal/wears for reflex flips. Use servo/arm for start+plunger, solenoids for flippers.
- **Mechanical**: give the effector a **compliant cupped tip** that seats over the button housing so the mechanical seat provides precision, not the arm's holding accuracy. Watch **reach geometry** — flipper buttons are ~55 cm apart (wider on widebody) vs ~40 cm arm reach; mock up against a real cabinet before committing.

## Architecture fork: cabinet-hugging rig

A recurring idea in the notes: a **rig that clamps onto the cabinet** (referencing off the lockdown bar + side rails) carrying the solenoid pressers and the playfield camera. This quietly solves three hard problems at once — **registration** (geometry comes from the machine, not the soft arm), **reach** (pressers sit where they belong regardless of base parking), and **camera vantage** (fixed, repeatable playfield view). Non-marring contact is mandatory (showroom machines); design for standard vs. widebody Stern spacing. **Open fork:** is the rig self-contained (own camera/solenoids/Thor onboard, XLeRobot just transports+places it) or are the SO-101 arms themselves the pressers on a lightweight camera-mast rig? Self-contained is cleaner for solving the *playing* problem first (a human places it during dev), and it puts Thor+battery next to the camera/solenoids for minimum latency.

## Vision + reflex budget

- **Camera**: global-shutter, **low-res / high-FPS**, not megapixels. Target sensor **AR0234** (1920×1200 GS, ~120 FPS); **GMSL2 into a Holoscan Sensor Bridge** is the cleanest Thor-native low-latency path (D3 Embedded ships a GMSL2 Holoscan bundle for the AGX Thor dev kit, JetPack 7). Avoid 25MP GS cameras — bottlenecked to ~35–50 FPS. **Gating factor is the JetPack-7/Thor driver, not the sensor** — confirm the exact SKU has a Thor driver before buying.
- **Frame-rate math**: at 120 FPS (~8.3 ms/frame) a 3 m/s ball moves ~25 mm/frame (~one ball diameter — trackable with a predictor); 5+ m/s → ~40 mm/frame (coarse; ROI-crop the lower playfield to push FPS up).
- **Chrome-ball-through-glass is the real enemy**: glass reflects showroom lights; the 27 mm mirror ball reflects the playfield's own flashing GI, so color/brightness are unstable. Mitigations in impact order: **circular polarizer + steep camera angle** to kill specular glare; **lens hood**; and **track by combining high-FPS frame-differencing + a YOLO-nano-class ball detector** fine-tuned on own footage — never a single cue.

> [!note] Tracker choice revised — see [Fast-ball tracking for robots](fast-ball-tracking-for-robots.md)
> The "frame-differencing + YOLO-nano" recommendation above has the **right instinct** (fuse motion + appearance) but the weaker mechanism. A **[TrackNetV2-class heatmap tracker + V4 motion attention](../../entities/tracknet.md)** is the better-evidenced version: heatmap output beats a YOLO baseline by **~30 F1** at this object scale, and V4's learned motion fusion replaces the hand-tuned two-cue arbitration. The chrome-ball-through-glass problem *strengthens* the case, since motion is stable when appearance isn't. **Avoid TrackNetV3** — its gain comes from a non-causal trajectory-inpainting module a reflex loop cannot run; that job belongs to the Kalman predictor below. Full analysis, including the latency and labeling-cost implications, on the linked page.

- **Predict, don't react**: feed the tracker into a ballistic/Kalman predictor and **pre-fire the solenoid** by the total pipeline latency (detector + inference + decision + solenoid mechanical delay, ~15–30 ms if the tracker stays lean). Keep the trigger path short — fire over direct GPIO/UART to the solenoid MCU, not through USB/ROS topics.

## Learning path

- **Reward is free**: OCR the machine's score display (DMD/LCD) and use **score-delta** as the learning signal.
- **Order**: (1) **imitation first** — teleoperate through games, collect demos (~400 demonstrations cited as a working dataset scale), fine-tune GR00T on the slow behaviors; (2) a **separately trained/tuned reactive flipper policy** bootstrapped in the fast loop; (3) **real-world RL with score-as-reward as phase three**, not phase one (sample-efficiency heavy).
- **Reference recipe**: NVIDIA's [GR00T end-to-end workflow](../../sources/nvidia-gr00t-e2e-workflow-docs.md) is the first-party version of this loop (teleop → collect → fine-tune → eval → deploy) on the same G1+Thor+Isaac-ROS+LeRobot stack — a concrete template for the slow-behavior half, even though its task is tabletop pick-and-place rather than pinball.
- **Embodiment caveat**: XLeRobot's bimanual+base config is **not a GR00T pretrained embodiment** → you fine-tune a NEW_EMBODIMENT regardless.
- **Safety** (from the notes' Q&A): rigorous sim validation + physical **e-stop** + software deployment safeguards; classical control / kill-switches as the reflex-layer safety net — consistent with the "whole-body controller = System 0 policy" framing.

## Navigation

Not a GR00T task — a **nav-stack** task. Run [Isaac ROS](../../entities/isaac-ros.md) (Visual SLAM + nvblox) or ROS 2 Nav2 on Thor; **add a depth camera or small lidar** to the base, because a glossy showroom full of reflective pinball glass is hostile to vision-only SLAM. Thor's MIG partitioning lets nav and policy share the GPU concurrently.

## Compute: the Spark + Thor split

The project uses the wiki's canonical [train-on-Spark, deploy-on-Thor](../platforms/jetson-thor-vs-dgx-spark.md) pairing — both 128 GB unified Blackwell, so a model that fits on the [DGX Spark](../../entities/dgx-spark.md) desk fits on [Thor](../../entities/jetson-thor.md); the same JetPack-7 container runs on both (runtime-flag difference only). Keep fine-tuning/eval on Spark; Thor earns its place once work moves onto the robot (real-time multi-model against live sensors, robotics I/O, MIG). Note the reported **Thor dev-kit limited release** — secure hardware if the dev-kit form factor is needed. Power the Thor from the battery via its **Micro-fit 9–28 V / 8 A** input (not USB-C PD) — 24 V nominal; budget ~100 W sustained under GR00T load → ~100 Wh ≈ 1 hr.

## Related

- [Fast-ball tracking for robots](fast-ball-tracking-for-robots.md) — **the perception deep-dive for this project's fast loop**: which parts of the TrackNet literature are causal enough to use, and why the rig fork buys a static camera. See its **§8 Field evidence** for what a real implementation confirmed and refuted.
- [pinball_tracker (repo)](../../sources/pinball-tracker-repo.md) — **the fast loop, actually built**: heatmap U-Net + homography normalization, F1 0.878 held-out on an unseen machine. Also the source of two corrections to the analysis page: classical-CV bootstrap labeling tracks only ~8% of frames (hand-label instead), and 600 training frames went much further than the 10–20k estimate.
- [XLeRobot Thor power budget](xlerobot-thor-power-budget.md), [GR00T on Spark → ZMQ → XLeRobot](gr00t-spark-zmq-xlerobot.md), [XLeRobot camera options (low light)](xlerobot-camera-options-low-light.md) — sibling project pages on the same platform.
- [Jetson Thor vs DGX Spark](../platforms/jetson-thor-vs-dgx-spark.md) — the compute-split rationale.
- [XLeRobot](../../entities/xlerobot.md), [SO-ARM101](../../entities/so-arm101.md), [GR00T](../../entities/nvidia-groot.md), [Isaac ROS](../../entities/isaac-ros.md), [Jetson Thor](../../entities/jetson-thor.md), [DGX Spark](../../entities/dgx-spark.md).

## Open decisions

1. **Rig fork** — self-contained cabinet rig vs. arms-as-pressers (determines where Thor + battery live).
2. **Flipper actuation** — solenoid effectors (recommended) confirmed before Thor arrives, since it drives the whole fast-loop design.
3. **Playfield camera + where the tracker runs** — sets the rest of the reflex budget and whether ~10 ms solenoid delay is comfortably inside the window.
