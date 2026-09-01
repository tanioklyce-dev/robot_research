---
title: "Robot-Powered Data Flywheels: Deploying Robots in the Wild for Continual Data Collection and Foundation Model Adaptation (Grannen et al., 2025)"
type: source
url: https://arxiv.org/abs/2511.19647
fetch_url: https://arxiv.org/pdf/2511.19647v1
local_path: raw/robot-powered-data-flywheels_2511.19647.pdf
sha256: e48d7f7dbef5ba35c9e739f70609306595ffa7a9fd00d06142c7c2cafcf40211
author: "Jennifer Grannen, Michelle Pan, Kenneth Llontop, Cherie Ho, Mark Zolotas, Jeannette Bohg, Dorsa Sadigh"
affiliations: Stanford University
published: 2025-11-24
venue: arXiv preprint
tags: [data-flywheel, scanford, foundation-model-adaptation, in-the-wild-deployment, mobile-manipulation, vlm, ocr, library, tidybot, franka, self-labeling, primary-source]
ingested: 2026-08-31
---

## Summary

**The wiki has been asking for a closed flywheel and this is one.** The [Nori YC profile](nori-robotics-yc-profile.md) ingest recorded that *"nobody has shown the flywheel closing at this tier"*; **Scanford** closes it, at a smaller and much better-instrumented tier than Nori proposes.

The framework — **Robot-Powered Data Flywheel (RPDF)** — inverts the usual relationship: robots stop being *consumers* of foundation models and become *generators* of the data those models lack. The argument is about coverage, not scale. Internet pretraining corpora massively underrepresent the messy conditions of real deployment: occluded, faded, multilingual, low-resolution text. Robots are embodied and can go stand in front of it.

The instantiation is **Scanford**, a mobile manipulator deployed in Stanford's **East Asia Library for two weeks (10 days × 4 hours)**. It scans shelves, identifies books with a VLM, and — the load-bearing trick — **labels its own images by cross-referencing the library catalog**, so there is no human annotation in the loop at all.

Results on both axes at once:

| | Before | After |
|---|---|---|
| Book identification (domain-specific) | 32.4% | **71.8%** |
| English OCR, hardest subset (domain-**adjacent**) | 24.8% | **46.6%** |
| Chinese OCR, hard subset (domain-adjacent) | 30.8% | **38.0%** |

Plus **2,103 shelves scanned**, a librarian-estimated **18.7 hours** of human labor saved, and **26 human interventions total** across 10 days (2.6/day, each under 5 minutes).

> [!note] The result that matters is the domain-*adjacent* one
> Fine-tuning on your deployment data to improve your deployment task is unsurprising. The claim with reach is that **library shelf photos improved general multilingual OCR on public benchmarks** — English 24.8 → 46.6 and Chinese 30.8 → 38.0, measured on each benchmark's *hardest* subset (occlusion, low resolution, calligraphic fonts, vertical text, blur). Robot-collected data made the foundation model better at something the robot was not doing. That is the difference between a data-collection story and a flywheel.

## How the self-labeling works

This is the part worth stealing, and it is why the flywheel closes without annotation cost. After each session the collected images are associated with the library section they came from, which maps to a **known call-number range** in the library's database. The VLM's predicted labels are then **filtered against that database**, discarding images whose predictions fall outside the expected range.

The numbers show the cost of that filter: **8,232 raw labeled images from 6 hours of deployment → 5,019 after curation.** About 39% discarded, entirely automatically.

The generalizable principle: *the flywheel closes when the environment already contains a ground-truth index that the robot can align itself against.* Libraries have catalogs. Grocery stores have SKUs. The paper names both, plus hospitals (handwritten prescriptions, expiry dates), as candidate domains.

## Hardware and the unglamorous engineering

**Franka FR3 arm on a TidyBot++ mobile base**, wrist-mounted **Intel RealSense D435** RGB-D, base-mounted **Unitree L2 LiDAR**. The base is 21 inches wide, chosen against the **ADA minimum 36-inch aisle** — a rare instance of a research platform sized by an accessibility standard rather than by what was in the lab.

Control is deliberately dumb: predefined shelf heights, arm sweeps them at each stop, base advances **0.3 m** (≈ half an image's coverage), repeat.

The interesting failure is localization. **Odometry drifts, and conventional SLAM fails outright** in book aisles — "repetitive geometry prevents robust localization" in a narrow, visually homogeneous corridor. The fix is a heuristic on raw LiDAR: the shelves on either side appear as two dense vertical clusters, so **fit planes to them, recenter the robot in the aisle, and align heading parallel to the shelves** before every vertical scan.

The deployment log also contains an honest, legible failure: on Tuesday of week 2 the shelves were **three tall instead of the standard seven**, which made LiDAR shelf-position sensing noisier and drove **12 interventions in one day** — nearly half the fortnight's total.

## Two findings the authors flag as design guidance

**Gains plateau at ~1.5 hours.** Most of the improvement — both domain-specific and domain-adjacent — arrives within roughly **1,352 images**, after which it flattens. Short deployments are enough. This is a strong claim against the assumption that flywheel value scales with deployment duration, and it deserves testing elsewhere before being believed generally.

**Task selection: the Zone of Proximal Development.** The paper draws an explicit pedagogy analogy — a deployment should sit just past current model and robot capability. Too easy (reading large-font signage) and there is no headroom to learn. Too hard (manipulating and reading foreign newspapers) and the data needs so much manual curation and intervention that the autonomy which makes the flywheel work is destroyed. **The flywheel has a difficulty window, not a difficulty floor.**

## Entities mentioned

- [Jeannette Bohg](../entities/jeannette-bohg.md), [Dorsa Sadigh](../entities/dorsa-sadigh.md) — senior authors, Stanford. Kenneth Llontop and Cherie Ho also appear on the un-published **MessyNav** (see [backlog](../backlog.md)).
- [Qwen](../entities/qwen.md) 2.5 — the fine-tuned VLM. **Gemini** as a pretrained baseline (43.7% book ID; notably only **3.4%** on hard Chinese OCR, which the authors attribute to less Chinese in its pretraining mixture than Qwen's).
- **TidyBot++** mobile base, **Franka FR3** arm, **Intel RealSense D435**, **Unitree L2** LiDAR. No wiki pages.
- **Stanford East Asia Library** — the deployment site.

## Concepts touched

- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — the *other* answer to the data bottleneck. RPDF is its opposite: instead of paying many humans to collect, deploy one robot that labels itself against an existing index.
- [Sim-to-real transfer](../concepts/learning/sim-to-real-transfer.md) / [dexterous tool manipulation](../concepts/robotics/dexterous-tool-manipulation.md) — the synthetic-data answer to the same bottleneck, from the same lab.
- [VLA models](../concepts/learning/vla-models.md) — the adaptation target here is a **VLM perception component**, not a policy, which is why the flywheel can close on catalog labels rather than task success.

## Open questions

- **Does it close when the label source is task success rather than an external index?** Scanford's flywheel works because the library catalog is ground truth the robot did not have to earn. Nothing here shows a flywheel closing on **manipulation** data, where there is no catalog — which is exactly the tier [Nori](nori-robotics-yc-profile.md) and [Sourccey](../entities/sourccey.md) are pitching.
- **The 1.5-hour plateau is the most important number and the least examined.** If it holds generally, the economics of every "deploy fleets to collect data" thesis in this wiki change: value comes from *breadth of deployments*, not *duration*. If it is an artifact of this task's narrow visual distribution, it says the opposite. One deployment, one task, no ablation.
- **26 interventions over 40 hours is a real autonomy number** — rare in this wiki, and worth holding against the vendor claims in the [consumer robotics value chain](../syntheses/society/consumer-robotics-value-chain.md). It is also a *librarian-estimated* labor saving, not a measured one.
- **Same lab, opposite prescriptions.** [SimToolReal](simtoolreal-paper.md) argues real-world demonstration data is the wrong path for dexterity and generates synthetic coverage instead; this paper argues real-world deployment data is precisely what foundation models lack. Both are Bohg-advised, three months apart. The reconciliation — synthetic for *control*, real for *perception* — is implied by neither and stated by neither.
