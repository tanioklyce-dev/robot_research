---
title: Index (Figure AI)
type: entity
subtype: dataset
created: 2026-08-27
updated: 2026-08-28
sources: 2
tags: [figure, index, dataset, human-data, egocentric, crowdsourcing, gig-economy, helix, unverified]
---

**App:** Google Play / App Store, launched 2026-08-25 · **Announcement:** [figure.ai/news/introducing-index](https://www.figure.ai/news/introducing-index)

**Index** — [Figure AI](figure.md)'s crowdsourced corpus of **human egocentric video of everyday physical tasks**, collected through a consumer smartphone app that pays contributors ("Creators") per submission. Announced 2026-08-25 after four months in stealth, positioned as *"the largest useful robot training dataset in the world"* and as the pretraining data for Figure's [Helix](../sources/helix-blog.md) VLA.

> [!warning] It contains no robot data
> Index is phone video of **humans** doing tasks. There are no action labels, no proprioception, no force readings, and the embodiment is a person rather than [Figure 03](figure.md). The name *"robot training dataset"* describes the intended use, not the contents. How the human→robot gap is crossed is not addressed anywhere in the announcement.
>
> **Amended 2026-08-28.** Figure *has* published a transfer result — [Project Go-Big](../sources/figure-project-go-big.md), 11 months earlier: Helix learned closed-loop **navigation** from 100% human video with no robot demonstrations. But that result is scoped to **SE(2) velocity commands**, the one case where the morphology gap essentially vanishes and the action labels are recoverable from the video itself. Index is overwhelmingly a **manipulation** corpus, and for manipulation Figure has published nothing. So the criticism stands and sharpens: the announcement is silent on the gap, and Figure's only public answer covers the easy half.

## Claimed scale ([announcement](../sources/figure-index-announcement.md))

| | |
|---|---|
| Downloads | 264,000 across 108 countries |
| Weekly active users | 44,000+ |
| Videos uploaded | 16M+ |
| Ingest rate | 30 min of video **per second** = **43,200 h/day** |
| Paid to Creators | $15M to date (~$0.94/video) |
| Committed spend | >$1B over 12 months on data **and compute** (undifferentiated) |
| Diversity per 1,000 h | 373 tasks · 1,146 objects · 116 environments |
| **Total hours** | **never stated** |

All figures are Figure-stated, uncorroborated, and published without results.

## Scale in context

At the claimed rate, Index ingests:

- [DROID](droid.md) (350 h) in **~12 minutes**
- [EgoDex](egodex.md) (829 h) in **~28 minutes**
- [EgoScale](../sources/egoscale-paper.md)'s 20,854 h human-video corpus — the largest published in this wiki — in **~11.6 hours**
- Helix's own stated ~500 teleop training hours in **~17 minutes**

That last comparison matters: Helix was announced in Feb 2025 on *"~500 hours"* of teleoperation, marketed as *"<5% of typical VLA datasets."* Index is Figure publicly retiring the small-data framing it once used as a differentiator.

**Uploaded is not accepted.** Five pipeline stages sit between ingest and anything trainable, and the yield is undisclosed — so none of these comparisons describes usable data.

## The collection pipeline

Five stages: **automated filtering** (technical, visual, semantic quality) → **fraud review** (human analysts auditing *at the user level* for deliberate evasion) → **deduplication** (embed each segment, discard above a similarity threshold) → **rebalancing** (task quotas plus embedding-based clusters) → **annotation** (hierarchical text captions per episode).

The fraud stage is the notable one: every other dataset in this wiki was collected under direct supervision, and **paying strangers per submission makes the corpus adversarial by construction**. See [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md).

## The labour marketplace

Index is not only an app for uploading video. Figure also lets customers **book a Creator to come and do their chores** — at home or at a business — and frames this explicitly as the human-staffed rehearsal for a product:

> "Index is laying the groundwork for ordering robots as a service. Today, you have people coming to help clean your house; eventually, a robot will do everything for you."

The chore service and the data-collection instrument are the same object. This is a value-chain position nothing else in the wiki occupies — see [consumer-robotics value chain](../syntheses/society/consumer-robotics-value-chain.md).

## What is missing

- **No results.** *"The generalization results we're seeing internally are already validating this thesis, and we will be sharing more in detail on this soon."*
- **No scaling law**, against [EgoScale](../concepts/learning/scaling-laws-vla.md)'s published fitted curve on the same kind of data.
- **No connection drawn to [Go-Big](../sources/figure-project-go-big.md)**, Figure's own prior human-video programme in [Brookfield](brookfield.md) properties — the announcement does not say whether Index extends it, replaces it, or runs alongside it.
- **No total size, no acceptance rate, no diversity trend.**
- **No mention of consent, privacy, retention, or data rights** — for a corpus filmed inside homes and workplaces by 44,000 people.
- **Not released.** Index is Figure-exclusive; there is no access path for anyone else.

## Related

- [Figure](figure.md) — owner; Helix is the consumer of this data
- [EgoDex](egodex.md) — the high-precision, small, *published* egocentric counterpart
- [DROID](droid.md) · [RoboMIND](robomind.md) · [Open X-Embodiment](open-x-embodiment.md) — the supervised-collection datasets it dwarfs in rate
- [Project Go-Big](../sources/figure-project-go-big.md) / [Brookfield](brookfield.md) — Figure's earlier, landlord-mediated version of the same thesis
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — the method
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md) — the thesis it asserts without evidence

## Mentioned in

- [Introducing Index (Figure AI)](../sources/figure-index-announcement.md)
- [Project Go-Big](../sources/figure-project-go-big.md) — the precursor programme.
