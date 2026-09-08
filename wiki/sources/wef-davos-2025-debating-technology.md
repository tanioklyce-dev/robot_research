---
title: "Debating Technology — World Economic Forum Annual Meeting 2025, Davos (town hall with Yann LeCun and Dava Newman)"
type: source
url: https://www.youtube.com/watch?v=MohMBV3cTbg
podcast_url: https://www.weforum.org/podcasts/agenda-dialogues/episodes/debating-technology/
author: "Yann LeCun (VP & Chief AI Scientist, Meta); Dava Newman (Director, MIT Media Lab); moderated by Ina Fried (Axios)"
venue: "World Economic Forum Annual Meeting 2025 (55th), Davos — town-hall session; published on the WEF YouTube channel and as an Agenda Dialogues podcast episode"
published: 2025-01-23
ingested: 2026-09-07
format: "video, 47:36; YouTube auto-captions (English) as transcript"
local_path: raw/2025-01-23-wef-davos-debating-technology.en.vtt
sha256: 629a176fb10f14aa6afb3eddbe4aa6d26086a1fed7fb5dc6ca119a30e09a0fc4
tags: [lecun, davos, wef, world-model, llm-critique, decade-of-robotics, consumer-robotics, open-source, ai-safety, alignment-faking, content-moderation, primary-source, video, transcript]
---

## Summary

**The primary behind the "decade of robotics" line — and it is more hedged, and more specific, than the secondary coverage made it.** A Davos town hall in January 2025, a year before AMI Labs, with LeCun still at Meta. Most of the 47 minutes is Meta content moderation, open source as sovereignty, and Dava Newman's technology-supercycle framing. The robotics content is two passages, and the second is the one that matters for this wiki: asked for a closing speed-round on audience-nominated topics, LeCun reaches **"consumer robotics"** and says *"maybe the coming decade will be the decade of robotics, **because maybe** we'll have AI systems that are sufficiently smart to understand how the real world works."* Two *maybes*, and the second one is the condition. TechCrunch's paraphrase — "the coming years could be the 'decade of robotics'" — kept the first hedge and dropped the dependency.

The session is also the origin of two numbers the wiki had been carrying from later restatements: the **3–5 year shelf life** of the LLM paradigm, stated here twice and sharpened to *"within five years nobody in their right mind would use them anymore, at least not as the central component,"* and the **10¹⁴-bytes argument** — a frontier LLM's entire text corpus equals what a four-year-old has taken in through the optic nerve — worked through on stage with the arithmetic.

> [!note] Transcript provenance
> `local_path` is the YouTube auto-caption VTT; a de-duplicated per-minute plain-text rendering sits beside it (`.txt`), with the `.info.json` and `.description`. Auto-captions garble names — *"Yan Lon," "David Newman," "Steven Pinker" rendered as "stepen… St Pinker"* — and the audience questioners are resolved below only where the name was checkable. The WEF podcast page for the same session (`podcast_url`) returns **403 to automated fetching**, so no `fetch_url` is set and the drift check does not run against this source; if YouTube regenerates the captions the VTT hash will simply stop matching on the next `--backfill`. Timestamps below are `[mm:ss]` from the video.

## Key claims

### Robotics — what was actually said

- **[07:xx–08:xx]** After arguing that video prediction is *"a completely intractable task"* for LLM-style techniques and that Meta is working on new ones which *"may take a few years before that pans out"*: when it does, systems will have *"some mental model of the world… predict the consequences of their actions and then plan a sequence of actions,"* opening the door to *"real agentic systems — everybody's talking agentic AI but nobody knows how to do it"* — *"and also to robotics. So **the coming decade may be the decade of robotics**."*
- **[05:xx–06:xx]** The cat line, in context: language is *"discrete… much simpler than understanding the real world,"* which is why AI *"can pass the bar exam or solve equations… **but we don't have robots that can do what a cat can do.** The understanding of the physical world of a cat is way superior to everything we can do with AI."*
- **[44:xx]** Speed round on the audience word cloud: *"**consumer robotics** — as I said, maybe the coming decade will be the decade of robotics, **because maybe we'll have AI systems that are sufficiently smart to understand how the real world works**."*

> [!warning] What this source does and does not license
> This is the closest LeCun comes on record to a statement about *household* robots with a timeframe attached, and it is: **a decade, conditional on a breakthrough he separately puts at 3–5 years away, said with two hedges under a slide heading he did not choose.** It is not a prediction that home robots arrive in the 2030s; it is a statement that *if* world-model AI arrives, robotics is what it unlocks. The [MIT Technology Review interview](mit-tech-review-lecun-ami-labs-interview.md) a year later says the same thing with the hedges removed and the date removed too. Read together: **the condition is stable across a year, the date never appears.**

### The paradigm claim and its arithmetic

- **[04:xx–05:xx]** *"Within the next three to five years we're going to see the emergence of a new… paradigm for AI architectures."* Four things *"essential to intelligent behavior that they really don't do very well: understanding the physical world, persistent memory, reasoning, and complex planning. LLMs really are not capable of any of this."* Bolting things on is *"a little bit of an attempt"*; *"ultimately this will have to be done in a different manner."* *"We may have to change the name of it because it's probably not going to be generative."*
- **[26:xx]** Restated to an audience question: *"the shelf life of the current paradigm — large language models — is fairly short, probably three to five years. I think within five years nobody in their right mind would use them anymore, at least not as the central component of an AI system."* The **Broca's-area analogy**: LLMs manipulate language, done by a small region that *"only popped up in the last few hundred thousand years — can't be that complicated"*; the prefrontal cortex, *"where we think… we don't know how to reproduce this."* And the conditional: *"**if** the plan that we're working on succeeds, with the timetable that we hope, within 3 to 5 years we'll have systems that are a completely different paradigm. They **may** have some level of common sense."*
- **[27:xx–28:xx]** The **10¹⁴-bytes argument**, with numbers: a frontier LLM trains on 20–30 trillion tokens × ~3 bytes ≈ 10¹⁴ bytes — *"almost all of publicly available text on the internet,"* several hundred thousand years of human reading. A four-year-old: ~1 byte/s per optic-nerve fibre × ~1M fibres per eye ≈ 2 MB/s, × 16,000 waking hours ≈ **10¹⁴ bytes**. *"Same number in four years… we're never going to get to human-level AI by just training on text. We need systems to be able to learn how the world works from sensory data."* Human-level within two years, as some claim: *"we're not going to get [there]."*

### Safety, control, and the "alignment faking" question

- **[38:xx–40:xx]** Asked about alignment faking: *"a slightly controversial opinion… **LLMs are intrinsically unsafe**, because they're not controllable. You don't have any direct way of controlling [what they say]. The only way you can do this is by training them to do it, but that training can be undone by going outside the domain where they've been trained."* Then the deflation: *"that's not particularly dangerous because they're not particularly smart either… a bit like driving assistance for cars."* On the faking itself: *"they don't have any intentions… they don't have any values… they don't have any notion of what this is at all."* And the promise: within five years, *"objective-driven"* systems whose output *"will be produced by reasoning, and the reasoning will guarantee that whatever output is produced satisfies certain guardrails… it wouldn't be possible to jailbreak them by changing the prompt, because that would be hardwired in the guardrails."*
- **[11:xx–12:xx]** On open-weights safety: Meta fine-tunes and red-teams so models are *"to first order"* not toxic, *"but there is a limit to how well that works… those systems can be jailbroken… prompt injection."* Concedes *"we say open source but we know technically those things are not really open source"* — weights and code free, usage restricted.
- **[43:xx]** Regulation: governments *"have been brainwashed to some extent into believing in the existential risk story,"* producing rules that make open-source distribution *"essentially illegal — and in my opinion that's way more dangerous than all the other potential dangers."*

### Open source as sovereignty (the through-line to AMI Labs)

- **[08:xx–09:xx]** Open-source foundation models *"are going to be dominant over proprietary systems… the substrate for the entire industry."* The smart-glasses argument: *"all of our digital diet would be mediated by AI assistants,"* so *"three or four of those… from a couple companies on the west coast of the US or China is not going to be good for cultural diversity, democracy."* — the exact argument he makes for AMI Labs a year later.
- **[35:xx–37:xx]** Diversity requires foundation models trained on all languages, cultures and value systems, fine-tuned by many; *"the same idea as a diverse press."* Likely to need **federated / distributed training** — each region or interest group with its own data centre contributing to *"a big global model… the repository of all human knowledge."*

### Meta content moderation (most of the session; not the wiki's subject)

- **[17:xx–22:xx]** Automated hate-speech takedown went from **20–25% (late 2017) to 96% (late 2022)** *"because of transformers, self-supervision"*; that *"probably went too far"* on false positives; thresholds vary by country (elections, legal regimes). Fact-checking partners *"don't scale"*; community notes with a karma system to replace them. Meta *"has never seen itself as having the legitimacy to decide what is right or wrong"*; asked governments to regulate during the first Trump administration and *"the answer was crickets… 'we have the First Amendment here, go away.'"*

### Dava Newman's positions (for contrast)

- A **technology supercycle**: AI, *"gen bio"* (generative biology — *"large nature models"*), and sensors / *"internet of all things,"* with **human-centred design** as the filter: *"if the answer to that is no… I don't think we should be doing it."*
- **The audience poll** [14:xx]: asked who feels AI is safe and secure enough to use today, *"anyone raise their hand? Well, I think there's the answer."* No hands.
- **"I think we're the threat… not my algorithms."** Watermark all generative output. Robots *"are the AI, they're the algorithm"* — the hardware/software distinction dissolves. Disagrees with LeCun on BCI: implanted brain control of prosthetics is *"the now."*

## Entities mentioned

- [Yann LeCun](../entities/yann-lecun.md) — the primary for "decade of robotics," the 3–5-year shelf life, and the 10¹⁴-bytes argument.
- [Meta FAIR](../entities/meta-fair.md) — *"which is what we're working on at Meta"*; the pre-AMI framing.
- [AMI Labs](../entities/ami-labs.md) — not yet founded; the open-source-sovereignty argument here is the one the company was later built on.
- Dava Newman (MIT Media Lab director), Ina Fried (Axios; moderator) — no entity pages; peripheral to this wiki.

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — the mental-model-to-plan argument, and *"predict videos… completely intractable"* as the motivation for latent prediction.
- [JEPA](../concepts/world-models/jepa.md) — unnamed here; *"new techniques… at Meta."*
- [AI guardrails](../concepts/safety/ai-guardrails.md) — *"intrinsically unsafe because not controllable"* vs the promised hardwired, un-jailbreakable guardrails of objective-driven systems.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — the alignment-faking exchange; existential-risk regulation as the greater danger.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the *"consumer robotics"* passage.

## Open questions

- **Audience questioners unresolved from captions:** *"Mukesh from Bangalore"*; *"moris band, light speed"* (plausibly a Lightspeed Venture Partners investor — unverified); *"MTA josi from London"*; **Martina Hirayama**, Swiss State Secretary for Education, Research and Innovation (resolved — real office-holder). Steven Pinker was in the room.
- **The five-year clock started January 2025.** The claim *"within five years nobody in their right mind would use [LLMs] as the central component"* falls due **January 2030**. Worth a dated check then; as of September 2026 the wiki's own agent thread runs on LLM orchestrators.
- **Was the 3–5-year paradigm claim repeated at Davos 2026?** ~~Fortune reports LeCun on a January 2026 Davos panel with Hassabis and Amodei~~ — **corrected 2026-09-07: he was not on that panel.** The [Hassabis–Amodei session](wef-davos-2026-the-day-after-agi.md) is now ingested (LeCun absent; Hassabis independently names world models as what robotics waits on). LeCun's own January-2026 remarks — *"completely LLM-pilled,"* *"the reason we don't have domestic robots"* — were at **AI House Davos**, a side venue — [now ingested](ai-house-davos-2026-lecun-embodied-ai.md).
- **Does the WEF podcast page carry an official transcript?** It 403s to automated fetch; if it does, it would supersede the auto-captions as `local_path`.
