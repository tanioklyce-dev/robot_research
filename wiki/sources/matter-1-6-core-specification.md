---
title: Matter 1.6 Core Specification
type: source
url: https://csa-iot.org/developer-resource/specifications-download-request/
local_path: raw/23-27349-011_Matter-1.6-Core-Specification.pdf
sha256: 48b3b117569f72558ba71813360d77abdfa11fcf28747bd269148104936b52b7
local: ../../raw/23-27349-011_Matter-1.6-Core-Specification.pdf
author: Connectivity Standards Alliance
published: 2026-06-16 (Document 23-27349, revision 11, Matter Specification R1.6)
ingested: 2026-08-17
venue: Connectivity Standards Alliance
format: PDF, 1,335 pages
tags: [matter, csa, smart-home, multi-admin, fabric, access-control, arl, arbitration, interoperability]
---

## Summary

The current **Matter Core Specification, R1.6** (2026-06-16), superseding the [1.4](matter-1-4-core-specification.md) revision ingested earlier the same day. Obtained as a user-supplied PDF alongside the [Application Cluster](matter-1-6-application-cluster-specification.md), [Device Library](matter-1-6-device-library.md) and [Standard Namespaces](matter-1-6-standard-namespaces.md) documents — the first time this wiki has held the full Matter document set rather than the core alone.

**It settles the question the 1.4 ingest left open.** The [home AI platform](../syntheses/agents/home-ai-platform-trust-and-authority.md) analysis asked whether Matter's lack of cross-controller arbitration was *structural or incidental* — the test being whether new device classes that physically move would bring arbitration with them. Two major versions later, with **Closures and a Robotic Vacuum Cleaner** in the device library: **they did not.** The gap is structural.

## Key claims

### The multi-admin model is unchanged from 1.4

**§7.5.3 Fabric-Scoped Data is verbatim identical** apart from one editorial substitution ("fabric-scoped *quality*" → "fabric-scoped *access*") and a renumbered cross-reference:

> "**Most cluster data instances are accessible regardless of the accessing fabric.** However, data that is exclusively associated with a particular fabric SHALL be defined as being fabric-scoped… Fabric-scoped data SHALL be limited to the following: • list of fabric-scoped structs, which MAY include fabric-sensitive fields • fabric-sensitive event"

Operational device state remains **shared across all commissioned fabrics**, and per-fabric isolation still covers only configuration lists.

### There is still no cross-controller arbitration — now measured across the whole document set

| Term | 1.4 Core | **1.6 Core** | 1.6 Cluster | 1.6 Device Library | 1.6 Namespaces |
|---|---|---|---|---|---|
| `arbitrat` | **0** | **0** | **0** | **0** | **0** |
| `interlock` | — | **0** | **0** | **0** | **0** |
| `preempt` | — | 1 | 0 | 0 | 0 |
| `conflict` | 8 | 9 | 7 | 3 | 0 |

The single `preempt` is unrelated: *"Network recovery procedure SHALL preempt autonomous network reconnect attempts."*

**Every `conflict` in the core spec was read individually.** Five are identifier collisions carried over from 1.4 (DNS-SD names, UDP ports, ephemeral node IDs, data-type naming, CHOICE-OF schema merging). The two that are *not* are both about something other than operational state:

- **`BusyWithOtherAdmin`** (§ArmFailSafe) — the command "SHALL leave the current fail-safe state unchanged and immediately respond with `ArmFailSafeResponse` containing an ErrorCode value of `BusyWithOtherAdmin`, indicating a likely **conflict between commissioners**." Mutual exclusion exists — **for commissioning sessions**.
- **Ecosystem Information Cluster** — "adds metadata to support **conflict resolution between multiple sources of the name and location data**" for bridged endpoints. Conflict resolution exists — **for name/location metadata**.

> [!note] CSA solved mutual exclusion exactly where it chose to
> The specification is not innocent of the problem. It has a named error code for two administrators colliding during commissioning, and a cluster dedicated to reconciling competing metadata. **It declines to define anything equivalent for competing commands to a device.** That is a design decision, not an oversight — and it is why the [home AI platform](../syntheses/agents/home-ai-platform-trust-and-authority.md) page's conclusion holds two versions later.

### The Access Restriction List is being developed, not deprecated

Mentions grew from 1.4 → 1.6: `Access Restriction List` 5 → **11**, `ReviewFabricRestrictions` 1 → **17**, plus 14 uses of `ACCESS_RESTRICTED`. The vendor-authored, per-fabric, deny-by-default authority bound identified in the 1.4 ingest is an area of active work.

### Version timeline (from the core spec's own revision history)

| Rev | Date | Version |
|---|---|---|
| 2 | 2022-09-23 | 1.0 |
| 3 | 2023-05-17 | 1.1 |
| 4 | 2023-10-18 | 1.2 |
| 5 | 2024-04-17 | 1.3 |
| 6 | 2024-11-04 | **1.4** (previously ingested) |
| 7 | 2025-03-17 | 1.4.1 |
| 8 | 2025-07-16 | 1.4.2 |
| 9 | 2025-11-10 | 1.5 |
| 10 | 2026-03-16 | 1.5.1 |
| 11 | **2026-06-16** | **1.6** (this document) |

Roughly two releases a year, dot-releases between.

## Entities mentioned

- [Matter](../entities/matter.md) · [Connectivity Standards Alliance](../entities/connectivity-standards-alliance.md)

## Concepts touched

- Multi-admin authority; deny-by-default access control; the distinction between arbitrating *sessions* and arbitrating *actions*.

## Open questions

- **Will the ARL grow into a general authority surface?** Its expansion is the one place Matter is moving toward what a robot-bearing home platform would need.
- **Is the absence of command arbitration ever discussed in CSA working-group material?** The specification is silent on the rationale; a design note or meeting record would settle whether it was considered and rejected.
