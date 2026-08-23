---
title: "GraspGen-X: Cross-Embodiment 6-DOF Diffusion-based Grasping"
type: source
url: https://graspgenx.github.io/
author: Beining Han, Yu-Wei Chao, Erwin Coumans, Clemens Eppner, Balakumar Sundaralingam, Jia Deng, Stan Birchfield, Adithyavairavan Murali
published: 2026-05-31
ingested: 2026-08-23
venue: CVPR 2026
format: paper + project page
tags: [grasping, 6-dof-grasping, cross-embodiment, diffusion, nvidia, princeton, gripper-morphology, swept-volume, procedural-generation, acronym, isaac-sim, agilex-piper, unitree-g1, cvpr-2026]
---

# GraspGen-X: Cross-Embodiment 6-DOF Diffusion-based Grasping

- Project page: <https://graspgenx.github.io/>
- arXiv: [2606.00998v1](https://arxiv.org/abs/2606.00998) (submitted 31 May 2026, 27 pp.)
- Code / model / dataset: <https://github.com/NVlabs/GraspGenX> (release promised)
- Video: <https://youtu.be/a2sv9EVQJXE>
- Affiliations: [NVIDIA](../entities/nvidia.md), Princeton University

## Summary

[GraspGen-X](../entities/graspgen.md) makes a **6-DOF grasp generator that transfers to a gripper it has never seen** — not just to novel objects. Its framing is the sharpest part: in a modular generalized-pick-and-place stack, *every other component already transfers*. Stereo depth, SAM2 segmentation, [cuRobo](../entities/curobo.md) motion planning and nvblox occupancy mapping are either model-based or foundation-model-based, so moving to a new arm is "a one-time effort to specify the robot's configuration." Grasp generation is not: change the gripper and you retrain, which for the predecessor GraspGen cost **a week of an 8-GPU node per embodiment**. The paper's words: grasp generation is *"the least transferable component in cross-embodiment settings."*

The fix is a deliberately cheap conditioning vector. Encode the gripper as its **swept volume** — an axis-aligned cube approximating the space the fingers pass through while closing — measured **fully open and half open**, giving a 12-number description of the gripper that conditions both the diffusion generator and the discriminator. Train it not on the handful of real grippers that exist but on **procedurally generated ones**. Zero-shot mAUC across 10 novel real grippers goes 0.126 (direct transfer) → 0.398 (the standard pose-retargeting heuristic) → **0.506**, and on a real UR10 with a Robotiq-2F140 the model reaches **79.0%** grasp success against 65.2% for retargeted GraspGen and 61.4% for AnyGrasp.

## Key claims

### The problem framing (§1)

- 6-DOF grasping is *"a crucial tool-calling subroutine in recent agentic robotics systems… for prehensile manipulation"* — this is a component paper for modular stacks, not an end-to-end policy.
- Retargeting — offsetting a Franka-trained grasp pose along the approach axis by the fingertip-distance difference — is the field's default cross-gripper move ([Murali 2020, Huang 2024]). The paper's quantitative case is that it *works* (200%+ over direct transfer) but *caps out*, because it models only a z-offset and ignores finger geometry and contact dynamics.

### Swept-volume gripper encoding (§3.1)

- Swept volume ≈ the region traversed by the fingers during closing, approximated as an **axis-aligned cube**: 3 cube dimensions + 3 translation components of the cube centre relative to the gripper base frame = 6 dims per pose.
- Taken at **fully open and half open** → a **12-dim vector**, encoded by a 3-layer MLP to a 512-dim embedding fed to generator *and* discriminator.
- The half-open sample is load-bearing, and the paper says exactly why: revolute 2-finger grippers (Robotiq-2F140, OnRobot RG2, XArm Hand) **advance their fingertips along +z while closing**, information a fully-open snapshot cannot contain. Fully-open-only (6-dim) loses specifically on that category.
- Covers three families: 2-finger parallel (Franka Panda Hand), 2-finger revolute (Robotiq-2F85), and high-DOF 3-finger ([Unitree G1](../entities/unitree-g1.md) 7-DOF hand).

### Procedural grippers (§3.2)

- 20 real grippers collected in total, split **10 train / 10 test**.
- Training instead uses **25 procedurally generated grippers** (10 parallel, 10 revolute 2-finger, 5 high-DOF 3-finger), built with **Infinigen-Sim** (Blender geometry nodes for articulated objects). Fine CAD detail (screws, connectors) is skipped; the generator optimises for diversity of overall morphology and of **finger geometry**, the part that touches the object.
- Randomisation ranges are tuned so that the procedural set's swept-volume distribution **covers** the real test grippers'. The stated failure of real-gripper training is distributional: the 10 real training grippers occupy regions non-overlapping with the 10 real test grippers and are sparse in gripper space.

### Dataset and cost (§4, App. F.1)

| | Procedural grippers | Objects | Total grasps |
|---|---|---|---|
| **CVPR model** (all results below) | 25 | 3.5 K train / 453 test | **350 M** |
| **Latest released checkpoint** | 32 | 8.5 K | **2 B** |

- Labelling pipeline: **ACRONYM** antipodal sampling + **Isaac Sim** physics evaluation; max 2 K grasps per (gripper, object).
- Generator data: 175 M grasps, **8.7 K GPU-hours**. Discriminator on-generator data: **5.2 K GPU-hours**.
- Generator training: 8× A100, 780 K steps, lr 1e-5, 80 h. Discriminator: 8× A100, 300 K steps, 76 h.
- Claimed as *"the largest multi-embodiment dataset that has ever been used to train the grasping model."*

> [!warning] Contradiction — the "2 Billion grasps" in the abstract is not the model that was evaluated
> The abstract (both on arXiv and the project page) says GraspGen-X is *"trained with… a large-scale dataset of 2 Billion grasps."* Appendix F.1 states plainly that **2 B is the post-CVPR checkpoint** (32 grippers, 8.5 K objects) and that the **CVPR model behind every number in the paper used 350 M** (25 grippers, 3.5 K objects). The project page's own body text agrees with the appendix ("trained on 350M sampled grasps") while its **abstract** carries a third figure, **395 Million** — reconciled with neither. Cite **350 M** for the reported results; cite 2 B only for the checkpoint you download. This is the the **scope-loss failure mode** occurring inside the authors' own abstract rather than in a secondary.

### Zero-shot results (§5.1, Table 1)

mAUC of the precision-recall curve, averaged over novel test objects, **10 novel real grippers**:

| Method | Parallel 2F (4) | Revolute 2F (4) | High-DOF 3F (2) | All (10) |
|---|---|---|---|---|
| GraspGen-DTR (Franka model, direct transfer) | 0.215 | **0.033** | 0.136 | 0.126 |
| GraspGen-RTG (Franka model + pose retargeting) | 0.365 | 0.379 | 0.503 | 0.398 |
| **GraspGen-X** | **0.502** | **0.413** | **0.699** | **0.506** |

- Direct transfer **collapses across category boundaries** — 0.033 on revolute 2-finger grippers is effectively zero.
- GraspGen-X beats retargeting by 25% overall and ~40% on 3-finger hands, i.e. the advantage grows with morphological distance from the Franka training gripper.
- **Out of distribution, unseen during training: two 5-finger hands** still score 0.404 (Surge Hand) and 0.363 (Inspire Hand) — above retargeting's all-gripper average.

> [!note] Two grippers where retargeting still wins (Table A2)
> Per-gripper numbers are less tidy than the category averages. **OnRobot RG2**: RTG 0.241 vs GraspGen-X **0.136**. **XArm Hand**: RTG 0.551 vs GraspGen-X **0.525**. The authors flag the RG2 case themselves and hypothesise its morphology is under-covered by the procedural distribution. The swept-volume abstraction is not uniformly dominant — it is dominant on average.

### Encoder ablation (§5.3, Table 2)

Same 10 novel test grippers, 453 objects, model trained on 32 procedural grippers:

| AdaGrasp (TSDF + 3D CNN) | UniGrasp (PointNet VAE latent) | PointNet++ (gripper mesh cloud) | **GraspGen-X (swept volume)** |
|---|---|---|---|
| 0.432 | 0.418 | 0.349 | **0.528** |

The **12 hand-picked numbers beat every learned geometric encoding of the gripper mesh**, including a 64³ TSDF. The claim is that swept volume encodes the *grasping process* rather than the *shape*.

### Other ablations (§5.4)

- **Procedural > real for every encoder tested**, not just theirs — the gain is in the training distribution, not the architecture. (Compare [RoboTwin 2.0](robotwin2-paper.md), where clean sim data helped nothing and the entire gain came from diversity.)
- **More procedural grippers helps** (25 → 50) for swept volume, TSDF and PointNet++ alike. Only 25 were used in the main model, for compute reasons.
- **Adding a gripper-type one-hot on top of swept volume *hurts*.** Hypothesis: partitioning the parameterisation space blocks information sharing between gripper families, which is the whole point of a cross-embodiment model.
- Gripper-type-only and retarget-offset-only conditioning fail outright.

### Real robot (§6)

**Industrial — UR10 + Robotiq-2F140** (a novel gripper for every method). Perception: one calibrated RealSense D435, SAM2 segmentation on a 6000 Ada, FoundationStereo depth. Planning: [cuRobo](../entities/curobo.md) + nvblox on a [Jetson](../entities/jetson-thor.md), top-100 ranked grasps handed to the planner, which rejects those in collision or without IK. 12 isolated objects × 5 poses; 5 objects × 3 poses on a cluttered shelf.

| Method | Isolated | Clutter | Overall |
|---|---|---|---|
| **GraspGen-X** | **85.7%** | **71.4%** | **79.0%** |
| GraspGen-RTG | 73.3% | 57.1% | 65.2% |
| AnyGrasp | 80.0% | 42.9% | 61.4% |

- Clutter costs GraspGen-X 14 points, and the diagnosis is about **coverage, not accuracy**: in clutter most grasps are rejected for kinematic infeasibility or collision, so the generator must produce grasps with high *spatial spread* to leave the planner anything feasible.
- AnyGrasp needed two undocumented post-processing steps to produce consistent predictions at all (camera z-offset to match its training depth; NMS disabled), and halves in clutter because it is **scene-centric, trained on tabletop** — a shelf is out of distribution. GraspGen-X and GraspGen are **object-centric**, so SAM2 carries them onto the shelf.

**Low-cost — [AgileX Piper](../entities/agilex-piper.md) + stock parallel gripper**, ZED2 on the end-effector. **100% success over 10 trials** on a YCB mustard bottle and an ArUco cube.

**Humanoid — [Unitree G1](../entities/unitree-g1.md) 3-finger 7-DOF hand**, chest stereo. **100% over 5 trials** on the mustard bottle in random stable poses.

> [!warning] The two 100% results are a much weaker test than the 79%
> Both the Piper and G1 experiments **assume access to the object model**: FoundationPose estimates a 6D pose and the model is fed the **complete** point cloud of a known mesh, then the arm executes a linearly interpolated IK trajectory — no motion planner, no clutter, 2 objects and 1 object respectively. The UR10 result is the one run on partial point clouds of unknown objects with a real planner. Read 79.0% as the headline number and the 100%s as embodiment-transfer sanity checks.

### Post-CVPR: Grasp Mixture-of-Experts (App. F.2)

- *"User feedback highlights a need for top-down grasps, particularly for benchmarks like [LIBERO](../entities/libero.md) where objects rest in upright stable poses. Although our diffusion model generates top-down grasps, it does not strictly enforce them."*
- The shipped fix is a **mixture of experts**: union the diffusion sampler's grasps with an **oriented-bounding-box sampler** (PCA on the object cloud, +z assumed gravity-aligned, samples top-down *and* side grasps), then let the **discriminator rank the pooled set**. OBB handles cuboids; diffusion handles non-convex shapes and awkward poses. **Enabled by default in the repo.**

### Acknowledged limits

- Swept volume discards **contact friction and kinematics**, and cannot express the **asymmetric thumb** of a 3-finger hand (+x thumb vs two −x fingers) — likely to matter for small objects.
- 3-finger grasps are generated by the same antipodal sampler as 2-finger ones, giving *"more limited variation than the more general dexterous hand grasping problem"* — flagged as future work.
- Non-graspable objects are handled by the discriminator scoring everything low, not by abstention (App. E).

## Entities mentioned

- [NVIDIA](../entities/nvidia.md) · [GraspGen / GraspGen-X](../entities/graspgen.md) · [Adithyavairavan Murali](../entities/adithyavairavan-murali.md)
- [cuRobo](../entities/curobo.md) · [NVIDIA Isaac Sim](../entities/nvidia-isaac-sim.md)
- [AgileX Piper](../entities/agilex-piper.md) · [Unitree G1](../entities/unitree-g1.md) · [Franka Panda](../entities/franka-panda.md) · [Galaxea](../entities/galaxea-r1.md)
- [LIBERO](../entities/libero.md)

## Concepts touched

- [6-DOF grasp generation](../concepts/robotics/six-dof-grasp-generation.md) — new page; this source is its anchor.
- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) — the same architectural argument on a different axis of heterogeneity.
- [Motion planning](../concepts/robotics/motion-planning.md) — the consumer of the grasp set, and the reason coverage matters as much as precision.

## Open questions

- **Does swept volume survive a 5-DoF arm?** The wiki's [5-DoF analysis](../syntheses/projects/five-dof-arms-in-robotwin.md) argues those arms are dexterous top-down and constrained laterally. GraspGen-X conditions on the *gripper*, and is entirely agnostic to the *arm* — feasibility is delegated to the planner's IK rejection. On a 5-DoF arm the rejection rate should be much higher, and the coverage problem the paper identifies in clutter becomes the dominant problem everywhere. Untested.
- The **OBB mixture-of-experts is a post-hoc patch for exactly the constraint the 5-DoF analysis predicted**, arrived at from the opposite direction (LIBERO benchmark users, not arm kinematics). Nobody has evaluated whether it is enough.
- **What is a swept-volume cube for a suction cup, an underactuated soft gripper, or the [SO-101](../entities/so-arm101.md)'s printed jaw?** The representation assumes fingers that close through a volume. Two of those three do not.
- Table A2's **OnRobot RG2 regression** is unexplained beyond a hypothesis. Is there a diagnosable morphology class where the cube abstraction is actively misleading?
- The **2 B-grasp checkpoint's numbers are unpublished.** Only its dataset size is reported.
