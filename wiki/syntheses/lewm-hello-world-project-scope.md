---
title: LeWM hello world — Project 1 detailed scope
type: synthesis
created: 2026-05-08
updated: 2026-05-08
tags: [leworldmodel, lewm, jepa, pusht, project-scope, reproduction, education]
---

# LeWM hello world — Project 1 detailed scope

Detailed working plan for Project 1 of the [JEPA project ladder](jepa-project-ladder-rosorin-pro.md). Reproduces LeWM's PushT planning result, builds intuition for the planner-as-cost-model pattern, and produces a from-scratch checkpoint that downstream projects (probing in Project 2, sim deployment in Project 4) can build on.

## Status as of 2026-05-08

Install verified during the [LeWM howto](leworldmodel-howto.md) live install on RTX 5070 WSL2. On disk:

- `~/projects_tanio/lewm/le-wm/` — `lucas-maes/le-wm` repo cloned.
- `~/.stable-wm/hf_pusht/weights.pt` + `config.json` — HF `quentinll/lewm-pusht` downloaded.
- `~/.stable-wm/pusht/lewm_object.ckpt` — converted to `swm.policy.AutoCostModel`-loadable format.

Project 1's plumbing is done. Remaining work is **running the model and building intuition** — not tooling.

## Success criteria

By the end you can answer four questions with your own evidence:

1. Does pretrained LeWM match the [paper](../sources/leworldmodel-paper.md)'s PushT planning success rate on your machine?
2. Does training-from-scratch reproduce the pretrained behavior?
3. What do the two losses (next-embedding MSE + SIGReg) actually look like during training?
4. How does planning success degrade as you change one knob (horizon, CEM samples, or training-data fraction)?

**Total time**: ~2.5 working days.

## Prerequisite reading

Before Phase 1, read [PushT § Concrete mechanics](../entities/pusht.md) to understand exactly what the planner is operating on: the gray-T-on-target visual scene, the 2D continuous action space, the no-grasping push-only constraint, and why the task is hard despite being 2D. This is the substrate for every observation, action, and reward you'll see in the next four phases.

## Phase 1 · Reproduce pretrained PushT eval (~half day)

Run the planner against the converted checkpoint and confirm it works.

```bash
cd ~/projects_tanio/lewm/le-wm
source ../.venv/bin/activate
python eval.py --config-name=pusht.yaml policy=pusht/lewm
```

### What to record
Success rate over N seeds, mean episode return, a few rendered rollouts. Save to `notes/phase1.md` alongside the repo.

### What to look at (the *learning* part)
- Open `config/eval/pusht.yaml` — note the planner's CEM hyperparameters (population size, horizon, iterations). These are the knobs for Phase 3.
- Step through `eval.py` once in a debugger or with prints: confirm the model is *not* a policy — it's invoked by the planner as a cost (latent prediction error against a goal embedding). This is the [JEPA](../concepts/jepa.md) cost-fn pattern from [JEPA task capabilities](jepa-task-capabilities.md) §3.
- Inspect `~/.stable-wm/hf_pusht/config.json` — note encoder size and predictor architecture. This is the 18M-param model you're running.

### Deliverable
Success-rate number comparable to the [LeWM paper](../sources/leworldmodel-paper.md)'s PushT result.

## Phase 2 · Train PushT from scratch + compare (~1 day)

Kick off your own training run and watch the loss curves.

```bash
# edit config/train/lewm.yaml: set wandb.config.entity / wandb.config.project
python train.py data=pusht
```

The paper claims ~hours on a single GPU; RTX 5070 should be in that range.

### What to look at
- WandB curves for the two losses: `loss_pred` (next-embedding MSE) and `loss_sigreg` (SIGReg variance/covariance regularizer). The whole reason for SIGReg is to **prevent representation collapse** — `loss_pred` should *not* go to zero trivially. If it does, SIGReg is failing.
- Per-step encoder gradient norm — JEPAs notoriously train unstably without the right objective; LeWM's two-loss design is what makes it stable. You should see this empirically.
- After training, run `eval.py` against your fresh checkpoint and compare to Phase 1's pretrained number. Within ~10pt is good; much worse means the training run hit an issue.

### Deliverable
Side-by-side plot of pretrained vs your-from-scratch eval success, plus the training curves.

## Phase 3 · One-knob ablation (~half day)

Pick **one** knob and sweep 4–6 values. Keep everything else fixed.

### Recommended knob: planning horizon (`planner.horizon`)
The 48× speedup claim from the [LeWM paper](../sources/leworldmodel-paper.md) vs foundation-model world models is partly a horizon-economics story; sweeping horizon makes the trade-off concrete.

```bash
for H in 4 8 16 32 64; do
  python eval.py --config-name=pusht.yaml policy=pusht/lewm planner.horizon=$H
done
```

### Alternatives if horizon proves uninteresting
- **CEM population size** — more samples = better plan, more compute. Expect a diminishing-returns curve.
- **Training-data fraction** — train on 25%, 50%, 100% of PushT trajectories. Plot eval success vs data. JEPA's sample-efficiency claim made concrete.

### Deliverable
Success rate vs knob value: one plot, a few lines of interpretation.

## Phase 4 · Writeup (~half day)

`notes/project-1-summary.md` with: install confirmation, four answered questions above, three plots (Phase 1 rollout, Phase 2 training curves, Phase 3 knob sweep). This is the evidence base — Project 2 (probing) builds on the trained checkpoint from Phase 2 here.

If results are interesting, file a `wiki/syntheses/lewm-pusht-reproduction.md` so the work compounds — this is the kind of **empirical result the wiki currently lacks** (everything to date is paper-derived, not reproduced locally).

## Risk register

- **WandB account**: free tier is fine. To skip entirely, set `wandb=disabled` in Hydra config or swap to TensorBoard.
- **WSL2 + headless rendering**: PushT eval may try to open a viewer. If it hits `cannot connect to X server`, set `MUJOCO_GL=egl` or equivalent off-screen GL backend.
- **CEM is stochastic**: single-seed eval numbers are noisy. Run ≥3 seeds for any comparison that matters.
- **Phase 2 mode-collapse canary**: SIGReg exists exactly to prevent it, so the bug *shouldn't* surface — but if `loss_pred` drops to zero immediately, that's the diagnostic.

## How this connects to the rest of the ladder

- **Project 2 (latent probing)** reuses the from-scratch checkpoint trained in Phase 2 — freezes it, attaches linear probes.
- **Project 3 (surprise detector on ROSOrin Pro)** reuses the *pretrained* checkpoint loaded in Phase 1 — applies it to real-robot RGB.
- **Project 4 (Gazebo PushT for ROSOrin Pro)** reuses the training pipeline from Phase 2 — swaps the dataset and the action space.

Phase 1 + Phase 2 together are the foundation for everything downstream. Knob sweep (Phase 3) is optional but cheap.

## Sources used

- [LeWorldModel — train and run howto](leworldmodel-howto.md) — install / train / eval recipe + the four documented gotchas.
- [LeWorldModel Paper](../sources/leworldmodel-paper.md) — model, two-loss design, PushT result.
- [LeWorldModel entity](../entities/leworldmodel.md) — capability summary.
- [JEPA task capabilities](jepa-task-capabilities.md) — planner-as-cost-fn pattern (§3) and probing/interpretability (§7).
- [JEPA project ladder for ROSOrin Pro](jepa-project-ladder-rosorin-pro.md) — parent ladder.
- Live install state at `~/.stable-wm/` and `~/projects_tanio/lewm/le-wm/` as of 2026-05-08.

## Related

- [JEPA project ladder for ROSOrin Pro](jepa-project-ladder-rosorin-pro.md) — parent.
- [LeWorldModel howto](leworldmodel-howto.md) — recipe-level companion.
- [LeWM on ROSOrin Pro — feasibility analysis](lewm-on-rosorin-pro-feasibility.md) — context for why the from-scratch checkpoint matters downstream.
