---
title: Matter 1.4 Core Specification
type: source
url: https://csa-iot.org/wp-content/uploads/2024/11/24-27349-006_Matter-1.4-Core-Specification.pdf
local_path: raw/matter-1.4-core-specification.pdf
sha256: 87dd5b9312ac69cbb1b636caefda744072df0593cecc4b56957922de2b0be5dd
local: ../../raw/matter-1.4-core-specification.pdf
author: Connectivity Standards Alliance
published: 2024-11-04 (Document 23-27349, Matter Specification R1.4)
ingested: 2026-08-17
venue: Connectivity Standards Alliance
format: PDF, 1,173 pages
license: CSA specification terms
tags: [matter, csa, smart-home, home-automation, multi-admin, fabric, access-control, acl, interoperability, trust-boundary]
---

## Summary

The **Matter Core Specification, revision 1.4** — the interoperability standard beneath Apple Home, Google Home, Amazon Alexa and SmartThings, and the wiki's first primary source on home automation at all. Ingested to settle one question raised by [the home AI platform synthesis](../syntheses/agents/home-ai-platform-trust-and-authority.md): **what does Matter's multi-admin model actually guarantee, and does any of it survive contact with a robot?**

It answers that, and it **falsifies the mechanism that synthesis asserted** while strengthening its conclusion. Matter's multi-admin support does not rest on conflict-free semantics for device state. It rests on **isolating per-fabric *configuration*** — ACLs, bindings, group keys — while leaving **operational state shared and unarbitrated**. The word "arbitrat" does not appear once in 1,173 pages.

It also delivers an unanticipated result: the **Access Restriction List** is a shipping, standardized, vendor-authored bound on what an ecosystem may touch — precisely the capability-manifest pattern the synthesis predicted vendors would need to invent.

> [!note] Version
> **1.4 is not the newest.** CSA lists 1.4.1, 1.4.2, 1.5 and 1.5.1 (1.5 adds cameras and closures; 1.5.0.1 dated 2025-12-02). 1.4 is the newest whose PDF is **directly retrievable** — the download-request page returns HTTP 403 to unauthenticated fetchers. The structural facts below (fabric model, ACL, fabric-scoped data, ARL) are foundational and unlikely to have been reversed, but **1.4 claims should not be quoted as current** without checking 1.5. See [open questions](#open-questions).

## Key claims

### The fabric is the ecosystem boundary (§2.4)

> "The Matter protocol explicitly supports multiple administrators, **unrelated by any common roots of trust** (multi-admin). This functionality is addressed via multiple fabrics… A **Fabric** is a collection of Matter devices sharing a trusted root. The root of trust in Matter is the **Root CA** that issues the NOCs which underpin node identities."

One fabric ≈ one ecosystem. A device commissioned into Apple's fabric and Google's fabric holds two independent Node Operational Certificates under two unrelated CAs. `SupportedFabrics` (fixed per device) caps how many; `CommissionedFabrics` counts the current ones.

**System-model minima (§2.11.1)** give a sense of the intended scale: at least **four ACL entries per fabric** ("a node that supports 5 fabrics must support at least 20 ACL entries"), at least **three group keys per fabric**, at least **four group table entries per fabric per endpoint**, and every fabric must be able to run a Read Interaction of up to **9 paths**.

### The decisive sentence: most state is *not* fabric-scoped (§7.5.3)

> "**Most cluster data instances are accessible regardless of the accessing fabric.** However, data that is exclusively associated with a particular fabric SHALL be defined as being fabric-scoped… Fabric-scoped data allows multiple accessing fabrics to **manipulate a list of data items without interfering with each other**."

And the scope is explicitly bounded:

> "Fabric-scoped data **SHALL be limited to** the following: • list of **fabric-scoped structs**, which MAY include fabric-sensitive fields • **fabric-sensitive event**"

Enforcement: "Any interaction, including cluster commands, SHALL NOT cause modification of fabric-scoped data… if the interaction has an accessing fabric different than the associated fabric for the data."

**Read carefully, this says isolation covers lists — configuration — and nothing else.** A light's `OnOff` attribute is a single shared value. Two ecosystems both writing it is not an error, not a conflict, and not arbitrated; the second write simply takes effect and both fabrics see it through their subscriptions.

> [!warning] There is no cross-fabric arbitration anywhere in the specification
> **"arbitrat" appears zero times in 1,173 pages.** All eight occurrences of "conflict" concern DNS-SD name collisions and ephemeral node-ID selection — none concern competing commands from different administrators. Matter did not solve multi-controller arbitration for operational state. **It externalized the problem to the triviality of the state**: a bulb toggling between two admins is an annoyance, cheaply re-set, with no physical consequence.

### Access control: deny-by-default, per-fabric, five nested privileges (§6.6)

> "The Access Control system is rule-based with **no implicit access permitted by default**. Access to a Node's Targets is denied unless the Access Control system grants the required privilege level to a given Subject."

Privileges are `{View, ProxyView, Operate, Manage, Administer}`, and the granting algorithm (§6.6.6) shows them strictly nested — `Administer` subsumes `Manage` → `Operate` → `View`, with `ProxyView` a separate branch above `View`.

**ACL entries are matched by fabric**: the conceptual algorithm skips any entry where `acl_entry.FabricIndex != subject_desc.FabricIndex`. An administrator in one ecosystem cannot grant privileges that apply in another.

### The Access Restriction List — a vendor-authored bound that overrides administrators (§6.6, §9.10)

> "In addition to the ACL, a **per-fabric Access Restriction List (ARL), which is set by the device**, MAY exist. The ARL contains **Access Restriction Entries, which identify the attributes, commands and events on specific endpoint clusters which are not accessible on a given fabric**."

And it wins against the ecosystem's own grants:

> "even though the ACL entry grants Operate privilege to all data model elements, attempts to read or write attribute 0x0000, or to invoke commands upon Cluster 0x0453 of Endpoint 1 would result in an error of **`ACCESS_RESTRICTED`**, since the Access Restriction List is a **subsequent overriding of an initial privilege granted**."

With a discovery and negotiation path: a Commissioner MAY read the **CommissioningARL** to identify restrictions before committing, and MAY invoke **`ReviewFabricRestrictions`** to start a review process (the "Managed Device" flow). Restrictions that would prevent commissioning are prohibited from taking effect.

**This is a shipping, standardized capability manifest** — the device vendor declares, per ecosystem, what that ecosystem may not touch, discoverable in advance and enforced below the administrator.

### Fabric Synchronization and Joint Fabric (§12.6, §11.24) — new in 1.4

Two mechanisms for ecosystems to share devices rather than merely coexist:

- **Fabric Synchronization** — ecosystems mirror devices to one another, with sections on **preventing device duplication**, changes to synchronized devices and locations, and setup flow. Consent is explicit and per-ecosystem: *"Each ecosystem SHALL independently ask the user for consent. This can be done before or after commissioning the device."*
- **Joint Fabric** — an **Anchor Fabric** whose **Anchor CA** is trusted by all participating fabrics, signing ICAs for the others, plus a **Joint Fabric Datastore Cluster**. A commercial/multi-admin trust-federation construct rather than a peer-to-peer one.

## Entities mentioned

- [Matter](../entities/matter.md)
- [Connectivity Standards Alliance](../entities/connectivity-standards-alliance.md)

## Concepts touched

- Multi-admin / multi-tenancy; capability manifests and access restriction; trust roots and certificate hierarchies; deny-by-default authorization.
- Bears directly on [the home AI platform synthesis](../syntheses/agents/home-ai-platform-trust-and-authority.md) and on [control abstraction levels](../concepts/robotics/control-abstraction-levels.md) — the ARL is an access-level bound expressed as data.

## Open questions

- **What changed in 1.5 / 1.5.1?** Cameras and closures are the headline additions, and **a camera is the first Matter device class whose data is as sensitive as a home robot's**. Not retrievable without the gated download; the highest-value follow-up.
- **Is there any device class in Matter today with non-trivial physical state?** Closures (1.5) move. If the spec added arbitration or interlocks for them, that would be the first evidence Matter is growing toward robot-grade semantics; if it did not, the gap this page identifies is structural rather than incidental.
- **Does any shipping device actually use the ARL?** The mechanism is specified; nothing here shows adoption. A vendor ARL in the field would be the strongest available evidence for the capability-manifest prediction.
- **How do the ecosystems behave in practice** when two fabrics issue competing commands? The specification is silent, so behaviour is implementation-defined — and unmeasured here.
- ~~Matter has **no robot device type**~~ — **corrected 2026-08-17**: it does. The [Device Library](matter-1-6-device-library.md) defines a **Robotic Vacuum Cleaner** device type (`0x0074`). This page asserted an absence from the Core Specification, which is not the document that defines device types. Superseded by the [1.6 core spec](matter-1-6-core-specification.md).
