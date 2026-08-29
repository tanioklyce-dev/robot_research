---
title: "Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation (Fu, Zhao, Finn — Jan 2024)"
type: source
url: https://mobile-aloha.github.io
arxiv: https://arxiv.org/abs/2401.02117
local_path: raw/mobile-aloha.pdf
sha256: 698c3b093b388575ea32e214b074e21b2539f6dae04e1f3bc614c7e461f05286
author: Zipeng Fu*, Tony Z. Zhao*, Chelsea Finn
affiliations: Stanford University
published: 2024-01
ingested: 2026-05-25
tags: [mobile-aloha, aloha, act, bimanual, mobile-manipulation, imitation-learning, co-training, stanford, chelsea-finn, tony-zhao, zipeng-fu, viperx-300, behavior-cloning, primary-source]
---

## Summary

Stanford's **Mobile ALOHA** is a **$32k bimanual mobile-manipulation system** (hardware + software, including onboard power + compute) that extends the original ALOHA puppeteering setup with a wheeled base and a **whole-body teleoperation interface** in which the operator is physically tethered to the mobile base and backdrives the wheels while both hands run ALOHA's leader arms. The paper's two contributions: (1) the hardware — a deliberately low-cost, untethered, hour-scale teleop platform; and (2) a **co-training recipe** showing that mixing 825 static-ALOHA bimanual demos with as few as 20–50 in-domain Mobile ALOHA demos produces **up to +90% absolute success-rate boost** on long-horizon mobile-manipulation tasks like sautéing shrimp, opening a two-door cabinet to store a heavy pot, calling an elevator, rinsing a pan under a faucet, and wiping a spilled wine glass. The recipe holds across **three imitation-learning method families**: ACT, Diffusion Policy, and VINN (with chunking).

This is the **first time the wiki has ingested ALOHA or ACT**, both of which prior pages had flagged as gaps (see [Chelsea Finn entity](../entities/chelsea-finn.md), [robot platforms comparison](../syntheses/platforms/robot-platforms-comparison.md)). The companion **[project page source](mobile-aloha-project-page.md)** ingest adds the tutorial URL, dataset Google Drive link, author homepages, and surfaces the **[ACT++](../entities/act-plus-plus.md)** codebase (`MarkFzp/act-plus-plus`) as the mobile-extended successor to the original ACT.

## Key claims

### Hardware ($32k total, including onboard compute + power)

| Spec | Value |
|---|---|
| Mobile base | **AgileX Tracer AGV** (warehouse differential-drive; $7k, 100 kg payload, 1.6 m/s top speed) |
| Arms | **4× Trossen [ViperX 300](../entities/viperx-300.md)** (2 leaders + 2 followers); 6 DOF each |
| Total DOF | 14 (arms) + 2 (base linear/angular vel) = **16-dim action vector** |
| Cameras | 3× **Logitech C922x** RGB webcams (2 wrist + 1 top), 480×640 @ 50 Hz |
| Compute | Consumer laptop — **Intel i7-12800H + NVIDIA RTX 3070 Ti (8 GB VRAM)** |
| Battery | **1.26 kWh** (14 kg, doubles as ballast); ~12 hr runtime |
| Reach | 65–200 cm vertical; 100 cm horizontal from base |
| Payload | 750 g per arm; 1.5 kg combined; can exert 100 N pull at 1.5 m |
| Weight | 75 kg total |
| Footprint | 80×84 cm (no leaders) / 90×135 cm (with leaders) |
| Repeatability / accuracy | 1 mm / 5–8 mm |
| Max base speed | 1.42 m/s (human walking) |
| Rolling resistance (operator backdrive) | 13 N on vinyl floor |

The **whole-body teleoperation gimmick**: operator wears a waist tether to the mobile base. Both hands are occupied with ALOHA leader arms, so the operator simply walks and the base follows by backdriving. The tether also provides coarse haptic feedback when the base collides. During autonomous execution, the tether and leader arms detach (4 screws), reducing footprint.

Hardware + software fully open-sourced with a 3D-printing + assembly + install tutorial at https://mobile-aloha.github.io.

### The co-training recipe

- Aggregate the **static ALOHA dataset** (`D_static`): 825 episodes from prior ALOHA / RT-X releases, tasks disjoint from Mobile ALOHA, two arms facing each other on a black tabletop.
- For each Mobile ALOHA task `m`: 20–50 in-domain demos `D_mobile^m`.
- Training objective:
  ```
  L_total = E_{(o,a_arms,a_base) ~ D_mobile} [ L(a_arms, a_base, π(o)) ]
          + E_{(o,a_arms) ~ D_static}        [ L(a_arms, [0,0],  π(o)) ]
  ```
- Zero-pad static-dataset base actions; sample with **equal probability** from each dataset; normalize actions to Mobile-ALOHA statistics; drop the static front-cam so both datasets have 3 cameras; batch size 16.

The recipe is method-agnostic — applied to **ACT**, **Diffusion Policy**, and **VINN+chunking** with consistent gains on the first two.

### Results — Table 1 (ACT, co-train vs no-co-train, success rate %)

| Task | Demos | Co-train whole-task | No-co-train whole-task | Δ |
|---|---|---|---|---|
| Wipe Wine | 50 | **95** | 50 | +45 |
| Cook Shrimp | 20 | 40 | 20 | +20 |
| Rinse Pan | 50 | **80** | 0 | **+80** |
| Use Cabinet | 50 | 85 | 85 | 0 |
| Call Elevator | 50 | **95** | 0 | **+95** |
| Push Chairs | 50 | **80** | 0 | **+80** (extrapolation: 4th + 5th chairs are OOD) |
| High Five | 20 | 85 | 85 | 0 |

**Average +34% absolute improvement** from co-training. The largest gains are on **precision-bottleneck sub-tasks**: pressing the elevator button (5 → 100), turning on the faucet (0 → 80), and lifting+wiping the glass (58 → 95). Co-training appears to act as a regularizer that prevents overfitting in the low-data (20–50 demos) regime with expressive transformer policies, and improves OOD extrapolation (4th+5th chair: +15% / +89%).

### Results — Table 2 (method compatibility on 2 tasks)

| Method | Wipe Wine (co/no) | Push Chairs (co/no) |
|---|---|---|
| **ACT** | 95 / 50 | 100 / 100 |
| **Diffusion Policy** | 65 / 35 | 100 / 80 |
| **VINN + Chunking** | 15 / 20 | 60 / 40 |

- ACT is the strongest overall.
- Diffusion Policy benefits from co-training (+30 / +20) but underperforms on Wipe Wine — authors hypothesize 50 demos is insufficient for DP, which typically wants ≥250.
- VINN+chunking is weakest; **only its visual encoder benefits from co-training** since the retrieval action-prediction mechanism can't leverage out-of-domain static data.

### Ablations

- **Data efficiency** (Wipe Wine): co-trained policy at 35 demos beats no-co-train policy at 50 demos by 20 pts (70% vs 50%).
- **Co-train data mixture robustness**: 30/50/70% static-sampling rates yield 95/95/90% on Wipe Wine — **not sensitive to mixture ratio**, reducing manual tuning.
- **Co-train > pre-train**: pre-training ACT on static then fine-tuning gives 50% (= no co-train baseline of 40%); co-training gives 95%. Authors hypothesize fine-tuning forgets the static distribution.

### User study

8 CS grad students (5F/3M, 21–26), 4 with prior teleop experience, none had used Mobile ALOHA before. 3-minute free-play, then expert demo + 5 trials of Wipe Wine and Use Cabinet:

- Wipe Wine completion time: **46 s → 28 s** (down 39%)
- Use Cabinet: **75 s → 36 s** (down 52%)

Average participant approaches expert speed within 5 trials.

### Action-chunk delay handling (mobile-specific trick)

Mobile base has a velocity-control delay >10 cm error on 1m-radius 180° turns. Position-controlled arms have negligible delay. To compensate, the robot executes the **first k−d arm actions** and the **last k−d base actions** of an action chunk of length k — i.e., the base is "delay-shifted" within the chunk to compensate for its slower response. This is a non-obvious imitation-learning trick that depends on action chunking being a first-class primitive.

### Tasks (the seven evaluated)

1. **Wipe Wine** — pick up towel from faucet, navigate to kitchen island, lift wine glass with one arm, wipe with other arm. 26 s. Bimanual + mobile.
2. **Cook Shrimp** — pour oil + raw shrimp into pan, flip with spatula while tilting pan, pour into bowl, place pan. 75 s. Longest horizon; only 20 demos.
3. **Rinse Pan** — grasp pan, open/close faucet, swirl water, place on drying rack. 22 s. Faucet knob is shiny 4×0.7 cm — visual servoing challenge.
4. **Use Cabinet** — open two-door wall cabinet by backing up while holding both handles, place 1.4 kg pot inside, close. 30 s. Pot exceeds single-arm payload (750 g).
5. **Call Elevator** — 15 m navigation across 10 m lobby, around column, press 2×2 cm button, enter elevator with 30 cm clearance. 45 s.
6. **Push Chairs** — push 5 chairs at a long desk; demos cover only first 3, tests on all 5 (extrapolation eval).
7. **High Five** — circumnavigate kitchen island; stop and high-five when approached, resume when path clears.

**Open-loop replay = 0% success on all tasks** — proves closed-loop visuomotor reaction is necessary; the system isn't just memorizing trajectories.

### Reproducibility scope

- $32k budget is **comparable to a single Franka Emika Panda arm**, and ~6× cheaper than a PR2 / TIAGo ($200k+).
- Tracer base is $7k vs Clearpath-class AGVs at >5× that price.
- 50% data sampling default; equal probability from each dataset; batch size 16. The simplicity of the recipe is part of the contribution.

## Entities mentioned

- [Mobile ALOHA + ALOHA platform line](../entities/aloha.md) — new entity created by this ingest.
- [ACT (Action Chunking Transformer)](../entities/act.md) — IL method introduced with original ALOHA; new entity.
- [Diffusion Policy](../entities/diffusion-policy.md) — used as one of three IL methods evaluated.
- [Chelsea Finn](../entities/chelsea-finn.md) — senior author; closes the prior "ALOHA / ACT not yet ingested" gap on her entity.
- [Tony Z. Zhao](../entities/tony-zhao.md) — co-lead; original ALOHA + ACT first author; new entity.
- [Zipeng Fu](../entities/zipeng-fu.md) — co-lead; new entity.
- [ViperX 300](../entities/viperx-300.md) — Trossen 6-DOF arm; ALOHA's standard leader/follower hardware; new entity.
- [Hello Robot Stretch](../entities/stretch.md) — referenced as prior single-arm mobile manipulator with limited teleop (gamepad/keyboard, not bimanual whole-body).
- [Franka Panda](../entities/franka-panda.md) — referenced as cost reference (Mobile ALOHA budget ≈ 1× Panda).
- [DROID](../entities/droid.md) — Chelsea Finn affiliation; not used here but tangentially related lineage.

## Concepts touched

- [Imitation learning](../concepts/learning/imitation-learning.md) — co-training with static-task data improves mobile-manipulation success and data efficiency.
- Action chunking — first-class to ACT and Diffusion Policy; here extended with a base-vs-arm delay-shift trick.
- Whole-body teleoperation — body-tether-as-haptic + backdrive-by-walking is the design contribution.
- Bimanual mobile manipulation — task class established here as the BC frontier.

## Open questions

- **2024 paper, ingested 2026** — has anyone reproduced this on top of Stretch 4 (omni base) or other platforms? Wiki has no follow-up ingests; worth checking ALOHA / Mobile ALOHA citation graph.
- **Single-task IL only** — the paper explicitly leaves multi-task / language-conditioned Mobile ALOHA as future work. Where does multi-task Mobile ALOHA sit relative to π0 / OpenVLA / GR00T-class generalists in 2026?
- **Heterogeneous static-data co-training** — recipe used disjoint-task static ALOHA. How robust is it when the static data is *partially overlapping* in task or scene? The paper doesn't ablate this.
- **OOD extrapolation pattern** — Push Chairs co-train improves 4th/5th chair by 15/89%; is co-training generally OOD-helpful, or task-specific? More OOD evals would clarify.
- **Battery + compute envelope** — 1.26 kWh + RTX 3070 Ti (8 GB) is the 2024 ceiling. With 2026 hardware (Jetson Thor, Orin NX), the same physical platform could host much larger policies — open question whether anyone has refreshed Mobile ALOHA's electronics stack.
- **Trossen ViperX 300 availability + lineage** — wiki has no other Trossen-arm coverage; the SO-ARM101 / xArm-7 / Franka clusters tracked here don't include ViperX. Worth checking whether Trossen is the de-facto bimanual-teleop SKU for academic labs.

## Why it matters for the wiki

1. **Closes a major coverage gap.** Both [chelsea-finn.md](../entities/chelsea-finn.md) and the [robot-platforms-comparison synthesis](../syntheses/platforms/robot-platforms-comparison.md) flagged "ALOHA / ACT — not yet ingested" before this ingest. Mobile ALOHA is the right entry point because it transitively pulls in original ALOHA + ACT + the bimanual-teleop hardware lineage.
2. **Establishes the co-training-with-static-data pattern as an IL primitive.** This is the same pattern the wiki tracks under different names: [DROID + scene diversity](../entities/droid.md), [RUM + data diversity over quantity](../entities/robot-utility-models.md), [EgoScale + human-video pretraining](../sources/egoscale-paper.md). Mobile ALOHA is the **smallest-scale demonstration** — 825 static demos + 20–50 in-domain → +90% on hard tasks — which makes it the cleanest evidence that the pattern generalizes downward, not just to web-scale.
3. **Bimanual mobile-manipulation hardware reference** — until now the wiki's mobile-manipulation coverage was [Stretch](../entities/stretch.md) (single arm + lift), [TurtleBot](../entities/turtlebot.md) (mobile, no arm), and [Reachy](../entities/reachy.md) (bimanual stationary). Mobile ALOHA defines the academic-budget bimanual-mobile reference.
4. **Action chunking + base-delay-shift** is the kind of mobile-IL trick that's easy to miss in a paper-skim but matters operationally. Filed on the [imitation learning concept page](../concepts/learning/imitation-learning.md).
