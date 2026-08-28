---
title: F.03 Battery Development (Figure AI)
type: source
url: https://www.figure.ai/news/f-03-battery-development
author: Figure AI
affiliation: Figure AI
published: 2025-07-17
ingested: 2026-08-28
tags: [figure, figure-03, battery, safety, un38.3, ul2271, thermal-runaway, botq, manufacturing, vendor-source]
---

> [!note] The most technically substantive Figure primary in this wiki
> Unlike the Helix and Index posts, this one names standards, tests and mechanisms that are externally checkable in principle. It is still vendor-published and carries no third-party test report.

## Summary

Figure's engineering write-up on the **F.03 battery**, published three months before Figure 03 itself. Figure designs and manufactures the pack in-house at [BotQ](../entities/botq.md). Headline: **2.3 kWh giving 5 hours at peak performance**, **2 kW fast charge with active cooling**, **78% cost reduction over F.02**, **94% energy-density improvement since F.01**, and a **structural pack** integrated into the torso that doubles as a load-bearing member. The safety architecture is the substance of the post: Figure specified that a single-cell thermal runaway **must not emit flame**, and worked with an OSHA NRTL to help write a **UL 2271** standard for humanoid robot batteries because none existed.

## Key claims

### Performance

- **2.3 kWh → 5 hours runtime at peak performance.** This is the primary behind the "5 hr" on the [product page](figure-03-product-page.md).
- **2 kW fast charge** with active cooling — matches the wireless foot-coil charging rate in the [Figure 03 announcement](figure-03-announcement.md).
- **94% energy-density increase across three generations** (F.01 → F.03). F.01 used "bulky rectangular modules… that only fit in an external backpack"; F.03 is integrated into the torso.
- **78% cost reduction over F.02.**

### Architecture

- **Multi-function components** throughout, giving "a high cell-to-pack ratio, lower cost, and lower complexity."
- **Structural battery** — enclosure of high-strength stamped steel, die-cast aluminium and structural adhesive, serving as a structural member of the torso to save mass and volume at robot level. Survives a **1 m drop onto concrete from any orientation**.
- **Active cooling integrated into the die casting**, minimising thermal resistance so fast charge works with "simple forced convection."

### Safety — four layers

1. **BMS**: custom, with sensors/switches/fuses against overcharge, overdischarge, over-temperature, external short.
2. **Cell**: certified to UN, UL and IEC standards for crush, impact, overcharge, heating; two internal fusing mechanisms.
3. **Interconnect**: cell-to-cell wirebond geometry **tuned to act as a fusible element** — a deliberate weak link as short-circuit protection.
4. **Pack**: anti-propagation via "thermally insulative potting compound in concert with a rapid heat distribution strategy," plus flame containment through a multi-function flame-arrestor vent and "a patented technology to prevent an external flame from exiting the pack."

- **Fault-injection tested**: a cell was deliberately heated into thermal runaway; the pack "is able to prevent external flame and attenuate cell-to-cell thermal propagation."
- **Certification**: UN38.3 achieved (per the Figure 03 announcement); **first humanoid robot battery in process to be certified to both UN38.3 and UL 2271**. Figure worked with an OSHA **Nationally Recognized Testing Laboratory** to develop the UL standard, "since the robot battery safety standard did not exist," and invested "thousands of hours" against the standard's **twenty-three primary tests** (mechanical stress, charge-discharge cycling, temperature stress, EMI immunity).

### Manufacturing

- Component strategy moved from machining to **die casting, stamping, injection molding and dip molding** to hit BotQ's 12,000/year line rate.
- Battery manufacturing brought in-house; tied into BotQ's PLM, ERP, WMS and MES.
- (Later, from [Ramping Figure 03 Production](figure-ramping-03-production.md): the battery line reached **99.3% first-pass yield** and shipped **500+ packs**.)

## Why this matters beyond Figure

Figure is **co-authoring the safety standard for its own product category**. UL 2271 covers light electric vehicle batteries; there was no humanoid equivalent, so Figure went to an NRTL and helped define one. Whoever gets there first shapes what "safe" means for every humanoid that follows — a standards-capture position, whether or not it is intended as one. This is the wiki's first concrete instance of humanoid-specific safety certification actually being created rather than discussed.

> [!note] Energy budget, for comparison
> 2.3 kWh / 5 h = **~460 W average draw** for a 61 kg biped doing useful work. That is a plausible-to-optimistic figure and, notably, is a *whole-robot* budget that must also cover onboard Helix inference — which Figure has never sized. Contrast the wiki's [Jetson module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md): a Thor-class module alone can draw 40–130 W, i.e. up to ~28% of this budget.

## Entities mentioned

- [Figure 03](../entities/figure-03.md) · [Figure](../entities/figure.md) · [BotQ](../entities/botq.md) · [Helix](../entities/helix.md) — the onboard consumer of this power budget

## Concepts touched

- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — UN38.3, UL 2271, NRTL process.

## Open questions

- **Cell chemistry and supplier are never named.** 2.3 kWh at a mass that keeps the robot at 61 kg implies a pack in the ~12–15 kg range at plausible pack-level densities; Figure gives no pack mass.
- **"In process to be certified" (July 2025) → UN38.3 achieved (October 2025).** UL 2271 status is unreported since. Worth re-checking.
- **Cycle life is absent.** Runtime and safety are covered; nothing on degradation, which is the number that determines service cost across a 12,000-unit/year fleet.
