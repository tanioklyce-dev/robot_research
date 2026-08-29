---
title: NVIDIA Jetson Linux 39.2.0 GA Release Notes (PDF)
type: source
url: https://docs.nvidia.com/jetson/archives/r39.2/ReleaseNotes/Jetson_Linux_Release_Notes_r39.2.pdf
local: ../../raw/jetson-linux-r39.2-release-notes.pdf
author: NVIDIA Corporation
published: 2026-06 (document revision RN_10698-r39.2.0)
ingested: 2026-08-17
venue: NVIDIA Jetson documentation archive
format: PDF, 27 pages
tags: [jetson, jetson-linux, l4t, r39-2, release-notes, jetpack-7, orin, thor, sbsa, flashing]
---

## Summary

The official release notes for **Jetson Linux 39.2.0 GA** — the BSP under [JetPack 7.2](nvidia-jetpack-7-2-release.md), and the release that **brings the Jetson Orin family onto the JetPack 7 line**. This is the primary the wiki's 2026-08-16 JetPack correction was missing: the [release page](nvidia-jetpack-7-2-release.md) gives the component list, but the *known issues* here are what change a flashing procedure. Three of them bear directly on this wiki's hardware recommendations — an ISO install that silently keeps the old power profile, an EMC-frequency crash that hits exactly the low-wattage modes the Orin NX is recommended for, and a capsule-update step that must be accepted or the install fails.

Kernel 6.8, UEFI bootloader, Ubuntu 24.04 rootfs, aarch64, SBSA-aligned. Release tag `jetson_39.2_GA`.

## Key claims

### Platform and release information (§1.1)

| Item | r39.2 | (r36.5 for contrast) |
|---|---|---|
| Host Linux for flashing | **Ubuntu 24.04 and 22.04** | Ubuntu 20.04 or 22.04 |
| Sample rootfs | **Ubuntu 24.04** | Ubuntu 22.04 |
| Linux kernel | **6.8** | 5.15 LTS |
| Cross-compile toolchain | **GCC 13.2** | Bootlin GCC 11.3 |
| Release tag | `jetson_39.2_GA` | `jetson_36.5` |

"This release supports the NVIDIA Jetson Thor™ and Jetson Orin platforms™" — **one BSP line for both generations**, ending the R36 (Orin) / R38 (Thor) split.

### What's new (§1.3)

- **"Adds support for the Jetson Orin product family within JetPack 7 releases."**
- `nv-load-display-modules` service updated to **manage driver differences between Orin and Thor at run time** — the mechanism by which one image serves both.
- **Native single-command NemoClaw installation** on developer kits.
- **Adds support for Jetson AGX Orin 32 GB Super Mode (MAXN_SUPER)** — the change behind the 200 → 241 TOPS figure on the [release page](nvidia-jetpack-7-2-release.md).
- **Unified ISO-based installation** for both Orin and Thor developer kits.
- Official **Yocto recipes** for Orin and Thor via the [OE4T GitHub repository](https://github.com/OE4T) (§1.4) — built from the same BSP sources as JetPack 7.2.
- **MIG on Jetson Thor T5000** as a technology preview.
- **Jetson SIPL API Package v2.0.0** — a major release unifying GMSL and CoE camera paths, with production GMSL driver support, new `nvsipl_camera` / `nvsipl_query` samples, and stereo pipeline support.

> [!warning] SIPL v2.0.0 is a breaking change for anyone carrying camera drivers forward
> §1.3 lists "significant changes from JetPack 7.1 that affect migration, including API namespace and type renames, updated JSON configuration requirements, new driver database loading behavior, changed package and installation paths, renamed sample apps, and **ABI changes requiring JetPack 7.1 UDDF drivers to be rebuilt against JetPack 7.2 headers**."

### Known issues that change a flashing or deployment decision (§3.1)

- **Issue 6266271 — the capsule-update prompt is not optional.** "When installing ISO on Orin devices with older QSPI images, it is important to allow Capsule update of the QSPI image. To trigger this, press 'y' when prompted. ISO installation continues after Capsule update is complete. **Skipping this step causes installation issues due to incompatibility of new ISO images with older QSPI images.**"
- **Issue 6279443 — the ISO install does *not* switch a unit to Super Mode.** "Jetson Orin Nano units that are updated to JetPack 7.2 using ISO install **continue to use the same profile that was set before update. Units will not default to 'Super' mode after the update.** To use 'Super' mode, you must flash the target using a Linux host or SDKM."
- **Issue 6236259 — low-wattage nvpmodel profiles can crash the system on reboot.** On Orin platforms, reducing EMC below Fmax (~3200 MHz) via `nvpmodel.service` during systemd initialization "can cause system crashes upon reboot… especially noticeable when a display is connected, regardless of its resolution." The affected modes are the *low* ones:

  | Platform | MAXN EMC | Affected power mode | Its EMC |
  |---|---|---|---|
  | AGX Orin 64 GB | ~3200 MHz | 15 W | 2133 MHz |
  | AGX Orin 32 GB | ~3200 MHz | 15 W | 2133 MHz |
  | AGX Orin Industrial | ~3200 MHz | 15 W | 2133 MHz |
  | **Orin NX 16 GB** | ~3200 MHz | **10 W** | 2133 MHz |
  | **Orin NX 8 GB** | ~3200 MHz | **10 W** | 2133 MHz |
  | **Orin Nano 8 GB** | ~3200 MHz | **7 W** | 2133 MHz |

  Workaround: switch to MAXN (restoring EMC to Fmax) *before* rebooting, then apply the desired mode after restart; if already rebooted into a bad mode, disconnect the display, boot, and reconnect.
- **Issue 5748062 — TPM hwrng costs hundreds of microseconds of real-time latency.** Mitigate by disabling `CONFIG_HW_RANDOM_TPM` (OP-TEE HWRNG takes over) or pinning the `hwrng` kernel thread to a non-RT core with `taskset`.

### MIG limitations (§3.8)

- MIG is a **technology preview**; "**MIG is currently not supported on Jetson T4000 or on the Jetson Orin Series of products**" (6230230/6230231).
- On AGX Thor, MIG is "recommended only for profiles 78 and 83 with this initial release" (6237160/6238288).
- `nvidia-smi` output is incorrect under MIG (6162096).

### Fixed issues (§4, selected)

- **PREEMPT_RT build fix**: `generic_rt_build.sh` needs `--enable EXPERT` added, "without this change, the built kernel does not have PREEMPT_RT enabled."
- The EMC-frequency-with-display crash also appears as a *fixed* issue (5763680) in a narrower form (setting EMC to e.g. 4266 MHz), while 6236259 above remains open for the low-power-mode case.
- Repeating `nvethernet` PCS block-lock kernel log spam; Wi-Fi 6 GHz WPA3 connect-after-flash; limited AP scan buffer (`wpa_cli set bss_max_count 500`).

## Entities mentioned

- [Jetson AGX Orin](../entities/jetson-agx-orin.md) — issue 6236259 hits its 15 W mode.
- [Jetson Orin NX](../entities/jetson-orin-nx.md) — issue 6236259 hits its 10 W mode.
- [Jetson Linux (L4T)](../entities/jetson-linux.md)
- [JetPack](../entities/jetpack.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [Jetson Thor](../entities/jetson-thor.md)
- [NVIDIA](../entities/nvidia.md)
- [NemoClaw](../entities/nemoclaw.md)

## Concepts touched

- Flashing / BSP update mechanics; power-mode (nvpmodel) configuration; real-time kernel latency.

## Open questions

- **Is 6236259 fixed in 7.2.1?** The 10 W Orin NX mode is the one this wiki recommends for battery robots, and the workaround (boot at MAXN, then drop) is awkward to automate on a headless robot. 7.2.1 release notes not yet ingested.
- **Does the display-connected condition mean a headless robot is safe?** The text says the crash is "especially noticeable when a display is connected," which implies it is not exclusive to that case. Not resolvable from this document.
- The release notes say "Jetson Orin product family" without a per-SKU table; the [release page](nvidia-jetpack-7-2-release.md)'s Yocto image list covers AGX Thor, AGX Orin and Orin Nano but **not Orin NX**, and that asymmetry is still unexplained.
