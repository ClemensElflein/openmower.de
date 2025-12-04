---
title: "External Wifi Antenna"
linkTitle: "External Wifi Antenna"
weight: 40
description: >
  To improve the WiFi signal quality, you can add an external antenna.
---

After adding the external antenna, you need to tell the Raspberry Pi CM4 to use the external antenna instead of the built-in one.

### Terminal Cast
<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="external-wifi-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>How to edit the antenna configuration</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        '{{< relref "/docs/Knowledge-Base/external-wifi-antenna" >}}/cast/change-antenna.cast',
        document.getElementById('external-wifi-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>

### Instructions
You can do this by:
- **Run** `sudo nano /boot/firmware/config.txt`
- **Scroll Down** to the `[cm4]` section and:
  - Comment `# dtparam=ant1`
  - Uncomment `dtparam=ant2`
- **Save** <kbd>CTRL</kbd> + <kbd>O</kbd> and **Exit Nano** <kbd>CTRL</kbd> + <kbd>X</kbd>
- **Reboot** the OS by running `sudo reboot`
