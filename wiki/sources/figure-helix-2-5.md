---
title: "Helix 2.5: Zero-Shot 30-Home Generalization (Figure AI)"
type: source
url: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
fetch_url: https://www.figure.ai/news/helix-2-5-zero-shot-30-home-generalization
local_path: raw/2026-09-17-figure-helix-2-5.txt
sha256: 7807ef9c882f3f8c969ff8c627e6750ebb91f3d7d802d5865f682b527eca2888
author: Figure AI
affiliation: Figure AI
published: 2026-09-17
ingested: 2026-09-27
venue: figure.ai/news
format: "company research blog post (~2,300 words) with 6 videos, 2 charts, 1 table and an evaluation-rubric appendix; chart images saved to raw/assets/helix-2-5/"
tags: [figure, helix, helix-2-5, index, human-data, egocentric, pretraining, zero-shot, generalization, scaling-laws, whole-body-control, loco-manipulation, household, deformable-manipulation, evaluation, vendor-source]
---

# Helix 2.5: Zero-Shot 30-Home Generalization (Figure AI)

> [!note] The first Figure post with success rates
> Every prior [Helix](../entities/helix.md) announcement — [Helix](helix-blog.md) (Feb 2025), [Go-Big](figure-project-go-big.md) (Sep 2025), [Helix 02](figure-helix-02.md) (Jan 2026), [Index](figure-index-announcement.md) (Aug 2026) — published videos and no numbers. This one publishes **per-task success counts with denominators (140 trials per task, 420 pooled), a pre-registered grading rubric, a controlled ablation, and a data-scaling curve.** It is still a vendor blog — no paper, no model size, no dataset hours, no external evaluator — but it is the first Figure result the wiki can *check against itself*. It is also the delivery on the Index post's *"we will be sharing more in detail on this soon"*, 23 days later.

## Summary

**Helix 2.5** is [Figure AI](../entities/figure.md)'s third-generation [Helix](../entities/helix.md) model, pretrained **from random initialization entirely on [Index](../entities/figure-index.md)** — Figure's crowdsourced corpus of egocentric human video — and then fine-tuned into three whole-body household behaviors: **living-room tidying, towel folding, and bed making**. Each behavior was evaluated with a single fixed checkpoint in **30 Bay Area homes where no data had been collected**, on objects held out of all task data. Pooled full-task success was **56% (237/420)**; the same architecture and task data trained from random init scored **8% (35/420)**. Figure additionally reports that Helix 2.5 matches a Helix 02 policy's success on the same task with **half the task-specific data**, and a **four-point data-scaling curve** over an 8× range of Index pretraining data whose largest point was forecast from the smaller three. The post's thesis: *"learn broadly in pretraining, specify a behavior once, and generalize at deployment"* — and *"It's time to scale up,"* backed by **$3.5B of compute committed to training Helix**.

## Key results (Figure-stated)

1. **Zero-shot whole-body autonomy across 30 unseen homes** — three long-horizon behaviors, no data collection, fine-tuning or adaptation in the evaluation homes or on evaluation objects. Priority claim: *"the first demonstration of zero-shot whole-body generalization at this scope on a humanoid."*
2. **One foundation model, three behaviors** — a single Index-pretrained base adapted to three behaviors spanning locomotion, rigid and deformable manipulation, bimanual coordination and active perception.
3. **Index pretraining drives generalization** — *"Holding task-specific data, architecture, training, and evaluation fixed, Index pretraining alone increased zero-shot success from 9% to 56%."*
4. **"Behavior specification got 2x cheaper while its scope expanded 30x"** — half the task data of a representative Helix 02 behavior, generalized across 30 homes instead of one.
5. **A human-to-humanoid transfer scaling law** — *"Repeatedly doubling Index pretraining data improved downstream robot-action prediction smoothly enough to forecast our largest run's loss to four decimal places before training."*

## The numbers (Figure 1, read from the chart)

"Zero Shot Success in 30 Homes", rollout-level success, error bars shown but not defined:

| Task | Success criterion (chart label) | From scratch | **Index-pretrained** |
|---|---|---|---|
| Towel folding | all 4 towels | 9% (12/140) | **62% (87/140)** |
| Living-room tidy | every toy (13–15) | 5% (7/140) | **40% (56/140)** |
| Bed making | all 3 items, grade ≥B | 11% (16/140) | **67% (94/140)** |
| **All three, pooled** | | **8% (35/420)** | **56% (237/420)** |

Wiki arithmetic: 237/420 has a 95% Wilson interval of roughly **51–61%**; 35/420 roughly **6–11%**. The gap is not a sampling artifact. 140 trials over 30 homes is ~4.7 trials per home per task; Figure does not say whether every home was used for every task, nor give per-home variance.

> [!warning] Contradiction — "9%" in the text, "8%" in the chart
> The prose (twice) says the from-scratch policy *"succeeded on 9% of zero-shot trials"* and calls 56% *"over 6x higher."* The chart's pooled bar is **8% (35/420 = 8.3%)**; 9% is the **towel** bar. Pooled, the ratio is ~6.8×. Small, and it cuts in Figure's favour, but the headline number in the text does not match the pooled figure it is presented as.

### Evaluation protocol

- **Holdouts**: no data collected in any evaluation home; no evaluation toy, towel or bedding appeared in task-specification data (verified by *"an AI model, followed by human review"*); the robot used each home's own couches, beds and folding surfaces.
- **Initial conditions** (Table 1): a person tosses toys across floor, couch and tables / drops towels onto the surface / messes up the comforter and pillows. *"Placement and orientation are uncontrolled."* Resets applied identically across compared policies.
- **Checkpointing**: one fixed checkpoint per task across all 30 homes; *"no evaluation rollout data or performance was used for checkpoint selection."*
- **Blind evaluation**, criteria fixed before evaluation. **No partial credit** in the headline metric.
- **Timeouts**: 1 min per toy; 3 min per towel; 1 min per pillow and per comforter side. Any safety intervention = abort and fail.
- **Rubric** (appendix): towels graded A (all 4 corners within 1 in, clean fold) / B (2 corners) / C (none, messy); pillows *Good* <15°, *Bad* <45°; comforter *Good* corners within 6 in, *Bad* 6–12 in.

This is the most complete evaluation protocol any humanoid vendor in the wiki has published — comparable in spirit to the per-height success tables in [Gemini Robotics 2](gemini-robotics-2-blog.md), and more explicit about holdouts than most academic VLA papers.

## Architecture and training — what is said, and what is not

- **Pretrained from random initialization entirely on Index**, *"unlike Helix 02, which started from a pretrained vision-language model."* This is a significant architectural statement: Helix 2.5 **drops the VLM initialization** that defined System 2 in [Helix](helix-blog.md) and [Helix 02](figure-helix-02.md). Whether the S2/S1/S0 tiering survives is not stated.
- **Index composition**: *"intentionally broad"*; *"No single evaluation task makes up more than 1.90% of the Index pretraining dataset."* Tasks are characterized by clustering video embeddings and VLM-generated per-segment text descriptions into a nested semantic hierarchy (appendix).
- **Index ingest**: now *"roughly 35 minutes of new human experience every second"* (≈ 50,400 h/day) — up from 30 min/s (43,200 h/day) in the [Index announcement](figure-index-announcement.md) 23 days earlier.
- **Compute**: *"we have committed $3.5B of compute to training Helix."* The August figure was ">$1B over 12 months on data **and** compute"; the two are not directly comparable (different scope, no time horizon on the new one).

**Not stated**: model size; Index hours used for pretraining; hours of task-specification data (only the 2× ratio); whether task data is teleoperation, human video, or both; how human video is converted to robot actions; onboard vs offboard inference; per-home results; cycle times.

## The ablation — what it proves and what it doesn't

Two policies, identical task data, architecture, optimization, hyperparameters and evaluation; one from random weights, one from the Index-pretrained model. 8% → 56%.

> [!note] The baseline is "no pretraining", not "other pretraining"
> The ablation cleanly shows that **pretraining on Index beats no pretraining at all**. It does not show that Index beats the alternatives a reader actually cares about — a VLM initialization (what Helix 02 used), pretraining on robot data, or pretraining on a curated human-video corpus like [EgoScale](egoscale-paper.md)'s. A from-scratch transformer fine-tuned on a modest task set failing to generalize to 30 homes is the expected result. The claim *"Index accounts for the majority of Helix 2.5's zero-shot capability"* is true relative to this baseline; the more interesting claim — *human video is the right pretraining corpus for a humanoid* — is argued, not tested.

The **Helix 02 comparison** partly fills this gap (Helix 02 was VLM-initialized), but it is reported without numbers: *"Helix 2.5 matched its success rate while using half as much adaptation data."* Which task, what success rate, and whether Helix 02 was evaluated zero-shot or only in its training environment (the text implies the latter) are not given.

## The scaling law

Figure 2: four models on **nested subsets of Index spanning 8×** (1×, 2×, 4×, 8×), model size and downstream training fixed, each fine-tuned on the same task data and evaluated on **held-out action-prediction loss**. Loss falls log-linearly with data; the largest run's loss was forecast from the three smaller ones with error *"just 0.54% of the variation across the full 8× data range."*

> [!note] Read the scaling claim at its actual size
> - **Four points, one of them the forecast target** — the fit is three points.
> - **8× range.** [EgoScale](egoscale-paper.md) fit its law over 20× (1k–20k h) with five points and reported **absolute hours**; Figure reports only relative multiples, and the chart's y-axis values are rendered illegibly (near-white on white) in the published image.
> - **The metric is validation loss, not success.** No success rate is reported at any point on the curve. EgoScale and [X-VLA](../entities/x-vla.md) both tie their loss/error to task success; Figure does not. *"Four decimal places"* is meaningless without the loss scale.
> - **Data only**: *"This measures data scaling only, with model size and downstream training fixed"* — Figure's own caveat.
>
> It is still the **first human-to-humanoid data-scaling curve from a humanoid vendor**, and the first on a whole-body (not tabletop) embodiment — the question [scaling laws](../concepts/learning/scaling-laws-vla.md) listed as open ("does the same law apply to whole-body humanoid control?"). It answers that question weakly and positively.

## Qualitative claims

- **Whole-body self-correction** — *"stepping back to reposition, changing stance, or moving around a full bed to correct a fold,"* attributed to Index pretraining. Video only; no recovery-rate metric.
- **Active perception** — walking to find objects, shifting stance to reach, in tight cluttered spaces *"that other form factors can't get into"* — the humanoid-in-the-home form-factor argument.
- Helix 02 is retroactively credited with *"running a logistics task autonomously for 200 hours."*

## Entities mentioned

- [Figure](../entities/figure.md) · [Helix](../entities/helix.md) · [Index](../entities/figure-index.md) · [Figure 03](../entities/figure-03.md) (the robot, implied — never named in the post)

## Concepts touched

- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — the first vendor human→humanoid curve.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — Index's first published payoff.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — loco-manipulation as the evaluated capability.
- [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — a pre-registered, blind, held-out-environment protocol from a vendor.
- [VLA models](../concepts/learning/vla-models.md) — a VLA-lineage model that drops VLM initialization.

## Open questions

- **How is human video turned into humanoid actions?** Still unpublished. The post says Index pretraining improves *"next robot action prediction"* but not what the pretraining objective on action-free human video is (latent actions? retargeted hand/body pose? video prediction?). This remains the central missing piece of Figure's programme.
- **What pretraining alternative does Index beat?** The ablation baseline is random init. Index vs VLM-init vs robot-data pretraining is the comparison that would settle the thesis.
- **What is the task-specification data?** Teleop on Figure 03, human video, or both — and how many hours? "2× less" than an unstated number.
- **Does success scale like loss?** No success rate on the scaling curve.
- **Is S2 gone?** Random-init pretraining on video implies no pretrained language backbone; how are behaviors selected and language-conditioned, if at all? The three behaviors appear to be three fine-tunes, not one instructable model.
- **Why is tidying the weakest (40%)?** It is the task that most needs search and locomotion; the per-toy attempt data the rubric records is not published.
- **Does it replicate outside the Bay Area?** 30 homes in one metro region is a strong eval by robotics standards and a narrow one by housing-stock standards.
