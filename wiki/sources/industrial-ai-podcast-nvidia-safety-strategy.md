---
title: "Industrial AI Podcast #352 — NVIDIA's safety strategy (Riccardo Mariani)"
type: source
url: https://kipodcast.podigee.io/352-when-safety-meets-ai-making-friends-not-foes
fetch_url: https://www.youtube.com/watch?v=4wZ0HTF1lFc
local_path: raw/2026-09-02-industrial-ai-podcast-352-nvidia-safety-strategy-transcript.txt
sha256: ab8818fbcd63d18435a7759352963b35530b2533fe08141c9dc4bceb3c1a8a55
author: "Robert Weber and Peter Seeberg (hosts); Riccardo Mariani, NVIDIA (guest)"
published: 2026-09-02
venue: "Industrial AI Podcast, episode 352, 52:10 (also on Spotify and YouTube; transcript from YouTube en-orig auto-captions)"
format: podcast interview + news segment (auto-caption transcript, ~8,250 words)
tags: [nvidia, halos, functional-safety, riccardo-mariani, iso-iec-tr-5469, iso-iec-ts-22440, iec-61508, iso-13849, certification, igx, outside-in-safety, alpamayo, industrial-ai, simulation]
ingested: 2026-09-07
---

## Summary

**The person behind NVIDIA Halos, in his own words** — and the wiki's first source on the [Halos](../entities/nvidia-halos.md) programme that is not NVIDIA marketing copy. [Riccardo Mariani](../entities/riccardo-mariani.md) leads NVIDIA's safety initiative *and* convenes the ISO/IEC working group writing the standard that AI functional safety will be certified against, which makes this simultaneously a vendor interview and a standards-body status report. The hosts push back twice, usefully.

The thesis is a business argument before it is a technical one: **safety has been treated as a cost of compliance, and NVIDIA is betting it is a value driver** — because the autonomous systems people actually want require AI *and* require safety, so making the two compatible is what unlocks the market rather than what taxes it. *"We want to get safety and AI good friends."*

Most of the architecture here **corroborates** what the wiki already has from NVIDIA's own [product page](nvidia-halos-robotics.md) and [developer blog](nvidia-halos-robotics-blog.md). What is new is the standards layer, the certification mechanics stated by the person doing them, one candid concession, and a prediction about what certification bodies will have to become.

> [!note] Transcript provenance
> Read from **YouTube auto-captions**, and they garble every proper noun — the hosts become "Rod Vieber" and "Peter Seabourg," the guest "Ricardo Marani," Alpamayo "alpayo," Schaeffler "Sheffller," ISO/IEC TR 5469 "ISIC 5469." Names and standard numbers here were reconciled against the episode's own show notes and against primary sources; two garbled items are flagged as unresolved below. The annotated transcript in `raw/` carries the correction key.

## The interview: what it adds beyond NVIDIA's own material

**The framing NVIDIA is arguing against.** *"In a traditional safety, AI has been seen as a bad guy for safety due to the non-deterministic and non-transparent nature."* The counter-claim is that everything that moves becomes autonomous, human–machine collaboration becomes a must-have, and therefore the pairing has to be made to work rather than avoided.

**"Egocentric" vs "outside-in."** Mariani's terms for the split the wiki records as Inside-Out / Outside-In. Egocentric = sensors on the machine reasoning about its own envelope; outside-in = infrastructure sensors supplying **contextual awareness** the machine cannot have.

His worked example is worth keeping, because it is a *safety-degradation* pattern rather than a safety-addition one: an autonomous forklift ([KION](../entities/nvidia-halos.md) is named as the partner) entering a trailer may **mute the safety function** so it can operate faster inside, and re-enable it when *"people start to be around, maybe around the corner."* That is the wiki's first concrete statement of what the Outside-In blueprint's MUTE/UNMUTE decision is *for* — the infrastructure's job is not only to stop the robot but to license it to go faster where nobody is.

**The runtime supervisor.** Asked about a term from a conference slide ("PSF containers"), Mariani does not confirm the term but describes the mechanism: around an AI perception pipeline you place *"a combination of monitors, let's say scaffolding,"* and a **supervisor** — runtime software designed to **IEC 61508** and **ISO 13849** — that checks the pipeline's inputs and outputs, **evaluates the uncertainty the model reports**, decides whether the perception output is accurate enough, and only then *"gives a green light."*

Two things follow. First, this is architecturally the same move as a [safety filter](../concepts/robotics/safety-filters.md), one layer earlier: it filters *perception* rather than *action*, and its admissibility criterion is model uncertainty rather than set invariance. Second, it makes **uncertainty estimation a certified-path dependency** — which sits directly against the [contact-rich survey](safe-learning-contact-rich-survey.md)'s finding that current foundation models have *"weak uncertainty estimation."*

**The stack, as he orders it**: safe hardware first (**IGX**, *"many thousands of hardware safety mechanisms,"* rated for what he calls a "C2 or C3" architecture — the ASR garbles which standard that categorization belongs to), then the OS (Halos), then the runtime supervisor, then the end-to-end chain *"from camera to pipeline to the evaluation going back to the signal."* He declines to name a most-important layer: *"at the end I would say everything is important, and this is why we believe we needed to offer a layered approach."*

**What does not change.** Asked whether AI means fewer safety sensors, he says no, and states the continuity explicitly: certified sensors, certified actuators, safety PLCs, safety MCUs (*"close control to motors"*; NVIDIA's own architecture uses a safety MCU as a companion), and the end-to-end safety protocols (CIP Safety, PROFIsafe) all remain. *"The use of AI and safety is new, but the principle of safety — that is the redundancy and diversity, the monitoring and the validation — are still the key pillar on which we build all the story."*

## The standards layer, which is the most valuable part

Mariani is the standards editor as well as the vendor, and the sequence he lays out is the answer to a question the wiki's [robot safety standards](../concepts/robotics/robot-safety-standards.md) page has been holding open — *how does a stochastic learned policy demonstrate conformity?*

| Standard | What it is | His role |
|---|---|---|
| **ISO/IEC TR 5469** | *"the first report that was created internationally about AI functional safety"* — enumerates the challenges and candidate mitigations. Published (2024). | **editor / project leader** |
| **ISO/IEC TS 22440** | the follow-on: **requirements**, i.e. the certifiable framework built on TR 5469. Includes an annex on AI tools, covering simulation tools and the accuracy you must measure for them. | **convenor** |
| **ISO/PAS 8800** | the automotive-domain equivalent ("gives the certifier that possibility") | — |
| **IEC 61508**, **ISO 13849** | the classical functional-safety bases the runtime supervisor is designed against | co-convenor of MT 61508 |
| **IEC 62998** | safety-related sensors; cited for the failure rates that make pure real-world validation impractical | — |

He says the industry has been working on this for *"about four years"* and that **TS 22440 will be published "next year."**

> [!warning] Two bookkeeping corrections to the wiki's Halos page
> 1. The [Halos entity page](../entities/nvidia-halos.md) records NVIDIA holding **"ISO/IEC TS 22440 co-Convenor."** Mariani says *"the ISO/IEC TS 22440, of which I am the convenor,"* and his published biography lists him as **convenor of ISO/IEC JTC 1/SC 42/JWG 4** (the joint working group that owns TS 22440) and **project leader** of both TR 5469 and TS 22440 — while being **co-convenor of MT 61508-1/2**. The wiki appears to have attached the "co-" to the wrong standard. Corrected on that page.
> 2. He introduces himself as **"VP of Industry Safety."** NVIDIA's published author bio says **"Head of Industry Safety."** Recorded as stated, with the discrepancy noted rather than silently resolved.

## The certification mechanics, and the conflict-of-interest shape

The wiki already has the **Halos AI Systems Inspection Lab** from NVIDIA's own pages. Mariani states the flow plainly, and the phrasing is worth quoting exactly:

> Let's imagine a partner like **Agility**, as humanoid, that is using Halos. What we do is to do an inspection using **an independent organization within NVIDIA** that inspects if that integration has been completed successfully. In this way we provide this input to the final certification agency.

Named agencies: **TÜV Rheinland**, **exida**, **SGS**, **CERTX**, **UL**, plus one the captions render as "QBud" and which is not resolvable — most plausibly a second TÜV body, but **not asserted here**.

The justification is real and worth taking seriously: *"this system are so complex that a very high level analysis will never reveal the issue,"* so a platform vendor's structured inspection genuinely carries information a notified body cannot cheaply reproduce.

> [!note] "An independent organization within NVIDIA"
> That phrase is the whole structure in five words. The inspection is ANAB-accredited to ISO/IEC 17020 and issues a certificate of inspection; the final certificate still comes from an external notified body. But the party attesting that the platform was integrated correctly is a unit of **the company that sells the platform**, and its output is an input the notified body relies on precisely because it cannot easily redo the work. This is not an accusation — accredited in-house inspection bodies are a recognized structure — but the wiki should record the shape, because [it has been asking](../concepts/robotics/robot-safety-standards.md) what conformity evidence for a learned-policy robot will actually look like, and this is the answer taking form: **the platform vendor becomes part of the certification chain.**

## The prediction: certification bodies need a simulation lab

The most forward-looking claim, and the one most specific to this source. NVIDIA published a **CVPR tech brief** on a *Halos safety evaluation framework*, and Mariani's expectation is that notified bodies will need, alongside their physical labs, *"kind of an assessment lab that is more so digital — with the synthetic data generation, with simulation,"* because it *"will allow them to test end-to-end those models, generate data, and stress this system with data."*

Two supporting arguments:
- **Failure-rate arithmetic.** To demonstrate the failure rates something like IEC 62998 demands *"by collecting real data in the real world, it may take a while."*
- **Scenario augmentation.** He describes a technology for taking a recorded scene and reproducing it under many conditions — *"different light condition, different setting of the room"* — as the accelerator.

And then the concession, delivered without hedging when the host raises the sim-to-real gap:

> If the question was, can we get rid of tests in the real world — I would say **no**. That, I think, everyone is clear.

He adds the standards answer to the gap: TS 22440's annex on AI tools specifies **the process by which you develop such tools and the type of accuracy you must measure**, so the gap is to be *"evaluated and reduced and controlled"* rather than eliminated. See [real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md) and [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) for the wiki's parallel finding that a cheap simulated evaluator ranks well and measures badly.

## VLMs and VLAs as safety reasoners — claim and pushback

Unprompted, at the end: *"some of the new evolution on AI, like visual—also language action model, so VLA, VLM, can be used as **safety reasoners**."*

Host, immediately: *"but we both know that they are not so good as as we hope."*

Mariani's answer does not dispute it. It is that NVIDIA designs models *for* this — he names **[Alpamayo](../entities/alpamayo.md)** — *"that are designed for safety in that sense that they provide explainability and transparency, and then can be used as a **safety judge**."* Second use: AI-based tools to *"accelerate, augment and automate steps"* of **risk analysis and FMEA** — the safety engineer's own workflow — with the same caveat that they must be reliable, which is what TS 22440 is for.

> [!warning] This is the claim the wiki has the most evidence against
> "VLM as safety judge" is exactly what [semantic safety](../concepts/safety/semantic-safety.md) measures, and the measurements are not encouraging: [Gemini Robotics 2](gemini-robotics-2-safety-report.md) finds frontier models score **100%** acting on a safety signal handed to them as structured text but **cannot reliably produce that signal from perception** (human-proximity false-negative rate >40% at low false-positive rate), and that knowing a constraint (≥96% in text) does not survive the move to pointing, bounding boxes, or tool use. The host's one-line objection is better supported than the answer.
>
> What Mariani is actually proposing is narrower and more defensible than "the VLM decides": a model *trained for auditability* feeding a **deterministic** supervisor that can veto it, plus AI assistance for the human-authored hazard analysis. That is the layered architecture, not an appeal to model judgment. But the interview does not make the distinction, and a reader who imports "VLM as safety judge" without the deterministic layer beneath will get it wrong.

## Key claims

- **Safety is an enabler, not a cost** — the episode's organizing argument, restated three times. The concrete instance offered is a *safety simulation environment* that shortens time-to-certification, which is a product, not a compliance line item.
- The market is moving to a **full-stack, software-defined** approach: *"it's not anymore a problem of one computer, like the computer that is in the machine, but is the computer which you use for training, and you need simulation."*
- The shift is **from egocentric to contextually-aware safety**, and that is what *"opens a lot of different opportunities."*
- **Halos targets machinery, not only robots.** Designed to **ISO 13849**; NVIDIA has partners *"in the PLC world"* integrating PLC functions into the architecture, and the platform supports a **soft PLC running alongside an AI pipeline**. Asked whether these are incumbent safety-PLC vendors or new entrants: *"To the traditional guys… many of them."* He declines to name them.
- Halos components are *"a lot of the things I mentioned are open sourced"* — consistent with the [Outside-In blueprint](halos-outside-in-safety-github.md) being Apache-2.0.
- **GTC Berlin, October 2026**, with safety as a key topic. *"Europe and Germany and safety is kind of a marriage"* — and asked whether that marriage is a European handicap, he rejects the premise twice: *"No, no, it's a value."*

## The news segment: four items, all checked against primaries

The first 25 minutes are the hosts' news round-up. **These are secondary reports and the wiki should not cite the podcast for any of them** — each was verified against a primary before being recorded here, and two of the four turn out to be significant items this wiki does not have.

| Podcast claim | Verified? | The primary |
|---|---|---|
| *"NVIDIA finally announced to buy Hugging Face"* | **Yes, with a date correction** | Definitive agreement **2026-09-02**, announced **2026-09-03**: **$12.93 B** (~$11.9 B to stockholders + up to ~$1.0 B employee retention), close expected **H1 2027**, subject to regulatory approval. NVIDIA commits the platform stays open, that *"NVIDIA compute will not be required to build on or deploy through Hugging Face,"* and to continued multi-cloud / **multi-accelerator** support. ([NVIDIA newsroom](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/); [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)). The host's *"one week ago"* refers to the **late-August press reports** that a deal was close, not to the agreement. |
| **Black Forest Labs FLUX 3** — *"frontier multimodal model for robotics… deployed at Audi… soft body manipulation"* | **Yes** | FLUX 3 announced **2026-07-23**: one architecture over image, video, audio and **action**. **FLUX-mimic**, built with **mimic robotics** on the FLUX 3 backbone, adds an action decoder; **Audi** is testing it for **flexible door-seal installation**. Reported ~101 ms response and fine-tuning from ~30 min of robot data. ([bfl.ai](https://bfl.ai/blog/flux-3-mimic)) |
| **US blocks import of foreign-made humanoids** on national-security grounds | **Yes** | **FCC**, announced **2026-07-29**: import ban on new foreign-made **humanoid and quadruped** robots. Of ~15,000 humanoids shipped globally in 2025, **[Unitree](../entities/unitree-g1.md)** and **[AGIBOT](../entities/agibot.md)** each shipped >5,000; China's share ~**85%**. Unitree is on a Pentagon list of firms with claimed military ties. Beijing calls it protectionism. |
| **Anthropic Model Hardware Standard** research preview | **Yes** — already ingested | See [Model Hardware Standard](../entities/model-hardware-standard.md). The hosts' angle is new though: Peter Seeberg, who co-produces the OPC Foundation's own podcast, reads MHS as **overlapping OPC UA** and argues the harder half is not the driver but the **semantics** — *"not just the connecting to the hardware but knowing what is behind… you know what the 150 values behind the robot mean."* |

Smaller items, recorded as leads rather than facts: **Schaeffler** as the "picks and shovels" of humanoids (forming technology said to cut actuator production *"from minutes to seconds,"* and *"actively working with around 45 humanoid OEMs globally"* — attributed to Neura Robotics CEO **David Reger**, unverified); **Bosch** working with humanoid manufacturers; **Neura Robotics** hiring **robot teleoperators in motion-capture suits** as a named new job category, and having acquired a cleaning-robot company and Bosch's **ActiveShuttle**; **Tesla Optimus** to be deployed in Tesla's own factories before external sale; **Jensen Huang** signing an open-models letter.

And one observation from Peter Seeberg that belongs with the wiki's [deployment](../concepts/robotics/robot-safety-standards.md) thread, quoting Edward Sh. (surname garbled): *"Steel in the ground requires a completely different type of discipline, virtually unknown in the valley — **you can't ship a factory and then fix the bugs later**."* The hosts' reading is that a decade of European discomfort with ship-then-patch may invert as physical AI makes hardware quality binding again.

## Entities mentioned

- [Riccardo Mariani](../entities/riccardo-mariani.md) — **new page**: the guest, and the convenor of the standard AI functional safety will be certified against.
- [NVIDIA Halos](../entities/nvidia-halos.md) — the subject; this source corroborates and corrects it.
- [Alpamayo](../entities/alpamayo.md) — **new page**: NVIDIA's open reasoning-VLA family, cited here as the "safety judge" instance.
- [Agility Robotics / Digit](../entities/digit.md) — named as the humanoid partner going through Halos inspection.
- [Hugging Face](../entities/hugging-face.md) · [Model Hardware Standard](../entities/model-hardware-standard.md) · [Unitree G1](../entities/unitree-g1.md) · [AGIBOT](../entities/agibot.md) — from the news segment.
- Not yet in the wiki: **KION**, **Schaeffler**, **Neura Robotics**, **Bosch**, **Black Forest Labs**, **mimic robotics**, **exida / CERTX / SGS / UL**.

## Concepts touched

- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — **the AI-functional-safety standards line (TR 5469 → TS 22440) added from this source**; it is the answer to that page's own open frontier.
- [Safety filters for learned policies](../concepts/robotics/safety-filters.md) — the runtime supervisor as a *perception*-stage filter gated on model uncertainty.
- [Semantic safety](../concepts/safety/semantic-safety.md) — "VLM as safety judge," and the measurements against it.
- [Real-to-sim-to-real](../concepts/robotics/real-to-sim-to-real.md) · [robot policy evaluation](../concepts/robotics/robot-policy-evaluation.md) — simulation as certification evidence, and its limits.
- [Contact-rich manipulation](../concepts/robotics/contact-rich-manipulation.md) — Audi door-seal installation is a *textbook* instance, and it is a deployment, not a benchmark.
- [Control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the layered stack, from the certification side.

## Open questions

- **What is in the CVPR tech brief on the Halos safety evaluation framework?** Named but not located. It is the artifact behind the "certification bodies need a digital assessment lab" claim, and it would be the wiki's first *safety-specific* simulation-evaluation source.
- **What does TS 22440 actually require of a learned policy?** Its publication — *"next year"* per Mariani — is the single most consequential date in this wiki's [standards](../concepts/robotics/robot-safety-standards.md) thread. TR 5469 is published and free-ish to obtain in draft form; nobody here has read it.
- **What is "PSF"?** The host asks about "PSF containers" from an NVIDIA conference slide; the guest answers the concept without confirming the term. Unresolved.
- **Does the ANAB inspection ever fail anyone?** The structure — vendor-internal accredited inspection feeding an external notified body — is only as informative as its rejection rate, and no source states one.
- **What is Halos' relationship to Alpamayo?** Mariani presents an open reasoning VLA as a safety component. Whether it runs *inside* the certified envelope or as an uncertified advisor to it is exactly the question the wiki keeps asking about learned policies under Halos, and this interview does not settle it.
- **FLUX-mimic at Audi may be the wiki's most concrete contact-rich industrial deployment.** Door-seal installation on a soft, deformable part is contact-rich under [the survey's definition](safe-learning-contact-rich-survey.md) — sustained contact, coupled motion and force — and it is running in a car plant, not a benchmark. Worth its own ingest.
