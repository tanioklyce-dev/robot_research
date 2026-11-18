---
title: "NVIDIA/soma-retargeter v0.2.0 (GitHub)"
type: source
subtype: code-repository
url: https://github.com/NVIDIA/soma-retargeter/tree/v0.2.0
fetch_url: https://raw.githubusercontent.com/NVIDIA/soma-retargeter/v0.2.0/README.md
capture: bundle
local_path: raw/2026-11-17-soma-retargeter-github-v0.2.0.md
sha256: e5441452742725be8a1556ed915f9c961f5a714c71a777610f658d8208655deb
author: NVIDIA
published: 2026-09-15
ingested: 2026-11-17
license: "code Apache-2.0; bundled motions NVIDIA Sample Data Evaluation License; robot assets BSD-3-Clause (Unitree, Booster) and Mulan PSL v2 (AgiBot)"
format: "repository at tag v0.2.0 (commit 1733b82). Captured as a bundle of six files (README, CHANGELOG, code overview, configuration reference, IK weight optimizer, foot contact). Also read: installation, compare-and-tune, batch-retargeting and troubleshooting docs, the motion-data licence, and the v0.2.0→v0.2.1 diff. Source code not read beyond file names."
tags: [soma-retargeter, motion-retargeting, humanoid, nvidia, newton, warp, inverse-kinematics, levenberg-marquardt, gmr, pyroki, bones-seed, licensing, unitree-g1, unitree-h2, booster-t1, agibot, primary]
---

# NVIDIA/soma-retargeter v0.2.0 (GitHub)

## Summary

The repository behind [NVIDIA's SOMA Retargeter post](nvidia-soma-retargeter-blog.md), at the tag that post links. It is the primary for how the tool works, and it settles several things the post left open. The solver is Newton's **Levenberg–Marquardt IK** with position, rotation, joint-limit and smoothing objectives, run per frame on the GPU. The tool **does not support high-DoF hands**. It names **GMR and PyRoki** as the open-source work it builds on. The README states plainly that "generated motion is kinematic" and must be validated in simulation before hardware. And the licensing is split: the code is Apache-2.0, but the bundled motion clips are under an **evaluation-only** NVIDIA licence. The repository, like the post, contains no benchmark of retargeting quality; what it adds is an optimiser that reports tracking and smoothness metrics for your own robot.

## Key claims

### Status and requirements
- "SOMA Retargeter is in active beta, so APIs and features may change without notice."
- "Generated motion is kinematic; validate its safety, feasibility, and controller compatibility in simulation before hardware use."
- **Requires an NVIDIA GPU** (Maxwell or newer, driver 545+), Python 3.12, Git LFS; Windows or Linux on x86-64. No local CUDA toolkit.
- **Releases**: v0.1.0 (2026-03-16), v0.2.0 (2026-09-15), v0.2.1 (2026-10-01, one Robot Configurator bug fix). The blog post that introduced the tool publicly was published two months after v0.2.0.

### The pipeline (code overview)
1. Scale human effector targets to robot proportions.
2. Prepend initialisation and stabilisation frames.
3. **Base IK pass**: "Newton Levenberg–Marquardt with position, rotation, joint-limit, and smooth-filter objectives," executed per frame with CUDA-graph capture. All five bundled robot configurations use 24 IK iterations per frame (the limb stabiliser in the post-process pass uses 20).
4. Optional post-process pass: two-bone limb stabilisation for feet and hands, and foot-plant correction blending.
5. Hard clamp of all joints to model limits.

Output is a CSV of root pose and actuated joint values; "two target robots can have different columns, even when they were generated from the same BVH."

### What it does not handle
- **Hands**: "High-DOF hands are not supported yet. Avoid registering robot descriptions that include articulated fingers or dense hand mechanisms. The current retargeting workflow is designed for humanoid body motion."
- **Other skeletons**: input must use "the source hierarchy and naming used by the SOMA base skeleton. An arbitrary BVH exported from another character or motion capture package may load incorrectly or fail." Adding a new source skeleton "is a code change, not a config change."
- **Dynamics**: nothing beyond kinematics. Robots "are assumed to be at origin and feet on the ground."

### Foot contact
Contact is detected **on the human skeleton only**, from foot speed and jerk (contact starts below 0.1 m/s, ends above 0.2 m/s for two frames), then promoted to a "plant" if the sole is within 25° of flat, the foot moves less than 1 cm per frame, and a confidence score passes 0.5. The robot supplies no foot geometry; the correction is blended into the robot's foot targets. The feature is labelled experimental.

### IK weight optimiser
- An experimental, corpus-level tool that repeatedly retargets a set of motions, measures solved poses against the scaled targets, and adjusts only the per-effector position and rotation weights, accepting a change only if it improves the objective and passes a guard against per-frame regressions.
- Reports position error in metres, rotation error in radians, smoothness, and mean, p95 and worst-frame tracking loss, per motion and per iteration.
- The docs warn: "Lower loss is evidence, not proof that the motion is better for control or deployment," and "avoid optimizing around motions the robot cannot realistically perform, because the optimizer may learn weights that chase impossible targets."
- Ships with 15 BONES-SEED clips as a starting corpus (throwing, digging, dancing, jumping, walking). The bundled config cannot run unchanged; its input folder is empty.

### Robots and assets
Five bundled targets: Unitree G1 (default) and H2, Booster T1, AgiBot X2 Ultra and A3T3. The tutorial for adding a robot uses Unitree H1. Robots are registered from URDF or MJCF through manifests (new in v0.2.0, which broke v0.1 configurations).

### Licensing
- Code: Apache-2.0.
- **Bundled motions** (10 example BVH clips, their CSV results for all five robots, and the 15 optimiser clips): "NVIDIA Sample Data Evaluation License," which grants internal use "solely to evaluate and test NVIDIA technologies" and forbids distributing the data or derivative works. The README points to BONES-SEED for "the broader motion collection and licensing options."
- Robot models: BSD-3-Clause for Unitree and Booster; Mulan PSL v2 for AgiBot.

### Lineage
"This project draws inspiration and builds upon excellent open-source work, including GMR (General Motion Retargeting) and PyRoki." These are the two tools the [SONIC paper](sonic-paper.md) used to retarget its 700 hours of capture.

## What this changes in the wiki
- The [blog post's](nvidia-soma-retargeter-blog.md) open question about hands is answered: not supported. The tool is for body motion only, so it does not compete with the hand retargeting used for dexterous learning ([EgoScale](egoscale-paper.md), [Gemini 4 Argon](gemini-4-argon-robotics-blog.md)).
- SOMA Retargeter and the GMR + PyRoki pipeline are not alternatives so much as the same approach repackaged around NVIDIA's skeleton. Which one produced SONIC's published data is still unstated, but the lineage makes the question less consequential.
- **For anyone building a training set**: the motion files in this repository cannot be used to train and ship a policy under their licence. Retargeting BONES-SEED, or your own capture, is the route, and BONES-SEED has its own access terms.

## Entities mentioned
- [NVIDIA](../entities/nvidia.md) · [Newton physics engine](../entities/newton-physics-engine.md)
- [Unitree G1](../entities/unitree-g1.md) · [Unitree H2](../entities/unitree-h2.md) · [Unitree H1](../entities/unitree-h1.md) (tutorial) · [Booster T1](../entities/booster-t1.md) · [AgiBot](../entities/agibot.md)
- [GEAR-SONIC](../entities/gear-sonic.md) (related work)
- No entity pages: GMR, PyRoki, SOMA-X, BONES-SEED, ProtoMotions, Kimodo, GEM-X

## Concepts touched
- [Motion retargeting](../concepts/robotics/motion-retargeting.md)
- [Whole-body control](../concepts/robotics/whole-body-control.md)

## Open questions
- Retargeting quality against GMR on a shared corpus. Neither repository nor post reports one.
- What changed between v0.1 and v0.2 in output quality. The changelog says mappings and scaling were "improved for better pose matching" without numbers.
- Throughput: no per-clip or per-hour timing is documented.

## Related sources
- [Adapt Human Motion for Robots with NVIDIA SOMA Retargeter](nvidia-soma-retargeter-blog.md): the announcement and tutorial.
- [SONIC paper](sonic-paper.md): GMR + PyRoki at 700 hours; BONES-SEED.
- [MotionBricks paper](motionbricks-paper.md): trained partly on SOMA-retargeted motion.
