---
title: Meta FAIR
type: entity
subtype: company
created: 2026-05-07
updated: 2026-05-07
sources: 5
tags: [meta, fair, lecun, world-model, jepa]
---

Meta's Fundamental AI Research lab ("FAIR at Meta"). Center of gravity for the [JEPA](../concepts/jepa.md) research line under Yann LeCun. Maintains [V-JEPA 2](v-jepa-2.md) / [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md), [DINO-WM](dino-wm.md) (with NYU), [DINO-world](dino-world.md), and [JEPA-WMs](jepa-wms.md) (Terver et al.). Adjacent to other Meta-affiliated efforts — [Robot Utility Models](robot-utility-models.md) (NYU + Meta authors include Soumith Chintala and Chris Paxton) and the Habitat embodied-AI suite.

## What we know
- **JEPA program**: V-JEPA → [V-JEPA 2](v-jepa-2.md) → V-JEPA 2-AC → [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md) (March 2026, "dense features"). And in parallel, [DINO-WM](dino-wm.md) (Nov 2024, with NYU) → [DINO-world](dino-world.md) (July 2025, video) → [JEPA-WMs](jepa-wms.md) (Dec 2025, robot-specific). Two parallel lines: *encoder-co-trained* (V-JEPA family) and *frozen DINOv2 features* (DINO-WM / DINO-world / JEPA-WMs).
- **Key people**: Yann LeCun (chief AI scientist), Mahmoud Assran, Adrien Bardes, Nicolas Ballas, Michael Rabbat, Franziska Meier (V-JEPA 2 core team). Adrien Bardes is also senior on [JEPA-WMs](../sources/jepa-wms-paper.md). Basile Terver is the bread-crumb across [DINO-world](../sources/dino-world-paper.md) and [JEPA-WMs](../sources/jepa-wms-paper.md). Federico Baldassarre + Piotr Bojanowski + Maximilian Seitzer carry the DINO-world line.
- **Simulator stance — observed pattern, not stated.** Early FAIR JEPA work (V-JEPA 2, June 2025) skipped sim entirely. The Dec 2025 JEPA-WMs paper moved into [RoboCasa](robocasa.md) + Metaworld + DROID + real Franka. V-JEPA 2.1 (March 2026) sustains the no-sim line with internet-video benchmarks + real-robot eval. FAIR is hedging across both. See [the revised synthesis](../syntheses/why-jepa-research-skips-the-simulator-stack.md).
- **Open source**: facebookresearch/vjepa2, facebookresearch/jepa-wms.
- **Adjacent**: [Robot Utility Models](robot-utility-models.md) (Meta-affiliated co-authors). [Habitat](habitat.md) — embodied-AI sim suite (note: notably absent from FAIR's own JEPA work despite shared institutional context).

## Why it matters
With NVIDIA pushing generative video as the world-model paradigm and AGIBOT pushing simulator-native scene generation, **FAIR's bet is latent-prediction JEPA** — predict next-state representation, not pixels. The contrast between paradigms is one of the most consequential open questions in agentic robotics 2026.

## Related
- [V-JEPA 2](v-jepa-2.md) — flagship product.
- [DINO-WM](dino-wm.md) — JEPA-adjacent (FAIR + NYU).
- [DINO-world](dino-world.md) — DINOv2 video world model.
- [JEPA-WMs](jepa-wms.md) — Terver et al. (Dec 2025), the heavy-sim FAIR JEPA paper.
- [Joint-Embedding Predictive Architecture](../concepts/jepa.md) — research program.
- [Mila](mila.md) — frequent collaborator.
- [Robot Utility Models](robot-utility-models.md) — Meta-affiliated adjacent project.

## Mentioned in
- [V-JEPA 2 Paper](../sources/v-jepa-2-paper.md)
- [V-JEPA 2.1 Paper](../sources/v-jepa-2-1-paper.md)
- [DINO-WM Paper](../sources/dino-wm-paper.md)
- [DINO-world Paper](../sources/dino-world-paper.md)
- [JEPA-WMs Paper](../sources/jepa-wms-paper.md)
