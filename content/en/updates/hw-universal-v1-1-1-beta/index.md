---
title: "Universal Board v1.1.1-beta"
date: 2025-06-19
author: "Clemens Elflein"
description: "EEPROM 3.3V fix, SATA replaced with XH connectors, fuse added, I2C4 EEPROM pins added."
---

[v1.1.1-beta](https://github.com/xtech/hw-openmower-universal/releases/tag/v1.1.1-beta) is a hardware revision fixing a critical EEPROM power issue and switching the inter-module connectors.

### Changes

**EEPROM 3.3V fix** — The 3.3V supply for the EEPROM was not connected in the previous revision. This is now routed correctly, fixing [#6](https://github.com/xtech/hw-openmower-universal/issues/6). Without this fix the core board cannot read the carrier board's EEPROM and therefore cannot auto-detect the attached mower model.

**XH connectors replace SATA** — The inter-module data connectors have been switched from SATA to XH connectors. SATA was a pragmatic choice in early revisions; XH connectors are more appropriate for this use case and easier to source.

**Fuse added** — A fuse has been added to the power path for protection.

**I2C4 EEPROM pins** — Pins for the I2C4 EEPROM interface have been added to the board.

**BOM fix** — Corrections to the bill of materials.

### Download

**[release-hw-openmower-universal-v1.1.1-beta.zip](https://github.com/xtech/hw-openmower-universal/releases/tag/v1.1.1-beta)** — Gerbers, BOM, and pick-and-place files.
