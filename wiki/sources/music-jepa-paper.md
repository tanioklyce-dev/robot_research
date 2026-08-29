---
title: "Music-JEPA: Learning a World Model of Sound from Action"
type: source
url: https://arxiv.org/abs/2607.22000
local_path: raw/music-jepa_2607.22000.pdf
sha256: 86f5ef0dd201d34a1e216ad447846a0dbb68418c64f7f10a3abb08f1eec798ce
author: Ziyu Wang, Kun Fang, Yann LeCun
published: 2026-07-24
ingested: 2026-08-26
venue: arXiv (cs.SD)
format: paper (9 pp)
tags: [jepa, world-model, action-conditioned, audio, music, planning, offline, lecun]
---

# Music-JEPA: Learning a World Model of Sound from Action

## Summary

Applies the action-conditioned [JEPA](../concepts/world-models/jepa.md) world-model recipe to piano audio by making an explicit state/action split: **audio is the state, the pianoroll is the instrument action.** Given a current audio state and an action, predict the resulting future audio state. Trained fully **offline** on paired audio–pianoroll data with no environment interaction. Downstream: beat tracking, composer identification, key estimation — and **piano transcription performed as planning**, by searching for the action sequence that best explains a target sound.

## Why it is filed here despite being about music

The wiki's world-model material is entirely visual. This is a clean demonstration that the action-conditioned latent-prediction formulation is **substrate-independent** — and it is unusually well-posed as a control problem, in a way visual world models are not:

- **The action space is ground-truth and discrete.** A pianoroll *is* the action, exactly, with no estimation error. Visual world models must either be given actions or infer them; here the action channel is clean by construction.
- **Transcription-as-planning is inverse dynamics run as search.** "Searching for actions that best explain a target sound" is precisely the [inverse-dynamics mode](../concepts/world-models/world-action-model.md) of a world-action model — and here it has an exact ground-truth answer to score against, which manipulation tasks never do.

That makes it a useful *sanity environment* for claims about action-conditioned latent prediction, in the same spirit as PushT but with an unambiguous action channel.

## Key claims

- **Dynamics sensitivity.** The model assigns lower prediction error to correct (state, action, target) triplets than to perturbed ones. Win rates (fraction of perturbations that increase error):

| Model | Input state (temporal) | Input state (random) | Target state (temporal) | Target state (random) |
|---|---:|---:|---:|---:|
| **Music-JEPA** | **0.929** | 0.999 | **0.991** | 0.992 |
| AO-JEPA (audio-only, no action) | 0.787 | 0.986 | 0.576 | 0.984 |

The informative column is **target state / temporal: 0.991 vs 0.576.** A passive audio-only JEPA is close to chance at telling whether the *target* it is predicting is the right one in time; the action-conditioned model is near-perfect. **Action conditioning is what makes the latent dynamics temporally discriminative** — the audio-only model can score well on random perturbations (0.984) while being nearly blind to temporal ones.

- Loss difference **increases with temporal distance**. Lowest win rate (still > 0.8) is when the input is replaced with `s_{t+1}` — "partial tolerance to repetition," which is musically sensible.
- **Counterfactual synthesis**: given `(s_t, a_{t+1})`, the model predicts the resulting audio, and swapping in a different action produces a correspondingly different prediction.
- Action perturbations tested include **pitch shifts, temporal shifts, velocity scaling**.

### Setup

**MAESTRO v3.0.0** — ~200 hours of piano with time-aligned MIDI from Yamaha Disklavier pianos, primarily classical, standard splits. Spectrogram patches 25×15 → 256 state patches; pianoroll patches 25×6 → 240 action patches; D = 256. State encoder 12 layers, action encoder 8, both predictors 6 layers; d_model 256, d_ff 512, 4 heads. **~19M parameters total** (6.5M state encoder, 4.9M state predictor, 4.3M action encoder, 3.3M action predictor). λ = 0.5, EMA momentum τ = 0.95, Adam, single A100, batch 128, 15–25 epochs. Baselines: **AO-JEPA** (re-implemented audio-only JEPA, following Audio-JEPA / A-JEPA) and **MERT** (large pretrained music model, non-JEPA).

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md); Ziyu Wang, Kun Fang.
- **MAESTRO, MERT, AO-JEPA** — no pages.

## Concepts touched

- [JEPA](../concepts/world-models/jepa.md) — action-conditioned variant outside vision.
- [World-action model](../concepts/world-models/world-action-model.md) — transcription-as-planning is the inverse-dynamics mode.
- [World model](../concepts/world-models/world-model.md).

## Open questions

- **No downstream numbers extracted for the MIR tasks** (beat tracking, composer ID, key estimation) or for transcription accuracy — the extracted text covers the dynamics evaluation; the MIR and transcription tables were not recovered cleanly. Treat this page as covering the *dynamics* result only.
- **Piano only, one dataset, ~19M parameters.** No claim of scale.
- **Notable in the reference list, not the wiki:** two further LeCun world-model papers this ingest did not cover — *"Closing the train-test gap in world models for gradient-based planning"* (arXiv 2512.09929) and *"Temporal straightening for latent planning"* (arXiv 2603.12231). Both look squarely relevant to the wiki's latent-planning thread.
