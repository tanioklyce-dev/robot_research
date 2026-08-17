---
title: Seeed — Flash JetPack OS to J401 Carrier Board
type: source
url: https://wiki.seeedstudio.com/reComputer_J4012_Flash_Jetpack/
author: Seeed Studio
published: undated (JetPack 7.2 image dated 2026-06-18)
ingested: 2026-08-17
venue: Seeed Studio Wiki
tags: [seeed, recomputer, j401, j4012, orin-nx, jetpack-7, flashing, carrier-board, thermals]
---

## Summary

Seeed's flashing guide for the **J401 carrier board** — the carrier under the **reComputer J4012 / Orin NX 16 GB**, which is this wiki's concrete recommendation for the [XLeRobot onboard-compute](../syntheses/platforms/jetson-onboard-compute-xlerobot.md) Orin NX tier. Ingested during the 2026-08-17 version sweep to answer the standing "Seeed carrier BSP status" question with a vendor primary rather than forum reports.

Two things matter more than the BSP version. First, **Seeed does ship a JetPack 7.2 image for the Orin NX 16 GB on J401**, dated **2026-06-18** — the carrier lag behind NVIDIA's 2026-06-01 release is about two and a half weeks, not the "weeks" the wiki previously recorded from a forum thread. Second, and unexpectedly, **Seeed tells J401 users not to enable Super Mode at all**, on thermal grounds — which puts a carrier-level ceiling under the Orin NX performance figures this wiki quotes.

## Key claims

### The JetPack 7.2 image and flow

- Prebuilt "mfi" image for the classic reComputer series: **`mfi_recomputer-orin-nx-16g-j401-7.2.0-39.2.0-2026-06-18.tar.gz`** — i.e. **JetPack 7.2.0 / Jetson Linux 39.2.0**, built 2026-06-18.
- Flow: verify SHA256 → `sudo tar xpf mfi_*.tar.gz` → `cd mfi_*` → `sudo ./tools/kernel_flash/l4t_initrd_flash.sh …` to flash **to the NVMe SSD**, with the board in force-recovery mode over USB-C.
- This is a **vendor prebuilt-image path**, not NVIDIA's unified-ISO-from-USB flow — the two coexist, and the Seeed image is what a J401 owner actually uses.
- Guide covers JP5.1.1 → JP5.1.3, JP6.0, JP6.1, JP6.2 and **JP7.2** as selectable targets. A note advises **JetPack 5.1.3 for modules with Hynix DRAM** (identifiable from chip markings).

### Host OS matrix — narrower than NVIDIA's

| JetPack | Ubuntu 18.04 | 20.04 | 22.04 | 24.04 |
|---|---|---|---|---|
| JetPack 5.x | ✅ | ✅ | | |
| JetPack 6.x | | ✅ | ✅ | |
| **JetPack 7.2** | | ✅ | ✅ | ✅ |

> "For JetPack 7.2, **Ubuntu 24.04 is supported for flashing and target-side component installation only. Use Ubuntu 20.04 or 22.04 if you need host development components.**"

Seeed also recommends **physical Ubuntu hosts over virtual machines** for flashing.

> [!note] This is stricter than the NVIDIA release notes
> [Jetson Linux 39.2 release notes](nvidia-jetson-linux-r39-2-release-notes.md) §1.1 lists the flashing host as "Ubuntu 24.04 and 22.04." Seeed adds 20.04 as usable and carves out 24.04 as flash-only. Both can be true — NVIDIA is stating what it validates, Seeed what its image needs — but a reader planning a host machine should follow the stricter line.

### The thermal warning

> **"danger — If you are using an Orin NX 16GB/8GB module, do not enable MAXN SUPER mode. The cooling capacity of the reComputer J401 carrier board is insufficient to support it."**

Seeed's product line distinguishes the **reComputer Super J4012** (marketed at **157 TOPS in Super MAXN**, and offered in the flash selector with "JetPack 6.2 with MAXN Super Mode — enhanced performance configurations now available for Orin Nano and Orin NX") from the **classic J401-based reComputer J4012**, whose flash page carries the warning above.

> [!warning] Contradiction — same module, two different sanctioned power ceilings
> Seeed markets 157 TOPS Super MAXN on the Super J4012 and forbids Super Mode on the J401. The reconciliation is that these are **different carriers with different cooling**, not different modules. Any Orin NX figure in this wiki quoted at Super Mode / 40 W therefore depends on *which* Seeed box was bought. Not independently verified here — the claim is Seeed's own, on Seeed's own product documentation.

### Other

- The default target in Seeed's device selector at ingest time is still **R36.4.3 (JetPack 6.2)** for the Super J4012 — 7.2 is available but not the presented default.
- J401 features: 1× GbE, 1× CAN, M.2 Key M (SSD), M.2 Key E (WiFi/BT), 2× CSI, 1× HDMI.

## Entities mentioned

- [Seeed Studio](../entities/seeed-studio.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md) (J3010/J3011 siblings)
- [JetPack](../entities/jetpack.md)
- [Jetson Linux (L4T)](../entities/jetson-linux.md)
- [XLeRobot](../entities/xlerobot.md)

## Concepts touched

- Carrier-board thermal limits as the real constraint on module performance modes; vendor BSP lag; prebuilt-image vs unified-ISO flashing paths.

## Open questions

- **Which Seeed SKUs can sustain Super Mode?** The Super J4012 is marketed for it; the J401 is not. Whether the Robotics J30/40 carrier (the [XLeRobot](../entities/xlerobot.md) battery-powered pick, quoted at 157 TOPS / 60 °C / 40 W) is Super-capable is not covered by this page and needs its own primary.
- **A capsule-update failure on this exact combination** ("Capsule staged 5 times but version not bumped, aborting") appears in an NVIDIA developer-forum thread for J4012/J401 on the JetPack 7.2 ISO. The mechanism is documented as issue 6266271 in the [r39.2 release notes](nvidia-jetson-linux-r39-2-release-notes.md); whether Seeed's mfi path avoids it is unverified.
- Seeed's AGX Orin 32 GB (J501) JetPack 7.2 status was an open forum question and is not answered here.
