---
title: "Time-Optimal Motion Planning Using Convex Sets (ARM Institute project page)"
type: source
url: https://arminstitute.org/news/motion-planning-convex-sets/
author: ARM Institute (project team, Dexai Robotics + MIT)
published: 2024-02-26
ingested: 2026-08-16
venue: ARM Institute news / project summary (2023 Technology Project Call)
format: web page
tags: [graphs-of-convex-sets, gcs, iris, motion-planning, deployment, dexai-robotics, arm-institute, manufacturing, roi]
---

# Time-Optimal Motion Planning Using Convex Sets (ARM Institute)

## Summary

A one-page project summary from the **ARM Institute** (Advanced Robotics for Manufacturing, the DoD-funded manufacturing innovation institute) describing a funded project with **[Dexai Robotics](../entities/dexai-robotics.md) as PI and MIT as partner**, selected from the 2023 Technology Project Call, that productized **[GCS](../concepts/robotics/graphs-of-convex-sets.md) trajectory optimization**. Its value to this wiki is narrow and high: it is the **independent corroboration** of the deployment claim [Tedrake makes verbally in his 2024 seminar](tedrake-gcs-foundation-models-talk.md), and it attaches a dollar figure and a deliverable list to it.

## Key claims

- **The pipeline is the paper's, unchanged**: *"The project team leveraged the latest advances in trajectory optimization using graphs of convex sets (GCS)"* — generate convex sets in **configuration space**, connect them into a GCS, optimize for a collision-free plan lying entirely within it. Described as *"an optimal, correct-by-design, motion planner."*
- **Deployed, not piloted**: *"demonstrated at ARM Member Dexai Robotics on robots assembling meals in the lab **and at multiple customer sites across the nation**."*
- **Commercially transitioned, with a number**: *"The project has already been transitioned into commercial use at Dexai Robotics, resulting in a **return exceeding $10,000/robot/year**."* Attributed to faster operation, serving more people, and reduced food waste *"by eliminating collisions and other errors."*
- **Five software modules** were delivered to ARM members through the Member Community: **`RobotModel`, `RobotConstraints`, `IrisBuilder`, `GcsPlanner`, `WarmGcsPlanner`.**

> [!note] `WarmGcsPlanner` is the interesting name on that list
> A *warm-started* GCS planner is exactly what the deployment regime demands and what the [paper](gcs-motion-planning-paper.md) does not describe: the same graph queried thousands of times a day with slightly different endpoints. It implies the productization work was about **repeated-query latency**, not about the optimality machinery — consistent with Tedrake's *"willing to precompute once… making plans all day long"* framing.

> [!warning] Read the ROI figure as a vendor-side estimate
> *">$10,000/robot/year"* is stated by the project page with no methodology, baseline, or fleet size. Direction is credible (cycle time is revenue in food assembly and GCS beat shortcut-PRM on runtime *and* path length in the paper); the magnitude is not independently checkable here.

## Entities mentioned

- [Dexai Robotics](../entities/dexai-robotics.md) — project PI; the deploying company.
- **ARM Institute** — funder and publisher; no wiki page.
- MIT — named partner (the [Tedrake](../entities/russ-tedrake.md) group, though the page does not name individuals).

## Concepts touched

- [Graphs of convex sets (GCS)](../concepts/robotics/graphs-of-convex-sets.md) — the deployment datapoint.
- [Motion planning (classical)](../concepts/robotics/motion-planning.md).

## Open questions

- **What is in the modules that is not in [Drake](../entities/drake.md)?** `IrisBuilder` and `WarmGcsPlanner` sound like the two pieces of engineering the paper leaves as exercises — region generation as a product, and warm-started repeated queries. They are behind ARM's member wall.
- **Which robot and which arm?** The page says "robots assembling meals" without naming the platform or DoF, so the deployment cannot be compared against the paper's 7-DoF iiwa benchmarks.
