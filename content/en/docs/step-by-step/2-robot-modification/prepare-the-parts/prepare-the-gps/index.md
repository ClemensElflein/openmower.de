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


{{% tab header="By-Nav M10+M20 USB offline" %}}

<div class="prep-gps-um9xx-tab">
  
## Using USB (cutecom)

**For using it with the M20, replace every COM1 with COM2.**

1. Connect your M10 to your PC using the supplied USB-C cable.
2. Open the recommended terminal program, cutecom.
3. Connect at 115200 baud.
4. You should see readable key/value style output. If not, check cable, port, and permissions.
5. Make sure your line-end termination is set to **CR/LF**.
6. In cutecom, you may switch off the output — it keeps running but won't be displayed.
7. Factory reset and disable cyclic outputs by entering the following commands, line by line:

   > FRESET<kbd>↵ Enter</kbd><br>
   > (After `FRESET` the module may take a few seconds to respond.)<br>

   > UNLOGALL<kbd>↵ Enter</kbd><br>

8. Switch the output back on in cutecom.
9. Re-check the connection with the simple command:

   > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

   You should see readable output.

10. Apply the rover configuration:

    > SERIALCONFIG COM1 460800<kbd>↵ Enter</kbd><br>

11. Re-check the connection using:

    > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

    You should still see readable output because we are connected on COM3. If not, check the connection and baud rate.

12. Continue with the rover configuration:

    > LOG COMCONFIG ONCE<kbd>↵ Enter</kbd><br>   (COM1 should show 460800 now)<br>
    > RTKTYPE ROVER<kbd>↵ Enter</kbd><br>
    > RTKTYPE<kbd>↵ Enter</kbd><br>
    > RTKTIMEOUT 5<kbd>↵ Enter</kbd><br>
    > RTKTIMEOUT<kbd>↵ Enter</kbd><br>

13. Define the cyclic output:

    > LOG COM1 GPGSV ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPRMC ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGSA ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPVTG ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGST ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGGA ONTIME 0.1<kbd>↵ Enter</kbd><br>

14. Finally, save the changes to flash memory:

    > SAVECONFIG<kbd>↵ Enter</kbd><br>

    **Pay attention to the `SAVECONFIG` command** — it stores settings so they survive power cycles.

15. Unplug the USB cable from the M10 module and mount it to the CarrierBoard (solder headers first if needed).

16. Remember to adapt the baud rate in the OpenMower ROS configuration:

```yaml
gps:
  baud_rate: 460800
  protocol: "NMEA"
```

</div>

{{< /tab >}}

{{% tab header="By-Nav M10+M20 TCP online" %}}

<div class="prep-gps-um9xx-tab">

## Using TCP (by_connect)

This section works on Linux and Windows (on Linux, run by_connect under Wine). You need to postpone this step until your OpenMower system is running. The configuration is done remotely over TCP.

### Prerequisites

- A WitMotion ByNav M10 GPS board (default baud rate: 115200)
- An OpenMower with OpenMowerOS installed
- A Windows or Linux PC
- [by_connect software](https://www.bynav.com/media/upload/LargeFile/BY_Connect.zip) from bynav.com
- [Interface protocol description (PDF)](https://www.bynav.com/media/upload/cms_15/UG017_Interface%20Protocol_Bynav.pdf) — valid for all ByNav modules (M10, M20, etc.)

**For using it with the M20, replace every COM1 with COM2.**

1. Mount the M10 to the CarrierBoard (solder headers first if needed).
2. Set the baud rate in the OpenMower ROS configuration to 115200:

```yaml
gps:
  baud_rate: 115200
  protocol: "NMEA"
```

3. Connect your M10 via TCP-serial by running `openmower expose-gps` from your OpenMower SSH terminal:
   ![openmower expose](openmower_expose-gps.png)

4. Open by_connect on your PC (download from bynav.com; on Linux, start it with Wine) — connect as **TCP Client** to OpenMower port 2000 (no baud rate needed):
   ![by_connect TCP Client](by_connect_tcp_client.png)

5. You should see readable key/value style output. If not, check the connection.
6. Make sure your line-end termination is set to **CR/LF**.
7. In by_connect, you may switch off the output — it keeps running but won't be displayed:
   ![by_connect input](by_connect_input.png)

8. Factory reset and disable cyclic outputs by entering the following commands, line by line:

   > FRESET<kbd>↵ Enter</kbd><br>
   > (After `FRESET` the module may take a few seconds to respond.)<br>

   > UNLOGALL<kbd>↵ Enter</kbd><br>

9. Switch the output back on in by_connect.
10. Re-check the connection with:

    > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

    You should see readable output.

11. Apply the rover configuration:

    > SERIALCONFIG COM1 460800<kbd>↵ Enter</kbd><br>

12. Re-check the connection:

    > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

    The output will be unreadable now because the baud rate has changed. Close the connection, update the baud rate to **460800** in the OpenMower ROS configuration, and reconnect via `openmower expose-gps`:
    ![change baud rate](changeBaud1.png)

13. Reopen by_connect, connect as TCP Client again, and verify readable output with:

    > LOG COMCONFIG ONCE<kbd>↵ Enter</kbd><br>

14. Continue with the rover configuration:

    > RTKTYPE ROVER<kbd>↵ Enter</kbd><br>
    > RTKTIMEOUT 5<kbd>↵ Enter</kbd><br>

15. If all worked as expected (you receive `ok` responses), save the settings to flash memory — otherwise disconnect, power cycle the OpenMower, and start over:

    > SAVECONFIG<kbd>↵ Enter</kbd><br>

16. Define the cyclic output:

    > LOG COM1 GPGSV ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPRMC ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGSA ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPVTG ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGST ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGGA ONTIME 0.1<kbd>↵ Enter</kbd><br>

17. Save the changes to flash memory:

    > SAVECONFIG<kbd>↵ Enter</kbd><br>

**Pay attention to the `SAVECONFIG` command** — it stores settings so they survive power cycles.

</div>

{{< /tab >}}

{{< /tabpane >}}

Continue with [Step 2.2: Prepare the SD Card]({{< relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-sd-card" >}})