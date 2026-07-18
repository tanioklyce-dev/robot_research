---
title: MolmoAct
type: entity
subtype: model
created: 2026-07-17
updated: 2026-07-17
sources: 1
tags: [molmoact, vla, vision-language-action, discrete-tokens, spatial-reasoning, allen-institute, molmo, baseline]
status: stub
---

# MolmoAct

**MolmoAct** (Lee et al., 2025 — *MolmoAct: Action Reasoning Models that can Reason in Space*, arXiv 2508.07917) is a **[VLA](../concepts/learning/vla-models.md)** built on the Allen Institute for AI's open **Molmo** vision-language model, positioned as an **"action reasoning model"** that reasons about **space** before acting. In the wiki's action-head taxonomy it is a **discrete-token** VLA (like [OpenVLA](openvla.md)).

## Why it matters in this wiki

MolmoAct is one of the **large-scale-action-pretrained** baselines in the wiki's most complete cross-method [LIBERO](libero.md) table — a fully-open (Allen Institute) VLA data point alongside the NVIDIA / Physical Intelligence / Hugging Face entries. It scores **86.8** avg on LIBERO ([VLA-0 paper](../sources/vla-0-paper.md), Table I), placing it **below** [VLA-0](vla-0.md) (94.7, no pretraining), [π0](pi-zero.md) (94.2), and [GR00T-N1](nvidia-groot.md) (93.9) but above plain [OpenVLA](openvla.md) (76.5) and [Octo](octo.md) (75.1) — i.e. a mid-pack discrete-token pretrained VLA. Its distinguishing pitch is **explicit spatial/action reasoning** (reasoning in space, not just emitting actions), which is why the [VLA-0](vla-0.md) authors group it with the discrete-token family while noting its reasoning framing.

> [!note] Primary source not yet ingested
> This page is grounded in the [VLA-0 paper](../sources/vla-0-paper.md)'s LIBERO comparison; the MolmoAct paper (arXiv 2508.07917) and its Molmo backbone are **not yet ingested**. Deepen (architecture, the "reason in space" mechanism, pretraining corpus, real-robot results) when the primary lands. **Molmo** (Allen Institute open VLM) also has no wiki entity yet.

## Reported numbers (from ingested sources)

- **LIBERO** ([VLA-0 paper](../sources/vla-0-paper.md), Table I): **86.8** avg (Spatial 87.0 / Object 95.4 / Goal 87.6 / Long 77.2), with large-scale action pretraining; rank 6.5.

## Related

- [VLA-0](vla-0.md) — the action-as-text VLA that surpasses MolmoAct on LIBERO without any action pretraining.
- [OpenVLA](openvla.md) — the other open-weights discrete-token VLA baseline.
- [VLA models](../concepts/learning/vla-models.md) — action-head taxonomy (discrete-token family).

## Open questions

- **Primary source (arXiv 2508.07917) + Molmo backbone not ingested** — needed for the "reason in space" mechanism, depth/spatial-token design, and pretraining details.
- Is MolmoAct's spatial-reasoning framing an [embodied chain-of-thought](../concepts/learning/chain-of-thought.md) instance? Worth checking against the wiki's CoT thread when the paper is filed.

## Mentioned in

- [VLA-0 paper](../sources/vla-0-paper.md) — MolmoAct as a discrete-token, action-pretrained LIBERO baseline.
