---
title: Crowdsourced robot training data
type: concept
created: 2026-08-27
updated: 2026-08-28
sources: 3
tags: [crowdsourcing, human-data, egocentric, data-pipeline, data-quality, fraud, deduplication, data-labor, gig-economy, scaling-laws, go-big, brookfield, consent]
---

**Crowdsourced robot training data** is the acquisition of physical-task data from the general public — typically egocentric or handheld video of people doing ordinary things — rather than from lab staff, paid teleoperators, or the robots themselves. It is a *sourcing* strategy, distinct from the question of how such data is turned into a policy.

> [!note] One instance, and it published nothing
> This page exists because [Figure's Index](../../entities/figure-index.md) ([announcement](../../sources/figure-index-announcement.md)) is the first large-scale attempt this wiki has ingested, and because the failure modes it names are real regardless of whether Figure's numbers are. **No results, no yield figures and no scaling curve have been published for any crowdsourced robot corpus.** Read the patterns below as a problem statement, not a validated method.

## Why anyone does this

The supervised alternatives do not scale to the diversity that generalist policies appear to need. The datasets this wiki tracks are all **hundreds to low thousands of hours**, collected under direct supervision: [DROID](../../entities/droid.md) 350 h, [EgoDex](../../entities/egodex.md) 829 h, [RoboMIND](../../entities/robomind.md) 305.5 h. [EgoScale](../../sources/egoscale-paper.md) reached 20,854 h of egocentric human video and fitted the field's only clean [scaling law](scaling-laws-vla.md) over it — with downstream task completion rising 0.30 → 0.71 across 1k → 20k hours, and no visible saturation.

If that curve keeps going, the binding constraint is acquisition throughput, and supervised collection cannot supply it. Figure's framing of why they built rather than bought is the honest version of the argument: *"Vendors couldn't hit the throughput, diversity, or quality bar."*

The second argument is about **the shape of the diversity, not its volume**. Figure's is the clearest statement of it:

> "The data inherits its diversity directly from the people generating it. Every new Creator brings an unseen environment, unfamiliar objects, and their own idiosyncratic way of completing a task — the kind of long-tail variation that's nearly impossible to define upfront."

That is a real argument. A lab cannot enumerate the tail; a hundred thousand kitchens contain it by construction.

## What breaks, and is specific to crowdsourcing

### 1. The data becomes adversarial

This is the structural difference from every supervised corpus, and it is not a quality problem — it is an incentive problem. A contributor paid per accepted submission is optimising **acceptance**, not fidelity. Duplicate uploads under different accounts, staged or trivial "tasks" that clear an automated filter, footage recycled from elsewhere, and collusion to reverse-engineer the filter are all rational.

Figure treats it as a first-class pipeline stage — *"human analysts then audit samples at the user level for deliberate attempts to evade them"* — and **auditing at the user level rather than the clip level is the correct unit**: fraud is a property of a contributor's behaviour over time, and a per-clip filter cannot see it.

The unresolved half: an adversarial contributor is trying to pass the filter, so the filter's own criteria become the specification of the fraud. No published work in this wiki measures how well that arms race goes.

### 2. Novelty has to be decided by a model

Deduplication at this volume cannot be human. Figure's method — *"we embed each video segment and discard those above a similarity threshold with previously accepted data"* — makes **an embedding model the arbiter of what counts as new**.

The failure mode is specific and important for robotics: whatever the embedding is blind to gets discarded as redundant. Two clips of the same kitchen, the same mug and the same reach may differ entirely in **contact dynamics, grip force, object mass, and hand pose** — exactly the variation a manipulation policy needs and exactly the variation a visual embedding is least likely to encode. Aggressive visual dedup can therefore *remove* the physical diversity the corpus was collected for.

The same caveat applies to using embedding clusters for rebalancing: you are shaping the corpus toward whatever axes the embedding happens to represent.

### 3. Rate is not size, and size is not yield

Crowdsourced pipelines are naturally reported as *throughput* — Figure's *"30 minutes of video every second"* — because throughput is what a consumer app produces and what distinguishes it from supervised collection. But throughput is upstream of five filtering stages, and **the accepted fraction converts a rate into a dataset**. Figure publishes the rate and not the yield, and never states total hours at all.

The reporting discipline this suggests: a crowdsourced corpus should be described by **(hours ingested, acceptance rate, hours retained, and the diversity trend over time)**. A rate alone is not a size, and a size alone is not a curve.

### 4. Marginal novelty, not total novelty, is what a rate buys

Figure reports diversity *per 1,000 hours* — 373 tasks, 1,146 objects, 116 environments. That is the right instrument, because it is size-invariant and measures whether new hours are still bringing new world.

But a rate quoted **without a trend is unfalsifiable**. The interesting question is whether that figure was measured on the first thousand hours or the most recent: a constant rate means the long tail is genuinely inexhaustible and spend converts linearly into coverage; a decaying one means the corpus is saturating and the marginal dollar buys re-runs of the same kitchen. Those imply opposite conclusions about a $1B commitment, and the published figure distinguishes them not at all.

### 5. The consent surface is enormous and unaddressed

Supervised collection happens in labs, with staff, under an ethics process. Crowdsourced collection happens in **strangers' homes and workplaces**, and the contributor consents for themselves — not for the family members, customers, colleagues, children or proprietary business environments in frame. Retention, deletion, licensing and downstream rights are all open questions the moment the corpus leaves the contributor's phone.

The Figure announcement does not mention consent, privacy, retention or data rights **once**, which is notable for a corpus explicitly sourced from *"every environment on earth."*

## Two sourcing models: the landlord and the marketplace

Added 2026-08-28. [Figure](../../entities/figure.md) has now run **both** variants of this, eleven months apart, and the contrast is the useful part:

| | [Project Go-Big](../../sources/figure-project-go-big.md) (Sep 2025) | [Index](../../entities/figure-index.md) (Aug 2026) |
|---|---|---|
| Who is filmed | people in **[Brookfield](../../entities/brookfield.md) properties** | the general public, anywhere |
| What is bought | **access to space** — 100k residential units, 660M sq ft commercial | **labour** — ~$0.94 per accepted clip |
| Counterparty | one institutional partner (also a Series C investor) | 44,000 weekly strangers |
| Adversarial? | **no** — no per-clip payment, so no incentive to game | **yes, by construction** — hence a fraud-review stage |
| Consent surface | mediated by the **property owner** | mediated by an app EULA |
| Published result | **navigation transfer**, no numbers | none |

**The space-access model is the less obvious of the two and the less discussed.** Environment diversity — real kitchens, real clutter, real hallways — is exactly what lab collection cannot stage, and it is owned by people who are not in robotics. Property portfolios are a robotics data asset, and Brookfield is the first owner to price one.

> [!warning] Neither model has addressed consent
> Index publishes nothing on consent, retention or data rights for a corpus filmed inside homes. Go-Big describes video *"collected passively as people do behaviors in real Brookfield homes"* and never says whether the units are occupied, who is filmed, or on what terms. **The landlord's consent is not the tenant's** — and the landlord-mediated variant is the one where the person filmed may have the least practical ability to decline.

## The problem this does not solve

None of the above touches the actual difficulty. **Human video has no action labels.** No joint commands, no proprioception, no forces — and a human hand is not the robot's. Crowdsourcing changes the cost and diversity of the *observation* stream and leaves the human→robot transfer problem exactly where it was.

The wiki has several published approaches to that gap — [EgoScale](../../sources/egoscale-paper.md)'s three-stage human-pretrain → aligned human-robot mid-train → task post-train recipe, [latent action tokens](latent-action-tokens.md) as a learned cross-embodiment interface, inverse-dynamics pseudo-labelling as used by [DreamGen](../../entities/dreamgen.md). A crowdsourcing programme is a bet that one of them works at scale, and that bet is the part worth evaluating.

> [!note] Except where the action space is embodiment-invariant
> [Go-Big](../../sources/figure-project-go-big.md) is the one case in this wiki where the label problem largely dissolves: for **SE(2) navigation**, a human's base trajectory and a humanoid's are nearly the same, and the labels are plausibly recoverable from the video's own camera motion rather than annotated. Figure trained a navigation policy on human video with **no robot demonstrations at all**. That is a real result and a narrow one — it tells you the gap is a function of *how far the action space is from the observation*, and manipulation sits at the far end. Cite it as the boundary case, not as evidence crowdsourcing solves manipulation.

## Related concepts

- [Scaling laws — VLAs and human data](scaling-laws-vla.md) — the thesis crowdsourcing is serving; EgoScale is its only fitted curve.
- [Latent action tokens](latent-action-tokens.md) · [Imitation learning](imitation-learning.md) — the label problem crowdsourcing leaves untouched.
- [Generative data augmentation](generative-data-augmentation.md) — the synthetic alternative to buying diversity from people.
- [Consumer-robotics value chain](../../syntheses/society/consumer-robotics-value-chain.md) — where the labour marketplace sits.
- [Visual relocalization and mapping](../robotics/visual-relocalization-and-mapping.md) — how camera-motion labels can come free from egocentric video.

## Current state

**Two ingested instances, one narrow result.** The right comparison is the pair: [EgoScale](../../sources/egoscale-paper.md) collected ~20,854 h under research conditions and published a fitted scaling law with downstream success rates; [Index](../../entities/figure-index.md) claims an ingest rate that would exceed that corpus in under twelve hours and has published no curve, no yield, and no result.

What would settle it is unglamorous: **an acceptance rate, a total, a diversity trend, and one downstream number.** Until then, crowdsourcing is a plausible answer to a real constraint, demonstrated only as a logistics achievement — plus [Go-Big](../../sources/figure-project-go-big.md)'s navigation result, which is genuine but sits at the easiest end of the transfer problem.

## Mentioned in

- [Introducing Index (Figure AI)](../../sources/figure-index-announcement.md) — the five-stage pipeline, fraud as a named stage, and the diversity-per-1,000-hours framing.
- [Project Go-Big](../../sources/figure-project-go-big.md) — the landlord-mediated variant, and the wiki's only human-video-only transfer result.
- [Figure–Brookfield partnership](../../sources/figure-brookfield-partnership.md) — property portfolios priced as a robotics data asset.
