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
| USB-C | **2× 140 W + 1× 100 W** | **2× 140 W** + USB-A combos | 1× 100 W + 1× 30 W |
| USB-A | 1× 12 W | 1× 12 W | 2× 12 W |
| **12 V car port** | ✅ **~120 W** (12 V/10 A) | ✅ **~120 W** (12 V/10 A) | ✅ 120 W (12 V/10 A) |
| Total max output | 300 W | 300 W | **1800 W** |
| Recharge | 140 W USB-C; 100 W solar | 330 W AC (→80 % in 50 min); 100 W solar | 1300 W AC; 600 W solar MPPT |
| UPS | ❌ | ❌ | ✅ **<20 ms** switchover |
| Price (approx) | ~$180 | ~$200 | ~$1,000 |

Sources: [C300 DC (A1726)](https://www.ankersolix.com/products/c300-dc), [C300 Power Station (A1722)](https://www.ankersolix.com/products/c300), [C300 weight 9.04 lb / 4.1 kg](https://batteryessence.com/anker-solix-c300-portable-power-station-review/), [C1000 (A1761)](https://www.ankersolix.com/products/c1000), [C300 family page](https://www.ankersolix.com/camping-battery-portable-power-station-a1726-a1722-pps).

> [!note] Two different "C300" products, same cell
> Anker sells a **C300 DC Power Bank (A1726)** and a **C300 Portable Power Station (A1722)** — both 288 Wh LiFePO4, **both with 2× 140 W USB-C and a 12 V/10 A car outlet**. The difference is the AC side: the **DC bank has no AC outlet and no 600 W surge** (hard-capped at 300 W), while the AC station adds 2× AC outlets + a 600 W SurgePad for +1.3 kg. **Both can drive the XLeRobot's two rails** (12 V car outlet → motors; USB-C → compute).

> [!note] BOM = DC bank; this build opts for the AC station for surge
> The official [XLeRobot BOM](https://xlerobot.readthedocs.io/en/latest/hardware/getting_started/material.html) lists the **C300 DC Power Bank (A1726, ~$160–180)** — and that unit already serves both rails (the [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) build runs its whole Tri-Bus on it: arms on the 12 V/10 A car outlet, wheels/neck + Jetson on USB-C). This build instead opts for the **AC Power Station (A1722)** for its **600 W surge headroom + AC outlet** — a deliberate margin, not a necessity. Earlier wiki drafts wrongly said the DC bank lacked a 12 V car port; **confirmed it has one** (user + paper).

## The decisive axes for an onboard robot battery

### 1. Weight — the C1000 is disqualified onboard
On a ~12 kg robot, the units add **2.8 / 4.1 / 12.9 kg** respectively. The C1000 would roughly **double** the robot's mass — a non-starter for a mobile base. The two C300s are rideable; the AC station's +1.3 kg over the DC bank (the inverter) is the cost of getting an AC outlet + 600 W surge — *not* extra rails (both have the 12 V car outlet).

### 2. Feeding a (capped) Thor — both C300s win, C1000 doesn't
The two C300s carry **2× 140 W USB-C**, which comfortably powers a software-capped [Thor](../../entities/jetson-thor.md) at any [`nvpmodel` budget](../../sources/nvidia-jetson-thor-platform-power-performance.md) (70 W trivially; even the 120 W mode fits the 140 W port). The **C1000's USB-C maxes at 100 W** — *below* Thor's 120 W mode — so on the C1000 you'd have to power compute off an AC brick (inverter loss) or boost the 12 V port. The cheap units are the better compute feed.

### 3. The two-rail problem — all three solve it; the question is surge & weight
The robot needs **two rails**: 12 V for the [STS3215](../../entities/so-arm101.md) motor bus and a 9–28 V feed for the compute ([§2 of the power-budget synthesis](../projects/xlerobot-thor-power-budget.md)). All three units have a **12 V/10 A car outlet + USB-C**, so all three serve both rails from one box — the [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) **Tri-Bus** does exactly this on the **C300 DC** (arms on the 12 V car outlet, wheels/neck + Jetson on separate USB-C rails). The real differences:
- **C300 DC**: serves both rails, **2.8 kg, cheapest, DC-native** — the paper-validated default. Limit: hard **300 W** total cap (no surge headroom) and no AC outlet.
- **C300 (AC)**: same rails **+ 600 W surge + AC outlet**, for +1.3 kg / ~+$20–40. Buy it if you want surge margin (e.g. you're *not* firmware-capping motor current) or an AC outlet.
- **C1000**: also serves both, but 12.9 kg and a 100 W USB-C ceiling (below Thor's 120 W mode).

> [!note] The surge may be optional
> The paper avoids needing 600 W surge by enforcing a firmware "virtual fuse" that caps the arm bus at ~240 W, keeping the whole system under the C300's 300 W ceiling. If you software-limit motor current that way, the DC bank's hard 300 W cap is fine and the AC station's surge is insurance rather than a requirement.

### 4. Capacity / runtime — C1000 is 3.7× but you can't carry it
With a 70 W-capped robot at ~145 W normal draw: **C300 (either) ≈ ~1.7 hr**; **C1000 ≈ ~6–7 hr**. The C1000's energy advantage is real but only usable in a stationary/tethered role.

## Verdict by role

| Role | Pick | Why |
|---|---|---|
| **Onboard default (lightest, cheapest)** | **C300 DC (A1726)** | Serves both rails (12 V car outlet + USB-C), **2.8 kg**, DC-native, ~$160–180 — and **proven untethered** ([Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) Tri-Bus). Limit: hard 300 W cap (no surge) → pair with firmware motor-current limiting. |
| **Onboard + surge margin** (this build) | **C300 Power Station (A1722)** | Same rails **+ 600 W surge + AC outlet** for +1.3 kg (4.1 kg) / ~+$20–40. The choice when you want transient headroom without firmware-capping motors, or an AC outlet for Thor's brick. |
| **Bench / charging dock / tether** | **C1000** | 3.7× energy (~6–7 hr), UPS, 6 AC + 12 V; too heavy to ride but ideal as the dev-time charging station. |

**Common setup:** a **C300 (DC or AC) rides on the robot; a C1000 (or wall) is the charging dock.** Between the two C300s it's a narrow call — the **DC bank** is lighter/cheaper and paper-validated; the **AC station** (this build's pick) trades +1.3 kg for 600 W surge headroom and an AC outlet.

## Related
- [XLeRobot + AGX Thor power budget](../projects/xlerobot-thor-power-budget.md) — the rate/runtime/two-rail analysis this comparison feeds.
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — the `nvpmodel` caps that make a 140 W USB-C feed sufficient for Thor.
- [XLeRobot](../../entities/xlerobot.md) — the platform (17× STS3215 @ 12 V; BOM lists the C300 DC A1726, this build substitutes the A1722).
- [Jetson Thor](../../entities/jetson-thor.md) — the compute being powered.
