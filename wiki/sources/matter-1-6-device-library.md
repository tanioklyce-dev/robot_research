---
title: Matter 1.6 Device Library Specification
type: source
url: https://csa-iot.org/developer-resource/specifications-download-request/
local: ../../raw/23-27351-010_Matter-1.6-Device-Library-Specification.pdf
author: Connectivity Standards Alliance
published: 2026-06-16 (Document 23-27351, revision 10)
ingested: 2026-08-17
venue: Connectivity Standards Alliance
format: PDF, 229 pages
tags: [matter, csa, device-types, robotic-vacuum, closure, camera, smart-home, robotics]
---

## Summary

The catalogue of **89 Matter device types** — the document that says what a Matter device can *be*. Ingested with the [1.6 core spec](matter-1-6-core-specification.md), and it **corrects a claim this wiki made earlier the same day**.

> [!warning] Correction — "Matter has no robot device type" was wrong
> The [1.4 ingest](matter-1-4-core-specification.md) and the [Matter entity](../entities/matter.md) both asserted that Matter has no robot device type and that "nothing contemplates a mobile actuated node." **That claim was drawn from the Core Specification, which is not the document that defines device types.** The Device Library defines **§12 Robotic Device Types**, whose first entry is the **Robotic Vacuum Cleaner (device type ID `0x0074`)**, now at revision 4.
>
> This is the same error shape as the JetPack correction earlier today: **asserting an absence from a document that would not have contained the thing**. Reading one document of a multi-document standard and generalising is the failure mode; the fix is to know what each document is for before concluding anything is missing.

## Key claims

### Robotic Vacuum Cleaner — §12.1, device type `0x0074`

A mobile, actuated, floor-traversing robot has been a standard Matter device class for several revisions. Cluster requirements:

| Cluster ID | Cluster | Conformance |
|---|---|---|
| 0x0003 | Identify | M |
| 0x0054 | RVC Run Mode | M |
| 0x0055 | RVC Clean Mode | O |
| 0x0061 | RVC Operational State | M |
| **0x0150** | **Service Area** | O |

Revision history: *"3 — Add support for the Service Area cluster; 4 — Mandate OperationCompletion Event."*

**The Service Area cluster is the interesting one for this wiki**: a standardised way for a controller to tell a mobile robot *which areas of the home to operate in*, and for the robot to report that it cannot reach one. See the [Application Cluster spec](matter-1-6-application-cluster-specification.md) for the `CannotReachTargetArea` error and the [Standard Namespaces](matter-1-6-standard-namespaces.md) for the room vocabulary it is named against.

### The physically-moving classes

- **Closure**, **Closure Panel**, **Closure Controller** — the device family added in 1.5 that opens and shuts under remote command.
- **Window Covering**, **Window Covering Controller**, **Door Lock**, **Door Lock Controller** — the older motion-capable classes.
- **Water Valve**, **Irrigation System**, **Pump**, **EVSE** — actuated but not locomotive.

### The camera family

**Camera**, **Floodlight Camera**, **Video Doorbell**, **Snapshot Camera**, **Camera Controller**, **Intercom**, **Audio Doorbell**, **Chime**, **Doorbell** — the sensor classes whose data sensitivity approaches a home robot's.

### Full device-type list (89)

Base, Root Node, Power Source, OTA Requestor, OTA Provider, Bridged Node, Electrical Sensor, Secondary Network Interface, **Joint Fabric Administrator**, On/Off Light, Dimmable Light, Color Temperature Light, Extended Color Light, On/Off Plug-in Unit, Dimmable Plug-In Unit, Mounted On/Off Control, Mounted Dimmable Load Control, Pump, Water Valve, Irrigation System, Dimmer Switch, Color Dimmer Switch, Control Bridge, Pump Controller, Generic Switch, Contact Sensor, Light Sensor, Occupancy Sensor, Temperature Sensor, Pressure Sensor, Flow Sensor, Humidity Sensor, On/Off Sensor, Smoke CO Alarm, Air Quality Sensor, Water Freeze Detector, Water Leak Detector, Rain Sensor, Soil Sensor, Door Lock, Door Lock Controller, Window Covering, Window Covering Controller, **Closure**, **Closure Panel**, **Closure Controller**, Thermostat, Air Purifier, Thermostat Controller, Basic Video Player, Casting Video Player, Speaker, Content App, Casting Video Client, Video Remote Control, Mode Select, Aggregator, **Robotic Vacuum Cleaner**, Laundry Washer, Refrigerator, Room Air Conditioner, Temperature Controlled Cabinet, Dishwasher, Laundry Dryer, Cook Surface, Cooktop, Oven, Extractor Hood, Microwave Oven, EVSE, Water Heater, Solar Power, Battery Storage, Heat Pump, Meter Reference Point, Electrical Energy Tariff, Electrical Meter, Electrical Utility Meter, Network Infrastructure Manager, Thread Border Router, **Camera**, **Floodlight Camera**, **Video Doorbell**, Intercom, Audio Doorbell, **Snapshot Camera**, Chime, **Camera Controller**, Doorbell.

## Entities mentioned

- [Matter](../entities/matter.md) · [Connectivity Standards Alliance](../entities/connectivity-standards-alliance.md)

## Concepts touched

- Device-type conformance as a certification surface; the Service Area cluster as a standardised household spatial contract.

## Open questions

- **What does the RVC do when two fabrics select different Service Areas?** The device library defines conformance, not concurrency. Nothing in any of the four 1.6 documents answers it.
- **Is there a device type on the roadmap for a general home robot** — one with an arm, or locomotion beyond floor-cleaning? Nothing in 1.6 suggests it.
