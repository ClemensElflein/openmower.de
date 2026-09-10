---
asciinema: true
title: "Schritt 3.2: Grundeinrichtung (Umgebungsvariablen, Firmware und xESC)"
linkTitle: "Grundeinrichtung"
weight: 20
description: >
  Richte die Umgebungsvariablen ein, installiere die Firmware auf dem xCore-Board und konfiguriere die xESC-Motorcontroller.
---
{{% toc %}}

## Überblick
### Arten von Einstellungen
Die Roboterkonfiguration besteht aus zwei Teilen:
- **Umgebungsvariablen:** Sie legen Mähermodell, Hardware-Version und die zu verwendende ROS-Version fest. **Diese richten wir zuerst ein.**
- **ROS-Parameter:** Sie bestimmen das Verhalten von ROS im Betrieb, etwa GPS-Einstellungen, Mähverhalten und MQTT-Konfiguration für das Smart Home.

### Das Kommandozeilenwerkzeug `openmower`
Das von uns entwickelte Kommandozeilenwerkzeug `openmower` hilft dir beim Betrieb, bei der Einrichtung und bei der Fehlersuche in der OpenMower-Software.

Das Tool ist auf OpenMowerOS vorinstalliert und bietet unter anderem diese Funktionen:
- ROS-Konfiguration und Umgebungsvariablen bearbeiten
- Firmware auf dem xCore-Board installieren und aktualisieren
- ROS-Software starten und stoppen
- ROS-Logs anzeigen
- Eine ROS-Shell zur Fehlersuche öffnen

### Zugriff auf das Terminal
Für alle folgenden Schritte brauchst du Zugriff auf das Terminal.
Du kannst dafür SSH oder das Terminal im Browser verwenden.

Für SSH gelten diese Zugangsdaten:
```
username: openmower
hostname: openmower
password: openmower
```

Das Terminal im Browser benötigt keine Zugangsdaten und ist hier erreichbar: [http://openmower:7681](http://openmower:7681)

## Schritt 3.2.0: Grundlegende Prüfungen

### Prüfen, ob das Dateisystem korrekt vergrößert wurde
{{% alert title="Warnung" color="warning" %}}
Bei OpenMowerOS kommt es derzeit gelegentlich vor, dass das Dateisystem nicht korrekt vergrößert wird.
Führe `df -h /` aus und prüfe, ob die Spalte `Use %` fast 100 % anzeigt. Daran erkennst du das Problem.

![df-Ausgabe mit fast vollständig belegtem Dateisystem](images/full-file-system.png)

{{% /alert %}}


**Wenn dein Dateisystem fast voll ist**, vergrößere es mit diesen Schritten:
- **Führe aus:** `sudo raspi-config`
- **Wähle** Advanced Options -> Expand Filesystem
- **Beende die Einrichtung und starte neu**
- **Führe erneut `df -h /` aus.** In der Spalte `Use %` sollte jetzt ein niedriger Wert stehen, abhängig von der Größe deiner SD-Karte

### Das Tool `openmower` aktualisieren
Aktualisiere das Tool `openmower`, damit du die neueste Version verwendest.
Es hat eine eingebaute Update-Funktion. Führe dazu aus:
```bash
sudo openmower update-self
```

So sollte die Ausgabe aussehen:
<div class="container pb-3">
<div class="row justify-content-md-center">
<div id="step-3-2-0-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Beispielausgabe nach einem erfolgreichen Update.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        'cast/openmower-update-self.cast',
        document.getElementById('step-3-2-0-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>

### Hostnamen ändern (optional)
Wenn du mehrere Roboter betreibst, helfen unterschiedliche Hostnamen dabei, sie auseinanderzuhalten.

Folge dazu der Anleitung in der Wissensdatenbank: [Hostnamen ändern]({{< relref "/docs/Knowledge-Base/maintenance/change-hostname" >}})

### Externe WLAN-Antenne aktivieren (optional)
Wenn du eine externe WLAN-Antenne angeschlossen hast, musst du sie aktivieren.
Folge dazu der Anleitung in der Wissensdatenbank: [Externe Antenne aktivieren]({{< relref "/docs/Knowledge-Base/installation/external-wifi-antenna" >}})


## Schritt 3.2.1: Umgebungsvariablen einrichten
Beginne jetzt mit der Konfiguration der Umgebungsvariablen.

- **Starte die Konfiguration** mit `openmower configure env`
- **Wähle** deinen bevorzugten Editor, zum Beispiel `nano`
- **Bearbeite die Umgebungsvariablen.** Die Kommentare erklären, was du tun musst<br>
  Wenn du eine ältere OpenMowerOS-Version verwendest, enthält die aktuelle `.env`-Datei möglicherweise zusätzliche Kommentare oder Optionen, die in deiner lokalen Kopie fehlen. Die aktuelle Version findest du hier: [Aktuelle `.env`-Datei von OpenMowerOS](https://github.com/ClemensElflein/OpenMowerOS/blob/main/stage-openmower/40-openmower/files/opt/stacks/openmower/.env)
- **Speichere die Datei** (<kbd>Strg</kbd> + <kbd>O</kbd>, <kbd>Enter</kbd> zum Speichern, danach <kbd>Strg</kbd> + <kbd>X</kbd>, <kbd>Enter</kbd> zum Beenden von nano)

Diese Bildschirmaufzeichnung zeigt den gesamten Ablauf:
<div class="container pb-3 pt-3">
<div class="row justify-content-md-center">
<div id="step-3-2-1-player" class=""></div>
</div>
<div class="row justify-content-md-center">
<div>Im Beispiel wird ein YardForce Classic 500 mit v2-Hardware verwendet.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        'cast/openmower-configure-env.cast',
        document.getElementById('step-3-2-1-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>



Danach weiß das System, welche ROS-Version und welches Mähermodell verwendet werden.

Das Tool `openmower` lädt nun die ausgewählte ROS-Version. **Das dauert eine Weile, etwa 30 Minuten.** Zeit für einen :coffee:.




## Schritt 3.3.1: Firmware installieren
Da das System jetzt deine Hardware kennt, kannst du die Firmware auf dem xCore-Board installieren.
{{< include-markdown file="/docs/Knowledge-Base/installation/firmware-update/index.md" >}}



## Schritt 3.3.2: xESC-Motorcontroller konfigurieren
{{< include-markdown file="/docs/Knowledge-Base/configuration/configure-xesc/index.md" >}}


## Weiter mit Schritt 3.4: [ROS-Parameter konfigurieren]({{< relref "/docs/step-by-step/3-software-setup/setup-ros" >}})
