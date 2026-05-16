---
title: Unitree H1
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-08
sources: 0
tags: [unitree-h1, humanoid, bipedal, china, affordable, research]
status: stub
---

**Unitree H1** — full-size bipedal humanoid from Unitree Robotics (Hangzhou, China). Released August 2023. **One of the cheapest serious research-tier humanoids** at ~$90,000 starter price (vs $1M+ for Atlas, ~$133k for Ameca, undisclosed for Optimus / Figure). Widely adopted for academic locomotion / RL / VLA work in 2024–2026.

## Specs
- ~1.8 m tall, ~47 kg.
- 19 DOF total.
- Walking speed up to ~3.3 m/s (claimed; field-verified slower).
- Battery: ~2 hr operating time.

## Why it matters
- **Affordable research humanoid.** The "Unitree price point" — ~$90k for H1, ~$16k for [G1](unitree-g1.md) — makes humanoid RL research economically feasible for academic labs, the way Stretch made mobile manipulation research feasible.
- **Rapid academic adoption.** Used for locomotion / whole-body control papers across multiple institutions starting 2024.
- **Vendor lock-in concerns.** Closed firmware + Chinese supply chain raise issues for some institutions; mitigated somewhat by open-source SDK + community support.

## Position vs other humanoids
- **Cheaper than Western-tier humanoids** (Atlas, Optimus, Figure) by 1–2 orders of magnitude.
- **More expensive but more capable than [G1](unitree-g1.md)**.
- **No bundled VLA** (vs Figure with Helix or NVIDIA's GR00T-on-Apptronik partnership) — Unitree sells hardware, AI is up to the user.

## Related
- Unitree Robotics — manufacturer (Hangzhou, China).
- [Unitree G1](unitree-g1.md) — smaller, cheaper sibling.
- [Atlas](atlas.md) / [Figure](figure.md) / [Tesla Optimus](tesla-optimus.md) — flagship-tier competitors.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — landscape.

## Mentioned in
- *(no source pages directly cite Unitree H1; entity built from general knowledge)*

## Open questions / TBD
- **No primary source ingested.** Unitree's product page + academic papers using H1 would anchor specs and adoption.
- Specific research papers using H1 for VLA / manipulation work — known to exist but not yet ingested in this wiki.
- H1 vs G1 selection criteria — not yet documented as a comparison.
