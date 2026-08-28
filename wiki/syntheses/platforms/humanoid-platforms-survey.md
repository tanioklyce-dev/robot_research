---
title: Humanoid platforms survey
type: synthesis
created: 2026-05-08
updated: 2026-08-28
tags: [humanoids, hardware, comparison, list, bipedal, education, research, figure-03, manufacturing]
---

# Humanoid platforms survey

Companion to [Robot platforms — comparison](robot-platforms-comparison.md) focused specifically on **humanoids**. Drives 2026 industry attention disproportionate to academic ingest in this wiki — most humanoid work is closed-development (Tesla, Atlas) or vendor-published (Figure, 1X), so the academic + open-source bias of the rest of the wiki under-represents this category. This page is a **list-with-comparison** to anchor future ingests.

> [!note] Coverage caveat
> Most entity pages referenced here are stubs filed from general knowledge. Exceptions with primary sources: [Agile ONE](../../entities/agile-one.md) and [EngineAI T800](../../entities/engineai-t800.md) (added 2026-07-16), and **[Figure 03](../../entities/figure-03.md)**, which as of 2026-08-28 is backed by six Figure primaries (announcement, product page, battery, Helix 02, production ramp, BMW). Treat the remaining specs as orientation, not citation.

## At a glance

| Robot | Tier | Manufacturer | Height | Price (est.) | AI strategy |
|---|---|---|---|---|---|
| [Atlas](../../entities/atlas.md) | Research (closed) | Boston Dynamics / Hyundai | ~1.5 m | Internal-only | Proprietary BD stack |
| [Tesla Optimus](../../entities/tesla-optimus.md) | Research (closed) | Tesla | ~1.73 m | Internal; aspirational $20–30k | Vertically integrated, FSD-derived |
| **[Figure 03](../../entities/figure-03.md)** | Research (closed) → home | Figure AI | **~1.73 m** / 61 kg | Not for sale; 350+ built | **[Helix 02](../../entities/helix.md)** (in-house, 3-tier) |
| [Agile ONE](../../entities/agile-one.md) | Industrial | [Agile Robots](../../entities/agile-robots.md) (Munich) | 1.74 m | Unannounced (integrated-stack) | DeepMind partner; AgileCore |
| [EngineAI T800](../../entities/engineai-t800.md) | Affordable / heavy-duty | [EngineAI](../../entities/engineai.md) (Shenzhen) | 1.73 m | ~PM01 sibling <$15k tier | Open; combat-league testbed |
| [1X NEO](../../entities/1x-neo.md) | Research / household (closed) | 1X Technologies | ~1.65 m | Pre-orders ~$20k+ | OpenAI-aligned FM |
| [Apptronik Apollo](../../entities/apptronik-apollo.md) | Research / industrial | Apptronik | ~1.73 m | Industrial pilots | NVIDIA-aligned ([GR00T](../../entities/nvidia-groot.md)) |
| [Digit](../../entities/digit.md) | Industrial (deployed) | Agility Robotics | ~1.75 m | Pilot pricing | Narrow-task BC |
| [Unitree H1](../../entities/unitree-h1.md) | Affordable research | Unitree Robotics | ~1.8 m | ~$90k starter | Open SDK, user-supplied AI |
| [Unitree G1](../../entities/unitree-g1.md) | Affordable research / educational | Unitree Robotics | ~1.32 m | ~$16k starter | Open SDK, user-supplied AI |
| [NAO V6](../../entities/nao.md) | Educational | SoftBank / Aldebaran | ~58 cm | ~$8–15k | Choregraphe + Python/C++ |
| [TonyPi / TonyPi Pro](../../entities/tonypi.md) | Educational (hobby) | Hiwonder | small | $300–700 | Pre-loaded demos |

## By tier

### Closed-development research humanoids (Atlas, Optimus, Figure 03, 1X)
The **flagship-capability tier** — Atlas (parkour, dexterous manipulation), Tesla Optimus (vertical FSD-derived stack), [Figure 03](../../entities/figure-03.md) ([Helix 02](../../entities/helix.md)), 1X NEO (household OpenAI-aligned). All four are characterized by:

- **Vendor-only access.** No academic units sold; capability claims are vendor-published.
- **Industrial / commercial pilots first.** BMW (Figure), Mercedes-Benz (Apptronik), Hyundai factory (Atlas), Tesla factory (Optimus). Consumer comes later.
- **AI strategy varies wildly.** Tesla = vertical, Figure = in-house Helix VLA, 1X = OpenAI-aligned, Apptronik = NVIDIA GR00T partner.

**Figure 03 is now the best-documented member of this tier** — not because Figure publishes results (it publishes none) but because it publishes *manufacturing*. See [Figure 03: the one closed humanoid with a paper trail](#figure-03-the-one-closed-humanoid-with-a-paper-trail) below.

### Industrial-deployed humanoids (Digit)
**[Digit](../../entities/digit.md)** is the outlier — Agility Robotics has Digit in **active commercial deployment at GXO Logistics and Amazon trials**, not just pilots. Narrow-task scope (warehouse package handling) is the price for getting to deployment first.

### Affordable research humanoids (Unitree H1, G1)
The **price-floor tier**. [H1](../../entities/unitree-h1.md) at ~$90k and [G1](../../entities/unitree-g1.md) at ~$16k are the only humanoids cheap enough for individual research labs to acquire without specialized funding. Open SDKs, user-supplied AI. Rapid 2024–2026 academic adoption for locomotion / RL papers.

### Educational humanoids (NAO, TonyPi, Pepper, Robotis OP3)
The **pedagogy tier**. [NAO](../../entities/nao.md) is the canonical platform since 2008. [TonyPi](../../entities/tonypi.md) occupies a much-cheaper-still hobbyist / classroom kit niche from [Hiwonder](../../entities/hiwonder.md) (same vendor as [ROSOrin Pro](../../entities/rosorin-pro.md)). Robotis OP3 / DARwIn-MINI (no entity pages here) and Pepper (no entity page) round out the niche.

## Figure 03: the one closed humanoid with a paper trail

*Added 2026-08-28 from six Figure primaries. Full detail: [Figure 03](../../entities/figure-03.md), [Helix](../../entities/helix.md), [BotQ](../../entities/botq.md).*

Figure 03 (announced 2025-10-09) matters to this survey for a reason that has nothing to do with its specs. Every other robot in the closed tier is a **capability** story told through videos. Figure 03 is the first one that is also a **manufacturing** story told through numbers — and manufacturing numbers are the ones that determine whether a humanoid tier exists at all in five years.

### Official specs

Figure publishes exactly six fields, on its [product page](../../sources/figure-03-product-page.md): **5'8" (~173 cm) · 61 kg · 20 kg payload · 5 h runtime · 1.2 m/s · electric.** Plus **2.3 kWh** battery from the [battery post](../../sources/figure-f03-battery.md). That is all. **No DOF. No onboard compute. No price.**

> [!warning] Three widely-circulated Figure 03 numbers have no primary behind them
> **168 cm** (Figure says 5'8" = 172.7 cm; 168 cm was *Figure 02's* number, apparently carried forward by copy-paste), **40 DOF** (absent from every Figure primary), and **4-hour runtime** (both Figure primaries say 5 h). Comparison tables across the web repeat all three. This is exactly the failure mode CLAUDE.md's primary-source rule exists for: a dozen sites agreeing is one source when they are all paraphrasing the same page.

> [!warning] Contradiction resolved — Figure 02's mass
> This wiki carried "~60 kg" for Figure 02. Figure 03 is 61 kg and **9% lighter than Figure 02**, implying Figure 02 was **~67 kg**. Corrected on [Figure](../../entities/figure.md).

### What actually changed from 02 → 03

Not strength, not height, not DOF. **Sensing and cost.**

| | Figure 02 | Figure 03 |
|---|---|---|
| Cameras | head + body RGB | **2× frame rate, ¼ latency, 60% wider FOV**, expanded DoF |
| In-hand sensing | none | **palm camera per hand** + **fingertip tactile at 3 g** |
| Fleet data | — | **10 Gbps mmWave offload** |
| Charging | wired | **2 kW inductive, coils in the feet** |
| Exterior | hard machined parts | **multi-density foam + washable soft textiles** |
| Primary process | **CNC machining** | **die-casting, injection moulding, stamping** |
| Battery | ~2.25 kWh (secondary) | **2.3 kWh**, structural, UN38.3, **−78% cost** |
| Mass | ~67 kg (implied) | **61 kg** |

### The three numbers worth carrying out of this

1. **1 robot per hour.** [BotQ](../../entities/botq.md) went from 1/day to 1/hour in under 120 days — 24× — and has delivered **350+ units** ([production ramp](../../sources/figure-ramping-03-production.md)). Nameplate is 12,000/year (~1.37/hour at 24/7), so Figure is now within its own order of magnitude. **No other humanoid maker in this survey has publicly claimed a comparable rate**, Unitree included.
2. **109,504 lines of C++, replaced.** [Helix 02](../../sources/figure-helix-02.md)'s **System 0** — a 10M-parameter policy at **1 kHz**, trained on 1,000+ h of retargeted human motion across 200k parallel sim environments — displaced Figure's hand-engineered whole-body controller outright. Algorithmically this is the standard motion-tracking recipe this wiki documents in [SONIC](../../sources/sonic-paper.md) and [BumbleBee](../../sources/bumblebee-experts-to-generalist-wbc.md); what is new is that it ships under a production VLA, over OTA, to a 350-unit fleet.
3. **80% first-pass yield.** Volunteered, not extracted. One robot in five fails end-of-line. Alongside burn-in testing and formal recall-campaign processes, this is the most credible signal in the tier that the fleet is real, precisely because it is unflattering.

### Where it sits against the tier

- **vs [1X NEO](../../entities/1x-neo.md)** — the closest competitor by intent. Both are household-aimed, closed-stack, aspirational-consumer. NEO takes pre-orders at ~$20k; Figure 03 is **not for sale at any price** while claiming home tasks "all autonomously" in the present tense on its product page. Neither has published a success rate.
- **vs [Tesla Optimus](../../entities/tesla-optimus.md)** — both vertically integrated; Tesla has the manufacturing pedigree, Figure has published manufacturing *numbers*. Figure's are checkable in kind; Tesla's are not stated.
- **vs [Apptronik Apollo](../../entities/apptronik-apollo.md) / [GR00T](../../entities/nvidia-groot.md)** — the open-ecosystem counterpoint. GR00T publishes benchmarks; Helix publishes videos. If you want a humanoid stack you can *evaluate*, that asymmetry decides it.
- **vs [Unitree G1](../../entities/unitree-g1.md)** — different universe. G1 is ~$16k and you can buy one; Figure 03 is a fleet you cannot access. For anyone in this wiki's actual position, G1 is a platform and Figure 03 is a **reference design to read**.

### What Figure 03 is useful *for*, here

Not as a purchase — it isn't one. As the tier's clearest worked example of three things:

- **Model → sensor → process co-design.** Palm cameras and 3 g tactile exist because Helix 02 needed those modalities; Figure says so outright. The die-cast structure exists because BotQ needed to stamp it. Requirements flow **model → hardware → factory**, which is the inverse of how most robotics programmes run.
- **Safety certification being *created*, not cited.** Figure worked with an OSHA NRTL to define a **UL 2271** humanoid-battery standard because none existed ([battery post](../../sources/figure-f03-battery.md)). Whoever gets there first shapes what "safe" means for every humanoid after. Worth watching from an [assistive-robotics](../../concepts/robotics/assistive-robotics.md) standpoint, where in-home certification is the gating problem.
- **A ~460 W whole-robot power budget** (2.3 kWh / 5 h) that must also cover onboard VLA inference — a constraint Figure never addresses and that anyone speccing onboard compute should hold next to the [Jetson module ladder](jetson-module-ladder-power-performance.md).

> [!warning] The asymmetry to keep in mind
> Figure's **hardware and manufacturing** disclosures are specific, unflattering where reality is unflattering, and externally checkable in kind. Its **AI** disclosures — the thing the company is valued at $39B on — contain **no success rate, no baseline, and no benchmark**, across Helix (Feb 2025), Helix 02 (Jan 2026) and [Index](../../entities/figure-index.md) (Aug 2026). Believe the factory; suspend judgement on the brain.

## Strategic patterns visible at this layer

### Three AI-strategy archetypes
1. **Vertical integration** (Tesla Optimus, Figure with Helix). Vendor controls hardware + AI; less dependence on outside infrastructure.
2. **Closed AI on partner hardware** (Boston Dynamics Atlas with proprietary stack, but increasingly NVIDIA-curious). Hardware-first lineage, AI follows.
3. **Open hardware + ecosystem AI** (Unitree H1/G1, Apptronik Apollo). Vendor sells hardware; AI ecosystem is open ([GR00T](../../entities/nvidia-groot.md), academic stacks, in-house dev).

### A fourth axis, visible only since 2026: design-for-manufacture
Added 2026-08-28. The archetypes above sort platforms by *AI strategy*; [Figure 03](../../entities/figure-03.md) makes clear there is an orthogonal axis that sorts them by **whether the robot was designed around a production process at all**. Figure 02 → 03 is an explicit move from CNC machining to die-casting/stamping/injection moulding, and [BotQ](../../entities/botq.md) is the first humanoid facility in this survey to publish yields, cycle time and unit counts. Unitree has volume and price but publishes no process detail; everyone else in the closed tier builds prototypes. **On current public evidence this is the widest moat in the humanoid tier, and it is not an AI moat.**

### Geographic clustering
- **US / North America**: Atlas (US, Hyundai-owned), Tesla, Figure, Apptronik, Agility, 1X (Norway-US dual).
- **China**: Unitree (H1, G1), [AGIBOT](../../entities/agibot.md) (humanoid line not separately filed), Fourier (GR-1, GR-2), LimX (CL-2), Booster Robotics (T1) — collectively a **rapidly growing affordable-humanoid cluster**.
- **Europe**: Aldebaran/SoftBank NAO (France), PAL Robotics (Spain), Engineered Arts (UK), **[Agile Robots](../../entities/agile-robots.md) (Germany)** — the DLR-spinout [Agile ONE](../../entities/agile-one.md) is the first serious *European industrial* humanoid entrant, betting on integration-into-a-stack rather than a standalone unit.
- **Japan**: AIST HRP series, Toyota T-HR3, Kawasaki Kaleido — historically strong but lower visibility in 2024–2026 vs the US-China dynamic.

### Price stratification (2026)
- **Internal-only tier**: Atlas, Optimus, **Figure 03** (vendor doesn't sell — Figure has built 350+ and priced none).
- **$50k–$100k tier**: H1, Apollo (limited availability).
- **$15k–$25k tier**: G1, NEO Beta.
- **$8k–$15k tier**: NAO V6.
- **<$1k tier**: TonyPi (educational kit).

There is **no $25k–$50k tier**. The market is bifurcating into "expensive enterprise" vs "cheap research / educational" with little middle.

> [!note] The internal-only tier is no longer synonymous with "prototype"
> Added 2026-08-28. Figure 03 sits in the unpriced tier while being manufactured at **one unit per hour** with an 80% first-pass yield. Unpriced now means *not yet sold*, not *not yet buildable* — a distinction that did not need making when this section was written.

## Why this is underrepresented in this wiki

The ingested literature skews toward **academic JEPA / VLA / world-model work** that uses tabletop arms (Franka) or wheeled mobile manipulators (Stretch), not humanoids. Humanoid VLAs ([GR00T](../../entities/nvidia-groot.md), Figure Helix) are mentioned but their **hardware-platform deployment papers** are not yet in the wiki. As humanoid VLA papers ingest (likely 2026 H2), this synthesis should grow into individual entity pages becoming substantive rather than stubs.

> [!note] Progress on that, 2026-08-28
> [Figure 03](../../entities/figure-03.md), [Helix](../../entities/helix.md) and [BotQ](../../entities/botq.md) are now substantive pages backed by six primaries — the first closed-tier platform here to stop being a stub. It also sharpens *why* this category resists ingest: there are no papers to ingest. The closed tier communicates through blog posts, and the useful ones turn out to be about **batteries and factories**, not models.

## What's still missing from this wiki

- **AGIBOT humanoid hardware** — [company](../../entities/agibot.md) is filed but the specific humanoid platforms (A2, X1, X2) aren't separate entities yet.
- **Fourier GR-1 / GR-2** — Chinese affordable research humanoid.
- **LimX CL-2 / CL-3, Booster T1** — affordable Chinese humanoids. ([EngineAI](../../entities/engineai.md) + its [T800](../../entities/engineai-t800.md) are now filed; SA01/SE01/PM01-front-flip still unfiled.)
- **PAL Robotics TIAGo / TALOS** — European research-tier.
- **Pepper** — SoftBank social-robot sibling of NAO.
- **Robotis OP3, DARwIn-MINI** — RoboCup-tier educational humanoids.
- **Sanctuary AI Phoenix** — Canadian humanoid with Carbon AI control.
- **Kawasaki Kaleido, Toyota T-HR3, HRP-5P** — Japanese research humanoids.

## Sources used in this synthesis

- Per-platform entity pages: [Atlas](../../entities/atlas.md), [Tesla Optimus](../../entities/tesla-optimus.md), [Figure](../../entities/figure.md) / [Figure 03](../../entities/figure-03.md) / [Helix](../../entities/helix.md) / [BotQ](../../entities/botq.md), [1X NEO](../../entities/1x-neo.md), [Apptronik Apollo](../../entities/apptronik-apollo.md), [Digit](../../entities/digit.md), [Unitree H1](../../entities/unitree-h1.md), [Unitree G1](../../entities/unitree-g1.md), [NAO](../../entities/nao.md), [TonyPi](../../entities/tonypi.md).
- Adjacent ingested context: [GR00T](../../entities/nvidia-groot.md) (NVIDIA's VLA targeting humanoids), [AGIBOT](../../entities/agibot.md) (Chinese embodied-AI company with humanoid line), [substrate-convergence synthesis](../simulators/newton-openusd-substrate-convergence.md) (notes on closed industrial stacks).
- **Figure primaries (added 2026-08-28):** [Introducing Figure 03](../../sources/figure-03-announcement.md) · [Figure 03 product page](../../sources/figure-03-product-page.md) · [F.03 Battery Development](../../sources/figure-f03-battery.md) · [Introducing Helix 02](../../sources/figure-helix-02.md) · [Ramping Figure 03 Production](../../sources/figure-ramping-03-production.md) · [F.03 Arrives at BMW](../../sources/figure-03-at-bmw.md).

## Related

- [Robot platforms — comparison](robot-platforms-comparison.md) — companion synthesis covering non-humanoid robots in the wiki.
- [index.md](../../index.md) — Robot platforms section.
