---
title: xArm 7
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-08-13
sources: 6
tags: [xarm, ufactory, robot-arm, manipulator, 7-dof, cross-embodiment]
status: stub
---

**xArm 7** — UFactory's commercial 7-DOF robotic arm. In this wiki, the **secondary tabletop manipulator** (after [Franka Panda](franka-panda.md)) appearing in cross-embodiment-transfer experiments. Specifically, [Robot Utility Models](robot-utility-models.md) used xArm 7 as the **transfer target** for policies trained on [Stretch](stretch.md): ~10pt drop in success rate vs Stretch baseline (tissue 80%→70%, bag 84%→76%) — strong evidence that BC policies trained on one embodiment can transfer with minimal loss to a different one.

## Specs (per the RUM paper context)
- **7 DOF.**
- Used with a **custom 3D-printed end-effector** mountable on standard robot arms (the same end-effector also fits Franka Panda).
- Wrist camera options tested: iPhone Pro (RUM default) or Intel RealSense D405.

> [!note] Primary-source ingest deferred
> Specs above are from the RUM paper's brief deployment description. UFactory's product page would give full payload / reach / repeatability numbers. Promote this entity beyond stub when a UFactory primary source or another paper using xArm 7 lands.

## Why it matters in this wiki
- **Cross-embodiment evidence.** RUM's Stretch → xArm 7 transfer numbers are the wiki's single empirical data point on how BC policies transfer across embodiments. Useful reference for any future cross-embodiment claim.
- **Alternative tabletop arm to Franka Panda.** Most JEPA / VLA / world-model work in this wiki defaults to Franka. xArm 7's appearance signals there's a second commercial 7-DOF option that lab teams use; could surface more if VLA work expands.

## In DimOS

🟨 **beta** in [DimOS](dimos.md) ([repo](../sources/dimos-github.md)), and the platform its manipulation and imitation-learning paths are built around: **[Drake](drake.md)**-based trajectory planning (`xarm7-planner-coordinator`, `dual-xarm6-planner-coordinator`), Quest VR teleop (`teleop-quest-xarm7`), keyboard teleop against a mock arm, perception-plus-agent blueprints in sim and on real hardware, and **`learning-collect-quest-xarm7`** — the Quest-teleop episode collector whose output `dimos dataprep` converts into a **[LeRobot](lerobot.md) v3.0 dataset**. The xArm is where DimOS's agentic stack and the wiki's imitation-learning coverage actually touch.

## Related
- [Robot Utility Models](robot-utility-models.md) — primary cross-embodiment use.
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md) — measured the transfer.
- [Franka Panda](franka-panda.md) — primary tabletop alternative.
- [Stretch](stretch.md) — RUM's training-platform partner.

## Mentioned in
- [Robot Utility Models Paper](../sources/robot-utility-models-paper.md)
- [Robot Utility Models Project Page](../sources/robot-utility-models-website.md)
