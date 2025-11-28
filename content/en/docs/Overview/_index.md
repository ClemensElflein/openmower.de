---
title: "Overview"
linkTitle: "Overview"
weight: 1
description: General information about the Open Mower project.
carousel:
  - image: open_mower_app_1.jpg
  - image: open_mower_app_2.jpg
  - image: homeassistant_dashboard.png
  - image: smarthome_tracker.png
---

### Why OpenMower exists

**OpenMower** is an open-source initiative that turns off-the-shelf lawn robots into reliable RTK-guided mowers. The project started as a garage prototype and matured into a community-maintained platform with reusable electronics, software, and documentation.

Watch the original introduction video for a quick tour of the concept:

<a href="https://www.youtube.com/watch?v=BSF04i3zNGw" target="_blank"><img src="https://user-images.githubusercontent.com/2864655/161540069-f4263fa7-a47b-49d2-a7bc-d1cdc3a47704.jpg" alt="OpenMower video thumbnail" /></a>



### What you get

- **Wire-free navigation:** Precise RTK GPS positioning replaces perimeter wires and enables multiple mowing zones.
- **Modern control app:** A responsive web interface works on desktop and mobile for setup, scheduling, and manual control.
- **Smart home integration:** Native Home Assistant integration exposes real-time telemetry (battery, motors, sensors) and lets you automate tasks like pausing for rain.
- **Community-tested electronics:** Modular v2 hardware combines a CM4 + STM32-based core board, and carrier boards for popular mower frames.
- **Transparent, hackable stack:** Firmware, App and ROS software sources are open source, so you can inspect, customize, and contribute.
- **Safety-first design:** Dedicated emergency stop loops and watchdogs safeguard blades and drivetrain.

{{< carousel height="500" unit="px" items="4" duration="3000" >}}


### Supported hardware

OpenMower works by replacing the stock electronics inside compatible chassis. Popular builds include:

- YardForce Classic 500(B) and SA series
- SABO MOWit 500F (Series I & II)
- John Deere Tango E5 (Series I & II)

Not sure whether your mower fits? Start with the [Compatible Mowers]({{% relref "/docs/knowledge-base/compatible-mowers" %}}) list and, if still unsure, ask in Discord before buying hardware. The universal carrier board also allows advanced builders to adapt additional models once basic requirements (wheel encoders, supported voltage, space for the mainboard) are met.

---

### Where to go next

- [Getting Started]({{% relref "/docs/getting-started/" %}}): Required skills, compatibility flowchart, and the full build sequence.
- [Compatible Mowers]({{% relref "/docs/knowledge-base/compatible-mowers" %}}): Confirm your chassis before buying hardware.
- [Shopping List]({{% relref "/docs/knowledge-base/shopping-list" %}}): Detailed bill of materials, including RTK components.
- [Links]({{% relref "/docs/links" %}}): GitHub repos, Discord invite, videos, and other resources.


### Roadmap

OpenMower keeps evolving through community contributions. Active areas include:

- Obstacle detection and avoidance
- Improved scheduling and multi-area workflows
- Expanded carrier boards and accessories for new mower frames
- Additional tooling around map editing and diagnostics

If you want to help, join the Discord server, report issues, or contribute docs/code.
