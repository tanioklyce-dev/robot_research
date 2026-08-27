---
title: LeWorldModel
type: entity
subtype: model
created: 2026-05-07
updated: 2026-08-26
sources: 35
tags: [leworldmodel, lewm, jepa, world-model, mila, end-to-end, sigreg, instruction-leakage]
---

LeWorldModel (LeWM) — a JEPA-style world model from [Mila](mila.md), NYU, Samsung SAIL, and Brown, presented as the **first JEPA trainable stably end-to-end from raw pixels** without the typical battery of training heuristics (stop-gradient, EMA, frozen encoder). Senior author: Yann LeCun (March 2026).

## Approach
- **Two loss terms only**:
  1. Next-embedding prediction (MSE) — encoder + predictor jointly trained.
  2. **SIGReg** — projects latent embeddings onto random univariate directions; runs a normality test on each; aggregates statistics to enforce isotropic Gaussian latents. Provides provable anti-collapse.
- Reduces tunable loss hyperparameters from **6 to 1** vs. PLDM (the prior end-to-end JEPA baseline).
- **15M parameters**; single GPU; hours of training.

## Architecture components (from GitHub `jepa.py`)
Four modules ([le-wm GitHub](../sources/lewm-github.md)):
1. **ViT encoder** — raw pixel frames → latent `z`
2. **AR Predictor** — autoregressively predicts next-step latent
3. **Action encoder + projector MLPs** — encode actions into predictor input space
4. **Gaussian regularizer ([SIGReg](../concepts/world-models/sigreg.md))** — enforces isotropic Gaussian latents; the single hyperparameter

## Baselines compared against
PLDM, LeJEPA, IVL, IQL, GCBC, [DINO-WM](dino-wm.md) — checkpoints on Google Drive.

## License
MIT.

## Headline claims
- **Plans up to 48× faster** than foundation-model-based world models (e.g. DINO-WM).
- Competitive across diverse 2D and 3D control tasks.
- Latent space probing reveals **encoded physical structure**.
- Surprise scores reliably detect physically implausible events.
- Reconstruction-free, reward-free, task-agnostic, pixel-based.

## Planning recipe (push-t, per the Welch Labs Part 2 walkthrough)
The [Welch Labs Part 2 explainer](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) concretizes how LeWM plans, beyond the architecture:
- **Cross-entropy method (CEM)**: sample ~**500 random action trajectories**, roll each out through the world model (actions batched in **groups of 5**), score by **Euclidean distance in embedding space** between the final predicted embedding and the **goal-image embedding**, keep an **elite set of ~30**, refit a Gaussian and resample, repeat. **All planning happens in latent space** — no decoding required to score.
- A separately-trained **decoder** maps predicted embeddings back to images purely for *visualization* (a "learned cartoon sketch" of push-t physics) — it is not in the planning loop.
> [!note] The Euclidean scoring step rests on an assumption nobody stated
> Scoring candidates by **Euclidean distance in embedding space** is valid as a measure of progress only if latent trajectories are approximately **straight** — otherwise Euclidean distance is a poor proxy for geodesic distance along the reachable manifold. [Temporal Straightening](../sources/temporal-straightening-paper.md) shows that pretrained-encoder latents are "usually highly curved" and that training for low curvature raises goal-reaching success by 20–60% open-loop. LeWM trains its encoder end-to-end rather than freezing DINOv2, so it is not the paper's target — but the metric assumption is the same one, and it has never been checked here. See [gradient-based planning](../concepts/world-models/gradient-based-planning.md).

- **Horizon limit**: reliably plans only **~5 prediction loops** ahead before the rollout drifts "off the rails" — the practical ceiling that motivates hierarchy.

> [!note] The hierarchical push-t result is [HWM](hwm.md), and its base is DINO-WM (not LeWM)
> The Welch Labs video showed LeWM for the *single-level* push-t demo, then described a hierarchical extension "from 5 to 15 steps." That hierarchical work is **[HWM — "Hierarchical Planning with Latent World Models"](../sources/hwm-paper.md)** (Zhang et al., incl. LeCun, April 2026), which instantiates its **Push-T** experiments on **[DINO-WM](dino-wm.md)**, not LeWorldModel. HWM is a model-agnostic two-level planning wrapper; its real numbers are Push-T **17%→61%** (d=75) and Franka **0%→70%**, not "5→15 steps." LeWM remains the *single-level* baseline the video used to explain CEM planning.

> [!warning] LeWM's own group measured it collapsing out-of-distribution
> The [stable-worldmodel paper](../sources/stable-worldmodel-paper.md) (2026-05-20 — same lead author, [Lucas Maes](lucas-maes.md)) benchmarks LeWM under controlled perturbation: **50.8 % base Push-T success → 6–26 % under targeted color / size / shape changes**, with **quadratic decay** as distractor objects are added. In-distribution it still looks strong (**94 %** Push-T, vs DINO-WM's 92 %) — which is the finding: in-distribution scores hide the fragility.
>
> Baseline caveat: the ingest surfaced both **50.8 %** and **94 %** as the unperturbed number (see the [source page](../sources/stable-worldmodel-paper.md)); the collapse to 6–26 % is consistent either way.
>
> This does not retract the headline claims below (they are in-distribution results and remain accurate), but it bounds them hard. Read the "competitive across diverse 2D and 3D control tasks" claim as *within the training distribution*. The companion [identifiability theorem](../concepts/world-models/identifiability.md) is not a defense here — it assumes a generative model a color-shifted environment plausibly violates outright.

> [!note] Two 2026 successors take opposite routes to LeWM's weaknesses
> **[LpWM](lpwm.md)** ([paper](../sources/lpwm-paper.md), Aug 2026) keeps LeWM's encoder and CEM planner but swaps SIGReg's dense isotropic Gaussian for **RDMReg**'s sparse non-negative codes, and reports **+24–57% on PushT at intermediate predictor capacity** (no advantage at high capacity, none on the already-linear Wall env) plus **84.7% vs 65.3%** on piecewise-affine navigation. The claim is that sparsity makes the *dynamics cheaper to model*, not that it plans better outright.
>
> **[AdaJEPA](adajepa.md)** ([paper](../sources/adajepa-paper.md), Jun 2026) leaves the geometry alone and attacks the **out-of-distribution collapse** measured above, by adapting the world model online inside the MPC loop — one gradient step per replan, using the observed transition as a free self-supervised label. On the same shift families ([shape, visual](../sources/stable-worldmodel-paper.md)) it reports *"nearly doubles the planning success rate"* on unseen shapes. Neither paper measures against the other, and **neither reports what fraction of the 50.8% → 6–26% collapse is recovered.**

## Why it matters
- Strips JEPA training down to two losses, making latent-prediction world models more practical for resource-limited research.
- Provides a single-GPU baseline that's hard to argue against — research labs without massive compute can do JEPA work.
- Different point in design space from [V-JEPA 2](v-jepa-2.md): smaller, simpler, end-to-end pixel-trained, vs. V-JEPA 2's massive video pretraining + frozen-encoder post-training.

## Related
- [Mila](mila.md) — primary affiliation.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — architecture family.
- [SIGReg](../concepts/world-models/sigreg.md) — the regularizer LeWM is built on; why the isotropic-Gaussian target, and where it is challenged.
- [Learned latent space](../concepts/world-models/latent-space.md) — LeWM is the first JEPA to learn its latent space *end-to-end from raw pixels* (no frozen DINOv2); SIGReg is the anti-collapse mechanism.
- [V-JEPA 2](v-jepa-2.md) — sibling JEPA model from a different group.
- [World-model simulators](../concepts/world-models/world-model-simulators.md) — broader paradigm.

## Code
- Official repo: https://github.com/lucas-maes/le-wm (built on [`stable-worldmodel`](stable-worldmodel.md) + `stable-pretraining`)
- Pretrained HF checkpoints: `quentinll/lewm-{pusht,cube,tworooms,reacher}`
- See [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md) for the practical recipe.

## Mentioned in
- [LeWorldModel Paper](../sources/leworldmodel-paper.md)
- [LeWorldModel — train and run howto](../syntheses/world-models/leworldmodel-howto.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs Part 2 (video)](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) — CEM planning + hierarchical push-t walkthrough.
- [le-wm GitHub](../sources/lewm-github.md)
- [MLWorks — Navigate the World from Raw Pixels](../sources/medium-lewm-navigate-world.md)
- [Towards Deep Learning — This World Model Learns Physics by Watching Videos](../sources/towardsdeeplearning-world-model-physics.md)
- [stable-worldmodel paper (Maes et al., 2026)](../sources/stable-worldmodel-paper.md) — the platform LeWM runs on, and the generalization benchmark that measures its out-of-distribution collapse.
- [WorldDP paper (Goswami et al., 2026)](../sources/worlddp-paper.md) — uses LeWM's OGBench env variants and benchmarks against LeWM (which, being single-stage, scores 0 on multi-stage Cube-Triple/Scene-Composite).
- [Sensorimotor World Models paper (Ivashkov et al., 2026)](../sources/sensorimotor-world-models-paper.md) — adopts LeWM's latent-planning setup; SIGReg (LeWM's regularizer) is its main anti-collapse baseline.
- [Grounding Spatial Relations in a Compact World Model (Wang et al., 2026)](../sources/grounding-spatial-relations-compact-wm-paper.md) — critiques the compact JEPA-latent + reference-anchor + language-goal recipe (à la LeWM) for [instruction leakage](../concepts/world-models/instruction-leakage.md); prescribes goal-free dynamics.
- [LeNEPA paper (Chemeris, Jin, Balestriero 2026)](../sources/lenepa-paper.md) — carries LeWM's SIGReg into time-series SSL (the "Le-" family sibling).
- [LpWM paper (Kuang et al., 2026)](../sources/lpwm-paper.md) — sparse-latent successor sharing LeWM's encoder and planner; the dense baseline it is measured against.
- [AdaJEPA paper (Wang et al., 2026)](../sources/adajepa-paper.md) — test-time adaptation as the online answer to LeWM's OOD fragility.
- [Temporal Straightening paper](../sources/temporal-straightening-paper.md) — the geometric condition under which LeWM's embedding-distance planning cost is meaningful.
