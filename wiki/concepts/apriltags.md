---
title: AprilTags
type: concept
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [vision, fiducials, localization, apriltags]
---

# AprilTags

A family of visual fiducial markers designed for robust, real-time detection and 6-DOF pose estimation from monocular cameras. Developed by Ed Olson at the University of Michigan (first published 2011). The de facto standard for robot localization in structured environments, used in both [[first-robotics-competition|FRC]] competition fields and research robotics.

## How they work

Each AprilTag is a square binary pattern (black and white cells) encoding a unique ID. A detection algorithm:
1. Finds quad-shaped regions in the image.
2. Decodes the binary payload to identify the tag ID and family.
3. Computes the tag's 6-DOF pose (position + orientation) relative to the camera using the known tag size and camera intrinsics.

Detection is robust to partial occlusion, motion blur, and varying lighting. Multiple tags can be detected simultaneously.

## Tag families

| Family | Bits | Capacity | Hamming distance | Common use |
|--------|------|----------|------------------|-----------|
| 36h11 | 36 | 587 tags | 11 | FRC fields, general robotics |
| 25h9 | 25 | 35 tags | 9 | Smaller applications |
| 16h5 | 16 | 30 tags | 5 | Legacy, low-res cameras |

**36h11** is the standard in FRC — provides high error-correction (Hamming distance 11) and large ID space ([[frc-2026-game-manual|FRC 2026 Game Manual]], §5.11).

## FRC usage (2026 REBUILT)

- **32 unique tags** (IDs 1–32) placed on HUBs (16), TOWERs (4), OUTPOSTs (4), and TRENCHEs (8) ([[frc-2026-game-manual|FRC 2026 Game Manual]], §5.11).
- Each tag: 8.125in square marker on 10.5in polycarbonate panel.
- Tags at known, published positions enable robot pose estimation for autonomous navigation and scoring.
- Teams use **PhotonVision** or **Limelight** coprocessors to detect tags and feed pose data to the [[roborio|roboRIO]] via NetworkTables.
- FRC rules prohibit robots from displaying imagery that mimics 36h11 AprilTags (R203-C).

## Research robotics usage

AprilTags are widely used in research for:
- **Robot localization** in structured environments (labs, warehouses).
- **Object pose estimation** for manipulation tasks.
- **Camera calibration** and multi-camera extrinsic estimation.
- **Ground-truth tracking** in motion-capture-free setups.

The [[stretch|Stretch]] platform uses ArUco markers (a related fiducial system) for navigation landmarks. AprilTags and ArUco markers are functionally similar but use different encoding schemes.

## Key references

- Olson, E. (2011). "AprilTag: A robust and flexible visual fiducial system." *ICRA 2011*.
- Wang, J. & Olson, E. (2016). "AprilTag 2: Efficient and robust fiducial detection." *IROS 2016*.
- Krogius, M., Haggenmiller, A., & Olson, E. (2019). "Flexible Layouts for Fiducial Tags." *IROS 2019*. (AprilTag 3)

## Related concepts
- [[sim-to-real-transfer|Sim-to-real transfer]] — simulated AprilTags used to train vision pipelines before deployment
- [[world-model|World model]] — AprilTag-based localization provides state estimates that world models could condition on

## Mentioned in
- [[frc-2026-game-manual|FRC 2026 Game Manual]] (§5.11)
