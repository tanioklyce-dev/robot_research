---
title: "MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space (Karmann, Li et al., 2026)"
type: source
url: https://arxiv.org/abs/2609.23881
local_path: raw/2609.23881v1.pdf
sha256: d587eb19540ee414d9cd99d4ac12a57e635e858efb7d4ea429b04ac9565b4ac1
author: Markus Karmann, Shile Li, Christian Internò, Bruno Andreis, David Klindt, Randall Balestriero, Jindong Gu, Philip Torr, Qi Zhang, Peng-Tao Jiang, Hao Zhang, Bo Li, Onay Urfalioglu
published: 2026-09-20
ingested: 2026-10-22
venue: arXiv (cs.CV), v1
format: "paper, 24 pp (9 main + references + supplementary §7–10). Affiliations: Oxford, vivo Tech Research GmbH, Bielefeld, Slater Labs, Cold Spring Harbor Laboratory, Brown, AMI Labs, vivo BlueImage Lab. Karmann and Li equal contribution. Code: github.com/mkarmann/motion-jepa (public, no license file as of 2026-10-22)."
tags: [motionjepa, disreg, jepa, slow-feature-collapse, feature-suppression, sigreg, inverse-dynamics, temporal-difference, leworldmodel, smwm, latent-probing, path-straightness, static-distractor, cem, pusht, ogbench, balestriero, klindt]
---

# MotionJEPA: Preventing Temporal Feature Collapse by Capturing Visual Changes in Latent Space (Karmann, Li et al., 2026)

## Summary

The paper adds a **label-free auxiliary objective, DISReg** (Difference Image and Single image embedding Regularization), to a [LeWorldModel](../entities/leworldmodel.md)-style JEPA. A second encoder embeds the **pixel difference image** `o_{t+1} − o_t` into `d_t`. A small head must then predict `d_t` from the pair of ordinary frame embeddings `(z_t, z_{t+1})`. Both `z` and `d` carry [SIGReg](../concepts/world-models/sigreg.md). The head has the structure of an inverse-dynamics module, but its target is an embedding of *visual change* rather than the action, so it needs no labels. An encoder that represents only what is constant within an episode gives the head nothing to predict the change from. The authors call the result **MotionJEPA**. They test it in two places. The first is three purpose-built synthetic games (Pong, Dino, Golf), probed for which features survive training. There, MotionJEPA is the only method whose frozen embedding keeps **every** feature group under 0.1 NMSE. LeWM keeps the slow ones (score, sky, background) and drops the fast ones, and [SMWM](../entities/smwm.md)'s inverse dynamics keeps only what the action moves. The second is the four LeWM benchmarks with a **per-episode wood-texture background** added as a static distractor. There, CEM planning success goes from **20.4% (LeWM) to 81.8%** at 25 steps, against **77.2%** for the authors' own inverse-dynamics baseline, and to **86.4%** when the two are combined. Everything is in simulation, with a fixed camera.

## Key claims

**Method (§3, Alg. 1, §7.1)**
- `d_t = DiffEnc(o_{t+1} − o_t)` (Eq. 1); `d̂_t = DiffPred(z_t, z_{t+1})` (Eq. 2). `L_DISReg = λ_z·SIGReg(z) + λ_d·SIGReg(d) + λ_pred·MSE(d, d̂)` (Eq. 5), added to the usual action-conditioned forward loss `MSE(z_{t+1}, ẑ_{t+1})` (Eq. 6). There is **no stop-gradient on `d`**: the difference encoder trains jointly.
- One fixed setting everywhere: **λ_z = 0.25, λ_pred = 0.5, λ_d = 2**. The paper does not say how these values were chosen.
- `DiffEnc` uses the same architecture as the main encoder: **ViT-Tiny**, patch 14, D = 192 from the [CLS] token, then a 1-layer MLP with BatchNorm. `DiffPred` is a 3-layer MLP (hidden size 512, LayerNorm + GELU) on `concat(z_t, z_{t+1})`. Both modules are **discarded after training**, so inference costs nothing extra (§5). The predictor is LeWM's 6-layer causal transformer with history 3.
- The authors' framing (§3): **λ_d = 0** lets `d` collapse, so the head predicts a constant and the model reduces to LeWM. **λ_z = 0** removes all regularisation of `z` and leaves only the motion-grounded term.
- The **world model itself is still action-conditioned**. "Without action labels" applies to the regulariser only.

**Collapse analysis on synthetic games (§4.1, Table 1, §7.2–7.3, §8)**
- **Environments.** Pong, Dino and Golf, rendered at 112×112. True state dimension is 6–8, far below D = 192, so capacity cannot cause the collapse. Initial states and actions are **sampled uniformly at random**, which decorrelates features and blocks probe shortcuts. Episodes are **four frames** long. Training uses **10M episodes**, batch 128, ~78k steps, the LeWM optimiser and schedule, and **3 seeds**. Golf includes a **wood-texture offset** that is constant within an episode: the [Sobal 2022](sobal2022-jepa-slow-features-paper.md) fixed-distractor case.
- **Protocol.** Freeze the encoder and predictor, then train a high-capacity residual MLP probe (depth 6, width 128) on 1M episodes and test on 10k. Probes are run on the image embedding `z` and on 5-step predicted rollouts `ẑ`. NMSE ≤ 0.1 counts as "not collapsed". The threshold comes from the **random-init encoder**, which already reaches 0.116 on Pong: training actively *removes* information that a random network carries.
- **Baselines.** LeWM (λ = 0.09) and SMWM (IDM weight 1.0), plus three common fixes: **LeWM-Time** (SIGReg along time, the [LeNEPA](lenepa-paper.md) recipe), **LeWM-Flat** (SIGReg over batch and time flattened) and **LeWM-Detached** (stop-gradient target). ForwardOnly and Random are controls. Every baseline gets a **10-point grid search** over its weight, from 0.1 to 100, using full 10M-episode runs; these are the starred `*` variants (Table 4). MotionJEPA is **not** searched.
- **Table 1a (image embedding, average NMSE).** MotionJEPA: **Pong 0.004 / Dino 0.021 / Golf 0.061**. The best tuned baseline per game: Pong LeWM-Flat* 0.008, Dino LeWM-Detached*/LeWM* ~0.28–0.33, Golf LeWM-Flat* 0.299. Default LeWM: 0.658 / 0.394 / 0.763. LeWM keeps only the Pong **score** (0.003) and loses the ball and bats (~1.0). In Golf it keeps only the **wood** background (0.084) and loses the ball, cross and bars. SMWM keeps only the action-driven variables (Pong bats 0.002, Golf ball 0.002). **Golf bars: MotionJEPA 0.095, every other method > 0.3.**
- **Table 1b (5-step rollout).** MotionJEPA still has the lowest average (0.036 / 0.055 / 0.164), but it is **not under 0.1 everywhere**: Golf cross is 0.348 (LeWM-Flat* 0.320) and Golf bars 0.262.
- **Tuning doesn't fix it (Fig. 7).** LeWM* improves Pong from 0.658 to 0.061 at λ = 100 but barely moves on Dino or Golf. The authors read this, following Sobal 2022, as a limitation of the anti-collapse mechanism and not of hyperparameters.
- **LeWM-Time** is the only baseline that encodes the Dino cactus, and it **collapses completely in Golf** (rollout average 0.997).
- **Collapse is invisible in the loss (Fig. 3).** In Dino, LeWM's online dino-position probe falls to ~0.1 by 5k steps and then **climbs back to ~1.0 by 20k**, with no sign of it in the training loss. The slow features (sky, hearts) saturate at ~0.01 NMSE by 10k steps.
- **Linear probes (Table 5)** give the same ranking, but the Golf margin is thin: average **0.746 vs LeWM-Flat* 0.797** on `z`.

**Latent path straightness (§4.1, Table 2, §9)**
- Measured as arc-to-chord ratio over 100 random linear state interpolations of 64 steps (1.0 = straight). **SMWM is straightest** (Pong 1.207, Golf 1.078). MotionJEPA is 2.756 / 5.789 / 3.305 for Pong / Dino / Golf. Any SIGReg along time makes paths much more curved: LeWM-Time* 23.4 / 10.0 / 38.8, LeWM-Flat* 22.2 / 15.6 / 26.7. In **Dino, MotionJEPA (5.789) is more curved than default LeWM (4.826) and ForwardOnly (4.045)**. The abstract's "low curvature" claim holds only relative to the distribution-regularised variants.

**Downstream planning with a static distractor (§4.2, Table 3, §7.4)**
- **Setup.** LeWM's Cube (OGBench), [Push-T](../entities/pusht.md), Reacher and TwoRoom, using LeWM's code and expert datasets. In PushT and TwoRoom the white background is replaced with a wood-texture crop. In Reacher and Cube the static region is found from a pixel-wise median and textured. **A new crop is drawn each rollout and held fixed within it.** Training: 10 epochs, batch 64, AdamW, learning rate 5e-5, frame-skip 5, history 3. Planning uses **LeWM's CEM protocol** (300 candidates, 30 elites). The 25-step setting plans 5 model steps. The 50-step setting executes 25 steps, replans once, then executes 25 more. This is **closed-loop in simulation**.
- **25-step success (%), Cube / PushT / Reacher / TwoRoom / mean.**
  - LeWM: 43.6 / 4.0 / 5.2 / 28.8 / **20.4**
  - LeWM-Flat: 55.2 / 14.4 / 49.2 / 48.0 / **41.7**
  - IDM: 76.0 / **83.6** / 49.2 / **100.0** / **77.2**
  - Ours with λ_z = 0: 60.4 / 76.8 / 24.8 / 99.6 / **65.4**
  - **Ours: 78.0 / 78.4 / 71.2 / 99.6 / 81.8**
  - **Ours+IDM: 80.8 / 82.4 / 82.4 / 100.0 / 86.4**
- **50-step mean.** LeWM 11.8, LeWM-Flat 31.9, IDM 59.3, Ours (λ_z = 0) 49.2, **Ours 70.3**, Ours+IDM 71.6. Push-T is weak for every method (≤ 29.6%), and IDM is ahead of Ours on TwoRoom (96.0 vs 92.0). Most of the gain is **Reacher, 62.0 → 98.0**.
- **Probes on the wood-background benchmarks (Tables 6–7, §10).** PushT agent-position MLP error: **LeWM 121.2, LeWM-Flat 55.7, IDM 3.66, Ours 8.60, Ours+IDM 4.32**. On Reacher, Ours recovers the joints and fingertip **linearly** (joint 0: 0.0265 rad vs LeWM 1.468, IDM 1.385). IDM is better on translation in PushT and Cube. The two signals are reported as **complementary**.
- **Decoder reconstructions (Figs. 8–9).** Trained on frozen latents, the decoder shows LeWM reproducing the wood texture and losing the foreground. MotionJEPA keeps the foreground plus the **coarse** background and smooths out the fine wood detail, which the authors call desirable because static context can still matter (goals, obstacles).

**Limitations stated (§5)**: two extra training-time modules, so more parameters and compute in training. The authors argue from Fig. 3 that the baselines plateau and that collapse is not a compute problem.

**Compute**: GPU type, GPU-hours and wall-clock are not reported. bf16 and `torch.compile` are mentioned.

## Reading it critically

> [!warning] Contradiction: the wiki's "no label-free barrier works" against MotionJEPA. Different evidence, mostly compatible theory
> The wiki's [slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) page, following [H-JEPA App. L](h-jepa-hierarchical-world-models-paper.md), says inverse dynamics is **"the only barrier that works, and it needs action labels"**. In H-JEPA, "time repulsion", the one label-free barrier tested, never beat the zero-action floor on DROID. MotionJEPA, which shares **senior author [Randall Balestriero](../entities/randall-balestriero.md)** and appeared **two weeks before H-JEPA**, reports a label-free term that works against the **same failure**. On the image embedding, MotionJEPA reaches 81.8% vs IDM's 77.2% at 25 steps, and 70.3% vs 59.3% at 50 steps. H-JEPA does not cite MotionJEPA. Three points reconcile the two papers:
>
> 1. **The theorems are not contradicted.** H-JEPA's Prop. 1 covers regularisers that see only the **marginal** law of single embeddings, which SIGReg does. DISReg's prediction term acts on the **joint law of `(z_t, z_{t+1})`**, as H-JEPA itself says a barrier must. It is the IDM construction with a **learned embedding of the pixel difference in place of the action**, and Prop. 3's argument carries over by analogy. Under collapse, `(z_t, z_{t+1})` depends only on the background, so the head cannot do better than `E Var(d_t | background)`. That is a floor *if* `d_t` actually varies within episodes. This transfer is the wiki's reading; **neither paper proves it.**
> 2. **It is also not time repulsion.** Time repulsion rewards *any* latent change, so it has no selector. H-JEPA's θ-window analysis shows why it fails when about half the foreground motion is unpredictable. DISReg rewards change that **predicts a specific target**, namely what changed in pixels. Its target is grounded, like IDM's.
> 3. **The test regime is the same failure, made as easy as possible for a difference image.** The wood crop is a per-episode background drawn from a near-continuous family, so it is H-JEPA's atomless-background case and not the single-scene simulation where SIGReg alone suffices. But it is **pixel-identical across frames under a fixed camera**, so `o_{t+1} − o_t` removes it exactly, apart from pixels a moving object uncovers. DROID adds lighting change, people in the background, compression noise and small camera shake. A mobile robot or wrist camera adds **ego-motion**, which makes the difference image *mostly background*. In that case `d` can again carry scene identity, and `SIGReg(d)` is itself marginal-only, so Prop. 1 applies to `d`. **MotionJEPA was not run on DROID or any real video, and has no moving-camera setting.**
>
> **Verdict.** This is real evidence that a label-free, joint-in-time barrier against slow-feature collapse **exists for static-camera settings**. It narrows the wiki's "only IDM works" from a general statement to "only IDM has been shown on scene-diverse real data". It does not answer H-JEPA's DROID result, and it says nothing about action-free training: MotionJEPA's predictor still uses actions.

> [!note] Different goals: keep everything vs. shed distractors
> H-JEPA's taxonomy treats action-independent movers (distractors) as content to **shed**. MotionJEPA aims at **task-agnostic completeness**, and its headline is encoding the Golf bars and Dino clouds, which are exactly such distractors. Under H-JEPA's Thm. 1, encoding unpredictable movers costs prediction error. MotionJEPA's games are deterministic given state, so that cost never arises. Which goal is right for planning in a cluttered home is open, and this paper's benchmarks can't decide it.

- **IDM, the strongest baseline, is the authors' own implementation.** It regresses the raw action from `Δz = z_{t+1} − z_t` with a 3-layer MLP (Delta-JEPA style), at λ_IDM = 1 "as our hyperparameter search ... showed little sensitivity". It is labelled `[18, 31]`, but it is **not SMWM as published**. Original SMWM, without distractors, scored Cube 84 / TwoRoom 99 ([SIGReg page](../concepts/world-models/sigreg.md)). The real SMWM is run only on the games.
- **The tuning is asymmetric.** In the planning table, plain LeWM runs at its default λ = 0.09, although the game sweep picked λ between 0.1 and 100 for LeWM*. LeWM-Flat uses λ = 1, transferred from the game sweep. MotionJEPA's single fixed setting is presented as a strength, but **where it came from is never stated**. If it was tuned on these environments, the "no search" comparison flatters it.
- **Table 3 has no seeds, standard deviations or episode counts.** Every value is a multiple of 0.4, which is consistent with 250 trials per cell (an inference, not stated). The 25-step lead over IDM is **+4.6 mean points**, and IDM wins PushT and TwoRoom outright. The game tables do report ±std over 3 seeds (Tables 8–10), and there MotionJEPA's margins are far outside seed noise.
- **The game episodes are four frames.** Within four frames the Pong score, Dino sky and hearts, and Golf wood are effectively constant, so they act as background. This is the right regime for studying collapse, but it is a long way from teleoperation horizons.
- **Not tested:** real video, multiple views, proprioception, gradient-based planning (CEM only), and compute matched against IDM (DiffEnc is a second ViT-Tiny during training). There is no **action-sensitivity** or within-episode-variance diagnostic (χ) to compare directly with H-JEPA's Table 12.
- **Two cross-checks that hold up.** LeWM-Flat (time in the sample axis) helps partially (20.4 → 41.7) but does not fix the problem. This matches H-JEPA's **Prop. 2**: a "real but small barrier". LeWM-Time (SIGReg *across* time) fails in Golf, and the H-JEPA analysis predicts that pure time-spreading rewards the wrong change.

## Why it matters here

- **It is the first candidate for the open question the wiki filed under H-JEPA**: is there a label-free barrier that acts on the joint law across time? For a home robot learning from passive video, this decides whether a JEPA world model needs logged actions at all. The answer so far: **plausibly not, if the camera is fixed. Not yet tested if it moves.** That second case is the one a mobile manipulator (Stretch's head camera, a wrist camera) faces. See [JEPA for a household mobile manipulator](../syntheses/world-models/jepa-for-household-mobile-manipulator.md) and [LeWM on Stretch](../syntheses/projects/lewm-on-stretch-feasibility.md).
- **It is cheap to adopt.** It drops into LeWM's own codebase, runs only at training time, and is complementary to IDM (Ours+IDM is best overall). For a LeWM user with action labels, adding DISReg on top of IDM is the lowest-risk version of the idea.
- **It reinforces a wiki-wide diagnostic.** Collapse **does not show up in the training loss** (Fig. 3). Probing and action-sensitivity are the checks. See [world-model evaluation](../concepts/world-models/world-model-evaluation.md) and [representation evaluation](../concepts/learning/representation-evaluation.md).
- **Lineage.** It is a temporal-difference idea, close to [TDV](tdv-paper.md) (which conditions prediction on the pixel difference; DISReg *predicts* its embedding instead). It also continues the inverse-dynamics line of [SMWM](sensorimotor-world-models-paper.md) and Delta-JEPA, and connects to [temporal straightening](temporal-straightening-paper.md) through the curvature analysis. See the [anti-collapse lineage](../syntheses/world-models/ssl-anti-collapse-lineage.md).

## Entities mentioned
- [LeWorldModel](../entities/leworldmodel.md) · [SMWM](../entities/smwm.md) · [LeNEPA](../entities/lenepa.md) · [Push-T](../entities/pusht.md)
- [Randall Balestriero](../entities/randall-balestriero.md) · [David Klindt](../entities/david-klindt.md) · [AMI Labs](../entities/ami-labs.md) · [Yann LeCun](../entities/yann-lecun.md) (cited; not an author)
- Not yet in the wiki: Delta-JEPA (Zhang et al. 2026), Gulati & Nemenman 2026 ("Contrast encodes inductive bias", arXiv 2606.07770), Toso et al. 2026 (arXiv 2602.18639), and the vivo research labs.

## Concepts touched
- [Slow-feature collapse](../concepts/world-models/slow-feature-collapse.md) — a label-free barrier, shown in fixed-camera simulation only.
- [SIGReg](../concepts/world-models/sigreg.md) — batch-axis SIGReg loses fast features; flattened (batch × time) helps partially; SIGReg across time breaks Golf and curves the latent paths.
- [JEPA](../concepts/world-models/jepa.md) — anti-collapse by an auxiliary prediction target instead of a distributional constraint.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) · [Representation evaluation](../concepts/learning/representation-evaluation.md) — probe-based collapse detection; the random-init floor as a reference point.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — the path-straightness results, although this paper plans with CEM.

## Open questions
- **Does DISReg survive DROID?** That means scene diversity, lighting change, people in the background and compression noise. H-JEPA's setting, scored by its Fréchet-fidelity metric, is the direct test, and both papers share an author and a codebase lineage.
- **Moving cameras.** With ego-motion the difference image carries the scene, so can `d` collapse onto episode identity? Would a motion-compensated difference (optical-flow warp) restore the floor?
- **Action-free training.** DISReg removes labels from the regulariser but not from the predictor. Does it prevent collapse in an action-free video JEPA (V-JEPA-style), which is where the label question actually matters?
- **A formal floor.** Can H-JEPA's Prop. 3 be stated for a learned target `d`, and under what condition on within-episode `Var(d_t | background)`?
- **Unpredictable distractors.** In stochastic scenes, does encoding every mover (the MotionJEPA goal) cost planning performance, as H-JEPA's Thm. 1 suggests?
- **Where λ = (0.25, 0.5, 2) came from**, and how sensitive the method is to it. The paper shows sensitivity plots for the baselines only.
