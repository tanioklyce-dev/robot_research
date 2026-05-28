---
title: ROSOrin Pro Setup Notes
type: notes
created: 2026-05-17
tags: [rosorin-pro, hiwonder, jetson, nvidia, edge-ai, hardware, robotics-compute]
---


# ROSOrin Pro Setup 

## Jetson Orin Nano 8GB

Jetson Orin Nano Series [L4T 36.5.0]
For JetPack 6.2, use Ubuntu 22.04.

```
lsb_release -a
uname -a
```


```
lsblk -d -p | grep nvme | cut -d\  -f 1

nvme0n1
```

```
sudo <env-var> ./tools/kernel_flash/l4t_initrd_flash.sh [ -S <rootfssize> ] -c <config> --external-device nvme0n1p1 --direct <nvmeXn1> <board> external

<config> is the NVMe SSD partition layout. See the example in Linux_for_Tegra/tools/kernel_flash//flash_l4t_t234_nvme.xml.

<board> is the type of Jetson device to be flashed:
  jetson-orin-nano-devkit / jetson-orin-nano-devkit-super
```
