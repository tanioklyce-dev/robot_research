---
title: Sharpa Wave hand
type: entity
subtype: hardware
created: 2026-05-15
updated: 2026-05-15
sources: 1
tags: [dexterous-hand, end-effector, sharpa, manipulation, hardware]
---

**Sharpa Wave** — a 22-DoF anthropomorphic dexterous robot hand with joint-space control. Used as the primary post-training target for **[EgoScale](../sources/egoscale-paper.md)** on the Galaxea R1Pro humanoid; chosen specifically because its high DoF preserves the fine-grained finger articulation present in retargeted human-hand data.

## Specifications (as reported in EgoScale)
- **22 degrees of freedom** across all fingers and the wrist.
- **Joint-space control** — actions directly specify target joint angles, vs. fingertip-SE(3) or wrist-only schemes.
- Manufacturer: **Sharpa** (referenced as `[29]` in EgoScale's bibliography; full manufacturer details not transcribed in the source page).

## Why it matters in this wiki
- **Primary dexterous-manipulation target in [EgoScale](../sources/egoscale-paper.md)** — the 22-DoF action space is what makes the human-data scaling law a *dexterous* manipulation result rather than a gripper-only one. EgoScale's ablation explicitly compares 22-DoF joint-space against fingertip-SE(3) and wrist-only representations; joint-space wins.
- **Action-space link to [VLA models](../concepts/learning/vla-models.md).** Joint-angle action outputs are the natural pairing for a high-DoF hand; pairing with a coarser representation (wrist only or SE(3)) loses contact-rich performance.

## Related
- [EgoScale Paper](../sources/egoscale-paper.md) — the only wiki source citing this hand.
- [NVIDIA GR00T](nvidia-groot.md) — VLA family adjacent to EgoScale's pretraining.

## Mentioned in
- [EgoScale Paper](../sources/egoscale-paper.md)

## Open questions
- Manufacturer details (Sharpa company location, product line, price, availability).
- Comparison to other dexterous hands in the field (Shadow Hand, Allegro, LEAP Hand, Tesla Optimus hand, NVIDIA's own Cosmos-developed hands).
- Sensing: does the Sharpa Wave include tactile feedback or is it open-loop joint-position only? EgoScale's perception system uses external cameras only (head + wrist-mounted), suggesting no tactile feedback was used.
