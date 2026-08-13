---
title: Zenoh
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 2
tags: [zenoh, middleware, pub-sub, dds-alternative, ros2, rmw, rust, eclipse, transport, dimos, zenoh-pico, benchmark, latency, embedded]
---

**Zenoh** (/zeno/, Eclipse Zenoh) — a **pub/sub + storage + query protocol** unifying *data in motion, data at rest, and computations* under one key space. Rust core, multi-language APIs, **EPL-2.0 / Apache-2.0** dual licence, Eclipse **incubating**. [eclipse-zenoh/zenoh](https://github.com/eclipse-zenoh/zenoh) — **3,078★ / 349 forks**, created January 2020, pushed daily as of 2026-08-13. From ZettaScale. Primary source: [zenoh.io](../sources/zenoh-io.md).

Two engineering claims define it: **5-byte minimum wire overhead** (it can run directly on OSI Layer 2), and **Zenoh-pico**, a microcontroller implementation at **300 bytes on an 8-bit Atmel**.

## Why it appears here

Two independent routes, and they are the interesting part:

- **[DimOS](dimos.md)** offers it as one of five interchangeable transports under an unchanged module API — and specifically as the **reliable** alternative to its LCM default. The [DimOS transport docs](../sources/dimos-github.md) are unusually candid about the trade: *"`lcm`: current legacy default… Fast and simple, but UDP multicast is best-effort. `zenoh`: network transport with reliable delivery semantics and the same typed message model."* Selectable at the CLI with `dimos --transport=zenoh`.
- **[ROS 2](ros2.md)** — `ros2/rmw_zenoh` (495★, actively developed) implements Zenoh as a ROS 2 middleware layer, the credible alternative to the DDS implementations ROS 2 has historically shipped. It also appears in the wiki's [ros2-mcp-server design](../syntheses/projects/ros2-mcp-server-design.md) work.

## Three primitives

| Primitive | What it does |
|---|---|
| **Pub/Sub** | Multiple reliability levels, dynamic discovery, fragmentation, wire-level batching |
| **Storages** | Geo-distributed with **sharding and replication** — historical data shares the live key space |
| **Queries & Queryables** | Register a *computation* that fires on query — *"allows many patterns… such as RPC and map-reduce"* |

**Three topologies**, and this is the structural difference from its rivals: peer-to-peer (mesh/clique), brokered, and routed infrastructure. **MQTT and Kafka are brokered-only; DDS is peer-to-peer-only; Zenoh does both** and mixes them.

## Measured performance

Independent evaluation by a National Taiwan University team ([blog + arXiv](../sources/zenoh-io.md)); Ryzen 7 5800X @ 4.0 GHz, 100 Gb Ethernet for multi-machine. Latency at 64-byte payload, µs, lower better:

| Target | Single machine | **Multi-machine** |
|---|---:|---:|
| `ping` baseline | 1 | 7 |
| **Zenoh-pico** | **5** | **13** |
| Cyclone DDS | **8** | 37 |
| **Zenoh P2P** | 10 | **16** |
| Zenoh brokered | 21 | 41 |
| MQTT | 27 | 45 |
| Kafka | 73 | 81 |

Throughput: **Zenoh P2P >4M msg/s** small payloads (up to 67 Gbps) vs Cyclone DDS ~2M, Kafka 56–63K, MQTT 33–38K.

> [!note] The single-machine row where DDS wins is the credible part
> **Cyclone DDS beats Zenoh's Rust implementation on one machine (8 µs vs 10 µs)** because DDS uses **UDP multicast**, which the main Zenoh implementation lacked at benchmark time; Zenoh-pico, which has it, lands at **5 µs**. A benchmark published by the project that still prints the row a competitor wins, with the mechanism.
>
> **Across a real network the ordering inverts decisively — Zenoh P2P 16 µs vs Cyclone DDS 37 µs.** Multicast is exactly what stops working across subnets, over Wi-Fi, and through NAT, which is the deployment this wiki cares about.

## What it is for

The problem Zenoh addresses is the one every robot fleet eventually hits: **DDS was designed for a LAN**, and multicast discovery degrades badly across subnets, over Wi-Fi, and through NAT. Zenoh's pitch is a single protocol that spans **on-device, edge, and cloud** with routers that bridge networks, plus a query/storage layer so historical data uses the same addressing as live data.

For this wiki's purposes, three properties matter:

1. **Reliable delivery** where LCM's UDP multicast is best-effort — the reason DimOS documents choosing between them per-task rather than globally.
2. **It routes** — no multicast requirement, so a robot behind a home router can participate. Compare [DimOS](dimos.md)'s **dimTELE**, which solves the same NAT problem for teleoperation by having the robot dial out to a broker.
3. **Rust**, with a small footprint aimed at embedded targets.

> [!note] The robotics numbers are 5 bytes and 300 bytes, not 4M msg/s
> 4M msg/s on a Ryzen is a datacentre figure and largely irrelevant to a robot. **5-byte wire overhead and a 300-byte 8-bit-micro footprint** are the robotics ones: the same protocol addresses a sensor MCU and a cloud store. That is what DDS has historically not done well, and the reason ROS 2 fleets fragment into "the DDS part" and "the cloud part." Zenoh's real pitch is **one addressing scheme from microcontroller to datacentre**; the performance table is supporting evidence, not the claim.

> [!note] Queryables have no ROS 2 analogue
> Pub/sub maps onto ROS 2 topics and DDS cleanly. **Queryables — a registered computation that fires on query — do not.** They collapse RPC, map-reduce, and historical retrieval into the same key-space operation as a live subscription. For the wiki's fleet work ([fleet agentic framework](../syntheses/projects/fleet-agentic-framework.md), [ros2-mcp-server](../syntheses/projects/ros2-mcp-server-design.md)) that is the interesting primitive: "current pose," "pose at 14:02 yesterday," and "summarize the last hour" become one addressed call instead of three subsystems.

> [!note] Middleware pluralism is now real, and this wiki was late to it
> Until this week's [DimOS](dimos.md) ingest, the wiki treated [ROS 2](ros2.md) as effectively the only robot middleware. Zenoh sits at the centre of the actual picture: it is simultaneously **a ROS 2 backend** (`rmw_zenoh`) *and* **a way to not use ROS 2** (DimOS's transport layer). The competition is not "ROS 2 vs an alternative" but a **stack that has come apart into interchangeable layers** — discovery, transport, and API are now separable choices. [Drake](drake.md) marking ROS 2 "unsupported" while shipping LCM natively is the same fragmentation from a third angle.

## Related

- [DimOS](dimos.md) — offers Zenoh as its reliable transport option
- [ROS 2](ros2.md) — `rmw_zenoh` makes Zenoh a first-class ROS 2 middleware
- [Drake](drake.md) — the LCM-native, ROS-2-unsupported end of the same fragmentation
- [ros2-mcp-server design](../syntheses/projects/ros2-mcp-server-design.md)

## Open questions

- ~~No measured numbers~~ — **closed 2026-08-13** by the NTU benchmark above. ~~License unconfirmed~~ — **EPL-2.0 / Apache-2.0**, confirmed on the project site.
- **Zenoh vs LCM is still unmeasured**, and it is the comparison this wiki actually needs — [DimOS](dimos.md) ships both and documents the trade only qualitatively.
- **Jitter is unreported.** Medians are published; for a control loop the tail is what decides.
- **Has the Rust implementation gained UDP multicast since 0.7?** If so, the single-machine DDS advantage disappears and the 2023 table understates current Zenoh.
- Is `rmw_zenoh` production-default in any ROS 2 distribution yet, or still opt-in?
- **No security/authn model** was read, despite routed multi-network deployment being the headline use case.

> [!warning] Incubating, and the benchmark is three years old
> Eclipse *incubation* is not a maturity endorsement, and the NTU numbers use **Zenoh 0.7.0-rc**. Zenoh is now 1.x with an API migration behind it. The *ordering* likely holds — it follows from architecture — but treat absolute figures as 2023 evidence.

## Mentioned in

- [Zenoh — project site, docs, and the NTU performance comparison](../sources/zenoh-io.md)
- [DimOS GitHub repository](../sources/dimos-github.md)
