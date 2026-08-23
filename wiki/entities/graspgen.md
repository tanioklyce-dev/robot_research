---
title: GraspGen / GraspGen-X
type: entity
subtype: model
created: 2026-08-23
updated: 2026-08-23
sources: 1
tags: [nvidia, grasping, 6-dof-grasping, diffusion, cross-embodiment, swept-volume, open-source, cvpr-2026]
---

**GraspGen** — [NVIDIA](nvidia.md)'s 6-DOF grasp-generation framework: an **SE(3) diffusion model** that samples candidate grasp poses conditioned on an object point cloud, paired with a **discriminator** that ranks them, trained on the discriminator's own on-generator positives and negatives in a flywheel. **GraspGen-X** is its cross-embodiment successor, which additionally conditions on a representation of *the gripper*, so one model serves grippers it has never seen.

| | GraspGen (2025) | **GraspGen-X** (CVPR 2026) |
|---|---|---|
| Conditioning | Object embedding | Object embedding **+ 12-dim swept volume** |
| Grippers | One per trained model | 25 procedural (CVPR) / 32 (latest) |
| Cost to add a gripper | **~1 week on an 8-GPU node** | Zero-shot, or a 4-hour finetune on 4× A100 |
| Ingested here | ✗ (cited only) | ✓ [paper](../sources/graspgenx-paper.md) |

## GraspGen-X

Han, Chao, Coumans, Eppner, Sundaralingam, Deng, Birchfield, [Murali](adithyavairavan-murali.md) — NVIDIA + Princeton, CVPR 2026 ([paper](../sources/graspgenx-paper.md), [arXiv 2606.00998](https://arxiv.org/abs/2606.00998), [NVlabs/GraspGenX](https://github.com/NVlabs/GraspGenX)).

**The idea in one line:** describe a gripper by the **cube of space its fingers sweep through while closing** — measured fully open and half open, 12 numbers total — and a diffusion grasp model generalises to novel gripper morphologies.

**Headline numbers** ([source page](../sources/graspgenx-paper.md) has the full tables):

- Zero-shot on 10 novel real grippers: **0.506 mAUC** vs 0.398 for pose retargeting and 0.126 for direct transfer.
- Real UR10 + Robotiq-2F140, unknown objects, partial point clouds, [cuRobo](curobo.md) planning: **79.0%** overall (85.7% isolated / 71.4% shelf clutter) vs 65.2% retargeted GraspGen and 61.4% AnyGrasp.
- Unseen 5-finger hands (never trained on 5-finger anything): 0.404 Surge, 0.363 Inspire.
- [AgileX Piper](agilex-piper.md) 100% / 10 trials and [Unitree G1](unitree-g1.md) 3-finger hand 100% / 5 trials — **but with known object meshes and complete point clouds**, so a far weaker test than the 79%.

**What it gets wrong or leaves open:** loses to plain retargeting on OnRobot RG2 (0.136 vs 0.241) and XArm Hand (0.525 vs 0.551); swept volume cannot express contact friction, gripper kinematics, or a 3-finger hand's asymmetric thumb; 3-finger grasps still come from a 2-finger antipodal sampler.

## Training data

| Checkpoint | Procedural grippers | Objects | Grasps |
|---|---|---|---|
| CVPR (all published results) | 25 | 3.5 K | **350 M** |
| Latest release | 32, in **6 kinematic families** (README) | 8 K+ | **2 B** |

Generated with the ACRONYM antipodal-sampling pipeline, labelled by physics rollout in [Isaac Sim](nvidia-isaac-sim.md). ~14 K GPU-hours of data generation for the CVPR model alone.

> [!warning] The abstract's "2 Billion grasps" is the released checkpoint, not the evaluated one
> Every number in the paper comes from the **350 M** CVPR model. The project page carries a third figure (395 M) in its abstract. See the [source page](../sources/graspgenx-paper.md) for the reconciliation.

## Grasp Mixture-of-Experts (post-CVPR, default in the repo)

Diffusion samplers generate top-down grasps but cannot be *forced* to. The shipped fix unions the diffusion sampler with a **PCA oriented-bounding-box sampler** (top-down and side grasps, +z assumed gravity-aligned) and lets the discriminator rank the pooled set. Motivated by users wanting enforced top-down grasps for [LIBERO](libero.md) — the same constraint this wiki derived kinematically for 5-DoF arms in the [RoboTwin 5-DoF analysis](../syntheses/projects/five-dof-arms-in-robotwin.md).

## Onboarding a new gripper — what it actually takes

The repo is live ([NVlabs/GraspGenX](https://github.com/NVlabs/GraspGenX), Apache-2.0 code, ~190 stars, last push 2026-07-14), checkpoints are on [HuggingFace](https://huggingface.co/adithyamurali/GraspGenXModel), and curated configs for ~10 popular grippers ship as a separate dataset (`adithyamurali/gripper_descriptions`: `franka_panda`, `franka_umi`, `robotiq_2f_85`, `robotiq_2f_140`, `unitree_g1`, `inspire_hand`, `surge_hand`, `barrett_hand`, `galaxea_g1`, `ezgripper`). **The swept volume is not computed from the URDF — it is auto-guessed and then hand-annotated in a GUI.**

`scripts/gripper_config_wizard.py` is a first-party Viser web wizard, six steps: align the base frame → confirm the open pose → drag a box around the inner volume at open → set the closed pose and drag a second box at half-open → review the animation → pick type and symmetry, save. Output is `assets/x_grippers/<name>/config.json`:

```json
"sweep_volume": { "extents": [x,y,z], "offset": [x,y,z],      // fully open
                  "extents2": [x,y,z], "offset2": [x,y,z] }   // half open
```
plus `open`/`close` joint states, `fingertip`, `standoff` (derived as `extents[2]/2`), `bbox`, `base_rotation` (4×4), `links`, `type` ∈ {`parallel_2f`, `revolute_2f`, `revolute_3f`}, and `symmetric`.

Two conventions and two defaults worth knowing before you start:

- **Frame convention is fixed and explicit** (Step 1): **+Z is the approach direction, +X is the closing direction.** Stored as `base_rotation` and applied to everything downstream.
- **The auto-guess is the *inner gap*, not the finger sweep.** `estimate_inner_sweep_volume()` picks the axis of maximum spread between *moving* finger centroids as the closing axis, sets the extent along it to the gap between the innermost finger surfaces, and takes the union of finger bboxes on the other two axes. For a parallel gripper this is exactly the graspable pocket — visible in the shipped configs, where `extents2[0]` is precisely half of `extents[0]` and the other two are unchanged.
- **`type` is inferred from actuated-joint count, not kinematics** — ≤2 → `parallel_2f`, ≤4 → `revolute_2f`, else `revolute_3f`. Wrong for any single-actuator revolute jaw; override in Step 6.
- **`symmetric` is hardcoded `True` in the save step** (checkbox in Step 6). It is consumed in `metrics.py` and the dataset loader, **not** in the inference path — so it changes evaluation and training, not what grasps come out of a zero-shot run.

## Why it matters here

GraspGen-X is the wiki's first entry on **grasping as a transferable module** rather than as something a policy learns implicitly. Its framing — grasp generation is "the least transferable component" of an otherwise embodiment-agnostic pick-and-place stack — is the cleanest statement anywhere in this wiki of what a modular manipulation stack still owes you. And its licence posture (model, code and dataset promised on NVlabs) puts it in reach of the low-cost arms this wiki tracks: it already runs on an [AgileX Piper](agilex-piper.md), and the arm it conditions on is *no arm at all* — only the gripper.

## Related

- [6-DOF grasp generation](../concepts/robotics/six-dof-grasp-generation.md) — the concept page.
- [cuRobo](curobo.md) · [Isaac Sim](nvidia-isaac-sim.md) · [NVIDIA](nvidia.md)
- [Soft-prompt cross-embodiment conditioning](../concepts/learning/soft-prompt-cross-embodiment.md) — the policy-side analogue.

## Mentioned in

- [GraspGen-X: Cross-Embodiment 6-DOF Diffusion-based Grasping](../sources/graspgenx-paper.md)
