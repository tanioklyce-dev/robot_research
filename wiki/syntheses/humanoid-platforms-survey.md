---
title: Humanoid platforms survey
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [humanoids, hardware, comparison, list, bipedal, education, research]
---

# Humanoid platforms survey

Companion to [Robot platforms — comparison](robot-platforms-comparison.md) focused specifically on **humanoids**. Drives 2026 industry attention disproportionate to academic ingest in this wiki — most humanoid work is closed-development (Tesla, Atlas) or vendor-published (Figure, 1X), so the academic + open-source bias of the rest of the wiki under-represents this category. This page is a **list-with-comparison** to anchor future ingests.

> [!note] Coverage caveat
> All entity pages referenced here are stubs filed from general knowledge. None has a primary source ingested in this wiki yet. Treat the specs as orientation, not citation.

## At a glance

| Robot | Tier | Manufacturer | Height | Price (est.) | AI strategy |
|---|---|---|---|---|---|
| [Atlas](../entities/atlas.md) | Research (closed) | Boston Dynamics / Hyundai | ~1.5 m | Internal-only | Proprietary BD stack |
| [Tesla Optimus](../entities/tesla-optimus.md) | Research (closed) | Tesla | ~1.73 m | Internal; aspirational $20–30k | Vertically integrated, FSD-derived |
| [Figure 02 / 03](../entities/figure.md) | Research (closed) | Figure AI | ~1.68 m | Industrial pilots only | Helix VLA (in-house) |
| [1X NEO](../entities/1x-neo.md) | Research / household (closed) | 1X Technologies | ~1.65 m | Pre-orders ~$20k+ | OpenAI-aligned FM |
| [Apptronik Apollo](../entities/apptronik-apollo.md) | Research / industrial | Apptronik | ~1.73 m | Industrial pilots | NVIDIA-aligned ([GR00T](../entities/nvidia-groot.md)) |
| [Digit](../entities/digit.md) | Industrial (deployed) | Agility Robotics | ~1.75 m | Pilot pricing | Narrow-task BC |
| [Unitree H1](../entities/unitree-h1.md) | Affordable research | Unitree Robotics | ~1.8 m | ~$90k starter | Open SDK, user-supplied AI |
| [Unitree G1](../entities/unitree-g1.md) | Affordable research / educational | Unitree Robotics | ~1.32 m | ~$16k starter | Open SDK, user-supplied AI |
| [NAO V6](../entities/nao.md) | Educational | SoftBank / Aldebaran | ~58 cm | ~$8–15k | Choregraphe + Python/C++ |
| [TonyPi / TonyPi Pro](../entities/tonypi.md) | Educational (hobby) | Hiwonder | small | $300–700 | Pre-loaded demos |

## By tier

### Closed-development research humanoids (Atlas, Optimus, Figure, 1X)
The **flagship-capability tier** — Atlas (parkour, dexterous manipulation), Tesla Optimus (vertical FSD-derived stack), Figure (Helix VLA), 1X NEO (household OpenAI-aligned). All four are characterized by:

- **Vendor-only access.** No academic units sold; capability claims are vendor-published.
- **Industrial / commercial pilots first.** BMW (Figure), Mercedes-Benz (Apptronik), Hyundai factory (Atlas), Tesla factory (Optimus). Consumer comes later.
- **AI strategy varies wildly.** Tesla = vertical, Figure = in-house Helix VLA, 1X = OpenAI-aligned, Apptronik = NVIDIA GR00T partner.

### Industrial-deployed humanoids (Digit)
**[Digit](../entities/digit.md)** is the outlier — Agility Robotics has Digit in **active commercial deployment at GXO Logistics and Amazon trials**, not just pilots. Narrow-task scope (warehouse package handling) is the price for getting to deployment first.

### Affordable research humanoids (Unitree H1, G1)
The **price-floor tier**. [H1](../entities/unitree-h1.md) at ~$90k and [G1](../entities/unitree-g1.md) at ~$16k are the only humanoids cheap enough for individual research labs to acquire without specialized funding. Open SDKs, user-supplied AI. Rapid 2024–2026 academic adoption for locomotion / RL papers.

### Educational humanoids (NAO, TonyPi, Pepper, Robotis OP3)
The **pedagogy tier**. [NAO](../entities/nao.md) is the canonical platform since 2008. [TonyPi](../entities/tonypi.md) occupies a much-cheaper-still hobbyist / classroom kit niche from [Hiwonder](../entities/hiwonder.md) (same vendor as [ROSOrin Pro](../entities/rosorin-pro.md)). Robotis OP3 / DARwIn-MINI (no entity pages here) and Pepper (no entity page) round out the niche.

## Strategic patterns visible at this layer

### Three AI-strategy archetypes
1. **Vertical integration** (Tesla Optimus, Figure with Helix). Vendor controls hardware + AI; less dependence on outside infrastructure.
2. **Closed AI on partner hardware** (Boston Dynamics Atlas with proprietary stack, but increasingly NVIDIA-curious). Hardware-first lineage, AI follows.
3. **Open hardware + ecosystem AI** (Unitree H1/G1, Apptronik Apollo). Vendor sells hardware; AI ecosystem is open ([GR00T](../entities/nvidia-groot.md), academic stacks, in-house dev).

### Geographic clustering
- **US / North America**: Atlas (US, Hyundai-owned), Tesla, Figure, Apptronik, Agility, 1X (Norway-US dual).
- **China**: Unitree (H1, G1), [AGIBOT](../entities/agibot.md) (humanoid line not separately filed), Fourier (GR-1, GR-2), LimX (CL-2), Booster Robotics (T1) — collectively a **rapidly growing affordable-humanoid cluster**.
- **Europe**: Aldebaran/SoftBank NAO (France), PAL Robotics (Spain), Engineered Arts (UK).
- **Japan**: AIST HRP series, Toyota T-HR3, Kawasaki Kaleido — historically strong but lower visibility in 2024–2026 vs the US-China dynamic.

### Price stratification (2026)
- **Internal-only tier**: Atlas, Optimus (vendor doesn't sell).
- **$50k–$100k tier**: H1, Apollo (limited availability).
- **$15k–$25k tier**: G1, NEO Beta.
- **$8k–$15k tier**: NAO V6.
- **<$1k tier**: TonyPi (educational kit).

There is **no $25k–$50k tier**. The market is bifurcating into "expensive enterprise" vs "cheap research / educational" with little middle.

## Why this is underrepresented in this wiki

The ingested literature skews toward **academic JEPA / VLA / world-model work** that uses tabletop arms (Franka) or wheeled mobile manipulators (Stretch), not humanoids. Humanoid VLAs ([GR00T](../entities/nvidia-groot.md), Figure Helix) are mentioned but their **hardware-platform deployment papers** are not yet in the wiki. As humanoid VLA papers ingest (likely 2026 H2), this synthesis should grow into individual entity pages becoming substantive rather than stubs.

## What's still missing from this wiki

- **AGIBOT humanoid hardware** — [company](../entities/agibot.md) is filed but the specific humanoid platforms (A2, X1, X2) aren't separate entities yet.
- **Fourier GR-1 / GR-2** — Chinese affordable research humanoid.
- **LimX CL-2 / CL-3, Booster T1, EngineAI PM01** — affordable Chinese humanoids.
- **PAL Robotics TIAGo / TALOS** — European research-tier.
- **Pepper** — SoftBank social-robot sibling of NAO.
- **Robotis OP3, DARwIn-MINI** — RoboCup-tier educational humanoids.
- **Sanctuary AI Phoenix** — Canadian humanoid with Carbon AI control.
- **Kawasaki Kaleido, Toyota T-HR3, HRP-5P** — Japanese research humanoids.

## Sources used in this synthesis

- Per-platform entity pages: [Atlas](../entities/atlas.md), [Tesla Optimus](../entities/tesla-optimus.md), [Figure](../entities/figure.md), [1X NEO](../entities/1x-neo.md), [Apptronik Apollo](../entities/apptronik-apollo.md), [Digit](../entities/digit.md), [Unitree H1](../entities/unitree-h1.md), [Unitree G1](../entities/unitree-g1.md), [NAO](../entities/nao.md), [TonyPi](../entities/tonypi.md).
- Adjacent ingested context: [GR00T](../entities/nvidia-groot.md) (NVIDIA's VLA targeting humanoids), [AGIBOT](../entities/agibot.md) (Chinese embodied-AI company with humanoid line), [substrate-convergence synthesis](newton-openusd-substrate-convergence.md) (notes on closed industrial stacks).

## Related

- [Robot platforms — comparison](robot-platforms-comparison.md) — companion synthesis covering non-humanoid robots in the wiki.
- [index.md](../index.md) — Robot platforms section.
