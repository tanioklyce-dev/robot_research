---
title: "Microduck — Pollen Robotics launch (product page, launch blog, press kit)"
type: source
url: https://pollen-robotics.com/microduck/
author: Pollen Robotics (Matthieu Lapeyre, Thomas Wolf, Antoine Pirrone, Augustin Crampette, Coralie Deplane, Anne Charlotte Passanisi)
published: 2026-08-27
ingested: 2026-08-27
venue: pollen-robotics.com
format: product page + launch blog post + press kit + two GitHub repositories
tags: [pollen-robotics, hugging-face, microduck, biped, reinforcement-learning, sim-to-real, mjlab, mujoco, ppo, onnx, dynamixel, rk3566, consumer-robotics, open-source, education]
---

# Microduck — Pollen Robotics launch

> [!note] Provenance — a bundle of primaries, not one page
> The requested URL is the marketing landing page. Per the [primary-source rule](../../CLAUDE.md), the decision-grade numbers here come from **Pollen's own press kit** (`/microduck/press-kit/`) and **launch blog post** (`/microduck/blog/introducing-microduck/`), plus the two **GitHub repositories** the site links. Each claim below names which of these it came from. The landing page alone is *misleading on two counts* — see the two contradiction callouts.

## Summary

**Microduck** is a 25 cm, sub-800 g bipedal robot from [Pollen Robotics](../entities/pollen-robotics.md) — [Hugging Face](../entities/hugging-face.md)'s Bordeaux robotics team — announced with pre-orders on **2026-08-27** at an introductory **$399**, shipping "before Christmas 2026" in North America, Europe and the UK. It is Pollen's **second consumer robot**, after [Reachy Mini](../entities/reachy-mini.md).

The product thesis is stated cleanly in the launch post: *"Reachy Mini is a platform for AI that interacts, while Microduck is a platform for AI that acts."* Microduck ships seven RL-trained locomotion/manipulation policies and — this is the actual point — publishes the **entire training recipe that produced them**: [mjlab](../entities/mjlab.md) (MuJoCo Warp) + PPO, a voltage-level actuator model, backlash simulation, domain randomization, ONNX export, and a 50 Hz onboard runtime on a **Rockchip RK3566**.

Its wiki value is not the toy. It is that the wiki now has, for the first time, a **complete, published, reproducible sim-to-real recipe attached to a shipping $399 robot** — every prior [sim-to-real](../concepts/learning/sim-to-real-transfer.md) source covered a technique, a benchmark, or a lab result. This one names the parts, the failure modes, and the price.

## Key claims

### The robot (press kit spec sheet)

| | |
|---|---|
| **Dimensions** | 25 cm tall, 14 cm wide |
| **Weight** | under 800 g |
| **Motors** | **15**, across articulated legs, head and neck (the RL repo says **14 servos** + the beak — see contradiction below) |
| **Compute** | **Rockchip RK3566 with AI accelerator** |
| **Memory** | **1 GB RAM, 32 GB storage** |
| **Vision** | front camera, with a dedicated camera-use indicator "inspired by classic REC lights" |
| **Motion sensing** | **2 IMUs** — one in the body, one in the head |
| **Range sensing** | "compact LiDAR, an **8×8 time-of-flight matrix**" |
| **Physical interaction** | articulated **grasping beak** |
| **Audio** | microphones + speaker, per-robot generated voice |
| **NFC** | 2 antennas — one in the head, one in the beak |
| **Connectivity** | Wi-Fi + Bluetooth |
| **Battery** | removable **NP-F550 camera battery**, 2600 mAh, ~1 hour runtime |
| **Control** | **50 Hz onboard policy loop** |
| **In the box** | robot, battery, USB-C cable, game controller |

Pricing ladder: robot **$399**; Charger pack **$39** (dual charger, 2× batteries); Dev pack **$119** (3× spare motors, 5× motor cables, 2× batteries, dual charger, 10× NFC tags, Hugging Face credit, screwdriver, screw pack); Accessory pack **$39** (laser pointer, NFC polaroid, 2× rollers, ball, 10× NFC tags). Four colourways: Cream `#f7e6cb`, Graphite `#6c6a68`, Lavender `#bfa9cf`, Sky `#a9dbe8`.

> [!warning] Contradiction — "LiDAR" is a marketing word here
> The landing page and the fast-facts block say **"Camera — plus LiDAR and two IMUs."** The press kit's own spec table says what it actually is: *"Compact LiDAR, an **8×8 time-of-flight matrix**."* An 8×8 ToF matrix (VL53L5CX class) is a **64-zone depth sensor**, not a scanning LiDAR — no rotating beam, no point cloud, ~metre-class range. The launch blog is the honest one: it says *"a small depth sensor."* Anyone budgeting Microduck for mapping or navigation work should plan against **64 depth pixels**, not a LiDAR.

> [!warning] Contradiction — is the hardware open or not?
> The press kit carries an explicit press instruction: *"The open-source statement covers the **software stack**. The mechanical and electronic design files are **not**, so please do not describe the robot as open-source hardware."* But the `microduck_rl` README's license section says: *"**Hardware design files are licensed under Creative Commons BY-SA-NC**."* These are two Pollen primaries published the same week. The most likely reconciliation: design files *are* published under **CC BY-SA-NC**, whose **non-commercial** clause disqualifies them from "open-source hardware" as OSHWA defines it, and the press kit is guarding against press shorthand rather than denying publication. Unresolved as stated; treat "open-source hardware" as **not claimable** and "design files available, non-commercial" as **probable**.

> [!note] 15 motors or 14?
> Every marketing surface says **15 motors**. The RL repo's joint layout enumerates **14 servos** (0–4 left leg: hip_yaw / hip_roll / hip_pitch / knee / ankle; 5–8 neck+head: neck_pitch / head_pitch / head_yaw / head_roll; 9–13 right leg) and the backlash model adds play "in series with each of the **14** servo joints." The fifteenth is the **beak** — confirmed by the [runtime docs](microduck-runtime-repo.md): *"joints exclude the mouth throughout; actions map back into 15 motor slots with index 9 left at zero."* No locomotion task actuates it, so it never enters the shared observation contract. Not a contradiction so much as marketing counting the gripper and the RL stack not needing to.

### The seven shipped behaviours (landing page)

Walk (velocity-tracking gait) · Sit & stand · Kick ("a one-shot boot, then straight back to walking") · Grab ("dips the beak to the ground, scoops, and pops back upright") · Roller skating (with skates equipped) · Get back up (from flat on its back) · plus a forward roll ("roulade") in the RL task list.

### The training stack (`pollen-robotics/microduck_rl`)

- Built on **[mjlab](../entities/mjlab.md)** (MuJoCo Warp + `rsl_rl`) with **PPO**. Policies trained at **50 Hz**, exported to **ONNX**, deployed by the Rust runtime in `pollen-robotics/microduck`.
- **~1–2 h on a CUDA GPU at 4096 parallel envs for a usable gait.** No GPU? `--hf-jobs` submits the same run to **Hugging Face Jobs** — the first sighting in this wiki of HF Jobs used as the *default fallback compute path for a consumer robot's RL training*.
- **13 registered tasks**, most in Flat/Rough variants: `Velocity` (the main task: velocity commands + head-pose commands), `VelStand` (walking + fall recovery in one policy), `StandUp`, `SitStand`, `GroundPick`, `BallKick` (70 mm / 15 g ball, *"actor is ball-blind"*), `Roulade`, and six roller-skating variants (`Rollers`, `Swizzle`, `RollerCrouch`, `RollerSlope`, `RollerStandUp`, `Spin`).
- **A shared 61-dimensional observation contract** across every policy — 48 proprioception + commands `[twist(3), head_pose(4), body_pose(6)]` — *"which is what makes runtime policy hot-swapping possible. Envs that don't use a command slot zero-pad it rather than dropping it."* This is the architectural decision that lets the robot switch between walk / recover / trick brains mid-operation.
- **Model variants per task family**, because collision geometry is a training-cost decision: `robot_walk.xml` strips trunk and head contacts (*"falling is cheap"*), `robot_allcollisions.xml` for anything that must lie on the ground, `robot_allcollisions_rollers.xml` for skates.
- MJCF exported from **Onshape** via `onshape-to-robot` (Rhoban).

### Actuator fidelity is the sim-to-real gap at this scale

The load-bearing engineering claim, stated flatly in the repo:

> "At this scale — tiny servos driving a ~800 g biped — **actuator fidelity is most of the sim2real gap**, which is why the actuator is modeled down to its voltage control law instead of an ideal PD."

Concretely (see [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md)):

- **BAM M6 actuator model** ([Rhoban](https://github.com/Rhoban/bam)) for the **[Dynamixel](../entities/dynamixel.md) XL330**: voltage control law, back-EMF, and Coulomb / Stribeck / load-dependent friction.
- **Domain randomization on the actuator, not the scene**: battery voltage, **voltage sag under load**, command delay, friction magnitude.
- **Backlash modeled as physics, not noise.** Every main task has a `-Backlash` twin training against **±1° of gear play (2° total)** in series with each servo joint. The implementation detail is the good part: each servo gets an unactuated `passive_<joint>_backlash` hinge, and *because the real encoder sits on the output side of the play*, both the firmware PD emulation and the `joint_pos` / `joint_vel` observations read **through** the backlash (`qpos[servo] + qpos[backlash]`). Observation and action dimensions are unchanged, so ONNX export and the runtime need no changes.
- **The exporter bakes the observation normalizer into the ONNX graph** — *"always deploy ONNX produced by `scripts/export.py`, never a hand-converted checkpoint, or the policy sees unnormalized observations at runtime."* A deployment footgun worth remembering well beyond this robot.

### Why small, in the makers' words (launch blog)

> "Learning movement is messy. A robot has to try things, fail, and try again. On a large humanoid, every bad attempt can be expensive, difficult to reset, or simply unsafe to run outside a robotics lab. … A failed behavior usually ends with a little robot on the floor, not a major incident. **Self-recovery also means you do not have to pick it up after every failed attempt.**"

The self-recovery policy is therefore not a party trick — it is **reset automation**, the thing that makes unattended real-world iteration possible on a desk. Compare the wiki's [real-world robot RL](../concepts/learning/real-world-robot-rl.md) coverage, where reset cost is the recurring blocker.

Also: *"Microduck is about ten times more fun when there are several of them. … For developers, it also creates a practical way to explore multi-robot behaviors without a room full of expensive hardware."* At $399, a **four-robot [multi-agent RL](../concepts/learning/multi-agent-rl.md) testbed costs $1,596** — cheaper than one SO-ARM101 pair plus a workstation GPU.

### Company facts (press kit boilerplate)

> "Pollen Robotics builds open-source robots from **Bordeaux, France**. **Founded in 2016 by former Inria researchers**, the team **joined Hugging Face in April 2025** and is its robotics team. Microduck is their **second consumer robot**, after Reachy Mini."

And from the launch blog: **"more than 10,000"** Reachy Minis shipped since its launch.

## Entities mentioned

- [Microduck](../entities/microduck.md) — the robot
- [Pollen Robotics](../entities/pollen-robotics.md) — maker
- [Hugging Face](../entities/hugging-face.md) — parent since April 2025
- [Reachy Mini](../entities/reachy-mini.md) — sibling product
- [Reachy 2](../entities/reachy.md) — the flagship
- [mjlab](../entities/mjlab.md) — training framework
- [MuJoCo](../entities/mujoco.md) — physics engine
- [Dynamixel](../entities/dynamixel.md) — XL330 servos
- [LeRobot](../entities/lerobot.md) — sibling HF robotics stack (notably *not* used here)

## Companion source

- [`pollen-robotics/microduck` — the onboard runtime](microduck-runtime-repo.md) — the code and design docs behind every runtime claim above.

## Concepts touched

- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md)
- [Actuator fidelity in sim-to-real](../concepts/learning/actuator-fidelity-sim2real.md)
- [Real-world robot RL](../concepts/learning/real-world-robot-rl.md)
- [Multi-agent RL](../concepts/learning/multi-agent-rl.md)

## Open questions

> [!note] Several of these were answered the same day
> The [onboard runtime repo](microduck-runtime-repo.md) was ingested immediately after this page and settles the motor count, the perception path and the compute ceiling. It also shows that **policies on the Hub is a roadmap item (M8), not a shipped feature** — today every policy ships inside the daemon artifact, and `robotd` has no way to swap an ONNX session under a running 50 Hz loop.

- **Why is Microduck not a [LeRobot](../entities/lerobot.md) platform?** Both Pollen and LeRobot are Hugging Face. LeRobot natively supports [Reachy 2](../entities/reachy.md) and has RL implementations (HIL-SERL, [TD-MPC](../entities/td-mpc.md)). Microduck instead ships its own Rust runtime + mjlab stack with no LeRobot dependency visible. Deliberate separation of the IL-manipulation stack from the RL-locomotion stack, or just a team that shipped what it already had? The `microduck_rl` repo predates the product repo by eight months (created 2025-12-06 vs 2026-07-29), which favours the second reading.
- ~~**What runs the camera and the ToF?**~~ **Answered** by the [runtime repo](microduck-runtime-repo.md), ingested the same day: depth is its own daemon (`tofd`) publishing the 8×8 matrix on its own socket; the camera lives in `mediad` with perception beside it; a `yolo11n` duck detector runs on the RK3566's **0.8 TOPS NPU** at p50 25.7 ms. But the autonomous brain that would consume any of it is **unported and has no design doc**, and no IPC yet exposes a camera frame at all.
- **Can an RK3566 with 1 GB RAM run anything larger than an MLP?** Partly answered: **yes, small vision** — a quantised `yolo11n` at 320×320 costs 3.9 MB and ~26 ms on the 0.8 TOPS NPU ([runtime repo](microduck-runtime-repo.md)). A [VLA](../concepts/learning/vla-models.md) remains impossible. Microduck is a locomotion-RL platform that structurally cannot host the wiki's dominant policy class — an interesting counterexample to the assumption that consumer robots converge on VLA-capable compute.
- **Spec sheet is explicitly provisional.** Press kit: *"Camera resolution and field of view, LiDAR range, radio versions and SDK languages are still being finalised — and so is any age recommendation."* Re-check at ship.
- Pre-orders opened the day of this ingest; **no independent reviews, no delivered units, no third-party verification of any number here**. Everything above is vendor-stated or vendor-published code.
