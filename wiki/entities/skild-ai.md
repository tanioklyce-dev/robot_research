---
title: Skild AI
type: entity
subtype: company
created: 2026-08-29
updated: 2026-08-29
sources: 1
tags: [skild-ai, s1, robot-foundation-model, in-context-learning, cmu, pittsburgh, physical-ai, omni-bodied, vendor-source]
---

**Skild AI** — Pittsburgh robot-foundation-model company, founded **2023** by former Carnegie Mellon faculty **Deepak Pathak** and **Abhinav Gupta**. Builds the **Skild Brain**, positioned as *"a unified, omni-bodied brain to control any robot for any task."* Its flagship model is **[S1](../sources/skild-s1-blog.md)** (August 2026), an **in-context learner** for manipulation: shown one demonstration video at inference, it executes the task with no fine-tuning and no weight update.

Skild is one of the four or five companies making the **model-layer bet** described in [the industry map](../syntheses/society/robot-ai-industry-map.md) — sell the policy, let others build the bodies — alongside [Physical Intelligence](physical-intelligence.md), [NVIDIA GR00T](nvidia-groot.md), [Gemini Robotics](gemini-robotics.md), and [TRI](tri.md)/[Walden](walden-robotics.md).

> [!warning] Everything below the founding facts is vendor-stated or trade press
> This page has **one ingested source**: the [S1 blog post](../sources/skild-s1-blog.md), which is a vendor announcement with no third-party evaluation. Funding and valuation figures are marked `[live-web]` and are **not ingested** — see the epistemic note in [the industry map](../syntheses/society/robot-ai-industry-map.md). No Skild model has been independently evaluated in any source this wiki holds, and no weights are released.

## The thesis: in-context learning instead of language prompting

Skild's technical position is a specific disagreement with the mainstream [VLA](../concepts/learning/vla-models.md) line. Where a VLA takes a **language instruction** and needs post-training to reach a new task, S1 takes a **demonstration video** and adapts inside the forward pass:

> *"Pre-training is the outer loop that teaches the policy how to learn from context; at inference time, the demonstration drives the inner loop without changing any weights."*

The evidence offered is a **scaling crossover** rather than a single benchmark — and it cuts against Skild at small scale, which is the detail worth carrying:

| Pre-training data | Setting | In-context learning | Language-conditioned |
|---|---|---|---|
| 1,000 h | seen | **43%** | **53%** |
| 100,000 h | **unseen** | **66%** | **9%** |

Skild's own claim is that *"a single demonstration in context is worth roughly 380 post-training examples"* ([S1](../sources/skild-s1-blog.md)). If that holds under independent evaluation it is a significant result about the [data bottleneck](../concepts/learning/crowdsourced-robot-training-data.md) — it converts a 50–100-hour teleoperation campaign into an 11-minute demonstration. It has not been independently evaluated.

See [in-context robot learning](../concepts/learning/in-context-robot-learning.md) for the concept and where else it appears.

## What is not claimed, despite the positioning

> [!warning] "Omni-bodied" is a claim about the roadmap and the locomotion predecessor, not about S1
> The company's site says *"An AI that truly understands the physical world should not be limited by robot or task type."* The [S1 announcement](../sources/skild-s1-blog.md) **names no robot platform anywhere**, and makes **no cross-embodiment claim for manipulation**. The only embodiment-transfer claim is for the predecessor locomotion model **LocoFormer** (Liu et al., 2025) — *"the policy is never told which body it is driving"* — which this wiki has not ingested.
>
> This matters because omni-bodiedness is exactly the property that would make the model layer capture value from hardware. It is the company's central strategic claim and its flagship model's announcement does not contain it.

## Products (company-stated)

Three application areas on the company site, none with published performance:

1. **Security / inspection** — navigating "unstructured, dangerous environments."
2. **Mobile manipulation.**
3. **Autonomous packing.**

Low-level skills — grasping, handover, navigation — are *"abstracted away using an API call, allowing users to build applications without worrying about details of the unstructured, messy real world."* The API framing is notable: it positions Skild as **infrastructure sold to integrators**, not as a robot vendor.

## Funding and standing

> [!note] `[live-web]` — none of this is an ingested source
> - **Series C, ~$1.4B at >$14B post-money** (mid-January 2026), led by **SoftBank** `[live-web]` [BusinessWire](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B).
> - Participation reported from **NVIDIA (NVentures), Bezos Expeditions, Samsung, LG, Schneider Electric, Salesforce Ventures** `[live-web]` [36Kr](https://eu.36kr.com/en/p/3660200362402434).
> - Earlier backers listed on the company site: Felicis, General Catalyst, Sequoia, Carnegie Mellon, SoftBank, Menlo, CRV, Lightspeed, Coatue, Amazon, Bezos Expeditions, SV Angel.
> - **>$2B total across three rounds in 18 months**; valuation roughly **tripled from $4.5B in ~7 months** `[live-web]` [BusinessWire](https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B).
> - Revenue reported to have gone from zero to **~$30M during 2025** `[live-web]` [36Kr](https://eu.36kr.com/en/p/3660200362402434) — unaudited, and one of the very few revenue figures attached to any company in this wiki.

**The investor list is the most analytically useful fact here.** **Samsung, LG, Schneider Electric and NVIDIA** are industrial strategics, not financial investors — the same pattern [the industry map](../syntheses/society/robot-ai-industry-map.md) identifies at Figure (Brookfield), Apptronik (Mercedes-Benz) and Walden (Toyota): **capital arriving disproportionately from parties who own the deployment environment**. Skild is the model-layer instance of that pattern, and the presence of two Korean electronics conglomerates plus an industrial-automation incumbent suggests the intended buyer is a factory, not a consumer.

## Why it matters in this wiki

- **The clearest published alternative to language-conditioned VLAs.** Most of this wiki's policy coverage — [π-series](physical-intelligence.md), [GR00T](nvidia-groot.md), [Gemini Robotics](gemini-robotics.md), [MolmoAct2](molmoact2.md) — conditions on language. S1 conditions on a demonstration. That is a different answer to the same specification problem, and worth tracking as such.
- **A rare public data-QC ratio.** *"For every dollar we spend on collecting data, we spend three on quality control"* ([S1](../sources/skild-s1-blog.md)) is the kind of operational number almost nobody publishes.
- **A test case for the model-layer bet.** At >$14B with no released weights, no paper, and no third-party evaluation, Skild is the sharpest instance of the gap this wiki keeps returning to: capital committed far ahead of demonstrated, verifiable capability.

## Related

- [Physical Intelligence](physical-intelligence.md) — the closest comparator at the model layer; language-conditioned.
- [UMI](umi.md) — appears in S1's data-source trade-off table.
- [In-context robot learning](../concepts/learning/in-context-robot-learning.md) — the concept.
- [The Robot AI industry](../syntheses/society/robot-ai-industry-map.md) — where Skild sits structurally.

## Mentioned in

- [Introducing S1: In-Context Learning for Robotics](../sources/skild-s1-blog.md) — the flagship-model announcement; the only ingested Skild source.

## Open questions / TBD

- **Which robots?** No embodiment is named in any Skild material read here.
- **LocoFormer** (Liu et al., 2025) — the locomotion predecessor carrying the actual cross-embodiment claim. **Uningested; the highest-value next Skild source.**
- **Founders have no entity pages.** Deepak Pathak and Abhinav Gupta are both significant CMU robot-learning researchers and appear nowhere else in this wiki.
- **Is there a paper?** S1 is a blog post. Whether a technical report follows determines whether any of this becomes citable.
- **Revenue composition.** ~$30M from what, sold to whom, on what contract terms — unknown.
