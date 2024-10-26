---
title: "Prepare the Robot"
linkTitle: Chassis
weight: 30
description: >
  Disassemble the robot, remove the existing mainboard and add optionally a USB connector.
---

### Prerequisites

- **YardForce Classic 500**
- **Some basic screwdrivers**


### Step 1: Open The Robot

The first step is to open up the robot. This is a bit tricky in some parts, so I recommend you checking my YouTube video here: [<i class="fa fa-brands fa-youtube"></i> YouTube Video](https://youtu.be/_bImqD-pQSA?t=148). The relevant time is: 2:25 - 5:08.


### Step 2: Remove Stock Electronics

You will need to remove these stock electronics:
- Mainboard
- Perimeter Sensor (slim PCB in the front of the robot).
- All cables in the orange cover (emergency stop).

Keep the battery in place.


### Step 3 **Optional**: Modify USB Socket

{{% alert title="🧰" %}}
The kit includes compatible USB socket adapter starting version 0.12.
{{% /alert %}}

The YardForce classic has a USB socket on the back of the robot. Unfortunately for us, this socket has some non-standard connector on the inside.

If you want to use this USB socket on the back of the robot (for example for controlling the robot using a gamepad like shown in the first video), you will need to add a USB A plug to the USB cable and plug it into the Raspberry Pi.

This way the USB port at the back of the robot is wired directly to the Raspberry Pi.
