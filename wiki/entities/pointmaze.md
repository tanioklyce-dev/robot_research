---
title: PointMaze
type: entity
subtype: benchmark
created: 2026-05-08
updated: 2026-05-08
sources: 3
tags: [pointmaze, navigation-benchmark, mujoco, lightweight-sim, gymnasium-robotics]
---

**PointMaze** — lightweight **2D point-mass maze navigation** benchmark. A point-mass agent navigates through a configurable maze layout to reach a goal. Originally part of the D4RL offline-RL evaluation suite; now ships in [Gymnasium-Robotics](gymnasium-robotics.md) under the Maze family (`PointMaze_*`). Variants include random-goal and procedurally-generated mazes.

## Position in this wiki
Across the JEPA literature, PointMaze is **the default 2D navigation bench** the way [PushT](pusht.md) is the default 2D manipulation bench:

- **[LeWorldModel](leworldmodel.md)** — included in the `stable-worldmodel` env zoo.
- **[DINO-WM](dino-wm.md)** — one of the six core eval environments (PushT, Wall, **PointMaze**, Rope, Granular, Reacher).
- **[JEPA-WMs](jepa-wms.md) (Terver et al.)** — included in the env list alongside Push-T, Wall, Metaworld, RoboCasa, DROID, Franka.

## Why it matters
- **Cheap discriminator** — fast simulation, simple state space, small action space. Trains in minutes; results are reproducible across seeds.
- **Task structure tests planning specifically** — unlike PushT which is contact-rich, PointMaze is navigation-specific. The two bench-types are complementary.
- **Long-horizon variants exist** — random goals and large mazes stress multi-step planning, useful for world-model evaluation.

## Related
- [Gymnasium-Robotics](gymnasium-robotics.md) — current canonical home (Maze family).
- [MuJoCo](mujoco.md) — physics backend.
- [PushT](pusht.md) — sibling lightweight bench (manipulation rather than navigation).
- [stable-worldmodel](stable-worldmodel.md) / [LeWorldModel](leworldmodel.md) / [DINO-WM](dino-wm.md) / [JEPA-WMs](jepa-wms.md) — primary JEPA-line consumers.

## Mentioned in
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [LeWorldModel — train and run howto](../syntheses/leworldmodel-howto.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)

## Open questions / TBD
- D4RL paper (origin) and Gymnasium-Robotics Maze docs not yet ingested as primary sources.
- Specific maze layouts used in JEPA-WMs vs DINO-WM may differ; not yet documented.
