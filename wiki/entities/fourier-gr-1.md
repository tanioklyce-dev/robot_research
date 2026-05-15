---
title: Fourier GR-1
type: entity
subtype: humanoid
created: 2026-05-15
updated: 2026-05-15
sources: 1
tags: [humanoid, fourier-intelligence, robot-platform, gr-1, dexterous-manipulation]
---

**Fourier GR-1** — humanoid robot from Fourier Intelligence (Shanghai). Used as the **primary out-of-distribution evaluation target** in [DreamDojo](../sources/dreamdojo-paper.md): all four eval benchmarks (In-lab Eval, EgoDex Eval, DreamDojo-HV Eval, Counterfactual Eval) are constructed using GR-1, with the robot replicating objects and actions observed in the human-video pretraining sets.

## Why it matters in this wiki
DreamDojo's headline OOD-generalization results (Table 3 PSNR improvements, Table 4 human-preference wins for DreamDojo-14B) are all reported on GR-1. The robot is the *measurement device* by which DreamDojo's pretraining gains are validated. Per the DreamDojo source page, GR-1 is also one of four robot embodiments used in latent-action-model training (alongside Unitree G1, AgiBot, YAM).

## Related
- [DreamDojo Paper](../sources/dreamdojo-paper.md) — primary use case.
- [NVIDIA GEAR](nvidia-gear.md) — built around this platform for the DreamDojo evals.

## Mentioned in
- [DreamDojo Paper](../sources/dreamdojo-paper.md)

## Open questions
- DoF count, payload, height, weight, price.
- Hand DoF (likely a separate dexterous hand mounted on the GR-1 arm).
- Software stack — does it have a vendor SDK, ROS interface, or both?
- Position vs Unitree G1 in the Chinese humanoid market.
- Whether the GR-1 used in DreamDojo is a custom NVIDIA-modified variant or stock Fourier.
