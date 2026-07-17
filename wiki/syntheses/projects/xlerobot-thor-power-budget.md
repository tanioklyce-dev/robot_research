---
title: XLeRobot + AGX Thor power budget — is a 300 W battery enough?
type: synthesis
created: 2026-05-30
updated: 2026-07-17
tags: [xlerobot, jetson-thor, power, battery, anker-c300, v-mount, d-tap, sts3215, energy-budget, nvpmodel, power-modes, tiered-power, projects]
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

## 3b. Thor-only runtime — one 140 W USB-C feed

The numbers above are the **whole robot** (Thor + motors + sensors). The isolated question — *how long does a **T5000 Thor alone** run on a dedicated 288 Wh pack fed from a single 140 W USB-C port* (a USB-C→DC PD-140 W cable) — is the [two-pack option](#putting-a-jetson-thor-onboard--the-two-pack-tiered-power-option)'s pack #2, and the runtime is set entirely by the `nvpmodel` cap.

**Usable energy:** 288 Wh × ~85–90 % (DC→USB-C PD conversion + real-world cutoff) ≈ **~250 Wh** at the port. A PD-trigger→DC cable passing 28 V/5 A adds little loss (Thor's onboard buck is already in its rated draw).

**Runtime = ~250 Wh ÷ actual board draw** (module cap + ~10–20 W dev-kit peripherals: NVMe, fan, Wi-Fi, USB):

| `nvpmodel` | Module cap | Board draw* | Thor-only runtime |
|---|---|---|---|
| Idle / light inference | ~30–40 W | ~45–55 W | **~4.5–5.5 hr** |
| **Mode 3 — 70 W** (battery default) | 70 W | ~85 W | **~3–3.5 hr** |
| **Mode 2 — 90 W** | 90 W | ~105 W | **~2.4 hr** |
| **Mode 1 — 120 W** (default) | 120 W | ~135 W | **~1.9 hr** |
| Mode 0 — MAXN | up to 130 W → **168 W board** | — | ❌ **not on one 140 W port** |

\*Module-only draw (ignoring peripherals) gives the optimistic bound the two-pack section quotes — **70 W ≈ 3.5 hr, 120 W ≈ 2 hr**; peripherals trim ~15–20 %. A typical **VLA-inference workload** averages a mid mode → **~2.5–3.5 hr**.

> [!warning] One 140 W USB-C port caps you below MAXN
> Thor's board can pull up to **168 W** at full tilt, but USB-C PD sink is hard-limited to **140 W** (§2) — an uncapped/full-load Thor **browns out on a single port**. Stay at `nvpmodel ≤ 120 W`; **70–90 W gives comfortable headroom** after peripherals. To run unthrottled you must feed the **Micro-Fit** (15 A / 168 W) instead — see the [canonical battery recommendation](#updated-battery-recommendation-canonical). Replicating the stock config: the bundled 28 V/5 A brick is USB-C and has the same 140 W limit, so you're not losing performance you otherwise had — just running it off a battery.

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

## V-mount / D-Tap batteries — the direct-voltage option

A **V-mount (V-lock) cine battery** is the cleanest off-the-shelf way to feed Thor, because it **already outputs the right voltage**. A V-mount's **D-Tap** port delivers *unregulated battery voltage* — for a 14.8 V-nominal Li-ion pack that's ~16.8 V full → ~12 V at cutoff, a range that sits **entirely inside Thor's 9–28 V window**. So a **D-Tap → Micro-Fit 3.0 cable feeds Thor directly**, with two advantages over the §"Updated battery recommendation" regulator path:

1. **No DC-DC regulator needed** — 14.8 V is already in-window (contrast the canonical build's ~20 V buck). Fewer parts, no conversion loss.
2. **It goes into Micro-Fit, so it bypasses the USB-C 140 W cap** — a D-Tap→Micro-Fit feed can carry the **full 168 W**, unlike any USB-C-PD battery (including the C300's 140 W port, §2/§3b).

This is a well-trodden path for Jetson generally — [JetsonHacks has a dedicated V-mount-for-Jetson guide](https://jetsonhacks.com/2024/05/23/v-mount-battery-to-power-nvidia-jetson-electronics-projects/) (the same channel behind the wiki's [Claude-Code-on-Jetson demo](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md)).

> [!note] Inherently safe against the 28 V ceiling
> A single 14.8 V-nominal pack tops out at ~16.8 V charged — **well under Thor's 28 V input limit**, so unlike a 6S/7S Li-ion or 8S LiFePO4 pack (the §"28 V ceiling trap"), a V-mount is **safe to direct-feed with no regulator**. Do *not* series two V-mounts into 29.6 V.

### Size by continuous current, not just watt-hours

The catch is the **D-Tap current rating**. At 14.8 V nominal, 168 W ≈ 11.4 A — and because Thor is a constant-*power* load, the current *rises as the pack sags* (168 W ÷ 12 V cutoff = 14 A). So **only a 15 A-rated pack holds the full 168 W across the whole discharge.** A 10 A pack (e.g. the mini **Moman Power 95**, 95 Wh) tops out ~148 W and will trip its over-current protection under MAXN; a 12 A pack is marginal at 168 W (fine if you cap Thor ≤120–140 W).

| Battery | Capacity | Cont. current | Max out | Runtime @ 120 W | Notes |
|---|---|---|---|---|---|
| Moman Power 95 | 95 Wh | 10 A | ~148 W | ~0.7 hr | **Under-rated for 168 W** — cap Thor ≤120 W; airline-legal |
| **Moman Power 99** | 99 Wh | **15 A** | 200 W | ~0.75 hr | Same mini form factor as the 95 but clears 168 W; adds 65 W USB-C; airline-legal (<100 Wh) |
| **SHAPE Mini 150 Wh** | 150 Wh | **15 A** | 216 W | ~1.1 hr | Twist D-Tap + USB-C in/out |
| FXLION Square BP-M200 | 198 Wh | 12 A | ~170 W | ~1.5 hr | Marginal at full 168 W — comfortable to ~140 W |
| **Watson VM-230-SP** | 230 Wh | **15 A** | ~216 W | ~1.7 hr (~1.2 hr @ 168 W) | Ground-use only (>160 Wh) |
| **FXLION High-Power (265 Wh+)** | 265 Wh+ | **15 A** sustained | 222 W | ~2.0 hr | Max headroom + runtime; ground-use only |

*(Runtime = ~90 % of Wh ÷ draw.)* Airline note: **>100 Wh needs carrier approval; >160 Wh is generally barred from flights** — the 99 Wh packs are the only travel-legal ones here.

### High-voltage (26 V) V-mounts — most runtime, but they need a buck

A separate cine-battery class runs at **26 V nominal** (e.g. **IndiPRO Micro-Series 26 V 260 Wh**, **FXLION BP-7S230 230 Wh / BP-7S270 270 Wh**). These are the **largest-capacity, highest-current** V-mounts here — but they are **7S Li-ion**, which means:

> [!warning] A charged 26 V pack is ~29.4 V — over Thor's 28 V limit. Do NOT direct-feed.
> Both use a **29.4 V charger** (IndiPRO 29.4 V/2.5 A; FXLION 29.4 V/5 A), confirming 7S chemistry: full charge **29.4 V**, sagging to ~21 V at cutoff. The top of that range **exceeds Thor's 28 V `VCC_SRC` ceiling** — this is the §"28 V ceiling trap" made concrete. Unlike a 14.8 V pack, **you cannot wire the 26 V D-Tap straight into Micro-Fit** — a full pack would over-volt Thor.

The fix is the one from the §"Updated battery recommendation": put a **DC-DC buck between the 26 V D-Tap and Micro-Fit, fixed at ~20 V** (or ≤24 V). With that regulator these become **the best V-mount option for Thor** — in effect the canonical "24 V-class pack + buck → Micro-Fit" build delivered as a hot-swappable cine battery. Bonus: at 26 V the load current is low (168 W ÷ 26 V ≈ 6.5 A), so wiring and connector heating are easy; the buck's ~20 V output draws ~8.4 A.

| Battery | Capacity | Cont. current | D-Tap for Thor's 168 W? | Runtime @ 120 W | Notes |
|---|---|---|---|---|---|
| **FXLION BP-7S270** | 270 Wh | 10 A norm / **15 A** max | ✅ D-Tap outputs 26 V @ 10–15 A directly | **~2.0 hr** (~1.4 hr @ 168 W) | Best runtime; native high-current D-Tap. Ground-use only |
| **FXLION BP-7S230** | 230 Wh | 10 A / **15 A** | ✅ same | ~1.7 hr (~1.2 hr @ 168 W) | Smaller sibling |
| **IndiPRO Micro-Series 26 V** | 260 Wh | **15 A** (via plate) | ⚠️ **built-in D-Tap only 4.1 A / 50 W** — needs a V-mount *plate* with a ~10 A direct-terminal D-Tap | ~1.9 hr (~1.3 hr @ 168 W) | Big capacity, but its own D-Tap is too weak for Thor; budget an extra plate |

**Verdict:** all three beat the 14.8 V packs on capacity/runtime and can deliver the full 168 W — **but only through a buck regulator** (their charged 29.4 V rules out direct-feed). Between them, the **FXLION BP-7S270** is the cleanest (native 15 A D-Tap, most Wh); the **IndiPRO** matches on capacity but its 50 W built-in D-Tap forces you to add a V-mount plate to reach Thor's current. If you'd rather skip the regulator entirely, stay with a **14.8 V, 15 A pack** (previous table) and accept less runtime.

### When to pick a V-mount over the canonical dual-DC-DC build

- **A 14.8 V V-mount** wins for **maximum simplicity + a self-contained Thor pack**: **no regulator** (direct D-Tap→Micro-Fit), hot-swappable, standard cine chargers, and it can hit full 168 W with a 15 A pack. Best when Thor is the *only* thing on it (like the [two-pack option](#putting-a-jetson-thor-onboard--the-two-pack-tiered-power-option)'s pack #2) — its 14.8 V rail doesn't match the 12 V motor bus, so it's not a one-pack-both-rails solution.
- **A 26 V V-mount (+ buck)** wins for **most runtime in a cine form factor** — but it *does* need the regulator (29.4 V charged > 28 V), so it's the canonical build with a hot-swappable pack, not a simpler one.
- **The §canonical 24 V-pack + dual-DC-DC build** wins when you want **one pack driving both rails** (20 V → Thor, 12 V → motors) at higher efficiency.

Still required either way: a **fabricated D-Tap → Micro-Fit 3.0 (2×2, 3.0 mm) cable** — none exists off-the-shelf for Thor yet — polarity-correct, and it remains **off-label** vs NVIDIA's "bundled PSU only" guidance.

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
- **A V-mount / D-Tap cine battery is the simplest off-the-shelf Thor feed** — its 14.8 V D-Tap is already inside the 9–28 V window (no regulator) and goes into Micro-Fit (so it can reach the full 168 W, unlike USB-C). Size by **continuous current — a 15 A pack** to hold 168 W; the 10 A mini Moman Power 95 falls short. For **most runtime**, a **26 V cine pack** (FXLION BP-7S270 270 Wh, IndiPRO 260 Wh) is biggest — but it charges to 29.4 V, so it **needs a buck** (can't direct-feed like 14.8 V). See [§V-mount / D-Tap](#v-mount--d-tap-batteries--the-direct-voltage-option).
- **To put a Thor onboard, add a second C300 DC** dedicated to it (the paper's own "additional power supply" fix): Thor @ 70 W on its own 288 Wh ≈ 3.5 hr, cleanest brownout isolation, motors stay on pack #1. Costs ~+4–5 kg + active cooling, and an Orin NX 16 GB on the *single* pack is usually the better fit unless you need Thor's 128 GB. See [the two-pack option](#putting-a-jetson-thor-onboard--the-two-pack-tiered-power-option).

## Related

- [XLeRobot](../../entities/xlerobot.md) — platform (17× STS3215 @ 12 V; stock Anker C300)
- [Jetson Thor](../../entities/jetson-thor.md) — the compute being added (40–130 W module; software-capped via nvpmodel; dev kit 28 V/140 W PSU)
- [Jetson Thor Platform Power & Performance (R38.4)](../../sources/nvidia-jetson-thor-platform-power-performance.md) — the nvpmodel power-mode source for §0
- [Onboard compute for XLeRobot — Orin Nano vs AGX Orin vs Thor](../platforms/jetson-onboard-compute-xlerobot.md) — the compute-tier side of this decision (why Thor is over-budget here)
- [Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md) — independent untethered XLeRobot build; its **Tri-Bus topology** corroborates the two-rail / motor-transient problem (a 12.2 V→0.3 V brownout on the stock shared bus) and isolates the Jetson on its own rail
- [Anker C300 DC vs C300 vs C1000](../platforms/anker-portable-power-stations.md) — the power-source comparison (incl. the C300-SKU contradiction the paper surfaces)
- [JetsonHacks — V-mount battery to power NVIDIA Jetson](https://jetsonhacks.com/2024/05/23/v-mount-battery-to-power-nvidia-jetson-electronics-projects/) — external primary reference for the §V-mount/D-Tap option; same channel as the wiki's [Claude-Code-on-Jetson demo](../../sources/jetsonhacks-ai-coding-jetson-claude-code.md)
- [XLeRobot camera options for low-light + clutter](xlerobot-camera-options-low-light.md) — sibling integration analysis
