---
title: DP3 (3D Diffusion Policy)
type: entity
subtype: model
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [dp3, diffusion-policy, point-cloud, 3d, robotwin, baseline, sim-artifact]
---

**DP3** (3D Diffusion Policy) — a point-cloud-conditioned [Diffusion Policy](diffusion-policy.md) variant. In this wiki it appears only as a **[RoboTwin 2.0](robotwin.md) baseline**, where it produces the single most instructive result in that benchmark's table.

## The result worth knowing

| | Easy | Hard | Drop |
|---|---:|---:|---:|
| **DP3** | **55.2** (best of all five) | **5.0** | **−50.2** |
| π0 | 46.4 | 16.3 | −30.1 |
| RDT | 34.5 | 13.7 | −20.8 |
| [ACT](act.md) | 29.7 | 1.7 | −28.0 |
| [Diffusion Policy](diffusion-policy.md) | 28.0 | 0.6 | −27.4 |

**DP3 beats every VLA on the clean setting and collapses hardest under domain randomization** — and the [RoboTwin authors say why themselves](../sources/robotwin2-paper.md): its strong few-shot showing *"partly stems from perfect point clouds and clean background segmentation in simulation."*

> [!warning] The wiki's clearest case of a simulation artifact flattering a policy class
> A 3D policy evaluated on **noiseless simulated depth** is being handed a perception problem it would not get in the real world. The 55.2 → 5.0 collapse is what happens when the randomization touches the thing the clean numbers were quietly assuming. Read any 3D-input policy's *simulation* result with this in mind — and note that the paper reporting it is the one that built the benchmark.

## Related

- [Diffusion Policy](diffusion-policy.md) — the 2D ancestor · [RDT-1B](rdt.md) — the scaled-up diffusion foundation model
- [RoboTwin 2.0](robotwin.md) · [RoboTwin 2.0 paper](../sources/robotwin2-paper.md)
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions

- **Primary paper un-ingested**; architecture, point-cloud encoder, and parameter count are all unestablished here.
- **Has DP3 ever been evaluated on real sensor depth?** That is the experiment its RoboTwin result demands and no ingested source runs.
