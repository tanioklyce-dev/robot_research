---
title: The Robot AI industry — structure, capital, and the gap between the two
type: synthesis
created: 2026-08-29
updated: 2026-08-29
tags: [industry, physical-ai, humanoid, market-structure, capital, automotive, vertical-integration, economics-of-ml, synthesis]
---

# The Robot AI industry — structure, capital, and the gap between the two

A map of the industry building Robot AI: what the layers are, who occupies which, where the money comes from, and how far the deployed capability is from the capital committed against it. Companion to [Who benefits from consumer robotics](consumer-robotics-value-chain.md), which reasons *upward from BOMs* about where value accrues in the consumer tier. This page reasons *across the whole industry* about who is positioned where and on what evidence.

> [!warning] Epistemic status — two kinds of claim on this page, marked differently
> This wiki is built from ingested sources and holds **almost no market data** — no revenues, no unit forecasts, no market sizing, no private-company financials. That constraint has not changed. This page therefore mixes two things and labels which is which:
>
> - **Wiki-sourced claims** link to a source page, as everywhere else. These are the load-bearing ones.
> - **Live-web facts** — funding rounds, ownership stakes, production targets — are marked `[live-web]` with a direct link, following the convention on [Russ Tedrake](../../entities/russ-tedrake.md). They are **not ingested sources**: no page has read the primary, no hash seals them, and several come from trade press rather than company filings. Treat them as orientation, not as evidence you would quote in a decision. Anything load-bearing should be promoted to a real ingest first — see [primary sources for decision-grade claims](../../../CLAUDE.md).
>
> Funding figures in particular are the weakest class here. Announced round sizes and post-money valuations are **company-disclosed, unaudited, and selection-biased** — rounds that do not close are not announced.

---

## 1. The number the whole industry is priced against

Start with the gap, because everything structural follows from it.

| | Figure | Source |
|---|---|---|
| Robot policy success, **controlled simulation** | **89.4%** (EquAct on RLBench, 18-task subset) | [AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) |
| Robot policy success, **realistic household tasks** | **12.4%** ([BEHAVIOR-1K](../../entities/behavior-benchmark.md) Challenge, top team) | [AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) |
| Safe completion on hazard-bearing tasks | **0.64** SSR (best model, ResponsibleRobotBench) | [AI Index 2026](../../sources/stanford-hai-ai-index-2026.md) |
| Humanoid venture funding, 2026 through July | **$8.7B** (Dealroom) | `[live-web]` [TechCrunch](https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/) |

**Capital is being committed against demonstrated capability of roughly one task in eight**, in the one benchmark that tries to be realistic. The AI Index's own summary is that "reliably executing household tasks in realistic environments is still beyond current capabilities," and that VLA technology "remains at the research stage."

And the 12.4% is generous, because most published robot success rates cannot support the precision they are quoted to. A ±2 pp confidence band needs ≈**1,030 rollouts**; typical evaluations run a fraction of that ([success-rate audit](../platforms/vla-success-rate-audit.md)). The honest reading is not "12.4% and rising" but "single-digit-to-low-double-digit, with error bars wide enough to swallow most claimed year-over-year progress."

This is the central fact of the industry as of 2026. Every structural choice below is a different bet about how that gap closes — or about getting paid before it does.

---

## 2. The layers, and who is structurally safe

Ordered by how close to the physical robot the value sits.

| Layer | Who | Position |
|---|---|---|
| **Silicon** | [NVIDIA](../../entities/nvidia.md) — **>60%** of global AI compute; TSMC fabricates nearly every leading AI chip ([AI Index](../../sources/stanford-hai-ai-index-2026.md)) | Paid regardless of which robot wins, and regardless of whether any ships |
| **Actuators** | [FeeTech](../../entities/feetech.md), [Dynamixel](../../entities/dynamixel.md), Chinese QDD suppliers | **86%** of one documented exoskeleton BOM ([UME](../../sources/ume-paper.md)). One actuator per DoF — the cost that scales with the product |
| **Platforms** | [Unitree](../../entities/unitree-g1.md), [Figure](../../entities/figure.md), [Apptronik](../../entities/apptronik-apollo.md), [1X](../../entities/1x-neo.md), [AgiBot](../../entities/agibot.md), [Boston Dynamics](../../entities/boston-dynamics.md), [XPENG Robotics](../../entities/xpeng-robotics.md) | Where the capital and the attention are; also where the capability gap bites |
| **Models** | [Physical Intelligence](../../entities/physical-intelligence.md), [NVIDIA GR00T](../../entities/nvidia-groot.md), [Gemini Robotics](../../entities/gemini-robotics.md), [TRI](../../entities/tri.md) / [Walden](../../entities/walden-robotics.md), [Skild AI](../../entities/skild-ai.md) | The bet that policy generalizes across bodies, making the body a commodity |
| **Deployment** | [Waymo](../../entities/waymo.md) (~2,500 robotaxis, ~450k weekly trips), Baidu Apollo Go (~11M driverless rides in 2025) ([AI Index](../../sources/stanford-hai-ai-index-2026.md)) | The one part of Physical AI with unambiguous commercial scale — and it is *driving*, not manipulation |

> [!note] The most under-remarked line in that table
> **Autonomous driving is the only layer with proven, large-scale, paid deployment**, and it solved a narrower problem than manipulation: one body, one task, enormous data, no contact. Every humanoid thesis implicitly claims manipulation will follow the same curve. Nothing in this wiki establishes that it will, and the [12.4%](#1-the-number-the-whole-industry-is-priced-against) says it has not yet.

---

## 3. Four postures

Companies in this industry are making one of four structurally different bets.

**Vertically integrated** — build the body, the model, and the factory. [Tesla Optimus](../../entities/tesla-optimus.md) (FSD-derived stack, closed development, no academic availability), [Figure](../../entities/figure.md) ([Helix](../../entities/helix.md) in-house after the OpenAI partnership dissolved in 2024; [BotQ](../../entities/botq.md) manufacturing reached one robot per hour in April 2026), [XPENG Robotics](../../entities/xpeng-robotics.md). Captures everything if it works; carries every risk if the capability gap persists.

**Model-layer** — sell the policy, let others build bodies. [Physical Intelligence](../../entities/physical-intelligence.md)'s π-series, [NVIDIA GR00T](../../entities/nvidia-groot.md), [Gemini Robotics](../../entities/gemini-robotics.md). The thesis is cross-embodiment generalization — π0 folding laundry across platforms without task-specific retraining ([AI Index](../../sources/stanford-hai-ai-index-2026.md)). If it holds, hardware commoditizes and this layer takes the margin.

**Platform / commodity hardware** — win on price and volume. [Unitree](../../entities/unitree-g1.md) (R1 from **$4,900**, G1 from **$13,500** — [AI Index](../../sources/stanford-hai-ai-index-2026.md)) is the clearest case, and the pattern already played out one tier down: [FeeTech](../../entities/feetech.md)'s ~3× price advantage over [Dynamixel](../../entities/dynamixel.md) is why **SO-10X arms drive 50%+ of community-contributed LeRobotDatasets** ([LeRobot ICLR 2026](../../sources/lerobot-iclr-2026-paper.md)). Cheap hardware buys ecosystem position, and ecosystem position is stickier than a spec advantage.

**Research-subsidiary** — a large incumbent funds a lab, absorbs the option value, spins out or deploys internally. [TRI](../../entities/tri.md) is the archetype: it funds [Drake](../../entities/drake.md) (model-based) *while* shipping [Large Behavior Models](../../concepts/learning/large-behavior-models.md) (learned), which is this wiki's clearest institutional evidence that the two programs are treated as complementary rather than successive — and in January 2026 it spun the LBM leadership out into [Walden Robotics](../../entities/walden-robotics.md).

> [!warning] The posture that has already failed once
> [K-Scale Labs](../../entities/k-scale-labs.md) — open-source humanoid, developer-tier — **shut down in late 2025**. The consumer/prosumer tier has the weakest evidence of any: [Zeroth M1](../../entities/zeroth-m1.md) takes pre-orders on a storefront with 404s on its own company pages and publishes **no accuracy figure for the fall-detection feature it sells for elder safety**; [Sourccey](../../entities/sourccey.md) has no published price. The one genuine exception is [NORI A3](../../entities/nori-a3.md) — priced, shipped, >$300K in six weeks — whose 4 GB [Pi 5](../../entities/raspberry-pi-5.md) cannot run inference onboard, so every unit sold creates someone-else's model-serving cost ([value chain](consumer-robotics-value-chain.md)).

---

## 4. Automotive companies that own or invest in robotics AI

The automotive industry is the single largest corporate bloc in Robot AI, and it arrived by a specific logic: carmakers already own the three things a humanoid program needs — **high-volume precision manufacturing, an actuator and sensor supply chain, and a factory floor to be the first customer.** They are simultaneously the buyers, the builders, and increasingly the owners.

The distinction that matters, and that trade coverage routinely blurs, is **equity versus purchase order.** A pilot deployment is a customer relationship; it is not ownership and confers no control. Both are listed below, separated.

### Ownership and equity

| Automaker | Robotics entity | Relationship | Detail |
|---|---|---|---|
| **Hyundai Motor Group** | [Boston Dynamics](../../entities/boston-dynamics.md) | **Wholly owned** | Took an **80% controlling stake in 2021** from SoftBank; in **July 2026 bought SoftBank's remaining ~10% for ~$325M**, valuing BD at ~$3.3B and making it a wholly owned subsidiary `[live-web]` [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-16/hyundai-to-buy-softbank-s-boston-dynamics-stake-in-robot-push), [KED Global](https://www.kedglobal.com/robotics/newsView/ked202606210001). [Atlas](../../entities/atlas.md) is slated for Hyundai Metaplant America (Georgia) from **2028** on parts sequencing, assembly by 2030; Hyundai has stated a target of **30,000 humanoids/year** for its factories by 2028 `[live-web]` [Axios](https://www.axios.com/2026/01/05/hyundai-humanoid-robots-boston-dynamics) |
| **Toyota** | [Toyota Research Institute](../../entities/tri.md) | **Wholly owned subsidiary** | Los Altos + Cambridge. Funds [Drake](../../entities/drake.md); home of the [LBM](../../concepts/learning/large-behavior-models.md) program ([TRI LBM paper](../../sources/tri-lbm-paper.md), 82 authors) |
| **Toyota** | [Walden Robotics](../../entities/walden-robotics.md) | **Anchor investor** | The TRI LBM leadership ([Tedrake](../../entities/russ-tedrake.md), Burchfiel, Feng, Gaidon, Ambrus) spun out Jan 2026; **$300M seed at $1.1B**, co-led by **Toyota Motor Corp, Toyota Invention Partners and Toyota Ventures** ([launch](../../sources/walden-robotics-launch.md)). Toyota is thus both the former parent and an anchor backer |
| **Tesla** | [Optimus](../../entities/tesla-optimus.md) | **In-house** | Vertically integrated on the FSD-derived vision/NN stack; closed development, no academic availability |
| **XPeng** | [XPENG Robotics](../../entities/xpeng-robotics.md) | **In-house subsidiary** | IRON humanoid (the **IRON-R01-1.11**, 50-dimensional action space, appears in [UniT](../../sources/unit-paper.md)). Robotics unit raised **>$900M at >$6.3B post-money** — reported as the largest single private round in China's embodied-AI sector; CEO He Xiaopeng took direct control of the unit; mass production targeted end-2026 `[live-web]` [TechCrunch](https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/) |
| **Mercedes-Benz** | Apptronik ([Apollo](../../entities/apptronik-apollo.md)) | **Investor + customer** | Participated in Apptronik's **$415M Series A (Feb 2025)** and the **$520M Series A-X (Feb 2026)** — total Series A **>$935M** at a reported **$5B** valuation — while also running Apollo in German plants `[live-web]` [CNBC](https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html), [Apptronik](https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a) |
| **BYD** | "Yao Shun Yu" programme; **Xiao Di** humanoid | **In-house** | Humanoid unveiled Aug 2026; stated plan of **20,000 units deployed internally by 2026**, commercial rollout 2028 `[live-web]` [WardsAuto](https://www.wardsauto.com/news/chinese-automakers-continue-advancements-in-humanoid-robots/799172/) |
| **Chery** | **AiMOGA** (robotics subsidiary) | **In-house subsidiary** | Mornine humanoid line; AiMOGA reported to be preparing an IPO `[live-web]` [Gasgoo](https://autonews.gasgoo.com/articles/icv/beyond-the-wheel-the-iron-men-set-out-automakers-plunge-into-robotics-area-2034975491411308544) |
| **GAC** | **GoMate** / GoMate Mini; **Huilun Technology** | **In-house subsidiary** | Dedicated robotics company established; trial and small-batch production targeted within 2026, mass production 2027 `[live-web]` [Gasgoo](https://autonews.gasgoo.com/articles/icv/beyond-the-wheel-the-iron-men-set-out-automakers-plunge-into-robotics-area-2034975491411308544) |
| **Xiaomi** | CyberOne line; in-plant robots | **In-house** (and now an automaker) | Robots already trialing inside Xiaomi's own car factories `[live-web]` [36Kr](https://eu.36kr.com/en/p/3954273153586820) |
| **Honda** | In-house humanoid/manipulation research | **In-house** | Listed in the AI Index §2.7 vendor table as *Japan / robotics platforms / general purpose / continuing humanoid and manipulation research* ([AI Index](../../sources/stanford-hai-ai-index-2026.md)) |

Beyond these, at least **ten Chinese automakers** — Chery, GAC, XPeng, BYD, Xiaomi, FAW, Dongfeng, Seres, Li Auto and Changan — are reported to be building complete robot units or to have established dedicated robotics companies `[live-web]` [TechCrunch](https://techcrunch.com/2026/08/28/chinese-automakers-are-following-teslas-bet-that-robots-are-the-next-big-profit-machine/).

Adjacent, non-automotive but vehicle-manufacturing: **John Deere** and **Ryder System** also participated in Apptronik's Series A-X `[live-web]` [Crunchbase News](https://news.crunchbase.com/venture/ai-humanoid-robot-funding-apptronik/) — the same logic (own the factory, own the fleet, buy the robot early) extending to agriculture and trucking.

### Customer, not owner

Worth separating, because these get reported as if they were investments:

| Automaker / supplier | Robot | Relationship |
|---|---|---|
| **BMW Group** | [Figure 02](../../entities/figure.md), then [Figure 03](../../entities/figure-03.md) | **Customer.** Plant Spartanburg, Hall 52, from 2026-06-30 — the *sequencing* use case ([F.03 at BMW](../../sources/figure-03-at-bmw.md)). Figure 02 logged **1,250+ runtime hours, 90,000+ parts across 30,000+ vehicles** over 11 months ([AI Index](../../sources/stanford-hai-ai-index-2026.md)). No equity stake documented here |
| **Magna** | [Atlas](../../entities/atlas.md) | **Pilot partner** — automotive supplier, announced Atlas pilots |

> [!note] Why the automotive bloc is the most informative part of this map
> These are the buyers with the clearest view of the product. An automaker running a humanoid on its own line sees the uptime, the cycle time, and the failure modes without a press release in between — and several have responded by **buying equity rather than just robots**. That is a stronger signal than any published success rate on this page, because it is a costly one.
>
> It cuts the other way too. Hyundai's Atlas timeline is **2028 for parts sequencing and 2030 for assembly** — from the company that has owned Boston Dynamics since 2021 and now owns it outright. The most committed, best-informed, most vertically integrated player in the industry is guiding to *sequencing* — the easiest factory task, the same one Figure is doing at BMW — **four years out**. Read every 2026 humanoid timeline against that.

---

## 5. Where the money is coming from

| Company | Round | Valuation | Notable backers |
|---|---|---|---|
| [Figure](../../entities/figure.md) | Series C, **>$1B** (closed 2025-09-16) | **$39B** post | [Brookfield](../../entities/brookfield.md) — which also supplies **100,000+ residential units** as a data source ([partnership](../../sources/figure-brookfield-partnership.md)) |
| Apptronik | Series A + A-X, **>$935M** | **~$5B** `[live-web]` | Google, **Mercedes-Benz**, B Capital, PEAK6, AT&T Ventures, John Deere, Qatar |
| [XPENG Robotics](../../entities/xpeng-robotics.md) | **>$900M** `[live-web]` | **>$6.3B** post | XPeng (parent) |
| [Walden Robotics](../../entities/walden-robotics.md) | **$300M** seed | **$1.1B** | **Toyota Motor Corp**, Toyota Invention Partners, Toyota Ventures, Deviation Capital |
| [Skild AI](../../entities/skild-ai.md) | Series C, **~$1.4B** `[live-web]` | **>$14B** post | **SoftBank** (lead), NVIDIA NVentures, Bezos Expeditions, **Samsung**, **LG**, **Schneider Electric**, Salesforce Ventures |

Four of these five have an **industrial strategic** as an anchor rather than a pure financial investor — Brookfield (real estate, and the data that comes with it), Mercedes-Benz (factory), Toyota (factory and former parent), and Skild's Samsung / LG / Schneider Electric (electronics manufacturing and industrial automation). The exception, XPeng, is itself the industrial strategic.

That pattern is the most reliable signal on this page. **The capital is coming disproportionately from people who own the deployment environment**, which is what you would expect in a field where the constraint is not model quality in the abstract but whether the thing works in a specific building. It is also what you would expect if the returns are expected to come from *internal cost reduction* rather than from selling robots — a materially different business than the one the consumer-facing announcements describe.

---

> [!warning] The extreme case
> **[Foundation Future Industries](../../entities/foundation-robotics.md)** reports ~$24M in government research contracts, **$100M in contracted ARR**, and a 50,000-unit-by-2027 target — against **zero published performance data**, a product page whose payload figure contradicts itself by 2×, an actuator its own company describes two incompatible ways, and a GM partnership claim that GM denied in the plainest available language (*"never had an agreement of any kind"*). It is the sharpest instance in this wiki of the gap this page is built around, and a reminder that the checks below are not academic.

## 6. How to read industry claims in this field

Five checks, each earned from a specific failure documented in this wiki.

1. **Separate announcement from shipment.** Most of the consumer tier is pre-order, deposit, or waitlist ([value chain](consumer-robotics-value-chain.md)).
2. **Separate equity from purchase order.** BMW–Figure and Mercedes–Apptronik are reported in similar language and are not the same relationship.
3. **Ask for the denominator.** Any success rate without a rollout count is uninterpretable ([success-rate audit](../platforms/vla-success-rate-audit.md)).
4. **Distinguish teleoperation from autonomy.** AgiBot's ~100 humanoids running up to 17 h/day are **teleoperated** ([AI Index](../../sources/stanford-hai-ai-index-2026.md)); much industry footage does not say which it is showing.
5. **Prefer primaries over landscape tables.** The AI Index's §2.7 vendor table described [TRI](../../entities/tri.md) as a Japanese teleoperated-logistics company for two months before correcting it to a US research lab doing diffusion policy and large behavior models ([Edition history](../../sources/stanford-hai-ai-index-2026.md#edition-history)). Aggregators are weakest exactly where this page is densest — per-company facts.

---

## Open questions

- **No revenue figures anywhere.** Not one company on this page has disclosed robotics revenue in a source this wiki holds. Valuations are priced off capability that the [12.4%](#1-the-number-the-whole-industry-is-priced-against) says is not there yet, and there is no public series that would falsify or confirm the thesis.
- **Is the Chinese automaker wave a real capability programme or a capital-markets one?** AiMOGA's reported IPO preparation and XPeng's $6.3B robotics valuation suggest at least part of the answer is financing. Unresolved with what is here.
- **Does cross-embodiment generalization actually commoditize hardware?** The entire model-layer bet depends on it. [π0/π0.6](../../entities/physical-intelligence.md) is the best evidence for; the [stable-worldmodel](../../sources/stable-worldmodel-paper.md) collapse results and the [success-rate audit](../platforms/vla-success-rate-audit.md) are the best evidence that published generalization is over-read.
- ~~**Skild AI** has no entity page~~ — **filed 2026-08-29** ([Skild AI](../../entities/skild-ai.md)) off the [S1](../../sources/skild-s1-blog.md) ingest. Still no entity pages for most of the Chinese automaker robotics units (AiMOGA, Huilun, BYD's programme), which are named here from trade press and nowhere else in the wiki.
- **What happened in the failures?** [K-Scale Labs](../../entities/k-scale-labs.md) shut down and this wiki holds no post-mortem. Failure data is systematically missing from an industry that publicizes only launches.
- **Promotion needed.** Every `[live-web]` fact here should become a real ingest before anyone quotes it in a decision. The funding figures and the Hyundai/SoftBank transaction are the highest-value candidates.
