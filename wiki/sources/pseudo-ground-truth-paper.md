---
title: "On the Limits of Pseudo Ground Truth in Visual Camera Re-localisation (Brachmann, Humenberger, Rother, Sattler — ICCV 2021)"
type: source
url: https://arxiv.org/abs/2109.00524
local_path: raw/2109.00524-pseudo-ground-truth.pdf
author: "Eric Brachmann, Martin Humenberger, Carsten Rother, Torsten Sattler"
published: 2021-09-01
ingested: 2026-08-13
tags: [pseudo-ground-truth, benchmark-methodology, visual-relocalization, evaluation, 7scenes, 12scenes, dsac, active-search, sfm, slam, measurement-thread, primary-source]
---

## Summary

Re-localisation benchmarks need 6-DoF poses for thousands of images, which no human can annotate. So they generate them with a **reference algorithm** — Structure-from-Motion, or depth-based SLAM. The consequence the paper draws out:

> *"Benchmarks measure how well visual re-localisation methods are able to **replicate the results of the reference algorithm**."*

And the reference algorithm is a *choice*. Different references optimise different cost functions — reprojection error over sparse point clouds for SfM, 3D alignment error for depth SLAM — and land in different local minima. The paper asks whether that choice changes the leaderboard, and finds it does, **catastrophically**.

Ingested as the **fourth and earliest instance of this wiki's measurement thread**, and the only one where the *labels* rather than the tasks, the metrics, or the sample sizes are the defect.

## The headline result: the ranking inverts

7Scenes, percentage of images localised within **5 cm / 5°**, averaged over seven scenes, under three pseudo-ground-truths — the original depth-SLAM pGT, a locally bundle-adjusted variant, and an SfM pGT:

| Method | orig. (D-SLAM) | +BA | **SfM** |
|---|---:|---:|---:|
| **Active Search** (classical SIFT, ~2012) | **68.7** *(last)* | 79.5 | **98.5** *(first)* |
| hLoc (SuperPoint + SuperGlue) | 76.8 | 83.1 | 95.7 |
| DenseVLAD + R2D2 | 77.6 | 83.0 | 95.7 |
| DenseVLAD + R2D2 (+D) | 80.2 | 85.0 | 92.9 |
| DSAC* (scene coordinate regression, RGB) | 82.9 | 90.3 | 97.8 |
| **DSAC\* (+D)** (RGB-D) | **94.7** *(first)* | 93.2 | 95.3 |

**Active Search goes from last to first — +29.8 points absolute — by changing nothing but the labels.** On Pumpkin and Red Kitchen it moves from localising **under 50%** of images to **over 99%**. The previously-leading depth-based methods drop to the bottom, each outperformed by its own RGB-only counterpart.

## The mechanism — this is bias, not noise

> [!warning] Methods that resemble the reference algorithm are rewarded for reproducing its mistakes
> *"Methods that optimise a similar cost function as the reference algorithm better replicate the local minima and **imperfections** of the pGT, to a degree that relative rankings can be (nearly) completely inverted."*
>
> This is the part that makes the paper more than a caution about measurement error. **A method is not scored on being right; it is scored on agreeing with a particular algorithm's errors.** The paper colour-codes every method in its results table by similarity to each reference algorithm, and the ranking follows the colour.
>
> Two beliefs the paper says are therefore **not absolute but artifacts of the reference choice**: that *"learning-based scene coordinate regression outperforms classical feature-based methods"*, and that *"RGB-D-based methods outperform RGB-based methods."*

> [!note] Brachmann is attacking a belief that favours his own line of work
> The lead author is the author of **DSAC** and later **[ACE](../entities/niantic-spatial.md)** — he *is* the scene-coordinate-regression line. The paper's first casualty is the claim that scene coordinate regression beats classical feature matching. Worth noting because the wiki's other measurement-thread papers mostly critique *someone else's* results.

## "We do not see a solution" — and four mitigations anyway

The conclusion is unusually blunt: *"This issue is **fundamental**, and we do not see a solution to this problem."* It then offers four ways to live with it:

1. **Ship multiple pGT versions** per dataset. Their example is instructive: *"although DSAC\* does not perform best under any pGT, it performs well under all pGT versions"* — **robustness across references as the thing to select for**, rather than peak under one.
2. **Group methods by similarity to the reference algorithm** and compare only *within* groups, never across.
3. **Use thresholds coarse enough that the pGT difference does not bite** — e.g. 5 cm / 5° for 12Scenes — which requires modelling pose uncertainty, itself unsolved.
4. **Task-specific evaluation** — measure re-localisation *"in the context of AR, robotic navigation, etc."*

Code and the new pGT are released at `github.com/tsattler/visloc_pseudo_gt_limitations`.

## Analysis

> [!note] Remedy 4 is exactly what VP² proposed, in a different subfield, two years later
> *"Task-specific evaluation… in the context of AR, robotic navigation"* is the same move [VP²](vp2-paper.md) makes for video prediction: stop scoring the intermediate artifact against a proxy metric, score it by whether a downstream controller succeeds. Two subfields independently concluding that **the fix for a broken proxy is to measure the task you actually care about.**
>
> And remedy 1's finding — DSAC* best under no pGT but good under all — is the same shape as [RoboTwin 2.0](robotwin2-paper.md)'s conclusion that VLA pretraining buys **robustness rather than peak**. Different domains, same preference for the model that degrades gracefully across conditions over the one that wins a single ranking.

> [!warning] The wiki's measurement thread now has four instances, and they decompose cleanly
> | Instance | Subfield | What is broken |
> |---|---|---|
> | **This paper** (2021) | visual relocalisation | **the labels** — ground truth is an algorithm's output |
> | [VP²](vp2-paper.md) (2023) | video prediction | **the metrics** — perceptual scores mis-rank for control, sign-dependent |
> | [LIBERO-PRO](libero-pro-paper.md) (2025) | VLA manipulation | **the tasks** — eval set is the training set |
> | [Success-rate audit](../syntheses/platforms/vla-success-rate-audit.md) (2026) | VLA benchmarks | **the sample sizes** |
>
> Four subfields, five years, and **no cross-citation between them**. Each community rediscovers that its instrument is not measuring what it thinks, in its own terms, without knowing the others did.

> [!note] What it implies for anything this wiki quotes from a relocalisation benchmark
> [RTAB-Map](../entities/rtab-map.md), [LingBot-Map](../entities/lingbot-map.md), and [Niantic Spatial](../entities/niantic-spatial.md)'s ACE line are all evaluated against pGT of exactly this kind. **LingBot-Map's SOTA claim on KITTI and Oxford Spires inherits this problem**, and its README does not name the reference algorithm. That is not a reason to disbelieve it — it is a reason to hold the *ranking* loosely while accepting the *capability*.

## Entities mentioned

- [Niantic Spatial](../entities/niantic-spatial.md) — Brachmann's lab; the ACE / scene-coordinate-regression line this paper partly deflates
- [LingBot-Map](../entities/lingbot-map.md), [RTAB-Map](../entities/rtab-map.md) — the wiki's other relocalisation-adjacent artifacts, both quoting benchmark numbers of this kind

## Concepts touched

- [Visual relocalization and mapping](../concepts/robotics/visual-relocalization-and-mapping.md) · [Robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md)

## Open questions

- **Has anything changed since 2021?** Do current relocalisation benchmarks ship multiple pGT versions, or group by reference similarity? Unknown here — and the papers still cite single-pGT leaderboards.
- **What is the analogue for robot policy benchmarks?** [LIBERO](../entities/libero.md)'s "ground truth" is task success in a simulator, which is not algorithm-generated in the same way — but [RoboTwin 2.0](../entities/robotwin.md)'s expert demonstrations *are* generated by an MLLM-plus-planner pipeline, and policies trained on them are scored against tasks that pipeline could solve. **Nobody has asked whether synthetic-demonstration benchmarks have a pGT problem.** That is the transposition of this paper into this wiki's main subject, and it is open.
- Datasets are **7Scenes and 12Scenes** — small-scale indoor. Whether large-scale outdoor SfM benchmarks show the same inversion is untested here.
