---
title: Whole-Body Control (WBC)
type: concept
created: 2026-07-15
updated: 2026-08-29
sources: 26
tags: [whole-body-control, wbc, humanoid, motion-tracking, loco-manipulation, unitree-g1, booster-t1, rl, sim-to-real, amass, agile, code, system-0, helix, figure-03]
---

# Whole-Body Control (WBC)

**Whole-body control** — coordinating *all* of a high-DoF robot's actuated joints into stable, coherent, dynamically-feasible motion, so a humanoid can walk, jump, crouch, box, and (increasingly) manipulate objects with its whole body rather than an isolated arm. For learning-based humanoids in this wiki, WBC is usually posed as a **motion-tracking** problem: an RL policy tracks a stream of retargeted reference poses (typically from human mocap, e.g. [AMASS](https://amass.is.tue.mpg.de/) → SMPL → robot), trained in sim ([Isaac Lab](../../entities/nvidia-isaac-lab.md)/IsaacGym or [MuJoCo](../../entities/mujoco.md)) and transferred to hardware.

WBC is the **low-level "System 1"** layer beneath a VLA/task policy: a [VLA](../learning/vla-models.md) (e.g. [GR00T](../../entities/nvidia-groot.md)) decides *what* to do and emits high-level commands or motion tokens; the WBC controller turns those into stable joint torques at 50–500 Hz. The wiki's clearest instance of that split is [SONIC](../../sources/sonic-paper.md), where a GR00T N1.5 VLA predicts universal motion tokens decoded by the SONIC WBC policy.

## The central problem: gradient conflict at scale

Training **one** policy on the full, diverse motion corpus is hard because different motion types demand *opposite* control priorities — aggressive jumps/fast walks need high-torque precision; conservative standing/reaching needs balance and smoothness. Mixed distributions cause **conflicting gradients** that degrade a naive generalist ([BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md)). The field has two broad answers:

- **"Be more powerful" (model level)** — larger/expressive backbones (Transformers, diffusion, big token models) that absorb a diverse distribution. [SONIC](../../sources/sonic-paper.md) (scale a single motion-tracking policy across model/data/compute) and [MotionBricks](../../sources/motionbricks-paper.md) (a 350k-clip modular latent backbone) exemplify this.
- **"Decompose the complexity" (data level)** — structure the data so specialists don't interfere. [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) clusters motions (semantic + kinematic), trains a per-cluster expert, and **distills experts → one generalist**. Exbody2's difficulty-progressive curriculum is a lighter version.

## Sim-to-real

The dominant real-world-adaptation trick in this cluster is **delta-action modeling** (from **[ASAP](../../sources/asap-paper.md)**, now ingested): fit a residual `π_Δ(s,a)` from real rollouts, reshape the simulator `s' = f_sim(s, a+π_Δ)`, and fine-tune the tracking policy in the corrected sim — iterated. [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) shows per-cluster delta-models beat one global delta-model (cluster-consistent dynamics fit better) — which is a direct, if polite, correction to ASAP's claim that its single global model is "not overfitted" and that iterating lifts real-robot success and foot stability. Foot placement is repeatedly the hardest residual gap ([SONIC](../../sources/sonic-paper.md): 53.7 vs 29.0 mm sim).

> [!note] The classical ancestor, and what the learned version gives up
> Model-based WBC is largely [operational space control](operational-space-control.md) (Khatib 1987) plus null-space prioritization on a floating base: a QP per tick with task objectives as **costs** and joint/torque/contact limits as **hard constraints**. The learned WBC policies on this page replace that QP with a network — buying robustness and contact-richness, and **giving up the hard-constraint property**, which is why the manipulation stacks in this wiki still keep a constrained QP between policy and hardware.

## Key references

- **[SONIC](../../sources/sonic-paper.md)** (NVIDIA [GEAR](../../entities/nvidia-gear.md), 2025-11) — motion tracking as *the* scalable foundational task; FSQ universal token space as the VLA↔controller interface; direct sim-to-real on [Unitree G1](../../entities/unitree-g1.md).
- **[MotionBricks](../../sources/motionbricks-paper.md)** (NVIDIA, SIGGRAPH 2026) — real-time (15k FPS/2ms) modular latent motion model spanning animation + robotics; smart-primitive interface adds object interaction SONIC lacks.
- **[BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md)** ([BeingBeyond](../../entities/beingbeyond.md) + Peking Univ, 2025-09) — clustered expert→generalist distillation; SOTA general WBC on G1, with the largest margin in realistic MuJoCo dynamics.
- **The 2024–25 foundation of this cluster, ingested 2026-08-29** — previously carried here only as secondhand names:
  - **[H2O](../../sources/h2o-paper.md)** (CMU, IROS 2024) — first learning-based real-time whole-body teleoperation from an RGB camera; introduces **"sim-to-data"**, using a privileged imitator to *delete* retargeted motions the robot cannot physically perform.
  - **[OmniH2O](../../sources/omnih2o-paper.md)** (CMU, CoRL 2024) — **kinematic pose as a universal control interface** (VR / voice / RGB / GPT-4o / learned policy), teacher–student distillation to sparse sensors, and the finding that **input history can replace the global linear velocity** that previously required MoCap.
  - **[HumanPlus](../../sources/humanplus-paper.md)** (Stanford, CoRL 2024) — shadowing from 40 h of human motion, then behavior cloning from egocentric vision; **60–100% on six autonomous tasks with ≤40 demonstrations**.
  - **[ASAP](../../sources/asap-paper.md)** (CMU + NVIDIA, 2025) — the delta-action-model primary, described in [Sim-to-real](#sim-to-real) above.
  - **[HOVER](../../sources/hover-paper.md)** (NVIDIA [GEAR](../../entities/nvidia-gear.md) + CMU, 2024) — multi-mode distillation with mode and sparsity masks; the generalist **beats specialists in their own modes**, which is the strongest form of the decomposition-vs-scale argument this page opens with.
  - **Exbody2** remains uningested.
  (The [GEAR publications page](../../sources/nvidia-gear-publications.md) is where HOVER/ASAP were previously reachable from.)

## Code / tooling

- **[GR00T-WholeBodyControl](../../sources/gr00t-wholebodycontrol-github.md)** (NVlabs) — the unified NVIDIA WBC toolchain: [GEAR-SONIC](../../entities/gear-sonic.md) training (`gear_sonic`, PPO) + C++/TensorRT deploy (`gear_sonic_deploy`) + [MotionBricks](../../sources/motionbricks-paper.md) + **Decoupled WBC** (the [GR00T](../../entities/nvidia-groot.md) N1.5/N1.6 controllers). Apache-2.0 code + NVIDIA Open Model License weights.
- **[WBC-AGILE](../../sources/wbc-agile-github.md)** ("A Generic Isaac-Lab based Engine for humanoid loco-manipulation," NVIDIA + ETH) — a reusable Isaac-Lab RL **engine** (teacher-student distillation, privileged critic) rather than a single controller; validated sim-to-real on **[Unitree G1](../../entities/unitree-g1.md) + [Booster T1](../../entities/booster-t1.md)** (a second benchmark humanoid). It's the "AGILE" underneath [Isaac Teleop](../../entities/nvidia-isaac-teleop.md) in NVIDIA's [GR00T end-to-end workflow](../../sources/nvidia-gr00t-e2e-workflow-docs.md).

## WBC in a shipped commercial stack: Figure's System 0

Added 2026-08-28. Everything above is academic or open-source. [Helix 02](../../sources/figure-helix-02.md) (Figure AI, Jan 2026) is the wiki's first look at the same recipe inside a **closed, commercially deployed** humanoid stack — [Helix](../../entities/helix.md)'s **System 0**, running on [Figure 03](../../entities/figure-03.md):

- **10M parameters**, in: full-body joint state + base motion; out: joint-level actuator commands at **1 kHz** — a third tier *below* the S1 (200 Hz visuomotor) / S2 (7–9 Hz VLM) split, so the VLA emits joint targets and S0 tracks them.
- Trained on **1,000+ hours of joint-level retargeted human motion**, entirely in sim across **200,000+ parallel environments** with domain randomisation, transferring directly to hardware and "across the fleet."
- No per-behaviour reward engineering: walking, turning, crouching and reaching all fall out of motion tracking — the same bet as [SONIC](../../sources/sonic-paper.md) and against the per-cluster-expert decomposition of [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md).
- Figure's headline framing: S0 **"replaces 109,504 lines of hand-engineered C++ with a single neural prior."** Taken at face value, that is the clearest statement anyone has made that learned WBC has displaced model-based WBC in a production humanoid.

**Perception-conditioned S0** followed in April 2026 ([production ramp](../../sources/figure-ramping-03-production.md)). Before: S0 "walked confidently across flat ground but was blind to the world in front of it. Stairs, ramps, and uneven terrain required hand-tuned mode switches and operator intervention." After: head-camera RGB is lifted to 3D through Figure's stereo model and fed to the policy alongside proprioception, trained end-to-end with RL across thousands of randomised terrains, transferring **zero-shot** to real stairs — "no real-world fine-tuning, no domain-specific calibration, no operator-in-the-loop adjustments."

> [!note] Architecturally unremarkable, which is the point
> 10M params, 1 kHz, mocap retargeting, massive-parallel sim, domain randomisation — this is the recipe the rest of this page already documents. That a company betting $39B on humanoids converged on it independently is corroboration for the approach. What Figure adds is **deployment**: OTA delivery to a 350+ unit fleet built at one robot per hour.

> [!warning] No numbers, at all
> Figure publishes **no tracking error, no success rate, no baseline, no ablation** for S0 — nothing comparable to SONIC's 53.7 vs 29.0 mm foot placement. The architecture is described; the performance is asserted. Cite S0 for *what was built*, never for *how well it works*.

> [!note] This branch went the opposite way from quadruped locomotion
> Every paper in this humanoid cluster except [ASAP](../../sources/asap-paper.md) is built on **privileged oracle-to-student distillation** — [H2O](../../sources/h2o-paper.md) uses it to filter data, [OmniH2O](../../sources/omnih2o-paper.md) to reach sparse sensors, [HOVER](../../sources/hover-paper.md) to unify modes, [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) to merge experts. Over the same period the quadruped line **abandoned** privileged teachers entirely for long context and scale ([locomotion adaptation lineage](../../syntheses/rl/locomotion-adaptation-lineage.md)). Two branches of learned legged control, moving in opposite architectural directions at the same time — see [humanoid whole-body control lineage](../../syntheses/rl/humanoid-wbc-lineage.md) for why.

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
- [Introducing Helix 02](../../sources/figure-helix-02.md) — Figure's System 0; the commercial-stack instance. [Ramping Figure 03 Production](../../sources/figure-ramping-03-production.md) — perception-conditioned S0, zero-shot stairs.
- [Gemini Robotics 2 blog](../../sources/gemini-robotics-2-blog.md) — whole-body control as a shipped VLA capability: humanoids that "walk, crouch, stretch, and manipulate" under one model. Pick-up success by height: shelf 76.3%, table 68.4%, **floor 45.7%**.
