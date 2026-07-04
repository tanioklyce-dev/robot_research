---
title: Unitree G1
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-07-04
sources: 3
tags: [unitree-g1, humanoid, bipedal, china, affordable, accessible, groot]
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
- **[GR00T N1.7 EA](../sources/isaac-gr00t-github.md)** ships `UNITREE_G1` and `UNITREE_G1_SONIC` embodiment tags — the latter for end-to-end language-conditioned manipulation + locomotion via the GEAR-SONIC controller.

## Position vs other humanoids
- **Smaller than [H1](unitree-h1.md)** — G1 is ~1.3 m vs H1 ~1.8 m. Reduced reach, payload, walking speed.
- **Cheaper than every other humanoid in this wiki by far.** [TurtleBot](turtlebot.md) still cheaper but isn't a humanoid; among humanoids, G1 is the floor.
- **Limited dexterous manipulation** — basic grippers; not the multi-finger hands of [Atlas](atlas.md) or [Figure](figure.md).

## Related
- Unitree Robotics — manufacturer.
- [Unitree H1](unitree-h1.md) — full-size sibling.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — landscape; G1 is the educational-research bridge.

## Mentioned in
- [GR00T N1.5 research page](../sources/groot-n1_5.md) — cross-embodiment post-training (98.8% seen / 84.2% novel)
- [GR00T N1.6 research page](../sources/groot-n1_6.md) — whole-body loco-manipulation data
- [Isaac-GR00T GitHub](../sources/isaac-gr00t-github.md) — `UNITREE_G1` / `UNITREE_G1_SONIC` embodiment tags

## Open questions / TBD
- **No Unitree-authored primary source ingested** — specs still from general knowledge; the G1 product page would anchor current numbers. (Now cited by three GR00T sources.)
- Whether G1 transitions to be the de-facto "academic humanoid" the way [Stretch](stretch.md) became the de-facto "academic mobile manipulator." The GR00T line adopting it as its whole-body target is a strong signal in that direction.
