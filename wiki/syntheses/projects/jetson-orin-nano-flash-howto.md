---
title: Jetson Orin Nano — flash Jetson OS to NVMe SSD howto
type: synthesis
created: 2026-05-16
updated: 2026-05-16
tags: [jetson, hardware, setup, howto]
---

# Jetson Orin Nano — flash Jetson OS to NVMe SSD

Operational howto for writing a [Jetson Linux](../../entities/jetson-linux.md) (L4T) image to an NVMe SSD on a **[Jetson Orin Nano](../../entities/jetson-orin-nano.md) Developer Kit** so the device boots from the SSD instead of microSD. Path-A recovery procedure and host requirements follow NVIDIA's official guide ([Jetson Orin Nano Dev Kit software setup](../../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)); the apt-update vs reflash distinction follows the L4T BSP update mechanism ([Jetson Linux R36.5 update mechanism](../../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)). Current production target is **[JetPack 6.2.2](../../sources/nvidia-jetpack-6-2-2-release.md)** (Jetson Linux 36.5).

> [!note]
> Steps below assume the NVIDIA Dev Kit. A custom carrier board (e.g., Hiwonder [ROSOrin Pro](../../entities/rosorin-pro.md), Seeed reComputer) ships its own BSP overlay and may have different recovery-pin locations and flash configs — check the carrier vendor's docs.

## Prerequisites

- Jetson Orin Nano Developer Kit with NVMe M.2 SSD installed in the on-board slot.
- USB-C cable (data-capable, not power-only) from Jetson to host.
- Barrel-jack 5 V / 4 A power supply (do **not** flash off USB-C power — a power blip mid-write can brick the board).
- Ubuntu host: **20.04 or 22.04 x86_64**, 8 GB RAM, 25 GB free disk. The user-guide chapter only lists 20.04 ([software setup](../../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)) but the R36.5 release notes officially support both ([release notes §1.1](../../sources/nvidia-jetson-linux-r36-5-release-notes.md)). WSL will not work (no native USB-recovery passthrough); a VM with USB passthrough can work but is fiddly.

## Path A — NVIDIA SDK Manager (recommended for first-timers)

1. Install SDK Manager on the Ubuntu host from <https://developer.nvidia.com/sdk-manager>.
2. Put the Jetson in **force-recovery mode**:
   - Power off.
   - Jumper pins **9 (GND) and 10 (FC REC)** on the button header (J14), *or* hold the FC REC button while applying power.
   - Connect Jetson USB-C → host. Verify with `lsusb` — should show `0955:7523 NVIDIA Corp.`.
3. Launch SDK Manager, log in, choose **JetPack 6.x** (or current). Under Target Components / Storage device, select **NVMe**. Untick DeepStream and other add-ons unless needed.
4. Run. SDK Manager flashes the QSPI bootloader to internal QSPI and the L4T rootfs to NVMe. ~30–45 min.
5. When prompted, remove the recovery jumper, power-cycle. First-boot Ubuntu setup runs off the SSD.

## Path B — Command-line flash

For headless hosts or repeatable builds:

```bash
cd ~ && mkdir jetson && cd jetson
# Download the BSP + sample rootfs tarballs matching your JetPack version from
# https://developer.nvidia.com/embedded/jetson-linux-archive
tar xpf jetson_linux_*_aarch64.tbz2
cd Linux_for_Tegra/rootfs
sudo tar xpf ../../tegra_linux_sample-root-filesystem_*.tbz2
cd ..
sudo ./apply_binaries.sh
sudo ./tools/l4t_flash_prerequisites.sh   # one-time on host

# With Jetson in recovery mode and USB-C plugged in:
sudo ./tools/kernel_flash/l4t_initrd_flash.sh \
    --external-device nvme0n1p1 \
    -c tools/kernel_flash/flash_l4t_external.xml \
    -p "-c bootloader/t186ref/cfg/flash_t234_qspi.xml" \
    --showlogs --network usb0 jetson-orin-nano-devkit internal
```

Flashes QSPI bootloader to internal flash and rootfs to `/dev/nvme0n1`.

## Gotchas

- **Older dev kits (pre-mid-2023)** shipped with a QSPI bootloader that cannot see NVMe. Both paths above update the bootloader, but you cannot skip the QSPI flash step and only copy a rootfs to the SSD — the bootloader update is mandatory.
- **Power source**: 5 V / 4 A barrel jack only during flashing. USB-C PD is not reliable enough.
- **Don't unplug** the recovery USB cable mid-flash.
- If `lsusb` doesn't show the NVIDIA device after entering recovery mode, the jumper isn't seating correctly or the cable isn't data-capable.
- Custom carrier boards (e.g., [ROSOrin Pro](../../entities/rosorin-pro.md)) override the flash config — `jetson-orin-nano-devkit` is the wrong target for those; use the vendor's BSP and config.
- **Multi-boot-media versions must match** ([R36.5 release notes §2.1](../../sources/nvidia-jetson-linux-r36-5-release-notes.md), issue 4201479): flashing different BSP versions to USB + NVMe + SD corrupts UEFI overlay partitions and crashes the system. Reflash all boot media together.
- For more performance, use **`jetson-orin-nano-devkit-super.conf`** instead of `jetson-orin-nano-devkit.conf` — unlocks 25 W and MAXN_SUPER on Orin Nano modules ([Platform Power and Performance — Orin series](../../sources/nvidia-jetson-platform-power-performance-orin.md)). For sustained MAXN_SUPER workloads use `jetson-orin-nano-devkit-super-maxn.conf` (more conservative thermals). The Path B command above passes the standard config; swap basenames for Super Mode. **Super Mode is hardware-locked at flash time** — you can't enable it later without reflashing.
- If `l4t_initrd_flash.sh` previously failed near completion with "Either the device cannot mount the NFS server..." — that bug was **fixed in R36.5** (issue 4695663).

## Alternative — microSD boot, then migrate to NVMe

If you want to avoid host-side flashing entirely, you can write the official microSD image to a card, boot from it, then run NVIDIA's `nvme_install.sh` script to copy rootfs to NVMe and switch boot device. Still requires the QSPI bootloader to support NVMe — same pre-mid-2023 caveat applies. Note that NVIDIA currently ships an SD image at **JetPack 6.2.1 / Jetson Linux 36.4.4**; apt-upgrade to JetPack 6.2.2 / Jetson Linux 36.5 after first boot ([JetPack 6.2.2 release](../../sources/nvidia-jetpack-6-2-2-release.md), [R36.5 update mechanism](../../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)).

## After flashing — switching power modes

Once the Jetson is booted, change power modes at runtime ([Platform Power and Performance — Orin series](../../sources/nvidia-jetson-platform-power-performance-orin.md)):

```bash
sudo /usr/sbin/nvpmodel -q             # query current mode
sudo /usr/sbin/nvpmodel -m <mode-id>   # set
```

Mode persists across reboots. **Mode IDs are not portable across modules** — on an 8GB Orin Nano flashed with the `-super` config, mode 1 = Super 25W and mode 2 = MAXN_SUPER; on a 4GB Orin Nano those IDs land on different modes. See [the entity page](../../entities/jetson-orin-nano.md) for the headline 8GB table.

## Updating an existing install

Once running, in-place updates use apt against NVIDIA's L4T Debian repo:
- **Point release** (e.g. 36.4 → 36.5): `sudo apt update && sudo apt upgrade`.
- **Minor release**: edit `/etc/apt/sources.list.d/nvidia-l4t-apt-source.list` to target the new release, then `sudo apt update && sudo apt dist-upgrade`.
- **Major release** (e.g. JetPack 5 / L4T 35.x → JetPack 6 / L4T 36.x): **not supported via apt — full reflash via SDK Manager or `l4t_initrd_flash.sh` is required** ([R36.5 update mechanism](../../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)).

The `nvidia-l4t-bootloader` package carries QSPI bootloader payloads, so apt upgrades within a release line do update bootloader firmware. Mixing packages across releases is explicitly discouraged; the system blocks partial upgrades by enforcing `nvidia-l4t-core` version-match across all Jetson packages.

## Related

- [ROSOrin Pro](../../entities/rosorin-pro.md) — Hiwonder humanoid arm built around a Jetson Orin Nano on a custom carrier; flashing path differs.
- [JEPA project ladder for ROSOrin Pro](jepa-project-ladder-rosorin-pro.md) — projects that assume a working Jetson.
- [ROSOrin Pro — Lego pick-and-place project plan](rosorin-pro-lego-pick-place.md) — same.
