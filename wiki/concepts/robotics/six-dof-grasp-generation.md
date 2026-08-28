---
title: 6-DOF grasp generation
type: concept
created: 2026-08-23
updated: 2026-08-23
sources: 2
tags: [grasping, 6-dof-grasping, manipulation, diffusion, discriminator, cross-embodiment, gripper-morphology, acronym, modular-manipulation]
---

**6-DOF grasp generation** — given an observation of an object or scene (usually a point cloud) and a gripper, predict **SE(3) poses at which closing the gripper stably lifts the object**. Not a policy and not a trajectory: a *set of candidate end-effector poses*, ranked, handed downstream to a motion planner. It is the component that turns "that is a mug" into "put the hand here."

The distinction from the [VLA](../learning/vla-models.md) line that dominates this wiki matters. A VLA outputs actions and subsumes grasping implicitly; a 6-DOF grasp generator is a **module in a modular pick-and-place stack**, explicitly described in [GraspGen-X](../../sources/graspgenx-paper.md) as *"a crucial tool-calling subroutine in recent agentic robotics systems."* Both approaches are live in 2026 and this wiki carries evidence for each.

## The canonical two-stage structure

Since Newbury et al.'s survey the problem has decomposed into:

1. **Grasp sampling** — propose candidate poses. Historically heuristic: analytic antipodal sampling, derivative-free optimisation, or pixel-wise prediction where every depth pixel is a candidate (AnyGrasp, Contact-GraspNet). Now generative: VAEs (6-DOF GraspNet), flow matching, and **diffusion over SE(3)** (GraspGen, SE(3)-DiffusionFields).
2. **Grasp analysis** — a **discriminator** scores each candidate for success probability, producing the ranking a planner consumes.

[GraspGen](../../entities/graspgen.md) (Murali et al., 2025) is the current reference implementation of this pairing: an SE(3) diffusion generator conditioned on a PointTransformer/PointNet++ object embedding, plus a discriminator trained on **on-generator** positives and negatives — i.e. the discriminator is trained on the generator's own output distribution, in a flywheel, rather than on a fixed dataset.

## Where the training data comes from

Real grasp labels do not scale, so the field labels in simulation. **ACRONYM** (Eppner et al., 2020) is the standard pipeline: antipodal-sample candidate poses on object meshes, then execute each in a physics simulator ([Isaac Sim](../../entities/nvidia-isaac-sim.md)) and record whether the object was lifted. Scale is set by GPU-hours, not human time — GraspGen-X spent **8.7 K GPU-hours** generating 175 M generator grasps and **5.2 K** more for discriminator data ([GraspGen-X](../../sources/graspgenx-paper.md)).

This makes grasp generation one of the few manipulation problems where the **data bottleneck is compute, not teleoperation** — the opposite of the constraint governing [VLA](../learning/vla-models.md) training and the reason a grasp model can be trained on 10⁸–10⁹ examples while a VLA trains on 10⁵ episodes.

## Cross-embodiment: the hard part is the gripper, not the arm

The observation that motivates [GraspGen-X](../../sources/graspgenx-paper.md), and the reason this concept page exists:

> In a modular generalized-pick-and-place stack, **every component except grasp generation already transfers to a new robot** for free. Stereo depth and segmentation are foundation models; [motion planning](motion-planning.md) ([cuRobo](../../entities/curobo.md)) and occupancy mapping (nvblox) are model-based and need only a config file. Change the gripper and the grasp model must be **retrained** — a week of an 8-GPU node per embodiment.

Three families of response:

| Approach | Mechanism | Measured (mAUC, 10 novel grippers) |
|---|---|---|
| **Direct transfer** | Use the Franka-trained model as-is | **0.126** — collapses to 0.033 across a category boundary |
| **Pose retargeting** | Offset the predicted pose along the approach axis by the fingertip-distance difference. The field default. | **0.398** |
| **Explicit gripper conditioning** | Feed the model a representation of the gripper | **0.506** ([GraspGen-X](../../sources/graspgenx-paper.md)) |

Retargeting is not useless — it is a 3× improvement over doing nothing, from one number. Its ceiling is that it models a **z-offset only**, and therefore nothing about finger geometry or contact dynamics.

### Encoding a gripper

The interesting result is which representation wins. Learned geometric encodings of the gripper mesh all lose to a **12-number hand-designed heuristic**:

| AdaGrasp (64³ TSDF + 3D CNN) | UniGrasp (PointNet VAE latent) | PointNet++ on gripper cloud | **Swept volume (12-dim)** |
|---|---|---|---|
| 0.432 | 0.418 | 0.349 | **0.528** |

**Swept volume** = an axis-aligned cube approximating the region the fingers traverse while closing, sampled **fully open and half open** (3 cube dims + 3 centre offsets, twice). The half-open sample is what carries the *process*: revolute grippers advance their fingertips forward along +z as they close, and a fully-open snapshot cannot represent that. The reading is that grasping is conditioned on **what the gripper does**, not on **what the gripper looks like** — and shape encoders spend capacity on the wrong thing.

A related negative result: appending a **gripper-type one-hot** to the swept volume *degrades* performance. Partitioning the conditioning space blocks information sharing across gripper families, which is the mechanism a cross-embodiment model runs on.

> [!note] Two axes of "cross-embodiment," often conflated
> [Soft-prompt cross-embodiment conditioning](../learning/soft-prompt-cross-embodiment.md) handles heterogeneity in **action space, camera rig, control frequency and task distribution** across robots for a *policy*. GraspGen-X handles heterogeneity in **gripper morphology and closing kinematics** for a *grasp model*. Different problems, same conclusion twice: an explicit, early-injected conditioning vector beats both per-embodiment output heads and post-hoc retargeting.

## Training distribution: procedural beats real

Only ~20 real gripper designs are worth collecting, they cluster, and a 10/10 train-test split leaves the two sets barely overlapping in gripper space. [GraspGen-X](../../sources/graspgenx-paper.md) instead generates grippers **procedurally** (Infinigen-Sim / Blender geometry nodes), tuning the randomisation so the synthetic swept-volume distribution *covers* the real one. This beat real-gripper training **for every encoder tested**, and more procedural grippers kept helping (25 → 50).

The same shape as [RoboTwin 2.0](../../sources/robotwin2-paper.md)'s finding that clean sim data bought nothing and the entire gain came from **diversity, not fidelity** — here applied to the robot rather than to the scene.

## Coverage, not just precision

The most transferable practical lesson in [GraspGen-X](../../sources/graspgenx-paper.md)'s real-robot section: on a cluttered shelf, most predicted grasps are discarded by the planner for **collision or IK infeasibility**, so a generator that emits a few excellent grasps in one region loses to one that emits merely-good grasps spread over the object. Grasp success in clutter is limited by **spatial coverage of the candidate set** as much as by per-grasp precision — which is why the metric of record is the AUC of a precision-recall curve over 2 K generated grasps rather than top-1 accuracy.

This also predicts where the approach strains: **the lower the arm's DoF, the higher the IK-rejection rate**, so coverage becomes the binding constraint everywhere, not only in clutter. See [Can RoboTwin 2.0 generate data for a 5-DoF arm?](../../syntheses/projects/five-dof-arms-in-robotwin.md).

## Top-down grasps

An independently interesting convergence. This wiki derived from kinematics that a 5-DoF arm is fully dexterous **top-down** and constrained laterally, and filed "top-down grasps only" as a task-design rule. GraspGen-X arrived at the same constraint from user complaints — *"user feedback highlights a need for top-down grasps, particularly for benchmarks like [LIBERO](../../entities/libero.md)"* — and shipped a **Grasp Mixture-of-Experts**: union the diffusion sampler with a PCA-fitted oriented-bounding-box sampler that emits top-down and side grasps, then rank the pooled set with the discriminator. Enabled by default in the release.

A diffusion model that *can* produce top-down grasps but cannot be *made* to is a real limitation of generative samplers, and the fix is a classical sampler bolted alongside — the same "learned + analytic in parallel" pattern this wiki sees in [safety filters](safety-filters.md) and [TAMP](task-and-motion-planning.md).

## Where it sits against end-to-end policies

| | Modular 6-DOF grasping | End-to-end [VLA](../learning/vla-models.md) |
|---|---|---|
| Data | 10⁸–10⁹ sim grasps, GPU-bound | 10⁴–10⁵ teleop episodes, human-bound |
| New gripper | Retrain, or condition (this page) | Retrain / finetune, cross-embodiment head |
| New task | Free — it is object-centric | Needs demonstrations |
| Non-prehensile, deformables, in-hand | Out of scope | In scope in principle |
| Composability | A tool call in an agent stack | Usually the whole controller |

[Flexion Reflect](../../sources/flexion-reflect-v1.md) states the coupling that makes the grasp number matter: *"a policy that works 95% and a grasp that works 90%… compound into failure."* 79.0% on a novel gripper in clutter is the figure that enters that product.

## Key references

- [GraspGen-X](../../sources/graspgenx-paper.md) (Han et al., CVPR 2026) — cross-embodiment conditioning; the anchor for this page.
- GraspGen (Murali et al., 2025) — the diffusion-generator + discriminator base. **Not yet ingested.**
- ACRONYM (Eppner et al., 2020) — the simulation grasp-labelling pipeline. **Not yet ingested.**
- AnyGrasp (Fang et al., 2023) — scene-centric pixel-wise baseline; 61.4% on the UR10 shelf/table test, degrading to 42.9% in shelf clutter because it was trained on tabletops.

## Related concepts

- [Motion planning](motion-planning.md) — the consumer of the ranked grasp set.
- [Task and motion planning](task-and-motion-planning.md) — the layer that decides *whether* to grasp.
- [Soft-prompt cross-embodiment conditioning](../learning/soft-prompt-cross-embodiment.md) — the policy-side analogue.
- [VLA models](../learning/vla-models.md) — the end-to-end alternative.

## Mentioned in

- [GraspGen-X](../../sources/graspgenx-paper.md)
