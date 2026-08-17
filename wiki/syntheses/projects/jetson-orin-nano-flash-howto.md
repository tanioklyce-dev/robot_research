---
title: Jetson Orin Nano — flash Jetson OS to NVMe SSD howto
type: synthesis
created: 2026-05-16
updated: 2026-08-16
tags: [jetson, hardware, setup, howto, uefi, efibootmgr, boot-order]
---

# Jetson Orin Nano — flash Jetson OS to NVMe SSD

Operational howto for writing a [Jetson Linux](../../entities/jetson-linux.md) (L4T) image to an NVMe SSD on a **[Jetson Orin Nano](../../entities/jetson-orin-nano.md) Developer Kit** so the device boots from the SSD instead of microSD. Path-A recovery procedure and host requirements follow NVIDIA's official guide ([Jetson Orin Nano Dev Kit software setup](../../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)); the apt-update vs reflash distinction follows the L4T BSP update mechanism ([Jetson Linux R36.5 update mechanism](../../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)). Current production target is **[JetPack 6.2.2](../../sources/nvidia-jetpack-6-2-2-release.md)** (Jetson Linux 36.5).

This page also covers **SD-primary with NVMe fallback** (UEFI auto-fallback) — see the section below.

> [!warning] Correction 2026-08-16 — this howto describes the **JetPack 6** flow, and JetPack 7.2 changed it
> **From JetPack 7.2 (2026-06-01) the Orin Nano Developer Kit has no downloadable SD-card image.** The flow is now a **unified ISO written to a USB stick**, which then installs Jetson Linux onto microSD *or* NVMe — NVIDIA's own guidance is *"do not flash the Jetson ISO to a microSD card."* The ISO defaults to **Super Mode** flashing configuration. **JetPack 7.2.1** shipped 2026-08-12.
>
> So: the SDK-Manager and `l4t_initrd_flash.sh` paths below remain valid for the JetPack 6 / L4T 36.x line, and the **microSD-image path in the "avoid host-side flashing" section no longer exists on JetPack 7.2**. Anything on this page that assumes an SD image is JetPack-6-only. Also note the major-release rule at the bottom applies again: **JetPack 6 → 7 is not an apt upgrade; it is a full reflash.**
>
> Primary source now ingested: **[JetPack 7.2 / Jetson Linux 39.2](../../sources/nvidia-jetpack-7-2-release.md)** (2026-06-02; CUDA 13.2.1, TensorRT 10.16.2). Two things from it to carry into any 7.x flash: **manual flashing steps changed for SBSA reasons**, and NVIDIA ships **`overlay_pcie.tbz2`**, which *"fixes an intermittent boot issue caused by initialization failures on some Jetson Orin Nano and Orin NX modules during power cycles or reboots."* **This page still documents the JetPack 6 procedure and has not been re-derived against 7.2.**

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

### Community wrapper — JetsonHacks `bootFromExternalStorage`

The [**jetsonhacks/bootFromExternalStorage**](https://github.com/jetsonhacks/bootFromExternalStorage) toolkit wraps the same `l4t_initrd_flash.sh` workflow Path B invokes, with helper scripts that handle the host-side BSP / rootfs downloads, signing-key generation, and flash config. Useful when:

- You'd rather run `./get_jetson_files.sh && ./flash_jetson_external_storage.sh` than assemble the `l4t_initrd_flash.sh` command line by hand.
- You want a single script that works across recent JetPack 5.x / 6.x versions on the Orin Nano / NX / AGX Orin Dev Kits and external NVMe + USB targets.
- You're already familiar with the JetsonHacks tutorials and want consistency with their other Jetson setup scripts.

It produces the same end state as Path B (QSPI bootloader + rootfs on external storage); same caveats apply (modern QSPI required, multi-boot-media versions must match, etc.).

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

## SD-primary with NVMe fallback (UEFI auto-fallback)

A different boot configuration from the "flash NVMe instead of SD" paths above: keep the microSD as the primary boot device, but have UEFI **automatically fall through to NVMe when the SD has no boot partition** (or has been pulled). This is the right setup if you want SD-card-based development with a recoverable NVMe backup of the OS.

### How it works

R36.5 uses a **UEFI firmware** with a `BootOrder` variable in NVRAM. UEFI walks the boot entries in order; **if an entry's bootloader is missing or its `extlinux.conf` is absent, UEFI silently moves to the next entry.** So "SD if bootable, else NVMe" reduces to: (1) make both bootable; (2) put SD first in `BootOrder`.

### Prerequisite — modern QSPI bootloader

The QSPI bootloader must be new enough to enumerate NVMe. **Pre-mid-2023 dev kits cannot see NVMe** at all from the QSPI bootloader stage (see Gotchas above). Confirm with:

```bash
sudo efibootmgr -v
```

If no NVMe-capable boot entry appears, update the bootloader within your JetPack 6.x line:

```bash
sudo apt update
sudo apt install --reinstall nvidia-l4t-bootloader
sudo reboot
```

If apt won't pull a Jetson with new-enough firmware (true for the very oldest QSPI), reflash from a host using the Path B `l4t_initrd_flash.sh` command above — that flashes both QSPI and the rootfs.

### Step 1 — Install Jetson OS on the NVMe (from the running SD system)

The easiest path uses NVIDIA's bundled tool:

```bash
sudo /opt/nvidia/l4t-bootloader-config/nvme_install.sh
```

This clones the running rootfs to NVMe, partitions it (GPT + ESP + ext4 rootfs), installs kernel + `extlinux.conf`, and registers an EFI boot entry.

If `nvme_install.sh` isn't on your install (varies by BSP variant), the manual path:

```bash
# 1. Partition NVMe — GPT + small ESP + ext4 rootfs
sudo parted -s /dev/nvme0n1 mklabel gpt
sudo parted -s /dev/nvme0n1 mkpart ESP fat32 1MiB 513MiB
sudo parted -s /dev/nvme0n1 set 1 esp on
sudo parted -s /dev/nvme0n1 mkpart rootfs ext4 513MiB 100%
sudo mkfs.fat -F32 /dev/nvme0n1p1
sudo mkfs.ext4   /dev/nvme0n1p2

# 2. Mount and rsync the running rootfs
sudo mkdir -p /mnt/nvme
sudo mount /dev/nvme0n1p2 /mnt/nvme
sudo rsync -aAXHv \
    --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found","/boot/efi/*"} \
    / /mnt/nvme/

# 3. Copy the ESP
sudo mkdir -p /mnt/nvme/boot/efi
sudo mount /dev/nvme0n1p1 /mnt/nvme/boot/efi
sudo rsync -aAXHv /boot/efi/ /mnt/nvme/boot/efi/

# 4. Rewrite NVMe's /etc/fstab and extlinux.conf to point at its own UUIDs
NVME_ROOT_UUID=$(sudo blkid -s UUID -o value /dev/nvme0n1p2)
NVME_ESP_UUID=$(sudo blkid -s UUID -o value /dev/nvme0n1p1)
sudo sed -i "s|UUID=[^ ]* */ |UUID=$NVME_ROOT_UUID / |" /mnt/nvme/etc/fstab
sudo sed -i "s|UUID=[^ ]* */boot/efi|UUID=$NVME_ESP_UUID /boot/efi|" /mnt/nvme/etc/fstab
sudo sed -i "s|root=[^ ]*|root=UUID=$NVME_ROOT_UUID|" /mnt/nvme/boot/extlinux/extlinux.conf

sudo umount /mnt/nvme/boot/efi /mnt/nvme
```

### Step 2 — Set UEFI boot order: SD first, NVMe second

List current entries:

```bash
sudo efibootmgr -v
```

Typical output:
```
Boot0000* ubuntu      HD(1,GPT,…)/File(\EFI\ubuntu\shimaa64.efi)   <- SD's bootloader
Boot0001* L4T         HD(1,GPT,…)/File(\EFI\BOOT\bootaa64.efi)     <- NVMe's bootloader
Boot0002* UEFI ...                                                  <- USB / network fallbacks
BootOrder: 0001,0000,0002
```

Reorder so the SD entry comes first:

```bash
sudo efibootmgr -o 0000,0001
```

UEFI now tries the SD bootloader first. If `\EFI\ubuntu\shimaa64.efi` (or your equivalent) isn't found — which is exactly the case when the SD has no boot partition — it **automatically falls through to entry 0001 (NVMe)** without user intervention.

### Step 3 — Verify

```bash
sudo efibootmgr -v   # confirm BootOrder = 0000,0001,...
sudo poweroff
```

- Pull SD card, power on → boots NVMe.
- Reinsert SD, power on → boots SD.
- An SD with the rootfs but no ESP / no `extlinux.conf` → UEFI falls through to NVMe.

### Caveats specific to this configuration

- **Multi-boot-media BSP versions must match.** Mixing different L4T versions across SD and NVMe corrupts UEFI overlay partitions and crashes the system ([R36.5 release notes §2.1, issue 4201479](../../sources/nvidia-jetson-linux-r36-5-release-notes.md)). Keep both media on the same L4T release. Apt-upgrade both rootfses in lockstep.
- **A blank NVMe is invisible to UEFI** — it must have a valid ESP + bootloader files to be a fallback. The Step 1 procedures above produce that; a raw `dd` of the SD image does not (UUIDs collide and extlinux still points at SD).
- **`extlinux.conf` paths must reference each rootfs's own UUID**, not `/dev/mmcblk0p1` or `/dev/nvme0n1p1` literals. The rsync + sed in Step 1 handles this; verify before powering off.
- **`efibootmgr` settings are persisted in QSPI NVRAM**, not on the SD or NVMe. Reflashing QSPI may reset `BootOrder` — re-run Step 2 after any QSPI flash.

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
- **[jetsonhacks/bootFromExternalStorage](https://github.com/jetsonhacks/bootFromExternalStorage)** — community toolkit that wraps `l4t_initrd_flash.sh` for booting Jetson Orin from NVMe / USB; recommended user-friendly alternative to running Path B by hand.
