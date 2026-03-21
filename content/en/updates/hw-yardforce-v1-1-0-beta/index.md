---
title: "YardForce Carrier Board v1.1.0-beta"
date: 2025-06-19
author: "Clemens Elflein"
description: "Fan voltage selector, fuses, AGPIO on extension headers, silkscreen improvements."
---

[v1.1.0-beta](https://github.com/xtech/hw-openmower-yardforce/releases/tag/v1.1.0-beta) brings a handful of hardware improvements to the YardForce v2 carrier board.

### Changes

**Fan voltage selector** — A voltage selector has been added for the fan connectors, allowing the fan supply voltage to be configured. Fan connector silkscreen labels have been added to match. The third FAN connector has been removed and the silkscreen documentation updated accordingly, resolving [#3](https://github.com/xtech/hw-openmower-yardforce/issues/3).

**Fuses** — Fuses have been added to the power path for protection.

**AGPIO on extension headers** — The extension header pins now use AGPIO, which is more appropriate for analog and general-purpose signal use on the STM32.

**Silkscreen improvements** — General silkscreen additions and corrections across the board.

### Download

**[release-hw-openmower-yardforce-v1.1.0-beta.zip](https://github.com/xtech/hw-openmower-yardforce/releases/tag/v1.1.0-beta)** — Gerbers, BOM, and pick-and-place files.
