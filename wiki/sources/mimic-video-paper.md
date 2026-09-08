---
title: "mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs (Pai et al., 2025)"
type: source
url: https://arxiv.org/abs/2512.15692
fetch_url: https://arxiv.org/pdf/2512.15692v2
local_path: raw/2512.15692v2.pdf
sha256: a7d2d3fa9367921bde900889e862025afa1e28e93437f287aa018b3b17e39658
author: "Jonas Pai, Liam Achenbach, Victoriano Montesinos, Benedek Forrai (core contributors), Oier Mees, Elvis Nava (co-advising) — mimic robotics; Microsoft Zurich; ETH Zurich; ETH AI Center; UC Berkeley"
published: 2025-12-17
venue: "arXiv preprint (v1 2025-12-17; **v2 2025-12-19**, the version read here — revised intro, related work, appendix). 15 pp. Project page: mimic-video.github.io"
format: paper (PDF + arXiv HTML)
tags: [mimic-video, video-action-model, vam, cosmos-predict2, flow-matching, inverse-dynamics, frozen-backbone, sample-efficiency, partial-denoising, libero, simpler, dexterous-manipulation, mimic-robotics]
ingested: 2026-09-07
---

## Summary

**The architecture behind [FLUX-mimic](flux-3-launch.md), and the paper that names the class.** A **Video-Action Model (VAM)** pairs a **pretrained, frozen video-diffusion backbone** with a **flow-matching action decoder** that cross-attends to the backbone's *intermediate* representations and acts as an **inverse dynamics model**. Reported: state of the art on simulated and real dexterous manipulation, **10× sample efficiency** and **2× convergence speed** against an architecturally matched VLA.

The argument against VLAs is stated as a claim about what pretraining data contains, not about model quality:

> While vision-language pretraining effectively captures semantic priors, **it remains blind to physical causality.** … the policy must implicitly infer complex physical dynamics and temporal dependencies solely from robot trajectories. This reliance creates an **unsustainable data burden**.

Ingested to settle a question the wiki opened this afternoon: **does mimic's system use force or tactile sensing?**

> [!warning] The answer is no — and the question is only half-settled
> The observation is stated formally as `oₜ = [I_{t−H+1}, …, Iₜ, l, qₜ]` — **RGB images, a language instruction, and proprioceptive state**. The real-world rig is *"a global workspace view, four wrist cameras, and full proprioception."* **There is no force/torque sensing, no tactile sensing, no impedance and no compliance anywhere in this paper**, on a bimanual setup with **16-DoF dexterous hands**.
>
> **But this paper's real-world tasks are not the Audi tasks.** Its evaluations are **Package Sorting** (pick, handover, place) and **Tape Stowing** (pick, stow, move box) — pick-and-place and handover, which are *not* [contact-rich](../concepts/robotics/contact-rich-manipulation.md) under the survey's definition. The ECU insertion and seal/cable handling reported at Audi appear **only in Black Forest Labs' blog**, on a **different backbone** (FLUX 3, not Cosmos-Predict2), with **no paper**.
>
> So: **mimic's published system is vision-plus-proprioception, and it has not been published doing a contact-rich task.** The tension recorded on [contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) narrows but does not close — and it now has a specific missing document rather than a general doubt.

> [!note] Terminology drift, second instance this week
> The paper writes *"to validate mimic-video on high-dimensional, **contact-rich** tasks"* for a bimanual pick-handover-place. Under [the survey's §2.1](safe-learning-contact-rich-survey.md), contacts fixed after the grasp are explicitly excluded. Here "contact-rich" means *many contacts, dexterous hands, heavy occlusion*; there it means *motion and force coupled through sustained contact*. Same word, different partition — as with [semantic safety](../concepts/safety/semantic-safety.md).

## The architecture

**Backbone: [NVIDIA Cosmos-Predict2](../entities/nvidia-cosmos.md)** — an open-source **2B latent DiT** over 3D-tokenized video; each layer alternates self-attention over the video sequence, cross-attention to T5-encoded language, and an MLP. Input is 5 clean context frames plus noisy future latents.

**Two coupled flow-matching models with independent flow schedules** (τ_v for video, τ_a for actions):
- **Video model** `v_φ(z⁰_past, z^{τ_v}_future, l, τ_v)` — LoRA-finetuned on robot video, then **frozen**.
- **Action decoder** `π_θ(A^{τ_a}, qₜ, h^{τ_v}, τ_a, τ_v)` — a DiT trained from scratch; each layer cross-attends to `h^{τ_v}`, the hidden states **after the k-th layer of the video model**, then self-attends over the action sequence. Proprioception is encoded as a token and **randomly replaced with a learned mask token during training** to prevent overfitting on the low-dimensional observation.

**Partial denoising is the key move.** Prior video-conditioned policies must *generate the future frames* to recover the policy — *"necessitating prohibitive video synthesis at every control step."* Here the video flow is integrated only to an intermediate τ_v, and the *intermediate activations* condition the decoder. No pixels are ever produced at inference.

The framing of what this buys: it *"decouples the inherent multi-modality of long-horizon planning, now offloaded to the video backbone, from the downstream control task,"* freeing the decoder for *"the far simpler, unimodal and non-causal problem of inverse dynamics."*

## The two results that matter most

**1. Oracle study — control reduces to prediction.** Condition the decoder on **ground-truth future video latents** instead of predicted ones:

> Conditioning on oracle latents yields **near perfect success rates regardless of whether the underlying backbone is finetuned** on the target distribution… **control effectively reduces to visual prediction, implying policy performance scales directly with video model quality.**

That is the strongest available statement of the video-model thesis, and it is also a **bound on it**: it says that for these tasks, everything control needs is present in the visual future. Whether that survives into tight-tolerance insertion is precisely what is untested.

**2. You do not need the pixels — and more denoising makes it worse.**

- Best **autonomous policy** performance on SIMPLER is at **τ_v = 1**, i.e. **pure noise** — a single forward pass of the backbone, no video denoising at all. *"High-fidelity video reconstruction is not required for performant robot policies."*
- On **ground-truth** latents, action-reconstruction MSE is lowest at **τ_v ≈ 0.4** and **rises sharply toward τ_v = 0** (full reconstruction).
- Their explanation for the gap: fully denoised *predicted* latents carry generation artifacts and **fall out of the decoder's training distribution**, while the intermediate representations behave non-monotonically in their own right.

> [!note] This partly dissolves the generative-vs-JEPA cost argument
> The wiki's [comparison](../syntheses/world-models/generative-video-vs-jepa-world-models.md) rests on: a video generator *"has to commit to a specific RGB rendering of every imagined future; a JEPA only has to commit to an embedding,"* and most of the cost difference traces to that.
>
> **mimic-video generates no video at inference.** It runs a generative backbone at maximum noise as a **feature extractor**, and reports that the more you actually reconstruct, the worse control gets. So the deployed object is a generative model *used as a representation learner* — it pays the training cost of pixel supervision and **not** the inference cost of pixel generation.
>
> That is a third architecture the paradigm table does not have a row for, and it takes the sharpest edge off the cost objection to the generative side.

## Numbers

**SIMPLER-Bridge** (avg success %, all trained on BridgeDataV2):

| Model | Avg |
|---|---|
| OpenVLA (finetuned) | 14.6 |
| Octo (finetuned) | 16.0 |
| π₀.₅-style VLA (scratch) — **the matched baseline** | 35.4 |
| ThinkAct (pretrained) | 43.8 |
| FLOWER (finetuned) | 45.0 |
| **mimic-video (scratch)** | **46.9** |
| mimic-video (scratch, **per-task τ_v tuning**) | 56.3 |

**LIBERO** (Spatial / Object / Goal, avg): mimic-video (scratch) **93.9** vs π₀.₅-style (scratch) 85.9, DiT Policy 88.6, OpenVLA 84.1 — and **OpenVLA-OFT (finetuned) 96.9**, which it does not beat. Reported plainly.

**Real-world bimanual** (two Franka Panda + **mimic 16-DoF hands**; Packing / Package handover):

| Model | Packing | Handover |
|---|---|---|
| DiT-Block Policy | 11.0 | 30.0 |
| DiT-Block Policy **+ wrist cams** | 42.6 | 74.1 |
| **mimic-video** (workspace camera only) | **72.0** | **93.0** |

The occlusion claim rides on that last row: the baseline needs four wrist cameras to reach 42.6/74.1, and mimic-video beats it from **one workspace view** — attributed to the generative prior *"bridging the visual uncertainty caused by occlusion."* Relevant because occlusion-at-contact is exactly why the [contact-rich literature](../concepts/robotics/contact-rich-manipulation.md) calls insertion force-first.

**Sample efficiency, precisely.** The decoder reaches the VLM-conditioned decoder's *maximum* success rate on **10% of the training data**. At **one episode per task — a 98% reduction** — it still returns **77% average success**, competitive with the Diffusion Policy baseline. Convergence is also faster and to a higher asymptote, *"despite the VLA baseline having been exposed to task-specific action data during FAST-pretraining."*

**Data**: video backbone LoRA-finetuned on a **200-hour** robot video corpus; action decoders trained on **1h33m (512 episodes)** and **2h14m (480 episodes)**.

> [!note] The controlled baseline is unusually honest, and worth copying
> The π₀.₅-style comparison uses **PaliGemma-3B** with **an action decoder identical to mimic-video's**, the knowledge-insulation two-stage protocol, and *"training on perfectly equivalent datasets… ensur[ing] that performance differences in our comparisons stem strictly from the quality of the conditioning representations (video vs. image-text)."*
>
> This is the cleanest **video-backbone vs VLM-backbone** ablation available, and it is the reason the 10× claim is worth more than a headline number. Most VLA comparisons in this wiki change the backbone, the decoder, the data and the recipe at once.

## Where to hold it at arm's length

- **"Per-task τ_v tuning" (46.9 → 56.3) is a hyperparameter tuned per evaluation task**, presented as *"a novel form of inference-time policy optimization."* It is a real capability, and it is also not a clean number to compare against methods that tuned nothing per task. The scratch row is the honest one.
- **LIBERO carries the wiki's standing caveat** — [LIBERO-PRO](libero-pro-paper.md) reports >90% collapsing to 0.0% under perturbation, so a 93.9 there is partly a statement about the benchmark. The SIMPLER and real-robot numbers are the load-bearing ones.
- **No trial counts or confidence intervals** are given for the real-world table. SIMPLER numbers land on values like 4.2/8.3/12.5/29.2 (multiples of ~4.17), implying **24 trials per cell** — around ±20 pp by [Clopper-Pearson](../concepts/robotics/robot-policy-evaluation.md). The 72.0-vs-42.6 real-world gap is large enough to survive; the LIBERO ordering among the top three is not.
- **Stated limitations**: a **single-view** video backbone (so policies are locked to one fixed workspace view); **no unified cross-embodiment model** trained yet; and real-world experiments *"limited to a focused set of tasks."*

## Entities mentioned

- [mimic robotics](../entities/mimic-robotics.md) — the lab; **Oier Mees** (UC Berkeley) and **Elvis Nava** (ETH) co-advise. mimic's own **16-DoF hands** are the real-world platform.
- [NVIDIA Cosmos](../entities/nvidia-cosmos.md) — **Cosmos-Predict2** is the backbone. Third-party evidence for the "Cosmos as a substrate other people build policies on" thesis.
- [FLUX 3](../entities/flux-3.md) / [Black Forest Labs](../entities/black-forest-labs.md) — the successor swaps Cosmos-Predict2 for FLUX 3.
- [LIBERO](../entities/libero.md) · [SIMPLER](../entities/simplerenv.md) — the simulated benchmarks. Baselines named: OpenVLA, OpenVLA-OFT, Octo, ThinkAct, FLOWER, DiT-Block Policy, Diffusion Policy, π₀/π₀.₅, PaliGemma, FAST.

## Concepts touched

- [World-action model](../concepts/world-models/world-action-model.md) — VAM as a named class; the frozen-backbone, no-pixels-at-inference variant.
- [Generative-video vs JEPA world models](../syntheses/world-models/generative-video-vs-jepa-world-models.md) — **the τ_v result belongs here**: a generative backbone run as a feature extractor at maximum noise.
- [VLA models](../concepts/learning/vla-models.md) — the matched comparison against a π₀.₅-style VLA.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — the force question, half-answered.
- [Flow matching](../concepts/learning/flow-matching.md) · [imitation learning](../concepts/learning/imitation-learning.md) · [low-rank adaptation](../concepts/learning/low-rank-adaptation.md) — the machinery.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — trial counts, per-task tuning, LIBERO.

## Open questions

- **The capability question now has a data point, and it is not favourable.** [τ](tau-touch-augmented-vla-paper.md) measures a pretrained π0.5 at **20%** on plug insertion from vision + proprioception and **60%** with tactile, across four tasks that closely match FLUX-mimic's Audi list. This paper's system is vision + proprioception and never runs such a task; that one does, and finds the terminal contact stage is exactly where the vision-only policy fails.
- **What does the Audi system actually sense?** This paper answers for *its* system, not for the FLUX-mimic deployment — different backbone, harder tasks, no publication. Until there is one, "learned contact-rich manipulation from vision alone" stays a vendor claim.
- **Does the oracle result hold for insertion?** *Conditioning on ground-truth future video gives near-perfect control* is measured on pick-and-place. Insertion's decisive information — jamming, alignment, contact mode — is substantially **not visible**, which is the whole reason the classical literature is force-first. **This is the single experiment that would settle the force question**, and it is cheap: run the oracle study on a tight-clearance insertion task.
- **Why does more denoising hurt?** They attribute it to OOD conditioning plus non-monotonic intermediate representations, and defer to an appendix. If the mechanism is distribution shift, it is the same failure that drives [PACS](pacs-paper.md)'s path-consistency result — a policy conditioned on something outside its training distribution collapses — arriving in a completely different place.
- **What is the latency?** τ_v = 1 means one backbone forward pass, and the paper leans on that for "real-time," but publishes **no rate**. The 101 ms figure comes from BFL's blog for the FLUX-based successor. A number here would put Cosmos-Predict2-2B on the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).
- **Would a multi-view backbone remove the single-view limit at no cost?** Named as their top limitation, and it is the one that most obviously binds on a factory cell.
