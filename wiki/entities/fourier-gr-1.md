---
title: Fourier GR-1
type: entity
subtype: humanoid
created: 2026-05-15
updated: 2026-07-04
sources: 6
tags: [humanoid, fourier-intelligence, robot-platform, gr-1, dexterous-manipulation]
---

**Fourier GR-1** — humanoid robot from Fourier Intelligence (Shanghai). NVIDIA GEAR's standard humanoid evaluation platform: the **primary real-robot platform for [GR00T N1](../sources/groot-n1-paper.md)** (88.4 h in-house teleop pretraining set; all real-world post-training evals) and the **primary out-of-distribution evaluation target** in [DreamDojo](../sources/dreamdojo-paper.md) (all four eval benchmarks constructed on GR-1).

## Why it matters in this wiki
- **GR00T N1** ([paper](../sources/groot-n1-paper.md)): GR-1 with dexterous hands is the embodiment behind the headline 76.8%-vs-46.4% real-robot result, the 88.4 h teleop corpus (VIVE Ultimate Tracker + Xsens Metagloves, 20 Hz), the DexMimicGen sim pretraining embodiment (mink whole-body IK), and the WAN2.1-generated neural trajectories.
- **DreamDojo**: headline OOD-generalization results (Table 3 PSNR, Table 4 human-preference wins for DreamDojo-14B) are all reported on GR-1. Also one of four embodiments in latent-action-model training (alongside Unitree G1, AgiBot, YAM).

## Related
- [GR00T N1 Paper](../sources/groot-n1-paper.md) — primary VLA trained/evaluated on this platform.
- [DreamDojo Paper](../sources/dreamdojo-paper.md) — world-model eval use case.
- [NVIDIA GEAR](nvidia-gear.md) — uses GR-1 as its de-facto humanoid testbed across both lines.

## Mentioned in
- [GR00T N1 Paper](../sources/groot-n1-paper.md)
- [DreamDojo Paper](../sources/dreamdojo-paper.md)

## Open questions
- DoF count, payload, height, weight, price.
- Hand DoF (likely a separate dexterous hand mounted on the GR-1 arm).
- Software stack — does it have a vendor SDK, ROS interface, or both?
- Position vs Unitree G1 in the Chinese humanoid market.
- Whether the GR-1 used in DreamDojo is a custom NVIDIA-modified variant or stock Fourier.
