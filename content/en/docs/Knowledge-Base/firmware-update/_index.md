---
title: "Firmware Update"
linkTitle: "Firmware Update"
description: >
  This guide shows you how to update the firmware on your Open Mower.
resources:
- src: "**.png"
---


## Prerequisites

This update guide assumes that you have the following:

- A mower with the OpenMowerOS running on it.

- **Important:** verified that the `/boot/openmower/mower_config.txt` file has the correct hardware version set (`OM_HARDWARE_VERSION`). If this is wrong, the wrong firmware will be installed on your device. Check the [Manual Firmware Installation]({{% relref "/docs/knowledge-base/manual-firmware-installation" %}}) guide on how to find that value.

- The Raspberry Pi is running, and you are able to connect to it via `ssh`

- The mower is connected to the internet


## Step 1: Run the Firmware Update Script

The OpenMowerOS image contains a firmware update script which will download and install the latest firmware version for you.

In order to run the script, execute the following commands:
{{< tabpane text=true >}}
{{% tab header="**OpenMowerOS version**:" disabled=true /%}}
{{% tab header="0.1.0" %}}
```bash
# Make sure that you are in your home directory (the script is located there):
cd ~/
# Execute the script:
~/fetch_and_upload_firmware.sh
```
{{% /tab %}}
{{< /tabpane >}}


If everything works as expected, the output should look like this:
<div class="container">
<div class="row justify-content-md-center">
<div id="player" class=""></div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        '538389.cast',
        document.getElementById('player'),
        { cols: 100, rows: 24, autoplay: true, loop: true }
    );
</script>


## Step 2: Done 🎉

That's everything you need to do.
