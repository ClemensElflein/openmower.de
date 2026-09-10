---
title: "YardForce Classic 500(B): Trägerplatine vor v1.2.0"
linkTitle: "Classic 500(B)"
weight: 30
description: >
  Umbauanleitung für YardForce Classic 500(B) mit Mainboard ≤ 1.1.0-beta
---
{{% alert title="Nur für v2-Hardware!" color="warning" %}}
Diese Anleitung gilt für OpenMower-v2.x-Hardware!
Wenn du v1-Hardware hast, folge der [älteren Dokumentation](https://openmower.de/archive/v1.0.2/docs/), denn bei v1-Hardware musst du auch die Ladestation umbauen!

Du hast **v1-Hardware**, wenn:
- du einen Raspberry Pi in voller Größe verwendest
- dein Mainboard die Versionsnummer **v0.xx** trägt
{{% /alert %}}

{{% alert title="Nur für Trägerplatinen 1.x bis 1.1.0-beta!" color="warning" %}}
Diese Anleitung gilt ausschließlich für **Trägerplatinen der Versionen 1.x bis 1.1.0-beta**!<br>
![Erkennungsmerkmale der Trägerplatine v1.1.0-beta](../carrierboard_version_v1.1.0-beta.jpg)<br>
{{% /alert %}}

## Voraussetzungen

### Benötigte Teile:
- **YardForce Classic 500(B)**
- **OpenMower-Mainboard** mit allen eingesetzten Modulen: xCore, CM4, GPS und 3× ESC
- **CoverUI-Platine** (optional)
- **GPS-Halterung aus dem 3D-Drucker**, **GPS-Antenne**, 2× M2,5×20-Schrauben und 2× M4×16-Schrauben für die GPS-Halterung

### Benötigtes Werkzeug:
- **XH-Steckverbinderset und einige Leitungen**, um Stecker für die Not-Aus-Sensoren und die CoverUI-Platine zu crimpen 
- **Einige einfache Schraubendreher** zum Zerlegen und Zusammenbauen.

## Schritt 2.4.1: Roboter zerlegen
Zerlege zuerst den Roboter.
Einige Stellen sind etwas knifflig. Schau dir dazu am besten mein Video an: [<i class="fa fa-brands fa-youtube"></i> YouTube-Video](https://youtu.be/_bImqD-pQSA?t=148). Der relevante Abschnitt reicht von Minute 2:25 bis 5:08.
Folge dem Video danach **nicht** weiter, da die übrigen Schritte veraltet sind.

Alternativ findest du hier eine bebilderte Anleitung zum Zerlegen:

### Schrauben der oberen Abdeckung lösen

{{< image-gallery gallery_dir="images/disassemble-mower/unscrew-the-cover" >}}


### Abdeckung vorsichtig aufhebeln

Einige Stellen sind etwas knifflig. Schau dir dazu am besten dieses Video an: [<i class="fa fa-brands fa-youtube"></i> YouTube-Video](https://youtu.be/_bImqD-pQSA?t=148). Der relevante Abschnitt reicht von Minute 2:25 bis 5:08.

{{< image-gallery gallery_dir="images/disassemble-mower/pry-the-cover" >}}


### Kabel der Abdeckung abstecken

Vorne führen zwei dünne Kabel zu den Radsensoren. Ein breites Kabel verbindet das Mainboard mit der CoverUI-Platine.
Der Schraubendreher auf den Bildern dient nur zur Veranschaulichung. Du kannst die Abdeckung einfach mit der Hand halten.

{{< image-gallery gallery_dir="images/disassemble-mower/unplug-the-cover" >}}


### Mainboard abstecken

{{< image-gallery gallery_dir="images/disassemble-mower/unplug-the-mainboard" >}}


### Vordere Platine entfernen

{{< image-gallery gallery_dir="images/disassemble-mower/remove-front-pcb" >}}


### CoverUI-Platine entfernen

{{% alert title="Info" color="info" %}}
Dieser Abschnitt geht davon aus, dass du die Original-Bedienplatine vollständig durch eine eigene Platine ersetzt. Du kannst die Originalplatine auch weiterverwenden, indem du eine angepasste Firmware aufspielst.
Wenn du das vorhast, lass sie eingebaut. Weitere Informationen findest du <a href="https://github.com/ClemensElflein/CoverUI/blob/main/Firmware/CoverUI/YardForce/README.md" target="_blank">im CoverUI-Repository *</a>.

\* Es wäre schön, wenn jemand diese Informationen in die Wissensdatenbank dieser Website übertragen könnte.
{{% /alert %}}

{{< image-gallery gallery_dir="images/disassemble-mower/remove-cover-ui-board" >}}


## Schritt 2.4.2: Originalelektronik entfernen

Entferne die folgenden Originalbauteile:
- Mainboard
- Begrenzungskabelsensor: die schmale Platine vorne im Roboter.
- Alle Kabel in der orangefarbenen Abdeckung (Not-Aus).

Lass den Akku eingebaut.

## Schritt 2.4.3: Kleinere Vorbereitungen

### 3.1 Kunststofflaschen im Deckel entfernen
Bei manchen YardForce-Classic-500-Modellen sitzen im Deckel Kunststofflaschen, die dem OpenMower-Mainboard im Weg sind.
Diese müssen entfernt werden. Ich habe einen großen Seitenschneider verwendet. Ein Dremel oder ein anderes geeignetes Werkzeug geht ebenfalls.
![Kunststofflaschen im Deckel entfernen](images/CuttingTheTabs.jpg)

Wenn dein Deckel keine solchen Laschen hat, musst du hier nichts tun.

### 3.2 GPS-Antennenhalterung zusammenbauen
![Zusammengebaute GPS-Antennenhalterung](images/GPSHolder.jpg)
Baue die GPS-Antennenhalterung wie auf dem Bild zusammen.

### 3.3 Neue Stecker an die Not-Aus-Kabel crimpen
Das OpenMower-Mainboard verwendet für jeden Not-Aus-Sensor einen eigenen JST-XH-Stecker. Beim ursprünglichen YardForce Classic 500 laufen dagegen alle Not-Aus-Taster auf einem großen Stecker zusammen.
Das folgende Bild zeigt das Originalkabel.
![Originalkabel der Not-Aus-Sensoren](images/EmergencyCables1.jpg)

Fertige jetzt **vier** Kabel an, eines pro Not-Aus-Sensor:
- Schneide das Kabel wie abgebildet **ganz nah am großen Stecker** ab. Du brauchst die volle Länge der Not-Aus-Kabel.
- Crimpe wie unten gezeigt XH-Stecker an die freien Kabelenden. **Prüfe unbedingt die Pinbelegung! Die Leitungen sind am Stecker verdreht!**
- **Wiederhole das für alle vier Not-Aus-Sensoren**, sodass jeder einen XH-Stecker erhält. Die Pinbelegung ist bei allen gleich.
![Neue XH-Stecker an den Not-Aus-Kabeln](images/EmergencyCables2.jpg)

Am Ende hast du vier Kabel mit **unterschiedlichen Längen, aber identischer Pinbelegung**.

### 3.4 Kabel für die CoverUI anfertigen
Wenn du eine eigene CoverUI-Platine verwendest, brauchst du ein Verbindungskabel zum Mainboard.
- Nimm vier Leitungen mit etwa 20 cm Länge.
- Crimpe wie abgebildet XH-Stecker an beide Enden. Verbinde die Pins eins zu eins: Pin 1 mit Pin 1 am anderen Stecker, Pin 2 mit Pin 2 und so weiter.

![Verbindungskabel zwischen CoverUI und Mainboard](images/CoverUICable.jpg)



## Schritt 2.4.4: OpenMower-Elektronik einbauen

Jetzt kannst du das OpenMower-Mainboard und die vorbereitete GPS-Antennenhalterung einbauen.
- Setze das Mainboard an die Stelle der Originalplatine.<br/>Hinten sitzt es zwischen Kunststofflaschen, vorne wird es mit zwei Schrauben gehalten.
- Ziehe für die GPS-Halterung zwei der weißen Kunststoff-Kabelhalter nach oben heraus. Stecke die Halterung in die passenden Löcher und befestige sie mit einer der zuvor aufbewahrten Schrauben.
- Schließe alle Kabel entsprechend dem Bild und der folgenden Liste an.

Fertig sollte es so aussehen:
![Angeschlossene Kabel am OpenMower-Mainboard](images/Connections.jpg)

**Die Anschlüsse sind wie folgt belegt:**
1. Mähmotorsensor
2. Hauptanschluss für Motoren: Fahrmotoren, Mähmotoren und Sensoren
3. Stromanschluss
4. Ladekontakte
5. Not-Aus-Taster im Deckel: links/rechts ist beliebig
6. Not-Aus-Taster im Deckel: links/rechts ist beliebig
7. USB-Anschluss an der Rückseite des Roboters
8. CoverUI-Platine im Deckel (optional)
9. GPS-Antenne
10. Hebesensor: links/rechts ist beliebig
11. Hebesensor: links/rechts ist beliebig




## Schritt 2.4.5: Externe WLAN-Antenne einbauen (optional)
Eine externe WLAN-Antenne für besseren Empfang lässt sich einfach einbauen.

![Externe WLAN-Antenne mit Halterung im Mäher](images/ExternalAntenna.jpg)

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


Manche Akkupacks schalten sich wegen des Einschaltstroms sofort ab. Falls das passiert, kannst du versuchen, den Mäher aus- und wieder einzuschalten. Danach sollte es funktionieren.

Nach dem Einschalten sollten die LEDs an ESCs, GPS, xCore-Board und Mainboard blinken.
**Lass den Roboter mindestens fünf Minuten eingeschaltet, damit das CM4 vollständig startet. Beim ersten Start führt es Einrichtungsschritte aus.**

{{% alert title="Info" color="info" %}}
Stelle den Mäher am besten in die Ladestation, damit der Akku nicht leer wird.

Der Akku wird in diesem Zustand noch nicht geladen, weil auf dem Core-Board noch nicht die richtige Firmware installiert ist. Die Spannung der Ladestation versorgt aber bereits die Elektronik, sodass der Akku nicht entladen wird.
{{% /alert %}}

Wenn alles in Ordnung aussieht, mache mit der [Software-Einrichtung]({{< relref "/docs/step-by-step/3-software-setup" >}}) weiter.

Andernfalls **höre hier auf und bitte auf dem Discord-Server um Hilfe**.
