---
title: "Causal-PIK: Causality-based Physical Reasoning with a Physics-Informed Kernel (Parés-Morlans et al., ICML 2025)"
type: source
url: https://arxiv.org/abs/2505.22861
fetch_url: https://arxiv.org/pdf/2505.22861v1
local_path: raw/causal-pik_2505.22861.pdf
sha256: 956b9ba359ade59bce128fbcc04d7ff0cba90ad2146763a60e60ed56a40c76bd
author: "Carlota Parés-Morlans, Michelle Yi, Claire Chen, Sarah A. Wu, Rika Antonova, Tobias Gerstenberg, Jeannette Bohg"
affiliations: Stanford University; University of Cambridge
published: 2025-05-28
venue: "ICML 2025 (PMLR 267)"
tags: [causal-pik, physical-reasoning, intuitive-physics, phyre, virtual-tools, bayesian-optimization, gaussian-process, kernel, human-baseline, cognitive-science, active-exploration, primary-source]
ingested: 2026-08-31
---

## Summary

> [!note] Presented at the [third World Modeling Workshop](chicago-booth-world-modeling-workshop-2026.md) (Chicago Booth, 2026-08-31, ~03:16) in [Bohg](../entities/jeannette-bohg.md)'s invited talk on world models from a robotics perspective.


**Causal-PIK** solves single-intervention physical-reasoning puzzles — place one object, let gravity run, see what happens — by putting **physics intuition inside the kernel of a Gaussian process** and running Bayesian optimization over actions. The premise is that these tasks cannot be planned in advance because the dynamics are unknown; they must be *actively explored*, and the only thing that matters is **learning as much as possible from each failed attempt**.

The insight is where the physics goes. A standard RBF kernel assumes actions that are *geometrically* close have similar outcomes — which is exactly wrong here, since a centimetre's difference in where you drop a block can send a ball to the goal or nowhere near it. The **Physics-Informed Kernel** instead measures whether two actions produce **similar causal effects**, using a learned dynamics model to predict the immediate consequence of each action and comparing those predictions.

> [!note] This closes a gap the wiki had explicitly flagged
> When [Physion-Eval](physion-eval-paper.md) was ingested, the wiki noted it had **nothing** from the cognitive-science tradition of physical reasoning — the one that asks whether a model's physical predictions match *humans'* on identical stimuli. This is that literature: **PHYRE** and **Virtual Tools** are its benchmarks, **AUCCESS** its metric, and the paper runs a **new n=50 IRB-approved human study** rather than citing one. It also names [Josh Tenenbaum](../entities/josh-tenenbaum.md)-lineage work (Battaglia, Smith, Allen) as its foundation — the intuitive-physics line his stub page flags as uncovered.

## The method

**Bayesian optimization over actions**, with the GP's kernel carrying the domain knowledge:

```
initialize X, y with 9 warm-up rollouts (not counted as attempts)
while not solved:
    gp ← GP(X, y, PhysicsInformedKernel)
    xᵢ ← CausalityBasedActionSelection(gp)
    yᵢ, success ← Execute(xᵢ)
    append
```

**Causality-based action selection** — sample 500 candidates with a Sobol sequence, score with a **UCB** acquisition function, then take the **top 5** and approximate their outcomes with a probabilistic physics simulation, choosing the best. The authors are explicit that this last step "mimics how humans use mental representations to imagine the potential effects of actions before committing."

**The Physics-Informed Kernel** encodes two separable intuitions:
1. **Causal effect** — a learned dynamics model (**RPIN**, Region Proposal Interaction Networks) predicts the next `n_pred` bounding boxes given an action and initial state. `n_pred` is deliberately **short**, capturing only the immediate effect rather than the full rollout.
2. **Causal similarity** — how alike are two actions' predicted effects. Computed as **cosine similarity** of the induced state-change directions combined with **magnitude similarity**, and shown to be a valid kernel.

The qualitative payoff (Fig. 4): given the same observations, the physics-informed posterior splits the action space into three legible regions — actions that move the ball toward the goal, actions that move it away, and unexplored actions that cause no movement at all. The RBF posterior takes many more attempts to become that informative.

## Results

**Virtual Tools** (20 puzzles, 100 tests each, max 10 attempts):

| Model | AUCCESS ↑ |
|---|---|
| **Ours: Causal-PIK** | **65.0 ± 25.0** |
| SSUP (Allen et al. 2020) | 58.0 ± 27.0 |
| **Humans** (Allen et al. 2020) | **53.25 ± 23** |
| Ours: RBF ablation | 42.0 ± 33.0 |
| DQN | 25.0 ± 24.0 |
| RAND | 16.0 ± 20.0 |

**PHYRE-1B Cross** (25 tasks × 10 folds, max 100 attempts):

| Model | AUCCESS ↑ | Action space |
|---|---|---|
| RPIN (Qi et al. 2021) | 42.2 ± 7.1 | 10K reduced |
| Ahmed et al. 2021 | 41.9 ± 8.8 | 10K reduced |
| **Ours: Causal-PIK** | **41.6 ± 9.33** | **full** |
| Dec [Joint] (Girdhar et al. 2020) | 40.3 ± 8 | 1K reduced |
| DQN | 36.8 ± 9.7 | 10K reduced |
| Harter et al. 2020 | 30.24 ± 8.9 | full |
| Ours: RBF ablation | 27.70 ± 9.68 | full |
| **Humans @10 attempts** | **36.6 ± 10.2** | — |
| Ours: Causal-PIK @10 attempts | 24.8 ± 9.22 | full |

**The RBF ablation is the cleanest evidence in the paper.** Same algorithm, same budget, only the kernel changes: 65.0 vs 42.0 on Virtual Tools, 41.6 vs 27.70 on PHYRE. The physics is doing the work, not the Bayesian optimization.

> [!warning] Read the attempt budget before quoting "beats humans"
> Causal-PIK beats humans on Virtual Tools (65.0 vs 53.25) and on PHYRE at 100 attempts. **Under a matched 10-attempt budget on PHYRE, humans win decisively — 36.6 vs 24.8.** The headline is a statement about persistence as much as about reasoning. The paper reports this plainly; anyone citing the result should carry the budget with it.

**The action-space caveat cuts the other way, in the method's favour.** PHYRE's full action space is **2,555,904 actions per puzzle**. The baselines Causal-PIK ties with are searching a **1K–10K discretization**; Causal-PIK searches the whole continuous space. The authors argue discretizing "is an unrealistic constraint when aiming to develop generalist algorithms," and cite Bakhtin et al.'s own finding that DQN's AUCCESS *degrades* as the number of ranked actions grows.

## Human alignment

A **new human study**: n=50 Prolific participants, one variation of each of 25 PHYRE puzzles, 10 attempts each, mouse-drawn actions, freeze-frame then gravity, Stanford IRB approved.

Per-puzzle correlation between model and human scores:

| Benchmark | Most human-like | Then | Then |
|---|---|---|---|
| Virtual Tools | SSUP **r = 0.71** | Causal-PIK 0.63 | DQN 0.32 |
| PHYRE | Causal-PIK **r = 0.73** | Causal-PIK@10 0.71 | RBF 0.64, Harter 0.55 |

The authors' own reading of the Virtual Tools result is honest and interesting: Causal-PIK is *less* correlated with humans than SSUP **while scoring higher**, because it solves several puzzles humans find very hard — which depresses per-puzzle correlation. **Beating humans and thinking like humans are different axes**, and this paper measures both rather than conflating them.

## Robustness to a bad dynamics model

The ablation worth remembering. Training the PHYRE dynamics model on *test templates* (prior exposure) improves bounding-box L2 error from **19.3 ± 4.55 to 3.56** — a 5× accuracy gain. AUCCESS improves from **41.6 to 45**, four points.

**A 5× better world model buys 4 points.** The kernel needs only the *relative ordering* of causal effects, not accurate prediction — which is why the authors suggest it is a plausible sim-to-real candidate.

## Stated limitations

- **No knowledge sharing across tasks.** Every puzzle starts cold; recognizing that two puzzles share dynamics is future work.
- Noisy causal predictions introduce misleading similarities, though the robustness result above bounds the damage.
- The action space here is **3-dimensional**. Scaling higher needs a different causal-effect predictor, though the authors note **kernel equations 2–6 would be unchanged**, since new dimensions are absorbed into the predicted state.

## Entities mentioned

- [Jeannette Bohg](../entities/jeannette-bohg.md) — senior author. **Carlota Parés-Morlans** also appears on the unpublished **MessyNav** ([backlog](../backlog.md)); **Rika Antonova** on [Sentinel](sentinel-paper.md).
- **Tobias Gerstenberg** — Stanford cognitive scientist working on causal judgment; the reason this paper has a real human study rather than a cited one. No wiki page.
- **PHYRE** (Bakhtin et al. 2019) and **Virtual Tools** (Allen et al. 2020) — the benchmarks. Neither ingested; both new to the wiki.
- **RPIN** — the dynamics-model architecture. **SSUP** — the Virtual Tools state of the art it beats.
- Acknowledges **Kelsey Allen** and **Kevin Smith** — the Virtual Tools / intuitive-physics cognitive-science group.

## Concepts touched

- [Physical reasoning benchmarks](../concepts/world-models/physical-reasoning-benchmarks.md) — the concept page this anchors.
- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — a fourth axis: not perceptual quality, not utility, not coherence, but **sample-efficiency against a human baseline**.
- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md) — the GP posterior over action outcomes *is* a belief, updated by acting; the same object Blackwell formalizes.
- [Gradient-based planning](../concepts/world-models/gradient-based-planning.md) — the alternative search regime; BO is the sample-efficient, derivative-free branch.
- [Inductive bias](../concepts/learning/inductive-bias.md) — the paper is a case study in it. The kernel *is* the prior, and swapping RBF for a physics-informed one is worth 23 AUCCESS points.

## Open questions

- **The 5×-accuracy-for-4-points result deserves to be tested elsewhere.** If a world model only needs to rank effects rather than predict them, that is a very different specification from the one [WorldRoamBench](../entities/worldroambench.md) and [stable-worldmodel](stable-worldmodel-paper.md) measure against — and a much cheaper one. It would also partly defuse the [fixed-width-latent](../concepts/world-models/belief-states-and-mixed-states.md) worry Blackwell raises.
- **Nothing here touches a real robot.** Both benchmarks are 2D. The authors gesture at sim-to-real; no result supports it yet.
- **The wiki now has two human-comparison results pointing opposite ways.** [Physion-Eval](physion-eval-paper.md): untrained humans massively out-detect MLLM critics on physical realism. Causal-PIK: a purpose-built agent out-*solves* humans on physical puzzles at generous budgets. Physical **judgment** and physical **problem-solving** are apparently not the same capability, and no source here examines why.
