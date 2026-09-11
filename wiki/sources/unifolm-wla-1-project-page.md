---
title: UnifoLM-WLA-1.0 — project page, README and model cards (Unitree Robotics)
type: source
url: https://unigen-x.github.io/unifolm-wla.github.io/
author: Unitree Robotics
published: 2026-09-11
ingested: 2026-09-11
format: web (project page + GitHub README + two HF model cards; no paper)
local_path: raw/2026-09-11-unifolm-wla-1-project-page.md
sha256: 37d10747ae4a76dd30ea2b2bd716141561c558bd0d76f8fd063fd9cf5deb7738
license: CC BY-NC-SA 4.0
tags: [unifolm, unitree, unitree-g1, vla, humanoid, embodied-reasoning, world-action-model, qwen3-vl, rvq, action-tokenization, dynamic-region-prediction, flow-matching, mmdit, whole-body-manipulation, dexterous-hands, china, open-weights, non-commercial]
---

## Summary

[Unitree](../entities/unitree.md)'s launch page for **UnifoLM-WLA-1.0**, billed as a "general-purpose humanoid robot foundation model" of **6B parameters**, trained on **≈2,500 hours** of real-robot data, driving **64 tasks** (10 whole-body, 54 tabletop) on a [Unitree G1](../entities/unitree-g1.md) with one set of weights, across two-finger grippers and several five-finger hands. The stack is three stages, each a separate artifact: **UnifoLM-ER-1** (a [Qwen3-VL](../entities/qwen.md)-4B fine-tuned on 5M+ embodied-reasoning samples) → **UnifoLM-ER-Flow** (the same VLM taught to emit discrete *future dynamic-region* mask tokens and residual-VQ action tokens) → **UnifoLM-WLA-1.0** (ER-Flow plus an MMDiT [flow-matching](../concepts/learning/flow-matching.md) action expert behind a stop-gradient). It is the third generation of the [UnifoLM](../entities/unifolm.md) line, after the video-generating WMA-0 world model (Sep 2025) and the VLA-Base checkpoints (Jan 2026).

> [!warning] What was actually released on 2026-09-11 — and what was not
> The README's open-source plan is explicit. **Released:** the two 4.4B ER checkpoints (`UnifoLM-ER-1`, `UnifoLM-ER-Flow`) and the 32-task **UniBot-V1 Challenge Dataset**. **Not released (unchecked boxes):** the **6B WLA-1.0 policy itself**, the post-training code, and the two larger datasets (Unitree-WBT, Unitree-Manipulation). There is no paper, no per-task success rate, no baseline, and no held-out protocol on the page — the 64-task claim is supported by demo videos only. Everything quantitative on the page is about the **ER backbone**, and that is what this source page can vouch for.
>
> The weights and repo are **CC BY-NC-SA 4.0** — non-commercial, share-alike. "Open source" in the video title means open *weights for research*, not the Apache/MIT-class licensing of [MolmoAct2](../entities/molmoact2.md) or [GR00T](../entities/nvidia-groot.md)'s code.

## Key claims

### Stage 1 — UnifoLM-ER-1 (embodied-reasoning VLM)

- **Base and data.** Built on **Qwen3-VL-4B**; trained on **>5M samples** across six task families — image point prediction, object detection, multi-image reasoning, 2D trajectory prediction, 3D object detection, multi-image spatial QA — **co-trained with general image–text data** "preserving broad vision-language capabilities." (HF `config.json` architecture: `Qwen3VLForConditionalGeneration`; 4.44B parameters per the HF API.)
- **Headline.** "Across 16 multimodal perception and understanding benchmarks, UnifoLM-ER-1 leads open-source models on seven and delivers overall performance comparable to leading proprietary models."
- **The seven wins** (best open-weight column, from the card's bolding): RefSpatial-Bench 61.7, Where2Place **82.0**, Pixmo-Point 73.8, BLINK 93.4†, EmbSpatial 88.9, RoboSpatial 73.1, VSR 88.1. Where2Place and EmbSpatial are best *overall*, proprietary included.
- **Where it loses to open models:** RoboVQA (62.4 vs Thinker-4B 62.7), Ego-Plan2 (55.1 vs 63.7), CV-Bench (88.6 vs Hy-Embodied-VLM 89.7), SAT (76.0 vs Cosmos-R1 82.7), **VSI-Bench (54.2 vs [Molmo2-ER](../entities/molmo2-er.md) 74.5)**, ERQA (50.0 vs Hy-Embodied-VLM 60.8), RealWorldQA, MME, MMMU.

> [!warning] The table contradicts its own "preserves general capability" sentence
> Against its own base **Qwen3-VL-4B**, ER-1 is *lower* on every general-VLM column the card reports: **MME 2223 vs 2325, MMMU-val 54.7 vs 57.8, RealWorldQA 69.8 vs 71.0** — and on **VSI-Bench 54.2 vs 59.3**. The embodied gains are large (Where2Place +19, Pixmo-Point +25.5, RefSpatial +15) but the co-training did not hold the general benchmarks flat, which is the specific thing the text claims. The VSI-Bench drop is the more interesting one: VSI is *video* spatial reasoning, and the ER-1 training mix is entirely image / multi-image — the base model's video competence appears to have been traded away. Compare [Molmo2-ER](../entities/molmo2-er.md)'s explicit rehearse stage, whose stated purpose is exactly this regression.

> [!note] Mixed provenance — the rows are not one experiment
> Twenty-three models × 16 benchmarks, but by the card's own footnotes: `*` rows are copied from other papers' reports (different harnesses, prompts, and in some cases benchmark versions), `‡` rows are Unitree's own API tests of proprietary models, and BLINK (`†`) is Unitree's own testing **restricted to two subtasks** (Relative Depth, Spatial Relation) for every model. Only the BLINK column and the ER-1 row are Unitree's measurements throughout. No confidence intervals anywhere. Treat gaps under ~3 points as noise, per the wiki's [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) discipline — which removes RoboVQA and CV-Bench from either side's ledger.

- **Vs Molmo2-ER-4B on the 8 shared columns:** ER-1 leads on 6 (RefSpatial +9.2, Where2Place +28, BLINK +7.7, CV-Bench +0.8, EmbSpatial +10.1, ERQA +3.2) and trails on 2 (SAT −2.0, **VSI-Bench −20.3**). Both are 4B-class; the wiki's Molmo2-ER page reports Ai2's own 13-benchmark average of 63.8 — this table does not compute an average, so the two headline claims are not directly comparable. Pixmo-Point — Ai2's signature pointing benchmark — is blank in the Molmo2-ER row.
- **Frontier proprietary rows** (Unitree's API tests): the models it names as GPT-6-Astra (RefSpatial 79.6, ERQA 77.7) and Gemini 3.1 Pro (RefSpatial 70.0, ERQA 65.2) remain well ahead on referring-expression and ERQA; ER-1 beats them on Where2Place, Pixmo-Point, EmbSpatial, RoboSpatial and VSR. "Comparable to leading proprietary models" is true per column and false on ERQA by 27 points.

### Stage 2 — UnifoLM-ER-Flow (world modeling + discrete actions inside the VLM)

- **Dynamic-region prediction.** Compute **optical flow** between frames *t₀* and *t₁*, threshold it into a **dynamic-region mask**, train a **VQ-VAE** to encode the mask into a fixed-length sequence of discrete tokens; the VLM, conditioned on the current image plus either a task description *or* an action, predicts the **future mask tokens**. Stated purpose: "focusing on interaction subjects and the scene changes they induce to enable interaction-centric world modeling." Demos: clean table, fold towel, package phone, place plates.
- **Discrete action learning.** The unified action space is **partitioned into three components — end-effector poses, end-effector joints (gripper / dexterous hand), lower-body joints —** each with its **own residual vector-quantization (RVQ) model**; token streams share timesteps and are fed synchronously, delimited by `<EEF_START>…<EEF_END>`, `<HAND_START>…<HAND_END>`, `<LOWER_START>…<LOWER_END>`.
- **Six aligned signals** in one VLM (model-card table): image tokens, language-or-action condition, future-region mask tokens, EEF tokens, hand tokens, lower-body tokens. ER-Flow is 4.45B parameters — the ER-1 vocabulary extended, not a new backbone.

### Stage 3 — UnifoLM-WLA-1.0 (the policy)

- **Architecture (from the page's live-graph diagram).** ER-Flow backbone → **stop-gradient** → **MMDiT flow-matching action expert** taking VLM hidden states, an **embodiment embedding**, robot state, and noised actions; blocks are adaLN-style (scale-and-shift, gate, RoPE, QK-norm), i.e. the [π0.5](../entities/pi-zero-5.md) / [Knowledge Insulation](../concepts/learning/knowledge-insulation.md) pattern: discrete tokens train the backbone, a continuous expert acts, gradients from the expert do not reach the VLM.
- **Data.** ≈2,500 h "high-quality real-robot data" including the **Unitree Open Datasets** and **BitRobot-HIW-500** (Humanoids-in-the-Wild, 500 h; BitRobot Foundation), "covering diverse robot embodiments," unified through a shared action space for **cross-embodiment prior transfer**. Co-trained with embodied-reasoning and general VLM data; "all robots, tasks and end effectors share the same model parameters."
- **Evaluation shown.** 10 whole-body manipulation tasks and 54 tabletop tasks on the G1, as video carousels. Supports "two-finger grippers and multiple five-finger dexterous hands." No numbers, no failure cases, no inference rate or hardware.
- **Dataset released.** UniBot-V1 Challenge Dataset = **32** HF datasets named `G1_Dex1_<Task>` (HangCup, ArrangePlates, PlugCharger, SyringeWaterTransfer, FoldTowel, PackPhone, Unlock, DisconnectEthernet …) — presumably a subset of the 54 tabletop tasks, on the Dex1 gripper.

### Lineage (HF org listing, cross-checked against the WMA-0 page)

| Date | Artifact | What it was |
|---|---|---|
| 2025-09-09/15 | `UnifoLM-WMA-0-Base` / `-Dual` | **World-Model-Action**: a video-generation model fine-tuned on Open-X, run in a *decision-making* mode (predict future interaction to help the action head) or a *simulation* mode (render outcomes of actions) |
| 2026-01-28 | `UnifoLM-VLM-Base`, `UnifoLM-VLA-Base`, `UnifoLM-VLA-Libero` | a conventional VLA generation (not documented on this page) |
| 2026-05 | `UnifoLM_WBT_Dataset` collection (14 items) | whole-body teleoperation data |
| 2026-09-11 | `UnifoLM-ER-1`, `UnifoLM-ER-Flow`; WLA-1.0 announced | this page |

The design shift from WMA-0 to WLA-1.0 is the substantive story: **the "world" component was demoted from a pixel-space video generator to a sparse, discrete prediction of *where the scene will change*, living inside the VLM's token stream.** WMA-0 now has its own [source page](unifolm-wma-0-project-page.md). See the [world-action model](../concepts/world-models/world-action-model.md) page for how that sits against mimic-video's "no video at inference" finding and GR00T N1.5's FLARE loss.

## Entities mentioned

- [Unitree](../entities/unitree.md) — publisher; [Unitree G1](../entities/unitree-g1.md) — the only robot shown.
- [UnifoLM](../entities/unifolm.md) — the model family (new entity).
- [Qwen](../entities/qwen.md) — Qwen3-VL-4B is the backbone.
- [Molmo2-ER](../entities/molmo2-er.md), [NVIDIA Cosmos](../entities/nvidia-cosmos.md) (Cosmos-R1-7B, Cosmos3-Super-64B rows), [Gemini Robotics](../entities/gemini-robotics.md) (Gemini-ER 1.5 / 2 rows), [AGIBOT](../entities/agibot.md) (GenieReasoner-3B row, unconfirmed attribution) — comparison rows.
- [Physical Intelligence](../entities/physical-intelligence.md) — the architecture is the π0.5/KI recipe, uncredited.

## Concepts touched

- [Embodied-reasoning VLMs](../concepts/learning/embodied-reasoning-vlms.md) — new concept page; this table is the wiki's widest single comparison of the class.
- [World-action model](../concepts/world-models/world-action-model.md) — the mask-token "sparse world target."
- [VLA models](../concepts/learning/vla-models.md), [Knowledge Insulation](../concepts/learning/knowledge-insulation.md), [flow matching](../concepts/learning/flow-matching.md).
- [Latent action tokens](../concepts/learning/latent-action-tokens.md) — contrast: these RVQ tokens are discretized *robot* actions per body-part group, not a cross-embodiment latent.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — lower-body tokens make the policy whole-body by construction; how the VLA's lower-body outputs meet the G1's balance controller is not described.
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md).

## Open questions

- **Does WLA-1.0 exist as a checkpoint anyone outside Unitree has run?** Until the policy and post-train code ship, the 64-task / cross-end-effector claims are marketing-tier. Watch the README's plan checkboxes.
- **Does the mask-token objective actually help the policy?** No ablation of ER-Flow vs ER-1 as a backbone is given — the one number that would justify the "W".
- **What does the lower-body token stream drive?** A 6B VLM cannot close a balance loop; presumably it emits targets for a whole-body controller, but the page is silent. *Partial answer (2026-09-11):* [HIW-500](../entities/hiw-500.md), one of WLA's named datasets, records actions as a 23-D WBC command — base velocity/pose/height plus EE poses and grippers — so that is the likely token content.
- **Control rate and compute.** Nothing. The wiki's [control-rate ladder](../syntheses/platforms/control-rate-ladder.md) cannot place it.
- ~~BitRobot-HIW-500~~ — ingested 2026-09-11 as [HIW-500](../entities/hiw-500.md) ([page](bitrobot-hiw-500-dataset-page.md)); the Unitree "open datasets" as a corpus remain unlisted.
- **The Molmo2-ER VSI-Bench gap.** If video spatial reasoning is what an embodied VLM most needs for manipulation-over-time, ER-1 optimized the wrong columns. The two recipes (co-train vs specialize-then-rehearse) are now directly comparable at 4B on 8 benchmarks — a cheap study.
