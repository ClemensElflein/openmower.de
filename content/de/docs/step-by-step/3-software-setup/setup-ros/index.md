---
asciinema: true
title: "Schritt 3.3: ROS konfigurieren"
linkTitle: "ROS konfigurieren"
weight: 30
description: >
  Richte ROS so ein, dass es weiß, auf welchem Mähermodell es läuft.
---
## Schritt 3.3.1: ROS-Parameter einstellen
Die ROS-Parameter stellst du ähnlich wie zuvor die Umgebungsvariablen ein.
Führe `openmower configure ros` aus und passe die Parameter an deinen Aufbau an.

Bei der ersten Einrichtung kannst du die meisten Parameter auf ihren Standardwerten belassen.

**Diese Parameter musst du einstellen:**
- **gps/baud_rate**: Die Baudrate des GPS-Moduls. Wenn du Ardusimple GPS mit der bereitgestellten Konfigurationsdatei verwendest, belasse sie bei 921600.
- **gps/protocol**: Das verwendete GPS-Protokoll. Wenn du Ardusimple GPS mit der bereitgestellten Konfigurationsdatei verwendest, belasse es bei „UBX“.
- **gps/datum_lat, gps/datum_long**: Verwende Koordinaten nahe dem geplanten Standort der Ladestation. **Tipp:** Öffne [Google Maps](https://maps.google.com/) und klicke mit der rechten Maustaste auf einen Ort, um die Koordinaten abzulesen. Der Punkt sollte nur wenige Meter von der Ladestation entfernt sein; besonders genau muss er hier nicht sein.
- __ntrip_client/\*__: Trage die NTRIP-Parameter für deine GPS-Basisstation ein.


<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="step-3-2-3-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Beispiel einer ROS-Konfiguration.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        'cast/openmower-configure-ros.cast',
        document.getElementById('step-3-2-3-player'),
        { cols: 130, rows: 30, autoplay: false, loop: true }
    );
</script>
