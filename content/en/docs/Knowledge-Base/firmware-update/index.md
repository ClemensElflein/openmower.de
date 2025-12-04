---
title: "Firmware Update"
linkTitle: "Firmware Update"
description: >
  This guide shows you how to update the firmware on your Open Mower.
---

{{% alert title="Warning" color="warning" %}}
Early versions of the xCore board have a bug in the bootloader which sometimes prevents the board from being detected by the `openmower` tool.

If you encounter Timeout errors during the firmware installation process, update the bootloader by running: `openmower update-bootloader` and try again.
{{% /alert %}}


To install the firmware to the xCore board, simply run: `openmower update-firmware`. The `openmower` tool will read your environment variables, download the appropriate firmware binary and upload it to the xCore board via Ethernet.


The expected output is shown below:
<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="step-3-2-2-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Example output for <code>openmower update-firmware</code> command.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        '{{< relref "/docs/Knowledge-Base/firmware-update" >}}/cast/openmower-update-firmware.cast',
        document.getElementById('step-3-2-2-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>
