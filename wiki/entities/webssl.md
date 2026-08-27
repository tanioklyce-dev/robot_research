---
title: WebSSL / Web-DINO
type: entity
subtype: model
created: 2026-08-26
updated: 2026-08-26
sources: 4
tags: [webssl, web-dino, vision-encoder, self-supervised, language-free, metaclip, scaling, frozen-encoder, robot-learning, lecun, meta-fair]
---

**Web-SSL** — a family of **language-free** visual SSL encoders from FAIR Meta + NYU, **1B to 7B parameters**, trained on **2 billion MetaCLIP web images** (MC-2B) ([paper](../sources/webssl-paper.md), Fan, Tong, …, [LeCun](yann-lecun.md), Bar, Xie; April 2025). Its DINOv2-style member is **Web-DINO**. The thesis: visual SSL only looked worse than CLIP because the two were trained on different data — control for that, and SSL scales *better* and **does not saturate at 7B**.

> [!warning] Web-SSL and Web-DINO are the same family, and the wiki was carrying opposite verdicts on them
> Under the name **WebSSL**, [Patch Policy](patch-policy.md) makes it a **co-winner** of a five-encoder sweep and recommends it for robot learning.
>
> Under the name **Web-DINO**, [action-relevant latents](../sources/action-relevant-latents-paper.md) measures it at **0.16 action R²** after inverse-dynamics tuning — clustered with pixel-reconstruction encoders, **negative on rotation**, and immovable under a λ sweep across five orders of magnitude ("the limitation is representational rather than optimization-related").
>
> **Both are true, and the reconciliation is what the two are measuring.** Patch Policy asks *do frozen patch tokens make a good input to a behavior-cloned policy* — a **feature-quality** question, answered on tasks where the demonstrations supply the dynamics. Action-relevant latents asks *can action be linearly decoded from the representation itself* — a **world-model** question, where the encoder must carry the dynamics. **Web-SSL is a strong perception front-end and a weak dynamics substrate**, and it is trained on still images, so there is no mechanism by which it would be otherwise.
>
> Practical consequence, and the reason this identity matters: **the encoder Patch Policy recommends for policies is one of the worst measured choices for a latent world model.** Anyone carrying the recommendation from one context to the other inherits a rotation collapse.

## What the primary establishes

- **The controlled question**: *"Do visual self-supervised approaches lag behind CLIP due to the lack of language supervision, or differences in the training data?"* Both arms trained on MC-2B; VQA inside an MLLM (Llama-3 8B Instruct held fixed) as the testbed.
- **Visual SSL matches or surpasses CLIP on VQA — including OCR & Chart**, the category assumed to need language.
- **No saturation at 7B parameters**; scales well in both capacity and data.
- **Classic vision stays competitive while VQA improves** — no trade-off.
- **Web-DINO matches SigLIP and [SigLIP 2](siglip-2.md) on VQA at 5× less data**, and beats off-the-shelf MetaCLIP on both VQA and classic vision.
- **Data composition matters**: a higher ratio of text-containing images is especially effective for OCR & Chart.
- **The real cost of dropping language**: no zero-shot classification out of the box. Recovered via instruction tuning inside an MLLM; LiT-style adaptation named and declared out of scope.

## As a robot-learning backbone

[Patch Policy](patch-policy.md) freezes five encoders as dense patch-feature sources across four simulated suites, 3 seeds — **DINOv2, DINOv3, WebSSL, [V-JEPA 2](v-jepa-2.md), [SigLIP 2](siglip-2.md)** — and finds **WebSSL and [DINOv2](dinov2.md) win**, recommending them explicitly. WebSSL carries that paper's headline table, reaching **1.68 / 1.68** on BlockPush and Cube where the same policy on globally-pooled features scores 0.23–0.25.

Two claims from that sweep make backbone choice consequential: the **ranking is stable across policy architectures** ("visual representation quality is still a primary bottleneck for policy learning, independent of the downstream action head"), and the **language-supervised encoder is the weakest of the five** — WebSSL winning is the positive half of the same finding.

> [!note] Scope on the recommendation
> One paper, visual input only, no language axis, no confidence intervals, in-domain tasks. And **the paper itself contains no control evaluation at all** — every WebSSL claim in the primary is VQA or classic vision. "Best frozen backbone for robot learning" is one comparison's finding.

## Open questions

- **Which variant?** The family spans 1B–7B and more than one objective; neither [Patch Policy](patch-policy.md) nor the wiki records which checkpoint was used.
- **Is Web-DINO's rotation collapse a property of the family or of the DINO objective?** Only the DINO member was probed for action-relevance.
- **In-domain vs frozen web-scale is untested at low demo counts** — see [DynaMo](dynamo.md), which argues for training your own encoder on 6 demonstrations.
- Licence and checkpoint availability are not recorded here.

## Related

- [Patch Policy](patch-policy.md) — the robot-learning sweep and recommendation.
- [DINOv2](dinov2.md) / [DINOv3](dinov3.md) — co-recommended and sibling encoders.
- [SigLIP](siglip.md) / [SigLIP 2](siglip-2.md) — the language-supervised comparison it matches at 5× less data.
- [V-JEPA 2](v-jepa-2.md) — the video-pretrained encoder that dominates on action R² and loses as a frozen policy backbone.
- [DynaMo](dynamo.md) — the in-domain alternative to using a frozen web encoder at all.
- [DINO-WM](dino-wm.md) — builds a world model on frozen image-SSL features, the design the Web-DINO result bears on.

## Mentioned in

- [Scaling Language-Free Visual Representation Learning](../sources/webssl-paper.md) — **the primary.**
- [Patch Policy paper](../sources/patch-policy-paper.md) — best frozen backbone for robot learning.
- [Are Video World Model Latents Action-Relevant?](../sources/action-relevant-latents-paper.md) — Web-DINO at 0.16 action R², negative on rotation.
- [Reconstruction or Semantics?](../sources/latent-space-robotic-world-models-paper.md) — Web-DINO **strong** as a diffusion-world-model latent space (IDM Pearson r = 0.820 vs V-JEPA 2.1's 0.829); the counterweight to the result above.
