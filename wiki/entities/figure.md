---
title: Figure
type: entity
subtype: robot
created: 2026-05-08
updated: 2026-08-27
sources: 4
tags: [figure, humanoid, bipedal, helix, openai, bmw, vla, system-1-system-2]
status: partial
---

**Figure** — humanoid robot line from **Figure AI** (Brett Adcock, founded 2022). Generations: **Figure 01** (2023), **Figure 02** (August 2024), **Figure 03** (2025). Notable for early **OpenAI partnership** (dissolved 2024) and Figure's own end-to-end VLA, **Helix**, announced 2025. Industrial pilots at BMW (vehicle assembly) since early 2024.

## Specs (Figure 02, August 2024)
- ~1.68 m tall, ~60 kg.
- 16 DOF in hands.
- Cameras at head + body for visual reasoning.

## Helix (Figure's VLA)

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

- **It contains no robot data.** Phone video of humans, with no action labels, no proprioception, no force, and a different embodiment from Figure 03. The announcement never says how the human→robot gap is crossed — a conspicuous omission given [EgoScale](../concepts/learning/scaling-laws-vla.md) published a recipe and a fitted scaling law for exactly this.
- **Figure now runs a labour marketplace.** Customers can *"book a Creator"* to do chores at home or at a business, framed as the human-staffed rehearsal for *"ordering robots as a service."* The chore service and the data-collection instrument are the same product.

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

## Open questions / TBD
- **No Helix paper.** Figure has not (as of ingest date) released a Helix paper; the blog is the only primary source. Architectural details may be incomplete or marketing-shaped.
- **Still no published results, 18 months on.** The Index announcement repeats the pattern: *"the generalization results we're seeing internally are already validating this thesis, and we will be sharing more in detail on this soon."* Figure has now made two major technical announcements — Helix (Feb 2025) and Index (Aug 2026) — with **zero externally checkable numbers** between them. Everything on this page remains vendor-stated.
- Figure 03 detailed specs — evolved from 02 but not exhaustively documented publicly.
- Comparison numbers vs other VLAs (LIBERO, real-world success rates) — not provided in the blog.
