---
title: Home robot forecast, 2026-Q4 to 2028-Q4 — dated predictions with a scorecard
type: synthesis
created: 2026-11-16
updated: 2026-11-16
tags: [forecast, predictions, scorecard, household-robot, consumer-robotics, adoption, capability, reliability, safety, privacy, 1x-neo, figure, weave-robotics, laundry-folding, dishes, calibration]
---

# Home robot forecast, 2026-Q4 to 2028-Q4

Predictions made on **2026-11-16** about household robots: how many are in homes, what they can do, how fast capability is growing, and whether they are safe. Each prediction is a number with an interval, or a probability, with a fixed resolution rule. They are scored **after the end of each quarter**, from 2026-Q4 through 2028-Q4.

> [!warning] These are judgment forecasts, not sourced facts
> The evidence is cited from this wiki. The numbers are the forecaster's estimates from that evidence, and no source states them. Confidence falls quickly with distance: the 2026-Q4 and 2027 rows rest on announced products and dates, while the 2028 rows are extrapolation. **The predictions on this page are frozen as of 2026-11-16.** Scoring is appended below; the forecasts themselves are never edited. A revised forecast goes on a new dated page.

## The short version

- A few hundred manipulation-capable robots are in consumer homes today. The forecast is about 5,000 by mid-2027, 20,000 by the end of 2027, and 90,000 by the end of 2028, with very wide intervals.
- Almost none will do a chore unattended through 2027. **Laundry folding and partial tidying arrive first**, with a remote human as backup. **Unattended dishes probably do not arrive by the end of 2028** (28%).
- Zero-shot capability is climbing fast from a low base. Reliability, the thing a product needs, is slower.
- Physical safety is likely to come from low mass and low force, not proven-safe software. Privacy and security are the weaker side.

## What is being counted

**"Home robots"** here means robots with at least one arm that a household owns, rents, or hosts in a vendor trial, worldwide, cumulative.

- **Included:** general-purpose and single-chore manipulators such as NEO, Isaac 0 and Isaac 1, NORI A3, Flourish 1, Sourccey, Memo, Figure 03 in a customer's home, GigaAI's home-trial units, and assistive robots living in a user's home.
- **Excluded:** robot vacuums (including ones with a small arm), toys and companions without useful arms, units in labs or offices, vendor-employee homes, and services where the robot leaves with its operator (Tau).

**Resolution method for counts.** No audited count exists. At each checkpoint, sum the vendor-stated or press-reported deliveries per product in a tally table, each with its source, and record a low and high bound. The prediction scores as a **hit** if the 80% interval overlaps the tally's bounds, and **unresolved** if the tally's own bounds span more than a factor of five.

## Evidence base (as of 2026-11-16)

| Product | Status | Source |
|---|---|---|
| [1X NEO](../../entities/1x-neo.md) | $20,000 or $499/mo; *"US Deliveries start 2026"*; no confirmed customer delivery; reported 10,000 sold out | [order page](../../sources/1x-neo-order-page.md), [TechCrunch](../../sources/techcrunch-hello-robot-homes-2026.md) |
| [Weave Isaac 0 / Isaac 1](../../entities/weave-robotics.md) | Isaac 0 folding in California, remotely assisted, 30–90 min per load; Isaac 1 on pre-order for fall 2026 | [eWeek](../../sources/eweek-weave-isaac-0.md), [Weave](../../sources/weave-isaac-1-product-page.md) |
| [NORI A3](../../entities/nori-a3.md) | $1,688; first batch reported sold out, second batch of 100 | [site](../../sources/nori-robotics-site.md) |
| [Flourish 1](../../entities/flourish-1.md) | 50 numbered units, December 2026 | [site](../../sources/flourish-robots-website.md) |
| [Sourccey](../../entities/sourccey.md) | Ships December 2026 | [site](../../sources/vulcan-robotics-sourccey-site.md) |
| [Sunday Memo](../../entities/sunday-robotics.md) | Beta *"late 2026"*, not for sale | [site](../../sources/sunday-memo-site.md) |
| [Figure 03](../../entities/figure-03.md) | 350+ built by April 2026; no home deployment announced | [production update](../../sources/figure-ramping-03-production.md) |

A web check on 2026-11-16 found no confirmed NEO, Isaac 1 or Figure home deliveries (external, not ingested: [1X status](https://physicalailab.io/en/1x-neo-price-preorder-delivery-status/), [1X factory release](https://www.globenewswire.com/news-release/2026/04/30/3285118/0/en/1x-opens-neo-factory-in-hayward-ca-america-s-first-vertically-integrated-humanoid-robot-factory-with-consumer-shipments-planned-for-2026.html), [Isaac 1 coverage](https://www.homeandrobot.com/articles/weave-robotics-isaac-1)). The full field is in the [household robots comparison](../platforms/household-robots-comparison.md).

**Capability evidence.**
- [Helix 2.5](../../sources/figure-helix-2-5.md): 56% pooled full-task success across 30 unseen homes (towels 62%, tidy 40%, bed 67%), against 8% without human-video pretraining.
- [Gemini Robotics On-Device 2](../../sources/gemini-robotics-on-device-2-model-card.md): 53.3% on the SO-101, against 6.7% one generation earlier.
- [π\*0.6](../../sources/pistar06-paper.md): learning from deployment doubled throughput and roughly halved failures; 2+ hours folding in a new home.
- [GR00T 2](../../sources/gr00t-2-whitepaper.md): fine-tuning alone 23–69 of 100, with human corrections 71–84, with a recovery agent 97–98.
- [TidyBot++](../../sources/tidybot-plus-plus-paper.md): dishwasher loading 7 of 10 in one apartment.
- Against: BEHAVIOR-1K's best full success is 12.4% ([AI Index](../../sources/stanford-hai-ai-index-2026.md)); π0.5 collapses under reworded instructions ([LIBERO-PRO](../../sources/libero-pro-paper.md)); 99% per action over 103 actions finishes about a third of the time ([TRI](../../sources/tri-grocery-mobile-manipulation-paper.md)).

**Safety evidence.** No vendor cites a home-robot safety certification, and no learned-policy robot is certified ([safety standards](../../concepts/robotics/robot-safety-standards.md)). Unitree robots have had root-takeover flaws ([record](../../sources/unitree-vulnerability-record-2026.md)). Remote operators are part of the NEO, Isaac and Tau products ([privacy and security](../platforms/home-robot-privacy-and-security.md)).

## Prediction set A: robots in homes (cumulative)

Baseline estimate today: **about 300** (80% interval 150–600).

| ID | Checkpoint | Point estimate | 80% interval |
|---|---|---|---|
| A1 | 2026-12-31 | 700 | 400 – 2,000 |
| A2 | 2027-03-31 | 2,000 | 700 – 8,000 |
| A3 | 2027-06-30 | 5,000 | 1,500 – 25,000 |
| A4 | 2027-09-30 | 10,000 | 3,000 – 50,000 |
| A5 | 2027-12-31 | 20,000 | 5,000 – 100,000 |
| A6 | 2028-03-31 | 30,000 | 7,000 – 180,000 |
| A7 | 2028-06-30 | 45,000 | 10,000 – 300,000 |
| A8 | 2028-09-30 | 65,000 | 13,000 – 450,000 |
| A9 | 2028-12-31 | 90,000 | 15,000 – 700,000 |

**Reasoning.** Through mid-2027 the spread is mostly 1X: it reports 10,000 units sold and none delivered. Figure's ramp from one robot a day to one an hour in under 120 days shows a fast ramp is possible. The upper tail from late 2027 assumes a second high-volume vendor, most likely Chinese, which this wiki covers poorly. The lower tail assumes continued delays, a funding squeeze, or a safety incident that freezes deliveries.

## Prediction set B: events (cumulative probability, %)

Each cell is the probability that the event **has happened on or before** that quarter's last day. *Confirmed* means a vendor announcement with customer evidence, or an independent press or owner report.

| ID | Event | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 28Q1 | 28Q2 | 28Q3 | 28Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Shipping** | | | | | | | | | | |
| B1 | 1X NEO: first confirmed customer delivery | 45 | 75 | 88 | 93 | 95 | 96 | 97 | 97 | 98 |
| B2 | Weave Isaac 1: first confirmed customer delivery | 55 | 85 | 92 | 95 | 96 | 97 | 97 | 97 | 98 |
| B3 | Flourish 1: at least one unit delivered | 50 | 75 | 85 | 88 | 90 | 91 | 92 | 92 | 93 |
| B4 | Sourccey: at least one unit delivered | 50 | 75 | 85 | 88 | 90 | 91 | 92 | 92 | 93 |
| B5 | Sunday Memo: beta running in non-employee homes | 30 | 55 | 70 | 78 | 83 | 86 | 88 | 90 | 91 |
| B6 | Figure: robots in paying or external customers' homes | 3 | 10 | 25 | 35 | 50 | 58 | 65 | 70 | 75 |
| B7 | 1X: 1,000 or more cumulative customer deliveries | 1 | 8 | 30 | 50 | 65 | 73 | 80 | 84 | 87 |
| B8 | 1X: 10,000 or more cumulative customer deliveries | 0 | 0 | 2 | 8 | 20 | 30 | 40 | 48 | 55 |
| **Capability** | | | | | | | | | | |
| B9 | Published zero-shot folding in unseen homes at 80% or better full-task success, 100+ trials | 5 | 18 | 35 | 48 | 60 | 68 | 75 | 80 | 84 |
| B10 | Published zero-shot whole-room tidying in unseen homes at 60% or better full-task success, 100+ trials | 5 | 18 | 35 | 47 | 58 | 66 | 72 | 77 | 81 |
| B11 | Published pooled zero-shot success of 70% or better across 3+ household tasks in unseen homes, 300+ trials (Helix 2.5 scored 56%) | 2 | 8 | 18 | 30 | 45 | 55 | 63 | 70 | 76 |
| B12 | The same, at 90% or better | 0 | 0 | 1 | 3 | 6 | 10 | 15 | 21 | 28 |
| B13 | A purchasable home robot folds laundry with **no remote human by default**, confirmed by an independent review | 1 | 3 | 8 | 15 | 25 | 33 | 42 | 50 | 57 |
| B14 | A purchasable home robot ships dishwasher loading or unloading as a feature, at any level of remote assistance | 1 | 3 | 6 | 12 | 20 | 28 | 36 | 44 | 52 |
| B15 | A purchasable home robot does dishes **unattended** (no remote human), confirmed by an independent review | 0 | 1 | 3 | 5 | 8 | 12 | 17 | 22 | 28 |
| B16 | A vendor or independent reviewer publishes measured remote-assistance or intervention rates for a home robot in customers' homes | 5 | 20 | 40 | 55 | 65 | 72 | 78 | 82 | 85 |
| B17 | A major independent reviewer recommends a general-purpose home robot as worth buying for chores | 0 | 1 | 3 | 6 | 10 | 15 | 21 | 27 | 33 |
| **Safety** | | | | | | | | | | |
| B18 | A home manipulation robot vendor cites a completed third-party home-safety certification (ISO 13482 or equivalent) | 2 | 5 | 10 | 16 | 22 | 28 | 34 | 40 | 45 |
| B19 | A publicly reported injury needing medical attention, caused by a consumer home manipulation robot | 1 | 4 | 10 | 17 | 25 | 32 | 39 | 45 | 50 |
| B20 | A publicly reported privacy or security incident on a consumer home manipulation robot other than Unitree's: leaked footage, a takeover in the wild, or a disclosed serious vulnerability | 8 | 20 | 35 | 48 | 58 | 66 | 72 | 77 | 81 |

**Notes on resolution.**
- **B9–B12:** the result must state trial counts and that the homes were unseen. Vendor-published results count; the scorer notes whether the protocol was blind.
- **B13 and B15:** "no remote human by default" means the vendor states that teleoperation is not used for the task in normal operation, and a review by an outlet with no commercial tie to the vendor reports it completing the chore on most attempts.
- **B17:** outlets such as Wirecutter, Consumer Reports, The Verge or CNET; a "recommended" or equivalent verdict for chores, not for novelty.
- **B19:** vacuums and toys are excluded, as in set A.

## Reasoning behind the capability and safety rows

**Why folding and tidying come first.** They tolerate failure: a badly folded towel or a missed toy costs nothing. Three independent lines already show them working in unseen homes at 40–67% (Helix 2.5), for hours at a time (π\*0.6), and as a shipping product with remote correction (Isaac 0).

**Why dishes come last.** Water, breakable objects, tight clearances and a long chain of steps. The best published number is 7 of 10 in one apartment, and one vendor excludes water and breakables outright.

**Why products trail demos.** Chores are long chains, so per-step reliability compounds. The recovery layer is what closes the gap, and today that layer is a remote person. The GR00T 2 result suggests a software agent can take over that role, which is why B13 rises steadily through 2028.

**Rate of growth.** The working assumption is that failure rates on a given household task halve every 6 to 12 months. From Helix 2.5's 44% failure in September 2026, that gives roughly 70% pooled success during 2027 (B11) and leaves 90% uncertain even by the end of 2028 (B12, 28%).

**Safety.** Light, weak, slow robots are safe by construction, and most of the sub-$10,000 tier is built that way. The injury risk in B19 comes mainly from heavier bipeds and from volume: more robots in more homes. B20 is higher because remote operation puts cameras and outside staff in the home by design.

## Scoring

**Schedule.** Score each checkpoint in the first two weeks after the quarter ends.

| Checkpoint | Quarter end | Score in | Status |
|---|---|---|---|
| 1 | 2026-12-31 | January 2027 | pending |
| 2 | 2027-03-31 | April 2027 | pending |
| 3 | 2027-06-30 | July 2027 | pending |
| 4 | 2027-09-30 | October 2027 | pending |
| 5 | 2027-12-31 | January 2028 | pending |
| 6 | 2028-03-31 | April 2028 | pending |
| 7 | 2028-06-30 | July 2028 | pending |
| 8 | 2028-09-30 | October 2028 | pending |
| 9 | 2028-12-31 | January 2029 | pending |

**Method.**
- **Set B:** for each event, record 1 if it happened by the quarter's end, else 0. The score is the **Brier score**, the squared difference between the forecast probability and the outcome, averaged over the 20 events. Lower is better. Always answering 50% scores 0.25.
- **Set A:** build the tally table, then record hit, miss or unresolved, plus the ratio of the tally's midpoint to the point estimate.
- **Calibration:** from checkpoint 3 on, group all scored set-B cells by forecast probability (0–10%, 10–30%, 30–70%, 70–90%, 90–100%) and compare with the observed frequency.
- **Evidence:** every resolution cites a source. A primary that matters to a decision gets ingested, per the wiki's primary-sources rule.
- **Disputes:** if the evidence is ambiguous, mark the cell unresolved and exclude it from the average. Do not resolve in the forecast's favour.

### Scorecard

*(Appended after each checkpoint. Nothing above this line changes.)*

| Checkpoint | Set A result | Set B Brier | Events resolved yes | Notes |
|---|---|---|---|---|
| 1 (2026-Q4) | | | | |
| 2 (2027-Q1) | | | | |
| 3 (2027-Q2) | | | | |
| 4 (2027-Q3) | | | | |
| 5 (2027-Q4) | | | | |
| 6 (2028-Q1) | | | | |
| 7 (2028-Q2) | | | | |
| 8 (2028-Q3) | | | | |
| 9 (2028-Q4) | | | | |

## Known weaknesses of this forecast

- **China.** The wiki has little on Chinese consumer vendors. If the volume comes from there, set A is too low and the wiki will be slow to see it.
- **Correlated cells.** A cumulative event that resolves early scores well in every later column, so the nine checkpoints are not independent tests.
- **Counting.** Vendors report "delivered", "shipped" and "sold" loosely. Figure's 350 "delivered" units are not homes.
- **Thin base rates.** No general-purpose home robot has ever shipped at volume, so every number here is extrapolated from announcements and research results.

## Related

- [Household robots compared](../platforms/household-robots-comparison.md) — the current field, and the evidence table this forecast starts from
- [Consumer robotics value chain](consumer-robotics-value-chain.md) — who profits if these volumes happen
- [Home robot privacy and security](../platforms/home-robot-privacy-and-security.md)
- [Long-term in-home robot deployments](../assistive/long-term-in-home-robot-deployments.md)
- [VLA success-rate audit](../platforms/vla-success-rate-audit.md) — why trial counts matter when scoring B9–B12
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md), [DAgger and interactive imitation](../../concepts/learning/dagger.md)
