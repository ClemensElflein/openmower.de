---
title: Assembling the YardForce Classic 500
linkTitle: Photo Guide
description: >
  Assembling the robot with Vermut's 0.13.x kit. 
tags: [ photo guide, assembly, 0_13_x ]
---

### Connect bottom wires

{{< image-gallery gallery_dir="images/vermut-0.13/connect-bottom-wires" >}}

### Install GPS antenna

The second picture is not perfect, the screw is out of the frame, yellow arrow pointing at it. Also, the GPS plane
itself is
historic from 0.9.3, yours will be green and shiny.

{{< image-gallery gallery_dir="images/vermut-0.13/install-gps-antenna" >}}

### Install external Wi-Fi adapter (optional)

{{% alert title="🔧" color="warning" %}}
This is optional and will vary with the size and shape of your adapter, because right now there is no "official"
external adapter and people are installing all kinds of stuff. Depicted is `Alfa USB Adapter AWUS036NHV`, on the
`rtl8188eu` chip using [custom driver](https://github.com/aircrack-ng/rtl8188eus).
{{% /alert %}}

{{% alert title="⚠️" color="danger" %}}
Important: If you install an external WiFi USB adapter, it might prevent you from seeing the OpenMower hotspot during initial setup. For first startup, it's recommended to keep the external adapter disconnected until you've completed the initial WiFi configuration. After successfully connecting to your network, you can then connect the external adapter.
{{% /alert %}}

{{< image-gallery gallery_dir="images/vermut-0.13/install-external-wifi-adapter" >}}

### Assemble mainboard

This step assumes that you did all previous configuration steps from the documentation.

{{< image-gallery gallery_dir="images/vermut-0.13/assemble-mainboard" >}}

### Connect and screw mainboard

{{< image-gallery gallery_dir="images/vermut-0.13/connect-and-screw-mainboard" >}}

### Modify rain sensor cable (kit version specific)

{{% alert title="🔧" color="warning" %}}
Kits till mid-2023 included incorrect rain sensor cable that has female connectors on both sides. This is a hacky
example of how this can be fixed. Alternatively, you can cut them and just solder together.
{{% /alert %}}

{{< image-gallery gallery_dir="images/vermut-0.13/modify-rain-sensor-cable" >}}

### Assemble cover

{{% alert title="🔧" color="warning" %}}
This section assumes that you are completely replacing the stock UI board with custom one. There is an experimental
option to reuse stock board with custom firmware. If you are going to go this path - everything that is cover-related
would be different for you. You can find more information in Discord, as of now it's work in progress.
{{% /alert %}}

On the photos you see an old patched version of rain sensor cable (see above). Yours might just fit in normally.

{{< image-gallery gallery_dir="images/vermut-0.13/assemble-cover" >}}

### Connect cover to bottom

{{< image-gallery gallery_dir="images/vermut-0.13/connect-cover-to-bottom" >}}

### Close the cover

Alight cutting height knob with mower motor, close the cover, push where needed to snap the latches. Or even leave it
lying on while you testing the setup, maybe you'll need to open it again.
