---
title: XLeRobot + AGX Thor power budget — is a 300 W battery enough?
type: synthesis
created: 2026-05-30
updated: 2026-05-30
tags: [xlerobot, jetson-thor, power, battery, anker-c300, sts3215, energy-budget, projects]
---

# XLeRobot + AGX Thor power budget

Can the stock XLeRobot battery — an **Anker SOLIX C300** (288 Wh, 300 W output) — run an **NVIDIA Jetson AGX Thor** plus the base motors and arms? Short answer: **the 300 W rate is fine; the binding constraints are the output-port wiring and the energy capacity.** Sibling to [LeRobot on ROSOrin Pro](lerobot-on-rosorin-pro.md) and the [XLeRobot camera options](xlerobot-camera-options-low-light.md) page — same "bolt powerful compute onto a cheap platform, mind the integration" theme.

## "300 W" is two specs

The [C300](https://www.ankersolix.com/products/c300) is rated **300 W output** (the *rate* it can deliver) **and 288 Wh capacity** (the *energy* it stores). The question "is 300 W enough" is about rate; rate turns out not to be the limiting factor.

## 1. Rate — adequate, with surge headroom

Worst-case draw, from verified specs:

| Load | Draw |
|---|---|
| **AGX Thor dev kit** | 40 W idle → ~130 W inference; ships with a **28 V / 5 A = 140 W** adapter (ADP-240LB), ~168 W enforced cap ([NVIDIA Jetson Linux dev guide](https://docs.nvidia.com/jetson/archives/r38.2/DeveloperGuide/SD/PlatformPowerAndPerformance/JetsonThor.html)) |
| **17× [Feetech STS3215](../../entities/so-arm101.md)** holding/idle | ~30–180 mA each → **~30–60 W** total ([RobotShop](https://www.robotshop.com/products/feetech-12v-30kgcm-magnetic-encoding-servo-sts3215)) |
| 17× STS3215 theoretical all-stall | 17 × 2.7 A × 12 V ≈ **550 W** (never simultaneous) |
| Pi relay + cameras | ~15 W |

- **Normal operation:** ~150 W (Thor ~70 + motors ~60 + 15) — comfortably under 300 W. ✅
- **Peak transient** (both arms lifting + base accelerating + Thor max): ~300–400 W — exceeds 300 W rated, but the C300's **600 W SurgePad** absorbs brief spikes. ⚠️
- Only sustained multi-servo-stall-while-driving-at-full-inference threatens the rail. In practice, **rate is fine.**

## 2. The real gotcha — two voltage rails, capped ports

Motors run at **12 V**; the Thor wants **28 V** (range 9–28 V, via Microfit barrel or USB-C PD). The C300 exposes *individually capped ports*, not generic DC:

- **AC outlet:** 300 W / 600 W surge
- **USB-C PD:** up to **140 W**
- **12 V car port:** typically ~10 A / ~120 W on these stations (verify on the C300) — *below* the motor peak

> [!warning] No single port gives you both rails
> The aggregate 300 W is not the constraint. Practical wiring: **Thor** → its 28 V brick on the **AC outlet** (~140 W of the AC budget), *or* **USB-C PD** if ≤140 W covers the load (may throttle near the 168 W ceiling). **Motors** → a **dedicated 12 V rail** (AC→12 V PSU or buck). Don't pull motor peaks through the car port — it'll current-limit and cut out.

## 3. The number that really changes — runtime

The wiki's stock "**10+ hr**" ([XLeRobot](../../entities/xlerobot.md)) assumes *no Thor*. With one:

| Mode | Avg draw | Runtime (288 Wh, ~AC losses) |
|---|---|---|
| Light / idle | ~115 W | ~2.5 hr |
| Normal | ~150 W | **~1.5–1.7 hr** |
| Heavy inference + manipulation | ~245 W | ~1.2 hr |

**~1.5–2.5 hr of real working time, down from 10+ hr.** Capacity, not rate, is what bites.

## Recommendations

- **Want more runtime? Buy more Wh, not more W.** A ~500–600 Wh pack roughly doubles working time with no higher output rating needed.
- **Wire two rails** (12 V motors + 28 V/PD Thor); respect each port's cap, not just the 300 W aggregate.
- **Prefer a DC-native battery** over an AC power station. The C300 *DC* variant (or a bare LiFePO4 12 V/24 V pack + buck converters) skips the AC-inversion loss, is lighter, and derives 12 V + a Thor rail more efficiently — a better fit than inverting to AC only to rectify back to DC.

## Related

- [XLeRobot](../../entities/xlerobot.md) — platform (17× STS3215 @ 12 V; stock Anker C300)
- [Jetson Thor](../../entities/jetson-thor.md) — the compute being added (40–130 W module; dev kit 28 V/140 W PSU)
- [XLeRobot camera options for low-light + clutter](xlerobot-camera-options-low-light.md) — sibling integration analysis
