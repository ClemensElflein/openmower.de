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

## Meaning of LEDs and buttons

Borrowed from Apehaenger's [custom firmware project](https://github.com/Apehaenger/CoverUI/tree/main/Firmware/CoverUI/yfc500#usage).

* 2hr-8hr LEDs act as 4 digit progressbar for GPS quality. Blink = uncalibrated
* Home button: Stop mowing and go back home to dock
* Play button: Start mowing of recorded area(s)
* S1: On = ROS is running but idle, Blink-slow = ROS in autonomous mode, Blink-fast = ROS in nirvana?
* S2 LED: >TODO<
* S2 Button: Short press, skip over to next mowing area. Long press (>= 3s), delete all recorded areas!
* Lock Button: Clear emergency state (probably long press >=3s)
* Mon-Sun as 7 digit progressbar for battery charge state (only in undocked state)
* Lifted: Show emergency states. >TODO<
* Wire: Also indicate a poor GPS. On = < 25%, Blink-fast = < 50%, Blink-slow < 75%, Off >= 75%
* Battery: On = Battery empty
* Charging LED: Fast blink = empty. Slow blink = approx. 1/2 charged. On = Fully charged.
