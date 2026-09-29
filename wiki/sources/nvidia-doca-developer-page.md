---
title: "NVIDIA DOCA Software Platform — Developer Page"
type: source
url: https://developer.nvidia.com/networking/doca
author: NVIDIA
published: 2026-09-29
ingested: 2026-09-29
venue: NVIDIA Developer (product page)
format: vendor landing page (undated; published = capture date)
local_path: raw/2026-09-29-nvidia-doca-developer-page.md
sha256: de851a64d4735f651390fafa20832dc78abe0181eeeb460f14e6e36057dac83d
tags: [nvidia, doca, bluefield, connectx, dpu, supernic, networking, data-center, zero-trust, vendor-page]
---

# NVIDIA DOCA Software Platform — Developer Page

## Summary

The developer landing page for **DOCA**, NVIDIA's SDK and runtime for **[BlueField](../entities/nvidia-bluefield.md) DPUs/SuperNICs and ConnectX NICs**. It is ingested as background for [NVIDIA Sentry](../entities/nvidia-sentry.md), which the [launch release](nvidia-newsroom-open-agent-safety-platform.md) says is *"built on NVIDIA DOCA."* The page itself **does not mention OpenShell, Sentry or agents** apart from a generic "Powering the Agentic AI Factory" header. It describes DOCA as data-centre infrastructure software: *"offload, accelerate, and isolate data center workloads,"* with BlueField *"isolat[ing] the infrastructure service domain from the workload domain."* That isolation property is the one Sentry depends on.

## Key claims

- **Two deployments:** **DOCA on BlueField** (an SDK plus a runtime that provisions and orchestrates containerized services on *"hundreds or thousands of DPUs and SuperNICs"*) and **DOCA-Host** (drivers and tools for BlueField and ConnectX on the host, Arm and x86, Ethernet and InfiniBand *"up to 800 Gb/s"*).
- **BlueField software bundle:** bootloader, kernel, NIC firmware, drivers, toolchain, and **Ubuntu 22.04**.
- **SDK components:** RDMA (UCX/UCC, GPUDirect), network acceleration (ASAP², VirtIO emulation, Firefly time sync), **security acceleration (inline crypto, "App Shield runtime security")**, storage, a data-path accelerator (DPA) SDK, management, and DPDK/SPDK/Netlink.
- **Forward and backward compatibility** across BlueField generations is claimed.

## Entities mentioned

- [NVIDIA BlueField](../entities/nvidia-bluefield.md) · [NVIDIA Sentry](../entities/nvidia-sentry.md) (by context only) · [NVIDIA](../entities/nvidia.md)

## Concepts touched

- [Robot security](../concepts/robotics/robot-security.md) (by contrast: no edge counterpart)

## Analysis

This is a thin source for the wiki's purposes, and deliberately so. It establishes what DOCA *is*, so the Sentry claims can be read correctly: Sentry is an application of a mature DPU/NIC SDK, not new silicon. **"App Shield runtime security"** is the pre-existing DOCA security feature closest to Sentry's host-introspection role; the page doesn't connect the two.

For robots, the relevant fact is an absence. **No Jetson module has a DPU, and DOCA targets data-centre NICs.** The in-silicon, out-of-band layer of the Open Agent Safety Platform therefore has **no on-robot equivalent**. A robot gets OpenShell, the software layer, and nothing beneath it. Any hardware-isolated enforcement on a robot would have to come from a different lineage, such as a safety MCU or safety PLC on the actuator bus ([ISO 13482](../concepts/robotics/robot-safety-standards.md) territory).

## Open questions

- Is Sentry a DOCA application or service (like App Shield), and will its source or container be published?
