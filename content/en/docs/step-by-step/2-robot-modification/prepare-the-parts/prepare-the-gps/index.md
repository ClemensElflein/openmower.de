---
title: "Step 2.1: Prepare the GPS"
linkTitle: GPS
weight: 1
description: >
  Update Firmware and configure the GPS modules.
tags: [gps, gps-rtk, simplertk2b, zed-f9p, ntrip, unicore, um9x, um9xx, um960, um980, um982]
---

{{< tabpane text=true >}}
{{% tab header="**GPS module**:" disabled=true /%}}
{{% tab header="Ardusimple F9P" %}}


## Update Firmware and configure the GPS board

{{% alert title="Info" color="info" %}}
There is a tutorial video available for this step of the process! <br/>
Check my YouTube video here: [<i class="fa fa-brands fa-youtube"></i> Video](https://youtu.be/_bImqD-pQSA?t=981)
(time 16:21 - 17:15)
{{% /alert %}}


### Prerequisites

- **An Ardusimple F9P GPS board**
- **A Micro USB Cable**
- **A Windows PC**
- **Latest v1 version of the u-center software:**<br/>
  🔗&nbsp;[https://www.u-blox.com/en/product/u-center](https://www.u-blox.com/en/product/u-center)<br/>
  Don't get u-center V2, you will need u-center v1 for the F9P.
- **The GPS configuration file**<br/>
  🔗&nbsp;<a href="https://raw.githubusercontent.com/ClemensElflein/OpenMower/refs/heads/main/configs/GPSConfig/robot-fw-1_51.txt" target="_blank">robot-fw-1_51.txt</a><br/>
  This will open in a new browser tab.  Use <kbd>Ctrl</kbd>+<kbd>S</kbd> to download the file.


### Step 2.1.0: Update Firmware

{{% alert title="Warning" color="warning" %}}
The F9P now exists in multiple variants. The firmware below is for the L1 + L2 version. Make sure that on the u-blox chip, it says one of the following: **ZED-F9P-02B, ZED-F9P-04B or ZED-F9P-05B!**.

If it's a different board, **don't** use the linked firmware, get it from u-blox.com directly.
{{% /alert %}}

Update the firmware of your Ardusimple board to version [`ZED-F9P HPG 1.51` - *link here*](https://content.u-blox.com/sites/default/files/2024-11/UBX_F9_100_HPG151_ZED_F9P.6c43b30ccfed539322eccedfb96ad933.bin). There's a guide on the [Ardusimple Website](https://www.ardusimple.com/zed-f9p-firmware-update-with-simplertk2b/).


### Step 2.1.1: Open u-center and connect to your GPS

After installing u-center, connect your Ardusimple board using the "Power+GPS" USB socket to your Windows computer. You should see the blue LEDs of the board come on and Windows should recognize the device as a COM port.
With the module connected to your PC, open the u-center software. 

In u-center, first connect to your board by selecting the appropriate COM port in the `Receiver -> Connection` menu.


### Step 2.1.2: Transfer the configuration to the GPS

![Transfer Settings to u-center](transfer-gps-settings.jpg)

After successfully connecting to the board, you can transfer
the previously downloaded configuration file `robot-fw-1_51.txt` by opening the window `Tools -> Receiver Configuration ...`. In this window you open the `robot-fw-1_51.txt` using the `...` button and then transfer the configuration to the GPS by clicking the `Transfer File -> GNSS` button.


### Step 2.1.3: Save configuration to Flash

![Save Settings to Flash](save-settings-to-flash.jpg)

In order to keep the GPS configured even after powering it down, you need to save the current configuration to Flash memory. In order to do this, select `View -> Configuration View`. In the new window you need to select `CFG (Configuration)` in the list on the left side and then enable `Save current configuration`. Make sure that `0 - BBR` and `1 - FLASH` are both selected on the right side of the window. Once that's done, click the `Send` button in the lower toolbar of the window.

Once successful, there will be a timer showing on the upper right side of the window. This is the timer since the last message was sent to your GPS board. It should be `0s` directly after clicking `Send`.


### Step 2.1.4: Done 🎉

Your GPS is now configured for use with the Open Mower software. You can disconnect it from your Windows PC.

{{% /tab %}}



{{% tab header="WitMotion Unicore UM9xx" %}}

<div class="prep-gps-um9xx-tab">

1. Connect your UM9xx to your PC using the supplied USB-C cable
1. Open a serial terminal (minicom, miniterm, CuteCom, etc.) at 115200 baud
1. Take attention that your line-end termination has to be CR/LF
1. Send `CONFIG`<kbd>↵ Enter</kbd> to verify the connection. You should see readable key/value style output. If not, check cable, port, and permissions.
1. Reset and switch the baud rate to 921600 by entering the following commands, line by line:
   > FRESET<kbd>↵ Enter</kbd><br>
   > CONFIG COM1 921600<kbd>↵ Enter</kbd>

   (After `FRESET` the module may take a few seconds to respond.)
1. Re-check connection with the simple `CONFIG` command. If you don't get similar results than before, change your serial terminal speed to 921600 baud (re-open if necessary) and run `CONFIG` again, till your get a reasonable response
1. Apply the rover configuration by entering the following commands, line by line:
   > MODE ROVER UAV<kbd>↵ Enter</kbd><br>
   > GPGSV COM1 2<kbd>↵ Enter</kbd><br>
   > GPRMC COM1 1<kbd>↵ Enter</kbd><br>
   > GPGSA COM1 1<kbd>↵ Enter</kbd><br>
   > GPVTG COM1 1<kbd>↵ Enter</kbd><br>
   > GPGST COM1 1<kbd>↵ Enter</kbd><br>
   > GPGGA COM1 0.2<kbd>↵ Enter</kbd><br>
   > SAVECONFIG<kbd>↵ Enter</kbd>

   Take attention to the `SAVECONFIG` command, which stores settings so they survive power cycles.
1. Unplug the USB cable from the UM9x module and mount it to the CarrierBoard (solder required headers first if required).

</div>

{{< /tab >}}

{{< /tabpane >}}

Continue with [Step 2.2: Prepare the SD Card]({{< relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-sd-card" >}})