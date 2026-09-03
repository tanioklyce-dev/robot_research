---
title: "galilai-group/tutorial — Tiny LeJEPA and LeWM tutorials (WM@Booth Day 3 material)"
type: source
url: https://github.com/galilai-group/tutorial
author: "Randall Balestriero (GalilAI group / Brown University)"
published: 2026-09-02
ingested: 2026-09-02
venue: GitHub repository
format: code (4 Python modules, 897 lines)
tags: [lejepa, lewm, sigreg, tutorial, world-model, moving-mnist, imagenette, stable-pretraining, workshop, balestriero, reproducible]
---

# Tiny LeJEPA and LeWM tutorials

## Summary

Four Python files — **897 lines total** — that train a [LeJEPA](lejepa-paper.md) encoder and an action-conditioned [LeWM](../entities/leworldmodel.md) world model from scratch, each in **under thirteen minutes on one GPU**, and then let you *drive the world model interactively in a browser*. Almost certainly the hands-on material for **Day 3** of the [Chicago Booth world-modeling workshop](chicago-booth-world-modeling-workshop-2026-day2.md). The provenance is about as tight as it gets: the repository contains **exactly two commits — `first` and `cleanup` — both by RandallBalestriero, both on 2026-09-02**, the later at 13:18 UTC, hours before the Day 3 stream. It was created that day, and the programme describes Day 3 as *"a hands-on coding workshop with tutorials and a modeling challenge."*

> [!note] Why this is the most useful LeJEPA source in the wiki
> Everything else here on this line is a paper, a full research platform, or an 8-hour reproduction. This is the **smallest complete artifact that exhibits both halves of the program** — the SSL objective and the action-conditioned world model — with published wall-clock times, published numbers, and a working demo. The existing [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) documents a multi-hour install-and-train against a research repo; this trains in twelve minutes on a laptop-scale problem and is the better on-ramp.

## The three programs

| File | What it trains | Reported result |
|---|---|---|
| `inet10.py` (129 lines) | ResNet9 LeJEPA on 64×64 ImageNette | **76.7% final / 78.1% peak** online linear probe in **8m29s** |
| `mmnist.py` (329 lines) | Action-conditioned LeWM on Moving MNIST | **12m28s**; see the probe table below |
| `app.py` (278 lines) | Interactive open-loop viewer for a trained LeWM | — |
| `utils.py` (161 lines) | The actual `LeJEPA` and `LeWM` modules | — |

Sole dependency is `stable-pretraining` (`spt`), the same lab's SSL library — which is where **SIGReg actually lives** (`stable_pretraining.methods.lejepa.SlicedEppsPulley`), not in the standalone [`lejepa`](lejepa-github.md) package.

The published ImageNette command, which is the whole configuration:

```bash
python inet10.py --epochs 29 --views 3 --slices 1024 \
  --lr 1.8e-3 --probe-lr 3e-3 --lamb 0.01 --batch-size 256 --workers 16
```

Constant-LR AdamW, three augmented views, 1,024 SIGReg slice directions, λ = 0.01. No scheduler, no teacher, no stop-gradient — the [LeJEPA](../concepts/world-models/sigreg.md) claim, exhibited at a size anyone can check.

## The LeWM in 60 lines — and what it reveals

The `LeWM` class is the clearest statement of the objective in this wiki, because there is nothing else in it:

- **Encoder**: ResNet9, 1 channel → 64-dim latent.
- **Predictor**: a 3-layer MLP, `(latent ⊕ action) → latent`. That is the entire dynamics model.
- **Loss** = one-step teacher-forced MSE **+ `rollout_weight` × recursive open-loop rollout MSE** + λ · SIGReg.

The rollout term is the part worth noticing. Training does not only predict one step ahead from ground-truth latents; it **unrolls the predictor from the first frame through all 8 actions and penalizes the drift**, at weight 1.0 by default. The wiki's [LeWM page](../entities/leworldmodel.md) describes a two-term loss; this shows the prediction term is itself two terms, and that open-loop stability is trained for directly rather than hoped for.

> [!note] Where do you apply the Gaussian constraint in a *temporal* model? Four answers, exposed as a flag
> `sigreg_mode` takes **`pooled`** (all `(N×T)` latents as one distribution — the default), **`per_time`** (a separate SIGReg per timestep, averaged), **`both`**, and **`pooled_pred`** (pooled over encoded latents *and* over the predicted rollout).
>
> This is a design question the wiki's [SIGReg](../concepts/world-models/sigreg.md) and [LeWM](../entities/leworldmodel.md) pages do not raise at all, and it is not obviously innocuous: `pooled` permits the marginal over all time to be isotropic Gaussian while any individual timestep's distribution is not. `pooled_pred` is the only mode that constrains the *predictor's own output* distribution, which is where rollout collapse would show up. **No comparison between the modes is published here** — the default is asserted, not defended.

## The Moving-MNIST setup, and the probe result that matters

The environment is deliberately minimal: **one MNIST digit, downsampled to 24×24, translated on a 64×64 canvas** by an observed action `(Δx, Δy)` drawn from `[-4, 4]²` and clamped to the canvas. Actions are normalized by 4. Eight steps per trajectory, 10,000 samples. An experimental **third action dimension** adds discrete −45° / 0° / +45° rotations (`--rotation-step 45`).

Because the generator knows the digit identity *and* the position, the training script probes for both — and that is the interesting part:

| Probe | Linear | 2-layer MLP |
|---|---|---|
| **Digit identity** (semantic) | 66.4% | 76.9% |
| **Position** (state), R² | **0.9195** | **0.9830** |

Plus latent rollout MSE **0.1247** and an online decoder MSE **0.00531**.

> [!note] The action-conditioned latent is far better at *state* than at *identity*, and that is the design working
> Position is recovered near-perfectly by a linear probe; digit class is not. A world model trained to predict *the consequences of actions* has every incentive to represent what the actions move and little incentive to represent what the thing is. That is precisely LeCun's *"eliminate the information you can't predict"* argument ([Day 1 panel](chicago-booth-world-modeling-workshop-2026.md)) showing up as a two-line probe table in a tutorial — and it is the same dissociation the wiki records in [Reconstruction or Semantics?](latent-space-robotic-world-models-paper.md) and the [DiT world-action model](dit-world-action-model-av-paper.md), reached at a scale where anyone can rerun it.
>
> It also sets up the obvious student exercise: the digit probe number is a **measure of what the world model threw away**, and whether you want it higher depends entirely on the downstream task.

## `app.py` — imagination you can steer

After a training run, `python app.py` serves an interactive viewer on `0.0.0.0:8000`. The mechanic is stated precisely in the README, and it is the pedagogically important bit:

> *"Only reset encodes a true image. Every arrow-key or button action after reset recursively advances the previous imagined latent."*

So after the first frame the model never sees the world again — the display is decoded pure imagination, and drift is visible in real time as you hold down an arrow key. The interface shows truth, decoded imagination, action history, and the full open-loop trajectory side by side.

This is the cheapest instrument in the wiki for the failure mode its world-model pages keep discussing abstractly: [long-horizon drift](../entities/worldtrace.md), [rollout degradation](../concepts/world-models/gradient-based-planning.md), and the [25 → 75 step collapse](../concepts/world-models/sigreg.md) the VISReg talk called *"a fundamental problem of the world model."*

## Key claims

- LeJEPA on ImageNette reaches **~77% linear-probe accuracy in ~8.5 minutes** on one datacenter GPU with a ResNet9 and no SSL heuristics.
- An action-conditioned latent world model on Moving MNIST trains in **~12.5 minutes** and recovers positional state at **R² 0.98** (MLP probe).
- CUDA runs use BF16 and `torch.compile` the encoder and projector automatically (`mode="reduce-overhead"`).
- Runs are reproducible by construction: `stable-pretraining`'s run manager writes `metrics.csv`, **frozen requirements**, and environment metadata under `runs/<date>/<time>/<run-id>/`.
- Smoke tests are first-class: `--steps 10 --workers 0 --no-compile` on both scripts.

## Caveats

> [!warning] Numbers are single-run, single-GPU, and self-reported
> "One datacenter GPU" is not identified. No seeds are swept, no error bars are given, and the two headline configurations are described as *"the measured speed/accuracy configuration"* and *"the clearest translation-only sweep configuration"* — i.e. selected after a sweep whose results are not published. Fine for a tutorial; not a benchmark.

- **Moving MNIST is not a control problem.** Actions are exogenous random walks, not chosen by a planner. Nothing here plans, so nothing here tests the thing world models are ultimately for. [stable-worldmodel](stable-worldmodel-github.md) is where planning lives.
- The rotation action is flagged **experimental**, and the published numbers are for the translation-only setting (`--rotation-step 0`).
- `pyproject.toml` lists a `debug_lewm` module that is **not in the repository** — a stale entry from the cleanup commit.

## Entities mentioned

- [Randall Balestriero](../entities/randall-balestriero.md) — sole committer. [LeWorldModel](../entities/leworldmodel.md), [stable-worldmodel](../entities/stable-worldmodel.md).

## Concepts touched

- [SIGReg](../concepts/world-models/sigreg.md) — `SlicedEppsPulley`, and the four temporal application modes.
- [JEPA](../concepts/world-models/jepa.md) · [world model](../concepts/world-models/world-model.md) · [latent space](../concepts/world-models/latent-space.md) · [world action model](../concepts/world-models/world-action-model.md).
- [Curriculum Module 12 — LeWM deep dive](../syntheses/curriculum/curriculum-12-lewm-deep-dive.md) and the [LeWM howto](../syntheses/world-models/leworldmodel-howto.md) — both of which this undercuts on cost.

## Open questions

- **Which `sigreg_mode` is right, and does it matter?** Four modes, one default, no ablation. This is a cheap, publishable experiment sitting in a tutorial repo — and it bears directly on whether SIGReg's guarantees survive the move from a static image distribution to a temporal one.
- **Does the digit/position probe gap widen with rollout length?** If the latent is discarding identity to keep state, longer horizons should sharpen the effect. Two flags and a rerun.
- **How does this scale to Push-T?** The gap between Moving MNIST and the wiki's [Push-T](../entities/pusht.md) results — where [stable-worldmodel](stable-worldmodel-paper.md) measured LeWM dropping from 50.8% to 6–26% under perturbation — is unbridged by anything here.
- **Day 3 itself is not ingested.** The stream (`PkaYC3fwEsc`) was still live with no captions as of 2026-09-02. See [backlog](../backlog.md).
