---
title: Figure
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-05-08
sources: 1
tags: [figure, humanoid, bipedal, helix, openai, bmw]
status: partial
---

**Figure** — humanoid robot line from **Figure AI** (Brett Adcock, founded 2022). Generations: **Figure 01** (2023), **Figure 02** (August 2024), **Figure 03** (2025). Notable for early **OpenAI partnership** (dissolved 2024) and Figure's own end-to-end VLA, **Helix**, announced 2025. Industrial pilots at BMW (vehicle assembly) since early 2024.

## Specs (Figure 02, August 2024)
- ~1.68 m tall, ~60 kg.
- 16 DOF in hands.
- Cameras at head + body for visual reasoning.

## Helix (Figure's VLA)
- End-to-end vision-language-action policy.
- Trained on Figure-collected data + simulation.
- Demos: bimanual manipulation, object handover between robots.
- One of the few non-NVIDIA, non-open VLA systems with public capability demos.

## Position vs other humanoids
- **AI-foundation-first strategy.** Figure's bet is that the humanoid policy stack matters more than the hardware — Helix is the differentiator.
- **Industrial pilots over consumer.** BMW + other manufacturing deployments first, consumer applications second.
- **Closed AI stack** but more visible than Tesla Optimus or Atlas — Figure publishes capability videos and partial technical claims regularly.

## Related
- Figure AI — manufacturer.
- [Atlas](atlas.md) / [Tesla Optimus](tesla-optimus.md) / [Apptronik Apollo](apptronik-apollo.md) — research-humanoid competitors.
- [VLA models](../concepts/vla-models.md) — Helix is in this paradigm.
- [Humanoid platforms survey](../syntheses/humanoid-platforms-survey.md) — landscape.

## Deployment data (from AI Index 2026)

Figure 02 at BMW plant (South Carolina), 2025:
- **11 months** on the line
- **1,250+ runtime hours**
- **90,000+ parts loaded** across 30,000+ vehicles

([Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md))

## Mentioned in
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)

## Open questions / TBD
- **No primary source ingested.** Figure AI's blog + Helix announcement would anchor the VLA design and capability claims.
- Helix specs (parameters, training data) — minimally disclosed publicly.
- Figure 03 detailed specs — evolved from 02 but not exhaustively documented publicly.
