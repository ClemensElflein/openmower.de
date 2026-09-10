---
asciinema: true
title: "Externe WLAN-Antenne"
linkTitle: "Externe WLAN-Antenne"
weight: 120
description: >
  Mit einer externen Antenne kannst du den WLAN-Empfang verbessern.
---
Nach dem Anschließen der externen Antenne musst du den Raspberry Pi CM4 so einstellen, dass er diese anstelle der eingebauten Antenne verwendet.

### Terminal-Aufzeichnung
<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="external-wifi-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>So änderst du die Antennenkonfiguration</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        '{{< relref "/docs/Knowledge-Base/installation/external-wifi-antenna" >}}/cast/change-antenna.cast',
        document.getElementById('external-wifi-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>

### Anleitung
Gehe so vor:
- **Führe aus:** `sudo nano /boot/firmware/config.txt`
- **Scrolle nach unten** zum Abschnitt `[cm4]` und:
  - Kommentiere `# dtparam=ant1` aus
  - Entferne das Kommentarzeichen vor `dtparam=ant2`
- **Speichern:** <kbd>Strg</kbd> + <kbd>O</kbd> und **Nano beenden:** <kbd>Strg</kbd> + <kbd>X</kbd>
- **Starte das Betriebssystem neu** mit `sudo reboot`
