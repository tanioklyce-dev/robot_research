---
title: Zenoh
type: entity
subtype: software-framework
created: 2026-08-13
updated: 2026-08-13
sources: 1
tags: [zenoh, middleware, pub-sub, dds-alternative, ros2, rmw, rust, eclipse, transport, dimos]
---

**Zenoh** (Eclipse Zenoh) — a Rust pub/sub, query, and storage protocol that *"unifies data in motion, data in-use, data at rest and computations,"* blending traditional pub/sub with geo-distributed storage and queries. [eclipse-zenoh/zenoh](https://github.com/eclipse-zenoh/zenoh) — **3,078★ / 349 forks**, created January 2020, pushed daily as of 2026-08-13. From ZettaScale; [zenoh.io](https://zenoh.io).

Filed because it shows up in **12 pages** of this wiki as the reliable-transport answer, without ever being described.

## Why it appears here

Two independent routes, and they are the interesting part:

- **[DimOS](dimos.md)** offers it as one of five interchangeable transports under an unchanged module API — and specifically as the **reliable** alternative to its LCM default. The [DimOS transport docs](../sources/dimos-github.md) are unusually candid about the trade: *"`lcm`: current legacy default… Fast and simple, but UDP multicast is best-effort. `zenoh`: network transport with reliable delivery semantics and the same typed message model."* Selectable at the CLI with `dimos --transport=zenoh`.
- **[ROS 2](ros2.md)** — `ros2/rmw_zenoh` (495★, actively developed) implements Zenoh as a ROS 2 middleware layer, the credible alternative to the DDS implementations ROS 2 has historically shipped. It also appears in the wiki's [ros2-mcp-server design](../syntheses/projects/ros2-mcp-server-design.md) work.

## What it is for

The problem Zenoh addresses is the one every robot fleet eventually hits: **DDS was designed for a LAN**, and multicast discovery degrades badly across subnets, over Wi-Fi, and through NAT. Zenoh's pitch is a single protocol that spans **on-device, edge, and cloud** with routers that bridge networks, plus a query/storage layer so historical data uses the same addressing as live data.

For this wiki's purposes, three properties matter:

1. **Reliable delivery** where LCM's UDP multicast is best-effort — the reason DimOS documents choosing between them per-task rather than globally.
2. **It routes** — no multicast requirement, so a robot behind a home router can participate. Compare [DimOS](dimos.md)'s **dimTELE**, which solves the same NAT problem for teleoperation by having the robot dial out to a broker.
3. **Rust**, with a small footprint aimed at embedded targets.

> [!note] Middleware pluralism is now real, and this wiki was late to it
> Until this week's [DimOS](dimos.md) ingest, the wiki treated [ROS 2](ros2.md) as effectively the only robot middleware. Zenoh sits at the centre of the actual picture: it is simultaneously **a ROS 2 backend** (`rmw_zenoh`) *and* **a way to not use ROS 2** (DimOS's transport layer). The competition is not "ROS 2 vs an alternative" but a **stack that has come apart into interchangeable layers** — discovery, transport, and API are now separable choices. [Drake](drake.md) marking ROS 2 "unsupported" while shipping LCM natively is the same fragmentation from a third angle.

## Related

- [DimOS](dimos.md) — offers Zenoh as its reliable transport option
- [ROS 2](ros2.md) — `rmw_zenoh` makes Zenoh a first-class ROS 2 middleware
- [Drake](drake.md) — the LCM-native, ROS-2-unsupported end of the same fragmentation
- [ros2-mcp-server design](../syntheses/projects/ros2-mcp-server-design.md)

## Open questions

- **No measured numbers here.** Latency, throughput, and jitter versus Cyclone/Fast DDS and versus LCM are all unestablished — and for a robot control loop those are the only numbers that decide anything.
- Is `rmw_zenoh` production-ready or still the recommended-but-not-default option in current ROS 2 distributions? Unverified.
- License reads `NOASSERTION` on the GitHub API (the project states EPL-2.0 / Apache-2.0 dual licensing elsewhere) — unconfirmed here.

## Mentioned in

- [DimOS GitHub repository](../sources/dimos-github.md)
