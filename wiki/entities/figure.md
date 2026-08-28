---
title: Figure
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-08-28
sources: 11
tags: [figure, humanoid, bipedal, helix, openai, bmw, vla, system-1-system-2, botq, figure-03]
status: partial
---

**Figure** — humanoid robot line from **Figure AI** (Brett Adcock, founded 2022). Generations: **Figure 01** (2023), **Figure 02** (August 2024), **[Figure 03](figure-03.md)** (October 2025). Notable for early **OpenAI partnership** (dissolved 2024) and Figure's own end-to-end VLA, **[Helix](helix.md)**, announced 2025. Industrial pilots at BMW (vehicle assembly) since early 2024; manufacturing at **[BotQ](botq.md)** reached **one robot per hour** in April 2026.

> [!note] This page is the line and the company
> Per-generation and per-system detail now lives on dedicated pages: **[Figure 03](figure-03.md)** (the current robot), **[Helix](helix.md)** (both model generations, including System 0), **[BotQ](botq.md)** (manufacturing), **[Index](figure-index.md)** (the data programme).

## Specs (Figure 02, August 2024)
- ~1.68 m tall.
- 16 DOF in hands.
- Cameras at head + body for visual reasoning.

> [!warning] Corrected 2026-08-28 — Figure 02's mass
> This page previously carried **"~60 kg"** for Figure 02. That cannot be right: [Figure 03](figure-03.md) is **61 kg** ([product page](../sources/figure-03-product-page.md)) and Figure states it has **9% less mass than Figure 02** ([announcement](../sources/figure-03-announcement.md)) — implying Figure 02 was **~67 kg**. Secondary coverage generally says 70 kg. Figure appears never to have published an official Figure 02 spec table, so no figure here is primary-sourced; the safe statement is **Figure 02 was heavier than Figure 03, by ~9%**.

> [!note] Figure 02's 28 DOF is secondary-only
> As is Figure 03's widely-repeated "40 DOF." Neither appears in any Figure primary.

## Helix (Figure's VLA)

*Summary of Helix 1; the full two-generation account including System 0 is on **[Helix](helix.md)**.*

Announced [Feb 2025](../sources/helix-blog.md). Hierarchical two-tier VLA:

- **S2 (System 2):** 7B-parameter internet-pretrained VLM @ 7–9 Hz — slow scene + language reasoning.
- **S1 (System 1):** 80M-parameter transformer visuomotor policy @ 200 Hz — fast continuous control.
- End-to-end gradient propagation between the two.

Figure-claimed firsts ([Helix blog](../sources/helix-blog.md)):
- First VLA with **high-rate continuous control of the entire humanoid upper body** (wrists, torso, head, individual fingers).
- First VLA to operate **simultaneously on two robots** on a shared long-horizon task with novel objects.
- Generalization to "thousands" of unseen household objects via natural-language prompts.
- Runs **onboard** on embedded low-power GPUs.
- One unified weight set across diverse tasks; no task-specific fine-tuning.

Training: ~500 hours teleoperated demos ("<5%" of typical VLA datasets per Figure); auto-labeled hindsight instructions via VLM.

> [!warning] Vendor source only
> All Helix figures (parameter counts, frequencies, hours of data) come from Figure's blog post and have not been independently verified. Treat as marketing-grade until replicated in a paper or third-party evaluation.

## Index — the data strategy, 2026

On **2026-08-25** Figure announced **[Index](figure-index.md)**, a crowdsourced corpus of human egocentric video collected through a consumer app that pays the public per submission ([announcement](../sources/figure-index-announcement.md)). Claimed: 264k downloads across 108 countries, 44k weekly actives, 16M+ videos, **30 minutes of video ingested per second** (43,200 h/day), $15M paid out, and >$1B committed over 12 months to *"data and compute."*

> [!note] It reverses Helix's original differentiator
> Helix was announced in Feb 2025 trained on **~500 hours** of teleoperation, explicitly marketed as *"<5% of typical VLA datasets"* — small-data efficiency as the selling point. Index ingests that volume roughly **every 17 minutes**. Figure has not retracted the earlier framing; it has simply stopped using it. The two announcements are the same company arguing opposite sides of the data question 18 months apart, and only the second one matches the field's consensus.

Two things about Index bear on how to read Figure generally:

- **It contains no robot data.** Phone video of humans, with no action labels, no proprioception, no force, and a different embodiment from Figure 03. The Index announcement never says how the human→robot gap is crossed — though [Project Go-Big](../sources/figure-project-go-big.md) (Sep 2025) is Figure's one published answer, and it covers **navigation only**. For manipulation, which is what Index is mostly for, Figure has published nothing — against [EgoScale](../concepts/learning/scaling-laws-vla.md)'s fitted scaling law on exactly that case.
- **Figure now runs a labour marketplace.** Customers can *"book a Creator"* to do chores at home or at a business, framed as the human-staffed rehearsal for *"ordering robots as a service."* The chore service and the data-collection instrument are the same product.

## Figure 03 and Helix 02, 2025–2026

Full detail on [Figure 03](figure-03.md), [Helix](helix.md) and [BotQ](botq.md). The arc in brief:

| Date | Event | The number that matters |
|---|---|---|
| 2025-07-17 | [F.03 battery](../sources/figure-f03-battery.md) | 2.3 kWh / 5 h; **78% cost cut** vs F.02; UN38.3 |
| 2025-09-17 | [Brookfield partnership](../sources/figure-brookfield-partnership.md) | **100,000+ residential units** as a data source; Brookfield also invests in the Series C |
| 2025-09-18 | [Project Go-Big](../sources/figure-project-go-big.md) | Navigation from **100% human video, no robot demos** — but **SE(2) only** |
| 2025-10-09 | [Figure 03 announced](../sources/figure-03-announcement.md) | Palm cameras + **3 g** fingertip tactile; −9% mass; designed for die-casting |
| 2026-01-27 | [Helix 02](../sources/figure-helix-02.md) | **System 0**: 10M params @ **1 kHz**, replacing **109,504 lines of C++** |
| 2026-04-29 | [Production ramp](../sources/figure-ramping-03-production.md) | **350+ units**; **1/day → 1/hour**; 80% first-pass yield |
| 2026-06-30 | [F.03 at BMW](../sources/figure-03-at-bmw.md) | Sequencing, not pick-and-place; loco-manipulation on a factory floor |
| 2026-08-25 | [Index](figure-index.md) | 16M+ videos; **43,200 h/day** of human phone video |

Two observations the individual posts don't make on their own:

- **The hardware is downstream of the model, and the factory is downstream of both.** Figure 03's palm cameras and tactile sensors exist because Helix 02 needed those modalities — Figure says so explicitly. Its die-cast structure exists because BotQ needed to stamp it. This is the cleanest instance in the wiki of **co-design running model → sensor → manufacturing process**, and it is a more defensible moat than any single spec on the robot.
- **Figure's disclosure quality is inversely proportional to how central the claim is.** The battery and manufacturing posts carry yields, certifications, test counts and cost deltas. The AI posts — the thing the company is valued on — carry **no success rate, no baseline, and no benchmark**, across three announcements and 18 months.

## Position vs other humanoids
- **AI-foundation-first strategy.** Figure's bet is that the humanoid policy stack matters more than the hardware — Helix is the differentiator.
- **Industrial pilots over consumer.** BMW + other manufacturing deployments first, consumer applications second.
- **Closed AI stack** but more visible than Tesla Optimus or Atlas — Figure publishes capability videos and partial technical claims regularly.

## Related
- Figure AI — manufacturer.
- [Atlas](atlas.md) / [Tesla Optimus](tesla-optimus.md) / [Apptronik Apollo](apptronik-apollo.md) — research-humanoid competitors.
- [VLA models](../concepts/learning/vla-models.md) — Helix is in this paradigm.
- [Index](figure-index.md) — the 2026 data programme feeding Helix.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — the method Index is the wiki's only instance of.
- [Figure 03](figure-03.md) — the current-generation robot.
- [Helix](helix.md) — the VLA, both generations.
- [BotQ](botq.md) — the manufacturing facility.
- [Brookfield](brookfield.md) — the property portfolio behind Project Go-Big's human video.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — landscape.

## Deployment data (from AI Index 2026)

Figure 02 at BMW plant (South Carolina), 2025:
- **11 months** on the line
- **1,250+ runtime hours**
- **90,000+ parts loaded** across 30,000+ vehicles

([Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md))

## Mentioned in
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md)
- [Helix (Figure AI blog)](../sources/helix-blog.md)
- [Introducing Index (Figure AI)](../sources/figure-index-announcement.md) — the crowdsourced-data programme; no results published.
- [Introducing Figure 03](../sources/figure-03-announcement.md) · [Figure 03 product page](../sources/figure-03-product-page.md) — the current robot and its only official spec table.
- [F.03 Battery Development](../sources/figure-f03-battery.md) — the most technically substantive Figure primary here.
- [Introducing Helix 02](../sources/figure-helix-02.md) — System 0 and full-body autonomy.
- [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md) — 350+ units at 1/hour.
- [F.03 Arrives at BMW](../sources/figure-03-at-bmw.md) — Figure 03's first commercial deployment.
- [Project Go-Big](../sources/figure-project-go-big.md) · [Brookfield partnership](../sources/figure-brookfield-partnership.md) — the human-video pretraining programme and the properties it runs in.

## Open questions / TBD
- **No Helix paper.** Figure has not (as of ingest date) released a Helix paper; the blog is the only primary source. Architectural details may be incomplete or marketing-shaped.
- **Still no published results, 18 months on.** The Index announcement repeats the pattern: *"the generalization results we're seeing internally are already validating this thesis, and we will be sharing more in detail on this soon."* Figure has now made two major technical announcements — Helix (Feb 2025) and Index (Aug 2026) — with **zero externally checkable numbers** between them. Everything on this page remains vendor-stated.
- ~~Figure 03 detailed specs~~ — **resolved 2026-08-28** via primaries; see [Figure 03](figure-03.md). What remains missing there: **DOF, onboard compute, and unit cost**, none of which Figure has ever published.
- Comparison numbers vs other VLAs (LIBERO, real-world success rates) — not provided in the blog.
