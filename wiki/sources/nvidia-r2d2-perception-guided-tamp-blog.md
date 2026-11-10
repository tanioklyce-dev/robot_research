---
title: "R²D²: Perception-Guided Task & Motion Planning for Long-Horizon Manipulation"
type: source
url: https://developer.nvidia.com/blog/r2d2-perception-guided-task-amp-motion-planning-for-long-horizon-manipulation/
author: "Raffaello Bonghi, Edith Llontop (NVIDIA)"
published: 2025-11-04
format: vendor technical blog post (R²D² series)
tags: [nvidia, nvidia-research, r2d2, tamp, owl-tamp, vlm-tamp, nod-tamp, cutamp, fail2progress, long-horizon, gpu-planning]
ingested: 2026-11-10
---

# R²D²: Perception-Guided Task & Motion Planning for Long-Horizon Manipulation

## Summary

Five [task and motion planning](../concepts/robotics/task-and-motion-planning.md) projects. Three connect planners to perception or language, cuTAMP moves the continuous part of planning onto the GPU, and Fail2Progress learns from failures.

> [!note] Secondary for the research it covers
> This post summarises NVIDIA papers. Its figures weren't checked against those papers at ingest. The arXiv IDs listed are the primaries to ingest before any number here feeds a decision.

## Key claims

- **OWL-TAMP.** A VLM turns open-ended instructions into constraints that a TAMP system checks in simulation. arXiv 2410.02193.
- **VLM-TAMP.** A VLM drafts plans that simulation and motion planning refine. It beats VLM-only and TAMP-only baselines on kitchen tasks needing **30–50 actions and up to 21 objects**. arXiv 2411.08253.
- **NOD-TAMP.** Uses neural object descriptors learned from point clouds in place of explicit geometric models, so plans generalise to new objects. arXiv 2311.01530.
- **cuTAMP.** For a given plan outline, samples thousands of seeds and optimises them in parallel on the GPU, backtracking when infeasible. Packing and stacking plans take **seconds instead of minutes or hours**. arXiv 2411.11833.
- **Fail2Progress.** Uses Stein variational inference to generate synthetic data resembling observed failures, then fine-tunes the skill model. arXiv 2509.01746.

## Concepts touched

- [Task and motion planning](../concepts/robotics/task-and-motion-planning.md) — learned components inside the planner.

## Open questions

- **Against what baseline is cuTAMP's speed-up?** "Minutes or hours" is not a specific comparison.
