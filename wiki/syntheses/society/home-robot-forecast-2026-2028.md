---
title: Home robot and JEPA forecast, 2026-Q4 to 2030-Q4 — dated predictions with a scorecard
type: synthesis
created: 2026-11-16
updated: 2026-11-16
tags: [forecast, predictions, scorecard, laundry, cleaning, cooking, meal-preparation, grocery, retail-robotics, jepa, ami-labs, yann-lecun, world-model, household-robot, consumer-robotics, adoption, capability, reliability, safety, privacy, 1x-neo, figure, weave-robotics, laundry-folding, dishes, calibration]
---

# Home robot and JEPA forecast, 2026-Q4 to 2030-Q4

Predictions made on **2026-11-16** about household robots: how many are in homes, what they can do, how fast capability is growing, and whether they are safe. Each prediction is a number with an interval, or a probability, with a fixed resolution rule. They are scored **after the end of each quarter**, from 2026-Q4 through 2030-Q4. A third set covers when JEPA-based AI reaches household products, a fourth covers grocery shopping, a fifth covers meal preparation and cooking, and a sixth covers laundry and cleaning.

> [!warning] These are judgment forecasts, not sourced facts
> The evidence is cited from this wiki. The numbers are the forecaster's estimates from that evidence, and no source states them. Confidence falls quickly with distance: the 2026-Q4 and 2027 rows rest on announced products and dates, while the 2028 rows are extrapolation. **The predictions on this page are frozen as of 2026-11-16.** The first version, filed that day, ran to 2028-Q4. The 2029–2030 columns, set C (JEPA), set D (grocery shopping), set F (meal preparation and cooking) and set G (laundry and cleaning) were added later the same day, before any scoring, without changing any number already filed. Scoring is appended below; the forecasts themselves are never edited. A revised forecast goes on a new dated page. Confidence in the 2029–2030 columns is low: they are extrapolations of extrapolations.

## The short version

- A few hundred manipulation-capable robots are in consumer homes today. The forecast is about 5,000 by mid-2027, 20,000 by the end of 2027, and 90,000 by the end of 2028, with very wide intervals.
- Almost none will do a chore unattended through 2027. **Laundry folding and partial tidying arrive first**, with a remote human as backup. **Unattended dishes probably do not arrive by the end of 2028** (28%).
- Zero-shot capability is climbing fast from a low base. Reliability, the thing a product needs, is slower.
- Physical safety is likely to come from low mass and low force, not proven-safe software. Privacy and security are the weaker side.
- **Groceries: the store-to-cupboard chain arrives in pieces.** Robot delivery to the door is growing regionally, piloted picking in stores gets trial results first, and putting groceries away at home is about even odds as a published result by mid-2029. A robot service that does a household's shopping with no human picker is 38% by the end of 2030.
- **Laundry leads every other chore; wet cleaning trails.** Mixed-garment folding at 80% is about even odds by late 2028 and the full laundry cycle by mid-2029. A bathroom cleaned unattended by a robot you can buy is 38% by the end of 2030. Cleaning sold as a service may reach most households first.
- **Cooking: appliances first, the stove last.** Making a hot drink or running a microwave is about even odds as a published result in unseen homes by the end of 2028. A shipped stovetop feature is 50% by the end of 2030, and a hot meal cooked unattended 35%.
- **JEPA reaches household robots first as a component, not as the controller.** A shipping home robot with a vendor-stated JEPA-style component passes 50% around 2029-Q3. A JEPA world model planning at run time reaches 40% by the end of 2030, and JEPA as the primary controller, LeCun's actual vision, only 19%.

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

**Extension to 2030 (added 2026-11-16).**

| ID | Checkpoint | Point estimate | 80% interval |
|---|---|---|---|
| A10 | 2029-03-31 | 120,000 | 18,000 – 1,000,000 |
| A11 | 2029-06-30 | 160,000 | 22,000 – 1,400,000 |
| A12 | 2029-09-30 | 210,000 | 26,000 – 1,900,000 |
| A13 | 2029-12-31 | 280,000 | 30,000 – 2,500,000 |
| A14 | 2030-03-31 | 350,000 | 35,000 – 3,200,000 |
| A15 | 2030-06-30 | 450,000 | 40,000 – 4,200,000 |
| A16 | 2030-09-30 | 570,000 | 45,000 – 5,500,000 |
| A17 | 2030-12-31 | 700,000 | 50,000 – 7,000,000 |

The 2029–2030 point estimates assume growth of roughly 3× a year slowing toward 2.5×. The intervals span two orders of magnitude because the outcome depends on whether any vendor reaches unattended usefulness (B13, B15), which is itself uncertain.

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

**Extension to 2030 (added 2026-11-16).** The same 20 events, same definitions.

| ID | Event (short) | 29Q1 | 29Q2 | 29Q3 | 29Q4 | 30Q1 | 30Q2 | 30Q3 | 30Q4 |
|---|---|---|---|---|---|---|---|---|---|
| B1 | NEO first delivery | 98 | 98 | 98 | 99 | 99 | 99 | 99 | 99 |
| B2 | Isaac 1 first delivery | 98 | 98 | 98 | 98 | 99 | 99 | 99 | 99 |
| B3 | Flourish 1 delivered | 93 | 93 | 94 | 94 | 94 | 94 | 95 | 95 |
| B4 | Sourccey delivered | 93 | 93 | 94 | 94 | 94 | 94 | 95 | 95 |
| B5 | Memo beta in outside homes | 92 | 92 | 93 | 93 | 94 | 94 | 94 | 95 |
| B6 | Figure in customers' homes | 78 | 81 | 83 | 85 | 87 | 88 | 89 | 90 |
| B7 | 1X at 1,000+ deliveries | 89 | 90 | 91 | 92 | 93 | 93 | 94 | 94 |
| B8 | 1X at 10,000+ deliveries | 60 | 64 | 68 | 71 | 74 | 76 | 78 | 80 |
| B9 | Folding 80%+ zero-shot, published | 87 | 89 | 91 | 92 | 93 | 94 | 95 | 95 |
| B10 | Tidying 60%+ zero-shot, published | 84 | 86 | 88 | 90 | 91 | 92 | 93 | 94 |
| B11 | Pooled 70%+ across 3+ tasks | 80 | 83 | 86 | 88 | 90 | 91 | 92 | 93 |
| B12 | Pooled 90%+ across 3+ tasks | 34 | 40 | 45 | 50 | 55 | 59 | 63 | 66 |
| B13 | Folding with no remote human | 62 | 66 | 70 | 73 | 76 | 78 | 80 | 82 |
| B14 | Dishwasher feature shipped | 58 | 63 | 67 | 71 | 74 | 77 | 79 | 81 |
| B15 | Dishes unattended | 33 | 38 | 42 | 46 | 50 | 53 | 56 | 59 |
| B16 | Intervention rates published | 87 | 88 | 89 | 90 | 91 | 92 | 92 | 93 |
| B17 | Independent "worth buying" verdict | 38 | 43 | 47 | 51 | 55 | 58 | 61 | 64 |
| B18 | Home-safety certification cited | 49 | 53 | 56 | 59 | 62 | 64 | 66 | 68 |
| B19 | Reported injury | 54 | 58 | 61 | 64 | 67 | 69 | 71 | 73 |
| B20 | Privacy or security incident | 84 | 86 | 88 | 89 | 90 | 91 | 92 | 93 |

**Notes on resolution.**
- **B9–B12:** the result must state trial counts and that the homes were unseen. Vendor-published results count; the scorer notes whether the protocol was blind.
- **B13 and B15:** "no remote human by default" means the vendor states that teleoperation is not used for the task in normal operation, and a review by an outlet with no commercial tie to the vendor reports it completing the chore on most attempts.
- **B17:** outlets such as Wirecutter, Consumer Reports, The Verge or CNET; a "recommended" or equivalent verdict for chores, not for novelty.
- **B19:** vacuums and toys are excluded, as in set A.

## Prediction set C: JEPA and household AI (added 2026-11-16)

**The question:** when does JEPA-based AI, the research program led by [Yann LeCun](../../entities/yann-lecun.md), reach household products?

**Where it stands** (evidence as of 2026-11-16):
- **LeCun gives no date for a home robot.** His stated precondition: *"that's not going to happen until we have good world models and planning"* ([MIT Technology Review](../../sources/mit-tech-review-lecun-ami-labs-interview.md)). [AMI Labs](../../entities/ami-labs.md) raised $1.03B and says its first targets are industrial systems, in one to two years, explicitly not robot arms or humanoids. Smart glasses are a named application.
- **Real-robot JEPA results are short and goal-image conditioned.** [RoboJEPA](../../entities/robojepa.md) at 8B parameters: grasp 67%, pick-and-place 27%, against 53% for π0.5, and planning takes several seconds on multiple GPUs. [HWM](../../entities/hwm.md) took pick-and-place from 0% to 70% with two levels of hierarchy. [H-JEPA](../../entities/h-jepa.md) reaches three levels in simulation only.
- **Robustness is the measured weak point.** [LeWorldModel](../../entities/leworldmodel.md) falls from 50.8% to 6–26% under colour, size and shape changes ([stable-worldmodel](../../sources/stable-worldmodel-paper.md)).
- **Three unmet conditions** from the wiki's [JEPA household synthesis](../world-models/jepa-for-household-mobile-manipulator.md): the recipe must ignore household variation, hierarchy must go past two levels and take language, and a force or tactile channel must enter the latent.
- **JEPA ideas already ship as components elsewhere.** The FLARE latent-prediction loss is in [GR00T N1.5](../../sources/groot-n1_5.md), and [VLA-JEPA](../../entities/vla-jepa.md) exists as research. Neither is in a consumer home robot.

**"JEPA-style component"** below means any of: an encoder pretrained with a JEPA objective, a latent-prediction auxiliary loss such as FLARE, or a latent (non-pixel) world model. The vendor or a paper must say so.

Cumulative probability (%), same convention as set B.

| ID | Event | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 28Q1 | 28Q2 | 28Q3 | 28Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **AMI Labs** | | | | | | | | | | |
| C1 | AMI Labs releases a model, API or product that outside customers can use (not only a paper or research code) | 3 | 8 | 15 | 23 | 32 | 40 | 47 | 53 | 58 |
| C2 | AMI Labs names a paying or pilot industrial deployment | 2 | 6 | 12 | 19 | 27 | 34 | 41 | 47 | 52 |
| C3 | AMI Labs announces a robotics product, robot partnership or robot-targeted model | 2 | 5 | 9 | 14 | 19 | 24 | 29 | 34 | 38 |
| **Research milestones** | | | | | | | | | | |
| C4 | A JEPA world model keeps 80%+ of its nominal success under colour, size, shape and distractor shifts on a stable-worldmodel-style benchmark | 3 | 8 | 14 | 20 | 27 | 33 | 39 | 44 | 49 |
| C5 | A JEPA hierarchy of 3+ levels, conditioned on language, on a real robot | 2 | 5 | 9 | 14 | 19 | 25 | 30 | 35 | 40 |
| C6 | A force or tactile channel in a JEPA latent, with real-robot contact-task results | 3 | 8 | 14 | 20 | 26 | 32 | 38 | 43 | 48 |
| C7 | A JEPA world model **plans** a language-specified task of 3+ steps on a real robot in an unseen environment at 60%+ success, 30+ trials | 1 | 3 | 6 | 10 | 15 | 20 | 25 | 30 | 35 |
| C8 | A JEPA-planning system matches or beats the paper's best VLA baseline on a real-robot, multi-task, language-conditioned benchmark, 100+ trials per method | 1 | 3 | 5 | 8 | 12 | 16 | 20 | 24 | 28 |
| C9 | A JEPA-planning result in 5+ unseen real homes on a household task, with stated trials | 0 | 1 | 3 | 5 | 8 | 12 | 16 | 20 | 24 |
| **In household products** | | | | | | | | | | |
| C10 | A shipping consumer home robot with a vendor-stated JEPA-style **component** | 3 | 6 | 10 | 14 | 19 | 24 | 29 | 34 | 38 |
| C11 | A shipping consumer home robot that uses a JEPA-style latent world model for **planning or action selection at run time** | 0 | 1 | 2 | 3 | 5 | 7 | 10 | 13 | 16 |
| C12 | A purchasable home robot whose **primary controller** is a JEPA world-model planner, doing chores | 0 | 0 | 0 | 1 | 1 | 2 | 3 | 4 | 5 |
| C13 | A shipping non-robot household product (smart glasses, home assistant) with a vendor-stated JEPA-family model | 2 | 5 | 9 | 13 | 18 | 23 | 28 | 33 | 37 |

| ID | Event (short) | 29Q1 | 29Q2 | 29Q3 | 29Q4 | 30Q1 | 30Q2 | 30Q3 | 30Q4 |
|---|---|---|---|---|---|---|---|---|---|
| C1 | AMI usable release | 63 | 67 | 70 | 73 | 76 | 78 | 80 | 82 |
| C2 | AMI industrial deployment named | 57 | 61 | 65 | 68 | 71 | 73 | 75 | 77 |
| C3 | AMI robotics announcement | 42 | 46 | 50 | 53 | 56 | 59 | 62 | 64 |
| C4 | Robust to household-type shifts | 53 | 57 | 61 | 64 | 67 | 70 | 72 | 74 |
| C5 | 3+ levels with language, real robot | 45 | 49 | 53 | 57 | 60 | 63 | 66 | 68 |
| C6 | Force or tactile in the latent | 52 | 56 | 60 | 63 | 66 | 69 | 71 | 73 |
| C7 | Plans 3+ step language task, 60%+ | 40 | 45 | 49 | 53 | 57 | 60 | 63 | 66 |
| C8 | Matches best VLA baseline | 32 | 36 | 40 | 43 | 46 | 49 | 52 | 55 |
| C9 | JEPA planning in 5+ real homes | 28 | 32 | 36 | 40 | 44 | 47 | 50 | 53 |
| C10 | Home robot with JEPA-style component | 43 | 47 | 51 | 55 | 58 | 61 | 64 | 67 |
| C11 | Home robot planning with JEPA at run time | 19 | 22 | 25 | 28 | 31 | 34 | 37 | 40 |
| C12 | JEPA planner as primary controller | 6 | 8 | 9 | 11 | 13 | 15 | 17 | 19 |
| C13 | JEPA in a non-robot household product | 41 | 45 | 49 | 52 | 55 | 58 | 61 | 63 |

**The direct answer.**
- **As a component** inside someone else's policy (C10): about even odds by 2029-Q3. This is the likeliest route, and the one the wiki's JEPA synthesis already pointed to.
- **In a non-robot household product** such as smart glasses (C13): about even odds by late 2029.
- **As a run-time planner** in a home robot (C11): 40% by the end of 2030, so the median date is after this forecast's horizon.
- **As the controller**, which is what LeCun's program actually proposes (C12): 19% by the end of 2030.

**Reasoning.**
- **The plan points away from homes first.** AMI Labs' stated sequence is industrial systems, then becoming a general supplier in three to five years. Robots are described as what world models eventually unlock. C3 is therefore lower than C1 and C2 throughout.
- **The research gaps are specific and being worked on.** H-JEPA, LeHami, DeepJEPA and RoboJEPA all appeared in autumn 2026, each aimed at one of the known limits. That pace is why C4–C6 pass 50% during 2029. Closing a gap in a paper is still several steps from a product.
- **The world-model role is being filled by a rival first.** Generative video world-action models ([DreamZero](../../entities/dreamzero.md), [GR00T 2](../../sources/gr00t-2-whitepaper.md), [Praxis-1](../../entities/praxis-1.md)) already act on real robots, and vendors are shipping them. JEPA's advantage is compute and label-free video; its handicap is that it arrived at real-robot scale later. C8 stays below 55% for that reason.
- **Run-time planning is expensive today.** RoboJEPA's 8B model takes seconds per plan on several GPUs. A home robot needs that on-board or over a link it can lose. C11 depends on that cost falling as much as on accuracy rising.
- **LeCun's own clock.** At Davos in January 2025 he gave the current paradigm three to five years. This forecast implies he is more likely wrong than right about *homes* on that schedule, while leaving real odds (C1 82%, C2 77%) that AMI Labs has working industrial products by then.

**Notes on resolution.**
- **C4:** the benchmark must apply the shifts at test time to a model not trained on them, as [stable-worldmodel](../../sources/stable-worldmodel-paper.md) does.
- **C7–C9:** the JEPA world model must do the planning. A JEPA encoder feeding a diffusion or VLA policy does not count here; it counts for C10.
- **C10–C12:** "shipping" means delivered to paying consumers, by the same test as set A. C12 implies C11, which implies C10.
- **C13:** a research demo or developer preview does not count.

## Prediction set D: grocery shopping (added 2026-11-16)

**The question:** when do robots help a household with groceries, from the store to the cupboard?

"Grocery robot" covers several different jobs at very different stages, and most of today's robots work for the retailer, not the household ([household robots comparison](../platforms/household-robots-comparison.md#grocery-shopping); [retail and grocery robotics](../../concepts/robotics/retail-and-grocery-robotics.md)).

**Where it stands** (evidence as of 2026-11-16):
- **To the door:** [Starship](../../entities/starship-technologies.md) reports over 10 million deliveries of all kinds and is moving more than 1,200 robots to grocery. In Finland, S Group says robots handle up to 20% of its online orders ([Starship releases](../../sources/starship-grocery-press-releases.md)). These are company figures. Someone still carries the bags inside.
- **In the store, piloted:** [Blue Collar Robotics](../../entities/blue-collar-robotics.md) reports about 120 items an hour with one remote person per robot, with paid trials planned for Q4 2026 ([Utah Business](../../sources/utah-business-blue-collar-robotics.md), [company](../../sources/blue-collar-robotics-site.md)).
- **In the store, autonomous:** TRI's best field result is 35.7% of runs and 28.9% of listed items, at night, excluding produce, refrigerated goods, glass and items over 4.5 kg ([TRI](../../sources/tri-grocery-mobile-manipulation-paper.md)). Simulated benchmarks agree: zero success on multi-step tasks in [RoboBenchMart](../../sources/robobenchmart-paper.md), under 15% in [MarketGen](../../sources/marketgen-paper.md).
- **Stocking shelves:** over 98% per object and 87% per task in a mock supermarket, with cans and small boxes only ([Pixels to Shelf](../../sources/pixels-to-shelf-paper.md)).
- **At home: almost no evidence.** The wiki has grocery bagging as a lab task for π0 ([FAST](../../sources/fast-paper.md)), fridge restocking as one of eleven teleoperated tasks in [HIW-500](../../sources/bitrobot-hiw-500-dataset-page.md), and a research robot opening a fridge 10 times in 10 in one apartment ([TidyBot++](../../sources/tidybot-plus-plus-paper.md)). No source reports a success rate for putting groceries away.

Cumulative probability (%), same convention as set B.

| ID | Event | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 28Q1 | 28Q2 | 28Q3 | 28Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **To the door** | | | | | | | | | | |
| D1 | A sidewalk-robot operator reports 20 million or more cumulative deliveries (Starship reported 10 million in June 2026) | 1 | 3 | 7 | 12 | 18 | 25 | 32 | 39 | 46 |
| D2 | A grocery retailer reports that robots deliver 30% or more of its online orders in some country or region (S Group reports up to 20% in Finland) | 1 | 3 | 6 | 10 | 14 | 18 | 22 | 26 | 30 |
| **In the store** | | | | | | | | | | |
| D3 | A remotely piloted in-store picking robot (Blue Collar Robotics or similar) reports paid-trial results with throughput and operator-to-robot ratio | 5 | 15 | 27 | 38 | 47 | 54 | 60 | 65 | 69 |
| D4 | A retailer announces a commercial deployment, not a trial, of robots picking customer orders from ordinary store shelves in 5 or more stores | 0 | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 |
| D5 | Published autonomous shopping from a list retrieves 70% or more of listed items in an unmodified store (TRI's best: 28.9% of items) | 1 | 3 | 6 | 10 | 15 | 20 | 26 | 32 | 38 |
| D6 | Published autonomous shopping completes 50% or more of runs in daytime with shoppers present | 0 | 1 | 3 | 5 | 8 | 12 | 16 | 20 | 24 |
| D7 | Published autonomous shopping handles produce or refrigerated items at 50% or better item success | 1 | 2 | 5 | 8 | 12 | 16 | 21 | 26 | 31 |
| D8 | A retailer provides follow-me carriers or shopping-assist robots for older or disabled shoppers in 10 or more stores | 2 | 4 | 7 | 10 | 14 | 18 | 22 | 26 | 30 |
| **At home** | | | | | | | | | | |
| D9 | A published result: a robot unpacks groceries and puts them away in fridge and cupboards in 5+ unseen homes at 60% or better full-task success, 50+ trials | 1 | 3 | 7 | 12 | 18 | 24 | 30 | 36 | 42 |
| D10 | A purchasable home robot ships putting groceries away as a listed feature, at any level of remote assistance | 1 | 2 | 5 | 9 | 14 | 19 | 25 | 31 | 37 |
| D11 | A purchasable home robot carries groceries in from the door or car, confirmed by an independent review | 0 | 1 | 3 | 5 | 8 | 12 | 16 | 20 | 25 |
| D12 | A shipping home robot with arms offers automatic reordering based on what it sees in the kitchen | 2 | 5 | 9 | 14 | 19 | 24 | 29 | 34 | 39 |
| **End to end** | | | | | | | | | | |
| D13 | A general-purpose robot leaves a home, shops in a store and returns with the groceries without teleoperation, as a published or independently reported demonstration | 0 | 1 | 2 | 3 | 5 | 7 | 9 | 12 | 15 |
| D14 | A consumer can buy or subscribe to a service that does a household's grocery shopping with no human picker: robot picking in the store plus delivery, in any city | 0 | 0 | 1 | 2 | 4 | 6 | 8 | 11 | 14 |

| ID | Event (short) | 29Q1 | 29Q2 | 29Q3 | 29Q4 | 30Q1 | 30Q2 | 30Q3 | 30Q4 |
|---|---|---|---|---|---|---|---|---|---|
| D1 | 20M sidewalk deliveries | 52 | 58 | 63 | 68 | 72 | 75 | 78 | 80 |
| D2 | Robots deliver 30%+ of a retailer's online orders | 34 | 38 | 41 | 44 | 47 | 50 | 52 | 54 |
| D3 | Piloted picker reports trial results | 72 | 75 | 77 | 79 | 81 | 82 | 83 | 84 |
| D4 | Commercial shelf-picking in 5+ stores | 34 | 39 | 43 | 47 | 51 | 54 | 57 | 60 |
| D5 | Autonomous shopping at 70%+ of items | 43 | 48 | 53 | 57 | 61 | 64 | 67 | 70 |
| D6 | Daytime shopping, 50%+ of runs | 28 | 32 | 36 | 40 | 44 | 47 | 50 | 53 |
| D7 | Produce or chilled items at 50%+ | 36 | 40 | 44 | 48 | 52 | 55 | 58 | 61 |
| D8 | Shopping-assist robots in 10+ stores | 34 | 37 | 40 | 43 | 46 | 49 | 51 | 53 |
| D9 | Put-away at 60%+ in unseen homes, published | 47 | 52 | 56 | 60 | 64 | 67 | 70 | 73 |
| D10 | Put-away shipped as a feature | 42 | 47 | 52 | 56 | 60 | 63 | 66 | 69 |
| D11 | Carries groceries in from the door | 29 | 33 | 37 | 41 | 45 | 48 | 51 | 54 |
| D12 | Robot reorders from what it sees | 43 | 47 | 51 | 55 | 58 | 61 | 64 | 66 |
| D13 | Home-to-store-and-back demonstration | 18 | 21 | 24 | 27 | 30 | 33 | 36 | 39 |
| D14 | Robot-only shopping service on sale | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 38 |

**The direct answer.**
- **Delivery to the door** keeps growing where retailers offer it (D1 at 46% by the end of 2028, 80% by 2030), but it stays a regional service.
- **Picking in the store** arrives first with a remote human pilot (D3 passes 50% in early 2028). A commercial rollout in five or more stores is about even odds by the start of 2030 (D4).
- **Putting groceries away at home** is the first household-side task: a published result at about even odds by mid-2029 (D9), and a shipped feature at about the same time (D10).
- **A robot that does your shopping for you**, end to end with no human picker, is 38% by the end of 2030 (D14). The median date is beyond this forecast.

**Reasoning.**
- **The store is harder than the home for a robot, and the home is where nobody is working yet.** Stores have tight shelves, other shoppers and thousands of products; TRI's chain of 103 actions is why 99% per action still fails two runs in three. But stores have a paying customer, the retailer, which is why piloted picking gets trials first.
- **Put-away borrows from general household progress.** It is pick-and-place into a fridge and cupboards, with deformable bags and some fragile items. It should track tidying (B10) with a lag of a year or more, since no one has published on it yet. D9 is set accordingly.
- **Produce, chilled goods and glass are the excluded majority.** TRI's exclusions cover much of a real shopping list. D7 trails D5 for that reason.
- **Carrying bags in is a mobility problem.** Thresholds, steps and doors are where wheeled home robots stop, so D11 is lower than D10 throughout.
- **End-to-end needs every link at once.** D14 requires store picking without a human picker and delivery, both commercial, in the same place. Commercial shelf-picking alone (D4) is only 60% by the end of 2030.

**Notes on resolution.**
- **D1–D2:** company-reported figures count, labelled as such.
- **D3–D4:** warehouses, dark stores and micro-fulfilment centres do not count; the robot must pick from shelves customers also use.
- **D5–D7:** the store must be unmodified and the list given at run time. D6 requires the paper to state that shoppers were present.
- **D9:** "unseen" means homes the system was not trained in; full-task means every item put away.
- **D10–D12:** "purchasable" and "shipping" as in set A.
- **D13:** any published or independently reported end-to-end run counts, even a single one.
- **D14:** a service with a human picker and robot delivery does not count.

## Prediction set F: meal preparation and cooking (added 2026-11-16)

**The question:** when do home robots prepare food, from making coffee to cooking a meal?

(The set is lettered F. The letter E is used by the [assistive forecast](../assistive/assistive-robot-forecast-2026-2030.md), and the two pages are scored together.)

**Where it stands** (evidence as of 2026-11-16):
- **Nothing you can buy cooks.** The [household robots comparison](../platforms/household-robots-comparison.md) lists cooking and opening cans as unavailable, and notes that no reviewed source shows any robot opening a can. [Flourish 1](../../entities/flourish-1.md) excludes water, anything sharp and anything breakable.
- **Stovetop cooking has one research data point.** [Mobile ALOHA](../../sources/mobile-aloha-paper.md) cooked shrimp (oil and shrimp into the pan, flip with a spatula, pour into a bowl) at **40%** success with co-training, in its own kitchen, from 20 demonstrations. Rinsing the pan reached 80%.
- **Appliances and drinks are further along.** [π\*0.6](../../sources/pistar06-paper.md) made espresso drinks for 13 hours continuously on a professional machine. Microwave, toaster and rice-cooker tasks appear as lab tasks ([π0](../../sources/pi-zero-paper.md), [FAST](../../sources/fast-paper.md), [a Stretch 3 study](../../sources/robot-self-improvement-human-video-dynamics-paper.md) that took five long-horizon tasks from 41.3% to 85.3%).
- **The broad benchmark is low.** BEHAVIOR-1K, whose tasks include cooking and slicing states, has a best full-task success of 12.4% ([AI Index](../../sources/stanford-hai-ai-index-2026.md); [paper](../../sources/behavior-1k-paper.md)).
- **Commercial kitchens already use classical robots.** [Dexai](../../entities/dexai-robotics.md)'s arm assembles bowls and salads with standard utensils, per live-web facts on its entity page, not an ingested source. That is engineered automation, not a learned general policy.
- **Assistive users already get value at low autonomy.** One Stretch user serves himself a protein shake, mostly by teleoperation ([TechCrunch](../../sources/techcrunch-hello-robot-homes-2026.md)).

Cumulative probability (%), same convention as set B.

| ID | Event | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 28Q1 | 28Q2 | 28Q3 | 28Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Appliances and cold food** | | | | | | | | | | |
| F1 | Published: a robot makes a hot drink or runs a countertop appliance (coffee machine, microwave, toaster, rice cooker) start to finish in 5+ unseen homes at 70% or better, 50+ trials | 3 | 8 | 14 | 21 | 28 | 35 | 42 | 48 | 54 |
| F2 | A purchasable home robot ships a hot-drink or countertop-appliance feature, at any level of remote assistance | 1 | 3 | 6 | 10 | 15 | 20 | 26 | 32 | 38 |
| F3 | Published: a cold meal (sandwich, salad or bowl) assembled from ingredients in 3+ unseen kitchens at 60% or better, 50+ trials | 2 | 5 | 9 | 14 | 20 | 26 | 32 | 38 | 44 |
| F4 | Published: sealed food containers (cans, jars or packets) opened at 70% or better on a home-capable robot, 30+ trials | 2 | 5 | 9 | 13 | 18 | 23 | 28 | 33 | 38 |
| **Cooking with heat and knives** | | | | | | | | | | |
| F5 | Published: a multi-step stovetop dish (heat, add ingredients, stir or flip, plate) in 3+ unseen kitchens at 60% or better, 30+ trials (Mobile ALOHA: 40% in its own kitchen) | 1 | 3 | 5 | 8 | 12 | 16 | 21 | 26 | 31 |
| F6 | Published: real food cut or chopped by a general-purpose robot in 3+ unseen kitchens at 60% or better, with a stated safety mechanism for the blade | 1 | 3 | 5 | 8 | 11 | 15 | 19 | 23 | 27 |
| F7 | Published: a complete meal of 2+ dishes cooked from raw ingredients, autonomously, in a home kitchen, with 10+ trials reported at any success rate | 1 | 2 | 4 | 7 | 10 | 14 | 18 | 22 | 27 |
| F8 | A robot plans a meal from what is in the fridge, cooks it and cleans up, shown end to end without teleoperation in a home, even once | 0 | 1 | 2 | 4 | 6 | 9 | 12 | 16 | 20 |
| **Products** | | | | | | | | | | |
| F9 | A purchasable general-purpose home robot ships stovetop or oven cooking as a listed feature, at any level of remote assistance | 0 | 1 | 2 | 4 | 6 | 9 | 12 | 16 | 20 |
| F10 | A purchasable home robot cooks a hot meal **unattended** (no remote human), confirmed by an independent review | 0 | 0 | 1 | 1 | 2 | 4 | 6 | 8 | 11 |
| F11 | A restaurant or food-service operator announces robots running a general-purpose learned policy from a foundation-model vendor doing food preparation in 10+ locations | 2 | 5 | 9 | 13 | 18 | 23 | 28 | 33 | 38 |
| **Assistive, benchmark and safety** | | | | | | | | | | |
| F12 | Published: an in-home study in which a robot prepares a simple meal or drink for 5+ users with disabilities (beyond feeding) | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 | 34 |
| F13 | The best published full-task success on BEHAVIOR-1K or its successor reaches 40% (12.4% in 2025) | 1 | 3 | 6 | 10 | 15 | 21 | 27 | 33 | 39 |
| F14 | A publicly reported kitchen fire, burn or cut attributed to a home robot | 0 | 1 | 2 | 4 | 6 | 8 | 11 | 14 | 17 |

| ID | Event (short) | 29Q1 | 29Q2 | 29Q3 | 29Q4 | 30Q1 | 30Q2 | 30Q3 | 30Q4 |
|---|---|---|---|---|---|---|---|---|---|
| F1 | Appliance or hot drink at 70%+, published | 59 | 64 | 68 | 72 | 75 | 78 | 80 | 82 |
| F2 | Appliance feature shipped | 43 | 48 | 53 | 57 | 61 | 65 | 68 | 71 |
| F3 | Cold meal assembly at 60%+, published | 49 | 54 | 58 | 62 | 66 | 69 | 72 | 74 |
| F4 | Opens cans, jars or packets at 70%+ | 43 | 47 | 51 | 55 | 58 | 61 | 64 | 67 |
| F5 | Stovetop dish at 60%+ in unseen kitchens | 36 | 41 | 45 | 49 | 53 | 57 | 60 | 63 |
| F6 | Knife work at 60%+, with a safety mechanism | 31 | 35 | 39 | 43 | 46 | 49 | 52 | 55 |
| F7 | Full 2-dish meal cooked, published | 31 | 35 | 39 | 43 | 47 | 50 | 53 | 56 |
| F8 | Plan, cook and clean up, end to end | 24 | 28 | 32 | 36 | 40 | 43 | 46 | 49 |
| F9 | Stovetop or oven feature shipped | 24 | 28 | 32 | 36 | 40 | 44 | 47 | 50 |
| F10 | Hot meal cooked unattended | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |
| F11 | Learned-policy food prep in 10+ commercial sites | 43 | 47 | 51 | 55 | 58 | 61 | 64 | 66 |
| F12 | Meal prep for 5+ disabled users at home | 38 | 42 | 46 | 50 | 53 | 56 | 59 | 61 |
| F13 | BEHAVIOR-1K at 40%+ | 44 | 49 | 54 | 58 | 62 | 65 | 68 | 71 |
| F14 | Reported kitchen fire, burn or cut | 20 | 23 | 26 | 29 | 32 | 35 | 38 | 40 |

**The direct answer.**
- **Hot drinks and countertop appliances come first**: a published result in unseen homes at about even odds by the end of 2028 (F1), and a shipped feature by mid-2029 (F2).
- **Cold meal assembly** follows, at about even odds by mid-2029 (F3).
- **Stovetop cooking** in unseen kitchens is about even odds as a published result by the end of 2029 (F5), and as a shipped feature only by the end of 2030 (F9, 50%).
- **A hot meal cooked unattended** by a robot you can buy is 35% by the end of 2030 (F10). The median date is beyond this forecast.

**Reasoning.**
- **Cooking stacks the hard things.** Heat, liquids, knives, deformable food, timing and a long chain of steps, with failures that cannot be undone: burnt food at best, a fire at worst. That is why every stovetop row trails its appliance counterpart by a year or more.
- **Appliances are short and structured.** Pressing buttons, loading a pod or a plate and waiting is close to the pick-and-place work that is already improving fast, and the appliance contains the heat.
- **Liability will set the product order.** A vendor can ship "microwave a meal" long before "use the stove", because the stove is a fire risk in an unattended home. F9 and F10 are held down by that, not only by capability. Expect interlocks and a person present to be required at first.
- **Knives are a safety question before a skill question.** This wiki's own robot stack has a rail built to refuse `pick(knife)` ([guardrails](../agents/guardrails-for-robot-agents.md)). F6 requires a stated safety mechanism for that reason.
- **Commercial kitchens pay first.** As with grocery picking, a business customer with a fixed menu and a controlled space is an easier first market than a home (F11 leads F9 throughout).
- **Assistive meal prep may arrive earlier in practice than F12 suggests**, because a user who directs the robot step by step does not need autonomy. F12 counts published studies, which lag.

**Notes on resolution.**
- **F1, F3, F5, F6:** "unseen" means homes or kitchens the system was not trained in. A fixed demo kitchen does not count.
- **F2, F9, F10:** "purchasable" and "shipping" as in set A. A dedicated cooking appliance, such as an automatic stir-fry machine, is not a home robot for these rows.
- **F7, F8:** the paper or report must state that no teleoperation was used.
- **F11:** the vendor must be a general-purpose robot-policy company; purpose-built kitchen automation does not count.
- **F13:** only if a new result is published on the benchmark or a named successor.
- **F14:** a robot vacuum or a cooking appliance does not count.

## Prediction set G: laundry and cleaning (added 2026-11-16)

**The question:** when do home robots take over laundry and cleaning, beyond the folding, tidying and dishes events already in set B?

**What set B already covers, and this set does not repeat:** folding at 80% in unseen homes (B9), whole-room tidying (B10), folding with no remote human (B13), and dishes (B14, B15). Set G adds the rest of the laundry cycle, garment variety and speed, wet cleaning, and cleaning sold as a service.

**Where it stands** (evidence as of 2026-11-16):
- **Laundry is the best-evidenced chore in the wiki.**
  - [Helix 2.5](../../sources/figure-helix-2-5.md) folded all four towels in 62% of trials and made beds in 67%, across 30 unseen homes.
  - [X-VLA](../../sources/xvla-paper.md) reports about 100% success at 33 folds an hour in its own setup, after 1,200 demonstrations.
  - [π\*0.6](../../sources/pistar06-paper.md) folded novel laundry for 2+ hours in a new home.
  - [Weave's Isaac 0](../../entities/weave-robotics.md) is a shipping folding product in California, at 30–90 minutes a load with remote correction ([eWeek](../../sources/eweek-weave-isaac-0.md)); the company cites 2,000+ field hours.
  - [Isaac 1](../../sources/weave-isaac-1-product-page.md) advertises finding dirty clothes, handling hampers, folding and putting clothes away, with teleoperation when needed. No delivery is confirmed.
  - [TidyBot++](../../sources/tidybot-plus-plus-paper.md) loaded laundry 7 times in 10 in one apartment.
- **Cleaning has research results for dry and light-wet tasks.** TidyBot++ wiped a counter 9 times in 10 and took out trash 10 in 10, in one apartment. [Mobile ALOHA](../../sources/mobile-aloha-paper.md) wiped a wine spill at 95% in its own kitchen.
- **Floors are solved by a different product.** Robot vacuums are the one household robot that works unattended. The arm on the [Saros Z70](../../sources/roborock-saros-z70.md) is limited to 300 g, and a reviewer could not get it to tidy anything automatically.
- **Whole-home cleaning exists only with a human pilot.** [Tau Robotics](../../entities/tau-robotics.md) sends piloted humanoids to dust, wipe, clean toilets, vacuum and mop in two metro areas, by invitation. Its terms say *"The robot is not autonomous"*, and it publishes no intervention rate ([service pages](../../sources/tau-robotics-service-site.md)). A reporter found it *"thorough but slow"*, with spills ([MIT Technology Review](../../sources/mit-technology-review-tau-cleaning.md)).
- **Some products exclude water outright.** [Flourish 1](../../entities/flourish-1.md) lists *"No water"* among its limits.

Cumulative probability (%), same convention as set B.

| ID | Event | 26Q4 | 27Q1 | 27Q2 | 27Q3 | 27Q4 | 28Q1 | 28Q2 | 28Q3 | 28Q4 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Laundry** | | | | | | | | | | |
| G1 | Published: mixed household laundry (shirts and trousers, not only towels) folded in unseen homes with 80% or more of items acceptable, 200+ items | 3 | 8 | 15 | 22 | 30 | 37 | 44 | 50 | 56 |
| G2 | Published: 60 or more items folded per hour, sustained for an hour, on mixed laundry by a home-capable robot (X-VLA: 33 an hour) | 2 | 5 | 9 | 14 | 20 | 26 | 32 | 38 | 44 |
| G3 | Published: a full laundry cycle (gather, load the washer, start it, move to dryer or rack, fold) done autonomously in 3+ unseen homes at 50% or better, 30+ trials | 1 | 3 | 6 | 10 | 15 | 20 | 26 | 32 | 38 |
| G4 | Published: garments ironed or hung on hangers at 60% or better in unseen homes | 1 | 2 | 4 | 7 | 10 | 14 | 18 | 22 | 26 |
| G5 | A purchasable home robot loads and unloads a washing machine as a shipped feature, at any level of remote assistance | 2 | 6 | 11 | 17 | 23 | 29 | 35 | 41 | 47 |
| G6 | A purchasable home robot puts folded clothes away in drawers or closets, confirmed by an independent review | 2 | 6 | 11 | 16 | 22 | 28 | 34 | 40 | 45 |
| G7 | A home laundry robot or service reports 1,000 or more paying households | 1 | 3 | 6 | 10 | 15 | 21 | 27 | 33 | 39 |
| **Cleaning** | | | | | | | | | | |
| G8 | Published: kitchen surfaces (counter, table or stovetop) wiped to a measured cleanliness criterion in 5+ unseen homes at 70% or better, 50+ trials | 3 | 8 | 14 | 21 | 28 | 35 | 42 | 48 | 54 |
| G9 | Published: a bathroom fixture (toilet, sink or shower) cleaned autonomously in 3+ unseen homes at 60% or better | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 | 34 |
| G10 | Published: bed making at 85% or better zero-shot in unseen homes (Helix 2.5: 67%) | 3 | 8 | 15 | 22 | 30 | 37 | 44 | 50 | 56 |
| G11 | A purchasable home robot ships surface wiping or bathroom cleaning as a listed feature, at any level of remote assistance | 1 | 3 | 7 | 12 | 18 | 24 | 30 | 36 | 42 |
| G12 | A purchasable home robot cleans a bathroom **unattended** (no remote human), confirmed by an independent review | 0 | 0 | 1 | 2 | 4 | 6 | 8 | 11 | 14 |
| G13 | A purchasable home robot takes household trash to an outdoor bin as a shipped feature | 0 | 1 | 2 | 4 | 6 | 9 | 12 | 16 | 20 |
| G14 | A robot vacuum with an arm earns a major reviewer's verdict that the arm reliably clears floor clutter | 2 | 5 | 9 | 14 | 19 | 24 | 29 | 34 | 39 |
| **Cleaning as a service** | | | | | | | | | | |
| G15 | A robot cleaning service states that its robots work without a live human pilot for most of a visit, in paying homes | 1 | 3 | 6 | 10 | 15 | 20 | 26 | 32 | 38 |
| G16 | A robot cleaning service operates in 10 or more metropolitan areas | 1 | 3 | 6 | 10 | 14 | 19 | 24 | 29 | 34 |

| ID | Event (short) | 29Q1 | 29Q2 | 29Q3 | 29Q4 | 30Q1 | 30Q2 | 30Q3 | 30Q4 |
|---|---|---|---|---|---|---|---|---|---|
| G1 | Mixed-garment folding at 80%+, published | 61 | 66 | 70 | 74 | 77 | 80 | 82 | 84 |
| G2 | Folding at 60+ items an hour | 49 | 54 | 58 | 62 | 66 | 69 | 72 | 75 |
| G3 | Full laundry cycle at 50%+, published | 43 | 48 | 53 | 57 | 61 | 65 | 68 | 71 |
| G4 | Ironing or hanging at 60%+ | 30 | 34 | 38 | 42 | 45 | 48 | 51 | 54 |
| G5 | Washer loading shipped | 52 | 57 | 61 | 65 | 68 | 71 | 74 | 76 |
| G6 | Puts clothes away, reviewed | 50 | 55 | 59 | 63 | 66 | 69 | 72 | 74 |
| G7 | Laundry robot at 1,000+ households | 44 | 49 | 54 | 58 | 62 | 65 | 68 | 71 |
| G8 | Surface wiping at 70%+, published | 59 | 64 | 68 | 72 | 75 | 78 | 80 | 82 |
| G9 | Bathroom cleaning at 60%+, published | 39 | 43 | 47 | 51 | 55 | 58 | 61 | 64 |
| G10 | Bed making at 85%+ | 61 | 66 | 70 | 74 | 77 | 80 | 82 | 84 |
| G11 | Wet cleaning feature shipped | 47 | 52 | 56 | 60 | 64 | 67 | 70 | 73 |
| G12 | Bathroom cleaned unattended | 17 | 20 | 23 | 26 | 29 | 32 | 35 | 38 |
| G13 | Takes the trash out | 24 | 28 | 32 | 36 | 40 | 43 | 46 | 49 |
| G14 | Vacuum arm that reliably tidies | 43 | 47 | 51 | 55 | 58 | 61 | 64 | 66 |
| G15 | Cleaning service mostly autonomous | 43 | 48 | 53 | 57 | 61 | 65 | 68 | 71 |
| G16 | Cleaning service in 10+ metros | 39 | 43 | 47 | 51 | 55 | 58 | 61 | 64 |

**The direct answer.**
- **Folding gets good before the rest of laundry does.** Mixed-garment folding at 80% is about even odds as a published result by late 2028 (G1). The full cycle, from hamper to folded pile, reaches even odds around mid-2029 (G3).
- **Putting clothes away and loading the washer** arrive as product features at about even odds in early 2029 (G5, G6), probably with remote help at first.
- **Wiping surfaces** is about even odds as a published result by the end of 2028 (G8). **Bathrooms trail** by a year or more (G9), and a bathroom cleaned unattended by a robot you can buy is 38% by the end of 2030 (G12).
- **Cleaning as a service** becomes mostly autonomous at about even odds by mid-2029 (G15). That may be how most households first get robot cleaning.

**Reasoning.**
- **Laundry forgives mistakes.** A badly folded shirt costs nothing, so vendors can ship early and improve in the field. That, plus three independent lines of evidence, is why the laundry rows lead every other chore on this page.
- **The cycle is harder than the fold.** Gathering clothes from around a home, opening a washer, and moving wet, tangled fabric are separate skills with almost no published results. G3 is held down by the weakest link.
- **Speed is its own barrier.** Thirty to ninety minutes a load is tolerable for a machine that works while you are out, but only if it needs no supervision. G2 tracks whether throughput catches up.
- **Water divides the cleaning tasks.** Dry tidying and light wiping are near what works today. Bathrooms add water, chemicals, tight spaces and hygiene standards, and some hardware is not built for water at all.
- **Services can launch before products.** A service keeps the robot under the vendor's control, with a pilot available and maintenance in-house. Tau already operates that way. G15 asks when the pilot stops being needed most of the time.
- **Vacuums may absorb part of this.** A robot vacuum with a capable arm would do floor clutter without a general-purpose robot (G14), which would reduce the demand set A assumes.

**Notes on resolution.**
- **G1, G3, G8–G10:** "unseen" means homes the system was not trained in. Vendor-published results count if they state trial counts.
- **G2:** the rate must be measured on real mixed laundry, not a single repeated item.
- **G5, G6, G11–G13:** "purchasable" and "shipping" as in set A.
- **G7:** company-reported figures count, labelled as such.
- **G12:** as B13 and B15, the vendor must state that no teleoperation is used for the task in normal operation.
- **G14:** outlets as in B17.
- **G15:** a vendor statement counts; note whether an intervention rate is published with it.

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
| 10 | 2029-03-31 | April 2029 | pending |
| 11 | 2029-06-30 | July 2029 | pending |
| 12 | 2029-09-30 | October 2029 | pending |
| 13 | 2029-12-31 | January 2030 | pending |
| 14 | 2030-03-31 | April 2030 | pending |
| 15 | 2030-06-30 | July 2030 | pending |
| 16 | 2030-09-30 | October 2030 | pending |
| 17 | 2030-12-31 | January 2031 | pending |

**Method.**
- **Sets B, C, D, F and G:** for each event, record 1 if it happened by the quarter's end, else 0. The score is the **Brier score**, the squared difference between the forecast probability and the outcome, averaged over the set's events (20 in B, 13 in C, 14 in D, 14 in F, 16 in G). Report the five sets separately. Lower is better. Always answering 50% scores 0.25.
- **Set A:** build the tally table, then record hit, miss or unresolved, plus the ratio of the tally's midpoint to the point estimate.
- **Calibration:** from checkpoint 3 on, group all scored cells from sets B, C, D, F and G by forecast probability (0–10%, 10–30%, 30–70%, 70–90%, 90–100%) and compare with the observed frequency.
- **Evidence:** every resolution cites a source. A primary that matters to a decision gets ingested, per the wiki's primary-sources rule.
- **Disputes:** if the evidence is ambiguous, mark the cell unresolved and exclude it from the average. Do not resolve in the forecast's favour.

### Scorecard

*(Appended after each checkpoint. Nothing above this line changes.)*

| Checkpoint | Set A result | Set B Brier | Set C Brier | Set D Brier | Set F Brier | Set G Brier | Events resolved yes | Notes |
|---|---|---|---|---|---|---|---|---|
| 1 (2026-Q4) | | | | | | | | |
| 2 (2027-Q1) | | | | | | | | |
| 3 (2027-Q2) | | | | | | | | |
| 4 (2027-Q3) | | | | | | | | |
| 5 (2027-Q4) | | | | | | | | |
| 6 (2028-Q1) | | | | | | | | |
| 7 (2028-Q2) | | | | | | | | |
| 8 (2028-Q3) | | | | | | | | |
| 9 (2028-Q4) | | | | | | | | |
| 10 (2029-Q1) | | | | | | | | |
| 11 (2029-Q2) | | | | | | | | |
| 12 (2029-Q3) | | | | | | | | |
| 13 (2029-Q4) | | | | | | | | |
| 14 (2030-Q1) | | | | | | | | |
| 15 (2030-Q2) | | | | | | | | |
| 16 (2030-Q3) | | | | | | | | |
| 17 (2030-Q4) | | | | | | | | |

## Known weaknesses of this forecast

- **China.** The wiki has little on Chinese consumer vendors. If the volume comes from there, set A is too low and the wiki will be slow to see it.
- **Correlated cells.** A cumulative event that resolves early scores well in every later column, so the nine checkpoints are not independent tests.
- **Counting.** Vendors report "delivered", "shipped" and "sold" loosely. Figure's 350 "delivered" units are not homes.
- **Thin base rates.** No general-purpose home robot has ever shipped at volume, so every number here is extrapolated from announcements and research results.
- **Set C depends on disclosure.** Vendors rarely say what is inside their models. C10–C12 can be true and unresolvable; such cells are marked unresolved, which biases the scored record toward research events.
- **Sets B and G overlap.** Folding, tidying and bed making appear in both at different thresholds, so their cells rise and fall together. Read the two Brier scores as related, not independent.
- **Set F rests on very little.** One stovetop result in one kitchen, one long espresso run and a handful of lab appliance tasks. The cooking rows are extrapolated from general household progress more than from cooking evidence.
- **Set D leans on company figures.** Delivery counts and retailer shares are self-reported, and the home-side rows start from almost no evidence, so their probabilities are the least anchored on the page.
- **Horizon.** Four years is long for this field. The 2029–2030 columns should be read as a statement of today's beliefs, to be replaced by a new dated forecast well before then.

## Related

- [Assistive robot forecast](../assistive/assistive-robot-forecast-2026-2030.md) — the companion forecast for disabled and older users, scored on the same dates
- [Household robots compared](../platforms/household-robots-comparison.md) — the current field, and the evidence table this forecast starts from
- [Consumer robotics value chain](consumer-robotics-value-chain.md) — who profits if these volumes happen
- [Home robot privacy and security](../platforms/home-robot-privacy-and-security.md)
- [Long-term in-home robot deployments](../assistive/long-term-in-home-robot-deployments.md)
- [VLA success-rate audit](../platforms/vla-success-rate-audit.md) — why trial counts matter when scoring B9–B12
- [Robot safety standards](../../concepts/robotics/robot-safety-standards.md), [DAgger and interactive imitation](../../concepts/learning/dagger.md)
- [Retail and grocery robotics](../../concepts/robotics/retail-and-grocery-robotics.md) — the evidence behind set D
- [JEPA for a household mobile manipulator](../world-models/jepa-for-household-mobile-manipulator.md) — the three conditions set C tracks
- [Three ways to scale a JEPA world model](../world-models/three-ways-to-scale-a-jepa-world-model.md), [JEPA](../../concepts/world-models/jepa.md), [AMI Labs](../../entities/ami-labs.md), [Yann LeCun](../../entities/yann-lecun.md)
