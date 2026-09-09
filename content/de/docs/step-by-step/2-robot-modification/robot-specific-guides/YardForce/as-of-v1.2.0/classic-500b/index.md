---
title: "YardForce Classic 500(B): Trägerplatine ab v1.2.0"
linkTitle: "Classic 500(B)"
weight: 10
description: >
  Umbauanleitung für YardForce Classic 500(B) mit Trägerplatine ab Version 1.2.0
---
{{% alert title="Nur für Trägerplatinen ab 1.2.0!" color="warning" %}}
Diese Anleitung gilt ausschließlich für **Trägerplatine ab Version 1.2.0**!<br>
![Erkennungsmerkmale der Trägerplatine v1.2.0](../carrierboard_version_v1.2.0.jpg)<br>
{{% /alert %}}


## Voraussetzungen

### Benötigte Teile:
- **YardForce Classic 500(B)**
- **OpenMower-Mainboard** mit allen eingesetzten Modulen: xCore, CM4, GPS und 3× ESC
- **GPS-Halterung aus dem 3D-Drucker**, **GPS-Antenne**, 2× M2,5×20-Schrauben und 2× M4×16-Schrauben für die GPS-Halterung _(bei Ardusimple RTK2B)_

### Benötigtes Werkzeug:
- **Einige einfache Schraubendreher** zum Zerlegen und Zusammenbauen.

## Schritt 2.4.1: Roboter zerlegen
Zerlege zuerst den Roboter.
Einige Stellen sind etwas knifflig. Schau dir dazu am besten mein Video an: [<i class="fa fa-brands fa-youtube"></i> YouTube-Video](https://youtu.be/_bImqD-pQSA?t=148). Der relevante Abschnitt ist 2:25 bis 5:08.
Folge dem Video danach **nicht** weiter, da die übrigen Schritte veraltet sind.

Alternativ findest du hier eine bebilderte Anleitung zum Zerlegen:

### Schrauben der oberen Abdeckung lösen

{{< image-gallery gallery_dir="images/disassemble-mower/unscrew-the-cover" >}}


### Abdeckung vorsichtig aufhebeln

Einige Stellen sind etwas knifflig. Schau dir dazu am besten dieses Video an: [<i class="fa fa-brands fa-youtube"></i> YouTube-Video](https://youtu.be/_bImqD-pQSA?t=148). Der relevante Abschnitt ist 2:25 bis 5:08.

{{< image-gallery gallery_dir="images/disassemble-mower/pry-the-cover" >}}


### Kabel der Abdeckung abstecken

Vorne führen zwei dünne Kabel zu den Radsensoren. Ein breites Kabel verbindet das Mainboard mit der CoverUI-Platine.
Der Schraubendreher auf den Bildern dient nur zur Veranschaulichung. Du kannst die Abdeckung einfach mit der Hand halten.

{{< image-gallery gallery_dir="images/disassemble-mower/unplug-the-cover" >}}


### Mainboard abstecken

{{< image-gallery gallery_dir="images/disassemble-mower/unplug-the-mainboard" >}}


### Vordere Platine entfernen

{{< image-gallery gallery_dir="images/disassemble-mower/remove-front-pcb" >}}


## Schritt 2.4.2: Originalelektronik entfernen

Entferne die folgenden Originalbauteile:
- Mainboard
- Begrenzungskabelsensor: die schmale Platine vorne im Roboter.

Lass den Akku eingebaut.

## Schritt 2.4.3: Kleinere Vorbereitungen

{{< tabpane text=true >}}
{{% tab header="**Wähle deine Variante**:" disabled=true /%}}

{{% tab header="Witmotion UM9xx/ByNav-Mxx" text=true %}}

### Witmotion-GPS-Modul montieren

<img class="special-img-class" style="width:50%" src="./images/WTRTK-GPS.jpg" />

Montiere dein Witmotion-UM9xx- oder ByNav-Mxx-GPS-Modul und das mitgelieferte Witmotion-Pigtail-Kabel wie abgebildet.

{{% /tab %}}


{{% tab header="Ardusimple RTK2B" text=true %}}

### GPS-Antennenhalterung zusammenbauen

![GPSHolder.jpg](images/GPSHolder.jpg)
Baue die GPS-Antennenhalterung wie auf dem Bild zusammen.

{{% /tab %}}

{{< /tabpane >}}



## Schritt 2.4.4: OpenMower-Elektronik einbauen

Jetzt kannst du das OpenMower-Mainboard und die vorbereitete GPS-Antennenhalterung einbauen.
- Setze das Mainboard an die Stelle der Originalplatine.<br/>Hinten sitzt es zwischen Kunststofflaschen, vorne wird es mit zwei Schrauben gehalten.
- Ziehe für die GPS-Halterung zwei der weißen Kunststoff-Kabelhalter nach oben heraus. Stecke die Halterung in die passenden Löcher und befestige sie mit einer der zuvor aufbewahrten Schrauben _(nur bei Ardusimple RTK2B)_.
- Schließe alle Kabel an.


**Die Anschlüsse sind wie folgt belegt:**
1. Mähmotorsensor
2. Haupt-Motoranschluss: Fahrmotoren, Mähmotoren und Sensoren
3. Stromanschluss
4. Ladekontakte
5. USB-Anschluss an der Rückseite des Roboters
6. OEM-CoverUI-Platine: Sicherheitssensoren, Regensensor, LEDs und Tasten
7. GPS-Antenne

![Mainboard-Anschlüsse](./images/MainboardConnections.jpg)

## Schritt 2.4.5: Externe WLAN-Antenne einbauen (optional)
Eine externe WLAN-Antenne für besseren Empfang lässt sich einfach einbauen.

![ExternalAntenna.jpg](images/ExternalAntenna.jpg)

## Voraussetzungen

### Benötigte Teile:
- **WLAN-Antennenhalterung:** 3D-Druckteil von [Printables](https://www.printables.com/model/1504184-openmower-yardforce-classic-500-wifi-antenna-mount)
- **Zwei Schrauben:** Du kannst die Schrauben des zuvor entfernten Frontsensors verwenden
- **WLAN-Antenne mit Kabel:** Erhältlich bei [Amazon](https://amzn.to/48iknlw)

### Vorgehen:
1. Befestige die Antenne an der Halterung
2. Befestige die Halterung mit den beiden Schrauben am Mäher
3. Schließe die Antenne an das CM4 an
4. Fixiere das Kabel mit einem Kabelbinder an der Platinenecke


## Schritt 2.4.6: Zum ersten Mal einschalten

Schalte den Roboter jetzt mit dem Schalter an seiner Rückseite ein.

{{% alert title="Warnung" color="warning" %}}
Wenn du etwas Ungewöhnliches siehst oder riechst, schalte **sofort aus!**

Dazu gehören unter anderem:
- Rauch oder Feuer
- Geruch nach heißer Elektronik
- Durchgebrannte Sicherungen
  {{% /alert %}}


Manche Akkupacks schalten sich wegen des Einschaltstroms sofort ab. Falls das passiert, kannst du versuchen, den Schalter aus- und wieder einzuschalten. Danach sollte es funktionieren.

Nach dem Einschalten sollten die LEDs an ESCs, GPS, xCore-Board und Mainboard blinken.
**Lass den Roboter mindestens fünf Minuten eingeschaltet, damit das CM4 vollständig startet. Beim ersten Start führt es Einrichtungsschritte aus.**

{{% alert title="Info" color="info" %}}
Stelle den Mäher am besten in die Ladestation, damit der Akku nicht leer wird.

Der Akku wird in diesem Zustand noch nicht geladen, weil auf dem Core-Board noch nicht die richtige Firmware installiert ist. Die Spannung der Ladestation versorgt aber bereits die Elektronik, sodass der Akku nicht entladen wird.
{{% /alert %}}

Wenn alles in Ordnung aussieht, mache mit der [Software-Einrichtung]({{< relref "/docs/step-by-step/3-software-setup" >}}) weiter.

Andernfalls **höre hier auf und bitte auf dem Discord-Server um Hilfe**.
