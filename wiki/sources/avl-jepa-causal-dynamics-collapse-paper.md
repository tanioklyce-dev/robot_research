---
title: "AVL-JEPA: Preventing Causal Dynamics Information Collapse in JEPA World Models (Qiao, Zhang, Song, Huang 2026)"
type: source
url: https://arxiv.org/abs/2610.03587
local_path: raw/2610.03587v1.pdf
sha256: 0875a97397f6e8a0d374193e66e0b48f480e17a6d49fb34e696c23758e864924
author: Yikang Qiao, Ling Zhang, Ziying Song, Duan Huang
published: 2026-10-02
ingested: 2026-10-22
venue: arXiv (cs.RO), v1; marked "Under review as a conference paper at ICLR 2027"
format: "paper, 17 pp (9 main + appendices A–D). Affiliations: Central South University (Qiao, Zhang, Huang), Yanshan University (Song); Zhang and Song corresponding. Code 'will be released upon publication' — none at v1."
tags: [avl-jepa, jepa, leworldmodel, sigreg, inverse-dynamics, slow-feature-collapse, causal-dynamics-collapse, visual-robustness, data-augmentation, cem, pusht, tworoom, ogbench, reacher, simulation-only]
---

# AVL-JEPA: Preventing Causal Dynamics Information Collapse in JEPA World Models (Qiao, Zhang, Song, Huang 2026)

## Summary

The paper argues that a [LeWorldModel](../entities/leworldmodel.md)-style JEPA can pass every global anti-collapse check (high rank, non-constant, SIGReg-satisfied) and still under-represent **how different actions change the physical state**. Two distinct actions can produce nearly identical predicted latent transitions. The authors name this **"causal dynamics information collapse."** The fix, **AVL** ("action-grounded vision-invariance latent"), is a two-stage fine-tune on top of LeWM. **Stage 1 ("action-grounded")** adds an auxiliary head that regresses the executed action block from the current latent and the latent change (z_t, Δz). Mechanistically this is an **inverse-dynamics (IDM) term**, with one twist: the head's output is the trunk's response to [z_t, Δz] minus its response to [z_t, 0], so it cannot predict the action from the state alone. **Stage 2 ("vision-invariance")** feeds a noise-corrupted current frame, trains its prediction toward the same *clean* future target, and keeps the stage-1 action loss active with the head frozen. The head is discarded at planning time, so the planner sees an unmodified LeWM. The evaluation is **simulation only** (TwoRoom, PushT, OGBench Cube, Reacher) with LeWM's CEM planner. Clean success moves little: +4.8 points on TwoRoom, +5.0 on Cube, a tie on PushT, and −1.2 on Reacher. The paper's real result is **robustness under visual perturbation**. With Gaussian policy-input noise σ=0.10, PushT goes **15.3% → 81.5%** and TwoRoom **65.7% → 88.7%**. Under saturation +0.35, PushT goes **14.0% → 62.0%**. Those gains come from the *combination*: either stage alone is often no better than LeWM, and sometimes worse.

## Key claims

**Failure-mode framing (§3.1)**
- Eq. 1–3: under squared loss, keeping a feature u_t helps prediction by ΔR(u_t) = E[tr Var(E[Y|X,u] | X)] ≥ 0. The paper's informal argument is that **temporally persistent visual factors** reduce prediction risk directly, while action-induced change "may require nonlinear state–action interactions" and so gives a weaker training signal. The visual content is kept and the dynamics are under-represented. This is a motivating identity, not a theorem that collapse occurs.
- Eq. 4: JEPA identifies observations only up to **predictive equivalence** over the action set seen in training. States that differ only in their consequences under unseen actions need not remain distinguishable.
- Positioning (§2): VICReg, EMA, SIGReg/LeJEPA, Sub-JEPA and SD-JEPA are described as fixing collapse "at the level of global latent statistics." SMWM ([Ivashkov et al.](sensorimotor-world-models-paper.md)) and Delta-JEPA are cited as concurrent work that "expect inverse-dynamics method alone to prevent collapse." **Neither is compared against.**

**Method (§3.3–3.4, §4.2)**
- Action head: a three-layer Linear–LayerNorm–GELU trunk φ_ψ (input 2·d_z = 384, hidden h = 256), then a bias-free projection W_o. r_ψ(z_t, Δz) = φ_ψ([z_t, Δz]) − φ_ψ([z_t, 0]), and â = W_o·r_ψ. Δz = z⁺_{t+H} − z_t is taken from the **shared target encoder**. The head predicts one action block of H = 5 low-level steps under a SmoothL1 loss (Eq. 5–8).
- Loss in both stages: L = L_pred + 0.09·L_SIGReg + 5·L_action (Eq. 7, 13). λ₂ = 5 was chosen by a **TwoRoom closed-loop sweep**: 85.2 / 87.2 / 92.8 / 92.6% for λ₂ ∈ {0.05, 0.5, 5, 10}.
- Stage 2: each current frame is drawn with probability ⅓ each from {clean, Gaussian σ=0.01, Gaussian σ=0.03}. Only o_t is perturbed; the target o_{t+H} stays clean. **There is no explicit invariance term** (no ‖z̃ − z‖). The "alignment" is implicit: clean and perturbed contexts are trained toward the same clean target. In effect this is **input-noise augmentation with a clean target**, plus a frozen IDM head whose loss keeps back-propagating into the encoder.
- Schedule: stage 1 runs 10 epochs (AdamW, lr 5e-5, wd 1e-3, bf16). Stage 2 initialises from stage 1 and runs 2 epochs at lr 1e-5, batch 128. Hardware is a single **RTX 5090**, at 15.3 (TwoRoom) to 61.9 (Cube) minutes per epoch. Backbone per App. B.6/D: 224² images, d_z = 192, history 3, one-step prediction, SIGReg with 17 knots and 1,024 projections, 90/10 split. App. B.6 also describes the "main LeWM training run" at **11 epochs**, so the LeWM baseline appears to be the authors' own retrain.

**Closed-loop planning (§4.1, §4.6, Table 2, App. C Tables 4–12)**
- Protocol: LeWM's CEM planner (300 samples, 30 iterations, 30 elites, horizon, receding horizon and action block all 5). Goals are 25 env steps ahead with a 50-step budget. There are **10 seeds × 50 episodes**, reported as mean ± population std.
- **Clean (Table 2)**: TwoRoom LeWM 88.4 → AVL **93.2**. PushT 96.0 → **96.0** (tie). Reacher **86.4** → 85.2 (LeWM best). Cube 73.2 → **78.2**. Other baselines: PLDM 91.7 / 78.1 / 78.3 / 65.2 and SD-JEPA 86.3 / 84.6 / 85.0 / 69.6.
- **Perturbed, LeWM → AVL**:
  - Gaussian σ=0.10 (Table 4): TwoRoom 65.7 → 88.7, **PushT 15.3 → 81.5**, Reacher 42.6 → 78.2, Cube 52.6 → 72.7.
  - Saturation +0.35 (Table 6): TwoRoom 54.8 → 86.7, PushT 14.0 → 62.0, Reacher 24.4 → 65.3, Cube 70.8 → 74.0.
  - Brightness +0.20 (Table 5): TwoRoom 78.0 → 88.9, PushT 39.6 → 72.0, **Reacher 11.6 → 14.7**, Cube 45.4 → 48.7.
- **The stages interact; they do not add.** On PushT σ=0.10, action-grounded alone gets **10.0** (below LeWM's 15.3), vision-invariance alone gets 31.3, and both together get 81.5. On TwoRoom saturation +0.35, action-grounded alone **drops to 36.0** from LeWM's 54.8, while vision-invariance alone reaches 85.3, close to AVL's 86.7. On TwoRoom brightness −0.20 (Table 11), action-grounded gets 43.2 vs LeWM's 54.0. **The IDM stage alone does not confer visual robustness and sometimes hurts it.**
- **Transfer claim (§4.6)**: stage 2 trains only on Gaussian noise, yet brightness and saturation robustness also improve. The authors read this as "learning and exploiting causal dynamics information rather than merely fitting a specific augmentation."

**Mechanism diagnostics (§4.3–4.5, Fig. 1, 3–5, 9; App. B)**
- **Counterfactual alignment (Fig. 4)**: 100 held-out states × a fixed bank of 12 candidate action sequences, each 5 blocks / 25 low-level steps. Simulator restoration was audited, with zero non-exact restores over 1,200 renders. Predicted-to-physical Spearman of pairwise transition distances, LeWM → AVL: TwoRoom 0.346 → 0.531, **PushT 0.192 → 0.851**, Reacher 0.072 → 0.536, **Cube 0.018 → 0.214**. Normalized regret: 0.152 → 0.061, 0.064 → 0.045, 0.304 → 0.277, 0.599 → 0.464. TwoRoom Top-1 / Top-3 oracle inclusion: **20 → 47% / 48 → 77%**.
- **Clean–noisy consistency (Table 1)**: 100 states, 3 repeats, σ=0.05. On TwoRoom, LeWM / action-grounded / AVL score Spearman 0.89 / 0.90 / 0.98, Top-1 agreement 58 / 60 / 76%, nuisance drift 8.9 / 8.7 / 6.8 and noisy regret 0.162 / 0.088 / 0.069. On PushT, Spearman is 0.809 / 0.970 / 0.998, Top-1 45.3 / 76.0 / 93.0%, and the action-to-nuisance ratio **2.35 / 7.21 / 19.23**. AVL vs action-grounded on TwoRoom: +0.081 Spearman (95% CI 0.065–0.099) and +16.3 points Top-1 (CI 9.7–23.0).
- **Targeted erasure (Fig. 5, Fig. 9)**: removing the top-k PCA directions of the candidate transitions degrades AVL's ranking far more than LeWM's. The authors read this as AVL **concentrating consequence information** in its leading directions. A random-subspace control appears only for TwoRoom (App. Fig. 9).
- **Fig. 1 PCA** is qualitative. The authors note that PC1 and PC2 explain only 5.80% and 4.94% of standardized variance.

## Reading it critically

> [!warning] The "action anchor" is inverse dynamics, the barrier the wiki already knows
> Regressing a_t from (z_t, z_{t+H} − z_t) through a shared encoder is an IDM term. It is the same kind of term as in [PLDM](pldm-paper.md), [Sobal 2022](sobal2022-jepa-slow-features-paper.md) and [SMWM](sensorimotor-world-models-paper.md), and it is the Ω(1) barrier of [H-JEPA App. L](h-jepa-hierarchical-world-models-paper.md). The genuinely new piece is the **zero-transition baseline subtraction**, which stops the head from reading the action off the state alone (a state-conditioned action prior). **No ablation tests it against a plain IDM head**, so it is unknown whether it matters. Stage 1 alone, which is effectively "LeWM + IDM," changes clean success by −4 to +4 points and **hurts** several perturbed conditions. That contrasts with SMWM's reported **84 vs 59** on Cube with IDM in place of SIGReg. The protocols differ, but the two papers are pointing at the same lever, and AVL does not run SMWM as a baseline.

> [!note] "Causal dynamics information collapse" vs slow-feature collapse: a soft cousin, measured differently
> The §3.1 mechanism is that persistent visual factors are cheap to predict while action-driven change is costly, so the encoder keeps the former and starves the latter. That is the **same pressure** as [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md). The regime is different. The wiki's slow-feature collapse is **total**: zero action sensitivity, triggered by **scene diversity across episodes** (DROID). AVL works only on **fixed-scene simulators**, where H-JEPA's account says SIGReg alone suffices against the total version. LeWM here plans at 73–96% clean, so whatever AVL measures is a **partial, graded** under-representation, not a collapse in the H-JEPA sense. It also mostly shows up as **fragility under pixel perturbation**. The paper never tests scene-diverse data, so it says nothing about the DROID failure. It does not offer a label-free barrier either: **both stages require action labels**. That is consistent with H-JEPA's conclusion, not a challenge to it.

> [!warning] Much of the headline gain is augmentation robustness, attributed to "causal dynamics"
> Stage 2 is input-noise augmentation toward a clean target, and the headline numbers come from evaluating under input noise. A model fine-tuned on Gaussian-corrupted frames being more robust to Gaussian-corrupted frames is the expected result. The transfer to brightness and saturation is more interesting, but it is uneven. **Reacher under brightness collapses for every model** (7–31%, with AVL at 14.7% vs LeWM's 11.6% at +0.20). Cube under brightness +0.10 has AVL **below** LeWM (54.1 vs 56.8). The cleanest evidence that the action loss matters is the **interaction** on PushT (10.0 and 31.3 alone vs 81.5 together). But AVL is also stage-1 weights plus 2 more epochs, and the paper never says how the "vision-invariance only" row was initialised: from LeWM? which head was frozen? So **training budget and initialisation are confounded** with the interaction.

- **Seeds are evaluation seeds, not training seeds.** Each model appears to be **one trained checkpoint** evaluated over 10 planner/episode seeds. The ± figures therefore cover planning variance only, not training variance. The Cube clean gain (73.2 ± 6.8 → 78.2 ± 5.3) is under one pooled std. The λ₂ value was also selected on TwoRoom closed-loop success, i.e. on the benchmark itself.
- **The baselines are the authors' own runs.** LeWM appears to be retrained (App. B.6), and PLDM and SD-JEPA have no stated provenance. LeWM numbers vary a lot across papers on nominally the same LeWM protocol: SMWM reports SIGReg/LeWM TwoRoom 94, Reacher 67, PushT 87, Cube 59, against this paper's 88.4 / 86.4 / 96.0 / 73.2. **Don't compare AVL's numbers across papers.**
- **The alignment metric is weakly tied to planning.** The "physical oracle" is the candidate with the **largest physical displacement norm**, and the model score is the **latent displacement norm**. That measures whether latent motion magnitude tracks physical motion magnitude, not goal-reaching. An IDM loss trains Δz to encode the action, so the metric sits close to the training objective. LeWM scores Spearman **0.192 on PushT and 0.018 on Cube yet plans at 96% and 73%**. A near-zero score on this metric is therefore compatible with strong planning. That undercuts reading it as "collapse."
- **The erasure logic cuts both ways.** "Erasing top directions hurts AVL more" is read as concentration of causal information. But LeWM's PushT baseline Spearman is already 0.19, leaving almost nothing to lose. The random-subspace control is shown only for TwoRoom.
- **Under-specified details.** The noise scale is never stated: training uses σ ∈ {0.01, 0.03} and evaluation σ up to 0.10 "in uint8 range" before normalisation. Nor is it stated whether stage 2's action loss uses the clean or the perturbed Δz. The text claims AVL is best "across all four conditions" on TwoRoom and PushT, but clean PushT is a tie with LeWM, and Reacher is omitted from the claim (LeWM or an ablation wins several Reacher cells). There is an AI-use statement for writing.
- **What is strong.** Planning-time cost is zero, since the head is dropped and the planner sees vanilla LeWM. The paper reports per-condition tables for 9 perturbation settings × 4 tasks with ablation rows. The simulator-restore audit for the counterfactuals is careful. The limitations are stated plainly: simulation only, and still dependent on SIGReg.

## Why it matters here

- It is the **second independent group in October 2026 to land on action labels** as what keeps a JEPA world model's latent tied to control. H-JEPA used theory and DROID; AVL uses simulation and perturbation. It strengthens the wiki's working rule (log actions; passive video is not enough) without extending it to scene-diverse data.
- For a household robot, the relevant point is **visual-nuisance robustness**: lighting and colour shifts break LeWM badly here (PushT 96 → 14% under saturation +0.35). This agrees with [stable-worldmodel](stable-worldmodel-paper.md)'s perturbation findings. A cheap fine-tune of IDM + noise augmentation recovers much of it in simulation. That is a plausible, low-cost recipe to try, but the evidence base is thin.

## Entities mentioned
- [LeWorldModel](../entities/leworldmodel.md) — the backbone, planner, and main baseline.
- [PLDM](../entities/pldm.md) — baseline, and the prior IDM-bearing JEPA.
- [SMWM](../entities/smwm.md) — cited as concurrent IDM-only work; not compared.
- [PushT](../entities/pusht.md) · [DeepMind Control Suite](../entities/dm-control.md) (Reacher)
- [Randall Balestriero](../entities/randall-balestriero.md) · [Yann LeCun](../entities/yann-lecun.md) — SIGReg/LeJEPA lineage, cited.
- Not in the wiki: SD-JEPA (Thil et al., arXiv 2605.31111; a baseline), Sub-JEPA (Zhao et al., 2605.09241), Delta-JEPA (Zhang et al. 2026), OGBench, and the authors' institutions (Central South University, Yanshan University).

## Concepts touched
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — a partial, fixed-scene variant of the same pressure, under a new name.
- [SIGReg](../concepts/world-models/sigreg.md) — kept unchanged (λ = 0.09) and argued to be necessary but not sufficient.
- [JEPA](../concepts/world-models/jepa.md) — another anti-collapse add-on in the taxonomy.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — counterfactual action-ranking metrics, clean–noisy consistency, and subspace erasure as diagnostics beyond success rate.
- [Identifiability](../concepts/world-models/identifiability.md) — the predictive-equivalence argument (Eq. 4).

## Open questions
- Does the zero-transition baseline subtraction matter, or is the action-grounded stage just IDM? A plain-IDM ablation and an SMWM comparison under the same protocol would settle it.
- Does AVL help where the total form of slow-feature collapse occurs, on scene-diverse data like DROID? Or is it purely a nuisance-robustness fix for fixed-scene simulators?
- How much of the perturbation gain survives against a fair augmentation-only baseline: LeWM fine-tuned 2 epochs on the same noise mix, starting from the same checkpoint and with the same total budget?
- Training-seed variance. With one checkpoint per model, are the Cube and TwoRoom clean gains real?
- Real-robot and closed-loop behaviour under natural lighting change, which the authors list as future work along with removing the SIGReg dependence.
