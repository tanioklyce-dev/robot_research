---
title: JetPack SDK
type: entity
created: 2026-05-16
updated: 2026-05-17
sources: 7
tags: [nvidia, jetson, jetpack, sdk, cuda, tensorrt, jetpack-7, jetson-thor, mig, sbsa]
---

# JetPack SDK

NVIDIA's **bundled software stack** for Jetson products — operating system image, AI/CV libraries, code samples, and developer tools shipped together as a versioned release. The supported way to put a working software environment on a [Jetson Orin Nano](jetson-orin-nano.md), AGX Orin, or Orin NX.

## What it bundles

A JetPack release is fundamentally three layers stacked together ([JetPack docs index](../sources/nvidia-jetpack-docs-index.md)):

1. **[Jetson Linux](jetson-linux.md) (L4T)** — the OS image: Ubuntu rootfs + Linux kernel + UEFI bootloader + OP-TEE + NVIDIA drivers.
2. **CUDA stack** — CUDA toolkit, cuDNN, TensorRT.
3. **Application-layer libraries** — VPI (vision), DeepStream (video analytics), DLA, multimedia.

Plus code samples, the `nvidia-jetpack` debian metapackage, and documentation.

## Current production release — JetPack 6.2.2

As of mid-2025, **JetPack 6.2.2** is the latest production release of the JetPack 6 line ([JetPack 6.2.2 release page](../sources/nvidia-jetpack-6-2-2-release.md)):

| Component | Version |
|---|---|
| Jetson Linux | 36.5 (kernel 5.15, Ubuntu 22.04 rootfs) |
| CUDA | 12.6.10 |
| cuDNN | 9.3.0 |
| TensorRT | 10.3.0 |
| DeepStream | 7.1 |
| VPI | 3.2 |
| DLA | 3.14 |

> [!note]
> The [JetPack docs index](../sources/nvidia-jetpack-docs-index.md) still references **6.2.1** (last updated 2025-06-26). The developer-site release page lists **6.2.2** as current. Docs lag the dev site.

### Notable new features in 6.2.2 vs prior 6.x

- **AprilTag Detector and Pose Estimator** in VPI — NVIDIA's first-party, GPU/PVA-accelerated [AprilTags](../concepts/robotics/apriltags.md) pipeline.
- Dynamic Remap; Recursive Gaussian Filter.
- PVA backend speedups (claimed up to 5×).
- Hardware Security Module (HSM) support for boot-image signing.

## Install paths

- **SD card image** (Orin Nano): NVIDIA publishes a JetPack 6.2.1 / Jetson Linux 36.4.4 SD image; users apt-upgrade to 6.2.2 after first boot.
- **NVIDIA SDK Manager** on a Linux x86_64 host — flashes OS + installs SDK components over USB-C with the target in force-recovery mode. Host OS officially **Ubuntu 20.04** for the Orin Nano workflow ([NVIDIA Software Setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)).
- **Debian package**: on a running Jetson, `sudo apt install nvidia-jetpack` pulls the SDK on top of an existing Jetson Linux install.

## Update mechanism

Within a JetPack 6.x line, updates flow through apt against NVIDIA's L4T Debian repo. Point releases use `apt upgrade`; minor releases require editing `/etc/apt/sources.list.d/nvidia-l4t-apt-source.list` then `apt dist-upgrade`. **Crossing major versions (5 → 6) is not supported via apt — full reflash required** ([R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)).

## Supported hardware

- Jetson AGX Orin (modules + Developer Kit).
- Jetson Orin NX (modules).
- [Jetson Orin Nano](jetson-orin-nano.md) (modules + Developer Kit).

Jetson Xavier-class hardware is on the older JetPack 5.x / L4T 35.x track and not supported by JetPack 6.

## JetPack 7 — Thor track

The Blackwell-generation [Jetson Thor](jetson-thor.md) (T5000, T4000) is on a **separate JetPack 7.0 line**, not JetPack 6. Orin-class modules remain on the JetPack 6.x track for compatibility — JetPack 6 and JetPack 7 are parallel, not sequential.

JetPack 7.0 launched alongside Thor on **2025-08-25** ([JetPack 7.0 for Jetson Thor software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md)) with the following bundle:

| Component | Version |
|---|---|
| [Jetson Linux (L4T)](jetson-linux.md) | **38.2** (kernel **6.8**, Ubuntu **24.04 LTS** rootfs) |
| CUDA | **13** |
| cuDNN | **9.12** |
| TensorRT | **10.13** |

Architectural commitments distinguishing JetPack 7 from JetPack 6:

- **SBSA (Server Base System Architecture) alignment** — Thor is positioned as a server-class ARM platform.
- **NVIDIA optimized preemptible real-time kernel** — ships in the release.
- **Multi-Instance GPU (MIG)** — Thor's Blackwell GPU can be partitioned (new on Jetson).
- **CSI-over-Ethernet (CoE)** via Holoscan Sensor Bridge.

Supported AI serving frameworks shipped or documented: **vLLM**, **SGLang**, **MLC**, **llama.cpp**, **Ollama**, **Hugging Face Transformers**. JetPack 7 also enables Thor's NVFP4 (Blackwell 4-bit float) quantization, which underpins the **7× post-launch generative-AI throughput improvement** documented in the [JetPack 7 software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md). Isaac ROS on Thor is on a separate, Thor-compatible release track (specific version not enumerated in the JetPack 7 primary sources).

See [Jetson Thor](jetson-thor.md) for module-side software details.

## Mentioned in
- [Jetson Orin Nano flash howto](../syntheses/projects/jetson-orin-nano-flash-howto.md)
- [Jetson Orin Nano](jetson-orin-nano.md)
- [Jetson Linux](jetson-linux.md)
- [NVIDIA](nvidia.md)
- [JetPack 6.2.2 release](../sources/nvidia-jetpack-6-2-2-release.md)
- [JetPack docs index](../sources/nvidia-jetpack-docs-index.md)
- [Jetson Linux R36.5 release](../sources/nvidia-jetson-linux-r36-5-release.md)
- [Jetson Linux R36.5 update mechanism](../sources/nvidia-jetson-linux-r36-5-update-mechanism.md)
- [NVIDIA Jetson Orin Nano Dev Kit software setup](../sources/nvidia-jetson-orin-nano-devkit-software-setup.md)
- [JetPack 7.0 for Jetson Thor software-stack reference](../sources/nvidia-jetpack-7-thor-whitepaper.md) — primary source for JetPack 7 / Jetson Linux 38.2 contents.
