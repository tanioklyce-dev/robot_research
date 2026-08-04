---
title: Evo-1
type: entity
subtype: model
created: 2026-08-04
updated: 2026-08-04
sources: 1
tags: [evo-1, vla, lightweight-vla, efficient-inference, libero]
---

**Evo-1** (Lin et al., CVPR 2026) — a **0.8 B-parameter lightweight [VLA](../concepts/learning/vla-models.md)**; one of the compact-architecture line that reduces model scale while **retaining** a pretrained multimodal backbone.

_Stub — known here only through the [TurboVLA](turbovla.md) comparison table._

| | Params | VRAM | Latency | LIBERO avg |
|---|---:|---:|---:|---:|
| Evo-1 | 0.8 B | 1.7 GB | 137.2 ms | 94.8 |
| [TurboVLA](turbovla.md) | 0.2 B | 0.9 GB | 31.2 ms | 97.7 |

> [!note] The one lightweight comparison that actually separates
> TurboVLA's 97.7 vs Evo-1's 94.8 at n = 2,000 gives **p < 0.001 — it survives** ([audit](../syntheses/platforms/vla-success-rate-audit.md)), unlike its ties with π0.5 and OpenVLA-OFT at the top of the table. Evo-1 is also the sharpest illustration that **small ≠ fast**: at 4× the parameters it is 4.4× slower, because it keeps a pretrained multimodal backbone in the loop. Parameter count and latency are separate axes.

## Related
- [SmolVLA](smolvla.md) — the other lightweight reference in this wiki
- [LLM-free VLA](../concepts/learning/llm-free-vla.md) — the alternative Evo-1 does *not* take

## Mentioned in
- [TurboVLA paper](../sources/turbovla-paper.md)
