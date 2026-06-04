---
title: XLeRobot + AGX Thor power budget — is a 300 W battery enough?
type: synthesis
created: 2026-05-30
updated: 2026-06-04
tags: [xlerobot, jetson-thor, power, battery, anker-c300, sts3215, energy-budget, nvpmodel, power-modes, tiered-power, projects]
---

# XLeRobot + AGX Thor power budget

Can the stock XLeRobot battery — an **Anker SOLIX C300** (288 Wh, 300 W output) — run an **NVIDIA Jetson AGX Thor** plus the base motors and arms? Short answer: **the 300 W rate is fine; the binding constraints are the output-port wiring and the energy capacity.** Sibling to [LeRobot on ROSOrin Pro](lerobot-on-rosorin-pro.md) and the [XLeRobot camera options](xlerobot-camera-options-low-light.md) page — same "bolt powerful compute onto a cheap platform, mind the integration" theme.

> [!note] This analysis assumes you software-cap Thor's power with `nvpmodel`
> Thor's draw is **not** a fixed 130 W — it's a software-selectable budget (70 / 90 / 120 W, or uncapped MAXN). Pinning a lower mode is the single biggest lever for a battery robot: it bounds peak draw, removes the surge risk against the 300 W rail, and stretches runtime — at a throughput cost. The [§0 nvpmodel section](#0-the-biggest-lever--software-cap-thors-watts-nvpmodel) below works this through; the rate/runtime numbers that follow assume a **70 W cap (Mode 3)** unless noted.

## 0. The biggest lever — software-cap Thor's watts (`nvpmodel`)

Per NVIDIA's [Jetson Thor Platform Power and Performance chapter (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md), the **T5000** module's power is a software-selected budget. You are not stuck at the 130 W TDP:

| `nvpmodel` mode | Module budget | CPU | GPU (TPC) | Best for |
|---|---|---|---|---|
| 0 — MAXN | uncapped, throttles @ **130 W** TDP | 14 cores @ 2601 MHz | **10** @ 1386 MHz | bench / burst; *not* sustained |
| 1 — 120 W (default) | **120 W** | 14 @ 2601 | **10** @ 1386 | full-throughput sustained |
| 2 — 90 W | **90 W** | 14 @ 2601 | **6** @ 1530 | CPU-heavy, GPU-light |
| 3 — 70 W | **70 W** | 12 @ 1998 | **6** @ 1530 | **battery robots** |

Switch at runtime, persists across reboot: `sudo nvpmodel -m 3` (then `nvpmodel -q` to confirm).

- **The trade-off is mostly GPU.** Any sub-120 W mode drops the GPU from **10 → 6 TPC (~−40 % GPU throughput)**; the CPU is barely affected at 90 W and only modestly clocked-down at 70 W. So **CPU/perception/control loops** lose little at 70 W, while **GPU-bound VLA inference** takes roughly a 40 % hit. For latency-sensitive single-policy VLA you may prefer 90 W (full CPU, reduced GPU) or accept the slower 70 W loop; for classic ROS perception + control, **70 W is nearly free.**
- **Capping fixes the rate problem outright.** At Mode 3, Thor is bounded ≤ 70 W, so the worst-case "heavy inference + manipulation" spike that previously flirted with the 300 W rail no longer does (see §1, §3). You stop depending on the C300's surge pad.
- **It can also simplify the wiring.** At 70 W, Thor's compute rail fits comfortably inside a single **USB-C PD feed (140 W)** with ~70 W to spare — so the "you must use Micro-Fit to reach the 168 W ceiling" constraint (§2) only bites if you run MAXN/120 W. Capped, USB-C alone powers the compute. (Motors still need their own 12 V rail regardless.)

## "300 W" is two specs

The [C300](https://www.ankersolix.com/products/c300) is rated **300 W output** (the *rate* it can deliver) **and 288 Wh capacity** (the *energy* it stores). The question "is 300 W enough" is about rate; rate turns out not to be the limiting factor.

> [!note] Which C300 — the analysis assumes the AC station
> The official [BOM](https://xlerobot.readthedocs.io/en/latest/hardware/getting_started/material.html) lists the **C300 DC Power Bank (A1726)** — 2.8 kg, DC-only (no AC outlet, hard 300 W cap), but it **does have a 12 V/10 A car outlet + USB-C**, so it serves both robot rails on its own (the [Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) Tri-Bus runs on exactly this unit). This page assumes the **C300 Portable Power Station (A1722, 4.1 kg)** instead, taken for its **600 W surge headroom + AC outlet** — a margin, not a necessity. The §2 wiring works on either; the AC just adds surge. See [Anker C300 DC vs C300 vs C1000](../platforms/anker-portable-power-stations.md).

## 1. Rate — adequate, with surge headroom

Worst-case draw, from verified specs:

| Load | Draw |
|---|---|
| **AGX Thor module** | 40 W idle → **software-capped budget: 70 / 90 / 120 W**, MAXN throttles @ 130 W TDP ([Thor Platform Power & Performance, R38.4](../../sources/nvidia-jetson-thor-platform-power-performance.md)). Dev kit ships with a **28 V / 5 A = 140 W** adapter (ADP-240LB) under a **~168 W** total-system cap. |
| **17× [Feetech STS3215](../../entities/so-arm101.md)** holding/idle | ~30–180 mA each → **~30–60 W** total ([RobotShop](https://www.robotshop.com/products/feetech-12v-30kgcm-magnetic-encoding-servo-sts3215)) |
| 17× STS3215 active manipulation | ~**90 W** typical (a few servos moving under load; not all-stall) |
| 17× STS3215 theoretical all-stall | 17 × 2.7 A × 12 V ≈ **550 W** (never simultaneous) |
| Pi relay + cameras | ~15 W |

Assuming a **70 W Thor cap (Mode 3)**:
- **Normal operation:** ~145 W (Thor ~70 + motors ~60 + 15) — comfortably under 300 W. ✅
- **Heavy (capped):** ~175 W (Thor **70**, hard-capped + motors active ~90 + 15) — still a wide margin to 300 W. ✅
- **Peak transient** (both arms lifting + base accelerating): the only way back toward the rail is many servos stalling at once; the C300's **600 W SurgePad** covers brief spikes, but with Thor pinned at 70 W you rarely get near it.

> [!note] What capping changes vs. running uncapped
> At **MAXN/120 W**, heavy inference + manipulation peaked ~**225–245 W** and leaned on the surge pad. At **Mode 3 (70 W)** the same scenario is ~**175 W** — **the rate question stops being interesting.** The cost is ~40 % GPU throughput (see §0). This is the recommended posture for the XLeRobot unless a specific VLA needs full GPU.

## 2. The real gotcha — two voltage rails, capped ports

Motors run at **12 V**; the Thor wants **9–28 V** (via USB-C PD or Micro-Fit). Per NVIDIA's [Carrier Board Spec](../../sources/nvidia-jetson-thor-carrier-board-spec.md), the input maxes at **5 A over USB-C (≈140 W @ 28 V) vs 15 A over Micro-Fit** — so USB-C tops out **~28 W below the 168 W ceiling** (full load needs Micro-Fit), the **bundled adapter is USB-C** (Micro-Fit is the higher-current/latching alternative), and a PD controller arbitrates **first-come-first-serve** (you can't sum USB-C + Micro-Fit). The C300 exposes *individually capped ports*, not generic DC:

- **AC outlet:** 300 W / 600 W surge
- **USB-C PD:** up to **140 W**
- **12 V car port:** typically ~10 A / ~120 W on these stations (verify on the C300) — *below* the motor peak

> [!warning] No single port gives you both rails
> The aggregate 300 W is not the constraint. Practical wiring: **Thor** → its 28 V brick on the **AC outlet** (~140 W of the AC budget), *or* **USB-C PD** if ≤140 W covers the load (may throttle near the 168 W ceiling). **Motors** → a **dedicated 12 V rail** (AC→12 V PSU or buck). Don't pull motor peaks through the car port — it'll current-limit and cut out.

## 3. The number that really changes — runtime

The wiki's stock "**10+ hr**" ([XLeRobot](../../entities/xlerobot.md)) assumes *no Thor*. With one, **the nvpmodel cap moves the runtime too** — capping draw stretches it:

| Scenario | Thor @ **70 W cap** (Mode 3) | Thor uncapped (120 W / MAXN) |
|---|---|---|
| Light / idle | ~95 W → **~2.6–3.0 hr** | ~115 W → ~2.5 hr |
| Normal | ~145 W → **~1.7–1.8 hr** | ~150 W → ~1.5–1.7 hr |
| Heavy inference + manipulation | ~175 W → **~1.4–1.5 hr** | ~225–245 W → ~1.1–1.2 hr |

*(288 Wh usable, derated for AC-inversion / DC-DC losses.)*

**~1.4–3.0 hr of real working time, down from 10+ hr.** Capping Thor at 70 W buys roughly **+15–25 % runtime in the heavy case** (≈1.2 → 1.5 hr) and flattens the draw, but **capacity, not rate, is still what bites** — the cap helps at the margin; a bigger pack helps more (§"Updated battery recommendation"). The honest framing: software-capping is free runtime + safety headroom you should take, but it won't turn a 288 Wh station into an all-day robot.

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

## Putting a Jetson Thor onboard — the two-pack (tiered-power) option

[Cutting the Cord](../../sources/cutting-the-cord-untethered-xlerobot.md) shipped an **[Orin Nano](../../entities/jetson-orin-nano.md)** precisely because a **[Jetson Thor](../../entities/jetson-thor.md)** (40–130 W) **"exceeds the power budget"** of a single 288 Wh pack — and named the fix: *"tiered compute architectures or an additional power supply, including using an additional Anker."* A **second [C300 DC](../platforms/anker-portable-power-stations.md)** dedicated to Thor is that fix, and it works.

**Topology — dedicate pack #2 to Thor:**
- **Pack #1** = the existing Tri-Bus: wheels/neck on a 140 W USB-C rail, the 17× [STS3215](../../entities/so-arm101.md) arms on the 12 V/10 A car outlet, sensors. Unchanged.
- **Pack #2** = Thor alone, fed from one **140 W USB-C** port (USB-C→DC PD-140 W cable), with Thor pinned to **`nvpmodel -m 3` (70 W)**. Optionally move the high-draw arm bus onto pack #2's car outlet as well.

**Why it works:**
- **Delivery** — Thor's input is 9–28 V / USB-C PD (bundled adapter = 28 V/5 A = 140 W), so a C300 DC 140 W port feeds it directly. Capped at 70 W (even 90 W), it sits well inside the port; at 120 W the *total* board draw nears the 140 W USB-C ceiling, so **70–90 W is the target on a USB-C feed**. No Micro-Fit needed.
- **Isolation** — a separate pack is the strongest form of the Tri-Bus principle: Thor never shares a rail with motor transients, so the 12.2 V→0.3 V brownout that killed the shared-bus design can't reach it.
- **Runtime** — Thor @ 70 W ≈ **~3.5 hr** on its own 288 Wh (@ 120 W ≈ ~2 hr). Since the motor pack runs ~1.5–1.7 hr, **the motors become the binding limit** and Thor stops eating into their runtime.

**Costs / caveats:**
- **Weight** — +2.8 kg (pack #2) + Thor (~1–1.5 kg dev kit) + its active cooler ≈ **+4–5 kg** on a ~12 kg robot; the holonomic base carries it but COM/agility suffer.
- **Cooling** — Thor at 70–130 W needs **active cooling** (its stock heatsink-fan); the paper's passive duct was sized for a 7–25 W Orin Nano.
- **PD handshake** — verify the C300 DC's 140 W port negotiates 28 V/5 A EPR with Thor's PD sink before relying on it (EPR handshakes can be finicky).
- **Fit, not feasibility** — this is a **$3,499 Thor on a ~$1.5 k robot**. Per the [compute comparison](../platforms/jetson-onboard-compute-xlerobot.md), unless you specifically need Thor's **128 GB for large/multiple VLAs**, an **Orin NX 16 GB** (10–40 W, fits the *single* existing pack, ~$600, drop-in on the Nano carrier) gets you onboard VLA inference with no second pack, no added weight, and no cooling rework.

> [!note] One pack is marginal, not impossible
> With aggressive 70 W capping, Thor (70 W) + robot (~80 W avg) ≈ 150 W is under the 300 W rate cap — so a *single* C300 DC can technically power both for light use. But energy drain + per-port contention are why the paper judged it over-budget; the second pack removes the doubt and the brownout risk.

## Summary takeaways

- **Software-cap Thor first (`sudo nvpmodel -m 3`, 70 W).** It's the cheapest win: bounds peak draw, removes surge dependence, adds ~15–25 % heavy-mode runtime, and lets a single USB-C PD feed power the compute. Cost is ~40 % GPU throughput — fine for control/perception, a real hit for GPU-bound VLA (use 90 W or accept a slower loop). See [§0](#0-the-biggest-lever--software-cap-thors-watts-nvpmodel).
- **300 W *rate* is fine** for normal operation; 600 W surge covers transients — and with a 70 W cap you're nowhere near the rail. Rate is not your constraint.
- **Two rails, capped separately**: 12 V motors + a 9–28 V Thor feed. On the C300 (A1722) you use two ports (AC/USB-C for Thor + 12 V car port for motors) — no single port gives both voltages; with a custom pack, the dual-DC-DC build above is cleaner.
- **Runtime, not rate, is the limit**: a Thor drops the XLeRobot from "10+ hr" to **~1.5–2.5 hr**. Buy **watt-hours, not watts**.
- **Prefer a DC-native pack** over an AC power station — skipping AC inversion is lighter and more efficient for a robot. See the canonical recommendation above for the regulator-into-Micro-Fit topology.
- **To put a Thor onboard, add a second C300 DC** dedicated to it (the paper's own "additional power supply" fix): Thor @ 70 W on its own 288 Wh ≈ 3.5 hr, cleanest brownout isolation, motors stay on pack #1. Costs ~+4–5 kg + active cooling, and an Orin NX 16 GB on the *single* pack is usually the better fit unless you need Thor's 128 GB. See [the two-pack option](#putting-a-jetson-thor-onboard--the-two-pack-tiered-power-option).

## Related

- [XLeRobot](../../entities/xlerobot.md) — platform (17× STS3215 @ 12 V; stock Anker C300)
- [Jetson Thor](../../entities/jetson-thor.md) — the compute being added (40–130 W module; software-capped via nvpmodel; dev kit 28 V/140 W PSU)
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — the nvpmodel power-mode source for §0
- [Onboard compute for XLeRobot — Orin Nano vs AGX Orin vs Thor](../platforms/jetson-onboard-compute-xlerobot.md) — the compute-tier side of this decision (why Thor is over-budget here)
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — independent untethered XLeRobot build; its **Tri-Bus topology** corroborates the two-rail / motor-transient problem (a 12.2 V→0.3 V brownout on the stock shared bus) and isolates the Jetson on its own rail
- [Anker C300 DC vs C300 vs C1000](../platforms/anker-portable-power-stations.md) — the power-source comparison (incl. the C300-SKU contradiction the paper surfaces)
- [XLeRobot camera options for low-light + clutter](xlerobot-camera-options-low-light.md) — sibling integration analysis
