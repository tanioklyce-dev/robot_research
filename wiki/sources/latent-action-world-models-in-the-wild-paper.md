---
title: "Learning Latent Action World Models In The Wild (Garrido, Nagarajan, Terver, Ballas, LeCun, Rabbat, 2026)"
type: source
url: https://arxiv.org/abs/2601.05230
fetch_url: https://arxiv.org/pdf/2601.05230v2
local_path: raw/2601.05230v2.pdf
sha256: b005b53ccba93bcc68471d7c9fb88b1504849b8e63f11395d18d6535fec2bca4
author: Quentin Garrido, Tushar Nagarajan, Basile Terver, Nicolas Ballas, Yann LeCun, Michael Rabbat
published: 2026-01-08
ingested: 2026-10-25
venue: arXiv (cs.AI). v1 2026-01-08, ingested v2 2026-01-20.
format: "paper, 19 pp (12 main + supplementary A–H). Affiliations: FAIR at Meta; Inria (Terver); NYU (LeCun). No code link in the paper."
tags: [latent-actions, latent-action-model, inverse-dynamics, world-model, v-jepa-2, in-the-wild-video, youtube-temporal-1b, vector-quantization, sparsity, vae, droid, recon, cem, planning, cross-embodiment, lecun]
---

# Learning Latent Action World Models In The Wild (2026-01-08)

> [!note] Title
> [LeCun's Lemley Lecture slides](lecun-brown-lemley-lecture-2026.md) cite this arXiv number as *"Inferring hidden actions from video"*. That is a slide caption. The paper's title is *Learning Latent Action World Models In The Wild*.

## Summary

A FAIR study of **latent action models (LAMs)** trained on **in-the-wild video** (YoutubeTemporal-1B) instead of the usual games, tabletop manipulation or curated robot data. An inverse dynamics model (IDM) infers a 128-d latent action from consecutive frames. A ViT-L world model then predicts the next frame from the past plus that latent. Both work in the latent space of a **frozen V-JEPA 2-L** encoder.

The paper compares three ways of limiting how much the latent action can carry: **sparsity**, **noise** (VAE-style) and **vector quantization**. Findings:
- **Continuous, constrained latents capture complex actions** such as a person entering the room. **VQ does not.** Its capacity stays near the no-action baseline.
- **Little next-frame leakage was found.** Prediction error more than doubles at an artificial scene cut for every setting.
- **Latent actions transfer between videos**, e.g. a man's leftward motion applied to a flying ball. Because the videos share no embodiment, the actions become **spatially localised and camera-relative**.
- **A small controller maps real actions into the latent space.** With it, the world model, trained only on natural video, can plan:
  - **DROID** arm reaching: best Δxyz **0.10 m** against V-JEPA 2-AC's 0.15 and the best JEPA-WMs model's 0.05.
  - **RECON** navigation: RPE 0.40, against NoMaD 0.52 and NWM 0.35.

## Key claims

### Setup (§3–4, App. A)
- **Loss:** `L_t = ‖s_{t+1} − p_ψ(s_{0:t}, z_t)‖₁ + L_z(z_t)`, with `z_t = g_φ(s_t, s_{t+1})`, trained jointly with teacher forcing.
  - The predictor is conditioned frame-wise through AdaLN-zero.
  - One latent per two frames, because of V-JEPA 2's tubelets.
  - Clips are 16 frames at 4 fps. Training is 30k iterations at batch 1,024, about **12 h on 64 H100s**.
- **Three regularisers:**
  - **Sparse:** L1 plus a VICReg-style variance–covariance–mean term, sweeping λ₁ over 0.4 … 0.01.
  - **Noisy:** KL to N(0,1) with β from 5e-3 to 1e-6.
  - **Discrete:** VQ in UniVLA's scheme, codebook size 16 to 32,768.
- **Capacity** is measured as one-step "in-the-wild prediction error" using the IDM. Lower error means higher capacity (Fig. 4).

### What the latents encode (§5–6)
- **Fig. 4:** sparse and noisy span the whole range from unconstrained to no conditioning. **VQ "struggles to scale its capacity and remains very close to the deterministic baseline."**
- **Future leakage (Table 1, Kinetics, LPIPS):** with videos spliced at a scene cut, error goes ×2.0–2.5 for every regulariser and capacity. A latent that copied the next frame would show no spike. The authors call the test *necessary, not sufficient* evidence against cheating.
- **Cycle consistency (Table 2):** infer on A, apply to B, re-infer, apply back to A. LPIPS rises only ×1.03–1.34 on Kinetics and RECON. Higher-capacity latents transfer worse, but still end with lower absolute error.
- **Locality (Fig. 8):** a walking action applied to a video with two people moves only the person at the matching image position. *"Latent actions capturing more spatially-localized, camera-relative transformations."*

### Planning through a controller (§7, App. A, C)
- **Controller:** 2 self-attention blocks over the previous frame's representation, plus cross-attention to embedded real actions. It outputs the 128-d latent and is trained with L2 for 3k iterations. **Actions alone are not enough.** Without the frame, the controller converges to a no-motion latent, because the same real action maps to different camera-relative latents.
- **DROID protocol** (following [JEPA-WMs](jepa-wms-paper.md)):
  - CEM with N = 300, K = 10, 15 iterations, H = 3.
  - **64 episodes, each a 4-frame clip from one of 16 validation videos.**
  - **Δxyz** is the L1 distance between the cumulative planned actions and the cumulative ground-truth actions. **This is an offline, open-loop metric against logged actions, not closed-loop robot execution.**
- **Table S1 (DROID Δxyz, m; lower is better):**

  | Latents | Low | Mid | High capacity |
  |---|---|---|---|
  | Sparse | 0.33 | 0.18 | 0.13 |
  | Noisy | 0.49 | 0.11 | **0.10** |
  | Discrete | 0.18 | — | 0.14 |
  | V-JEPA 2-AC (action-labelled) | | 0.15 | |
  | V-JEPA 2 + WM ([Terver et al.](jepa-wms-paper.md)) | | **0.05** | |

- **Table S2 (RECON, NWM protocol: CEM N = 120, 1 iteration, straight-line trajectories, H = 8):** best RPE is 0.40 (noisy, high capacity). **NWM 0.35**, NoMaD 0.52.
- **Neither extreme of capacity is best for rollouts.** Rollout quality and planning score don't track each other: *"noisy latent actions obtain the best planning performance when the unrollings are the worst, relatively speaking."*

### Scaling and domain data (§8, App. D)
- **Fig. 12:** IDM prediction improves with model size (L → g), training length and data. **On DROID planning, only training length clearly helps.** Model size helps noisy latents only, and data quantity shows *"no significant trend"*. The default recipe sees about 1% of all frames.
- **Table S3, mixing DROID into pretraining:** at 10% DROID, noisy Δxyz drops 0.14 → 0.09. At 75–90% it reaches **0.06, against 0.05 for an action-labelled world model on the same data**.
- A DROID-only LAM *"makes a robotic arm appear"* when a person enters a room, because the arm is the only moving thing it ever saw.

### Stated limitations (§9)
- The information constraint is a single static coefficient.
- Sampling and planning **directly in latent-action space** is open. Sampling breaks down for high-capacity continuous latents (App. B, UMAP).
- The encoder is frozen and *"not designed with prediction in mind"*. The authors suggest using latent actions inside V-JEPA 2 pretraining for single-stage training.

## Reading notes (wiki inference)

> [!warning] The DROID comparison picks the best capacity after seeing the test score
> The Low/Mid/High capacities come from an 8-point sweep, and Table S1 reports all of them. "Similar performance to V-JEPA 2-AC" holds for the best few. The worst noisy setting scores 0.49, more than 3× worse. No held-out selection procedure is described, and there are no seeds or confidence intervals on 64 episodes from 16 videos. So the defensible reading is: **at a well-chosen capacity, an in-the-wild LAM plus a small controller matches an action-labelled V-JEPA 2-AC on short-horizon offline reaching.** It does not match a purpose-built world model (0.05).

- **Continuous beats discrete where the actions are rich; discrete is fine where they are simple.** VQ cannot express "a person enters", yet on DROID's simple reaching it scores 0.14–0.18, competitive with the continuous settings. That splits the wiki's [latent action tokens](../concepts/learning/latent-action-tokens.md) story, where the field's cross-embodiment answer is a discrete codebook (UniVLA, UniT). Discrete codes may be adequate for robot action spaces and a bottleneck only for open-world video. That is not established by this paper alone.
- **The scene-cut test is a reusable leakage diagnostic.** Any model whose latent is inferred from the future (a latent action, an IDM-derived conditioning) can cheat by encoding the answer. Splicing two clips and checking for an error spike is cheap, interpretable and model-agnostic. It sits alongside the latent-LQR and mid-depth-readout diagnostics in [world-model evaluation](../concepts/world-models/world-model-evaluation.md).
- **The IDM has a different job here from the collapse synthesis.** In the [collapse synthesis](../syntheses/world-models/jepa-dynamics-collapse-fixes.md), an inverse-dynamics term is a regulariser that keeps the encoder action-informative. Here the IDM *produces* the conditioning variable, and the danger runs the other way: the latent carrying too much, not the representation carrying too little. The encoder is frozen, so encoder collapse cannot arise. The two literatures share the IDM but not the failure mode.
- **Camera-relative actions are a real limit for robot use.** The latents mean "make whatever is at this image position move this way". A robot controller then has to resolve embodiment from the frame, which is why the action-only controller collapsed to no motion. For a fixed-camera arm that is learnable (DROID). For a moving or re-mounted camera it is a source of transfer error, and it bears on any plan that relies on a stable camera pose.
- **Scaling doesn't show up in the planning metric.** IDM quality improves on every axis, but planning improves only with training length. The authors blame the simplicity of downstream tasks. That matches the wiki's recurring theme that short-horizon benchmarks saturate before representations stop improving.

## Entities mentioned
- [Yann LeCun](../entities/yann-lecun.md) · [Basile Terver](../entities/basile-terver.md) · [V-JEPA 2](../entities/v-jepa-2.md) (frozen encoder; V-JEPA 2-AC baseline) · [JEPA-WMs](../entities/jepa-wms.md) (DROID protocol and upper bound) · [DROID](../entities/droid.md) · [UniVLA](../entities/univla.md) (VQ scheme)

## Concepts touched
- [Latent action tokens](../concepts/learning/latent-action-tokens.md): continuous against discrete latent actions on in-the-wild video.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md): scene-cut leakage and cycle-consistency diagnostics; rollout quality is not planning quality.
- [Cross-embodiment](../concepts/learning/cross-embodiment.md): latent actions as a universal interface via a per-embodiment controller.
- [JEPA](../concepts/world-models/jepa.md): an action-free route to action-conditioned latent world models.

## Open questions
- Closed-loop: does the DROID result hold when the plan is executed on a robot, not scored against logged actions?
- Does the scene-cut test catch subtler leakage, such as the latent encoding only the moving object's next appearance, which the test cannot distinguish from a genuine action?
- Would single-stage training (latent actions inside V-JEPA 2 pretraining) change the camera-relative character of the actions?
- With a fixed per-embodiment camera, how much robot data does the controller need? It was trained for only 3k iterations here, but data quantity is not reported.
