---
title: AMI Labs
type: entity
subtype: organization
created: 2026-05-09
updated: 2026-09-07
sources: 10
tags: [ami-labs, lecun, jepa, world-model, startup]
---

> [!note] The lab is well-sourced; its *publications* are not
> **Existence and funding — corroborated.** Beyond the original [Towards AI article](../sources/towardsai-lecun-ami-labs.md), the launch has [TechCrunch coverage](https://techcrunch.com/2026/03/09/yann-lecuns-ami-labs-raises-1-03-billion-to-build-world-models/) (2026-03-09, $1.03 B) and a [Wikipedia article](https://en.wikipedia.org/wiki/Advanced_Machine_Intelligence_Labs). The earlier "single secondary source / treat as provisional" caveat is retired for these facts.
>
> **Publications — the first AMI Labs byline has now appeared.** As of **2026-07-26**, the LeCun *world-model* papers the wiki tracks (the V-JEPA / LeJEPA / stable-worldmodel line) still carry **NYU/Mila/Meta** affiliations, **not** AMI Labs. **But [WorldDP](worlddp.md) (arXiv 2606.08775, 7 Jun 2026) — a robotics paper — lists LeCun as "Courant Institute, NYU" *and* "AMI Labs".** This is the first AMI-Labs-affiliated paper found. See [Attribution correction](#attribution-correction) below.

**AMI Labs** — reported new AI research lab / company founded by [Yann LeCun](yann-lecun.md) after his reported departure from [Meta FAIR](meta-fair.md) (~November/December 2025 per the article). Research direction: world models and the JEPA program, positioned as an alternative to large language model scaling.

## Funding (reported)
- **$1.03 billion seed round**
- Named investors: Mark Cuban, Eric Schmidt, Tim Berners-Lee, Jim Breyer, Bezos Expeditions.

## Research context
The article frames AMI Labs' founding as a bet against LLM scaling ("technological dead end"), with JEPA-style world models as the alternative path.

### Attribution correction

The [Towards AI article](../sources/towardsai-lecun-ami-labs.md) attributes "three world-model papers shipped within 60 days" to LeCun's work at the lab ([V-JEPA 2.1](../sources/v-jepa-2-1-paper.md), [LeWorldModel](leworldmodel.md), and a third unnamed project). **This wiki previously repeated that framing; it does not survive checking the papers.**

| Paper | Printed affiliations | AMI Labs? |
|---|---|---|
| [V-JEPA 2.1](../sources/v-jepa-2-1-paper.md) (2026-03) | **FAIR at Meta** + Mila | ❌ |
| [LeWorldModel](../sources/leworldmodel-paper.md) (2026-03) | Mila / NYU / Samsung SAIL / Brown | ❌ |
| [stable-worldmodel](../sources/stable-worldmodel-paper.md) (2026-05-20) | Mila & UdeM / **NYU** / UFMG / Independent / LanceDB / Oxford / Brown | ❌ |
| [When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md) (2026-05-25) | Cold Spring Harbor / **NYU** / Brown | ❌ |
| **[WorldDP](../sources/worlddp-paper.md) (2026-06-07)** | NYU Tandon + **Courant NYU / AMI Labs** (LeCun) | ✅ |

Checked 2026-07-26 against the printed affiliations of each: the four *world-model-line* papers carry NYU/Mila/Meta only. **WorldDP is the exception and the update** — LeCun's byline there reads "Courant Institute of Mathematical Sciences, New York University" **and** "AMI Labs". So an AMI-Labs-affiliated paper now demonstrably exists.

Two caveats keep this modest: (1) it is a **co-authorship** with an NYU Tandon robotics group (Goswami / Krishnamurthy / Khorrami), not a paper *authored by the lab*; AMI Labs appears only as LeCun's personal affiliation tag. (2) The world-model research the press attributes to AMI Labs ([V-JEPA 2.1](../sources/v-jepa-2-1-paper.md), [LeWorldModel](leworldmodel.md)) still shows academic affiliations. So: the lab now has *a* byline, but **whether it has published substantive work under its own name remains thin** — WorldDP is a robotics collaboration, not the industrial-world-model program LeCun describes as AMI's actual mission.

**Founding vision document.** AMI Labs' research direction is, in effect, the execution of LeCun's **["A Path Towards Autonomous Machine Intelligence" (2022)](../sources/lecun2022-path-towards-ami.md)** — a six-module differentiable agent architecture built around a configurable predictive world model, hierarchical JEPA as the substrate, and intrinsic-cost-driven behavior. The "AMI" in the lab's name corresponds directly to the "Autonomous Machine Intelligence" in the paper's title. Its landing-page tagline, per the [Welch Labs Part 2 explainer](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md): **"Real intelligence does not start in language. It starts in the world."**

## Near-term plan (LeCun, per Welch Labs Part 2, May 2026)
- **1–2 years**: apply world-model planning to **complex industrial systems "that cannot be reduced to a small number of equations"** — jet engines, airplanes, chemical/power plants; a diabetes patient's blood-sugar control; coaxing a stem cell into an insulin-producing beta cell; materials / catalyst / battery design. Framed as gaining experience pushing the methodology into practice, **not** initially a revenue model. Explicitly *not* simple robot arms / humanoids / rockets (those have writable dynamical equations).
- **3–5 years**: stated ambition to become **"the main supplier of intelligent systems, whatever the application is."**

## Leadership, structure, and targets (LeCun, per MIT Technology Review, 2026-01-22)

From the [exclusive launch interview](../sources/mit-tech-review-lecun-ami-labs-interview.md), one day after the announcement:

- **Roles.** LeCun is **executive chairman** — *"I can do management, but I don't like doing it"* — and keeps his NYU post. **Alex LeBrun** is CEO: three prior AI companies (sold to Microsoft; sold to Facebook, then ran FAIR Paris engineering; founded Nabla). *"It's going to be LeCun and LeBrun."*
- **Saining Xie as chief scientist** — asked directly, not confirmed: *"Let's just say I have a lot of respect for him."*
- **Footprint.** HQ Paris; a North American office (New York implied — *"Silicon Valley is a bit of a monoculture"*); probably Asia. Positioned as *"a credible frontier AI company that is neither Chinese nor American,"* with open-source-as-platform and AI sovereignty as the pitch to investors and governments.
- **Recruiting** from OpenAI, Google DeepMind, and xAI, framed as belief-driven rather than pay-driven.
- **Data:** video, audio, *"sensor data of all kinds… from the position of a robot arm to lidar data to audio,"* plus a JEPA project on *"complex physical and clinical phenomena."*
- **Stated applications:** industrial processes with thousands of sensors (jet engine, steel mill, chemical factory); **smart glasses** that predict the wearer's next action; reliable agentic systems. Domestic robots and Level 5 driving are named as what world models *eventually unlock*, not as targets — consistent with the plan below.
- **Meta:** *"Meta might be our first client!"* Non-competing by his account: AMI on physical-world world models, Meta on generative AI and LLMs.

**The founder's own framing of the mission, the same week** ([AI House Davos](../sources/ai-house-davos-2026-lecun-embodied-ai.md), billed as *"Founder and Executive Chairman, Advanced Machine Intelligence"*): *"a new, very ambitious company with the idea that we're going to be able to solve that problem within a few years — systems that understand the physical world or any modality you throw at them, can build world models, use them to plan, build hierarchical world models."* And the scope note that makes the industrial-first plan above coherent: *"it's not just embodied AI… it's also disembodied physical AI — a manufacturing process, a turbojet engine — anything for which the data comes to you as a sequence of high-dimensional, continuous, noisy signals."*

## Related
- [Yann LeCun](yann-lecun.md) — reported founder.
- [WorldDP](worlddp.md) — the first paper carrying an AMI Labs affiliation on LeCun's byline.
- [Meta FAIR](meta-fair.md) — LeCun's prior affiliation.
- [Joint-Embedding Predictive Architecture](../concepts/world-models/jepa.md) — research direction.

## Mentioned in
- [MIT Technology Review — LeCun launch interview (2026-01-22)](../sources/mit-tech-review-lecun-ami-labs-interview.md) — **the primary for leadership, structure, data modalities, and target applications**; predates and is consistent with the Welch Labs plan.
- [Towards AI — LeCun / AMI Labs article](../sources/towardsai-lecun-ami-labs.md)
- [Welch Labs — Yann LeCun's $1B Bet Against LLMs Part 2 (video)](../sources/welchlabs-lecun-1b-bet-against-llms-part2.md) — landing-page tagline + near-term industrial plan
- [When Does LeJEPA Learn a World Model?](../sources/when-does-lejepa-learn-a-world-model-paper.md) / [stable-worldmodel](../sources/stable-worldmodel-paper.md) — the May 2026 LeCun world-model papers, both **NYU**-affiliated, checked against this page's attribution claim.
- [WorldDP paper (Goswami et al. 2026)](../sources/worlddp-paper.md) — the first AMI-Labs-affiliated LeCun byline found.
- [HAI Issue Brief — The World Model and Spatial Intelligence Era](../sources/hai-world-model-spatial-intelligence-brief.md) — AMI Labs named alongside [World Labs](world-labs.md) and Odyssey as the world-model startups facing the incumbents; the wiki's two founder-led world-model companies sit at opposite architectural poles (JEPA latent prediction vs. pixel rendering).
- [Embodied AI — AI House Davos 2026](../sources/ai-house-davos-2026-lecun-embodied-ai.md) — the founder's own mission statement, and the *"disembodied physical AI"* scope note.
