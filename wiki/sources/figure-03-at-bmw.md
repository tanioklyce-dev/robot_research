---
title: F.03 Arrives at BMW (Figure AI)
type: source
url: https://www.figure.ai/news/f-03-at-bmw
author: Figure AI
affiliation: Figure AI
published: 2026-06-30
ingested: 2026-08-28
tags: [figure, figure-03, helix-02, bmw, manufacturing, logistics, loco-manipulation, deployment, vendor-source]
---

## Summary

Figure 03 returns to **BMW Group Plant Spartanburg** (Hall 52, assembly and logistics), succeeding the Figure 02 deployment that contributed to **30,000 cars in 2025**. The task changes qualitatively: from *"classic pick-and-place sheet metal loading"* to **sequencing** — selecting and ordering parts for the assembly line from containers where parts *"do not arrive in mathematically perfect orientations."* Figure frames this as the first commercial demonstration of **[Helix 02](figure-helix-02.md)'s loco-manipulation** on a factory floor: manipulating parts while stepping and repositioning the body, including **pulling a heavy cart on caster wheels**.

## Key claims

- First demonstration of **Figure 03** performing a logistics workflow at BMW Spartanburg.
- **Helix 02 coordinates hands, arms, torso and feet** as one system — the robot manipulates parts *while* stepping and repositioning, and pulls a large metal cart down the line.
- **Sequencing** is characterised as "an intractable sorting environment": parts "may have shifted, rotated, partially occluded, or presented differently within a container," so "each interaction requires the robot to perceive the scene and make small corrections on the fly." Not solvable "with a fixed series of hard-coded motions."
- **The humanoid-form argument, stated explicitly**: this is "dynamic material manipulation that is structurally infeasible to solve with traditional, fixed automation or six-axis robotic arm."
- **Two force regimes in one workflow**: precise picking/placing of thin-walled individual parts, and forceful whole-body manipulation (the cart).
- Prior generation context: **Figure 02 contributed to the assembly of 30,000 cars at BMW** in 2025 (consistent with the [AI Index 2026](stanford-hai-ai-index-2026.md) figures of 11 months, 1,250+ hours, 90,000+ parts).

## Assessment

> [!note] This is the strongest form of the humanoid business case in the wiki
> Not "humanoids are general" in the abstract, but a named task with a named reason fixed automation fails it: **the parts are not presented repeatably, and the workspace is larger than an arm's envelope**. Sequencing needs perception-driven correction *and* mobility *and* two force scales. Whether a humanoid is the cheapest answer is a separate question the post does not touch — a mobile base with one arm is the obvious rival, and the cart-pulling is the only part of the described workload that clearly wants legs and a torso.

> [!warning] No throughput, no cycle time, no success rate, no unit count
> Figure 02's BMW deployment eventually produced auditable-sounding numbers (30,000 cars, 90,000 parts, 1,250 hours). This post has **none** — it announces arrival, not results. Read as a milestone marker; the numbers, if they come, will come a year later as they did for Figure 02.

> [!note] The home pivot did not replace the factory
> Figure's [product page](figure-03-product-page.md) is now entirely home-facing, yet the commercial deployment continued in parallel. Figure's stated logic in the [Figure 03 announcement](figure-03-announcement.md) is that solving the home's variability *produces* the general-purpose product that the workforce wants — the home is the hard training environment, not a market pivot away from industry.

## Entities mentioned

- [Figure 03](../entities/figure-03.md) · [Helix](../entities/helix.md) · [Figure](../entities/figure.md)

## Concepts touched

- [Whole-body control](../concepts/robotics/whole-body-control.md) — loco-manipulation under load.
- [VLA models](../concepts/learning/vla-models.md) — "pixels-to-actions VLA" in a production environment.

## Open questions

- **Is this a pilot or a production role?** "Arrived" and "demonstration" suggest the former; Figure 02 took ~a year to reach reported production contribution.
- **How many Figure 03 units at Spartanburg?**
- **What does BMW say?** Every claim here is Figure's; BMW Group has its own newsroom and is not quoted.
