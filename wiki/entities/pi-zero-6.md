---
title: π0.6 (and intermediates π0.5, π0.6-MEM)
type: entity
subtype: model
created: 2026-05-25
updated: 2026-08-03
sources: 7
tags: [pi-zero-6, pi-zero-5, pi-zero-6-mem, pi-zero, physical-intelligence, vla, flow-matching, intermediate, lineage, knowledge-insulation]
status: stub
---

> [!note] Stub entity — anchors a wiki-known lineage gap
> Filed 2026-05-25 during lint (π0.6: 47 mentions / 14 files; π0.5: 23 mentions / 12 files; π0.6-MEM: 14 mentions / 6 files). **Update 2026-08-03: π0.5's primary is now ingested** — [paper](../sources/pi-zero-5-paper.md) + [entity](pi-zero-5.md) (arXiv 2504.16054, public since Apr 2025; the stub's original "no publicly released primary" framing was wrong for π0.5). **This stub now anchors only π0.6 and π0.6-MEM**, which remain documented solely via downstream references in [π0.7](pi07.md) and [π*0.6](pistar06.md). Deepen if + when their primaries land.

The wiki's two strongest 2025 VLAs — **[π0.7](pi07.md)** and **[π*0.6](pistar06.md)** — both build on intermediate **π0.6** + **π0.6-MEM** generations of Physical Intelligence's π-series. Those intermediates inherit from **π0.5**, which itself sits between [π0](pi-zero.md) and π0.6. This entity exists to give the lineage a stable anchor.

## What we know from downstream references

### π0.5 (intermediate after π0)

- Adds **intermediate-subtask conditioning** — high-level text describing the next semantic subtask (e.g. "open the fridge door") in addition to the overall task description ("clean the kitchen"). [π0.7 paper](../sources/pi07-paper.md) §V-A: "Following π0.5, we include intermediate, higher-level text that captures the next semantic subtask as part of the prompt."
- The "VLM-as-planner + π-VLA-as-controller" stack pattern starts here.
- **π0.5-KI** — π0.5 trained with the [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) recipe — *does* have an ingested primary ([KI paper](../sources/knowledge-insulation-paper.md), Driess et al. 2505.23705); it's that paper's "Ours (from generalist model)" (LIBERO avg 94.3). So while plain π0.5 has no paper, the π0.5-**KI** variant referenced across the wiki is fully sourced.

### π0.6 (intermediate after π0.5)

- **Larger backbone + more diverse conditioning** ([π*0.6 paper](../sources/pistar06-paper.md) §I): "π0.6 is an improvement on π0.5, adding a larger backbone and more diverse conditioning."
- The direct parent of [π*0.6](pistar06.md) (RL variant via RECAP) and [π0.6-MEM](pi-zero-6.md) (memory variant), which together feed into [π0.7](pi07.md).

### π0.6-MEM (intermediate after π0.6)

- Adds the **MEM video history / memory encoder** — temporal + spatial compression over history observations, outputting a fixed number of tokens regardless of frame count.
- [π0.7 paper](../sources/pi07-paper.md) §IV: "π0.7 is our newest robotic foundation model that builds on the existing VLA architecture from π0.6 [42] and the MEM memory system [37] and extends it with multi-modal context conditioning."

## π-series lineage (consolidated)

```
π0  →  π0.5  →  π0.6  →  π0.6-MEM  →  π0.7    (Oct 2024 → late 2025)
                                  ↘   π*0.6   (RL variant)
```

| Model | Year | Status in wiki | Primary source ingested |
|---|---|---|---|
| [π0](pi-zero.md) | Oct 2024 | Full entity + source | [pi-zero-paper.md](../sources/pi-zero-paper.md) ✓ |
| **π0.5** | — | **Stub here** | **No** |
| **π0.6** | — | **Stub here** | **No** |
| **π0.6-MEM** | — | **Stub here** | **No** |
| [π0.7](pi07.md) | 2025 | Full entity + source | [pi07-paper.md](../sources/pi07-paper.md) ✓ |
| [π*0.6](pistar06.md) | 2025 | Full entity + source | [pistar06-paper.md](../sources/pistar06-paper.md) ✓ |

## Why this matters in this wiki

- **Anchors the most-frequently-referenced unfiled lineage in the wiki** (~84 combined mentions across 14+ files).
- **Closes the citation gap** — pages referencing "π0.6" or "π0.6-MEM" now have a target entity to link instead of dangling text.

## Related

- [π0](pi-zero.md), [π0.7](pi07.md), [π*0.6](pistar06.md) — primary-source ingested π-series entries.
- [Physical Intelligence](physical-intelligence.md) — see the full lineage table on this entity.
- [Flow matching](../concepts/learning/flow-matching.md) — action-head family used throughout the π-series.

## Mentioned in
- [so101_ros2 readthedocs](../sources/so101-ros2-readthedocs.md) — π0.5/π0.6 among supported deployment policies.
- [Rosetta GitHub](../sources/rosetta-github.md) — π0.5 (sibling of π0.7) among supported policies.

## Open questions

- **Whether π0.5 / π0.6 / π0.6-MEM ever had standalone publications** is unclear from the public Physical Intelligence website. If they're blog-only or technical-report-only, the wiki may not get a primary source for these intermediates.
- **What "larger backbone" means specifically for π0.6** — π0 uses PaliGemma 3 B, π0.7 uses Gemma3 4 B. Whether π0.6 = Gemma3 4 B is the architectural step is plausible but not confirmed.
- **MEM memory system specifics** (referenced as `[37]` in π0.7 and π*0.6) — the underlying paper isn't in the wiki.
