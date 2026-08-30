---
title: Foundation Robotics (Foundation Future Industries) — Phantom
type: entity
subtype: company
created: 2026-08-29
updated: 2026-08-29
sources: 0
tags: [foundation-robotics, phantom, humanoid, defense, vendor-source, contested-claims, cycloid-actuator, live-web]
---

**Product page:** [foundation.bot/phantom](https://foundation.bot/phantom)

**Foundation Future Industries, Inc.** (commonly "Foundation Robotics") — humanoid company founded **2024**, building **Phantom**, described on its own page as *"our first production humanoid robot."* Unlike most of the humanoid field, its stated market is **military and industrial**, not household or service work.

> [!warning] Read this page as a claims record, not a spec sheet
> **Foundation's published specifications contradict each other, and its most-repeated corporate claim was denied outright by the company it named.** This page exists to record that, because Phantom otherwise reads as an ordinary entry in the [humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) and it is not one.
>
> `sources: 0` is accurate — **no primary is ingested here.** Everything below is `[live-web]`: the vendor's product page, read directly, plus reporting from CNBC, Newsweek and Humanoids Daily. Nothing has been sealed or independently verified.

## The spec sheet contradicts itself

The [product page](https://foundation.bot/phantom) states Phantom's payload **twice, with different numbers**, inside the same specification block:

```
PAYLOAD CAPACITY 88.2lbs (40kg)    PAYLOAD CAPACITY 40l (20kg)
```

**40 kg and 20 kg, a factor of two apart.** Foundation's briefing to [Humanoids Daily](https://www.humanoidsdaily.com/news/foundation-emerges-with-phantom-humanoid-betting-on-novel-actuators-and-hybrid-ai) cites *"approximately 20 kg payload capacity"* — matching the lower figure. Whatever the true number, **Phantom's payload cannot be quoted from Foundation's own page**, and any secondary source quoting 40 kg is repeating one half of a self-contradiction.

### And the actuator is described two incompatible ways

| Source | Claim |
|---|---|
| [Product page](https://foundation.bot/phantom) | *"Phantom's **proprietary cycloid actuators** set a new benchmark for power, precision, and efficiency"* |
| Foundation, briefing [Humanoids Daily](https://www.humanoidsdaily.com/news/foundation-emerges-with-phantom-humanoid-betting-on-novel-actuators-and-hybrid-ai) | uses *"**rolling contact gearboxes** rather than harmonic or **cycloid** drives found in competitors"* |

These are not two descriptions of one thing — the second explicitly names cycloid drives as what competitors use and Foundation does *not*. The actuator is the company's stated core differentiator, with a claimed **90–95% efficiency against 50–60% for competitors**, and it is described inconsistently by the company itself.

## Published specifications `[live-web]`

| | |
|---|---|
| Height / weight | 1.8 m (5'11") / 80 kg (176 lb) |
| Degrees of freedom | **29** |
| Max speed | 1.7 m/s |
| Response time | <10 ms |
| Max peak torque | 160 Nm (118 lb-ft) |
| Max back-driving torque | **<1.0 Nm** |
| Joint torques | wrist 20 Nm, shoulder 119 Nm, legs >160 Nm |
| Voltage / actuator speed | 48 V / 72 V; 9 rad/s @ 48 V, 12 rad/s @ 72 V |
| Payload | **disputed — see above** |

**What the page does not publish at all:** battery, runtime, onboard compute, sensors, or price. For a page presenting a "production humanoid robot," the absence of a runtime figure is notable — it is the specification that determines whether a robot can do a shift.

Reported elsewhere but not on the page: camera-only perception with a 360° head array, **explicitly rejecting LiDAR** (Tesla-style), an **AMD** compute partnership, initial deployment **tethered for power** with battery versions planned, and target pricing around **$100k via subscription**.

## Software claims `[live-web]`

Per the [Humanoids Daily](https://www.humanoidsdaily.com/news/foundation-emerges-with-phantom-humanoid-betting-on-novel-actuators-and-hybrid-ai) briefing: a **hybrid** approach combining imitation learning with state-based models incorporating physics, kinematics and task dynamics, with **RL for locomotion**. The claim is that *"simple tasks can be learned in about 30 minutes,"* reducing dependence on large teleoperation fleets.

No benchmark, success rate, rollout count, or independent evaluation accompanies any of this. Per the [success-rate audit](../syntheses/platforms/vla-success-rate-audit.md), a "30 minutes to learn a task" claim without a task definition or a success criterion is not a measurable statement.

## The claims record

Recorded because it is directly relevant to how much weight the specifications above deserve, and because it is documented by mainstream outlets rather than inferred.

**The GM claim, denied.** [CNBC reported in June 2024](https://www.cnbc.com/2024/06/12/robotics-startup-synapse-ceo-exaggerated-gm-claims.html) that Foundation was raising funds with exaggerated claims about ties to General Motors, including that GM had committed to invest and had placed a **$300 million purchase order**. GM's response, verbatim:

> *"GM has never invested in Foundation Robotics and has no plans to do so. In fact, GM has never had an agreement of any kind with the company."*

**A public demonstration failure.** At a [Newsweek](https://www.newsweek.com/could-this-humanoid-robot-become-the-armys-ultimate-warrior-11063424) demonstration, Phantom stood unassisted briefly and then **collapsed while standing** beside the CEO and a reporter. Foundation attributed it to an *"EtherCAT drop"* caused by electrostatic discharge.

> [!note] The demo failure is the least damning item here
> Robots fall, ESD is a real and mundane failure mode, and a company willing to demo live at all is doing something most of this wiki's humanoid entries do not. It matters only in context: a company asking defense agencies to field its robots is claiming a reliability standard, and this is the only public reliability datapoint that exists.

**Production targets that move.** An early briefing gave **40–50 units in 2025** and **over 10,000 in 2026**, with deliveries starting April–May 2025. Later reporting describes a target of **50,000 units by 2027** from a 2025 base of dozens. Both cannot be plans for the same company on the same timeline.

**Founder and adviser background**, as reported: CEO **Sankaet Pathak** was previously CEO of **Synapse**, a banking-as-a-service platform that **filed for bankruptcy in 2024**; the GM episode surfaced within weeks of that bankruptcy. Co-founders include **Arjun Sethi** (CEO of Tribe Capital, which led Foundation's ~$11–12M pre-seed) and **Mike LeBlanc** (14-year Marine Corps veteran, co-founder of Cobalt Robotics). **Eric Trump** is chief strategy adviser.

**Commercial and defense position**, as reported: ~$24M in government research contracts covering inspection, logistics and **weapons handling**; a claimed **$100M in contracted annual recurring revenue**; testing in Ukraine; a stated goal of US front-line deployment; and fundraising of ~$100M at a ~$1B valuation, with reported backing from Saudi royals.

## Why it matters in this wiki

- **It is the sharpest instance of the pattern [the industry map](../syntheses/society/robot-ai-industry-map.md) describes** — capital and contracts committed far ahead of demonstrated capability. The wiki's canonical framing is the **12.4% [BEHAVIOR-1K](behavior-benchmark.md)** number; Foundation reports $100M contracted ARR and 50,000-unit targets against zero published performance data.
- **It is a test of the wiki's own standards.** Everything on the [product page](https://foundation.bot/phantom) would pass an uncritical read: real units, plausible torques, a named actuator technology. Only reading the page *closely* surfaces a payload stated twice at 2× difference, and only reading the company's other statements surfaces the actuator contradiction. **A spec sheet is not evidence; it is a document that can be checked.**
- **Defense is a market segment the wiki otherwise does not cover.** Most humanoid entries here target factories or homes. Weapons-handling contracts and battlefield testing are a different regulatory and safety regime, and this wiki holds nothing on it — see [robot safety standards](../concepts/robotics/robot-safety-standards.md), which is written around ISO 13482-style human-proximity safety, not armed systems.

## Related

- [Humanoid platforms survey](../syntheses/platforms/humanoid-platforms-survey.md) — where Phantom sits among comparable machines.
- [The Robot AI industry](../syntheses/society/robot-ai-industry-map.md) — the capital-ahead-of-capability pattern.
- [Zeroth M1](zeroth-m1.md) — the wiki's other case of a product sold on a claim with no published evidence behind it.
- [Helix](helix.md) — the standard this wiki applies to vendor-only claims: marketing-grade until replicated.

## Mentioned in

*No ingested source. This page is built entirely from `[live-web]` material — see the warning at the top.*

## Open questions / TBD

- **Which payload figure is real?** Resolvable only by a datasheet Foundation has not published.
- **Cycloid or rolling-contact?** The company's differentiator is described both ways; no third-party teardown or actuator test exists in any source found.
- **No runtime, battery, or compute specification** has been published for a robot described as in production.
- **Is the $100M contracted ARR verifiable?** No breakdown, counterparty, or filing is public; it is a company statement.
- **Nothing here is ingested.** If Foundation publishes a datasheet or technical report, it should be ingested and sealed — at which point the contradictions above become checkable against a fixed document rather than a live page that can change without notice.
