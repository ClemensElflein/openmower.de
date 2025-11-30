---
title: "YardForce Classic 500(B)"
linkTitle: "YardForce Classic 500(B)"
weight: 10
description: >
  Modification Guide for YardForce Classic 500(B)
---
{{% alert title="v2 Hardware Only!" color="warning" %}}
This guide here is for OpenMower v2.x Hardware!
If you have v1 Hardware, follow the legacy docs [here](https://openmower.de/archive/v1.0.2/docs/), because for v1 hardware you will also need to modify the docking station!

You have **v1 hardware**, if:
- You are using a full-size Raspberry Pi
- Your mainboard shows version **v0.xx**
{{% /alert %}}

## Prerequisites

- **YardForce Classic 500**
- **Some basic screwdrivers**

## Step 1: Disassemble the Robot
The first step is to disassemble up the robot.
This is a bit tricky in some parts, so I recommend you checking my YouTube video here: [<i class="fa fa-brands fa-youtube"></i> YouTube Video](https://youtu.be/_bImqD-pQSA?t=148). The relevant time is: 2:25 - 5:08.
**Do not** follow the video further than that, because it is outdated.

Alternatively, here is a picture guide of the disassembly process:

### Unscrew top cover

{{< image-gallery gallery_dir="images/vermut-0.13/unscrew-the-cover" >}}


### Pry the cover

This is a bit tricky in some parts, so I recommend you checking YouTube video
here: [<i class="fa fa-brands fa-youtube"></i> YouTube Video](https://youtu.be/_bImqD-pQSA?t=148). The relevant time is:
2:25 - 5:08.

{{< image-gallery gallery_dir="images/vermut-0.13/pry-the-cover" >}}


### Unplug the cover

2 small wires on the front going to wheel sensors, and 1 wide wire from mainboard to cover UI board.
Screwdriver is in the pictures for illustrative purposes, you can simply hold it with your hand.

{{< image-gallery gallery_dir="images/vermut-0.13/unplug-the-cover" >}}


### Unplug the mainboard

{{< image-gallery gallery_dir="images/vermut-0.13/unplug-the-mainboard" >}}


### Remove front PCB

{{< image-gallery gallery_dir="images/vermut-0.13/remove-front-pcb" >}}


### Remove cover UI board

{{% alert title="Info" color="info" %}}
This section assumes that you are completely replacing the stock UI board with a custom one. There is an option to reuse stock board by flashing it with custom firmware.
If you are going to go this path - leave it in place. You can find more information [in the Cover UI Repo *](https://github.com/ClemensElflein/CoverUI/blob/main/Firmware/CoverUI/YardForce/README.md).

\* Would be nice if someone could transfer this to the Knowledge Base on this website though.
{{% /alert %}}

{{< image-gallery gallery_dir="images/vermut-0.13/remove-cover-ui-board" >}}


### Step 2: Remove Stock Electronics

You will need to remove these stock electronics:
- Mainboard
- Perimeter Sensor (slim PCB in the front of the robot).
- All cables in the orange cover (emergency stop).

Keep the battery in place.
