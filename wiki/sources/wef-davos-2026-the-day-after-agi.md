---
title: "The Day After AGI — World Economic Forum Annual Meeting 2026, Davos (Demis Hassabis and Dario Amodei, moderated by Zanny Minton Beddoes)"
type: source
url: https://www.youtube.com/watch?v=NnVW9epLlTM
podcast_url: https://www.weforum.org/podcasts/radio-davos/episodes/ai-agi-dario-amodei-demis-hassabis/
author: "Demis Hassabis (CEO, Google DeepMind); Dario Amodei (CEO, Anthropic); moderated by Zanny Minton Beddoes (Editor-in-Chief, The Economist)"
venue: "World Economic Forum Annual Meeting 2026 (56th), Davos — panel; published on the WEF YouTube channel and as a Radio Davos podcast episode"
published: 2026-01-20
ingested: 2026-09-07
format: "video, 32:10; YouTube auto-captions (English) as transcript"
local_path: raw/2026-01-20-wef-davos-the-day-after-agi.en.vtt
sha256: 39cfeaf0149d3c73270fe39608ad7af0fa0b7aa3c52f21837cc35c2b5a246c5d
tags: [agi, timelines, hassabis, amodei, google-deepmind, anthropic, davos, wef, self-improvement, labor-displacement, export-controls, world-model, continual-learning, robotics, primary-source, video, transcript]
---

## Summary

**Two frontier-lab CEOs, one year apart on the same question, and robotics appears in both of their answers as the thing that comes *after*.** A Davos panel billed as a sequel to their Paris 2025 conversation. [Amodei](../entities/dario-amodei.md) holds to *"AI that's better than humans at everything in maybe one to two years, maybe a little longer"* and to *"half of entry-level white-collar jobs"* gone within one to five years. [Hassabis](../entities/demis-hassabis.md) holds to *"a 50% chance"* of AGI *"by the end of the decade"* — restated as *"5 to 10 years"* — and names *"one or two missing ingredients."* The disagreement, both agree, reduces to **how fast the AI-builds-AI loop closes** in coding and research.

Ingested here for two passages that neither the [Fortune coverage](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/) nor the wiki's prior framing carried. First, Hassabis puts **physical AI inside his definition of AGI** and names **hardware in the loop as a rate limiter on self-improvement** — robotics is not a downstream application in his account but a constituent, and the slow one. Second, his closing forecast for what changes by next year: *"world models, continual learning — these are the things that will need to be cracked if self-improvement doesn't deliver the goods on its own. And then I think things like **robotics may have its sort of breakout moment**."* That is the LeCun precondition ([Davos 2025](wef-davos-2025-debating-technology.md), [MIT Tech Review 2026](mit-tech-review-lecun-ami-labs-interview.md)) stated from the other camp: **world models first, robots after, no date on the robots.**

> [!warning] Correction to how this session was referenced
> The [Davos 2025 page](wef-davos-2025-debating-technology.md) filed this as *"a January 2026 Davos panel with Hassabis and Amodei"* on which LeCun appeared. **He did not.** Fortune's article combines *separate* remarks: this two-person panel, a later Google-sponsored Hassabis talk, and LeCun speaking at **AI House Davos** — a side venue, not a WEF session — where the *"completely LLM-pilled"* and *"the reason we don't have domestic robots"* lines come from. That AI House talk is the LeCun primary for January 2026 and is **not ingested**; see Open questions.

> [!note] Transcript provenance
> `local_path` is the YouTube auto-caption VTT from the official WEF upload; a per-minute plain-text rendering (`.txt`), `.info.json`, and `.description` sit beside it. Captions garble names (*"Dar Amade," "Deis," "Enthropic," "Fermy paradox"*). The WEF Radio Davos page for the same session returns 403 to automated fetching, so no `fetch_url` is set. Timestamps are `[mm:ss]`.

## Key claims

### Timelines, restated a year on

- **Amodei, on his Paris-2025 claim of Nobel-laureate-level models across many fields by 2026–27 [01:xx–02:xx]:** *"I don't think that's going to turn out to be that far off."* Mechanism: models good at coding and AI research produce the next generation — *"a loop."* *"We might be 6 to 12 months away from when the model is doing most, maybe all, of what SWEs do end to end."* Not every part speeds up — *"chips, manufacture of chips, training time"* — so *"it's easy to see how this could take a few years. It's very hard for me to see how it could take longer than that."*
- **Hassabis [03:xx–04:xx]:** *"I'm still on the same kind of timeline"* — the 50%-by-end-of-decade claim. Verifiable domains (coding, mathematics) automate first; natural science *"may have to test experimentally, and that will all take longer."* The missing capability: *"not just solving existing conjectures… but actually coming up with the question in the first place… the highest level of scientific creativity… there may be one or two missing ingredients."* Whether the self-improvement loop *"can actually close without a human in the loop"* is open.
- **The convergence [16:xx–17:xx], Amodei:** *"We might have AI that's better than humans at everything in maybe one to two years, maybe a little longer."* On the gap between them: *"I may be saying the same thing Demis is, just factored out of that difference we have about timelines, which I think ultimately comes down to **how fast you close the loop on code**."*
- **Both, when asked what changes by next year [29:xx–30:xx]:** Amodei — *"AI systems building AI systems, how that goes."* Hassabis — *"I agree on that… but also world models, continual learning. These are the things that will need to be cracked if self-improvement doesn't deliver the goods on its own. And then I think things like robotics may have its breakout moment."*

### Robotics — the two passages that matter here

- **[08:xx–09:xx] Hassabis, on closing the loop:** *"You may need AGI itself to be able to do that in some domains… where there's more messiness around them, it's not so easy to verify your answer… **I also include, by the way, for AGI, physical AI, robotics working, all of these kinds of things — and then you've got hardware in the loop that may limit how fast the self-improvement systems can work.** But I think in coding and mathematics… I can definitely see that working."* So: robotics is *in* the AGI definition, it is the *unverifiable, hardware-bound* part, and it is why the loop closes slower there.
- **[30:xx] Hassabis:** world models and continual learning as the fallback if self-improvement stalls, with robotics' *"breakout moment"* conditional on them. **No date attached to the robots** — the only dates in the session are for AGI (1–2 years vs 5–10) and for jobs.

> [!note] Three leaders, one shape
> Across [LeCun at Davos 2025](wef-davos-2025-debating-technology.md), [LeCun in January 2026](mit-tech-review-lecun-ami-labs-interview.md), and Hassabis here, robotics is named each time as **what a world-model breakthrough unlocks**, and each time the breakthrough gets a horizon and the robot does not. Amodei, who gives the most aggressive dates in the room, does not mention robots at all. The wiki's own estimate on the [assistive landscape](../syntheses/assistive/assistive-robotics-research-landscape.md) — 5–10 years for long-horizon household tasks — sits inside Hassabis's AGI window, not before it.

### Labor

- **Amodei [13:xx, 16:xx–17:xx]:** *"half of entry-level white-collar jobs"* gone in one to five years — *"as of six months ago, I would stick with that."* Concedes no labor-market impact at the time he said it; *"maybe we're starting to see just the little beginnings of it, in software and coding… I can look forward to a time where on the more junior end and then the intermediate end we actually need less and not more people"* at Anthropic. The worry: *"as this exponential keeps compounding… it will overwhelm our ability to adapt."*
- **Hassabis [14:xx–15:xx, 18:xx–19:xx]:** near-term, *"the normal evolution when a breakthrough technology arrives"* — disruption plus new, *"perhaps more meaningful"* jobs; entry-level effects begin *"this year."* Post-AGI is *"uncharted territory"*: distribution of productivity, then *"meaning and purpose."* *"Even on my timelines of 5 to 10 years away, that isn't a lot of time."* Both say **economists are not working on this enough.**
- **Moderator's counter:** US unemployment uptick is post-pandemic over-hiring, not AI, per the studies The Economist has reviewed.

### Governance, geopolitics, risk

- **Anthropic's revenue [06:xx]:** *"0 to 100 million in 2023, 100 million to a billion in 2024, and 1 billion to 10 billion in 2025."* Cited as the reason an independent lab can survive to AGI.
- **Chips [22:xx–24:xx], Amodei:** *"Not selling chips is one of the biggest things we can do to make sure that we have the time."* Against the administration's bind-them-into-US-supply-chains logic: *"Are we going to sell nuclear weapons to North Korea because that produces some profit for Boeing?"* — *"we've done a lot of more aggressive stuff toward China that is much less effective than this one measure."* The framing: *"if we can just not sell the chips, then this isn't a question of competition between the US and China. This is a question of competition between me and Demis."*
- **Pace [21:xx–23:xx]:** Hassabis — *"maybe it would be good to have a slightly slower pace than we're currently predicting, even my timelines… that would require some coordination"*; calls for *"international… minimum safety standards for deployment."* Amodei — *"I prefer Demis' timeline. I wish we had 5 to 10 years… assume I'm right and it can be done in one to two years — why can't we slow down? Because we have geopolitical adversaries building the same technology at a similar pace."*
- **Deception and doom [25:xx–28:xx]:** Amodei — Anthropic *"pioneered this idea of mechanistic interpretability"*; both *"have background in"* neuroscience; *"increasingly documented the bad behaviors of the models when they emerge"*; skeptical of *"doomerism… this is a risk that if we all work together we can address."* Hassabis — technical safety is *"a very tractable problem **if we have the time**… maybe we don't have that."* On the Fermi paradox as an argument for AI doom: *"we should be seeing paper clips coming towards us… we're past the great filter. It was probably multicellular life."*
- **Amodei's forthcoming risks essay [09:xx–13:xx]:** the counterpart to *Machines of Loving Grace*, framed on *Contact*'s question — *"how did you get through this technological adolescence without destroying yourselves?"* Named risk classes: control of systems *"smarter than any human,"* individual misuse (bioterrorism), state misuse (*"the CCP, other authoritarian governments"*), labor displacement, *"and what haven't we thought of."*

### Competitive landscape

- Moderator: a year ago *"the DeepSeek moment"* and DeepMind *"lagging OpenAI"*; now Google has *"declared code red"* — a reference to a competitor, garbled in captions.
- Hassabis: *"we've always had the deepest and broadest research bench… marshalling that all together… getting the startup mentality back"*; Gemini 3 and Gemini-app share; DeepMind as *"the engine room of Google."*
- Amodei: what Google and Anthropic share is being *"led by researchers who focus on the models… who have these hard scientific problems as a north star."* The moderator declines to ask what happens to the companies that are not.

## Entities mentioned

- [Demis Hassabis](../entities/demis-hassabis.md) · [Google DeepMind](../entities/google-deepmind.md) — AGI 50% by 2030, physical AI inside the definition, world models + continual learning as the fallback.
- [Dario Amodei](../entities/dario-amodei.md) · [Anthropic](../entities/anthropic.md) — 1–2 years, revenue curve, chips, the risks essay.
- [Yann LeCun](../entities/yann-lecun.md) — **not present**; named here only to correct the record and because Hassabis's closing restates his precondition.

## Concepts touched

- [World model](../concepts/world-models/world-model.md) — named by Hassabis as one of two things to crack if self-improvement stalls.
- [AI safety and alignment](../concepts/safety/ai-safety-alignment.md) — deployment standards, interpretability as the response to observed deception, the pace argument.
- [Mechanistic interpretability](../concepts/safety/mechanistic-interpretability.md) — Amodei's account of its origin and current use.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the wiki's household timeline, placed against these AGI windows.

## Open questions

- ~~**LeCun's AI House Davos 2026 talk is the actual January-2026 LeCun primary**~~ — **ingested 2026-09-07** as [Embodied AI — AI House Davos 2026](ai-house-davos-2026-lecun-embodied-ai.md). The 54-minute official upload and the 35-minute attendee upload turned out to be the *same* conversation (with Marc Pollefeys); the official one is filed.
- **Amodei's risks essay** — announced here as forthcoming; whether it was published, and what it says about embodiment, is unchecked.
- **The one-to-two-year clock.** *"Better than humans at everything in maybe one to two years"* was said January 2026; the wiki should check it against its own evidence in January 2027 and January 2028, alongside LeCun's January-2030 clock from [Davos 2025](wef-davos-2025-debating-technology.md).
- **"Code red"** — the captions garble which competitor declared it; not resolved from the transcript alone.
