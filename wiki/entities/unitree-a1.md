---
title: Unitree A1
type: entity
subtype: robot
created: 2026-08-29
updated: 2026-08-29
sources: 2
tags: [unitree-a1, quadruped, legged-robot, locomotion, rma, locoformer, research-platform]
---

**Unitree A1** — a low-cost 12 kg quadruped from [Unitree](unitree-g1.md), and **the workhorse platform of learned quadruped locomotion research**. It is the robot [RMA](../sources/rma-paper.md) was deployed on in 2021 and one of the ten robots [LocoFormer](../sources/locoformer-paper.md) controls zero-shot in 2025 — which makes it a rare fixed point across four years of this wiki's locomotion coverage.

## What the ingested sources establish

- **Mass 12 kg**, with a manufacturer-advertised payload of **5 kg** ([RMA](../sources/rma-paper.md)). RMA carried **12 kg — 100% of body weight** — while the stock controller began sagging at 8 kg.
- **Ships with a factory controller** using force-based control with MPC. [RMA](../sources/rma-paper.md) benchmarks against it directly and beats it: the stock controller **fails outright on uneven foam** and on large step-ups/step-downs, destabilized by unstable footholds.
- **Joint-position interface with an onboard PD controller** — learned policies emit target joint angles which the PD loop converts to torques ([RMA](../sources/rma-paper.md)).
- **Limited onboard compute.** This is the constraint that shaped RMA's architecture: its adaptation module runs at **10 Hz** against the base policy's **100 Hz**, asynchronously with no shared clock, explicitly because of *"low-cost robots like A1 with limited on-board compute."*
- **Zero-shot controllable by a generalist.** [LocoFormer](../sources/locoformer-paper.md) scores **0.92** on A1 with no A1 data at all, against **0.97** for a per-robot expert.

## Why it matters in this wiki

**The A1 is where "cheap hardware buys ecosystem position" shows up in research rather than in sales.** The [industry map](../syntheses/society/robot-ai-industry-map.md) argues Unitree's commodity-hardware posture converts price into ecosystem standing; the A1 is the earlier, quieter instance — inexpensive enough for academic labs to risk on rocky terrain and oily plastic, and consequently the default quadruped that a generation of locomotion papers report on. The same dynamic later played out with the [Go2](unitree-go2.md) in Anthropic's robotics evaluations.

It is also a useful **compute-budget marker**. RMA's asynchronous two-rate design exists because of what an A1 can run onboard; [LocoFormer](../sources/locoformer-paper.md)'s authors name resource intensity as their first limitation. The platform did not change much between the two papers — the assumption about available compute did.

## Related

- [Unitree G1](unitree-g1.md), [Unitree H1](unitree-h1.md), [Unitree Go2](unitree-go2.md) — the rest of the line in this wiki; **G1, H1 and Go2-W are also in LocoFormer's zero-shot test set**.
- [RMA](../sources/rma-paper.md) — the adaptation work built on it.
- [LocoFormer](../sources/locoformer-paper.md) — the generalist that controls it without training on it.

## Mentioned in

- [RMA: Rapid Motor Adaptation for Legged Robots](../sources/rma-paper.md) — the deployment platform; payload, controller baseline and compute constraints all documented there.
- [LocoFormer: Generalist Locomotion via Long-context Adaptation](../sources/locoformer-paper.md) — evaluated zero-shot at 0.92.

## Open questions / TBD

- **No vendor datasheet ingested.** Everything above comes from two research papers that happened to use the robot; DoF, actuator specs, battery, and pricing are not established here from a primary.
- **Discontinued?** The A1 predates the Go1/Go2 line and its current commercial status is not recorded in any source here.
