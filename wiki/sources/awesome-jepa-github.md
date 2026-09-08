---
title: "awesome-jepa (AI-in-Transportation-Lab) — 248-paper JEPA index"
type: source
url: https://github.com/AI-in-Transportation-Lab/awesome-jepa
local_path: raw/2026-09-07-awesome-jepa-readme.md
sha256: 133f847ba5ed79009aeb8b4789a8ec57d27cbc4eab2bbc3dbec09ddc7fbc1293
author: "AI-in-Transportation-Lab (GitHub org)"
published: 2026-09-07
venue: "GitHub awesome-list; 140 stars, last pushed 2026-09-07 (captured same day)"
format: curated link list (README.md)
tags: [jepa, awesome-list, index, gap-analysis, world-models, ssl, transportation, triage]
ingested: 2026-09-07
---

## Summary

**A 248-paper index of the JEPA literature, and a useful gap-check on a wiki that thought it had this area covered.** Cross-referenced by arXiv ID against every page and raw file here: **8 of 248 overlap.** That sounds damning and is not — this wiki's JEPA coverage is narrow and deep (LeJEPA, SIGReg, identifiability, LeWorldModel, LeVJEPA, PLDM, stable-worldmodel, the anti-collapse lineage), while the list is broad and shallow. They are complements, and the list's value is as **triage input**, not as reading.

Ingested at request to review what is worth pulling from it. The ranked shortlist is in [the backlog](../backlog.md); the assessment of the resource is here.

## What it actually is

- **248 linked paper entries.** The `## Library` and `## Tutorial` sections **exist and are empty**, despite the repo description promising *"tools, libraries, research papers, projects, and tutorials."* It is a paper list.
- **Curated by a transportation lab**, and it shows: driving, UAV, wireless and traffic work is heavily represented (Drive-JEPA, WA-JEPA, HanoiWorld, SkyJEPA, radio world models, wireless CSI, beyond-5G predictive remote control). **The lens is transportation, not robotics** — worth knowing before treating the ranking as a field consensus.
- Actively maintained: last push the same day it was captured.

> [!note] The list is accurate — verified rather than assumed
> Seven of the shortlisted entries were checked against arXiv abs pages directly: **all seven exist with matching titles.** One genuine defect found: **2608.10780 appears twice with two different titles** ("StageWAM: Joint-Embedding Stage Prediction…" and "JEPA-WAM: Stage-Level Joint-Embedding Prediction…"). The arXiv record says **StageWAM**; the second entry is the list's error.

## What its shape says about the field

The most interesting thing here is not any single paper. It is **how far JEPA has diffused from vision**: the list carries JEPA variants for **EEG**, **cardiac electrophysiology**, **hydrology**, **wireless channel state information**, **financial transactions**, **audio and music**, **trajectory similarity**, **document retrieval**, **PDE control**, and **radio-astronomy reionization inference**.

That corroborates, from an outside index, something this wiki inferred from one researcher's CV a few hours earlier: **the JEPA programme's centre of gravity is not robot control.** [Balestriero's own site](randall-balestriero-personal-site.md) lists his application domains as *"vision, NLP, geophysics, bioacoustics, medical signals, and quantitative finance"* — robotics absent. Two independent sources, same signal. This wiki reads the line largely through robot control; the field does not.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — the index's subject.
- [World-action model](../concepts/world-models/world-action-model.md) · [identifiability](../concepts/world-models/identifiability.md) · [SIGReg](../concepts/world-models/sigreg.md) — the three areas the shortlist draws from most.
- [SSL anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md) — where a "No Gaussian Required" result would land.

## Open questions

- **Is 8-of-248 the right overlap?** The shortlist argues about ten more are worth reading. If the remaining ~230 are genuinely not worth this wiki's time, that is a statement about JEPA's spread rather than about the wiki's coverage — and it is the kind of claim that should be revisited if the shortlist reads well.
- **Where is the equivalent list for the reconstruction side?** The wiki has no index of the MAE/VideoMAE/diffusion-world-model literature, and [the crossover result](joint-embedding-vs-reconstruction-paper.md) says that half matters exactly as much.
