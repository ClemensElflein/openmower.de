---
title: Cover UI board assembly
linkTitle: Cover UI
weight: 45
description: >
  This describes custom Cover UI board assembly.
---

{{% alert title="Using the kit" color="info" %}}
Kit will come with board partially assembled: ICs, buttons and minor SMD components pre-soldered.

Early boards marked `WIP` had a blue patch wire. You don't need it, ignore it on the photos.
{{% /alert %}}

* solder front side LEDs. Don't forget spacers. Align cut on the LED with barely visible cut on the silkscreen. To the right if looking from the front side.
* solder back side connectors
* solder back side buzzer (round pin is `+`). Early versions had silkscreen `+` on wrong side, be careful. 
* solder Pico Dev board, either directly to the board or use pin headers (not included in the kit)

{{< image-gallery gallery_dir="/photo-guide/cover-ui-board" >}}

After that, upload the cover UI firmware to Pico Board: https://github.com/ClemensElflein/CoverUI/releases/latest

You need `.uf2` file from `firmware.zip`. Hold `BOOT` button on Pico, insert USB and drag `.uf2` to Pico disk drive. 

This is described in more details in [MicroPython guide](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#drag-and-drop-micropython), you can follow that, just use our `.uf2` file instead.
