---
title: Physical reasoning benchmarks and the human baseline
type: concept
created: 2026-08-31
updated: 2026-08-31
sources: 1
tags: [physical-reasoning, intuitive-physics, phyre, virtual-tools, physion, auccess, human-baseline, cognitive-science, benchmark, active-exploration]
---

**Physical reasoning benchmarks** ask whether an agent understands how the physical world behaves — and, distinctively, they usually ask it **against a measured human baseline on identical stimuli**. That inheritance is from cognitive science rather than machine learning, and it makes this family different in kind from the [world-model evaluation](world-model-evaluation.md) landscape the wiki otherwise tracks.

## Two traditions that don't cite each other

| | **Generative-video tradition** | **Cognitive-science tradition** |
|---|---|---|
| Question | Does generated video obey physics? | Can the agent *solve* a physical problem? |
| Ground truth | Human annotation or a model judge | Task success, plus a human baseline |
| Benchmarks | VBench, VideoPhy, [Physion-Eval](../../sources/physion-eval-paper.md), [WorldArena](../../entities/worldarena.md) | **PHYRE**, **Virtual Tools**, Physion / Physion++ |
| Metric | Glitch rate, perceptual score, Youden's J | **AUCCESS** — success weighted toward fewer attempts |
| In this wiki | well covered | **thin — this page and [Causal-PIK](../../sources/causal-pik-paper.md)** |

The wiki reached the second tradition late and by accident: the [Physion-Eval](../../sources/physion-eval-paper.md) ingest noted the gap explicitly, and [Causal-PIK](../../sources/causal-pik-paper.md) turned out to sit squarely in it.

## The benchmarks

**PHYRE** (Bakhtin et al. 2019) and **Virtual Tools** (Allen et al. 2020) are 2D single-intervention puzzles: place one object, gravity runs, did the red ball reach the green region. They look trivial and are not — hard for humans, and hard in a specific way. **The dynamics are unknown, so the solution cannot be planned; it must be actively explored.** That makes them a test of *learning from failure* rather than of prediction.

**AUCCESS** is the metric: success percentages aggregated with weights `w_k = log(k+1) − log(k)`, which pushes credit toward solving in **fewer attempts**. Sample-efficiency is the quantity, not final accuracy.

**Scale matters and is usually hidden.** PHYRE's full action space is **2,555,904 actions per puzzle**. Most published agents search a 1K or 10K discretization — and Bakhtin et al.'s own analysis shows DQN's AUCCESS *degrades* as the number of ranked actions grows. **A score without its action space is uninterpretable.**

## What the human baseline buys

Two things nothing else in the wiki's evaluation coverage provides.

**A ceiling that is not a leaderboard artifact.** On Virtual Tools, humans score 53.25 AUCCESS. On PHYRE at 10 attempts, 36.6. These are hard numbers to argue with, and they anchor claims that otherwise float.

**A second axis: alignment, separate from performance.** [Causal-PIK](../../sources/causal-pik-paper.md) reports per-puzzle correlation with humans alongside raw score, and the two come apart. On Virtual Tools, SSUP correlates better with humans (r = 0.71) than Causal-PIK does (0.63) — while Causal-PIK *scores higher*, because it solves puzzles humans find very hard. On PHYRE the ordering flips (Causal-PIK r = 0.73).

> [!note] Beating humans and thinking like humans are different measurements
> Almost every benchmark in this wiki collapses them. This family separates them by construction, which is why a purpose-built agent can be simultaneously *better than* and *less like* people. Worth importing into robot-policy evaluation, where "matches human teleoperator success rate" is routinely treated as if it implied similar competence structure.

> [!warning] Always quote the attempt budget
> Causal-PIK beats humans on Virtual Tools and on PHYRE at 100 attempts. Under a **matched 10-attempt budget on PHYRE, humans win 36.6 to 24.8.** The headline result is partly a statement about persistence. Any "beats humans" claim from this family needs its budget attached.

## The finding with the widest reach

Causal-PIK's robustness ablation: training its dynamics model on test templates improves bounding-box L2 error from **19.3 → 3.56** (≈5×), and AUCCESS rises only **41.6 → 45** (4 points).

**A 5× better world model buys 4 points.** The method needs the *relative ordering* of causal effects, not accurate prediction. If that generalizes, it is a much cheaper specification than the one [stable-worldmodel](../../sources/stable-worldmodel-paper.md) and [WorldRoamBench](../../entities/worldroambench.md) measure against — and it partly defuses the [fixed-width-latent](belief-states-and-mixed-states.md) objection Blackwell raises, since an ordering survives compression that a trajectory does not.

## The contradiction sitting in the wiki

Two human-comparison results now point opposite ways, and nothing here reconciles them:

- [**Physion-Eval**](../../sources/physion-eval-paper.md): *untrained* humans vastly out-detect the best MLLM critics at spotting physical implausibility — Youden's J of 24.9–61.8% versus 9.8–19.1%.
- [**Causal-PIK**](../../sources/causal-pik-paper.md): a purpose-built agent out-*solves* humans on physical puzzles at generous budgets.

**Physical judgment and physical problem-solving are apparently not the same capability.** One is recognizing that something violates physics; the other is searching for an action that exploits it. No source in this wiki examines the split.

## Related concepts

- [World-model evaluation](world-model-evaluation.md) — the generative-video side, and the perceptual/utility/coherence axes.
- [Belief states and mixed states](belief-states-and-mixed-states.md) — a GP posterior over action outcomes *is* a belief, updated by acting.
- [Inductive bias](../learning/inductive-bias.md) — Causal-PIK is a clean case study: swapping an RBF kernel for a physics-informed one is worth 23 AUCCESS points on the same algorithm.
- [Gradient-based planning](gradient-based-planning.md) — the alternative search regime; Bayesian optimization is the sample-efficient derivative-free branch.

## Key references

- [Causal-PIK](../../sources/causal-pik-paper.md) — Parés-Morlans et al., ICML 2025. The anchor; includes a new n=50 IRB-approved PHYRE human study.
- **PHYRE** (Bakhtin et al. 2019), **Virtual Tools** (Allen et al. 2020), **SSUP** (Allen et al. 2020) — not ingested.
- **Physion** (Bear et al. 2021) and **Physion++** (2023) — human-vs-model physical *prediction*; not ingested, on the [backlog](../../backlog.md).
- Battaglia et al. 2013, Smith et al. 2018 — the intuitive-physics-engine line, and the work [Josh Tenenbaum](../../entities/josh-tenenbaum.md)'s stub page flags as uncovered.

## Mentioned in

- [Causal-PIK paper](../../sources/causal-pik-paper.md)
- [Physion-Eval paper](../../sources/physion-eval-paper.md)
- [World-model evaluation](world-model-evaluation.md)
