---
title: Humanoid platforms survey
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [humanoids, hardware, comparison, list, bipedal, education, research]
---

# Humanoid platforms survey

Companion to [[robot-platforms-comparison|Robot platforms — comparison]] focused specifically on **humanoids**. Drives 2026 industry attention disproportionate to academic ingest in this wiki — most humanoid work is closed-development (Tesla, Atlas) or vendor-published (Figure, 1X), so the academic + open-source bias of the rest of the wiki under-represents this category. This page is a **list-with-comparison** to anchor future ingests.

> [!note] Coverage caveat
> All entity pages referenced here are stubs filed from general knowledge. None has a primary source ingested in this wiki yet. Treat the specs as orientation, not citation.

## At a glance

| Robot | Tier | Manufacturer | Height | Price (est.) | AI strategy |
|---|---|---|---|---|---|
| [[atlas\|Atlas]] | Research (closed) | Boston Dynamics / Hyundai | ~1.5 m | Internal-only | Proprietary BD stack |
| [[tesla-optimus\|Tesla Optimus]] | Research (closed) | Tesla | ~1.73 m | Internal; aspirational $20–30k | Vertically integrated, FSD-derived |
| [[figure\|Figure 02 / 03]] | Research (closed) | Figure AI | ~1.68 m | Industrial pilots only | Helix VLA (in-house) |
| [[1x-neo\|1X NEO]] | Research / household (closed) | 1X Technologies | ~1.65 m | Pre-orders ~$20k+ | OpenAI-aligned FM |
| [[apptronik-apollo\|Apptronik Apollo]] | Research / industrial | Apptronik | ~1.73 m | Industrial pilots | NVIDIA-aligned ([[nvidia-groot\|GR00T]]) |
| [[digit\|Digit]] | Industrial (deployed) | Agility Robotics | ~1.75 m | Pilot pricing | Narrow-task BC |
| [[unitree-h1\|Unitree H1]] | Affordable research | Unitree Robotics | ~1.8 m | ~$90k starter | Open SDK, user-supplied AI |
| [[unitree-g1\|Unitree G1]] | Affordable research / educational | Unitree Robotics | ~1.32 m | ~$16k starter | Open SDK, user-supplied AI |
| [[nao\|NAO V6]] | Educational | SoftBank / Aldebaran | ~58 cm | ~$8–15k | Choregraphe + Python/C++ |
| [[tonypi\|TonyPi / TonyPi Pro]] | Educational (hobby) | Hiwonder | small | $300–700 | Pre-loaded demos |

## By tier

### Closed-development research humanoids (Atlas, Optimus, Figure, 1X)
The **flagship-capability tier** — Atlas (parkour, dexterous manipulation), Tesla Optimus (vertical FSD-derived stack), Figure (Helix VLA), 1X NEO (household OpenAI-aligned). All four are characterized by:

- **Vendor-only access.** No academic units sold; capability claims are vendor-published.
- **Industrial / commercial pilots first.** BMW (Figure), Mercedes-Benz (Apptronik), Hyundai factory (Atlas), Tesla factory (Optimus). Consumer comes later.
- **AI strategy varies wildly.** Tesla = vertical, Figure = in-house Helix VLA, 1X = OpenAI-aligned, Apptronik = NVIDIA GR00T partner.

### Industrial-deployed humanoids (Digit)
**[[digit\|Digit]]** is the outlier — Agility Robotics has Digit in **active commercial deployment at GXO Logistics and Amazon trials**, not just pilots. Narrow-task scope (warehouse package handling) is the price for getting to deployment first.

### Affordable research humanoids (Unitree H1, G1)
The **price-floor tier**. [[unitree-h1|H1]] at ~$90k and [[unitree-g1|G1]] at ~$16k are the only humanoids cheap enough for individual research labs to acquire without specialized funding. Open SDKs, user-supplied AI. Rapid 2024–2026 academic adoption for locomotion / RL papers.

### Educational humanoids (NAO, TonyPi, Pepper, Robotis OP3)
The **pedagogy tier**. [[nao|NAO]] is the canonical platform since 2008. [[tonypi|TonyPi]] occupies a much-cheaper-still hobbyist / classroom kit niche from [[hiwonder|Hiwonder]] (same vendor as [[rosorin-pro|ROSOrin Pro]]). Robotis OP3 / DARwIn-MINI (no entity pages here) and Pepper (no entity page) round out the niche.

## Strategic patterns visible at this layer

### Three AI-strategy archetypes
1. **Vertical integration** (Tesla Optimus, Figure with Helix). Vendor controls hardware + AI; less dependence on outside infrastructure.
2. **Closed AI on partner hardware** (Boston Dynamics Atlas with proprietary stack, but increasingly NVIDIA-curious). Hardware-first lineage, AI follows.
3. **Open hardware + ecosystem AI** (Unitree H1/G1, Apptronik Apollo). Vendor sells hardware; AI ecosystem is open ([[nvidia-groot|GR00T]], academic stacks, in-house dev).

### Geographic clustering
- **US / North America**: Atlas (US, Hyundai-owned), Tesla, Figure, Apptronik, Agility, 1X (Norway-US dual).
- **China**: Unitree (H1, G1), [[agibot|AGIBOT]] (humanoid line not separately filed), Fourier (GR-1, GR-2), LimX (CL-2), Booster Robotics (T1) — collectively a **rapidly growing affordable-humanoid cluster**.
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

The ingested literature skews toward **academic JEPA / VLA / world-model work** that uses tabletop arms (Franka) or wheeled mobile manipulators (Stretch), not humanoids. Humanoid VLAs ([[nvidia-groot|GR00T]], Figure Helix) are mentioned but their **hardware-platform deployment papers** are not yet in the wiki. As humanoid VLA papers ingest (likely 2026 H2), this synthesis should grow into individual entity pages becoming substantive rather than stubs.

## What's still missing from this wiki

- **AGIBOT humanoid hardware** — [[agibot|company]] is filed but the specific humanoid platforms (A2, X1, X2) aren't separate entities yet.
- **Fourier GR-1 / GR-2** — Chinese affordable research humanoid.
- **LimX CL-2 / CL-3, Booster T1, EngineAI PM01** — affordable Chinese humanoids.
- **PAL Robotics TIAGo / TALOS** — European research-tier.
- **Pepper** — SoftBank social-robot sibling of NAO.
- **Robotis OP3, DARwIn-MINI** — RoboCup-tier educational humanoids.
- **Sanctuary AI Phoenix** — Canadian humanoid with Carbon AI control.
- **Kawasaki Kaleido, Toyota T-HR3, HRP-5P** — Japanese research humanoids.

## Sources used in this synthesis

- Per-platform entity pages: [[atlas|Atlas]], [[tesla-optimus|Tesla Optimus]], [[figure|Figure]], [[1x-neo|1X NEO]], [[apptronik-apollo|Apptronik Apollo]], [[digit|Digit]], [[unitree-h1|Unitree H1]], [[unitree-g1|Unitree G1]], [[nao|NAO]], [[tonypi|TonyPi]].
- Adjacent ingested context: [[nvidia-groot|GR00T]] (NVIDIA's VLA targeting humanoids), [[agibot|AGIBOT]] (Chinese embodied-AI company with humanoid line), [[newton-openusd-substrate-convergence|substrate-convergence synthesis]] (notes on closed industrial stacks).

## Related

- [[robot-platforms-comparison|Robot platforms — comparison]] — companion synthesis covering non-humanoid robots in the wiki.
- [[index|index.md]] — Robot platforms section.
