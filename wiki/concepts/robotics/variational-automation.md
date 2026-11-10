---
title: Variational automation
type: concept
created: 2026-11-09
updated: 2026-11-10
sources: 3
tags: [variational-automation, automation, agentic-robotics, graph-as-policy, benchmark, industrial]
---

# Variational automation

## Definition

**Variational automation (VA)** is repeated robot work in which each instance varies in object geometry and pose, within a workcell, robot, sensor set and object range that are all known in advance. The term comes from the [GaP paper](../../sources/gap-graph-as-policy-paper.md).

| Class | What varies | Typical method |
|---|---|---|
| Fixed automation | Nothing meaningful | Hand-tuned motions |
| **Variational automation** | Objects and poses, within known bounds | Reusable models, calibrated sensors, modular skills |
| Generalist robotics | Tasks and environments | End-to-end learned policies |

Examples in the paper are packing varied items, fulfilling grocery orders, and making coffee in a café.

## Why the distinction matters

It changes what counts as fair information. If the object meshes and pose ranges are part of the task, a system can build its own simulator without reconstruction or domain randomization ([GaP](../../sources/gap-graph-as-policy-paper.md)). A general policy can't assume that.

It also suggests a commercial path that doesn't wait for generality. Most deployed value in logistics and service is repetitive work of this kind, and it's measured in throughput, not task breadth.

## Key references

- [GaP paper](../../sources/gap-graph-as-policy-paper.md) — names the class, offers eight benchmarks.
- [NVIDIA at CoRL 2026](../../sources/nvidia-corl-2026-robotics-simulation-blog.md) — announces VABAR, a six-task benchmark for the class.

## Related concepts

- [Code as policy](../agents/code-as-policy.md) — the method class GaP belongs to.
- [Graph-as-Policy](../../entities/graph-as-policy.md) — the system introduced with the term.
- [VLA models](../learning/vla-models.md) — the generalist alternative.

## A manufacturer's version of the same class (2026-11-10)

[NVIDIA's GB300 tester-tray work](../../sources/nvidia-r2d2-gb300-tester-tray-assembly-blog.md) is this task class under another name. The authors call it flexible automation: low volumes and rapid design cycles rule out fixtures that hold parts to submillimetre accuracy, while parts and their CAD models are known. Their solution leaned on that knowledge, using a per-part pose model trained from CAD renders. Reported success is 90–95% and above, against a 99.5% target.

## Current state

As of November 2026 the term has one paper and one announced benchmark. The authors say cycle times are still far from the industrial standard of 7 s per unit. Measured real-robot picks take about 67 s.

No result yet compares a VA system with a learned policy fine-tuned on the same varied distribution.

## Mentioned in

- [GaP paper](../../sources/gap-graph-as-policy-paper.md)
- [NVIDIA at CoRL 2026](../../sources/nvidia-corl-2026-robotics-simulation-blog.md)
- [NVIDIA — The Machines that Make the Machines (GB300)](../../sources/nvidia-r2d2-gb300-tester-tray-assembly-blog.md) — GB300 tray assembly as "flexible automation" with known CAD parts.
