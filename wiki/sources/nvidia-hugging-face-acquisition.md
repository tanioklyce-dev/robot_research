---
title: "NVIDIA to acquire Hugging Face — $12.93B (Sept 2026)"
type: source
url: https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/
fetch_url: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm
local_path: raw/2026-09-03-nvidia-to-acquire-hugging-face.md
sha256: 2d4e9e2d886c18b19f3b6cd8f5f2e8d48e07e73837595036935ab48409745a08
author: "Jensen Huang (NVIDIA newsroom post); NVIDIA Corporation (SEC Form 8-K)"
published: 2026-09-03
venue: "Two primaries: NVIDIA newsroom blog (2026-09-03, by Jensen Huang) and **SEC Form 8-K**, accession 0001045810-26-000078, Items 8.01 and 9.01, reporting a definitive agreement dated 2026-09-02"
format: corporate announcement + SEC filing
tags: [nvidia, hugging-face, lerobot, acquisition, open-weights, m-and-a, vertical-integration, smolvla, so-101, regulatory, multi-accelerator]
ingested: 2026-09-07
---

## Summary

**NVIDIA is acquiring Hugging Face for $12,930,300,000.** Definitive agreement **2026-09-02**, announced **2026-09-03**, expected to close in the **first half of 2027** subject to customary closing conditions including **regulatory approvals**. Structure per the 8-K: approximately **$11.9 B to Hugging Face stockholders**, plus **up to ~$1.0 B in equity-based retention** for employees joining NVIDIA.

This wiki is not a finance wiki, and this is here for one reason: **Hugging Face maintains [LeRobot](../entities/lerobot.md)** — the de-facto software stack for the low-cost manipulator ecosystem this wiki tracks most closely (SO-ARM100/101, LeKiwi, [XLeRobot](../entities/xlerobot.md), Koch) — plus [SmolVLA](../entities/smolvla.md) and the Hub that hosts nearly every open VLA weight referenced here. The acquirer already sells the [Jetson](../entities/jetson-thor.md) hardware those robots run on and the [Halos](../entities/nvidia-halos.md) safety stack above them.

> [!note] Sourcing
> Read from **both primaries**, not from coverage. The blog was fetched directly. **sec.gov returns 403 to scripted fetches**, so the 8-K was read through a fetch tool rather than captured to `raw/`; its terms are transcribed here and in the `raw/` header, and the accession number is recorded so it can be re-checked. Earlier secondary reports (TechCrunch, CNBC, Bloomberg, late August) described a deal as "close" before the agreement existed — see the date note below.

## The terms, as filed

| | |
|---|---|
| **Total consideration** | **$12,930,300,000** (Huang states the figure exactly) |
| **To stockholders** | ~**$11.9 B** |
| **Employee retention** | up to ~**$1.0 B**, equity-based, for HF employees joining NVIDIA |
| **Definitive agreement** | **2026-09-02** |
| **Announced** | 2026-09-03 |
| **Expected close** | **H1 2027**, subject to customary conditions incl. **regulatory approvals** |
| **Termination fee** | **none stated in the filing** |
| **8-K items** | 8.01 (Other Events) and 9.01 |
| **Brand** | retained — *"their same iconic 🤗 brand"* |

**Hugging Face scale, as NVIDIA states it**: more than **18 million** developers, researchers and creators; **3 million+ models**, **500,000 datasets**, **1 million applications**; **200,000+ companies** using the platform.

**And NVIDIA's existing position in it**, which is the fact that makes this less of a discontinuity than the headline suggests: *"NVIDIA is the largest contributor of open models and data to Hugging Face"* — **500+ models and 250+ open datasets** released there.

> [!note] Hugging Face approached NVIDIA
> *"I am honored that **Clem came to me** as he considered the next chapter of Hugging Face and believed NVIDIA would be a great home for the company."* Worth recording because it changes the shape of the story from capture to sale, and because it is the acquirer's account of it — the only one available in a primary.

## The commitments, and where they live

Four, stated in the blog:

1. *"Hugging Face will remain an **open platform for the entire AI ecosystem**. Developers will choose the models they want, the frameworks they want, the clouds and inference service providers they want and the computing platforms they want."*
2. *"**NVIDIA compute will not be required to build on or deploy through Hugging Face.**"*
3. *"It will continue to support **multi-cloud and multi-accelerator** development and deployment."*
4. Continued support for *"open source and open weight models from across the ecosystem, from every model builder."*

The 8-K carries the same undertaking in the filing itself — to keep the platform open *"consistent with Hugging Face's existing practices,"* permitting upload and download of models and datasets of the user's choosing, and **"to support other silicon vendors."**

> [!warning] Specific, public, and not demonstrably binding
> That these commitments appear in an **SEC filing** rather than only a blog post is worth more than nothing — it is a statement to the market with liability attached to being false. But it appears under **Item 8.01, "Other Events,"** which is a *voluntary* disclosure, not a contractual term the public can inspect and not a regulatory condition. **No merger agreement text, no covenant, no term sheet is public.**
>
> So the accurate reading is: *NVIDIA has publicly and specifically committed to multi-accelerator neutrality, and the enforcement mechanism is reputational and — if regulators choose to make it one — remedial.* The wiki should hold the commitment and the absence of a mechanism together, and re-check both at close.

## Why it matters here, concretely

**The wiki's own stack sits inside the acquisition.** [LeRobot](../entities/lerobot.md) is Hugging Face's. So is [SmolVLA](../entities/smolvla.md). The Hub hosts the weights behind most of the [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) and the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md). The [SO-101 / XLeRobot](../entities/xlerobot.md) line is LeRobot-native.

**And the acquirer already owns everything under and around it.** Drawing the stack from this wiki's own entity pages:

| Layer | NVIDIA holding |
|---|---|
| Silicon | [Jetson Thor / IGX](../entities/jetson-thor.md) |
| Certified safety | [Halos](../entities/nvidia-halos.md), plus the ANAB-accredited inspection lab |
| Simulation | [Isaac Sim](../entities/nvidia-isaac-sim.md) / [Isaac Lab](../entities/nvidia-isaac-lab.md), Omniverse, Newton (co-developed) |
| World models | [Cosmos](../entities/nvidia-cosmos.md) — **and Cosmos-Predict2 is [mimic-video](mimic-video-paper.md)'s backbone** |
| Robot foundation models | [GR00T](../entities/nvidia-groot.md) |
| AV reasoning models | [Alpamayo](../entities/alpamayo.md) |
| **Model distribution** | **Hugging Face Hub, LeRobot, SmolVLA** ← this transaction |

That is transistor to model registry, and the last row was the one layer NVIDIA did not hold. **This is the wiki's clearest instance of vertical integration across a stack it has been documenting piece by piece for months**, and none of the individual pages sees it.

> [!note] Offer
> A synthesis page mapping this stack — what NVIDIA owns at each layer, what remains genuinely independent, and which of this wiki's comparisons (Hailo, AMD, Apple Silicon, the open-VLA alternatives) are the load-bearing checks on the neutrality commitment — is a page's worth of work and is **not** filed. Worth doing if wanted.

**The sharpest concrete test the wiki already has** is [Hailo NPU vs Jetson for XLeRobot](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md): a comparison of a competitor's accelerator for exactly the robots whose software stack NVIDIA is buying. *"Support other silicon vendors"* either keeps that comparison meaningful or it does not, and it is checkable rather than rhetorical.

> [!note] It closes a loop from three ingests ago
> Huang references *"an open letter on the importance of open weights to the AI economy"* that he coauthored. That is the letter Peter Seeberg raised on [Industrial AI Podcast #352](industrial-ai-podcast-nvidia-safety-strategy.md) — *"why open models matter… open models strengthen safety, cyber security, they accelerate innovation and diffusion, and enable sovereignty"* — and Robert Weber's reply on that episode was to connect it to this acquisition. The hosts read the sequence correctly, a week before the wiki did.

## Two things the hosts got right and one they got wrong

The same podcast, recorded within a day of the announcement, raised the concentration question directly: *"how strong will the world allow NVIDIA to become? Is there an FTC kind of organization that at some point in time is going to say, well, you can't be everything?"* That question now has a docket: **close is conditioned on regulatory approvals, expected H1 2027**, which is a roughly nine-month review window. **Watch item, not a prediction.**

They also read the strategic logic correctly — Alexander Pavlenko's line, quoted on the episode, that the companies building *the best infrastructure to operate robots* are the ones that come out ahead, with the acquisition as the software half of that.

And the correction, recorded when that episode was ingested: the host's *"one week ago NVIDIA finally announced to buy Hugging Face"* referred to **late-August press reports that a deal was close** (TechCrunch 2026-08-26, CNBC 2026-08-27). The **definitive agreement is 2026-09-02** — the same day that episode published. Secondary-source date drift, of exactly the kind the wiki's primary-source rule exists for.

## Entities mentioned

- [Hugging Face](../entities/hugging-face.md) — the target; page updated.
- [NVIDIA](../entities/nvidia.md) — the acquirer; page updated.
- [LeRobot](../entities/lerobot.md) · [SmolVLA](../entities/smolvla.md) — the robotics assets that come with it.
- [Jetson Thor](../entities/jetson-thor.md) · [NVIDIA Halos](../entities/nvidia-halos.md) · [Cosmos](../entities/nvidia-cosmos.md) · [GR00T](../entities/nvidia-groot.md) · [Alpamayo](../entities/alpamayo.md) · [Isaac Sim](../entities/nvidia-isaac-sim.md) — the rest of the stack.
- **Clément Delangue, Julien Chaumond, Thomas Wolf** — HF founders, named in the post; no pages.

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — the Hub is where nearly every open VLA weight this wiki cites is distributed.
- [Crowdsourced robot training data](../concepts/learning/crowdsourced-robot-training-data.md) — LeRobot datasets live on the Hub.
- [Open-source robot AI projects](../syntheses/platforms/open-source-robot-ai-projects.md) · [VLA deployability landscape](../syntheses/platforms/vla-deployability-landscape.md) — the comparisons most exposed to a change in platform neutrality.

## Open questions

- **Does multi-accelerator support hold in practice?** The most checkable commitment, and [Hailo vs Jetson on XLeRobot](../syntheses/platforms/hailo-npu-vs-jetson-xlerobot.md) is the wiki's own instrument for checking it. Re-run that comparison after close.
- **What happens to LeRobot's governance?** It is an open-source project with an outside contributor community, now inside a hardware vendor with a competing robot-foundation-model line ([GR00T](../entities/nvidia-groot.md)). The blog says nothing about LeRobot specifically — **not one word about robotics anywhere in it**, which is itself notable given what the wiki cares about here.
- **Does the review impose conditions?** H1 2027, regulatory approvals required, no termination fee disclosed. Whether neutrality becomes a *remedy* rather than a *promise* is the difference between the commitment being binding and being reputational.
- **Is there a competing distribution layer if it stops being neutral?** The wiki has no page on alternatives to the Hub, and until now never needed one.
