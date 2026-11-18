---
title: Motion retargeting
type: concept
created: 2026-11-17
updated: 2026-11-17
sources: 13
tags: [motion-retargeting, humanoid, human-motion, mocap, inverse-kinematics, whole-body-control, teleoperation, dexterous-hands, cross-embodiment, amass, bones-seed]
---

# Motion retargeting

**Motion retargeting** is converting motion recorded on one body, usually a human, into motion for a different body: a humanoid, a robot hand, or an animated character. The human and the robot differ in limb lengths, joint structure, joint limits and mass, so copying joint angles does not work. As NVIDIA puts it, "a robot cannot simply copy the same joint motion from a human" ([SOMA Retargeter post](../../sources/nvidia-soma-retargeter-blog.md)).

In robot learning the word covers three different jobs, and they fail in different ways.

## Three uses

**1. Reference motion for whole-body tracking policies (offline, body).** A human motion corpus is retargeted to a humanoid and becomes the target a tracking policy learns to follow in simulation. This is the dominant use in the wiki:

| System | Corpus | Target | Source |
|---|---|---|---|
| H2O | [AMASS](../../entities/amass.md), 10k sequences | [Unitree H1](../../entities/unitree-h1.md) | [H2O paper](../../sources/h2o-paper.md) |
| BumbleBee | AMASS, PHC-filtered to 8,179 | [Unitree G1](../../entities/unitree-g1.md) | [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) |
| ASAP | retargeted human motion | G1 | [ASAP paper](../../sources/asap-paper.md) |
| [SONIC](../../entities/gear-sonic.md) | ~700 h mocap via GMR + PyRoki, filtered to 611 h | G1 | [SONIC paper](../../sources/sonic-paper.md) |
| Helix 02 System 0 | "over 1,000 hours of joint-level retargeted human motion data" | [Figure 03](../../entities/figure-03.md) | [Helix 02](../../sources/figure-helix-02.md) |
| SOMA Retargeter v0.2 | BONES-SEED and any SOMA-skeleton source | G1, H2, Booster T1, two AgiBot humanoids | [post](../../sources/nvidia-soma-retargeter-blog.md), [repo](../../sources/soma-retargeter-github.md) |

**2. Teleoperation (online).** The operator's tracked pose is mapped to the robot in real time. NVIDIA's [Isaac Teleop](../../entities/nvidia-isaac-teleop.md) ships "retargeters" as a package component ([source](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md)); [UMe](../../entities/ume.md) retargets one exoskeleton to three arms, only one of them demonstrated on real hardware ([source](../../sources/ume-paper.md)).

**3. Action labels from human hands (dexterous).** Human hand motion from video or gloves is mapped to a robot hand's joints to make training actions. [EgoScale](../../sources/egoscale-paper.md) uses "retargeted 22-DoF dexterous hand joint actions" for a [Sharpa Wave](../../entities/sharpa-wave.md) hand; [Gemini 4 Argon](../../sources/gemini-4-argon-robotics-blog.md) retargets egocentric hand keypoints to a 76-DoF simulated humanoid.

## The recurring problem: retargeted motion is often infeasible

Retargeting is kinematic. It matches poses within joint limits; it does not check balance, contact forces or actuator torque. The consequences show up the same way across sources:

- **Filtering is part of the pipeline.** H2O's central idea is "sim-to-data": a large retargeted corpus contains many motions the robot "physically cannot do," so a privileged policy in simulation is used to discard them ([H2O](../../sources/h2o-paper.md)). BumbleBee filters with PHC; SONIC filters about 700 hours down to 611.
- **Foot sliding is the commonest artifact.** SOMA Retargeter adds a foot-plant correction because a sliding reference foot gives a tracking policy "conflicting targets" ([source](../../sources/nvidia-soma-retargeter-blog.md)).
- **For contact-rich manipulation it is not enough on its own.** In [SimToolReal](../../sources/simtoolreal-paper.md), a kinematic-retargeting baseline reached 8.1% success in simulation and 0% on the real robot: "kinematic motion establishes no stable contact."

The tools say so themselves. SOMA Retargeter's README: "Generated motion is kinematic; validate its safety, feasibility, and controller compatibility in simulation before hardware use" ([repository](../../sources/soma-retargeter-github.md)).

So a retargeter produces a *reference*. Something downstream, a tracking policy trained in simulation or a filter that runs one, has to turn it into motion the robot can actually execute.

## Body tools and hand tools are separate

The open body retargeters do not do hands. SOMA Retargeter's documentation: "High-DOF hands are not supported yet... The current retargeting workflow is designed for humanoid body motion" ([repository](../../sources/soma-retargeter-github.md)). Hand retargeting for dexterous learning, as in EgoScale and Argon, is done with separate, usually per-hand, pipelines.

## The open tools share a lineage

SOMA Retargeter "builds upon" GMR and PyRoki ([repository](../../sources/soma-retargeter-github.md)), the same two tools the [SONIC paper](../../sources/sonic-paper.md) used for its 700 hours of capture. It solves per-frame inverse kinematics with Levenberg–Marquardt over weighted position, rotation, joint-limit and smoothing objectives, then corrects foot contacts detected on the human side. Its contribution is packaging around one skeleton, a configurator for new robots, and an optimiser for the objective weights, not a different method.

## Representation is the leverage point

Retargeting cost scales with sources times robots unless both sides meet in a shared format. Two standards appear in the wiki: SMPL (the format of AMASS, used by the CMU H2O line and BumbleBee) and NVIDIA's SOMA skeleton, which its capture dataset (BONES-SEED), single-video reconstruction (GEM-X) and two text-to-motion generators all emit. With a shared skeleton, configuring one new robot makes every source usable for it ([SOMA Retargeter post](../../sources/nvidia-soma-retargeter-blog.md)).

## Current state

Retargeting has become routine infrastructure for humanoid whole-body control: every learned whole-body controller in the wiki trains on retargeted human motion, and the corpora have grown from thousands of AMASS clips to hundreds or thousands of hours. What is still missing from the public record is measurement of the retargeter itself. None of the ingested sources compares retargeters on a common metric, and the open tools (GMR, PyRoki, SOMA Retargeter) are described by what they do, not by how well. SOMA Retargeter's optimiser reports position, rotation and smoothness errors per motion for your own robot, which is the closest thing to a quality measure any of them publishes.

## Related concepts
- [Whole-body control](whole-body-control.md): the main consumer of retargeted body motion.
- [Cross-embodiment](../learning/cross-embodiment.md): retargeting is the explicit, hand-designed form of the mapping that cross-embodiment learning tries to learn.
- [Imitation learning](../learning/imitation-learning.md): retargeted human motion and hand poses as demonstrations.
- [Real-to-sim-to-real](real-to-sim-to-real.md): retargeted human video as a source of simulated demonstrations.

## Mentioned in
- [Adapt Human Motion for Robots with NVIDIA SOMA Retargeter](../../sources/nvidia-soma-retargeter-blog.md) — the tool, the shared skeleton, foot-plant correction.
- [NVIDIA/soma-retargeter v0.2.0 (GitHub)](../../sources/soma-retargeter-github.md) — the solver (Levenberg–Marquardt IK), no hand support, GMR and PyRoki lineage, evaluation-only sample data.
- [H2O paper](../../sources/h2o-paper.md) — sim-to-data filtering of infeasible retargeted motion.
- [SONIC paper](../../sources/sonic-paper.md) — GMR + PyRoki at 700 hours; BONES-SEED.
- [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md) — AMASS to G1 with PHC filtering.
- [ASAP paper](../../sources/asap-paper.md) — retargeted motion as tracking pretraining.
- [Introducing Helix 02](../../sources/figure-helix-02.md) — over 1,000 hours of retargeted motion for System 0.
- [EgoScale](../../sources/egoscale-paper.md) — retargeted hand joints as action labels.
- [Gemini 4 Argon for Robotics](../../sources/gemini-4-argon-robotics-blog.md) — hand keypoints retargeted to a 76-DoF humanoid in simulation.
- [SimToolReal](../../sources/simtoolreal-paper.md) — kinematic retargeting fails for dexterous tool use.
- [NVIDIA Isaac Teleop and GR00T 1.7 in LeRobot](../../sources/nvidia-isaac-teleop-gr00t17-lerobot-blog.md) — retargeters in a teleoperation stack.
- [UMe paper](../../sources/ume-paper.md) — one exoskeleton retargeted to three arms.
- [MotionBricks paper](../../sources/motionbricks-paper.md) — generative motion whose G1 model trained partly on SOMA-retargeted data.

## Open questions
- A common metric for retargeting quality, and a comparison of the open retargeters on it.
- How much downstream policy performance depends on retargeter quality versus the filtering step after it.
