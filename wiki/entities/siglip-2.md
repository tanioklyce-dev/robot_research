---
title: SigLIP 2
type: entity
subtype: model
created: 2026-08-26
updated: 2026-08-26
sources: 5
tags: [siglip-2, vision-encoder, vlm-backbone, language-supervised, action-relevance, frozen-encoder, groot, molmo]
---

**SigLIP 2** — the second generation of Google's sigmoid-loss image–text encoder ([SigLIP](siglip.md)). Filed separately because the wiki's evidence is **specifically about SigLIP 2**, not about the family: every control measurement here names the 2 variant, and the claims should not be silently back-propagated to SigLIP 1.

## Where it is used

| System | Role |
|---|---|
| [GR00T N1](nvidia-groot.md) | Eagle-2 VLM = **SmolLM2 + SigLIP-2** (System 2, 10 Hz) |
| [Molmo2 / Molmo2-ER](molmo2-er.md) | **SigLIP2 ViT** → connector → LLM, in the [Molmo](molmo.md) lineage |
| [Patch Policy](patch-policy.md) | One of five frozen encoders swept as policy backbones |

## The control evidence — and it does not point one way

This is the part worth having a separate page for. Three ingested sources measure SigLIP 2 for control and **they disagree**.

**Weak (1): action decodability.** [Are Video World Model Latents Action-Relevant?](../sources/action-relevant-latents-paper.md) probes eight encoder families with a shared inverse-dynamics head on LIBERO, task-OOD split:

| Family | Encoder | Params | Frozen action R² | After ID tuning |
|---|---|---:|---:|---:|
| Latent prediction | [V-JEPA 2](v-jepa-2.md) | — | — | **0.85** |
| Image SSL | [Web-DINO](webssl.md) ViT-L | 304M | −0.01 | 0.16 |
| **Image SSL** | **SigLIP 2 ViT-L** | 316M | **0.05** | **0.17** |

It stays clustered with pixel-reconstruction encoders, goes **negative on rotation** even after ID supervision, and a λ sweep across five orders of magnitude leaves it in a 0.1-wide band — *"the limitation is representational rather than optimization-related."*

**Weak (2): as a policy backbone.** [Patch Policy](patch-policy.md) finds **SigLIP 2 falls short across the environments**, with a mechanistic explanation: its "emphasis on semantic language-image alignment **sacrifices the dense geometric features necessary for manipulation**."

> [!warning] Strong, on a different axis: [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md)
> Evaluated as the **latent space of a diffusion world model on real Bridge V2 data**, **SigLIP 2 posts the best generated-latent success-classifier accuracy** of the encoders tested, and the "semantic" group it belongs to **beats every reconstruction encoder**.
>
> The wiki records this as an [open contradiction](../concepts/world-models/jepa.md) with candidate reconciliations, none verified: **Pearson r vs R²** (r ignores the scale and bias errors R² punishes); **spatial patch latents vs mean-pooled features**; **real Bridge V2 vs simulated LIBERO task-OOD**; and **aggregation over 7 DoF masking a rotation-specific collapse**.
>
> The safe reading: SigLIP 2 is a poor substrate for **decoding actions** and a decent one for **judging whether a generated rollout succeeded** — which are different jobs, and only the first is what a planner needs.

## Relationship to SigLIP 1

**Undocumented in this wiki**, and that is the main gap. Neither the SigLIP nor the SigLIP 2 primary is ingested, so the architectural delta, training scale, and whether the control findings transfer backwards are all unknown. The wiki's *backbone-role* claims mostly name **SigLIP** or **SigLIP-so400M**; its *control* claims name **SigLIP 2**. Do not merge them.

One indirect datapoint: [Web-DINO matches SigLIP and SigLIP 2 on VQA while seeing 5× less data](../sources/webssl-paper.md) — a language-free encoder reaching parity on the language-adjacent benchmark.

## Open questions

- **No primary ingested** for either SigLIP generation.
- **Does the rotation collapse hold for SigLIP 1?** Untested; it is the version inside most of the VLA backbones the wiki tracks.
- **The Bridge V2 vs LIBERO disagreement is unresolved** and matters for [DINO-WM](dino-wm.md)-style designs built on frozen image-SSL features.

## Related

- [SigLIP](siglip.md) — the family page and the backbone roles.
- [WebSSL / Web-DINO](webssl.md) — the language-free encoder measured alongside it, with the same rotation collapse and the same contradiction.
- [V-JEPA 2](v-jepa-2.md) — the video-pretrained encoder that dominates on action R².
- [Patch Policy](patch-policy.md) / [DINO-WM](dino-wm.md) / [GR00T](nvidia-groot.md) / [Molmo2-ER](molmo2-er.md).

## Mentioned in

- [Are Video World Model Latents Action-Relevant?](../sources/action-relevant-latents-paper.md) — 0.17 action R², negative rotation.
- [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md) — best generated-latent success-classifier accuracy.
- [Patch Policy paper](../sources/patch-policy-paper.md) — weakest of five frozen policy backbones.
- [Scaling Language-Free Visual Representation Learning](../sources/webssl-paper.md) — matched on VQA by a language-free encoder at 5× less data.
- [GR00T N1 paper](../sources/groot-n1-paper.md) — Eagle-2 VLM = SmolLM2 + SigLIP-2.
