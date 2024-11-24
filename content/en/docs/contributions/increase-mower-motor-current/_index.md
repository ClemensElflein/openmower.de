---
title: Increase mower motor to 6A
linkTitle: Mower motor to 6A
description: >
  Updating motor configuration for more mowing power.
---

Author: ow@discord

YardForce Classic Mower Motor: https://gist.github.com/olliewalsh/fcc2e6d7852cad5c1f64ce0837306a66

Alternative config was made by Tomm: https://discord.com/channels/958476543846412329/961803746399101008/1110669606038806698


Battery current limit is 3a, motor current limit is 6a. RPM limited to 3500. Disabled backing off when temp increases or voltage drops. I would use a 6amp fuse, seen drive motors report over 1a sometimes.

Instructions:
Open cover, replace fuse, upload central xESC config with [VESC-TOOL](https://vesc-project.com/vesc_tool).
