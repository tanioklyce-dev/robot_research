---
title: "Evaluating the World Model Implicit in a Generative Model (Vafa, Chen, Rambachan, Kleinberg & Mullainathan, NeurIPS 2024)"
type: source
url: https://arxiv.org/abs/2406.03689
fetch_url: https://arxiv.org/pdf/2406.03689v3
local_path: raw/vafa-world-model-implicit_2406.03689.pdf
sha256: 36b330af8f170f6f195dc7fead4da7b9cfd77a318576475bdbd1b5c7e0475dfc
author: "Keyon Vafa, Justin Y. Chen, Ashesh Rambachan, Jon Kleinberg, Sendhil Mullainathan"
affiliations: Harvard University; MIT; Cornell University
published: 2024-06-06
venue: NeurIPS 2024
tags: [world-model-evaluation, myhill-nerode, dfa, implicit-world-model, sequence-model, transformer, coherence, navigation, othello, llm, benchmark, primary-source]
ingested: 2026-08-31
---

## Summary

If a sequence model has "learned a world model," what would that mean, and how would you check? This paper gives the first answer in the wiki that is **a theorem rather than a probe**. Restrict to domains whose underlying reality is a **deterministic finite automaton** — games, logic, state tracking, navigation — and the classic **Myhill-Nerode theorem** says the DFA's states are exactly the equivalence classes of prefixes that admit the same set of valid suffixes. So world-model recovery decomposes into two testable halves:

- **Sequence compression** — two prefixes reaching the *same* state must admit the *same* continuations. (Does the model over-distinguish?)
- **Sequence distinction** — two prefixes reaching *different* states must be separated by some suffix valid at one and not the other. (Does the model under-distinguish?)

The finding is that models pass the field's existing diagnostics and fail these. A transformer trained on NYC taxi rides finds valid routes **96–99%** of the time and produces the **true shortest path 97%** of the time; its next-token legality is **1.00** and a linear probe recovers the current intersection **91%** of the time. Its compression precision is **0.10**.

Reconstructing the map implied by the model's own generations gives a Manhattan containing **streets whose orientations are physically impossible** — an edge labelled NW that faces east — and **flyovers passing above other streets**. The control matters: corrupting *true* sequences at the same error rate produces a map far closer to reality, so this is not transcription noise on top of a good map. It is an incoherent map.

> [!note] Why this belongs near the top of the wiki's evaluation thread
> The wiki's [world-model evaluation](../concepts/world-models/world-model-evaluation.md) landscape is mostly **perceptual or utility** scoring. Vafa et al. add the third thing: **internal coherence, measured against a formal ground truth.** It is also the cleanest published demonstration of a claim this wiki keeps meeting informally — that **task success and world-model quality are different variables** — and it is the paper [Physion-Eval](physion-eval-paper.md) and [WorldArena](worldarena-paper.md) are groping toward without the benefit of a DFA.

> [!note] The subject of a keynote's second half
> **Dave Donoho** walked through this paper's Manhattan taxi experiment at the [third World Modeling Workshop](chicago-booth-world-modeling-workshop-2026.md) (Chicago Booth, 2026-08-31, ~01:15), in a keynote whose first half was on **David Blackwell**. The pairing is apt and, in the transcript, unremarked: Blackwell formalized the belief state; this paper measures how badly a sequence model recovers one.

## The metrics

Given a DFA `W` and two states `q₁, q₂`:

- **Myhill-Nerode boundary** — the set of *minimal* suffixes accepted at `q₁` but not `q₂`. The shortest evidence that the two states differ.
- **Myhill-Nerode interior** — sequences too short to tell them apart.

A model's *implied* boundary is computed by asking which suffixes it assigns probability above a threshold `ε` (0.01 throughout), and compared to the true boundary to give **distinction precision** and **distinction recall**. **Compression precision** samples two prefixes reaching the same state and checks whether the model admits the same suffixes for both.

The two are independent, and the paper shows a model can pass one and fail the other — which is the argument for reporting both.

## Results

**NYC navigation (Table 1)** — 4,580 intersections, 9,846 streets, from NYC Taxi & Limousine Commission pickup/dropoff data. GPT-2-architecture transformers (89.3 M for shortest paths, 1.5 B for the others) trained three ways:

| Model | Next-token test | Current-state probe | **Compression precision** | **Distinction precision** | **Distinction recall** |
|---|---|---|---|---|---|
| Untrained transformer | 0.03 | 0.10 | 0.00 | 0.00 | 0.00 |
| Shortest paths | **1.00** | 0.91 | **0.10** | 0.35 | 0.20 |
| Noisy shortest paths | **1.00** | 0.92 | **0.05** | 0.37 | 0.24 |
| Random walks | **1.00** | 0.99 | **0.50** | 0.99 | 1.00 |
| True world model | 1.00 | — | 1.00 | 1.00 | 1.00 |

Read the first two columns and every trained model looks solved. Read the last three and only the random-walks model is close, and even it fails compression **half** the time.

**Detour fragility (Table 2)** — the practical consequence. Fraction of traversals still valid as detours are injected:

| Training data | 0% | 1% | 10% | 50% | 75% |
|---|---|---|---|---|---|
| Shortest paths | 0.99 | 0.69 | **0.08** | 0.00 | 0.00 |
| Noisy shortest paths | 0.96 | 0.52 | **0.03** | 0.00 | 0.00 |
| Random walks | 0.99 | 0.99 | 1.00 | 0.97 | 0.74 |

A **1%** detour rate takes the shortest-paths model from 0.99 to 0.69. At 10% it is at 0.08. The model that plans beautifully cannot re-route.

**Othello** — applying the metrics to the two models of Li et al.: the one trained on **real championship games performs poorly** on both metrics, the one trained on **synthetic games performs well**, and the existing diagnostics show them as similar. The detour exercise confirms it.

**Logic puzzles (Figure 4)** — seating-arrangement puzzles with chain-of-thought:

| Model | Task accuracy | Compression precision | Distinction recall |
|---|---|---|---|
| GPT-4 | **1.00** | 0.21 | 0.56 |
| Qwen 1.5 (110B) | 0.98 | 0.53 | 0.53 |
| Llama-3 (70B) | 0.98 | 0.25 | 0.57 |
| GPT-3.5 turbo | 0.83 | 0.33 | 0.18 |
| True world model | 1.00 | 1.00 | 1.00 |

**GPT-4 solves the puzzle perfectly with a compression precision of 0.21.** That single row is the paper's thesis in miniature.

> **The recurring structural finding:** across navigation *and* Othello, **models trained on random or synthetic data recover more structure than models trained on real-world data.** Real traversals are shortest paths and expert games — they never visit the state space broadly enough for the model to learn that different prefixes reach the same state. Coverage of the state space, not realism of the data, is what builds a coherent world model.

## Stated limitation

**The DFA restriction.** The framework needs a ground truth expressible as a deterministic finite automaton, which covers games, logic and state tracking but not continuous or unknown dynamics. The authors suspect compression and distinction generalize and leave it to future work.

## Entities mentioned

- **Keyon Vafa** (Harvard), **Justin Y. Chen**, **Ashesh Rambachan**, **Sendhil Mullainathan** (MIT), **Jon Kleinberg** (Cornell). No wiki pages.
- Models evaluated: GPT-4, GPT-3.5-turbo, Llama-2 70B, Llama-3 8B/70B, Mixtral 8x22B, Qwen 1.5 72B/110B.
- **NYC Taxi & Limousine Commission** data; **Othello-GPT** (Li et al.) as the reused prior setup.

## Concepts touched

- [World-model evaluation](../concepts/world-models/world-model-evaluation.md) — the coherence axis this adds.
- [Belief states and mixed states](../concepts/world-models/belief-states-and-mixed-states.md) — Myhill-Nerode equivalence classes are the deterministic, observable-alphabet cousin of the mixed states in [Blackwell's construction](jurgens-crutchfield-hmp-entropy-rate.md).
- [World model](../concepts/world-models/world-model.md) — what the term is being made to mean here.
- [Chain-of-thought](../concepts/learning/chain-of-thought.md) — the LLMs were prompted with CoT and still failed compression.

## Open questions

- **Does the coverage finding transfer to robot data?** "Random/synthetic beats real" is a direct challenge to the wiki's teleoperation-data orthodoxy — [Mobile ALOHA](mobile-aloha-paper.md), [DROID](../entities/droid.md), [Figure's Index](../entities/figure-index.md) all collect *expert* demonstrations, which is precisely the shortest-paths regime that produced compression precision 0.10 here. Nobody has run a compression-style test on a VLA.
- **Detour fragility is the robotics failure mode with a different name.** A 1% perturbation collapsing performance from 0.99 to 0.69 is what [Flexion Reflect](flexion-reflect-v1.md) describes as compounding failure and what [stable-worldmodel](stable-worldmodel-paper.md) measures as distribution shift. Three literatures, one phenomenon, no shared metric.
- **What replaces the DFA for continuous control?** The paper's own stated gap, and the thing standing between these metrics and any use on a robot policy.
