---
title: "Schritt 2.2: SD-Karte vorbereiten"
linkTitle: "SD-Karte"
weight: 20
description: "In diesem Schritt installieren wir OpenMower OS auf der SD-Karte."
---
Wir haben ein Raspberry-Pi-Image speziell für OpenMower angepasst. Dazu gehören:

- Netzwerkkonfiguration für das interne Roboternetzwerk
- Ein Hotspot, mit dem du den Roboter einfach mit deinem Heimnetz verbindest
- Docker für die einfache Verwaltung der Container
- Zugriff auf das Terminal des Roboters im Browser
- … und mehr!

In diesem Schritt spielen wir das Image auf und nehmen die ersten Einstellungen vor.

{{% alert title="Hinweis" color="info" %}}
Diese Anleitung gilt für das Raspberry Pi Compute Module **Lite**, also die Version **ohne** eMMC-Speicher.

Wenn du ein Compute Module **mit eMMC** hast, kannst du diesen Schritt zunächst überspringen und mit der [Vorbereitung des Mainboards]({{% relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-mainboard/index.md" %}}) weitermachen.

Du kannst das CM4 flashen, sobald dein Mäher mit Strom versorgt wird. [Hier findest du die Anleitung dazu]({{% relref "/docs/Knowledge-Base/installation/flash-cm4-emmc/index.md" %}}).
{{% /alert %}}

## Voraussetzungen

Du brauchst:

- **Raspberry Pi CM4 Lite ohne eingebauten Speicher**
- **MicroSD-Karte mit mindestens 16 GB**
- **Einen PC mit installiertem Raspberry Pi Imager:**<br/>
  🔗&nbsp;[https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)
- **Das aktuelle OpenMowerOS-Image:**<br/>
  🔗&nbsp;[https://github.com/ClemensElflein/OpenMowerOS/releases](https://github.com/ClemensElflein/OpenMowerOS/releases)<br/>
  Du findest es im Bereich `Assets`. Du musst das Image nicht entpacken.
- **Ein SD-Kartenlesegerät**

## Image auf die SD-Karte schreiben

{{< image-gallery gallery_dir="images/imager/" >}}

- Starte Raspberry Pi Imager.
- Wähle `Raspberry Pi 4` und klicke auf „Next“.
- Klicke auf `Use Custom`, um die zuvor heruntergeladene Image-Datei zu öffnen. Klicke auf „Next“.
- Wähle deine SD-Karte aus. **Vergewissere dich, dass du wirklich die richtige Karte ausgewählt hast. Alle Daten auf dem ausgewählten Gerät werden gelöscht!** Klicke auf „Next“.
- Prüfe die Angaben und klicke auf `WRITE`. Du musst den Vorgang noch einmal bestätigen und eventuell dein Administratorpasswort eingeben.
- Warte, bis der Vorgang abgeschlossen ist.

### Image konfigurieren

Ältere Versionen von Raspberry Pi Imager konnten das Image direkt im Programm konfigurieren. In der aktuellen Version ist das nicht mehr möglich.

Mit einer älteren Imager-Version kannst du das Image weiterhin wie gewohnt konfigurieren. **Der Benutzername lässt sich jedoch nicht ändern.** Er lautet immer `openmower`.

## Fertig 🎉

Du kannst die SD-Karte jetzt aus dem PC entfernen. Sie ist für OpenMower vorbereitet. Lege sie beiseite und mache mit der [Vorbereitung des Mainboards]({{% relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-mainboard/index.md" %}}) weiter.
