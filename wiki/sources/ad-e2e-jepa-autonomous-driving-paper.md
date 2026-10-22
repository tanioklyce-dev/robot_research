---
title: "AD-E2E-JEPA: A Joint-Embedding Predictive Architecture for End-to-End Autonomous Driving (Zhu, Zhang, LeCun, Choromanska, 2026)"
type: source
url: https://arxiv.org/abs/2609.34085
local_path: raw/2609.34085v1.pdf
sha256: f925d3b0fa733ff7ad82b45b5a729c7d7d97792a44aac8b63f76af5160f0b1fd
author: Haoran Zhu, Wancong Zhang, Yann LeCun, Anna Choromanska
published: 2026-09-28
ingested: 2026-10-22
venue: arXiv (cs.RO), v1
format: "paper, 17 pp (9 main + references + appendices A.1–A.5). Affiliations: NYU, AMI Labs. Code: github.com/HaoranZhuExplorer/AD-E2E-JEPA (public; repo created 2026-09-29, contains a NAVSIM fork, the planning vocabulary and scripts; no checkpoints confirmed)."
tags: [ad-e2e-jepa, jepa, world-model, autonomous-driving, end-to-end-driving, navsim, epdms, leworldmodel, dino-wm, jepa-wms, dinov3, sigreg, projector, zero-shot-planning, goal-conditioned-planning, trajectory-vocabulary, imitation-learning, lecun, choromanska, ami-labs, nyu]
---

# AD-E2E-JEPA: A Joint-Embedding Predictive Architecture for End-to-End Autonomous Driving (Zhu, Zhang, LeCun, Choromanska, 2026)

## Summary

The paper takes the three action-conditioned JEPA world models the wiki tracks, [LeWorldModel](../entities/leworldmodel.md), [DINO-WM](../entities/dino-wm.md) and [JEPA-WMs](../entities/jepa-wms.md), and evaluates them on driving for the first time. All are retrained on **NAVSIM** front-camera video, with the action defined as the relative pose change (Δx, Δy, Δθ) between frames at 2 Hz. To keep world-model quality separate from policy learning, no driving policy is trained. The model is given the **ground-truth image 4 s ahead as the goal** and picks, from a fixed vocabulary of candidate trajectories, the one whose rolled-out latent lands closest to the goal's latent. The finding is a **speed/quality split**. LeWM (global CLS token) plans in 0.7 s but badly. DINO-WM and JEPA-WM (dense DINO patch tokens) plan well but take **92–101 s per scene**. The proposed fix keeps the JEPA-WM recipe (frozen DINOv3 ViT-L, AdaLN+RoPE predictor, optional multi-step rollout loss) and inserts a **learnable two-layer strided-conv projector** between encoder and predictor. The projector cuts the token count 16× and the width 4× (1024 → 256). A stop-gradient on the projected target and **[SIGReg](../concepts/world-models/sigreg.md) applied per patch location** keep the projected space from collapsing. Planning drops to **0.8 s per scene** and quality roughly matches the dense models. Two further results: scaling the candidate vocabulary to 8,192 trajectories raises EPDMS to **72.9** on the full test set, and the self-supervised projector, transplanted into a small imitation-learning driver, lifts it from **80.2 to 85.4 EPDMS** over a randomly initialised projector.

## Key claims

**Setup (§3.1–3.3, §4.1–4.2)**
- Front camera only. Context K+1 = **4 frames (2 s)**, horizon F = **8 frames (4 s)**, NAVSIM sampled at 2 Hz. Poses are expressed relative to the current ego pose; action a_t = relative pose change between consecutive frames (Eq. 3, following Epona).
- **Baseline world model** = the best JEPA-WMs configuration: **frozen DINOv3 ViT-L**, AdaLN predictor with RoPE, MSE loss only, **no anti-collapse term**, since targets come from the frozen encoder (Eqs. 4–6).
- **AD-E2E-JEPA projector** (Eq. 7): two conv layers with **stride 2×2**, applied to history and future frames alike. Spatial tokens ↓16×, D 1024 → 256. Motivated by [Temporal Straightening](temporal-straightening-paper.md), whose projector used stride 1×1 and only reduced width. The curvature regulariser from that paper is **not** used.
- **Collapse risk named explicitly** (§3.2.2): with a trainable projector on both branches, "distinct DINOv3 embeddings [can be] mapped to nearly constant vectors." Two defences: **stop-gradient on the projected target** (Eq. 9) and **SIGReg**.
- **SIGReg placement differs from LeWM** (Eq. 10). LeWM applies it to the global CLS embedding across the batch at each time step, then averages over time. AD-E2E-JEPA applies it **to each patch location at each time step, across the batch**, then averages over all locations and times. Epps–Pulley test, 17 knots on [0, 3], **M = 1,024** random directions (App. A.1). λ = 0.09 by default; **0.025** for the batch-512 trainval run, "tuned heuristically based on early training loss curves."
- **Rollout variant** (Eq. 12, App. A.2): a teacher-forcing loss over the 8-frame horizon plus autoregressive rollout losses L₂…L₈ with truncated BPTT (stop-gradient through the context before each predictor call, as in JEPA-WMs). SIGReg spans t−K to t+F.
- **Planner** (§3.3.1): **no CEM**, which the authors call too costly for driving. Instead an **exhaustive search over a fixed trajectory vocabulary**: the 8,192 clustered anchors from VADv2, sorted by angle and evenly subsampled to 256 by default. Cost = squared L2 between the rolled-out latent at t+F and the encoded goal frame I_{t+F} (Eqs. 13–14). All candidates are evaluated in parallel on one A100 80 GB.
- **Data**: `navtrain` (**10 h** of driving) for the head-to-head; the training portion of `trainval` (**70 h**) for AD-E2E-JEPA scaling.

**Compute (Table 1)**: LeWM 4×A100, **batch 8**, 1 d. DINO-WM 4×A100, batch 64, 11 h. JEPA-WM 4×A100, batch 64, 13 h. AD-E2E-JEPA **1×A100, batch 128, 20 h** (rollout: 1 d 22 h). Trainval runs: 4×A100, 2 d 5 h / 4 d 2 h. 30 epochs everywhere. **LeWM here uses a ViT-L encoder trained from scratch** (§4.2).

**Zero-shot planning (Table 2; per-submetric Tables 4–5)**

| Model (navtrain unless noted) | Scenes | EPDMS | EPDMS† | Time (s) | FDE (m) | Δθ (°) | Hit@1/@5 (%) |
|---|---|---|---|---|---|---|---|
| LeWM | 100 | 48.3 | 73.9 | **0.7** | 12.4 | 13.6 | 6 / 18 |
| DINO-WM | 100 | 68.3 | 91.4 | 91.8 | 3.9 | 5.9 | 40 / 73 |
| JEPA-WM | 100 | 74.2 | 90.9 | 101.0 | 4.0 | 5.2 | 45 / 75 |
| AD-E2E-JEPA | 100 | **76.6** | **92.4** | 0.8 | 4.2 | 4.7 | 27 / 59 |
| + rollout, trainval | 100 | 72.3 | 91.9 | 0.8 | **3.2** | 3.6 | **47 / 78** |
| LeWM | 12,146 | 39.8 | 66.7 | 0.7 | 14.6 | 17.2 | 5.7 / 11.3 |
| AD-E2E-JEPA | 12,146 | 63.5 | 80.1 | 0.8 | 6.3 | 6.3 | 32.9 / 65.3 |
| + rollout, trainval | 12,146 | 67.3 | 84.1 | 0.8 | 4.0 | 3.5 | **53.8 / 82.7** |
| + rollout, trainval, 8,192 traj. | 12,146 | **72.9** | **86.5** | 18.2 | **2.8** | **2.0** | 15.3 / 33.8 |

- **DINO-WM and JEPA-WM were evaluated on only 100 scenes**; the full 12,146-scene set would take "over 10 days" for them. The comparisons with the dense models therefore rest on 100 scenes. EC (extended comfort) is dropped on that subset because it has no temporally adjacent scenes.
- **Speedup**: 0.8 s vs 91.8 / 101.0 s, about 115–126×. The paper rounds it to "100×." The abstract's "0.8 s for an 8-frame rollout over 256 candidates" is the same number.
- **vs LeWM**: +23.7 EPDMS on the full set at matched data (63.5 vs 39.8, both navtrain).
- **Compression costs ranking reliability, and data plus rollout loss buy it back.** At matched data, AD-E2E-JEPA's hit rate (27/59) is well below DINO-WM (40/73) and JEPA-WM (45/75), even though its EPDMS is highest. The rollout + trainval variant reaches 47/78.
- **EPDMS and geodesic metrics disagree.** On the 100-scene subset the rollout variants have better FDE and hit rate but lower EPDMS (70.4, 72.3 vs 76.6). The authors suggest 100-scene variance or a mismatch between a latent-distance objective and NAVSIM's driving score. Table 4 locates most of the drop in **drivable-area compliance** (DAC 87 → 77 for the navtrain rollout variant).
- **Vocabulary scaling** (full set): 256 → 8,192 candidates raises EPDMS 67.3 → 72.9 and lowers FDE 4.0 → 2.8 m, at 0.8 → 18.2 s. Top-1 hit rate falls (53.8 → 15.3%) because the ground-truth trajectory now competes with many near-duplicates.

**Transfer to imitation learning (§3.4, §4.4, Table 3, App. A.5)**
- The predictor is discarded and DINOv3 + projector are kept. The model gets a Drive-JEPA-style head (temporal and patch-position embeddings, driving command, one cross-attention trajectory query, MLP, MSE loss) and is **fully fine-tuned** on 4 front frames at 3×256×512.
- **Random projector 80.2 → pretrained projector 85.4 EPDMS** (NAVSIMv2 navtest stage 1). The largest submetric gains are DAC 89.8 → 93.7 and EC 84.1 → 88.7.
- Reference methods, which the paper says are "not direct baselines": Latent-WAM 89.3, **WA-JEPA 91.7** (multi-view; 64 A800s for stage 1), Transfuser 76.7 and Drive-JEPA 87.8, the last two reported before a NAVSIM human-filter bug fix and so not on the same scale.

## Reading it critically

> [!warning] The goal is the answer. This is not a driving policy.
> The planner is given **the real camera frame 4 s in the future** and asked which trajectory gets there. That is closer to **visual odometry or inverse dynamics by search** than to driving: the goal image already encodes where the car ends up. The authors are clear that the purpose is to isolate world-model quality, and for that it is a reasonable probe. But the EPDMS numbers (67.3–72.9) **cannot be set beside policies'** NAVSIM scores, the 85.4 imitation result included, because a deployed driver never has its future frame. The abstract's "reaches goals located 20 meters away on average within 2.8 m" should be read in the same light. The paper gives no "20 m" figure outside the abstract.

> [!warning] Offline, non-reactive, one seed, no error bars
> NAVSIM is a **non-reactive pseudo-simulation**: other agents replay their logs and the ego plan is scored, not driven in closed loop. Everything here is open-loop scoring of one selected trajectory per scene. No table reports seeds or variance. The baseline comparison uses **100 scenes**, and the authors themselves attribute a 4-point EPDMS gap on that subset to its variance.

> [!note] The LeWM baseline is far from LeWM's recipe
> LeWM is a ~15M-parameter end-to-end model. Here it is trained with a **ViT-L from scratch at batch size 8**. SIGReg's normality test runs **across the batch**, so with B = 8 its statistic is very noisy. All three baselines are author re-implementations on NAVSIM. LeWM's weak result (Hit@1 5.7% on the full set) may say as much about this configuration as about the global-CLS design. The paper attributes the gap to CLS vs patches, but no ablation separates the two: no LeWM at a sane batch size, and no DINOv3-CLS model.

- **No ablation of the anti-collapse pieces.** There is no run without SIGReg, without the stop-gradient, or with SIGReg on a pooled rather than per-patch embedding. That a frozen-target projector would collapse without them is asserted, not shown, so the paper doesn't establish which piece is load-bearing.
- **The imitation comparison is narrow.** It is pretrained vs random projector on the same frozen-backbone architecture, with no seeds. That isolates projector pretraining, as intended. It does not show that world-model pretraining beats simply fine-tuning DINOv3 without a projector, which is not reported.
- **Good on measurement.** Hit rate (rank of the ground-truth trajectory among candidates by latent cost) is a **direct test of action sensitivity**, the check the [slow-feature-collapse page](../concepts/world-models/slow-feature-collapse.md) recommends over loss. Reporting planning time beside quality is likewise better than most of the JEPA planning literature.
- **Code is public** (NAVSIM fork, vocabulary, scripts). The paper text does not mention released checkpoints.

## Bearing on collapse and on the LeWM / DINO-WM / JEPA-WM comparison

- **Driving is the multi-scene regime where slow-feature collapse should bite.** NAVSIM spans many routes, cities, weather and lighting conditions, so scene identity varies between clips. The [H-JEPA theory](h-jepa-hierarchical-world-models-paper.md) predicts that an end-to-end encoder with only SIGReg can collapse onto it. **LeWM, the only end-to-end-trained encoder here, is also the only one whose actions barely matter**: Hit@1 5.7% and Hit@5 11.3% over 257 candidates, against chance of about 0.4% and 2%. That is above chance, so not a full collapse, but it fits the prediction. The paper does not diagnose it in those terms, and the batch-8 configuration is a confound.
- **The frozen-encoder models sidestep it.** DINO-WM, JEPA-WM and AD-E2E-JEPA all predict in frozen DINOv3 space, which cannot drift toward the scene. AD-E2E-JEPA's projector re-opens a collapse surface, and the authors guard it with stop-gradient plus per-patch SIGReg. Per-patch SIGReg is still a constraint on a **marginal** distribution (per location, per time), so H-JEPA's Proposition 1 applies in principle. What probably protects AD-E2E-JEPA is that the frozen DINOv3 input and the stop-gradient target leave the projector little room to discard ego-motion. That is an inference, not a result in the paper.
- **The JEPA-WM vs DINO-WM ordering holds in a new domain**, by a small margin: 74.2 vs 68.3 EPDMS and 45/75 vs 40/73 hit rate on 100 scenes, with matching cost. This is the first wiki evidence for the [JEPA-WMs](../entities/jepa-wms.md) recipe outside robot manipulation and navigation.
- **LeWM's speed advantage reappears**: about 130× faster than DINO-WM here, against the "up to 48×" LeWM claims. On driving, though, the speed came with a large quality loss, and the paper's projector is a middle point between the two.

## Possible contradictions with other wiki pages

> [!warning] Contradiction: NAVSIM is "non-reactive," not "closed-loop"
> The [X-VLA source page](xvla-paper.md) calls NAVSIM "a closed-loop autonomous-driving benchmark." This paper, and the NAVSIM paper it cites (Dauner et al. 2024, "Data-driven **non-reactive** autonomous vehicle simulation and benchmarking"), describe it as pseudo-simulation with non-reactive agents. X-VLA's 87.3 is also **PDMS (NAVSIM v1)**, not v2's EPDMS, so the two numbers are not on the same scale.

## Entities mentioned
- [LeWorldModel](../entities/leworldmodel.md) · [DINO-WM](../entities/dino-wm.md) · [JEPA-WMs](../entities/jepa-wms.md) · [DINOv3](../entities/dinov3.md) · [DINOv2](../entities/dinov2.md) · [V-JEPA 2](../entities/v-jepa-2.md)
- [Yann LeCun](../entities/yann-lecun.md) · [Anna Choromanska](../entities/anna-choromanska.md) · [AMI Labs](../entities/ami-labs.md) · [Waymo](../entities/waymo.md) (named in the introduction only)
- Wancong Zhang (also first author of [HWM](../entities/hwm.md) and [H-JEPA](../entities/h-jepa.md)) and Haoran Zhu have no entity pages. Neither do NAVSIM, WA-JEPA, Drive-JEPA, Latent-WAM, VADv2 or Transfuser.

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md) — first action-conditioned JEPA planning on driving.
- [SIGReg](../concepts/world-models/sigreg.md) — a fourth placement: **per patch location × time step, across the batch**, guarding a learned projector over a frozen encoder.
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — the multi-scene regime; LeWM's weak action sensitivity.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — hit rate as an action-sensitivity probe; the privileged-goal caveat.
- [Learned latent space](../concepts/world-models/latent-space.md) — compressing frozen-encoder patches for planning.
- [Imitation learning](../concepts/learning/imitation-learning.md) — world-model pretraining as an initialiser for a driving policy.
- [World-action model](../concepts/world-models/world-action-model.md) — the E2E-driving JEPA landscape the related work maps (Drive-JEPA, WA-JEPA, Latent-WAM, DA-WAM).

## Open questions
- **Without the oracle goal**, with a route command or a learned goal proposer, how much of the 67–73 EPDMS survives? That is the number that would compare with driving policies.
- Which anti-collapse piece is load-bearing: stop-gradient, per-patch SIGReg, or neither, given the frozen input?
- Is LeWM's failure the global CLS bottleneck, slow-feature collapse in multi-scene data, or batch-8 SIGReg? An LeWM + inverse-dynamics run, or a DINOv3-CLS model, would separate them.
- Does the 16×/4× projector transfer to manipulation, where JEPA-WMs' DROID planning is just as slow, and does it hold up under CEM rather than vocabulary search?
- Hit rate falls as the vocabulary grows, while EPDMS rises. Is the latent cost resolving fine trajectory differences, or is it just choosing among more near-duplicates?
