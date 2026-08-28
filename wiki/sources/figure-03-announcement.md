---
title: Introducing Figure 03 (Figure AI)
type: source
url: https://www.figure.ai/news/introducing-figure-03
author: Figure AI
affiliation: Figure AI
published: 2025-10-09
ingested: 2026-08-28
tags: [figure, figure-03, humanoid, helix, tactile-sensing, botq, manufacturing, home-robotics, vendor-source]
---

> [!warning] Vendor announcement, not a paper
> Every claim below is Figure-stated and uncorroborated. There is no evaluation, no baseline, and no third-party measurement anywhere in the post. Filed as a **primary** so that Figure 03 specs quoted elsewhere in this wiki trace to Figure's own words rather than to the secondary-coverage ecosystem, which already disagrees with itself (see [Contradictions](#contradictions)).

## Summary

**Figure 03** — [Figure AI](../entities/figure.md)'s third-generation humanoid, announced 2025-10-09. The framing is a ground-up hardware *and* software redesign along four axes named in the post: **Helix** (a redesigned sensory suite and hand system built for the VLA), **the home** (soft goods, wireless charging, better audio, battery safety), **mass manufacturing** (designed for tooled processes and a new supply chain at [BotQ](../entities/botq.md)), and **the world at scale** (faster actuators for commercial work). The generational story is not "more capable joints" — it is **sensing density and unit cost**. See [Figure 03](../entities/figure-03.md) for the consolidated platform page.

## Key claims (all Figure-stated)

### Sensing — the actual generational change

- New camera architecture: **2× the frame rate, ¼ the latency, 60% wider field of view per camera**, in a more compact form factor, with expanded depth of field. Stated purpose: "a denser, more stable perceptual stream" for Helix.
- **Embedded palm camera in each hand**, wide FOV, low latency — "redundant, close-range visual feedback during grasps," specifically so Helix keeps visual awareness "when the main cameras are occluded (i.e. when reaching into a cabinet)."
- **First-generation in-house tactile sensor** in each fingertip, detecting **forces as small as three grams** — "sensitive enough to register the weight of a paperclip." Figure says it built its own after "surveying existing market options" and finding they "could not withstand real-world use."
- Softer, more adaptive fingertips increase contact surface area for stable grasps on varied shapes.
- **10 Gbps mmWave data offload**, so "the entire fleet [can] upload terabytes of data for continuous learning."

### Home design

- **9% less mass and significantly less volume than Figure 02.**
- Multi-density foam at pinch points; covered in **soft textiles rather than hard machined parts**; soft goods fully washable and removable **without tools**; customisable clothing including cut-resistant materials.
- Battery has **multiple layers of protection** at BMS, cell, interconnect and pack level, and has **achieved UN38.3 certification** (see [F.03 Battery Development](figure-f03-battery.md) for the engineering detail).
- Audio upgrade for speech-to-speech: speaker **2× the size and nearly 4× more powerful** than Figure 02; microphone repositioned.
- **Wireless inductive charging at 2 kW** via **charging coils in the feet** — the robot steps onto a stand. Paired with wireless data offload, this is a "fully autonomous, wire-free system": it "can automatically dock and recharge itself as needed throughout the day."

### Manufacturing

- Figure 02 was "primarily designed to be manufactured with CNC machining"; Figure 03 "relies heavily on tooled processes such as **die-casting, injection molding, and stamping**." Consequence claimed: "each Figure 03 unit now costs dramatically less to build."
- Aggressive reduction of part count, assembly steps and non-critical components.
- **Vertical integration** across actuators, batteries, sensors, structures and electronics — "all designed completely in-house" — plus a year-long effort to qualify outside suppliers.
- [BotQ](../entities/botq.md)'s first-generation line: **up to 12,000 humanoids/year**, goal of **100,000 robots over four years**. Internally developed MES, full traceability on every subassembly.

### Commercial

- Actuators run at **2× faster speeds** with improved torque density (post writes "nm/kg"; presumably N·m/kg).
- Inductive charging enables "near-continuous operation"; mmWave offload happens "during shift breaks just by returning to the dock."
- Per-customer uniforms; **new side screens** for fleet identification and customer branding.

## What the announcement does *not* contain

Notable given how widely the numbers circulate: **the post states no height, no weight, no DOF count, no payload, no runtime, and no battery capacity.** The only quantitative body claim is the relative "9% less mass." Those absolute figures live on Figure's [product page](figure-03-product-page.md) (height/weight/payload/runtime/speed) and in the [battery post](figure-f03-battery.md) (2.3 kWh / 5 h) — different documents, published at different times. Also absent: price, availability, any autonomy or success-rate result, and any mention of onboard compute.

## Contradictions

> [!warning] The wiki's Figure 02 mass is wrong
> [Figure](../entities/figure.md) has carried "~60 kg" for Figure 02. Figure 03 is **61 kg** ([product page](figure-03-product-page.md)) and is **9% lighter** than Figure 02 — which implies Figure 02 was **~67 kg**. Secondary coverage generally cites 70 kg for Figure 02, and Figure appears never to have published an official Figure 02 spec table. The "~60 kg" figure cannot be reconciled with either. Corrected on the entity page.

> [!warning] Secondaries disagree on runtime
> Coverage of this announcement splits between **4-hour** and **5-hour** runtime. Figure's own product page and its own battery post both say **5 hours** (2.3 kWh at peak performance). The 4-hour figure has no primary behind it.

> [!note] "40 DOF" is secondary-only
> Widely repeated, absent from every Figure primary found. Figure 02's 28 DOF is likewise secondary-only. Treat both as uncited.

## Entities mentioned

- [Figure 03](../entities/figure-03.md) · [Figure](../entities/figure.md) · [BotQ](../entities/botq.md) · [Helix](../entities/helix.md)

## Concepts touched

- [VLA models](../concepts/learning/vla-models.md) — the hardware is explicitly subordinated to the model.
- [Whole-body control](../concepts/robotics/whole-body-control.md) — the sensing this post adds is what [Helix 02](figure-helix-02.md) later consumes.
- [Assistive robotics](../concepts/robotics/assistive-robotics.md) — the home-safety design choices (foam, textiles, washability).
- [Robot safety standards](../concepts/robotics/robot-safety-standards.md) — UN38.3 / UL2271 battery certification.

## Open questions

- **No onboard compute disclosed.** Helix is claimed to run onboard; nothing in three generations of Figure announcements says on what.
- **Is soft-goods-over-structure a safety argument or an appearance argument?** Foam and textiles reduce pinch and abrasion injury; they do nothing about the momentum of a 61 kg biped. No force, speed-limit, or standards claim (ISO 13482, ISO/TS 15066) accompanies the safety framing.
- **Cost is claimed, never stated.** "Dramatically less to build" and a 78% battery cost reduction are the only cost signals; no unit cost or price appears in any Figure primary.
- **What does the 3 g fingertip threshold mean in use?** Sensitivity is a floor, not a resolution, bandwidth, or drift spec.
