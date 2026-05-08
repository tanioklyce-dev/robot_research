---
title: Meta FAIR
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-07
sources: 5
tags: [meta, fair, lecun, world-model, jepa]
---

Meta's Fundamental AI Research lab ("FAIR at Meta"). Center of gravity for the [[jepa|JEPA]] research line under Yann LeCun. Maintains [[v-jepa-2|V-JEPA 2]] / [[v-jepa-2-1-paper|V-JEPA 2.1]], [[dino-wm|DINO-WM]] (with NYU), [[dino-world|DINO-world]], and [[jepa-wms|JEPA-WMs]] (Terver et al.). Adjacent to other Meta-affiliated efforts — [[robot-utility-models|Robot Utility Models]] (NYU + Meta authors include Soumith Chintala and Chris Paxton) and the Habitat embodied-AI suite.

## What we know
- **JEPA program**: V-JEPA → [[v-jepa-2|V-JEPA 2]] → V-JEPA 2-AC → [[v-jepa-2-1-paper|V-JEPA 2.1]] (March 2026, "dense features"). And in parallel, [[dino-wm|DINO-WM]] (Nov 2024, with NYU) → [[dino-world|DINO-world]] (July 2025, video) → [[jepa-wms|JEPA-WMs]] (Dec 2025, robot-specific). Two parallel lines: *encoder-co-trained* (V-JEPA family) and *frozen DINOv2 features* (DINO-WM / DINO-world / JEPA-WMs).
- **Key people**: Yann LeCun (chief AI scientist), Mahmoud Assran, Adrien Bardes, Nicolas Ballas, Michael Rabbat, Franziska Meier (V-JEPA 2 core team). Adrien Bardes is also senior on [[jepa-wms-paper|JEPA-WMs]]. Basile Terver is the bread-crumb across [[dino-world-paper|DINO-world]] and [[jepa-wms-paper|JEPA-WMs]]. Federico Baldassarre + Piotr Bojanowski + Maximilian Seitzer carry the DINO-world line.
- **Simulator stance — observed pattern, not stated.** Early FAIR JEPA work (V-JEPA 2, June 2025) skipped sim entirely. The Dec 2025 JEPA-WMs paper moved into [[robocasa|RoboCasa]] + Metaworld + DROID + real Franka. V-JEPA 2.1 (March 2026) sustains the no-sim line with internet-video benchmarks + real-robot eval. FAIR is hedging across both. See [[why-jepa-research-skips-the-simulator-stack|the revised synthesis]].
- **Open source**: facebookresearch/vjepa2, facebookresearch/jepa-wms.
- **Adjacent**: [[robot-utility-models|Robot Utility Models]] (Meta-affiliated co-authors). Habitat — embodied-AI sim suite (mentioned but no entity page yet).

## Why it matters
With NVIDIA pushing generative video as the world-model paradigm and AGIBOT pushing simulator-native scene generation, **FAIR's bet is latent-prediction JEPA** — predict next-state representation, not pixels. The contrast between paradigms is one of the most consequential open questions in agentic robotics 2026.

## Related
- [[v-jepa-2|V-JEPA 2]] — flagship product.
- [[dino-wm|DINO-WM]] — JEPA-adjacent (FAIR + NYU).
- [[dino-world|DINO-world]] — DINOv2 video world model.
- [[jepa-wms|JEPA-WMs]] — Terver et al. (Dec 2025), the heavy-sim FAIR JEPA paper.
- [[jepa|Joint-Embedding Predictive Architecture]] — research program.
- [[mila|Mila]] — frequent collaborator.
- [[robot-utility-models|Robot Utility Models]] — Meta-affiliated adjacent project.

## Mentioned in
- [[v-jepa-2-paper|V-JEPA 2 Paper]]
- [[v-jepa-2-1-paper|V-JEPA 2.1 Paper]]
- [[dino-wm-paper|DINO-WM Paper]]
- [[dino-world-paper|DINO-world Paper]]
- [[jepa-wms-paper|JEPA-WMs Paper]]
