---
title: Connectivity Standards Alliance
type: entity
subtype: organization
created: 2026-08-17
updated: 2026-08-17
sources: 5
tags: [csa, standards-body, matter, zigbee, smart-home, interoperability]
---

**Connectivity Standards Alliance (CSA)** — the standards body that publishes [Matter](matter.md), the smart-home interoperability standard beneath Apple Home, Google Home, Amazon Alexa and SmartThings. Formerly the Zigbee Alliance.

## In this wiki

The CSA is the wiki's only home-automation standards body, and the [Matter 1.6 document set](../sources/matter-1-6-core-specification.md) plus the superseded [1.4 core spec](../sources/matter-1-4-core-specification.md) are its ingested documents. It matters here because the **[home AI platform](../syntheses/agents/home-ai-platform-trust-and-authority.md)** — agentic robot AI fused with home automation — inherits Matter's trust model on the automation side, and Matter is the only half of that fusion with a published, mature answer to multi-ecosystem authority.

Specification identifiers seen: Matter 1.4 is **CSA Document 23-27349**, revision R1.4, dated **2024-11-04**.

## Release cadence

Roughly two dot-releases a year, each adding device types:

| Version | Notable |
|---|---|
| 1.0 | 2022-11 — initial |
| 1.2 | 2023-10 |
| 1.3 | 2024-05 |
| **1.4** | **2024-11-04** — Fabric Synchronization, Joint Fabric, enhanced multi-admin, energy management |
| 1.4.1 / 1.4.2 | — |
| 1.5 | **2025-11-10** — cameras, closures, enhanced energy management |
| 1.5.1 | 2026-03-16 |
| **1.6** | **2026-06-16** — **the version ingested here**, as a four-document set |

> [!note] Access
> Specification PDFs are distributed from `csa-iot.org` behind a **name/company/email download-request form**, which returns **HTTP 403** to unauthenticated fetchers. Several *older* core-specification PDFs are directly linkable from the uploads path — that is how **1.4** was retrieved. **1.5 and 1.6 are not**: five URL patterns were probed and all returned 404. The **1.6 set was supplied by the user through the download form**, which is the only route that works for current revisions.

## The document set

Matter is **four documents**, and confusing them is a live failure mode — this wiki asserted "no robot device type" from the Core Specification, which does not define device types:

| Document | CSA number | 1.6 size | Defines |
|---|---|---|---|
| [Core Specification](../sources/matter-1-6-core-specification.md) | 23-27349 | 1,335 pp | Fabrics, commissioning, security, access control, the data model |
| [Application Cluster Specification](../sources/matter-1-6-application-cluster-specification.md) | 23-27350 | 982 pp | What devices can *do* — clusters, attributes, commands |
| [Device Library Specification](../sources/matter-1-6-device-library.md) | 23-27351 | 229 pp | What devices can *be* — 89 device types and their conformance |
| [Standard Namespaces](../sources/matter-1-6-standard-namespaces.md) | 23-31936 | 71 pp | Semantic tags — the shared vocabulary for homes, rooms, objects, activities |

## Related

- [Matter](matter.md) — the standard
- [The home AI platform — trust and authority](../syntheses/agents/home-ai-platform-trust-and-authority.md)

## Mentioned in

- [Matter 1.6 Core Specification](../sources/matter-1-6-core-specification.md) · [Application Cluster](../sources/matter-1-6-application-cluster-specification.md) · [Device Library](../sources/matter-1-6-device-library.md) · [Standard Namespaces](../sources/matter-1-6-standard-namespaces.md)
- [Matter 1.4 Core Specification](../sources/matter-1-4-core-specification.md) — superseded
