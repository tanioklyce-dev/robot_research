---
title: xArm 7
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [xarm, ufactory, robot-arm, manipulator, 7-dof, cross-embodiment]
status: stub
---

**xArm 7** — UFactory's commercial 7-DOF robotic arm. In this wiki, the **secondary tabletop manipulator** (after [[franka-panda|Franka Panda]]) appearing in cross-embodiment-transfer experiments. Specifically, [[robot-utility-models|Robot Utility Models]] used xArm 7 as the **transfer target** for policies trained on [[stretch|Stretch]]: ~10pt drop in success rate vs Stretch baseline (tissue 80%→70%, bag 84%→76%) — strong evidence that BC policies trained on one embodiment can transfer with minimal loss to a different one.

## Specs (per the RUM paper context)
- **7 DOF.**
- Used with a **custom 3D-printed end-effector** mountable on standard robot arms (the same end-effector also fits Franka Panda).
- Wrist camera options tested: iPhone Pro (RUM default) or Intel RealSense D405.

> [!note] Primary-source ingest deferred
> Specs above are from the RUM paper's brief deployment description. UFactory's product page would give full payload / reach / repeatability numbers. Promote this entity beyond stub when a UFactory primary source or another paper using xArm 7 lands.

## Why it matters in this wiki
- **Cross-embodiment evidence.** RUM's Stretch → xArm 7 transfer numbers are the wiki's single empirical data point on how BC policies transfer across embodiments. Useful reference for any future cross-embodiment claim.
- **Alternative tabletop arm to Franka Panda.** Most JEPA / VLA / world-model work in this wiki defaults to Franka. xArm 7's appearance signals there's a second commercial 7-DOF option that lab teams use; could surface more if VLA work expands.

## Related
- [[robot-utility-models|Robot Utility Models]] — primary cross-embodiment use.
- [[robot-utility-models-paper|Robot Utility Models Paper]] — measured the transfer.
- [[franka-panda|Franka Panda]] — primary tabletop alternative.
- [[stretch|Stretch]] — RUM's training-platform partner.

## Mentioned in
- [[robot-utility-models-paper|Robot Utility Models Paper]]
- [[robot-utility-models-website|Robot Utility Models Project Page]]
