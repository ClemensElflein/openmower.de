---
asciinema: true
title: "Firmware aktualisieren"
linkTitle: "Firmware aktualisieren"
weight: 100
description: >
  Diese Anleitung zeigt dir, wie du die Firmware deines OpenMower aktualisierst.
---
{{% alert title="Warnung" color="warning" %}}
Frühe Versionen des xCore-Boards haben einen Fehler im Bootloader. Dadurch wird das Board manchmal nicht vom Tool `openmower` erkannt.

Falls bei der Firmware-Installation Timeout-Fehler auftreten, aktualisiere den Bootloader mit `openmower update-bootloader` und versuche es erneut.
{{% /alert %}}


Führe `openmower update-firmware` aus, um die Firmware auf dem xCore-Board zu installieren. Das Tool `openmower` liest deine Umgebungsvariablen, lädt die passende Firmware-Datei herunter und überträgt sie per Ethernet auf das xCore-Board.


Die Ausgabe sollte ungefähr so aussehen:
<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="step-3-2-2-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Beispielausgabe des Befehls <code>openmower update-firmware</code>.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        '{{< relref "/docs/Knowledge-Base/installation/firmware-update" >}}/cast/openmower-update-firmware.cast',
        document.getElementById('step-3-2-2-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>
