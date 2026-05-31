---
title: XLeRobot + AGX Thor power budget — is a 300 W battery enough?
type: synthesis
created: 2026-05-30
updated: 2026-05-31
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

Motors run at **12 V**; the Thor wants **9–28 V** (via USB-C PD or Micro-Fit). Per NVIDIA's [Carrier Board Spec](../../sources/nvidia-jetson-thor-carrier-board-spec.md), the input maxes at **5 A over USB-C (≈140 W @ 28 V) vs 15 A over Micro-Fit** — so USB-C tops out **~28 W below the 168 W ceiling** (full load needs Micro-Fit), the **bundled adapter is USB-C** (Micro-Fit is the higher-current/latching alternative), and a PD controller arbitrates **first-come-first-serve** (you can't sum USB-C + Micro-Fit). The C300 exposes *individually capped ports*, not generic DC:

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

## What NVIDIA and the forums recommend

**NVIDIA does not bless any battery for the AGX Thor *Dev Kit*.** An NVIDIA staffer states the dev kit "is required to be used with the power supply that is bundled with the kit" ([External Power Supply Recommendation](https://forums.developer.nvidia.com/t/external-power-supply-recommendation/366448)) — battery operation is off-label and DIY. The robotics-intended path is the bare **T5000 module** on a custom carrier (rails **SYS_VIN_HV 22 A @ 9 V**, **SYS_VIN_MV 6 A @ 5 V** — [T5000 power thread](https://forums.developer.nvidia.com/t/queries-regarding-power-consumption-of-thor-t5000-module/348819)).

For powering the dev kit from a battery, the input window is **9–28 VDC**, with — per the [Carrier Board Spec (SP-12533-001)](../../sources/nvidia-jetson-thor-carrier-board-spec.md) — **max 5 A over USB-C vs 15 A over the latching Micro-Fit 3.0 J83**, under the **168 W enforced cap**. Two consequences the earlier forum-only picture missed: **USB-C (≈140 W) can't reach the 168 W ceiling — only Micro-Fit can**; and the **bundled adapter is USB-C**, so a battery is a genuinely separate Micro-Fit feed. A **CYPD8225 PD controller arbitrates first-come-first-serve**, so you can't sum the two inputs. No one names a specific commercial battery; the community data points ([Battery for Jetson Thor Developer's Kit](https://forums.developer.nvidia.com/t/battery-for-jetson-thor-developers-kit/350320)):

| Source | Setup | Notes |
|---|---|---|
| downingbots | **2× 26 Ah 12 V SLA in series** → 24 V, ~550 Wh | Chosen for safety/cost + existing recharger; **~1.6 hr at full load** |
| nleak (reply) | Recommends **Li-ion / LiFePO4** instead | Charges far faster (0.5–3C vs <0.1C for SLA) |
| Another deployment | Custom wheeled humanoid, battery via Micro-Fit | **~2 hr** on AI models, "easily/safely recharged" |

downingbots' 550 Wh → 1.6 hr independently corroborates the runtime math above. De-facto recipe: **any pack in the 9–28 V window, fed to the Micro-Fit port, sized for ~150–250 W and ~2 hr; Li-ion/LiFePO4 chemistry.**

> [!warning] The 28 V ceiling is the trap when picking a "24 V" pack
> - **2× 12 V SLA in series** floats to ~27–29 V charged — right at/over the limit.
> - **8S LiFePO4** ("24 V nominal") charges to **29.2 V → exceeds 28 V.** Don't direct-feed.
> - **Safe-by-construction direct feed:** **6S Li-ion** (25.2 V max) or **4S LiFePO4** (14.6 V max). **7S Li-ion** (29.4 V max) is too high.
> - Anything that can exceed 28 V needs a **DC-DC buck regulator** ahead of the Micro-Fit.

## Updated battery recommendation (canonical)

Incorporating the carrier-spec facts (5 A USB-C / 15 A Micro-Fit; USB-C bundled; first-come-first-serve):

1. **Feed the Micro-Fit J83, not USB-C.** It's the only input that carries the full 168 W (USB-C tops out ~140 W) and it latches. USB-C is fine for bench/light use.
2. **Put a DC-DC regulator between battery and Micro-Fit**, set to a fixed **~19–20 V** (well inside 9–28 V). This is the single best choice: it **eliminates the 28 V-ceiling trap entirely** regardless of pack chemistry, and at ~20 V the 168 W draw is only ~8.4 A (well under the 15 A limit). A buck-boost also holds the rail steady as the pack sags.
3. **Chemistry: Li-ion or LiFePO4** (fast charge, energy-dense). For *direct* feed without a regulator, only **6S Li-ion** (≤25.2 V) or **4S LiFePO4** (≤14.6 V) are inherently safe — see the 28 V-ceiling warning above.
4. **Size for watt-hours: ~300–500 Wh** for ~2 hr at ~150–250 W robot draw (corroborated by downingbots' 550 Wh ≈ 1.6 hr at full load). Buy Wh, not W.
5. **Don't wire both inputs** — first-come-first-serve means the second does nothing.
6. **Off-label caveat:** NVIDIA officially supports only the bundled USB-C PSU; and the spec's caution is explicit — **connect the module + all peripherals before applying power.**

### For the XLeRobot specifically
A cleaner build than the stock Anker AC station: **one 24 V-class DC pack + two DC-DC converters** —
- **converter A → ~20 V into Thor's Micro-Fit** (≤168 W),
- **converter B → 12 V for the 17× STS3215 motor bus.**

This gives both rails efficiently (no AC-inversion loss), respects each input's current limit, and is lighter than inverting to AC only to rectify back to DC.

## Summary takeaways

- **300 W *rate* is fine** for normal operation; 600 W surge covers transients. Rate is not your constraint.
- **Two rails, capped separately**: 12 V motors + a 9–28 V Thor feed. With the stock C300, no single port serves both; with a custom pack, the dual-DC-DC build above is cleaner.
- **Runtime, not rate, is the limit**: a Thor drops the XLeRobot from "10+ hr" to **~1.5–2.5 hr**. Buy **watt-hours, not watts**.
- **Prefer a DC-native pack** over an AC power station — skipping AC inversion is lighter and more efficient for a robot. See the canonical recommendation above for the regulator-into-Micro-Fit topology.

## Related

- [XLeRobot](../../entities/xlerobot.md) — platform (17× STS3215 @ 12 V; stock Anker C300)
- [Jetson Thor](../../entities/jetson-thor.md) — the compute being added (40–130 W module; dev kit 28 V/140 W PSU)
- [XLeRobot camera options for low-light + clutter](xlerobot-camera-options-low-light.md) — sibling integration analysis
