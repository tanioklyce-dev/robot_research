---
title: Unitree G1
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-07-15
sources: 11
tags: [unitree-g1, humanoid, bipedal, china, affordable, accessible, groot, whole-body-control]
---

**Unitree G1** — smaller, cheaper bipedal humanoid from Unitree Robotics. Released May 2024. **Starter price ~$16,000** — the cheapest credible serious humanoid platform. Targeted at developers and researchers.

## Specs
- ~1.32 m tall, ~35 kg (G1 EDU base configuration).
- 23 DOF (some configurations, including EDU+).
- Walking + simple manipulation demos at launch; capability evolving rapidly.

## Why it matters
- **Lowest serious-research price tier ever for a humanoid.** $16k is in the same range as a research-grade tabletop arm, not the previous $90k+ humanoid floor.
- **Educational + research bridge.** Cheap enough for individual researcher / small lab budgets; capable enough for real research papers.
- **Rapid iteration.** Unitree updates G1 firmware + capabilities frequently; the platform changes faster than typical research robots.

## As a GR00T embodiment
The G1 is the GR00T line's main **cross-embodiment / whole-body** target beyond [Fourier GR-1](fourier-gr-1.md):
- **[GR00T N1.5](../sources/groot-n1_5.md)** post-training (1K demos): seen objects 44.0% → **98.8%**, novel objects **84.2%** — the first strong non-GR-1 humanoid result in the GR00T line.
- **[GR00T N1.6](../sources/groot-n1_6.md)** adds G1 **whole-body loco-manipulation** teleop data to pretraining.
- **[GR00T N1.7 EA](../sources/isaac-gr00t-github.md)** ships `UNITREE_G1` and `UNITREE_G1_SONIC` embodiment tags — the latter for end-to-end language-conditioned manipulation + locomotion via the **[GEAR-SONIC](gear-sonic.md)** controller ([paper](../sources/sonic-paper.md)). SONIC is a **G1-only** whole-body controller (29 joints): a motion-tracking RL policy scaled to 611 h / 100M+ frames of mocap, with direct sim-to-real (99.2%) and a universal-token interface a GR00T N1.5 VLA drives for loco-manipulation. G1 is the sole robot SONIC targets — the strongest signal it's becoming GR00T's de-facto humanoid.

## Position vs other humanoids
- **Smaller than [H1](unitree-h1.md)** — G1 is ~1.3 m vs H1 ~1.8 m. Reduced reach, payload, walking speed.
- **Cheaper than every other humanoid in this wiki by far.** [TurtleBot](turtlebot.md) still cheaper but isn't a humanoid; among humanoids, G1 is the floor.
- **Limited dexterous manipulation** — basic grippers; not the multi-finger hands of [Atlas](atlas.md) or [Figure](figure.md).

The G1 is fast becoming the **de-facto benchmark platform for learned [whole-body control](../concepts/robotics/whole-body-control.md)** — it is the common target across [SONIC](../sources/sonic-paper.md) (NVIDIA GEAR), [MotionBricks](../sources/motionbricks-paper.md) (NVIDIA, SIGGRAPH 2026), and [BumbleBee](../sources/bumblebee-experts-to-generalist-wbc.md) ([BeingBeyond](beingbeyond.md)), which all evaluate WBC methods on it. (Note DoF varies by config — SONIC uses the 29-joint G1; BumbleBee a 23-joint config.)

## Related
- Unitree Robotics — manufacturer (no entity page yet).
- [Unitree H1](unitree-h1.md) — full-size sibling.
- [Unitree Go2](unitree-go2.md) — the quadruped line from the same vendor.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — the concept for which G1 is the shared benchmark robot.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — landscape; G1 is the educational-research bridge.

## Mentioned in
- [SONIC Paper](../sources/sonic-paper.md) — SONIC is a G1-only whole-body controller (primary robot)
- [MotionBricks Paper](../sources/motionbricks-paper.md) — NVIDIA real-time motion model deployed on G1 for WBC
- [BumbleBee Paper](../sources/bumblebee-experts-to-generalist-wbc.md) — expert→generalist WBC, SOTA on G1
- [GR00T-WholeBodyControl GitHub](../sources/gr00t-wholebodycontrol-github.md) — primary supported robot for the SONIC/MotionBricks/Decoupled-WBC code
- [WBC-AGILE GitHub](../sources/wbc-agile-github.md) — validated WBC engine on G1 (+ Booster T1)
- [GR00T end-to-end workflow docs](../sources/nvidia-gr00t-e2e-workflow-docs.md) — the G1 is the workflow's robot (pick-and-place, sim + Jetson-Thor real path)
- [GR00T N1.5 research page](../sources/groot-n1_5.md) — cross-embodiment post-training (98.8% seen / 84.2% novel)
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — whole-body loco-manipulation data
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — `UNITREE_G1` / `UNITREE_G1_SONIC` embodiment tags

## Open questions / TBD
- **No Unitree-authored primary source ingested** — specs still from general knowledge; the G1 product page would anchor current numbers. (Now cited by three GR00T sources.)
- Whether G1 transitions to be the de-facto "academic humanoid" the way [Stretch](stretch.md) became the de-facto "academic mobile manipulator." The GR00T line adopting it as its whole-body target is a strong signal in that direction.
