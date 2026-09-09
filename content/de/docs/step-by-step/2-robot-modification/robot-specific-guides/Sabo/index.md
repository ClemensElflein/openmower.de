---
title: "SABO / John Deere"
linkTitle: "SABO / John Deere"
weight: 20
description: "Umbauanleitung für SABO MOWiT 500F / John Deere Tango E5"
---
## Voraussetzungen

### Benötigte Teile

- **SABO MOWiT 500F oder John Deere Tango E5**
- **OpenMower-v2-Trägerplatine für SABO** mit allen eingesetzten Modulen: xCore, CM4, GPS und 3× ESC

{{< image-gallery gallery_dir="images/prerequisites" >}}

### Benötigtes Werkzeug

- **Ratsche mit 10-mm-Nuss** für das Gehäuse
- **5-mm-Inbusschlüssel** für das Messer
- **Torx T30** für den Mainboard-Halter
- **Torx T20** für das Mainboard

## Schritt 2.4.1: Mäher öffnen und Original-Mainboard ausbauen 🔓

1. Lege den Mäher auf den Rücken und entferne die sechs 10-mm-Schrauben am Gehäuse.
2. Entferne das Messer mit dem 5-mm-Inbusschlüssel. Es hat ein Rechtsgewinde. Trage Handschuhe und halte das Messer beim Lösen sicher fest.
3. Halte das Gehäuse mit beiden Händen zusammen und stelle den Mäher wieder auf die Räder.
4. Öffne die Abdeckung auf der Griffseite hinten um einige Zentimeter.
5. Leuchte mit einer Taschenlampe hinein und löse die Display-Flachbandkabel:
   - Serie I: Zwei Flachbandkabel führen zur CoverUI. Jeder Stecker hat kleine seitliche Verriegelungen. Drücke sie zum Entriegeln und ziehe die Stecker dann vom Mainboard ab.
   - Serie II: Ein Flachbandkabel. Ziehe es gerade aus dem Mainboard-Anschluss. Es hat keine Verriegelung.
6. Jetzt kannst du die Abdeckung weiter öffnen. Ein einzelnes Kabel führt von den Ladekontakten der Abdeckung zum Mainboard. Davor sitzt ein zweipoliger Molex-Stecker. Drücke die Verriegelung und trenne ihn. Lege die Abdeckung für den späteren Umbau und Zusammenbau beiseite.
7. Trenne alle übrigen Kabel vom Original-Mainboard. Viele Stecker haben eine Rastnase. Drücke sie vor dem Abziehen.
8. Das Original-Mainboard sitzt auf einem schwarzen Kunststoffhalter. An dessen Rückseite befinden sich zwei größere Torx-T30-Schrauben. Entferne sie und nimm das Mainboard zusammen mit dem Halter heraus.
9. Löse die Torx-T20-Schrauben, um das Original-Mainboard vom Halter zu entfernen.

{{< image-gallery gallery_dir="images/disassemble-mower" >}}

## Schritt 2.4.2: Vorbereitete Teile montieren

Baue die zuvor [vorbereiteten Teile]({{% relref "/docs/step-by-step/2-robot-modification/prepare-the-parts" %}}) ein:

1. Montiere das vorbereitete UM9x-GPS-Modul auf der Trägerplatine und schließe das IPEX/SMA-Kabel wie gezeigt an. Es liegt dem UM9x normalerweise bei.<br>
   ![UM9x-IPEX/SMA-Kabel](images/UM9x-IPEX-SMA-Cable.jpg)
2. Setze die Kombination aus xCore, CM4 und optionalem Kühlkörper auf die Trägerplatine, falls noch nicht geschehen.

## Schritt 2.4.3 (optional): WLAN-Klebeantenne anbringen 📶

Die WLAN-Klebeantenne kannst du wie gezeigt platzieren:

{{< image-gallery gallery_dir="images/wifi-adhesive-antenna" >}}

## Schritt 2.4.4: Trägerplatine und Mainboard-Halter montieren 🔩

1. Wenn alle Module vorbereitet und aufgesteckt sind, befestige die Trägerplatine am Mainboard-Halter.<br>
   **Wenn du weniger Schrauben als Löcher hast, verwende zuerst die Löcher in der Nähe der größeren Steckverbinder!**
2. Setze die Trägerplatine mit dem Halter wieder in den Mäher ein und befestige sie mit den beiden T30-Schrauben.
3. Schließe alle Stecker vorsichtig an. Manche passen in mehrere Buchsen. Prüfe deshalb die Beschriftungen oder verwende diese Anschlussübersicht:<br>

   | Anschlüsse Serie I | Anschlüsse Serie II |
   | :---: | :---: |
   | ![Anschlüsse Serie I](images/om-sabo-cb-s1-v02-plugs.jpg) | ![Anschlüsse Serie II](images/om-sabo-cb-s2-v02-plugs.jpg) |

   Hinweis: Manche Stecker sind gedreht angeordnet. Verwende keine Gewalt!

## Schritt 2.4.5: GPS-Antenne, zum Beispiel HA/HX-901, auf der Abdeckung montieren 🛰️

Eine alternative Halterung für den Innenraum, die ohne Eingriffe ins Gehäuse auskommt, hat [STS entworfen](https://discord.com/channels/958476543846412329/1355300774523174922/1426287736356077808). Weitere Details und gegebenenfalls STL-Dateien findest du in der Discord-Diskussion.

1. Bohre ein Loch mit 6,5 bis 7 mm Durchmesser ungefähr an der auf den Bildern gezeigten Stelle in die Abdeckung.
2. Montiere das mitgelieferte 30–40 cm lange SMA-Verlängerungskabel. Der SMA-Durchführungsanschluss muss weit genug herausragen, damit sich die HA/HX-901 vollständig aufschrauben lässt und guten Kontakt hat. Lass im Zweifel innen eine Unterlegscheibe oder einen Abstandshalter weg, um mehr Gewindelänge zu erhalten.<br>
   Dichte den Anschluss von oben mit Silikon oder einem ähnlichen Dichtmittel ab. Verwende oben nicht zu viel, damit sich die HA/HX-901 später noch aufschrauben lässt.
3. Dichte auch die Innenseite gründlich ab, damit kein Wasser eindringen kann. Innen gilt beim Dichtmittel: *Mehr ist besser.*
4. Lass das Dichtmittel ausreichend aushärten, bevor du weitermachst.

{{< image-gallery gallery_dir="images/gps-antenna" >}}

## Schritt 2.4.6: Gehäuse schließen ✅

1. Setze die Abdeckung wieder auf den Mäher. Lass sie vorne leicht einrasten, halte sie hinten aber noch weit genug offen, um nacheinander das GPS-Antennenkabel an die Trägerplatine, das Ladekontaktkabel und zuletzt die CoverUI-Flachbandkabel anzuschließen.
2. Schließe die Abdeckung vollständig, sodass sie rundum gleichmäßig sitzt und einrastet.
3. Halte das Gehäuse mit beiden Händen zusammen und drehe den Mäher wieder auf den Rücken.
4. Setze die sechs 10-mm-Sechskantschrauben ein und ziehe sie fest.
5. **Montiere das Messer noch nicht.**
6. Stelle den Mäher wieder auf seine Räder.
7. Schraube zum Schluss die HA/HX-901-Antenne auf die Abdeckung.

## Schritt 2.4.7: Zum ersten Mal einschalten

Schalte den Roboter mit dem Schalter an seiner Rückseite ein.

{{% alert title="Warnung" color="warning" %}}
Wenn du etwas Ungewöhnliches siehst oder riechst, schalte **sofort aus!**

Dazu gehören unter anderem:

- Rauch oder Feuer
- Geruch nach heißer Elektronik
- Durchgebrannte Sicherungen
{{% /alert %}}

Nach dem Einschalten dauert es etwa zehn Sekunden, bis LEDs und LCD erste Lebenszeichen zeigen.
**Lass den Roboter mindestens fünf Minuten eingeschaltet, damit das CM4 vollständig startet. Beim ersten Start führt es Einrichtungsschritte aus.**

{{% alert title="Hinweis" color="info" %}}
Stelle den Mäher am besten in die Ladestation, damit der Akku nicht leer wird und laden kann.
{{% /alert %}}

Wenn alles in Ordnung aussieht, mache mit der [Software-Einrichtung]({{< relref "/docs/step-by-step/3-software-setup" >}}) weiter.

Andernfalls **höre hier auf und bitte auf dem Discord-Server um Hilfe**.
