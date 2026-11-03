---
title: "Scaling Transformer Energy-Based Models For High Quality Image Synthesis (TEM) (Lee, Gladstone, Du, 2026)"
type: source
url: https://arxiv.org/abs/2610.31889
fetch_url: https://arxiv.org/pdf/2610.31889v1
local_path: raw/2610.31889v1.pdf
sha256: a42db0a85b520a5bb688414285557348732f1db15daa9000dfccc07604f7114c
author: Jungsoo Lee (MIT), Alexi Gladstone (UIUC), Yilun Du (Harvard)
published: 2026-10-22
ingested: 2026-11-02
venue: arXiv (cs.LG), v1 preprint
format: "paper, 19 pp. Project: int-lee.github.io/scalable-ebm (not inspected). Code: github.com/int-lee/TEM (README read 2026-11-02; no license file found at the default path)."
tags: [tem, energy-based-model, ebm, contrastive, langevin, mcmc, replay-buffer, image-generation, imagenet, dinov2, representation-alignment, compositional-generation, ood-detection, yilun-du]
---

# Scaling Transformer Energy-Based Models For High Quality Image Synthesis (TEM)

## Summary

**TEM** is a contrastively trained [energy-based model](../concepts/learning/energy-based-models.md) that generates class-conditional ImageNet at 256×256 and 512×512 with no diffusion trajectory and no classifier-free guidance. A transformer outputs a scalar energy over Stable Diffusion VAE latents, and Langevin MCMC both supplies the training negatives and generates the samples. TEM-XL (609M parameters) reports **FID-50K 3.82 at 256×256 and 8.24 at 512×512**, which the authors believe are the best large-scale results for a contrastive EBM using its own MCMC negatives. The paper's three additions are multi-layer energy heads, **Positive Representation Alignment (PRA)** against DINOv2, and inference-time sampling control. Its importance for this wiki is the claim it tests: [Dawid & LeCun](dawid-lecun-lvebm-lecture-notes.md) argue that contrastive methods scale too badly to matter, and this is a contrastive EBM at a scale the wiki's earlier EBMs never reached. The result narrows that claim without overturning it (see [What this does to the scaling argument](#what-this-does-to-the-scaling-argument)).

## Key claims

**Architecture (§3.1)**
- A transformer with rotary position embeddings, query-key normalization, SwiGLU and AdaLN-style conditioning. No spectral normalization or other EBM-specific stabilizer is required.
- **Multi-layer energy extraction:** with `k` heads on `L` layers, heads attach near `L/k, 2L/k, …, L`, and training uses the sum of their energies. The paper presents this as composition inside one model, which previously took several separately trained models.

**Training (§3.2, App. B–C)**
- The EBM works entirely in the frozen Stable Diffusion VAE latent space: 32×32×4 at 256px.
- `L_total = L_contrast + λ1·L_sampler-match + λ2·L_PRA`. The contrastive term includes an L2 penalty on energy magnitude to resolve the "gauge freedom" of energies that only matter relatively. The sampler-matching term is a KL-motivated regularizer with a nearest-neighbour entropy estimate.
- **PRA** maximizes patch-wise cosine similarity between projected EBM features and **DINOv2-large** features, on **positive samples only**. In the ablation (TEM-B at 50K steps), FID is **19.9 with PRA, 36.6 aligning positives and negatives, 42.8 with no alignment**.
- Negatives come from 40 Langevin steps with a replay buffer (replay probability 0.99, capacity 16,000). Step size is 500 and noise scale 0.05, deliberately decoupled from the standard Langevin prescription and chosen empirically.
- **Cost:** TEM-XL takes about 6 days on 4 H200 GPUs for 50K steps at 256×256; 512×512 takes 3–4× longer. Sampling 50K images at 60 steps takes about an hour on one H200. Training compute is reported as 146 E FLOPs for TEM-XL (50K steps, 12.8M images seen) against 393 E for SiT + REPA and 638 E for DiT and SiT.

**Results (Table 1, Table 4; baselines as reported in their original papers, not rerun)**

| Model | Params | NFE | FID, no guidance | FID, CFG |
|---|---|---|---|---|
| TEM-L | 415M | 60 | 4.74 | – |
| **TEM-XL** | 609M | 60 | **3.82** | – |
| DiT-XL/2 | 675M | 250 | 9.62 | 2.27 |
| SiT-XL/2 | 675M | 250 | 8.3 | 2.06 |
| SiT-XL/2 + REPA | 675M | 250 | 5.9 | 1.42 |
| GigaGAN | 569M | 1 | 3.45 | – |

- **Sample steps trade fidelity against diversity, and FID is not monotonic:** 40 steps gives FID 7.63, 60 gives 3.82, 80 gives 4.72. Precision rises 0.65 → 0.76 → 0.81 while recall falls 0.65 → 0.57 → 0.51. The authors compare this curve to classifier-free guidance, obtained without any unconditional network evaluations.
- **Compositional generation:** on CLEVR 256×256, object detection success for 1/2/3-object compositions is **0.956 / 0.766 / 0.274** against Composable Diffusion's 0.863 / 0.598 / 0.262.
- **OOD detection from one forward pass:** average AUROC **0.717** across four benchmarks against 0.598 (DiT), 0.573 (SiT) and 0.549 (SiT-REPA). It is not a clean sweep: DiT beats it on Places365, 0.669 vs 0.636.
- **Inpainting** needs no retraining: sample the masked latent region and reset observed latents after each step.
- **Stated limitations (§6):** iterative sampling is costly in training and inference, and longer chains sharpen images while reducing diversity.

## Reading the numbers

> [!warning] "60 NFE vs 250" and "outperforms unguided diffusion" need qualifying
> These caveats are this wiki's reading, not the authors'.
> - **Persistent chains.** Per the [repo's](https://github.com/int-lee/TEM) evaluation protocol, once the buffer fills, chains start from buffered states rather than fresh noise. A reported sample may therefore descend from far more than 60 updates. The paper's App. C does correct for one bias, that each Langevin step costs about 2F: it reports 14.48T FLOPs per sample for TEM-XL against 29.66T for unguided DiT and SiT. But that accounting charges 60 steps per sample and does not count the chain history inherited from the buffer, so the 2× saving is an upper bound on what a fresh-from-noise sampler would see. Accelerated diffusion solvers would also narrow it, as the authors note.
> - **The fair baseline uses the same crutch.** TEM trains with DINOv2 alignment, so the like-for-like unguided comparison is SiT + REPA (5.9), not bare SiT (8.3). TEM still wins, by less.
> - **60 steps is the FID-best point on TEM's curve.** At the 40-step training horizon, FID is 7.63.
> - **Guided diffusion remains well ahead on FID** (1.42 vs 3.82). The paper's own Table 4 shows DiT reaching 3.22 at a guidance scale of just 1.25.

## What this does to the scaling argument

[Dawid & LeCun](dawid-lecun-lvebm-lecture-notes.md) assert that generating contrastive points has *"bad (even exponential!) scaling with the data dimension."* TEM is evidence against the strong form, with limits on how far it reaches. This section is the wiki's interpretation:

- **The dimension is reduced first.** The sampler runs in a 4,096-dimensional VAE latent, not pixel space, so the VAE has already absorbed much of the problem.
- **The supervision is not purely contrastive.** PRA roughly halves FID in the TEM-B ablation, and its target, DINOv2, is a self-supervised joint-embedding model. The authors' stated reason is that contrastive training alone gives only a scalar signal per sample. That partly supports the regularized camp's position even as the result challenges it.
- **The task is different.** LeCun's argument concerns learning world-model representations. TEM shows image generation works, and says nothing about whether the method beats regularized joint embedding for prediction or planning.

## Entities mentioned

- [DINOv2](../entities/dinov2.md): the representation alignment target.
- Yilun Du, Alexi Gladstone and Jungsoo Lee have no entity pages. Du and Gladstone appear elsewhere in the wiki on [DreamZero](dreamzero-paper.md) and [TDV](tdv-paper.md) respectively.

## Concepts touched

- [Energy-based models](../concepts/learning/energy-based-models.md)
- [IBC](../entities/ibc.md) (the robot-policy EBM that hit the scaling and negative-sampling problem)

## Open questions

- **Does the recipe rescue EBM policies?** [IBC](ibc-paper.md) was overtaken by denoising methods partly because of its negative-sampling cost. Replay-buffer MCMC, multi-head energies and alignment to a vision model could all transfer, but nothing here tests an action space, and robot control has latency limits that an hour per 50K images does not address.
- **Is energy useful as a robot anomaly signal?** A scalar energy gives one-pass OOD scoring, yet an average AUROC of 0.717 is far from deployable, and the benchmarks are ImageNet-versus-other-datasets rather than policy-relevant distribution shift.
- **How independent is 3.82?** There is no third-party rerun in the wiki, and the repo currently offers a 256×256 checkpoint only.
- **What happens without the VAE and DINOv2?** The paper has no pixel-space run and no test of an unaligned TEM at XL scale.

## See also

- [AI Search news roundup, 2026-11-01](ai-search-news-2026-11-01.md): the video through which this paper entered the wiki.
