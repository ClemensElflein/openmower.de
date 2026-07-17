---
title: "Classic 500(B)"
linkTitle: "Classic 500(B)"
weight: 10
description: >
  Modification Guide for YardForce Classic 500(B) with Carrierboard version ≥ 1.2.0
---


{{% alert title="Carrierboard ≥ 1.2.0 only!" color="warning" %}}
This guide is exclusively for **Carrierboard version ≥ 1.2.0**!<br>
![v1.2.0 Carrierboard identification](../carrierboard_version_v1.2.0.jpg)<br>
{{% /alert %}}


## Prerequisites

### Things you will need:
- **YardForce Classic 500(B)**
- **Open Mower Mainboard** with all modules installed (xCore, CM4, GPS, 3x ESCs)
- **GPS Holder (3d printed part)**, **GPS Antenna**, 2x M2,5x20 screws, 2x M4x16 screws for the GPS holder _(when using Ardusimple RTK2B)_

### Tools you will need:
- **Some basic screwdrivers** for disassembly and assembly.

## Step 2.4.1: Disassemble the Robot
The first step is to disassemble up the robot.
This is a bit tricky in some parts, so I recommend you checking my YouTube video here: [<i class="fa fa-brands fa-youtube"></i> YouTube Video](https://youtu.be/_bImqD-pQSA?t=148). The relevant time is: 2:25 - 5:08.
**Do not** follow the video further than that, because it is outdated.

Alternatively, here is a picture guide of the disassembly process:

### Unscrew top cover

{{< image-gallery gallery_dir="images/disassemble-mower/unscrew-the-cover" >}}


### Pry the cover

This is a bit tricky in some parts, so I recommend you checking YouTube video
here: [<i class="fa fa-brands fa-youtube"></i> YouTube Video](https://youtu.be/_bImqD-pQSA?t=148). The relevant time is:
2:25 - 5:08.

{{< image-gallery gallery_dir="images/disassemble-mower/pry-the-cover" >}}


### Unplug the cover

2 small wires on the front going to wheel sensors, and 1 wide wire from mainboard to cover UI board.
Screwdriver is in the pictures for illustrative purposes, you can simply hold it with your hand.

{{< image-gallery gallery_dir="images/disassemble-mower/unplug-the-cover" >}}


### Unplug the mainboard

{{< image-gallery gallery_dir="images/disassemble-mower/unplug-the-mainboard" >}}


### Remove front PCB

{{< image-gallery gallery_dir="images/disassemble-mower/remove-front-pcb" >}}


## Step 2.4.2: Remove Stock Electronics

You will need to remove these stock electronics:
- Mainboard
- Perimeter Sensor (slim PCB in the front of the robot).

Keep the battery in place.

## Step 2.4.3: Small Preparations

{{< tabpane text=true >}}
{{% tab header="**Choose your option**:" disabled=true /%}}

{{% tab header="Witmotion UM9xx/ByNav-Mxx" text=true %}}

### Assemble Witmotion GPS Module

<img class="special-img-class" style="width:50%" src="./images/WTRTK-GPS.jpg" />

Install your Witmotion UM9xx or ByNav-Mxx GPS module and the included Witmotion pigtail-cable as shown in the illustration.

{{% /tab %}}


{{% tab header="Ardusimple RTK2B" text=true %}}

### Assemble GPS Antenna Holder

![GPSHolder.jpg](images/GPSHolder.jpg)
Take the GPS antenna holder and assemble it as shown in the picture.

{{% /tab %}}

{{< /tabpane >}}



## Step 2.4.4: Install OpenMower Electronics

Now you can install the OpenMower mainboard and the GPS antenna holder we prepared earlier.
- Put the mainboard into the mower just as the original board was installed <br/>(in the rear it sits between plastic tabs, on the front there are two screws holding it in place).
- To fit the GPS holder into the mower, you need need to remove two of the white plastic cable ties by just pulling them upwards. Then plug it into the corresponding holes and fix it with one screw you saved earlier _(only when using Ardusimple RTK2B)_.
- Connect all cables.


**The connections are as follows:**
1. Mower Motor Sensor
2. Main Motor Connector (Drive motors, mower motors, sensors)
3. Power Connector
4. Charging Contacts
5. USB Connector on the Rear of the Robot
6. OEM CoverUI Board (Emergency sensors, rain sensor, LEDs, buttons)
7. GPS Antenna

![Mainboard Connections](./images/MainboardConnections.jpg)

## Step 2.4.5: Install external WiFi Antenna (optional)
If you want to use an external WiFi antenna for better reception, installation is simple.

![ExternalAntenna.jpg](images/ExternalAntenna.jpg)

## Prerequisites

### Things you will need:
- **WiFi Antenna Mount:** 3D printed part available on [Printables](https://www.printables.com/model/1504184-openmower-yardforce-classic-500-wifi-antenna-mount)
- **Two Screws** you can use the screws from the front sensor we removed earlier
- **WiFi Antenna with Cable** You can get it from [Amazon](https://amzn.to/48iknlw)

### Steps:
1. Mount the antenna to the holder
2. Mount the holder to the mower using the two screws
3. Connect the antenna to the CM4 board
4. Zip tie the cable to the corner of the PCB


## Step 2.4.6: First Startup

It's time to power the robot up by hitting the switch at the back of the robot.

{{% alert title="Warning" color="warning" %}}
If you see / smell anything unexpected, turn the switch off **immediately!**

This includes but is not limited to:
- Smoke / Fire
- Smell of hot electronics
- Blown Fuses
  {{% /alert %}}


Some battery packs don't like the inrush current and will turn off immediately. If this happens, you can try to turn the switch off and on again and it should work.

Once turned on, LEDs should start blinking on the ESCs, the GPS, the xCore board and the mainboard.
**Keep the robot turned on for at least five minutes to maker sure the CM4 boots up properly. It does setup during the first boot.**

{{% alert title="Info" color="info" %}}
It's a good idea to place the mower into the docking station, so that the battery doesn't drain.

In this state, the battery does not charge, because the core board does not have the correct firmware installed, but the docking voltage will still be used to power the electronics, so the battery will not drain.
{{% /alert %}}

If everything seems healthy, proceed to the [Software Setup]({{< relref "/docs/step-by-step/3-software-setup" >}}).

Otherwise, **stop here and ask for help on the Discord server**.
