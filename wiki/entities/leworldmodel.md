---
title: LeWorldModel
type: entity
subtype: model
created: 2026-05-07
updated: 2026-07-26
sources: 24
tags: [leworldmodel, lewm, jepa, world-model, mila, end-to-end, sigreg]
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
4. **Gaussian regularizer (SIGReg)** — enforces isotropic Gaussian latents; the single hyperparameter

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
- **Horizon limit**: reliably plans only **~5 prediction loops** ahead before the rollout drifts "off the rails" — the practical ceiling that motivates hierarchy.

> [!note] The hierarchical push-t result is [HWM](hwm.md), and its base is DINO-WM (not LeWM)
> The Welch Labs video showed LeWM for the *single-level* push-t demo, then described a hierarchical extension "from 5 to 15 steps." That hierarchical work is **[HWM — "Hierarchical Planning with Latent World Models"](../sources/hwm-paper.md)** (Zhang et al., incl. LeCun, April 2026), which instantiates its **Push-T** experiments on **[DINO-WM](dino-wm.md)**, not LeWorldModel. HWM is a model-agnostic two-level planning wrapper; its real numbers are Push-T **17%→61%** (d=75) and Franka **0%→70%**, not "5→15 steps." LeWM remains the *single-level* baseline the video used to explain CEM planning.

> [!warning] LeWM's own group measured it collapsing out-of-distribution
> The [stable-worldmodel paper](../sources/stable-worldmodel-paper.md) (2026-05-20 — same lead author, [Lucas Maes](lucas-maes.md)) benchmarks LeWM under controlled perturbation: **50.8 % base Push-T success → 6–26 % under targeted color / size / shape changes**, with **quadratic decay** as distractor objects are added. In-distribution it still looks strong (**94 %** Push-T, vs DINO-WM's 92 %) — which is the finding: in-distribution scores hide the fragility.
>
> Baseline caveat: the ingest surfaced both **50.8 %** and **94 %** as the unperturbed number (see the [source page](../sources/stable-worldmodel-paper.md)); the collapse to 6–26 % is consistent either way.
>
> This does not retract the headline claims below (they are in-distribution results and remain accurate), but it bounds them hard. Read the "competitive across diverse 2D and 3D control tasks" claim as *within the training distribution*. The companion [identifiability theorem](../concepts/world-models/identifiability.md) is not a defense here — it assumes a generative model a color-shifted environment plausibly violates outright.

## Why it matters
- Strips JEPA training down to two losses, making latent-prediction world models more practical for resource-limited research.
- Provides a single-GPU baseline that's hard to argue against — research labs without massive compute can do JEPA work.
- Different point in design space from [V-JEPA 2](v-jepa-2.md): smaller, simpler, end-to-end pixel-trained, vs. V-JEPA 2's massive video pretraining + frozen-encoder post-training.

## Related
- [Mila](mila.md) — primary affiliation.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — architecture family.
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
