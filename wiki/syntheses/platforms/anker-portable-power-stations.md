---
title: "Anker SOLIX portable power for a mobile robot — C300 DC vs C300 vs C1000"
type: synthesis
created: 2026-06-03
updated: 2026-06-03
tags: [anker, power-station, battery, c300, c300-dc, c1000, xlerobot, jetson-thor, energy-budget, platforms, buying-decision]
---

# Anker SOLIX portable power for a mobile robot — C300 DC vs C300 vs C1000

A buying-decision comparison of three Anker SOLIX units as the power source for a DC mobile robot (the running example is the [XLeRobot](../../entities/xlerobot.md) + [Jetson Thor](../../entities/jetson-thor.md) build analyzed in the [power-budget synthesis](../projects/xlerobot-thor-power-budget.md)). The two "C300" units are **different products with the same cell** — easy to confuse — and the C1000 is a different weight/role class entirely.

## Spec table

| | **C300 DC Power Bank** (A1726) | **C300 Power Station** (A1722) | **C1000** (A1761) |
|---|---|---|---|
| Capacity | 288 Wh (90,000 mAh) | 288 Wh (90,000 mAh) | **1056 Wh** (→ 2112 Wh expandable) |
| Chemistry | LiFePO4 | LiFePO4 | LiFePO4, 3,000 cycles to 80% |
| **Weight** | **2.8 kg** (6.2 lb) | **4.1 kg** (9.04 lb) | **12.9 kg** (28.4 lb) |
| **AC outlet** | ❌ none (DC-only) | ✅ **2×, 300 W / 600 W surge** (pure sine) | ✅ 6×, 1800 W / 2400 W surge (pure sine) |
| USB-C | **2× 140 W** + 1× 15 W | **2× 140 W** + USB-A combos | 1× 100 W + 1× 30 W |
| USB-A | 1× 12 W | 1× 12 W | 2× 12 W |
| **12 V car port** | ❌ none | ✅ **~120 W** (12 V/10 A) | ✅ 120 W (12 V/10 A) |
| Total max output | 300 W | 300 W | **1800 W** |
| Recharge | 140 W USB-C; 100 W solar | 330 W AC (→80 % in 50 min); 100 W solar | 1300 W AC; 600 W solar MPPT |
| UPS | ❌ | ❌ | ✅ **<20 ms** switchover |
| Price (approx) | ~$180 | ~$200 | ~$1,000 |

Sources: [C300 DC (A1726)](https://www.ankersolix.com/products/c300-dc), [C300 Power Station (A1722)](https://www.ankersolix.com/products/c300), [C300 weight 9.04 lb / 4.1 kg](https://batteryessence.com/anker-solix-c300-portable-power-station-review/), [C1000 (A1761)](https://www.ankersolix.com/products/c1000), [C300 family page](https://www.ankersolix.com/camping-battery-portable-power-station-a1726-a1722-pps).

> [!warning] Two different "C300" products, same cell
> Anker sells a **C300 DC Power Bank (A1726)** and a **C300 Portable Power Station (A1722)** — both 288 Wh LiFePO4, both with **2× 140 W USB-C**, but the **DC bank has no AC outlet, no 12 V car port, and no 600 W surge** (it's hard-capped at 300 W). They are not interchangeable for a two-rail robot.

> [!note] BOM = DC bank; this build substitutes the AC station
> The official [XLeRobot BOM](https://xlerobot.readthedocs.io/en/latest/hardware/getting_started/material.html) lists the **C300 DC Power Bank (A1726, $179.99)**. This analysis (and the wiki's [power-budget synthesis](../projects/xlerobot-thor-power-budget.md)) assumes a deliberate **substitution to the AC Power Station (A1722)** — precisely *because* the DC bank lacks the AC outlet and 12 V car port the two-rail Thor wiring needs. The trade-off you're buying with that swap is the subject of this page.

> [!warning] Contradiction — does the C300 DC have a 12 V car outlet?
> The [Cutting the Cord paper](../../sources/cutting-the-cord-untethered-xlerobot.md) (a built-and-measured XLeRobot) cites *its* unit (ref [22]) as the **"Anker SOLIX C300 DC Portable Power Station," $159.99**, and explicitly builds its Tri-Bus on the C300's **"three USB-C ports (two 140 W, one 100 W) and a 12 V DC car outlet capable of 10 A."** That **conflicts** with the web-sourced spec above, where the C300 *DC Power Bank* has no 12 V car port (and only 2× 140 W + 1× 15 W USB-C). Possible explanations: a distinct DC SKU/variant (e.g. C300X DC), an incomplete Anker web listing, or loose "DC" naming in the paper. The paper is primary + measured, so **if you're sourcing for the two-rail wiring, verify the exact SKU's port set before buying** — a C300 DC *with* the 12 V/10 A car outlet would make the AC substitution unnecessary for the motor rail.

## The decisive axes for an onboard robot battery

### 1. Weight — the C1000 is disqualified onboard
On a ~12 kg robot, the units add **2.8 / 4.1 / 12.9 kg** respectively. The C1000 would roughly **double** the robot's mass — a non-starter for a mobile base. The two C300s are rideable; the AC station's +1.3 kg over the DC bank (the inverter) is the cost of getting an AC outlet and a 12 V port.

### 2. Feeding a (capped) Thor — both C300s win, C1000 doesn't
The two C300s carry **2× 140 W USB-C**, which comfortably powers a software-capped [Thor](../../entities/jetson-thor.md) at any [`nvpmodel` budget](../../sources/nvidia-jetson-thor-platform-power-performance.md) (70 W trivially; even the 120 W mode fits the 140 W port). The **C1000's USB-C maxes at 100 W** — *below* Thor's 120 W mode — so on the C1000 you'd have to power compute off an AC brick (inverter loss) or boost the 12 V port. The cheap units are the better compute feed.

### 3. The two-rail problem — only the AC units solve it from one box
The robot needs **two rails**: 12 V for the [STS3215](../../entities/so-arm101.md) motor bus and a 9–28 V feed for Thor ([§2 of the power-budget synthesis](../projects/xlerobot-thor-power-budget.md)).
- **C300 DC**: serves the Thor rail (USB-C) but has **no 12 V output** → motors need a separate USB-C-PD→12 V buck. No AC outlet either.
- **C300 (AC)**: serves **both** — 12 V car port for motors, USB-C/AC for Thor — plus 600 W surge headroom. This is why it's the right onboard choice despite the weight penalty.
- **C1000**: also serves both (12 V port + AC), but at 12.9 kg and a 100 W USB-C ceiling.

### 4. Capacity / runtime — C1000 is 3.7× but you can't carry it
With a 70 W-capped robot at ~145 W normal draw: **C300 (either) ≈ ~1.7 hr**; **C1000 ≈ ~6–7 hr**. The C1000's energy advantage is real but only usable in a stationary/tethered role.

## Verdict by role

| Role | Pick | Why |
|---|---|---|
| **Onboard, mobile robot** | **C300 Power Station (A1722)** | Both rails from one box (12 V car port + USB-C/AC), dual 140 W USB-C for capped Thor, 600 W surge, 4.1 kg rideable, ~$200. The recommended **substitution** for this build (BOM ships the DC bank). |
| Onboard, weight-critical, single-rail | C300 DC (A1726) | ~1.3 kg lighter + DC-native (no inverter loss), but **no 12 V output and no AC** → only if you add a buck for motors and don't need surge. |
| **Bench / charging dock / tether** | **C1000** | 3.7× energy (~6–7 hr), UPS, 6 AC + 12 V; too heavy to ride but ideal as the dev-time charging station. |

**Common setup:** **C300 (A1722) rides on the robot; a C1000 (or wall) is the charging dock.** The C300 DC is the niche pick — only when shaving ~1.3 kg matters more than having the AC outlet, the 12 V port, and the surge.

## Related
- [XLeRobot + AGX Thor power budget](../projects/xlerobot-thor-power-budget.md) — the rate/runtime/two-rail analysis this comparison feeds.
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — the `nvpmodel` caps that make a 140 W USB-C feed sufficient for Thor.
- [XLeRobot](../../entities/xlerobot.md) — the platform (17× STS3215 @ 12 V; BOM lists the C300 DC A1726, this build substitutes the A1722).
- [Jetson Thor](../../entities/jetson-thor.md) — the compute being powered.
