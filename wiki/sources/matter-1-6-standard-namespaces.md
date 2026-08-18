---
title: Matter 1.6 Standard Namespaces
type: source
url: https://csa-iot.org/developer-resource/specifications-download-request/
local: ../../raw/23-31936-008_Matter-1.6-Standard-Namespaces.pdf
author: Connectivity Standards Alliance
published: 2026-06-16 (Document 23-31936, revision 8)
ingested: 2026-08-17
venue: Connectivity Standards Alliance
format: PDF, 71 pages
tags: [matter, csa, semantic-tags, ontology, household-world-model, spatial-privacy, fall-detection, smart-home]
---

## Summary

The smallest of the four 1.6 documents and, for this wiki, **the most consequential**. It defines **28 semantic-tag namespaces** — a standardised vocabulary for describing a home: its rooms, its furniture, positions, directions, levels, and **what the people in it are doing**.

> [!note] This is the household world model's *schema*, published as a standard
> The [home AI platform](../syntheses/agents/home-ai-platform-trust-and-authority.md) analysis argued the platform asset is a **persistent world model of a household** — floorplan, objects, routines, people. CSA has not published anyone's *data*, but it has published the **ontology**: a shared, cross-vendor vocabulary for exactly those four things. That materially changes the multi-homing argument, because a shared schema is what makes a household model *portable* between ecosystems, and portability is the enemy of the lock-in that makes the model a moat.

## Key claims

### 28 namespaces

Common Closure · Common Compass Direction · Common Compass Location · Common Direction · Common Level · Common Location · Common Number · Common Position · Electrical Measurement · Commodity Tariff Chronology · Commodity Tariff Commodity · Laundry · Power Source · **Common Area** · **Common Landmark** · Common Relative Position · Commodity Tariff Flow · Refrigerator · Room Air Conditioner · Switches · Closure · Closure Panel · Closure Covering · Closure Window · Closure Cabinet · Identified Sound · **Identified Object** · **Identified Human Activity**

### Common Area Namespace (`0x10`) — the rooms of a house

*"to indicate an association with an indoor or outdoor area of a home."* Aisle, Attic, BackDoor, BackYard, Balcony, Ballroom, Bathroom, **Bedroom**, Border, Boxroom, BreakfastRoom, Carport, Cellar, Cloakroom, Closet, Conservatory, Corridor, CraftRoom, Cupboard, Deck, Den, Dining, DrawingRoom, DressingRoom, Driveway, Elevator, **Ensuite** (*"a bathroom directly accessible from a bedroom"*), Entrance, Entryway, FamilyRoom, Foyer, FrontDoor, FrontYard, GameRoom, Garage, GarageDoor, Garden, GardenDoor, **GuestBathroom**, **GuestBedroom**, GuestRoom, Gym, Hallway, HearthRoom … (continues).

### Common Landmark Namespace (`0x11`) — the furniture

*"to indicate an association with a home landmark."* AirConditioner, AirPurifier, BackDoor, BarStool, BathMat, Bathtub, **Bed**, Bookshelf, Chair, ChristmasTree, CoatRack, CoffeeTable, CookingRange, Couch, Countertop, **Cradle**, **Crib**, Desk, DiningTable, Dishwasher, Door, Dresser, LaundryDryer, Fan, Fireplace, Freezer, FrontDoor, **HighChair**, KitchenIsland, Lamp, **LitterBox**, Mirror, Nightstand, Oven, **PetBed**, **PetBowl**, **PetCrate**, Refrigerator, **ScratchingPost**, ShoeRack, **Shower**, SideDoor, Sink, Sofa, Stove, Table, **Toilet**, TrashCan, LaundryWasher, Window, WineCooler.

### Identified Human Activity Namespace — including falls

| ID | Name | Summary |
|---|---|---|
| 0x00 | Unknown | Unknown human activity is detected |
| **0x01** | **Fall** | **Human fall is detected** |
| 0x02 | Sleeping | Human sleeping is detected |
| 0x03 | Walking | Human walking is detected |
| 0x04 | Workout | Human workout is detected |
| 0x05 | Sitting | Human sitting is detected |
| 0x06 | Standing | Human standing is detected |
| 0x07 | Dancing | Human dancing is detected |
| 0x08 | PackageDelivery | Human delivery of package is detected |
| 0x09 | PackageRetrieval | Human retrieval of package is detected |

> [!warning] `Fall` is now a standard interoperable tag — and the wiki's consumer evidence is unchanged
> The [Zeroth M1](../entities/zeroth-m1.md) markets *"gentle fall detection"* for elder safety with **no accuracy figure, no trial, and no deployment evidence**. Matter 1.6 makes fall detection a **cross-vendor signal any device can emit and any ecosystem can consume**. Standardising the *reporting* of a claim does nothing to standardise its *accuracy* — there is no conformance requirement here for how well a device must detect a fall before setting `0x01`. See [aging in place](../concepts/robotics/aging-in-place.md), where the gap is being filled by marketing rather than evidence.

## The inference surface, stated concretely

[World-model governance](../concepts/safety/world-model-governance.md) warns that a spatial model "may infer home routines, workplace patterns, **health-related behavior**, **social relationships**, or sensitive locations that were never explicitly labeled," and that policy must reach "the downstream creation of persistent spatial profiles."

**This document is that inference surface, itemised.** Cross the three namespaces and the vocabulary already distinguishes:

- **Who lives there** — Crib, Cradle, HighChair (an infant); PetBed, LitterBox, ScratchingPost (a cat); GuestBedroom, GuestBathroom (visitors).
- **Where the private spaces are** — Bedroom, Ensuite, Bathroom, Shower, Toilet, DressingRoom.
- **What people are doing in them** — Sleeping, Sitting, Standing, Walking, Workout, Dancing, **Fall**.

None of that requires a camera or a name. It is inference from tags a home is expected to publish for interoperability — which is precisely the harm shape the governance page describes, now with a published vocabulary behind it.

## Entities mentioned

- [Matter](../entities/matter.md) · [Connectivity Standards Alliance](../entities/connectivity-standards-alliance.md) · [Zeroth M1](../entities/zeroth-m1.md)

## Concepts touched

- [Aging in place](../concepts/robotics/aging-in-place.md) · [world-model governance](../concepts/safety/world-model-governance.md) · household ontology as shared schema

## Open questions

- **Is there any conformance requirement on the accuracy of `Fall`?** Nothing in this document sets one, and the Application Cluster spec was not searched exhaustively for it.
- **Does a shared ontology actually make household models portable in practice?** A common vocabulary is necessary but not sufficient — the map, the history and the embeddings are still vendor-private.
- **Who is expected to emit `Identified Human Activity`?** A radar sensor, a camera, a robot? The namespace is device-agnostic by design, which is what makes it an inference surface rather than a camera feature.
