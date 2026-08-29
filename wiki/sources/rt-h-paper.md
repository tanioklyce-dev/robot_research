---
title: "RT-H: Action Hierarchies Using Language"
type: source
url: https://arxiv.org/abs/2403.01823
local_path: raw/2403.01823.pdf
sha256: e38aaea90d294c347b89ba093b4561e00e8d8fd5875e57b086ed84402605d544
author: Suneel Belkhale, Tianli Ding, Ted Xiao, Pierre Sermanet, Quan Vuong, Jonathan Tompson, Yevgen Chebotar, Debidatta Dwibedi, Dorsa Sadigh
venue: arXiv 2403.01823v2 (cs.RO), 23 pp.; Google DeepMind + Stanford
published: 2024-06-01
ingested: 2026-08-04
format: pdf
tags: [rt-h, action-hierarchy, language-motions, action-representation, controlled-natural-language, interactive-imitation-learning, corrections, rt-2, pali-x, vla, cross-embodiment]
---

# RT-H: Action Hierarchies Using Language

**Belkhale, Ding, [Xiao](../entities/ted-xiao.md), [Sermanet](../entities/pierre-sermanet.md), Vuong, Tompson, Chebotar, Dwibedi, [Sadigh](../entities/dorsa-sadigh.md)** — [Google DeepMind](../entities/google-deepmind.md) + Stanford. Project page: [rt-hierarchy.github.io](https://rt-hierarchy.github.io/).

## Summary

RT-H inserts a **language layer between the task and the action**. Given *"close the pistachio jar"* and an image, it first predicts a **language motion** — a short phrase like *"move arm forward"* or *"rotate arm right"* — and then predicts the low-level action conditioned on that phrase, the task, and the observation. One [PaLI-X](../entities/pali-x.md) 55B VLM serves both queries.

The motivating problem is **data sharing**. Language-conditioned policies share data across semantically similar tasks ("pick coke can" / "pick an apple"), but that sharing collapses as tasks diverge ("pick coke can" / "pour a cup"). The insight: *"pour a cup" and "pick up a coke can" **entirely overlap at the language motion level** until the object is picked.* Moving the shared representation down to the motion layer restores data sharing across tasks that share no task-level semantics.

This is the wiki's **primary source for the "is there a subset of natural language for robot actions?" question** — see [action representation languages](../syntheses/agents/action-representation-languages.md), which this ingest was requested to put on firm footing.

## Key claims

### The vocabulary is mechanically derived from proprioception (§III-C) — the most important detail

This is the part secondary coverage omits, and it changes what RT-H *is*.

Human labeling was tried and rejected: it produced *"language inconsistency across the dataset and even inaccuracy"* — annotators mislabeled skill transitions and misjudged motion direction from camera angles. Instead, the authors built an **automated extraction procedure**:

1. Map each dimension of the change in end-effector pose to a spatial word (the z-axis of position change → "up"/"down").
2. Do this for **all 9 action dimensions** — 3 delta position, 3 delta orientation, 2 base movement, 1 gripper.
3. Threshold out dimensions below a "small action" cutoff.
4. Compose the survivors **in order of action magnitude** → *"move arm forward and close gripper."*

The combinatorics yield **over 2,500 language motions with zero human annotation**. The procedure is fixed across all tasks and datasets — *"designing this procedure is a one-time fixed cost for the developer."*

> [!note] What this means: RT-H's "language" is a labeled discretization of the action space
> The language motions are **not** learned semantics and **not** hand-authored per task. They are a *rendering into English of a thresholded, magnitude-ordered partition of the robot's own 9-D action space*, produced by a fixed generative grammar (axis words × sign × composition order). That makes RT-H a genuine **controlled natural language** — with a specified grammar and an induced lexicon — which is a much closer fit to the "subset of natural language" question than the abstract suggests.
>
> It also explains the embodiment coupling precisely: the 9 dimensions **are this robot's** (arm deltas + *mobile base* + parallel gripper). Port to a suction cup, a five-finger hand, or a fixed-base arm and the extraction procedure — hence the entire lexicon — must be redefined. The grammar might transfer; the vocabulary cannot.

### The words themselves carry value beyond the partition (§V-A ablations) — the decisive result

Three ablations over the *same* underlying hierarchy separate three different hypotheses:

| Variant | What it changes | Result |
|---|---|---|
| **RT-H** | — | best overall |
| **RT-H-Joint** | one autoregressive query instead of two (motion into decoder, not encoder) | comparable |
| **RT-H-Cluster** | K-means over actions → integer class labels, replacing the labeling procedure | **slightly worse on average**, *better on the hardest precise tasks* |
| **RT-H-OneHot** | **the same language motions, relabeled as integers** | **much worse** |

**RT-H-OneHot is the load-bearing one.** It holds the partition fixed and removes only the English surface form — and performance drops substantially. The authors' conclusion: *"while action hierarchy itself gets us part of the way, **the structure of language greatly improves language motion and action prediction**."* The words are not decoration over a codebook; a VLM co-trained on internet-scale data can compose *"move arm forward"* in ways it cannot compose integer 47.

RT-H-Cluster is the interesting near-miss: finer-grained clusters give the action query *more* guidance (hence better on precise jar tasks) but are *harder to predict* (hence worse across a broad task set) — the abstraction tradeoff, measured.

> [!note] Two independent confirmations, two years apart
> RT-H-OneHot (2024, PaLI-X 55B, real mobile manipulator) and [TurboVLA](turbovla-paper.md)'s task-ID ablation (2026, 0.2 B LLM-free policy, LIBERO — 95.4 vs 97.7 semantic, p = 0.0001) are the **same experiment on opposite ends of the model-scale and architecture spectrum**, and they agree: *a closed set of opaque labels over the same task/motion partition underperforms natural language.* Compositional linguistic structure is doing work that the partition alone does not. This is the strongest evidence in the wiki that a human-readable action vocabulary is not merely a convenience.

### The paper names the abstraction tradeoff explicitly (§III-C)

> *"the more fine-grained they are, the harder they would be to predict for the language motion query, but the more guidance they provide to the action query, and vice versa."*

The authors also sketch the alternatives they did not take: a **higher-level object-referential** motion space (*"reach the object," "grasp the object handle"*) which "likely requires human annotation or robust object detection and tracking," and a **finer** one describing rate (*"move arm forward slowly"*). This is the design space for any action CNL, stated by the people who built one.

### Results

Platform: the RT-1/RT-2 mobile manipulator (arm + mobile base; the vendor is not named in the paper). Dataset: **Diverse+Kitchen (D+K) = 100K demonstrations** — the 70K RT-1/RT-2 Kitchen set (6 semantic task categories) plus a new 30K **Diverse** set (24+ categories). Evaluation: **8 of the hardest tasks × 10 trials = 80 trials per method**. The paper reports **95% Wilson score confidence intervals** — better evaluation hygiene than most sources in this wiki.

| Claim | Numbers | N | Verdict ([audit](../syntheses/platforms/vla-success-rate-audit.md) method) |
|---|---|---:|---|
| RT-H beats RT-2 by **+15 pp** average (~40% vs ~25%) | 6/8 tasks higher; nonzero on 6/8 vs RT-2's 4/8 | 80 | **survives, marginally** (p = 0.043) |
| Language-motion corrections: RT-H **40% → 63%** with 30 correction episodes/task | +23 pp | 80 | **survives** (p = 0.0036) |
| RT-H-Intervene **63%** vs RT-2-IWR **13%** | +50 pp | 80 | **survives** (p < 0.0001) |
| RT-2-IWR *degrades* 25% → 13% under teleop corrections | −12 pp | 80 | **marginal** (p = 0.053) — the "IWR degrades" framing is borderline |
| Object generalization 65% vs RT-2's 55% | pick 70/60, move 60/50 | 50 | **TIE** (p = 0.31) — not a supported claim |
| Offline action MSE vs RT-2 | **~20% lower**; with ground-truth motions, **40% lower** | — | not a rollout metric; no N needed |

The **40% gap between inferred-motion MSE and ground-truth-motion MSE** is the most diagnostic number in the paper: the action query is far better than the end-to-end system, so **language-motion prediction is the bottleneck**, not action decoding. That is exactly why correcting at the motion layer works so well.

### Corrections are cheaper to learn from than teleoperation (§IV-A, §V-C)

Because the human intervenes in *language*, not in the action space, corrections need only a keyboard or a microphone — and crucially, **only the language-motion query is retrained**. The action query already knows how to execute the corrected phrase. *"This significantly reduces the complexity of learning from corrections, since we only need to learn minor changes in the smaller language motion space rather than the large action space."*

The authors' explanation for why [DAgger](https://arxiv.org/abs/1011.0686)-style teleop corrections (IWR) *hurt*: teleoperated actions introduce distributions too far from the base policy's, while language-motion corrections keep actions on-policy (they still come from the model, under a slightly different phrase).

A side benefit they call out: corrections make failures **interpretable and debuggable** — they diagnosed a stuck policy as "keeps predicting *close gripper*," which is a legible failure in a way a joint-space error is not.

### Contextuality — the phrases are not primitives

*"Move arm left"* means "move the oatmeal packet precisely above the bowl" in one scene and "move the lid to latch onto the jar" in another. The same phrase produces different speeds, different non-dominant axes, and different gripper poses depending on task and observation. The authors: *"It would be immensely challenging to design a single 'move arm left' primitive to capture this contextuality."*

RT-H also follows **out-of-distribution** language motions — phrases never paired with that task in training — which is what makes free-form correction viable.

### Inference cost

Two sequential queries **double inference time**, which at 55B is prohibitive. Two mitigations: **asynchronous querying** (train the motion query to predict one step ahead, then batch it with the current action query — "nearly identical querying lag as RT-2"), which they use; or **fixed-frequency** motion re-query every H steps, which they reject because motions need to change at precise moments. Compare the async-inference pattern in [SmolVLA](../entities/smolvla.md) and the [control-rate ladder](../syntheses/platforms/control-rate-ladder.md).

## Limitations the paper states

- **Absolute success rates remain low** — 63% after corrections on the hard eight.
- **Systemic motion-prediction errors confuse action prediction** in ways a flat model wouldn't exhibit (oscillation; the stuck-on-"close gripper" mode).
- **Correction quality is capped by the action query.** If *"move arm left"* overshoots, the operator's only recourse is more phrases — "this can make the process slower than teleoperation." Rare in-distribution, likelier as tasks drift OOD.
- **The right abstraction level is unresolved** — object-referential vs. motion-referential is named as future work.
- Only **one** intermediate layer is tested; they propose stacking more (long-horizon instruction → task → language motion → action) with correction possible at any level.

## Open questions

- **The cross-embodiment proposal is the paper's own, and nobody has executed it.** Future Work states language motions *"could even be used to help bridge datasets with many different embodiments like [OXE](../entities/open-x-embodiment.md), or even to learn from human videos with actions described only in language."* That is precisely the question [action representation languages](../syntheses/agents/action-representation-languages.md) asks — proposed in 2024, and the 2026 cross-embodiment literature went to **unified latent tokens** instead. Why the language route was not taken is unrecorded: abandoned, tried-and-failed, or simply not attempted.
- **Would the OneHot result survive at small scale?** RT-H's language advantage plausibly comes from PaLI-X's internet-scale prior. TurboVLA's task-ID result suggests it does survive at 0.2 B with only BERT — but nobody has run the two designs head to head.
- **Does the extraction grammar transfer?** The procedure is embodiment-specific by construction. Whether *re-running the same grammar* on a different morphology yields a compatible lexicon (enabling exactly the OXE bridge above) is untested.
- **No LIBERO or standard-benchmark numbers**, so RT-H cannot be placed in the wiki's [LIBERO table](../entities/libero.md); its evaluation is entirely on in-house DeepMind data with an unnamed robot.

## Entities mentioned

- [RT-H](../entities/rt-h.md) · [RT-2](../entities/rt-2.md) · [PaLI-X](../entities/pali-x.md)
- [Google DeepMind](../entities/google-deepmind.md) · [Ted Xiao](../entities/ted-xiao.md) · [Pierre Sermanet](../entities/pierre-sermanet.md) · [Dorsa Sadigh](../entities/dorsa-sadigh.md) · [Suneel Belkhale](../entities/suneel-belkhale.md)
- [Open X-Embodiment](../entities/open-x-embodiment.md) — the corpus the paper proposes bridging with language motions

## Concepts touched

- [Action representation languages](../syntheses/agents/action-representation-languages.md) — the synthesis this source anchors
- [VLA models](../concepts/learning/vla-models.md) — RT-2 as backbone; the action-hierarchy pattern
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — an intermediate level *inside* a single learned policy
- [Imitation learning](../concepts/learning/imitation-learning.md) — interactive IL, DAgger, IWR
- [LLM-free VLA](../concepts/learning/llm-free-vla.md) — the OneHot ablation is the same measurement as TurboVLA's task-ID ablation
