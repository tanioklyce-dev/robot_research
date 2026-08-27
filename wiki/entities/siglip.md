---
title: SigLIP
type: entity
subtype: model
created: 2026-08-26
updated: 2026-08-26
sources: 3
tags: [siglip, vision-encoder, vlm-backbone, sigmoid-loss, clip, paligemma, smolvlm, eagle, groot, frozen-encoder]
---

**SigLIP** — Google's **sigmoid-loss** contrastive image–text encoder ([arXiv 2303.15343](https://arxiv.org/abs/2303.15343)), the CLIP successor that replaced the softmax-over-the-batch objective with a **pairwise sigmoid loss**, decoupling the loss from batch size. In this wiki it appears almost entirely as a *component*: the vision half of the VLM backbones that VLAs are built on.

> [!note] Filed as a hub for a component the wiki depends on without ever documenting
> No ingested source page is *about* SigLIP; it is named inside a dozen others as the encoder that some other model uses. This page collects those mentions and, more usefully, collects the **two independent 2026 results measuring how it performs for control** — which is the thing the wiki actually needs from it and had scattered across two source pages.

## Where it sits in the wiki's model stack

| Model | Role of SigLIP |
|---|---|
| [PaliGemma](paligemma.md) | Vision encoder; the backbone [π0](pi-zero.md) is initialized from |
| [SmolVLM](smolvlm.md) / SmolVLM-2 | Vision encoder (~0.4B total = SigLIP + SmolLM2), backbone of [SmolVLA](smolvla.md) |
| [Eagle 2.5](../sources/eagle-2-5-paper.md) | **Drops** Eagle-1's mixture-of-encoders design for a **single SigLIP-so400M** plus long-context machinery — the VLM backbone of [GR00T N1.5](../sources/groot-n1_5.md) |
| [OpenVLA-OFT](openvla.md) | Fuses **[DINOv2](dinov2.md) + SigLIP** patch features |

The pattern is worth naming: SigLIP is the **default semantic vision encoder** of the 2025–26 VLA generation, usually paired with a language decoder and often paired with a *second*, geometry-oriented encoder (DINOv2) — which is itself a hint about what it does and does not provide.

## The control result: strong semantics, weak action structure

Two independent 2026 measurements, from different directions, reach the same verdict.

**1. Action-relevant latents.** [Are Video World Model Latents Action-Relevant?](../sources/action-relevant-latents-paper.md) probes eight encoder families for how much action information their frozen features carry (inverse-dynamics probe, LIBERO, task-OOD split):

| Family | Encoder | Params | Frozen action R² | After ID tuning |
|---|---|---:|---:|---:|
| Latent prediction | [V-JEPA 2](v-jepa-2.md) | — | — | **0.85** |
| Image SSL | Web-DINO ViT-L | 304M | −0.01 | 0.16 |
| **Image SSL** | **SigLIP 2 ViT-L** | 316M | **0.05** | **0.17** |

> [!warning] The limitation is representational, not a tuning problem
> SigLIP 2 and Web-DINO "stay at 0.16–0.17 after ID tuning, clustered with reconstruction encoders, and a λ sweep across five orders of magnitude leaves them in a 0.1-wide band — *the limitation is representational rather than optimization-related.*"
>
> And the failure localizes: **rotation**. Translation and gripper state are recoverable from relatively weak features, but "Web-DINO and SigLIP produce **negative** rotation R² even after ID supervision." Rotation is "the dimension requiring physically coherent latent dynamics," and a language-image contrastive objective has no reason to preserve it.

**2. As a policy backbone.** [Patch Policy](patch-policy.md) sweeps five frozen encoders as dense-feature sources for behavior-cloned policies and finds **SigLIP 2 falls short across the environments**, with an explanation that matches the finding above: its "emphasis on semantic language-image alignment **sacrifices the dense geometric features necessary for manipulation**." For tasks prioritizing spatial reasoning over linguistic understanding, vision-language grounding is "a less effective signal for policy learning."

**The synthesis the wiki can now state:** SigLIP is an excellent *semantic* encoder and a poor *geometric* one, and manipulation needs the second. That explains the architectural pattern above — why VLAs that care about contact pair it with DINOv2 rather than using it alone, and why the strongest results for control come from encoders trained on **temporal** or **dense** objectives rather than image–text alignment.

## Open questions

- **No primary ingested.** Everything here is second-hand from pages about other models. The SigLIP and SigLIP 2 papers are unfiled, so the sigmoid-loss mechanism, training scale, and the SigLIP→SigLIP 2 delta are undocumented.
- **SigLIP vs SigLIP 2 is not disambiguated in the wiki's own claims.** The negative control results are specifically **SigLIP 2 ViT-L**; the backbone roles above are mostly **SigLIP** / **SigLIP-so400M**. Whether the control finding transfers backwards is untested.
- **The pairing hypothesis is inferred, not sourced.** No ingested source says "we pair SigLIP with DINOv2 because SigLIP lacks geometry" — the wiki is reading that off the architectures plus the probe results.

## Related

- [PaliGemma](paligemma.md) / [SmolVLM](smolvlm.md) / [Eagle VLM](eagle-vlm.md) — the backbones it sits inside.
- [DINOv2](dinov2.md) / [DINOv3](dinov3.md) — the geometry-oriented encoders it is paired with, and beaten by, for control.
- [V-JEPA 2](v-jepa-2.md) — the latent-prediction alternative that dominates on action R².
- [Patch Policy](patch-policy.md) — the frozen-backbone comparison.
- [VLA models](../concepts/learning/vla-models.md) — the class that consumes it.

## Mentioned in

> [!note] No source page is *about* SigLIP
> It is named as a component inside these; the claims above are sourced inline.

- [Are Video World Model Latents Action-Relevant?](../sources/action-relevant-latents-paper.md) — the action-R² probe.
- [Patch Policy paper](../sources/patch-policy-paper.md) — frozen-backbone sweep.
- [Eagle 2.5 paper](../sources/eagle-2-5-paper.md) — single SigLIP-so400M backbone.
- [FLARE paper](../sources/flare-paper.md), [TurboVLA paper](../sources/turbovla-paper.md), [DreamGen paper](../sources/dreamgen-paper.md), [Latent-space robotic world models](../sources/latent-space-robotic-world-models-paper.md) — component mentions.
