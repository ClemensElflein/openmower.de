---
title: "RTK Receiver Options"
linkTitle: "RTK Receiver Options"
weight: 310
description: >
  Choosing an RTK-capable GNSS receiver for your OpenMower — compatibility notes, anti-jamming, and upgrade options.
---

## What the standard build uses

The standard OpenMower hardware design is built around the **u-blox ZED-F9P** RTK module. It is a proven, affordable choice and works well on open lawns.

OpenMower reads standard **NMEA sentences** (e.g. `$GGA`, `$RMC`) over UART and sends **RTCM 3.x corrections** to the receiver. Any RTK-capable receiver that speaks NMEA out / RTCM in can be used as a drop-in replacement.

## What to look for in a receiver

- **NMEA output over UART** — OpenMower parses standard GGA/RMC sentences.
- **RTCM 3.x input** — required for base/rover corrections.
- **Multi-band** (L1/L2/L5) — faster RTK convergence and better accuracy than single-band modules.
- **Jamming immunity** — mowers operate near houses, Wi-Fi, power lines, solar inverters and radio links. The ZED-F9P has roughly **25 dB** of jamming immunity; receivers built around Septentrio mosaic modules (AIM+ technology) offer around **60 dB** and hold RTK fixed in much noisier environments.

## Receiver options

| Receiver | Notes |
|----------|-------|
| u-blox ZED-F9P (standard) | Default choice; solid performance, ~25 dB jamming immunity |
| Septentrio mosaic-based (e.g. UAV GNSS EV322, HB-series) | Drop-in NMEA/RTCM receivers with AIM+ anti-jamming (~60 dB); dual-antenna heading available on P3H variants |

[UAV GNSS](https://uav-gnss.com) publishes a Septentrio integration guide with wiring and parameters for Pixhawk/ArduPilot/PX4 ([github.com/uavgnss6-bot/septentrio-gnss-integration-guide](https://github.com/uavgnss6-bot/septentrio-gnss-integration-guide)); the same NMEA/RTCM interface applies to OpenMower.

## Practical notes

- **Antenna placement matters most.** Keep the antenna away from motor controllers, radio links, and wiring bundles. A survey-grade antenna with a ground plane improves multipath rejection.
- **The base station is exposed too.** If your base sits near solar inverters or power lines, interference there affects every rover on the property.
- Seeing random RTK dropouts? Check the [GPS/RTK troubleshooting]({{< relref "../troubleshooting/gps-rtk" >}}) section and the [RTK base setup]({{< relref "rtk-base-setup" >}}) guide before swapping hardware.
