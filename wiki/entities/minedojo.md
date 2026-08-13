---
title: MineDojo
type: entity
subtype: benchmark
created: 2026-08-03
updated: 2026-08-03
sources: 1
tags: [minedojo, minecraft, open-ended, benchmark, nvidia-gear]
---

**MineDojo** — an open-ended Minecraft agent benchmark and simulation framework from [NVIDIA GEAR](nvidia-gear.md) (NeurIPS 2022, outstanding paper). It is the substrate [Voyager](voyager.md) runs on, paired with the Mineflayer JavaScript API for motor control.

## Why it appears in this wiki
MineDojo is the **cheap-trial domain** that made autonomous code revision practical before robotics could support it. Failures are free, resets are instant, and success is programmatically checkable — the three properties [ASPIRE](aspire.md) identifies as *missing* in real-world robot deployment. The GEAR line runs MineDojo → Voyager → ASPIRE, carrying the same open-ended-learning architecture from a domain where trials are free into one where they are not.

## Related
- [Voyager](voyager.md) — built on it.
- [NVIDIA GEAR](nvidia-gear.md) — home lab; MineDojo heads the open-ended-agents pillar.
- [Code as policy](../concepts/agents/code-as-policy.md) — the cheap-trial precedent.

## Mentioned in
- [Voyager paper](../sources/voyager-paper.md) — the simulation environment.
- [NVIDIA GEAR Lab — Publications](../sources/nvidia-gear-publications.md) — listed under open-ended agents.
