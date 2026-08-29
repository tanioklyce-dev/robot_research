---
title: NVIDIA Jetson Linux 36.5 Release Notes (PDF)
type: source
url: https://docs.nvidia.com/jetson/archives/r36.5/ReleaseNotes/Jetson_Linux_Release_Notes_r36.5.pdf
local_path: raw/jetson-linux-r36.5-release-notes.pdf
sha256: fa13ad1034165e06e70003b62eb6dcce2dfc85d95c7ad9a7b77f8fe75a8e981b
local: ../../raw/jetson-linux-r36.5-release-notes.pdf
author: NVIDIA Corporation
published: 2026-02 (document revision RN_10698-r36.5.0)
ingested: 2026-05-16
tags: [jetson, jetson-linux, l4t, r36-5, release-notes, jetpack-6, uefi, super-mode]
---

## Summary
The 17-page official release notes for **Jetson Linux 36.5 GA**. Document-revision date February 2026 — this is the version that explicitly pairs R36.5 with **JetPack 6.2.2**. R36.5 itself is positioned as a **security-focused minor release** ("includes security-related fixes"); there are no headline feature additions. The substance is in the platform-and-release table (config files, module part numbers, host OS, toolchain) and the **Fixed Issues** section (UEFI assertion that previously required a full reflash, intermittent initrd-flash failure, CUDA-memory regression after a 6.4.4 → 6.4.7 apt upgrade). Also surfaces operational constraints (GPIO sysfs deprecated, no plugin manager under UEFI, can't mix BSP versions across boot media).

## Key claims

### Platform & release table (§1.1)
- **Host OS for flashing**: Ubuntu x64 **20.04 or 22.04** (both officially supported per release notes — the user-guide chapter lists only 20.04).
- **Sample rootfs**: Ubuntu 22.04.
- **Linux kernel**: 5.15 LTS.
- **Architecture**: aarch64.
- **Toolchain**: Bootlin **GCC 11.3** for cross-compilation.
- **Release tag**: `jetson_36.5`.

### Flash configuration files (§1.1)
The `.conf` basenames used with `flash.sh` and the modules each targets — material for anyone scripting flashes:

| Config | Modules | Notes |
|---|---|---|
| `jetson-orin-nano-devkit.conf` | Orin Nano 8GB (P3767-0003), 4GB (P3767-0004), SD-Card dev kit (P3767-0005), Orin NX 16GB (P3767-0000), Orin NX 8GB (P3767-0001) | Standard power modes; Orin Nano Carrier P3768-0000 |
| `jetson-orin-nano-devkit-super.conf` | Same module list | **Super Mode** — boosted: 25W Orin Nano, 40W Orin NX, MAXN for all |
| `jetson-agx-orin-devkit.conf` | AGX Orin dev-kit module (P3701-0000), AGX Orin 32GB (P3701-0004), 64GB (P3701-0005) | AGX Orin reference carrier P3737-0000 |
| `jetson-agx-orin-devkit-industrial.conf` | AGX Orin Industrial (P3701-0008) | Same P3737-0000 carrier |

> [!note]
> "Some of the products require flashing through initrd instead of `flash.sh`." NVMe / USB / SD-card targets typically use `l4t_initrd_flash.sh`.

### What's New (§1.3) — verbatim characterization
- "Jetson Linux 36.5 is the latest production-quality Jetson Linux minor release that supports NVIDIA JetPack™ 6.2.2, which includes security-related fixes."
- Jetson Linux Sources also on Git in addition to the Jetson Linux page.
- Pointer to *Jetson Module Adaptation and Bringup* for custom carrier boards.

### Known issues (§2)

**General system usability:**
- **GPIO sysfs deprecated**: `/sys/class/gpio` no longer works. Use the GPIO character-device API (`libgpiod`).
- **Multi-boot-media constraint** (issue 4201479): Jetson Linux supports flashing the BSP to multiple boot media (USB / NVMe), but all media must carry the **same** BSP version — mixing versions corrupts UEFI overlay partitions and crashes the system.
- AGX Orin: some bundled USB cables produce `Cannot enable. Maybe the USB cable is bad?` errors — swap cables.

**Flashing:**
- On Ubuntu 18.04 host, `apply_binaries.sh` shows `qemu: Unsupported syscall: 293` — typically harmless; reinstall `qemu-user-static` to suppress.
- Some hosts hit `Cannot enable. Maybe the USB cable is bad?` during flash — try different USB port / cable / reboot host.

**Camera:**
- HAWK Stereo (AR0234): first captured frame is dark with argus apps.
- `v4l2-utils`: `VIDIOC_G/S_PARM` fails v4l2-compliance.
- DOL HDR sensors: marginal noise increase.

**Display:**
- Hotplugging DP after boot on AGX Orin may corrupt the screen.
- xrandr sees a secondary display as connected but `gdm` isn't rendered on it.
- CableCreation-branded DP-to-HDMI converter doesn't work; use a different one.
- Vulkan re-run fails after killing the app; VT switch doesn't take while Vulkan D2D apps run.

**Compute stack:**
- **VPI PVA in Docker requires the same VPI version on the host** as in the container. Cross-version PVA calls inside a container will fail.

### Fixed issues (§3) — operationally significant
- **Initrd-flash near-completion failure** (4695663): "Either the device cannot mount the NFS server on the host or a flash command has failed." Hit anyone using `l4t_initrd_flash.sh` for NVMe/USB/SD targets — **fixed in 36.5**. Material for the [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md).
- **UEFI assertion during boot** (5412830): previously intermittent; the device would stop at bootloader and require a full firmware reflash to recover. Fix addressed `StandaloneMM` variable-storage and block-erase logic.
- **CUDA memory regression after JetPack 6.4.4 → 6.4.7 apt upgrade** (5602402): `unable to allocate CUDA0 buffer`. Two-part fix: NvMap allocation policy + multi-thread allocation-exceeding-capacity hang.
- **GStreamer h264parse missing on R36.5 Ubuntu 22.04 desktop images** (5842995): `gstreamer1.0-plugins-bad` is no longer pre-installed (FFMPEG GPL licensing). Manual `sudo apt install gstreamer1.0-plugins-bad` required — not a "fix" so much as a documented gotcha.
- Wake-on-LAN: enabling `wol g` no longer immediately disconnects the network on AGX Orin; WOL config now deferred to suspend.
- argus_camera JPEG parameter mismatch ("library thinks size is 584, caller expects 728"); MJPEG bitstream allocation; deinterlace support added.

### Implementation details (§4)

**Camera (§4.1):**
- Sensor kernel drivers live in `<TOP>/kernel/nvidia-oot/drivers/media/i2c/`.
- **Recommendation**: "all camera drivers be packages like Loadable Kernel Module (LKM) for JetPack 6 and later" — module artifacts under `/lib/modules/5.15.116-release-tegra/extra/...`.

**Device registration (§4.2):**
- "Because **UEFI boot is enabled in this release, the plugin manager is no longer supported.**" Camera/peripheral registration must use **device tree overlays** (`.dtbo`) — full DTS example for Dual-IMX274 in the doc.
- Two paths: with on-board EEPROM (overlay applied at runtime by camera ID) or via the **Jetson-IO tool** (place `.dtbo` in `/boot`, run tool).

**UEFI (§4.3):**
- NVIDIA maintains the UEFI source on **GitHub** publicly; post-release fixes go there.

## Entities mentioned
- [Jetson Linux](../entities/jetson-linux.md)
- [JetPack](../entities/jetpack.md)
- [Jetson Orin Nano](../entities/jetson-orin-nano.md)
- [NVIDIA](../entities/nvidia.md)

## Concepts touched
- None directly.

## Open questions
- What is **Super Mode**? The notes reference "Supported Modes and Power Efficiency" in the Developer Guide. Worth following up — the 25W Orin Nano / 40W Orin NX / MAXN unification reads like the same package as the late-2024 "Orin Nano Super" performance unlock. Targeted ingest of the Developer Guide section would close this.
- The CUDA-memory regression was specifically on 6.4.4 → 6.4.7 apt upgrade — not 6.2.x. Need to verify whether the 6.2 line was affected and whether the fix landed before or in 36.5.
- Which exact QSPI bootloader payload version ships in `nvidia-l4t-bootloader` for R36.5? The notes don't say; the manifest is probably in the BSP archive.
- UEFI GitHub repo URL not embedded in the PDF text — likely `NVIDIA/edk2-nvidia` or similar; pin in a follow-up ingest.
