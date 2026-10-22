---
title: Agile ONE SN
type: entity
subtype: robot
created: 2026-10-22
updated: 2026-10-22
sources: 2
tags: [humanoid, research-humanoid, reference-platform, agile-robots, gr00t, jetson-thor, wuji-hand, dexterous-hands, halos, europe, germany]
---

# Agile ONE SN

**Agile ONE SN** is a compact **R&D humanoid** from [Agile Robots](agile-robots.md). It is NVIDIA's named **reference humanoid** for the Isaac platform and ships preconfigured with [GR00T](nvidia-groot.md) 1.7, GR00T whole-body control and the GR00T end-to-end workflow, on [Jetson Thor](jetson-thor.md). It was announced at GTC Berlin on 2026-10-21 and is due at the beginning of 2027 ([Agile release](../sources/agile-robots-agile-one-sn-launch.md), [NVIDIA release](../sources/nvidia-isaac-platform-gtc-berlin-2026.md)).

## Specifications

| Attribute | Value | Source |
|---|---|---|
| Height | 1.40 m | both |
| Weight | **43 kg** (Agile) · 40 kg (NVIDIA) | ⚠ disagree |
| Body DoF | 31 | both |
| Hands | 2× WUJI Hand 2, 5 fingers, **20 DoF each**, tactile, 1 kHz force control | name + 1 kHz from NVIDIA only |
| Total DoF | 71 | Agile |
| Joint torque | up to 140 Nm | Agile |
| Payload | 3 kg per arm | both |
| Compute | Jetson Thor (128 GB) + **Intel i3 N305** base module | i3 from Agile product page |
| Sensing | RGB-D head; wrist cameras; 3D LiDAR at the waist; RGB-D at the waist and back; IMUs | Agile product page / NVIDIA |
| Software | GR00T 1.7 VLA, GR00T WBC, URDF + USD for Isaac Sim / Lab | both |
| Safety | e-stop; Halos integration "planned" (NVIDIA) / "exploring" (Agile) | ⚠ wording differs |
| Price · battery · speed | not stated | — |

> [!warning] Contradiction
> NVIDIA's release gives **40 kg**. Agile's release and product page both give **43 kg**. The manufacturer's figure is used here. The product page's "Excluding hands" label may mean the two count the hands differently; neither source says so.

## Why it matters here

- **NVIDIA's first named third-party *reference* humanoid.** The GR00T stack has so far been shown on the [Unitree G1](unitree-g1.md) and other partner robots. Here a vendor ships GR00T 1.7 + WBC as the factory configuration. That makes it the closest thing to a turnkey "GR00T humanoid" for a research lab.
- **Size class.** At 1.40 m / 43 kg it sits beside the [Unitree G1](unitree-g1.md) (~1.32 m), not the full-size humanoids. Its 20-DoF tactile hands and 128 GB Thor are a large step up from a base G1, so it competes as a *research* platform, not on price. Its price is unannounced.
- **Lab-to-line claim.** Agile says skills and data transfer to the full-size [Agile ONE](agile-one.md) (174 cm / 69 kg, 21-DoF hands). No evidence for that is given.

## Related
- [Agile ONE](agile-one.md) — the full-size industrial sibling.
- [Agile Robots](agile-robots.md) — the manufacturer.
- [NVIDIA Halos](nvidia-halos.md) — the safety stack, planned or exploratory.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md)

## Mentioned in
- [Agile Robots launches Agile ONE SN](../sources/agile-robots-agile-one-sn-launch.md) (2026-10-21)
- [NVIDIA advances Isaac platform (GTC Berlin)](../sources/nvidia-isaac-platform-gtc-berlin-2026.md) (2026-10-21)
