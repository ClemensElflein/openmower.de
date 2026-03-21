---
title: "Universal Board v1.0.0-beta — v1.0.2-beta"
date: 2024-10-21
author: "Clemens Elflein"
description: "Initial release of the OpenMower Universal carrier board, with two quick follow-up fixes."
---

Three beta releases shipped in quick succession in October 2024, establishing the initial hardware design for the Universal carrier board.

### v1.0.0-beta — 2024-10-19

The first public release of the Universal carrier board design. The Universal board is designed to work with a wide range of robot mower platforms and can be broken apart into separate modules if the full board doesn't fit a given chassis. Power can be delivered via screw terminals or XT30 plugs; motor connections can be soldered directly or via screw terminals. GPS options include the Ardusimple F9P Arduino board, the Ardusimple micro, or the UM9XX module.

### v1.0.1-beta — 2024-10-19

Released the same day with two corrections:

- Switched to non-PCB-mount XT30 connectors.
- Added the JLC part number for the xCore connector to the BOM.

### v1.0.2-beta — 2024-10-21

- **Extension port added** — An extension port has been added for custom add-ons.
- Silkscreen labels removed to clean up the board layout.

### Download

Design files (Gerbers, BOM, pick-and-place) for each revision are available on the [releases page](https://github.com/xtech/hw-openmower-universal/releases).
