---
title: "Does a reComputer Robotics J4012 fit on a LeKiwi base?"
type: synthesis
created: 2026-07-15
updated: 2026-07-15
tags: [lekiwi, j4012, recomputer, orin-nx, mechanical-fit, mounting, onboard-compute, xlerobot, buying-decision]
---

# Does a reComputer Robotics J4012 fit on a LeKiwi base?

Short answer: **the base plate is physically large enough to carry the J4012, and mounted correctly it need not obstruct the wheels — but it does not drop into the stock Raspberry Pi location, because the arm owns the center of the top plate.** Expect a custom riser/second-tier mount plus a separate power rail.

## The two footprints (measured, not estimated)

| | Footprint (W × D) | Height | Notes |
|---|---|---|---|
| **[LeKiwi](../../entities/lekiwi.md) base plate** | **~216 × 213 mm** | 7 mm per layer (×2 stacked) | Measured from the CAD bounding box of `3DPrintMeshes/base_plate_layer1.stl` / `layer2.stl` in the [LeKiwi repo](../../sources/lekiwi-github.md). Roughly a ~216 mm disc/rounded-triangle. |
| **[reComputer Robotics J4012](../../sources/seeed-jetson-selection-guide.md)** | **130 × 121 mm** | **66 mm** | Orin NX 16 GB Super; fan-cooled; **XT30 (2+2) 19–54 V DC** input; 6× USB 3.2 + 4-in-1 GMSL2 + 2× Eth. |
| [Raspberry Pi 5](../../entities/raspberry-pi-5.md) (stock compute) | ~85 × 56 mm | ~16 mm w/ connectors | What the base was designed around — mounts on the **second-layer top plate**. |

So the J4012's plan area is ~**2.5–3×** the Pi 5 it would replace, and it is ~4× taller.

## Wheels — clears them if it stays on the plate

The base is a 3-wheel [Kiwi drive](../../entities/lekiwi.md): **3× 4-inch (~102 mm) VEX omni wheels at 120°**, mounted at the plate edges and spinning in **vertical planes**. The obstruction risk is *overhang into a wheel's rotation plane*, not deck area.

- Center the 130 × 121 mm box on the 216 × 213 mm plate and you have **~43 mm clearance on the X edges, ~46 mm on Y** before you reach the plate rim where the wheels live. A centered top-deck box does **not** intrude on any wheel plane.
- The wheels are only obstructed if the box is (a) pushed far enough off-center to overhang one edge into a wheel sector, or (b) mounted low, down at wheel/motor level. Keep it on the upper deck and roughly centered and the wheels are fine.

**Verdict on wheels: not obstructed, with margin — provided the box is mounted on the top deck and doesn't overhang the rim.**

## The arm is the real constraint

The [SO-ARM101](../../entities/so-arm101.md) mounts **dead-center on the second-layer top plate** (4× M5×25 screws), and it needs clearance for shoulder-pan rotation and the arm folding/swinging over the base. The J4012 is **130 × 121 mm ≈ 62 % of the plate width** — it cannot share the flat top plate with the arm base and its swing arc. The stock flat single-tier layout (Pi-sized board next to the arm) does **not** scale to a box this size.

Workable mounts, in rough order of preference:

1. **Raised tier above the arm base.** Use LeKiwi's own stacking convention (3.5 mm holes on 20 mm spacing) to add a standoff-mounted upper plate carrying the J4012 *above* the arm's shoulder, clearing the swing arc. Budget the full **66 mm height** plus fan intake clearance, and keep the mass low/centered — a ~130 mm brick raised high shifts the CoG on a holonomic base ([payload/top-load dynamics are already an open question](../../entities/lekiwi.md)).
2. **Offset into one 120° wheel sector.** Slide it toward the gap between two wheels so the arm keeps the center. Risk: a 130 mm box offset far enough to clear the arm starts to overhang toward a wheel — check the specific sector geometry before committing.
3. **Underslung / lower tier.** Only if there's vertical room below the deck and above the motors; usually tighter than going up.

## Don't forget power

The J4012 wants a **19–54 V XT30 rail** ([selection guide](../../sources/seeed-jetson-selection-guide.md)) — it does **not** run off LeKiwi's **12 V STS3215 motor bus**. Mounting is only half the integration: you need a separate higher-voltage source (a battery in range, or a buck/boost stage), which is the same rail concern flagged in the [XLeRobot power-budget analysis](xlerobot-thor-power-budget.md). Fits the [onboard-compute picture](../platforms/jetson-onboard-compute-xlerobot.md) too — the J4012 is exactly the "buy-a-robot-ready-carrier" version of the Orin NX 16 GB drop-in upgrade.

## Examples in the wild — but of bare modules, not the J4012 box

Jetson-on-LeKiwi is documented and works — just not (yet) with this large carrier:

- **[alfredang/lerobot](../../sources/alfredang-lerobot-lekiwi-chatgpt.md)** — a **Jetson Orin Nano 8 GB mounted on a LeKiwi base**, explicitly replacing the Raspberry Pi; runs LeRobot + ROS 2 Humble SLAM + a GPT-4o vision loop. The closest documented onboard-Jetson stock-LeKiwi build.
- **[Cutting the Cord (Shaw et al., 2026)](../../sources/cutting-the-cord-untethered-xlerobot.md)** — the measured onboard-**Orin Nano** build, on the LeKiwi-*class* [XLeRobot](../../entities/xlerobot.md) (dual-arm / IKEA cart).
- Vendor listings (Seeed/resellers) advertise LeKiwi as **Orin NX-compatible** via the 20 mm modular mounting, but ship Pi-5-based.

**The catch that keeps this page relevant:** every documented mount uses a **bare Orin Nano module** (~Pi footprint that drops into the RPi spot) — *none* mounts the boxed **reComputer Robotics J4012** (130 × 121 × 66 mm). The real builds succeed precisely because a bare module *doesn't* trigger the arm/height conflict analyzed above; the J4012's ~2.5× footprint and 66 mm height still needs the raised-tier mount.

## Bottom line

- **Fits the base footprint?** Yes — the ~216 mm plate comfortably contains a 130 × 121 mm box.
- **Obstructs the wheels?** No, if mounted on the top deck without overhanging the rim.
- **Obstructs the arm?** Yes, in any flat layout — the arm owns the center. Needs a **raised tier (or offset sector) mount** that clears the shoulder swing and budgets the 66 mm height.
- **Plus:** wire it to its own **19–54 V** rail.

> [!note] Confidence / gaps
> Base-plate footprint and wheel size are from the LeKiwi CAD and Seeed/XLeRobot docs; the J4012 dimensions are from the [Seeed selection guide](../../sources/seeed-jetson-selection-guide.md). Not yet measured: the SO-ARM101 shoulder **swing radius / keep-out circle** at the base, and the exact wheel-well standoff height — both would let this go from "needs a riser" to a specific standoff spec. If you want that, the next step is the SO-ARM101 base CAD.

## Related
- [alfredang/lerobot](../../sources/alfredang-lerobot-lekiwi-chatgpt.md) — the documented onboard-Jetson-Orin-Nano LeKiwi build.
- [LeKiwi](../../entities/lekiwi.md) — the base (now carries measured plate dimensions + onboard-Jetson examples).
- [Onboard compute for XLeRobot — Orin Nano vs NX vs AGX Orin vs Thor](../platforms/jetson-onboard-compute-xlerobot.md) — where the J4012 sits in the Jetson ladder (the Orin NX 16 GB drop-in pick).
- [Seeed Jetson selection guide](../../sources/seeed-jetson-selection-guide.md) — J4012 dimensions, power input, interfaces.
- [XLeRobot + AGX Thor power budget](xlerobot-thor-power-budget.md) — the higher-voltage-rail concern in detail.
