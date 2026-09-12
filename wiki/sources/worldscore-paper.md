---
title: WorldScore — A Unified Evaluation Benchmark for World Generation (Duan, Yu, Chen, Li, Wu; arXiv 2025)
type: source
url: https://arxiv.org/abs/2504.00983
fetch_url: https://arxiv.org/pdf/2504.00983v2
author: Haoyi Duan, Hong-Xing Yu, Sirui Chen, Li Fei-Fei, Jiajun Wu (Stanford University)
published: 2025-04-01
ingested: 2026-09-11
venue: arXiv v2 (2025-11-29), cs.GR — no venue stated in the PDF
local_path: raw/2504.00983v2.pdf
sha256: 7ddf259570f4b302f44650329fd24ab331a19e218adf538b47019218fb235d06
format: pdf (8 pp. + 7 pp. supplement, 7 figures, 2 tables + 7 supplementary tables)
tags: [worldscore, benchmark, world-generation, world-model-evaluation, video-generation, 3d-scene-generation, 4d-generation, camera-control, controllability, 3d-consistency, human-preference, stanford, fei-fei-li, jiajun-wu, wonderworld, cogvideox, vbench]
---

## Summary

The benchmark the [HAI brief](hai-world-model-spatial-intelligence-brief.md) lists as "controllability, quality, and dynamics in world generation," read in the primary. Duan, Yu, Chen, [Fei-Fei Li](../entities/fei-fei-li.md) and [Jiajun Wu](../entities/jiajun-wu.md) argue that single-scene video benchmarks such as VBench cannot see whether a model builds a *world*: Figure 1 shows two models VBench rates 80.28 ≈ 83.06 that WorldScore separates 70.70 vs 46.28, because the second never generates the next scene or follows the camera instruction. Their fix is to **decompose world generation into a chain of next-scene generation tasks**, each a triplet of (current scene image + prompt, next-scene prompt, layout) where the layout is a ground-truth **camera trajectory** plus its text description. Because every model is asked to produce a *video* along that trajectory, **3D scene generators, a 4D generator, image-to-video and text-to-video models are scored on one leaderboard** — the first benchmark to do so, by the authors' Table 1. The dataset is **3,000 world specifications** (2,000 static, 1,000 dynamic; half photorealistic, half stylized); the metric is **10 automated sub-metrics** in three families, validated by a 400-participant 2AFC study. Over 20 models the findings are that **3D models dominate static world generation** (WonderWorld 72.69, LucidDreamer 70.40 vs the best video model, CogVideoX-I2V, at 62.15), that **video models cannot follow a camera** (best 40.22 against 84.60–94.01 for every 3D model), and that the best open-source video model beats both closed-source ones (Gen-3, Hailuo). What WorldScore does *not* measure is as important for this wiki as what it does: there is no physical-law metric, no object interaction, no action beyond the camera, and no utility test — it is a control-and-consistency benchmark for renderers, and the top model on its own leaderboard was built by three of its five authors.

## Key claims

### The framing (§1, §3.1)

- "World generation" = "the creation of large-scale, diverse worlds with various scenes," with applications in "entertainment, education, simulation, and embodied AI." Existing benchmarks (TC-Bench, EvalCrafter, FETV, VBench, T2V-CompBench, ChronoMagic-Bench, WorldModelBench) are single-scene, have no camera specification or reference image, and so are "incompatible with many state-of-the-art 3D/4D scene generation methods that require an image or a camera trajectory as inputs" (Table 1).
- Task step = (C, N, L): C = {image I, prompt P}; N = next-scene prompt; L = {camera trajectory T = (C₁…C_N), camera text Y}. Output V = g_world(w_proc(C, N, L)), where w_proc is a model-specific pre-processor (Supp. A): 3D/4D models receive the **camera matrices**; video models receive only the **camera text** appended to the prompt; T2V models are "treated as I2V models that ignore image-based control signals."
- Two task types, deliberately separated: **static world generation** (new scene contents + large camera moves, scored for controllability and quality) and **dynamic world generation** (same scene, in-scene motion, camera fixed, scored for dynamics).

### The dataset (§3.2, Supp. B, Table S4)

- **3,000 examples: 2,000 static + 1,000 dynamic.** Static: 5 indoor categories (dining, living, passage, public, work) × 5 outdoor (city, suburb, aquatic, terrestrial, verdant) × 100 images = 1,000 photorealistic, each with a stylized counterpart. Dynamic: 5 motion types (articulated, deformable, fluid, rigid, multi-motion) × 100, plus stylized counterparts.
- Photorealistic images sourced from 11 scene datasets (Matterport3D, Hypersim, SUN-RGBD, DIODE, ETH3D, LHQ, EDEN, Argoverse-HD, InteriorVerse) and Unsplash; filtered on quality (CLIP-IQA, CLIP Aesthetic), perspective (Perspective Fields — extreme roll/pitch and narrow FOV removed), CLIPSIM similarity, brightness, and a final manual pass, from **~5,000 candidates to the top 100 per category**. GPT-4o writes captions and does the 10-way classification.
- **7 styles** (anime, cyberpunk, Chinese ink, ukiyo-e, impressionism, post-impressionism, Minecraft), rendered by a commercial style-controlled T2I model (Recraft).
- Next-scene prompts are generated **autoregressively by GPT-4o** ("generate a scene description different from the past scenes"), 1–3 named entities per scene. **20% of static examples are "large worlds"** (three new scenes, four total); the rest are one-step "small worlds."
- **8 camera movements** "widely used in movie industry": push in, pull out, orbit left/right, move left/right, pan left/right — chosen to cover all directions and to match the language video models saw in training.

### The ten metrics (§3.3, Supp. C)

| Family | Metric | How it is computed |
|---|---|---|
| Controllability | Camera controllability | DROID-SLAM recovers per-frame poses; error = √(e_θ · e_t), rotation error in degrees × scale-invariant translation error vs the ground-truth trajectory |
| | Object controllability | Grounding DINO detection success rate for the 1–2 entities in N |
| | Content alignment | CLIPScore against the whole prompt N (objects are "only ≈¼ of the prompt length") |
| Quality | 3D consistency | DROID-SLAM dense reprojection error between co-visible pixels in consecutive frames — geometry, "regardless of slight changes in visual textures" |
| | Photometric consistency | Forward-then-backward optical flow; Average End-Point Error of the round trip. Motivated by the claim that CLIP/DINO consistency metrics "focus on categorical identity but fail to capture fine-grained texture changes" |
| | Style consistency | Frobenius distance between Gram matrices of first and last frame |
| | Subjective quality | Arithmetic mean of CLIP-IQA+ and CLIP Aesthetic — the combination that best matched the human study |
| Dynamics | Motion accuracy | max flow inside the SAM2-tracked motion mask minus max flow outside it (SEA-RAFT flow); outside flow "cancels out the global motion caused by unintended camera movements" |
| | Motion magnitude | Median optical-flow magnitude per frame pair |
| | Motion smoothness | Drop odd frames, re-interpolate with VFIMamba, MSE/SSIM/LPIPS against the dropped frames |

- **WorldScore-Static** = arithmetic mean of the 7 controllability + quality scores. **WorldScore-Dynamic** = mean of all 10. "For 3D scene generation models that do not support dynamic tasks, we assign 0 to each dynamics metric."
- **Normalization (Supp. C.8–C.9).** Each raw metric is linearly mapped to 0–100 between empirical bounds. Camera controllability's worst bound is a **fixed-camera sequence** ("penalizes … generation that fails to exhibit any camera movement"); the three consistency metrics' worst bound is a frame-interpolated video between two random dataset images; motion smoothness's worst bound is bilinear interpolation of OpenVid-1M clips. For **content alignment, subjective quality, motion accuracy and motion magnitude**, "defining appropriate empirical bounds is challenging," so bounds are set by **z-score rescaling so that the evaluated models fall within 25–75** — these four scores are relative to the cohort, not absolute.

### Human validation (§4, Supp. D)

- **400 participants**, 2AFC on video pairs from five models (CogVideoX-I2V, VideoCrafter1-I2V, DynamiCrafter, WonderJourney, InvisibleStitch), a single question — "which video has higher quality" — because a preliminary study found raters "often struggle to differentiate between specific dimensions" of quality.
- Table S5, agreement with the human majority: CLIP-IQA+ & CLIP Aesthetic **0.637**, best of 11 candidates; CLIP Aesthetic alone 0.628; the upper bound (a metric that always agrees with the majority) is **0.772**.
- Table S6, other metrics, comparing score buckets 30 points apart (60±5 over 30±5; 90±5 over 60±5): camera controllability **71.2% / 73.5%**, object controllability 96.3% / 87.7%, 3D consistency 91.7% / 97.3%, photometric consistency 91.6% / 95.1%, motion magnitude 91.8% / 76.2%. Content alignment, style consistency, motion accuracy and motion smoothness do not appear in the table.
- Resolution robustness: EasyAnimate at 1344×768 vs center-cropped 256×256 — every metric differs by **≤ 0.83** (Table S7).

### Results — Table 2 (20 models)

Selected columns; WS-S = WorldScore-Static, WS-D = WorldScore-Dynamic, Cam = camera controllability, 3D = 3D consistency, Subj = subjective quality, MAcc/MMag/MSm = motion accuracy / magnitude / smoothness.

| Model | WS-S | WS-D | Cam | 3D | Subj | MAcc | MMag | MSm |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Gen-3 (closed, I2V) | 60.71 | 57.58 | 29.47 | 68.31 | 63.85 | 54.53 | 27.48 | 68.87 |
| Hailuo (closed, I2V) | 57.55 | 56.36 | 22.39 | 67.18 | 52.44 | 63.46 | 27.20 | 70.07 |
| DynamiCrafter | 52.09 | 47.19 | 25.15 | 72.90 | 54.40 | 41.11 | 39.25 | 26.92 |
| VideoCrafter1-T2V | 47.10 | 43.54 | 21.61 | 64.86 | 42.63 | 11.76 | 75.00 | 18.87 |
| VideoCrafter1-I2V | 50.47 | 47.64 | 25.46 | 74.42 | 54.85 | 55.63 | 25.00 | 42.49 |
| VideoCrafter2 | 52.57 | 47.49 | 28.92 | 65.14 | 56.74 | 47.12 | 30.40 | 29.39 |
| T2V-Turbo | 45.65 | 40.20 | 27.80 | 38.72 | 68.74 | 34.87 | 40.09 | 7.48 |
| EasyAnimate | 52.85 | 51.65 | 26.72 | 67.29 | 50.31 | 75.00 | 31.16 | 40.32 |
| Allegro | 55.31 | 51.97 | 24.84 | 70.50 | 47.41 | 54.39 | 40.28 | 37.81 |
| Vchitect-2.0 | 42.28 | 38.47 | 26.55 | 41.53 | 44.58 | 33.59 | 33.81 | 21.31 |
| LTX-Video | 55.44 | 56.54 | 25.06 | 78.41 | 49.08 | 76.22 | 29.95 | 71.09 |
| CogVideoX-T2V | 54.18 | 48.79 | **40.22** | 68.81 | 44.67 | 25.00 | 47.31 | 36.28 |
| CogVideoX-I2V | **62.15** | **59.12** | 38.27 | 86.21 | 62.44 | 69.56 | 26.42 | 60.15 |
| SceneScape (3D) | 50.73 | 35.51 | 84.99 | 76.54 | 32.75 | 0 | 0 | 0 |
| Text2Room (3D) | 62.10 | 43.47 | 94.01 | 88.71 | 36.69 | 0 | 0 | 0 |
| LucidDreamer (3D) | 70.40 | 49.28 | 88.93 | 90.37 | 58.99 | 0 | 0 | 0 |
| WonderJourney (3D) | 63.75 | 44.63 | 84.60 | 80.60 | 66.56 | 0 | 0 | 0 |
| InvisibleStitch (3D) | 61.12 | 42.78 | 93.20 | 88.51 | 58.50 | 0 | 0 | 0 |
| **WonderWorld (3D)** | **72.69** | 50.88 | 92.98 | 86.87 | 49.81 | 0 | 0 | 0 |
| 4D-fy (4D) | 27.98 | 32.10 | 69.92 | 35.47 | 0.89 | 22.22 | 22.88 | 80.06 |

The paper's six observations (§4.1):

1. **3D models excel in static world generation** — WonderWorld 72.69 and LucidDreamer 70.40 "much better than the best video model CogVideoX-I2V (62.15)," attributed to inherent camera controllability, hence better content alignment "due to the larger space they can create," plus high 3D and photometric consistency. They "do not allow for the generation of dynamic worlds"; the one 4D model, 4D-fy, "does not perform well, likely due to the intrinsic difficulty in 4D scene generation."
2. **Video models lack camera controllability** — the best, CogVideoX-T2V at 40.22, "scored much lower than any 3D/4D generation model." Named as "the main challenge for video generation models," with camera-conditioning work (CameraCtrl, MotionCtrl) as the suggested remedy.
3. **The best open-source video model is as good as the closed-source ones** — CogVideoX-I2V beats Gen-3 and Hailuo on both aggregates, though not per axis: better camera controllability, worse object controllability and content alignment.
4. **Motion magnitude trades against smoothness** — "larger motion often comes at the cost of lower smoothness."
5. **Magnitude does not buy accuracy** — "the correlation between the motion magnitude and accuracy is weak"; large-motion models "could hallucinate unintended camera motion or irrelevant motion."
6. **Video models are weak on long sequences and outdoors** (Figure 7): they "struggle significantly" on large-world (four-scene) tasks and are "significantly weaker than 3D models in outdoor scenes, while the gap is smaller in indoor scenes." Also: **T2V models are easier to steer than I2V** — higher controllability and motion magnitude, lower quality — because "T2V models are willing to generate larger camera motion, while I2V models tend to stick to the input image viewpoint."

Compute (Table S1): all runs on H100/L40S; WonderWorld ≈ 10 s per instance versus 2–16 min for most video models; 4D-fy ≈ 3 h per instance *after* the authors cut its iteration count from a native ~20 h.

### Stated limitations and conclusion (§5)

The conclusion names the open problems as "bridging the gap between 3D and 4D representations, developing more robust controllability mechanisms, and designing architectures capable of handling extended scene sequences." There is no limitations section for the *benchmark itself*; the caveats below (cohort-relative bounds, zero-filled dynamics, interface asymmetry) are the wiki's reading, not the authors'.

> [!note] Small internal inconsistency in the model count
> §1 describes the 13 video models as "6 image-to-video models (with 2 leading closed-source models), 7 text-to-video models"; §4 and Table S1 have 9 I2V (2 closed + 7 open) and 4 T2V. Table S1 additionally lists VideoCrafter2 as T2V where §4 counts it among the open I2V models. The total of 20 is consistent throughout; the I2V/T2V split is not.

## Reading it against the wiki

> [!note] The closed loop, now read in the primary
> [World-model evaluation](../concepts/world-models/world-model-evaluation.md) and the [Jiajun Wu](../entities/jiajun-wu.md) page flag that the HAI brief's "no adequate benchmark" verdict cites a benchmark two of its own authors wrote, and the [backlog](../backlog.md) asked whether WorldScore's own framing supports or undercuts the brief. **It supports it.** WorldScore's ten metrics contain nothing about physical law, object permanence, contact, or what happens when an agent acts: the only "action" is a camera trajectory, "dynamics" means *where and how much* optical flow appears, and the paper never claims otherwise — its stated use cases lead with entertainment and education, and "embodied AI" is named once in the introduction and never tested. The brief's characterization ("controllability, quality, and dynamics in world generation") is accurate to the word.
> The loop is tighter than the wiki had it, though. The model that tops WorldScore-Static, **WonderWorld (72.69), is by Yu, Duan, Herrmann, Freeman and Wu**, and the fourth-place WonderJourney (63.75) is by Yu, Duan, … Wu as well — the benchmark's first two authors and its senior author built the winning entry. Nothing in the paper discloses this, and the human study draws one of its five models (WonderJourney) from the same group. That is not evidence of anything improper — WonderWorld is a strong system, and the metrics are open — but it is the kind of provenance the wiki's [policy-vs-evidence](../syntheses/society/world-model-policy-vs-wiki-evidence.md) synthesis should carry. Add that Li's [World Labs](../entities/world-labs.md) ships [Marble](../entities/marble.md), a commercial 3D world generator in exactly the category WorldScore ranks 3D models first in.

- **Where it sits on the progression.** The evaluation page's line "VBench → VideoPhy/PhyGenBench → WorldScore/WorldModelBench → WorldArena runs from *how it looks* toward *what it is good for*" needs one correction: WorldScore is not further along a *physics* axis than VideoPhy — it has no physics axis at all. It is further along a **control** axis: does the model go where it is told, show what it is told, and keep geometry and texture stable while doing so. In the [functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md)'s terms it is a **renderer** benchmark, and a good one; it says nothing about the simulator or planner roles the taxonomy calls consequential.
- **Camera controllability is partly an interface measurement.** 3D/4D models receive the ground-truth camera matrices and render along them; video models receive the sentence "camera moves left." DROID-SLAM then recovers the pose track and compares it to the same ground truth. For a 3D model the metric asks whether SLAM can recover a trajectory the renderer was *given*; for a video model it asks whether the model inferred it from text. The 84–94 vs ≤ 40 gap is real, but it is a gap in *input modality* as much as in capability — which the paper concedes by pointing to camera-conditioned video models as the fix.
- **WorldScore-Dynamic penalizes not attempting.** 3D models get 0 on all three dynamics metrics, so their Dynamic score is exactly 0.7 × Static (WonderWorld 72.69 → 50.88). CogVideoX-I2V's headline "59.12, best overall" is therefore a ranking in which the strongest static generators forfeit three of ten axes. Quote WorldScore-Static for renderers and WorldScore-Dynamic for video models; the combined leaderboard mixes the two.
- **Four of ten scores are cohort-relative.** Content alignment, subjective quality, motion accuracy and motion magnitude are z-scored so the evaluated models land in 25–75. A new model added to the leaderboard can move existing models' scores on those axes, and a WorldScore number quoted from a later leaderboard snapshot is not comparable to Table 2 without checking the cohort. This is the [drift-check](../../CLAUDE.md) problem in metric form.
- **The human validation is real but coarse — and it is a validation of preference, not of failure detection.** [Physion-Eval](physion-eval-paper.md) asks whether automated critics *see the glitches humans see*; WorldScore asks whether a **30-point score gap** agrees with which of two videos 400 raters think looks better, on **one question**, for five of the ten metrics. Camera controllability, the metric the paper's headline finding rests on, is the weakest at 71–74% agreement. Subjective quality's 0.637 agreement sits against a 0.772 ceiling. This is better than most rows in the evaluation page's table, which have no validation at all, but it does not touch the Physion-Eval objection that fine-grained physical violations are invisible to flow- and CLIP-based metrics — because WorldScore does not try to detect them.
- **Motion magnitude vs smoothness** is the [perception-distortion tradeoff](../concepts/world-models/perception-distortion-tradeoff.md) wearing different clothes: smoothness is scored against a frame-interpolator's reconstruction (a distortion metric that rewards the conditional mean), magnitude rewards leaving it. A model can max either by construction — VideoCrafter1-T2V scores 75.00 magnitude / 18.87 smoothness; T2V-Turbo 7.48 smoothness. The authors report the trade-off without naming the mechanism.
- **PAN's "WorldScore consistency" is now legible.** The [PAN report](pan-world-model-paper.md) scores its Long-horizon Forecast with "WorldScore consistency metrics with late-step penalties"; those are the DROID-SLAM reprojection error, the forward-backward flow AEPE, and the Gram-matrix style distance above — all appearance-stability measures, none of them action-conditioned.
- **For the robotics reader.** Compare the three *ingested* world-model benchmarks. [WorldArena](worldarena-paper.md) asks whether a world model is useful as data engine, evaluator, or planner; [WorldRoamBench](worldroambench-paper.md) scores per-frame *action* fidelity and gates physics on it; WorldScore scores a camera path and a motion mask. Its 3,000 specifications and open metrics make it the cheapest of the three to run, and its 3D-consistency and photometric metrics are worth borrowing as regression tests for any generative renderer in a [real-to-sim](../entities/world-labs.md) pipeline. It is not a test of whether the world behaves.

## Entities mentioned

- [Fei-Fei Li](../entities/fei-fei-li.md), [Jiajun Wu](../entities/jiajun-wu.md) — senior authors; Haoyi Duan, Hong-Xing Yu (equal first), Sirui Chen (Stanford; no pages). Duan is also first author on [WorldArena 2.0](worldarena-2-paper.md).
- [World Labs](../entities/world-labs.md) / [Marble](../entities/marble.md) — not mentioned in the paper; the commercial 3D world generator from the senior author's company, in the category the benchmark ranks first.
- [Stanford HAI](../entities/stanford-hai.md) — not the paper's affiliation (Stanford University), but the publisher of the [brief](hai-world-model-spatial-intelligence-brief.md) that cites this benchmark.
- Evaluated models, none with pages: Runway Gen-3, MiniMax Hailuo (closed); DynamiCrafter, VideoCrafter1/2, T2V-Turbo, EasyAnimate, Allegro, Vchitect-2.0, LTX-Video, CogVideoX (open video); SceneScape, Text2Room, LucidDreamer, WonderJourney, InvisibleStitch, WonderWorld (3D); 4D-fy (4D).
- Cited but not evaluated: [Cosmos](../entities/nvidia-cosmos.md) (as a video generator), [OpenAI](../entities/openai.md)'s Sora ("video generation models as world simulators"), Luma Dream Machine.
- Tooling: DROID-SLAM, Grounding DINO, SAM2, SEA-RAFT, VFIMamba, CLIP-IQA+, CLIP Aesthetic, GPT-4o, Recraft (no pages).

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the "not ingested" row is now filled; the progression sentence and the closed-loop note both need the corrections above.
- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) — WorldScore is squarely in the generative-video tradition (automated metrics, human 2AFC as validation, no human *baseline*); it does not test physical understanding on either tradition's terms.
- [World-model functional taxonomy](../concepts/world-models/world-model-functional-taxonomy.md) — a renderer benchmark by the taxonomy's own authors' group, published fourteen months before the taxonomy.
- [Perception-distortion tradeoff](../concepts/world-models/perception-distortion-tradeoff.md) — the magnitude/smoothness trade-off.
- [Spatial intelligence](../concepts/world-models/spatial-intelligence.md), [world model](../concepts/world-models/world-model.md) — the framing WorldScore predates; note that its "world" is a chain of camera-navigable scenes, not an environment that responds to action.

## Open questions

- Does a WorldScore-Static score predict anything downstream — e.g. policy performance in a [R2S2R](world-labs-r2s2r.md) pipeline built on the same renderer? Nothing in the paper or the wiki correlates it with a utility measure the way WorldArena correlates EWMScore with planning (r = 0.360).
- How do camera-conditioned video models (CameraCtrl, MotionCtrl, and the 2025–26 generation of models with explicit pose input) score? If the 3D-vs-video gap closes when the interface is equalized, observation 2 was about inputs, not architectures. The live leaderboard may already answer this; the paper does not.
- Are the four cohort-relative metrics re-normalized when the leaderboard grows? If so, Table 2's numbers are already stale for those columns.
- Why were content alignment, style consistency, motion accuracy and motion smoothness left out of the Table S6 human check?
- The paper is cs.GR and its stated audience is graphics; the HAI brief cites it to policymakers as evidence about world models for "safety-critical deployment." The paper never uses those words. Which reading did the brief's authors intend?
