---
title: GTSAM
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [gtsam, factor-graphs, slam, pose-graph-optimization, smoothing-and-mapping, borglab, georgia-tech, dimos]
---

**GTSAM** (Georgia Tech Smoothing and Mapping) — a C++ library implementing **smoothing and mapping using factor graphs and Bayes networks** as the computing paradigm *"rather than sparse matrices."* From Frank Dellaert's lab (borglab). [borglab/gtsam](https://github.com/borglab/gtsam) — **3,631★ / 977 forks**, created 2017, pushed daily.

## Why it matters in this wiki

It is the **optimization back-end under the wiki's navigation coverage**, and it appears in the two places that matter for the current project work:

- **[DimOS](dimos.md)** ships a `mapping` extra explicitly described as *"GTSAM-backed pose graph optimization (relocalization, cmu_nav PGO)"* — the offline step in its **premap + relocalization** workflow, where you record once, optimize the pose graph offline, then localize against the exported premap at runtime.
- **[RTAB-Map](rtab-map.md)**-class graph SLAM uses the same factor-graph machinery for loop-closure-constrained map optimization.

> [!note] The factor-graph framing is the point
> Posing SLAM as a factor graph — variables are poses/landmarks, factors are measurements — makes **loop closure a constraint you add and re-optimize**, rather than a correction you splice in. That is why "record a map, run pose-graph optimization offline, then relocalize" is a clean workflow and "map continuously forever" is not: the offline step is where you can afford to re-solve the whole graph.
>
> Relevant to the [XLeRobot bring-up plan](../syntheses/projects/xlerobot-nav-manip-teleop-bringup.md), which takes exactly this route via RTAB-Map's localization-only mode.

## Related

- [RTAB-Map](rtab-map.md) — RGB-D SLAM front-end whose back-end this class of library serves
- [DimOS](dimos.md) — ships GTSAM-backed PGO for relocalization · [DimOS repo](../sources/dimos-github.md)
- [Nav2](nav2.md) · [ROS 2](ros2.md)

## Open questions

- **No primary source ingested.** Everything is via DimOS's dependency documentation and the repo description.
- DimOS depends on **`gtsam-extended`** (a fork by contributor `jeff-hykin`) rather than upstream — what it adds is unrecorded.
- The wiki has **no page for Frank Dellaert** or the factor-graph SLAM lineage generally, which is a larger uncovered area than this one library.
