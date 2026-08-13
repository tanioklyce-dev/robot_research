---
title: CLIPort
type: entity
subtype: model
created: 2026-08-03
updated: 2026-08-03
sources: 2
tags: [cliport, imitation-learning, manipulation, baseline, transporter-nets, generalization]
---

**CLIPort** — a language-conditioned imitation-learning policy for tabletop manipulation (CLIP semantics + Transporter Nets spatial reasoning), widely used as the pre-VLA supervised baseline.

## Why it matters in this wiki — the collapse baseline
CLIPort is the policy that **goes to zero** in the early [code-as-policy](../concepts/agents/code-as-policy.md) papers, and it is the clearest precedent for the 2026 [LIBERO-PRO](../sources/libero-pro-paper.md) result:

| Source | CLIPort in-distribution | CLIPort out-of-distribution |
|---|---|---|
| [Code as Policies](../sources/code-as-policies-paper.md), 50 trials/task | 78.8–97.3% | **0.00–0.01%** (unseen attributes + instructions) |
| [Inner Monologue](../sources/inner-monologue-paper.md), 50 episodes/task | up to 94% (with oracle termination) | **0.0%** on every unseen task |

Trained on 30k demonstrations in the CaP evaluation. **In-distribution it beats the code-writing agent** on spatial-geometric tasks (97.33 vs 89.30) — the advantage of code-as-policy was never raw capability, only graceful degradation.

Four years later [OpenVLA](openvla.md) and [π0](pi-zero.md) post the same 0.00 under perturbation. The pattern is old; what changed is that the collapsing models are now internet-scale foundation models rather than a 30k-demo policy.

## Related
- [Imitation learning](../concepts/learning/imitation-learning.md) — the method class.
- [Code as policy](../concepts/agents/code-as-policy.md) — where the contrast is drawn.
- [LIBERO](libero.md) — where the same shape recurs in 2026.

## Mentioned in
- [Code as Policies paper](../sources/code-as-policies-paper.md) — supervised baseline trained on 30k demos.
- [Inner Monologue paper](../sources/inner-monologue-paper.md) — baseline with and without termination oracle.
- [VoxPoser paper](../sources/voxposer-paper.md) — the Transporter/CLIPort simulation lineage its block-world mirrors.

## Open questions / TBD
- The original CLIPort paper (Shridhar et al., CoRL 2021) is not ingested; the wiki knows it only as a baseline in other people's tables.
