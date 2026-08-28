---
title: "Introducing Index: Building The World's Largest and Most Diverse Physical Dataset (Figure AI)"
type: source
url: https://www.figure.ai/news/introducing-index
author: Figure AI
affiliation: Figure AI
published: 2026-08-25
ingested: 2026-08-27
venue: figure.ai/news
format: company announcement blog post (~800 words, no figures, no results)
tags: [figure, index, helix, human-data, egocentric, crowdsourcing, data-pipeline, gig-economy, scaling-laws, vla, humanoid, data-labor, privacy]
---

# Introducing Index (Figure AI)

> [!warning] Vendor announcement, zero evidence
> Every number on this page is stated by Figure with **no third-party verification, no paper, no results, and no released data**. The post's own words on the outcome: *"The generalization results we're seeing internally are already validating this thesis, and we will be sharing more in detail on this soon."* A search for independent coverage two days after publication returned nothing. Treat the entire page as a **claim of intent and scale**, not a finding.

## Summary

Figure AI has come out of stealth with **Index**, a smartphone app that pays members of the public — *"Creators"* — to film themselves doing everyday physical tasks, and the data pipeline behind it. Launched on Google Play and the App Store on **2026-08-25** after four months in stealth.

The thesis is stated plainly and is not novel: *"Our AI stack, [Helix](helix-blog.md), gets more capable the same way every learned system does: with data… The data needed to scale a truly general purpose robot doesn't exist on the internet — it has to come from the real world."*

What *is* notable is the delivery mechanism. Figure tried to buy this data and could not: *"Vendors couldn't hit the throughput, diversity, or quality bar Helix requires, so we built the pipeline ourselves."* The replacement is a **consumer app plus a gig-labour marketplace**, and the announcement's most consequential sentence is the one about the marketplace, not the dataset — see [The business model inversion](#the-business-model-inversion) below.

## The stated numbers

| | claimed |
|---|---|
| App downloads | **264,000** across **108 countries** (headline says "100+") |
| Weekly active users | **44,000+** |
| Videos uploaded | **16M+** |
| Ingest rate | **30 minutes of video every second** |
| Restated as | *"4.9 years of human work every day"* |
| Paid to Creators to date | **$15M** |
| Committed spend | *"over $1B the next 12 months on data **and compute**"* |
| Diversity, per 1,000 hours | **373** unique tasks · **1,146** unique manipulated objects · **116** unique environments |
| Time in stealth | 4 months |

Task range is claimed as *"cooking, cleaning, laundry, and other household chores at home, as well as inside businesses such as logistics centers, restaurants, factories, and offices,"* with examples *"as obscure as cleaning kitty litter, changing oil, busing restaurant tables."*

## What the ingest rate actually means

30 minutes of video per second is **1,800 hours per hour**, or **43,200 hours per day**. Against the corpora this wiki already tracks, that is the number worth internalising:

| Corpus | Hours | Index ingests it in |
|---|---|---|
| [RoboMIND](../entities/robomind.md) | 305.5 | **~10 minutes** |
| [DROID](../entities/droid.md) | 350 | **~12 minutes** |
| [EgoDex](../entities/egodex.md) | 829 | **~28 minutes** |
| [OXE](../entities/open-x-embodiment.md) share in the [TRI LBM](tri-lbm-paper.md) mix | ~1,150 | **~38 minutes** |
| [EgoScale](egoscale-paper.md) human-video pretraining corpus | 20,854 | **~11.6 hours** |
| [Helix](helix-blog.md)'s own stated training set | ~500 teleop hours | **~17 minutes** |

That last row is the one that reframes Figure's own history. Helix was announced in Feb 2025 trained on *"~500 hours"* of teleoperation, marketed as *"<5% of typical VLA datasets."* Index ingests that volume roughly every quarter of an hour. Whatever else this announcement is, it is Figure publicly abandoning the small-data framing it used to differentiate Helix.

> [!note] Units check — "4.9 years of human work" is calendar-years, not work-years
> 43,200 h/day ÷ 8,766 h/year = **4.93 calendar-years** of footage per day. Read as *working* years at ~2,000 h, the same volume is **21.6 work-years per day**. The post's phrase lands between the two readings and is only correct under the first. The larger number is the more meaningful one for a labour comparison, and Figure used the smaller.

> [!warning] The rate and the video count do not obviously reconcile
> 16M videos over a 4-month stealth period, against a current rate of 43,200 h/day, admits two readings that cannot both be right:
> - **The rate is a recent peak.** At ~2 minutes per video, 16M videos ≈ **533,000 hours** total — which the current rate would produce in about **12 days**. So the 30 min/s figure describes a very recent ramp, not the period average.
> - **Videos are long.** Sustaining 43,200 h/day for 120 days implies ~5.2M hours, or **~19 minutes per video** — implausible for task clips.
>
> The first reading is far more likely. Either way, **the announcement never states total hours collected**, and the rate figure must not be multiplied by the stealth period to estimate corpus size. That the diversity statistics are quoted *per 1,000 hours* — a size-invariant rate — means the total is absent from the post twice over.

## Pay, per unit

$15M across 16M videos is **~$0.94 per accepted-or-submitted video** (the post does not say which). At ~2 minutes per clip that is roughly **$28 per hour of footage**; at the implausible 19-minute average it collapses to ~$3/hour. The per-video figure is the robust one. Neither the acceptance rate nor the pay schedule is disclosed, so the effective hourly rate a Creator earns — as opposed to the rate Figure pays per delivered minute — is unknowable from this post.

The **$1B/12mo** commitment is explicitly *"on data **and compute**"*, undifferentiated. Compute for a company training humanoid foundation models could absorb nearly all of it, so this is not a $1B data commitment and should not be quoted as one.

## The five-stage pipeline

The most technically substantive part of the post, quoted nearly in full because it is the only part with mechanism:

1. **Filtering** — *"Automated filters first screen for technical, visual, and semantic quality."*
2. **Fraud review** — *"Human analysts then audit samples at the user level for deliberate attempts to evade them."*
3. **Deduplication** — *"we embed each video segment and discard those above a similarity threshold with previously accepted data."*
4. **Rebalancing** — *"using task quotas — based on how well each submission matches its selected task — and embedding-based clusters that capture variation beyond task labels."*
5. **Annotation** — *"we generate hierarchical text captions associated with every episode."*

Figure also names the infrastructure shift as the real cost: ingesting at this rate *"required rebuilding our data infrastructure around constraints more typical of a consumer app: 24/7 availability, continuous large-scale compute for processing, and real-time feedback to users."*

> [!note] Fraud is a named pipeline stage, and this is the first time this wiki has seen that
> Every other dataset here — [DROID](../entities/droid.md), [RoboMIND](../entities/robomind.md), [EgoDex](../entities/egodex.md), [OXE](../entities/open-x-embodiment.md) — was collected by researchers, lab staff, or paid teleoperators under direct supervision. **Paying strangers per submission makes the data adversarial by construction**: the contributor's incentive is to maximise accepted submissions, not to represent the world. That Figure devotes a pipeline stage and *human analysts auditing at the user level* to it is the most credible detail in the post, precisely because it is an admission of a problem. See [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md).

> [!note] Deduplication by embedding is a diversity policy, not a measurement
> *"Discard those above a similarity threshold"* means an embedding model is the arbiter of what counts as new. Whatever that model is blind to — subtle contact dynamics, force, hand pose under an identical-looking scene — is dropped as redundant. Neither the model nor the threshold is named. The same caveat applies to the *"embedding-based clusters that capture variation beyond task labels"* used in rebalancing.

## The business model inversion

The two sentences with the widest implications are not about data at all:

> "Anyone can become a Creator and start recording real tasks in their own home or workplace… **Or, you can book a Creator through the app who comes to you to help with daily tasks and chores. We'll even send one to your business.**"

And:

> "Index is laying the groundwork for **ordering robots as a service**. Today, you have people coming to help clean your house; eventually, a robot will do everything for you."

So Figure is operating a **household-and-business chore marketplace whose product is the training data**, explicitly framed as the human-staffed pilot of the robot service it intends to sell. The customer-facing service and the data-collection instrument are the same object, and the humans are the temporary implementation.

This is a genuinely different value-chain position from anything else in this wiki's [consumer-robotics value chain](../syntheses/society/consumer-robotics-value-chain.md) analysis, which reasoned about actuator vendors, model servers and integrators. None of it anticipated *the robot company running the labour marketplace it plans to displace*.

## Entities mentioned

- [Figure](../entities/figure.md) — the company and its humanoid line
- [Index](../entities/figure-index.md) — the dataset and app
- Helix — Figure's VLA ([blog](helix-blog.md))

## Concepts touched

- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md)
- [Scaling laws — VLAs and human data](../concepts/learning/scaling-laws-vla.md)
- [Imitation learning](../concepts/learning/imitation-learning.md)
- [Latent action tokens](../concepts/learning/latent-action-tokens.md) — one answer to the problem this post does not mention

## Open questions

- **How does human video become robot actions?** The post never says. Phone video of a human has **no action labels, no proprioception, no force, and a different embodiment from [Figure 03](../entities/figure.md)** — hand morphology, kinematics, viewpoint and camera intrinsics all differ. This is *the* hard problem in human-video pretraining, and the wiki has several published answers to it ([EgoScale](egoscale-paper.md)'s two-stage human→aligned→task recipe, [latent action tokens](../concepts/learning/latent-action-tokens.md), IDM pseudo-labelling in [DreamGen](../entities/dreamgen.md)). Figure gestures at none of them. A post titled *"the world's largest robot training dataset"* about a corpus containing **no robot data** owes the reader that paragraph.
- **What is the accepted fraction?** Five filtering stages sit between 16M uploads and anything trainable. The yield is the number that converts an ingest rate into a dataset, and it is absent.
- **What are the total hours?** Never stated. Diversity is quoted per-1,000-hours; volume is quoted as a rate. The two never multiply into a size.
- **Does the diversity rate hold, or decay?** 373 tasks / 1,146 objects / 116 environments *per 1,000 hours* is a marginal-novelty rate. The interesting question is whether it is measured on the first thousand hours or the most recent — a saturating rate and a constant one imply completely different returns on the $1B. A rate quoted without a trend is unfalsifiable.
- **Where is the scaling law?** [EgoScale](egoscale-paper.md) published a fitted law (`L = 0.024 − 0.003·ln(D)`, R² = 0.9983) over 1k–20k hours of egocentric human video, with downstream task completion rising 0.30 → 0.71. Figure asserts the same thesis at ~1000× the ingest rate with **no curve, no axis, and no number**. The comparison is unflattering and entirely avoidable.
- **Consent, privacy and data rights are not mentioned once.** 44,000 people are filming inside homes and workplaces — with bystanders, children, customers, colleagues and proprietary business environments in frame. The post says nothing about bystander consent, retention, deletion, licensing, or what rights a Creator signs away. For a corpus explicitly sourced from *"every environment on earth"*, that omission is the most conspicuous in the piece.
- **What happens to Creator earnings as the robots arrive?** The post's closing frame — *"today, you have people coming to help clean your house; eventually, a robot will do everything for you"* — describes paying people to generate the data that removes the need to pay them. Stated cheerfully and without comment.
