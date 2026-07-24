---
title: Whole-Body Control (WBC)
type: concept
created: 2026-07-15
updated: 2026-07-15
sources: 8
tags: [whole-body-control, wbc, humanoid, motion-tracking, loco-manipulation, unitree-g1, booster-t1, rl, sim-to-real, amass, agile, code]
---

# Whole-Body Control (WBC)

**Whole-body control** — coordinating *all* of a high-DoF robot's actuated joints into stable, coherent, dynamically-feasible motion, so a humanoid can walk, jump, crouch, box, and (increasingly) manipulate objects with its whole body rather than an isolated arm. For learning-based humanoids in this wiki, WBC is usually posed as a **motion-tracking** problem: an RL policy tracks a stream of retargeted reference poses (typically from human mocap, e.g. [AMASS](https://amass.is.tue.mpg.de/) → SMPL → robot), trained in sim ([Isaac Lab](../../entities/nvidia-isaac-lab.md)/IsaacGym or [MuJoCo](../../entities/mujoco.md)) and transferred to hardware.

WBC is the **low-level "System 1"** layer beneath a VLA/task policy: a [VLA](../learning/vla-models.md) (e.g. [GR00T](../../entities/nvidia-groot.md)) decides *what* to do and emits high-level commands or motion tokens; the WBC controller turns those into stable joint torques at 50–500 Hz. The wiki's clearest instance of that split is [SONIC](../../sources/sonic-paper.md), where a GR00T N1.5 VLA predicts universal motion tokens decoded by the SONIC WBC policy.

## The central problem: gradient conflict at scale

Training **one** policy on the full, diverse motion corpus is hard because different motion types demand *opposite* control priorities — aggressive jumps/fast walks need high-torque precision; conservative standing/reaching needs balance and smoothness. Mixed distributions cause **conflicting gradients** that degrade a naive generalist ([BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md)). The field has two broad answers:

- **"Be more powerful" (model level)** — larger/expressive backbones (Transformers, diffusion, big token models) that absorb a diverse distribution. [SONIC](../../sources/sonic-paper.md) (scale a single motion-tracking policy across model/data/compute) and [MotionBricks](../../sources/motionbricks-paper.md) (a 350k-clip modular latent backbone) exemplify this.
- **"Decompose the complexity" (data level)** — structure the data so specialists don't interfere. [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) clusters motions (semantic + kinematic), trains a per-cluster expert, and **distills experts → one generalist**. Exbody2's difficulty-progressive curriculum is a lighter version.

## Sim-to-real

The dominant real-world-adaptation trick in this cluster is **delta-action modeling** (from **ASAP**): fit a residual `π_Δ(s,a)` from real rollouts, reshape the simulator `s' = f_sim(s, a+π_Δ)`, and fine-tune the tracking policy in the corrected sim — iterated. [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) shows per-cluster delta-models beat one global delta-model (cluster-consistent dynamics fit better) and that iterating lifts real-robot success and foot stability. Foot placement is repeatedly the hardest residual gap ([SONIC](../../sources/sonic-paper.md): 53.7 vs 29.0 mm sim).

## Key references

- **[SONIC](../../sources/sonic-paper.md)** (NVIDIA [GEAR](../../entities/nvidia-gear.md), 2025-11) — motion tracking as *the* scalable foundational task; FSQ universal token space as the VLA↔controller interface; direct sim-to-real on [Unitree G1](../../entities/unitree-g1.md).
- **[MotionBricks](../../sources/motionbricks-paper.md)** (NVIDIA, SIGGRAPH 2026) — real-time (15k FPS/2ms) modular latent motion model spanning animation + robotics; smart-primitive interface adds object interaction SONIC lacks.
- **[BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md)** ([BeingBeyond](../../entities/beingbeyond.md) + Peking Univ, 2025-09) — clustered expert→generalist distillation; SOTA general WBC on G1, with the largest margin in realistic MuJoCo dynamics.
- Prior art referenced across the above: **ASAP, HOVER, OmniH2O/H2O, HumanPlus, Exbody2** (see the [GEAR publications page](../../sources/nvidia-gear-publications.md) for HOVER/ASAP arXiv links).

## Code / tooling

- **[GR00T-WholeBodyControl](../../sources/gr00t-wholebodycontrol-github.md)** (NVlabs) — the unified NVIDIA WBC toolchain: [GEAR-SONIC](../../entities/gear-sonic.md) training (`gear_sonic`, PPO) + C++/TensorRT deploy (`gear_sonic_deploy`) + [MotionBricks](../../sources/motionbricks-paper.md) + **Decoupled WBC** (the [GR00T](../../entities/nvidia-groot.md) N1.5/N1.6 controllers). Apache-2.0 code + NVIDIA Open Model License weights.
- **[WBC-AGILE](../../sources/wbc-agile-github.md)** ("A Generic Isaac-Lab based Engine for humanoid loco-manipulation," NVIDIA + ETH) — a reusable Isaac-Lab RL **engine** (teacher-student distillation, privileged critic) rather than a single controller; validated sim-to-real on **[Unitree G1](../../entities/unitree-g1.md) + [Booster T1](../../entities/booster-t1.md)** (a second benchmark humanoid). It's the "AGILE" underneath [Isaac Teleop](../../entities/nvidia-isaac-teleop.md) in NVIDIA's [GR00T end-to-end workflow](../../sources/nvidia-gr00t-e2e-workflow-docs.md).

## Related concepts

- [VLA models](../learning/vla-models.md) — the high-level System-2 layer WBC sits under.
- [Sim-to-real transfer](../learning/sim-to-real-transfer.md), [imitation learning](../learning/imitation-learning.md) (DAgger distillation), [optimal control](optimal-control.md) (the model-based counterpart).
- [Motion planning](motion-planning.md) — the classical-planning neighbor; WBC here is learned, not planned.
- [Robot combat sports as a development testbed](robot-combat-sports.md) — humanoid fighting leagues ([URKL](../../sources/urkl-robot-combat-league.md) / [EngineAI T800](../../entities/engineai-t800.md)) as an adversarial real-world stress-test of the balance/fall-recovery WBC exercises.

## Mentioned in

- [SONIC paper](../../sources/sonic-paper.md), [MotionBricks paper](../../sources/motionbricks-paper.md), [BumbleBee paper](../../sources/bumblebee-experts-to-generalist-wbc.md).
- [GR00T-WholeBodyControl GitHub](../../sources/gr00t-wholebodycontrol-github.md), [WBC-AGILE GitHub](../../sources/wbc-agile-github.md) — the code/tooling.
- [NVIDIA GEAR publications](../../sources/nvidia-gear-publications.md) — several WBC papers (SONIC, HOVER, ASAP, MotionBricks) in the GEAR line.
- [Unitree G1](../../entities/unitree-g1.md) — the common target platform; [Booster T1](../../entities/booster-t1.md) — AGILE's second benchmark humanoid.
