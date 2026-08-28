---
title: Figure 03
type: entity
subtype: robot
created: 2026-08-28
updated: 2026-08-28
sources: 6
tags: [figure, figure-03, humanoid, bipedal, helix, tactile-sensing, botq, home-robotics, bmw, vendor-source]
status: partial
---

**Figure 03** — third-generation humanoid from [Figure AI](figure.md), announced **2025-10-09**. The generational thesis is not stronger joints: it is **sensing density and unit cost**. Figure 03 adds palm cameras and fingertip tactile sensing (the modalities [Helix 02](helix.md) is built on), sheds 9% of Figure 02's mass, wraps itself in washable soft goods, charges wirelessly through its feet, and — the point of the whole exercise — was redesigned for **die-casting, stamping and injection moulding** so it can be built at [BotQ](botq.md) at **one robot per hour**.

> [!warning] Everything on this page is vendor-stated
> Figure has published no paper, no benchmark, and no third-party measurement on Figure 03 or Helix. Multiple numbers in wide circulation (168 cm height, 40 DOF, 4-hour runtime) have **no Figure primary behind them** — see [Disputed and unsourced numbers](#disputed-and-unsourced-numbers).

## Specifications

From Figure's own [product page](../sources/figure-03-product-page.md) — the only official spec table Figure publishes:

| | |
|---|---|
| Height | **5'8" (~173 cm)** |
| Weight | **61 kg** |
| Payload | **20 kg** |
| Runtime | **5 hr** |
| Speed | **1.2 m/s** |
| System | Electric |
| Battery | **2.3 kWh**, 2 kW fast charge ([battery post](../sources/figure-f03-battery.md)) |
| Mass vs Figure 02 | **−9%**, "significantly less volume" ([announcement](../sources/figure-03-announcement.md)) |
| Actuators | **2× faster**, improved torque density (N·m/kg) |
| DOF | **not published by Figure** |
| Onboard compute | **never disclosed, any generation** |
| Price / availability | **not for sale** |

## Sensing — the actual generational change

All from the [announcement](../sources/figure-03-announcement.md):

- **Cameras**: new architecture at **2× frame rate, ¼ the latency, 60% wider FOV per camera**, more compact, expanded depth of field. Purpose: "a denser, more stable perceptual stream" for Helix.
- **Palm cameras**, one per hand — close-range visual feedback that survives head-camera occlusion "when reaching into a cabinet or working in confined spaces."
- **Fingertip tactile sensors**, developed in-house after Figure found market options "could not withstand real-world use." Detect **forces as small as 3 grams** — "the weight of a paperclip." Enables distinguishing "a secure grip and an impending slip **before it occurs**."
- Softer, more adaptive fingertips for larger contact area.
- **10 Gbps mmWave data offload** for fleet-scale data upload.

[Helix 02](../sources/figure-helix-02.md) states plainly that palm cameras and tactile "are new hardware capabilities from Figure 03. **This is the first time we've demonstrated neural network policies that depend on these modalities**" — i.e. the hardware was specified by what the model needed. That co-design is the most transferable idea on this page.

## Home design

- **Multi-density foam** at pinch points; **soft textiles rather than hard machined parts**; soft goods **fully washable, removable without tools**; optional cut-resistant garments.
- **Audio**: speaker **2× the size, ~4× more powerful** than Figure 02; microphone repositioned — for real-time speech-to-speech.
- **Wireless inductive charging at 2 kW** via **coils in the feet**: the robot steps onto a stand. With mmWave offload this is a wire-free system that "can automatically dock and recharge itself as needed throughout the day."

> [!note] The soft-goods claim is about abrasion and pinch, not momentum
> Foam and textiles address contact injury and trapping. Nothing in any Figure primary addresses the kinetic energy of a 61 kg biped, and no humanoid safety standard (ISO 13482, ISO/TS 15066) is cited anywhere. See [robot safety standards](../concepts/robotics/robot-safety-standards.md).

## Battery — the most substantive Figure engineering disclosure

From [F.03 Battery Development](../sources/figure-f03-battery.md) (2025-07-17):

- **2.3 kWh → 5 h at peak performance**; **2 kW fast charge** with integrated active cooling.
- **94% energy-density improvement across F.01 → F.03**; **78% cost reduction over F.02**.
- **Structural pack** — stamped steel, die-cast aluminium, structural adhesive; serves as a **load-bearing member of the torso**; survives a **1 m drop onto concrete from any orientation**.
- Four-layer safety: BMS, cell (2 internal fuses), interconnect (wirebond **tuned as a fusible element**), pack (anti-propagation potting + patented flame-arrestor vent). Fault-injection tested by heating a cell into thermal runaway; **no external flame**.
- **UN38.3 certified**; first humanoid battery in process for **UL 2271**, a standard Figure helped an OSHA NRTL *create* because none existed.

> [!note] ~460 W is the whole-robot power budget
> 2.3 kWh / 5 h. That must cover locomotion, actuation **and** onboard Helix inference — which Figure has never sized. For context, a Thor-class module alone draws 40–130 W ([Jetson module ladder](../syntheses/platforms/jetson-module-ladder-power-performance.md)), up to ~28% of the budget.

## Manufacturing and fleet

[Announcement](../sources/figure-03-announcement.md) + [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md) (2026-04-29):

- Figure 02 was designed for **CNC machining**; Figure 03 for **die-casting, injection moulding, stamping** — a large tooling investment traded for per-unit cost.
- Vertical integration across actuators, batteries, sensors, structures, electronics.
- **350+ units delivered** by April 2026; rate **1/day → 1/hour, 24× in under 120 days**.
- **80%+ end-of-line first-pass yield**; **99.3%** on the battery line (500+ packs); **9,000+ actuators across 10+ SKUs**; **50+ in-process inspection points**; **80+ end-of-line functional tests** per robot plus thousands-of-cycle burn-in (squats, shoulder presses, jogging).
- Fleet infrastructure: custom Fleet Management System, **OTA updates**, in-house Field Service Management, formal **recall-campaign** processes, and software **"fallback ladders"** for graceful degradation.

## Deployment

- **BMW Group Plant Spartanburg**, Hall 52, from **2026-06-30** ([F.03 at BMW](../sources/figure-03-at-bmw.md)) — the **sequencing** use case: parts that "do not arrive in mathematically perfect orientations," requiring perception-driven correction plus mobility plus two force regimes (thin-walled parts *and* pulling a caster-wheeled cart). Figure's stated form-factor argument: "structurally infeasible to solve with traditional, fixed automation or six-axis robotic arm."
- Predecessor: **Figure 02** contributed to **30,000 cars / 90,000+ parts / 1,250+ runtime hours over 11 months** at the same plant ([AI Index 2026](../sources/stanford-hai-ai-index-2026.md)).
- **Home: not deployed.** Figure's [product page](../sources/figure-03-product-page.md) claims household tasks "all autonomously" in the present tense; no home deployment, price, or availability has been announced.

## Disputed and unsourced numbers

> [!warning] Height — 5'8" (Figure) vs 168 cm (everyone else)
> 5'8" is **172.7 cm**. Secondary coverage almost universally says **168 cm** — which is 5'6", and which was *Figure 02's* number. Likeliest a copy-paste carry-forward. This wiki uses **~173 cm**.

> [!warning] Figure 02's mass, and this wiki's own error
> [Figure](figure.md) carried "~60 kg" for Figure 02. Figure 03 is **61 kg** and **9% lighter** than Figure 02 → Figure 02 was **~67 kg**. Secondaries say 70 kg. Figure appears never to have published an official Figure 02 spec table. "~60 kg" is corrected.

> [!warning] Runtime — 5 h, not 4 h
> Secondary coverage splits. Both Figure primaries (product page, battery post) say **5 hours**. The 4-hour figure has no primary.

> [!note] "40 DOF" is secondary-only
> Repeated everywhere, present in no Figure primary. The closest Figure disclosure is oblique: **9,000+ actuators across 350+ robots ≈ 26 actuators/robot** ([production ramp](../sources/figure-ramping-03-production.md)) — which does not obviously reconcile with 40.

## Related

- [Figure](figure.md) — the line and company; Figure 01 / 02 history.
- [Helix](helix.md) — the AI system Figure 03 exists to run; Helix 02 **requires** this hardware.
- [BotQ](botq.md) — the factory Figure 03 was designed around.
- [Index](figure-index.md) — the human-video data programme feeding Helix.
- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — where Figure 03 sits in the landscape.
- [1X NEO](1x-neo.md) — the closest competitor by intent (household humanoid, closed stack, aspirational consumer).
- [Tesla Optimus](tesla-optimus.md) · [Apptronik Apollo](apptronik-apollo.md) · [Atlas](atlas.md) — the closed research-humanoid tier.

## Mentioned in

- [Introducing Figure 03](../sources/figure-03-announcement.md) — the primary announcement.
- [Figure 03 product page](../sources/figure-03-product-page.md) — the only official spec table.
- [F.03 Battery Development](../sources/figure-f03-battery.md) — 2.3 kWh, UN38.3/UL2271, structural pack.
- [Introducing Helix 02](../sources/figure-helix-02.md) — the model built on this hardware's new sensors.
- [Ramping Figure 03 Production](../sources/figure-ramping-03-production.md) — 350+ units, 1/hour, yields.
- [F.03 Arrives at BMW](../sources/figure-03-at-bmw.md) — first commercial deployment.
- [Stanford HAI — AI Index Report 2026](../sources/stanford-hai-ai-index-2026.md) — Figure 02 BMW deployment data.

## Open questions

- **Onboard compute is the biggest hole.** Three generations, a claimed onboard three-tier model running S0 at 1 kHz, and Figure has never named a chip or a wattage.
- **DOF.** Every competitor publishes it. Figure does not.
- **Unit cost.** "Dramatically less to build" plus a 78% battery cost cut is the entire disclosure.
- **What fraction of the 350+ units is outside Figure's own buildings?**
- **UL 2271 status** — "in process" as of July 2025, unreported since.
- **Does the 20 kg payload survive the −9% mass?** Identical to Figure 02's widely-cited payload; possibly inherited rather than re-rated.
