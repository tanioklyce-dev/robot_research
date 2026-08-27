---
title: CuRobo
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-23
sources: 1
tags: [curobo, motion-planning, gpu, cuda, nvidia, inverse-kinematics, collision-checking, robotwin, trajectory-optimization]
---

**CuRobo** — NVIDIA's **CUDA-accelerated robot library**: GPU-parallel inverse kinematics, collision checking, and trajectory optimization, fast enough to run motion planning inside a data-generation or control loop rather than offline. [NVlabs/curobo](https://github.com/NVlabs/curobo) — **1,769★ / 329 forks**, Apache-2.0, Python, created Oct 2023.

## Why it matters in this wiki

**It is the planner underneath [RoboTwin 2.0](robotwin.md)'s data generator**, and therefore underneath the wiki's sharpest cross-embodiment finding. Configuring a new embodiment in RoboTwin is *mostly* configuring CuRobo ([source](../sources/robotwin2-paper.md), [docs](https://robotwin-platform.github.io/doc/usage/new-embodiment.html)): a `curobo_tmp.yml` naming `base_link`, `ee_link`, `cspace/joint_names`, a `retract_config`, and hand-authored **collision spheres**.

> [!warning] CuRobo solves IK as optimization — which matters for kinematically deficient arms
> This is the detail flagged in the [5-DoF experiment plan](../syntheses/projects/five-dof-arms-in-robotwin.md). Against a full SE(3) pose target, a **5-DoF arm has no exact solution**. CuRobo will not return a clean "infeasible" — it returns a **best-effort solution with residual orientation error**. Anyone running it on such an arm must **log the residual explicitly**, or near-misses get silently counted as planning failures and the informative signal is lost.
>
> This is also the mechanism behind RoboTwin's headline DoF result: grasp-candidate augmentation works by giving the optimizer *more reachable targets to choose from*, which is worth **+22.7 pts** on a 6-DoF Piper and **−0.1** on a 7-DoF Franka that never needed the help.

## As the embodiment-agnostic half of a pick-and-place stack

[GraspGen-X](../sources/graspgenx-paper.md) uses CuRobo (with nvblox, on a Jetson) as the planner behind its real UR10 experiments, and builds its whole argument on what CuRobo *is*: **model-based, so moving it to a new robot is a one-time config file**. That is precisely the property the grasp model lacks, which is why the paper calls grasp generation *"the least transferable component in cross-embodiment settings."* The grasp generator hands CuRobo its **top-100 ranked poses**; CuRobo rejects those in collision or without an IK solution.

This inverts the usual reading of the [5-DoF warning](../syntheses/projects/five-dof-arms-in-robotwin.md) above. There, CuRobo's best-effort IK silently absorbs deficiency into residual error. Here, IK rejection is the **selection mechanism** — and GraspGen-X's clutter result (85.7% isolated → 71.4% on a shelf) is attributed not to worse grasps but to the planner rejecting most of them, making **spatial coverage** of the candidate set the binding constraint. On a 5-DoF arm the rejection rate rises everywhere, not just in clutter.

## Related

- [RoboTwin 2.0](robotwin.md) — the data generator built on it · [RoboTwin 2.0 paper](../sources/robotwin2-paper.md)
- [5-DoF arms in RoboTwin](../syntheses/projects/five-dof-arms-in-robotwin.md) — where its IK behavior becomes the experiment
- [Drake](drake.md) — the model-based alternative; optimization-first but CPU/structure-oriented rather than GPU-parallel
- [Motion planning](../concepts/robotics/motion-planning.md) · [Optimal control](../concepts/robotics/optimal-control.md) · [6-DOF grasp generation](../concepts/robotics/six-dof-grasp-generation.md)

## Open questions

- **No primary source ingested** — everything here is via RoboTwin's configuration docs. Planning rates, success rates versus sampling planners (OMPL/RRT-family), and GPU memory cost are unestablished.
- How does it behave on **redundant** arms (7-DoF) versus **deficient** ones (5-DoF)? The RoboTwin result implies the answer indirectly and nobody has measured it directly.

## Mentioned in

- [GraspGen-X: Cross-Embodiment 6-DOF Diffusion-based Grasping](../sources/graspgenx-paper.md)
- [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation (Chen et al., Jun 2025)](../sources/robotwin2-paper.md)
