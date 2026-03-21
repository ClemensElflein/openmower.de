---
title: "YardForce Carrier Board v1.0.0-beta — v1.0.1-beta"
date: 2024-10-19
author: "Clemens Elflein"
description: "Initial release of the YardForce v2 carrier board, followed by an efficiency and GPS power control fix."
---

The YardForce v2 carrier board is the reference design for the OpenMower v2 hardware platform. It connects the universal xCore board to the YardForce mower's motors, charging circuit, and sensors, and shares the same SODIMM form factor as the original board with the same connectors.

### v1.0.0-beta — 2024-10-07

First public release of the YardForce v2 carrier board design.

### v1.0.1-beta — 2024-10-19

- **DCDC bias supply** — A bias supply has been added to the DC-DC converter for improved efficiency under light load conditions.
- **F9P power switch** — A dedicated power switch for the Ardusimple F9P GPS module has been added, allowing the GPS to be powered down independently.
- **xCore library update** — The xCore KiCad library has been updated to the latest version.

### Download

Design files (Gerbers, BOM, pick-and-place) for each revision are available on the [releases page](https://github.com/xtech/hw-openmower-yardforce/releases).
