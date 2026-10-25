---
title: "Causal-JEPA: Learning World Models through Object-Level Latent Masking (Nam, Le Lidec, Maes, LeCun, Balestriero, 2026)"
type: source
url: https://arxiv.org/abs/2602.11389
fetch_url: https://arxiv.org/pdf/2602.11389v2
local_path: raw/2602.11389v2.pdf
sha256: 956e136d92c4c944a53e3c2d9cd826aebc96b06af542cd767a0a213e47fb609b
author: Heejeong Nam, Quentin Le Lidec, Lucas Maes, Yann LeCun, Randall Balestriero
published: 2026-02-11
ingested: 2026-10-25
venue: ICML 2026 (PMLR 306); arXiv cs.AI. v1 2026-02-11, ingested v2 2026-05-28.
format: "paper, 25 pp (9 main + appendices). Affiliations: Brown University / GalilAI (Nam, Balestriero), NYU (Le Lidec, LeCun), Mila / Université de Montréal (Maes). Code: github.com/galilai-group/cjepa (not inspected). Built on stable-pretraining and stable-worldmodel."
tags: [c-jepa, causal-jepa, jepa, object-centric, slot-attention, videosaur, savi, masking, world-model, pusht, clevrer, phyre, dino-wm, cem, mpc, counterfactual-reasoning, efficiency, stable-worldmodel, lecun, balestriero]
---

# Causal-JEPA (C-JEPA): object-level latent masking for world models (2026-02-11, ICML 2026)

## Summary

[C-JEPA](../entities/c-jepa.md) is a [JEPA](../concepts/world-models/jepa.md)-style world model over **object slots** instead of image patches. A frozen object-centric encoder (VideoSAUR on frozen DINOv2, or SAVi) turns each frame into N slots. A bidirectional ViT-style predictor is then trained with one change: **whole objects' histories are masked**, all but an identity anchor at the first frame. The predictor must fill in a masked object's trajectory from the other objects and from actions and proprioception, while it also predicts the future. The paper's argument is that masking a whole object removes the shortcut of extrapolating that object's own motion, so the loss can only be minimised by modelling interactions.

**Results:**
- **CLEVRER visual QA:** counterfactual accuracy per question rises **+21.1 pp** (47.7 → 68.8%) over the same architecture without history masking, using VideoSAUR slots.
- **Push-T planning (CEM):** **88.67%** success with **6 tokens × 128 dims**, against [DINO-WM](../entities/dino-wm.md)'s 91.33% with 196 × 384 patch tokens. That is **1.02% of the latent input** and **8.6× faster planning** (673 s vs 5,763 s per 50-trajectory evaluation on one L40S).

The authors call it the first combination of JEPA with object-centric world modelling.

## Key claims

### Method (§4)
- **Entity tokens:** `Z_t = {S_t, U_t}`. Slots plus **auxiliary variables** (action, proprioception) as *separate* tokens, each embedded by a small 1-D temporal conv. Fig. 3: treating them as separate entities beats concatenating them into the object latents, which is the DINO-WM scheme.
- **Masked token:** `z̃_τ^i = φ(z_{t0}^i) + e_τ`, a linear projection of the object's earliest slot plus a temporal position embedding. The anchor is needed because slots are permutation-equivariant and carry no entity position encoding.
- **Loss (Eq. 5–6):** L2 on every masked token over history and future, i.e. `L_history` (masked-object completion) + `L_future` (forward prediction). The target encoder is frozen; there is no EMA and no anti-collapse regulariser.
- **Inference:** full history, mask only the future. The masking exists only at training time.
- **Remark 1:** "causal" means *temporally directed predictive dependencies*, **not** causal identifiability.

### Theory (§6, App. L–M)
- Four assumptions: time-lagged dependencies, a stationary transition mechanism, slots that align with objects, and finite-history sufficiency. Causal sufficiency is not assumed.
- **Influence neighbourhood** `N_t(i)`: a minimal subset of the context that keeps `p(z_t^i | ·)` unchanged when object i's history is masked.
- **Proposition / Corollary 1:** a predictor that ignores `N_t(i)` cannot reach the minimum masked-completion loss. So repeated object masking pushes attention towards these neighbourhoods. The authors present it as a **statement about predictive sufficiency, not recovery of causal parents**, and relate it to invariant causal prediction and IRM.

### Visual reasoning: CLEVRER + ALOE (§5.1, Tables 1–2, A2–A4)
- Protocol: roll 128 frames out to 160 with the world model, then train ALOE on the imagined slot trajectories. 7 slots.
- **The masking gain depends on the encoder** (Table 1):

  | Encoder | Masked objects \|M\| | Avg (per question) | Counterfactual (per question) |
  |---|---|---|---|
  | VideoSAUR | 0 (OC-JEPA) | 82.79 | 47.68 |
  | VideoSAUR | 4 | **89.40** | **68.81** |
  | SAVi | 0 (OC-JEPA) | 77.28 | 41.10 |
  | SAVi | 2 | **83.88** | **60.19** |
  | SAVi | 4 | 73.28 | 34.06 (below no masking) |

  The authors: excessive masking removes informative dependencies, and the best budget *"depends on the robustness of the underlying object representations."*
- **Against object-centric baselines on SAVi** (Table 2): SlotFormer 79.44 avg falls to **44.94 without reconstruction loss**. OCVP-Seq goes 83.11 → 80.09 without reconstruction. C-JEPA scores 83.88 with **no reconstruction at all**. That narrowly beats OCVP-Seq *with* reconstruction on average (83.88 vs 83.11) and more clearly on counterfactual per question (60.19 vs 56.06).
- **Masking granularity** (Table A4, CLEVRER): at matched budgets, token masking at 56% reaches 89.32 and tube masking at 56% reaches **89.46**, against object masking at 4/7 with 89.40. The authors concede that the differences on CLEVRER are *"correspondingly limited"* and argue that object masking is more *stable* across budgets.

### Control: Push-T MPC (§5.2, Table 3, App. G–H)
- Planner: CEM with 300 samples, 30 elites, 30 iterations, H = 5 with action blocks of 5 (25 env steps), receding horizon 5, 50-step budget. The goal is the dataset state 25 steps after the start. Success means position error < 20 (of 450) and angle error < π/9. Slots are **Hungarian-matched** to goal slots before computing the cost. 4 slots.

  | Model | Tokens × dim | Success |
  |---|---|---|
  | DINO-WM | 196 × 384 | **91.33** |
  | DINO-WM (registers) | 196 × 384 | 88.00 |
  | OC-DINO-WM (slots, DINO-WM's autoregressive predictor) | 6 × 128 | 60.67 |
  | OC-JEPA (bidirectional masked predictor, no history masking) | 6 × 128 | 76.00 |
  | **C-JEPA** (\|M\| = 1) | 6 × 128 | **88.67** |

- The decomposition is the paper's cleanest result. **Slots alone lose 30.7 pp. The JEPA-style joint predictor wins back 15.3 pp. Object masking wins back another 12.7 pp.**
- **Masking strategy on Push-T** (Table A5, captioned "CLEVRER" in the paper but evidently Push-T, with masks out of 4 objects):
  - At 25%: object 88.67, token 84.67, **tube 55.33**.
  - At 50%: object 82.67, token 84.00, **tube 5.33**.
- Training: predictor with 6 layers, 16 heads, MLP 2048. 30 epochs, batch 256, one GPU, on **pre-extracted** slot embeddings. 0–2 objects masked per sample on Push-T.

### PHYRE (§5.3, App. J): qualitative only
- C-JEPA rollouts are more physically plausible than OC-JEPA's, and its cross-slot attention concentrates on the interacting slot. The authors label this a proxy and *"not … evidence of formal causal graph identification."*

### Stated limitations (§7)
- Performance is bounded by the object-centric encoder.
- Influence neighbourhoods are not validated against datasets with ground-truth temporal causal graphs.
- Training the encoder jointly without representational collapse is left as future work.

## Reading notes (wiki inference)

> [!warning] The Push-T comparison is not quite like-for-like
> 1. **The encoder saw a different Push-T.** VideoSAUR was trained on a *"Push-T dataset variant, where each object is moving in a random manner"* (App. D.1). DINO-WM's frozen DINOv2 needs no such data. That extra data is part of C-JEPA's pipeline cost and is not counted in the comparison.
> 2. **Training budgets differ.** DINO-WM baselines were trained for 10 epochs (*"more epochs did not improve … and often degrades"*) with 10-d action embeddings. C-JEPA, OC-JEPA and OC-DINO-WM were trained for 30 epochs with 128-d embeddings.
> 3. **Seeds and noise.** The timing figure averages *three seeds* × 50 trajectories. Every success rate in Table 3 is a multiple of 1/150 (91.33 = 137/150, 88.67 = 133/150), consistent with 150 episodes per cell, and no spread is reported. **The 2.7 pp gap to DINO-WM is 4 episodes**, so "comparable" is the right word. The ranking is not established.
> 4. **Hungarian slot matching** sits inside the planning cost for object-centric models only. It is a fair necessity, but it is a hand-built correspondence step that patch models don't need.

- **Two answers to the same slot problem.** Slots are unordered, so a dynamics loss between slot sets is ill-posed without correspondence. [WorldDP](../entities/worlddp.md) fixes ordering with privileged SAM2 masks. C-JEPA instead uses an identity anchor in the predictor and Hungarian matching in the planner cost. Neither paper compares against the other.
- **"Object-level" is not what drives the CLEVRER result; it is what drives the Push-T one.** On CLEVRER, token and tube masking match object masking at their best budgets. On Push-T, tube masking collapses to 5.33% and token masking is ~4 pp behind. So the strong claim, that entities are the right mask unit, rests on the control task. That task has 4 slots and was evaluated on about 150 episodes.
- **Encoder sensitivity is large.** With SAVi, masking 4 of 7 objects scores *below* no masking (counterfactual 34.1 vs 41.1). With VideoSAUR the same budget is the best setting. The optimum masking budget is a property of slot quality, not a constant, and the paper gives no rule for choosing it.
- **Relation to the [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md).** C-JEPA sidesteps encoder collapse entirely: the encoder is frozen and only the predictor trains. Its masking is a *predictor-side* anti-shortcut measure, analogous in spirit to the synthesis's "grounded targets" barriers. It also gives a **direct Push-T data point on the pushed object**. The 60.67% → 88.67% path shows that an object-centric state keeps the T-block representable, and that what an autoregressive predictor fails to learn is the agent–block *interaction*. This is a different failure from the encoder dropping the object, which the [Preserving Unstable Modes](preserving-unstable-modes-inverse-dynamics-paper.md) reading note is about.
- **Efficiency is the robotics-relevant headline.** 6 tokens per step makes CEM rollouts cheap: 8.6× wall-clock on Push-T. For on-robot MPC on edge compute, token count per state is the cost driver, and an object-centric state is the most compact one in the wiki. The cost moves to the encoder: a slot model that must be trained per domain and that bounds performance.
- **Ecosystem.** Built on [stable-worldmodel](../entities/stable-worldmodel.md) and stable-pretraining (Maes, Balestriero). The stable-worldmodel repo names C-JEPA as a downstream user ([stable-worldmodel GitHub](stable-worldmodel-github.md)). Same group as [LeWorldModel](../entities/leworldmodel.md), whose SIGReg encoder training is the obvious thing to combine with this predictor objective. The paper does not try it.

## Entities mentioned
- [C-JEPA](../entities/c-jepa.md) · [DINO-WM](../entities/dino-wm.md) (baseline) · [PushT](../entities/pusht.md) · [stable-worldmodel](../entities/stable-worldmodel.md) · [Lucas Maes](../entities/lucas-maes.md) · [Randall Balestriero](../entities/randall-balestriero.md) · [Yann LeCun](../entities/yann-lecun.md) · [WorldDP](../entities/worlddp.md) (comparison, not cited)

## Concepts touched
- [JEPA](../concepts/world-models/jepa.md): the first object-centric JEPA world model; masking at the entity level.
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) / [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md): a predictor-side anti-shortcut objective with the encoder frozen.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md): the Table 3 decomposition (representation, predictor, objective) as an ablation template; small-n success rates.

## Open questions
- Does C-JEPA's Push-T advantage survive [stable-worldmodel](stable-worldmodel-paper.md)'s visual perturbations? Slots might be more robust to colour and size changes than patches, or less, if VideoSAUR's grouping breaks.
- With an end-to-end SIGReg encoder (LeWM-style) instead of a frozen slot encoder, does object masking still help, and does it interact with collapse?
- How does it scale to real robot scenes with more objects, occlusion and slot identity swaps? Every task here has 4–7 slots in clean synthetic scenes.
- Is there a principled way to pick the masking budget from encoder quality, given the opposite optima on SAVi and VideoSAUR?
