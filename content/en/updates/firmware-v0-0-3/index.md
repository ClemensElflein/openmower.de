---
title: "Firmware Release v0.0.3"
date: 2026-03-06
author: "Clemens Elflein"
description: "v0.0.3 brings significant SABO / John Deere support, battery management, dynamic power management, and input service improvements."
---

Firmware [v0.0.3](https://github.com/xtech/fw-openmower-v2/releases/tag/v0.0.3) is out. This release is a big step forward for SABO / John Deere users and brings a handful of robustness improvements that benefit all platforms.

### SABO / John Deere Support

Most of the work in this release went into maturing SABO support, driven almost entirely by [@Apehaenger](https://github.com/Apehaenger) — huge thanks!

The SABO carrier board can now be considered properly supported:

- **BMS integration** — The SBS/SABO battery management system is now integrated, giving the firmware visibility into battery state, charge levels, and health.
- **Dynamic power management** — Power management functions are now implemented dynamically and wired up for the SABO platform, allowing the firmware to manage power states intelligently rather than statically.
- **COBS parsing efficiency** — The YardForce ESC driver received a character-match interrupt to make COBS frame parsing more efficient, reducing CPU load during serial communication.

### Input Service Improvements

The input handling layer got a round of improvements:

- **Configurable delays** — Input service delays are now configurable, making it easier to tune debounce and hold behaviour per platform.
- **Key press injection** — A mechanism to inject synthetic key presses has been added, which is useful for automated testing and hardware-in-the-loop simulation.
- **Brief-input emergency trigger** — The firmware now correctly triggers an emergency stop for inputs that are only active for a very short time. Previously, a momentary signal could be missed — this is now fixed, improving safety on all platforms.

### Internals

- `xbot_framework` and the `services` submodule have both been updated to their latest versions.
- The SystemView build (used for real-time tracing and debugging) has been fixed.

### Download

Grab the firmware bundle from the [v0.0.3 release page](https://github.com/xtech/fw-openmower-v2/releases/tag/v0.0.3):

- **`fw-openmower-v2-v0.0.3.zip`** — contains binaries for all supported carrier boards
