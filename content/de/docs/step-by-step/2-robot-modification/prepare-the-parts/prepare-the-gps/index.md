---
title: "Schritt 2.1: GPS vorbereiten"
linkTitle: "GPS"
weight: 1
description: >
  Firmware aktualisieren und GPS-Module konfigurieren.
tags: [gps, gps-rtk, simplertk2b, zed-f9p, ntrip, unicore, um9x, um9xx, um960, um980, um982]
---
{{< tabpane text=true >}}
{{% tab header="**GPS-Modul**:" disabled=true /%}}
{{% tab header="Ardusimple F9P" %}}


## Firmware aktualisieren und GPS-Platine konfigurieren

{{% alert title="Info" color="info" %}}
Für diesen Schritt gibt es eine Videoanleitung! <br/>
Hier findest du mein YouTube-Video: [<i class="fa fa-brands fa-youtube"></i> Video](https://youtu.be/_bImqD-pQSA?t=981)

(Abschnitt 16:21 bis 17:15)
{{% /alert %}}


### Voraussetzungen

- **Eine Ardusimple-F9P-GPS-Platine**
- **Ein Micro-USB-Kabel**
- **Ein Windows-PC**
- **Die aktuelle v1-Version von u-center:**<br/>
  🔗&nbsp;[https://www.u-blox.com/en/product/u-center](https://www.u-blox.com/en/product/u-center)<br/>
  Lade nicht u-center V2 herunter. Für den F9P brauchst du u-center v1.
- **Die GPS-Konfigurationsdatei**<br/>
  🔗&nbsp;<a href="https://raw.githubusercontent.com/ClemensElflein/OpenMower/refs/heads/main/configs/GPSConfig/robot-fw-1_51.txt" target="_blank">robot-fw-1_51.txt</a><br/>
  Der Link öffnet sich in einem neuen Browser-Tab. Verwende <kbd>Strg</kbd>+<kbd>S</kbd>, um die Datei herunterzuladen.


### Schritt 2.1.0: Firmware aktualisieren

{{% alert title="Warnung" color="warning" %}}
Den F9P gibt es inzwischen in mehreren Varianten. Die unten verlinkte Firmware ist für die L1+L2-Version. Prüfe, ob auf dem u-blox-Chip eine dieser Bezeichnungen steht: **ZED-F9P-02B, ZED-F9P-04B oder ZED-F9P-05B!**

Bei einer anderen Platine darfst du die verlinkte Firmware **nicht** verwenden. Lade die passende Version direkt von u-blox.com herunter.
{{% /alert %}}

Aktualisiere die Firmware deiner Ardusimple-Platine auf [`ZED-F9P HPG 1.51` – *Download*](https://content.u-blox.com/sites/default/files/2024-11/UBX_F9_100_HPG151_ZED_F9P.6c43b30ccfed539322eccedfb96ad933.bin). Eine Anleitung findest du auf der [Ardusimple-Website](https://www.ardusimple.com/zed-f9p-firmware-update-with-simplertk2b/).


### Schritt 2.1.1: u-center öffnen und GPS verbinden

Verbinde nach der Installation von u-center die Ardusimple-Platine über ihre USB-Buchse „Power+GPS“ mit deinem Windows-PC. Die blauen LEDs sollten aufleuchten, und Windows sollte das Gerät als COM-Port erkennen.
Öffne anschließend u-center. 

Wähle in u-center unter `Receiver -> Connection` den passenden COM-Port, um die Verbindung zur Platine herzustellen.


### Schritt 2.1.2: Konfiguration auf das GPS-Modul übertragen

![Einstellungen mit u-center übertragen](transfer-gps-settings.jpg)

Öffne nach erfolgreicher Verbindung `Tools -> Receiver Configuration ...`.
Wähle dort über `...` die zuvor heruntergeladene Datei `robot-fw-1_51.txt` aus. Übertrage die Konfiguration mit `Transfer File -> GNSS` auf das GPS-Modul.


### Schritt 2.1.3: Konfiguration im Flash speichern

![Einstellungen im Flash speichern](save-settings-to-flash.jpg)

Damit die Konfiguration nach dem Ausschalten erhalten bleibt, musst du sie im Flash-Speicher sichern. Öffne `View -> Configuration View`, wähle links `CFG (Configuration)` und aktiviere `Save current configuration`. Rechts müssen sowohl `0 - BBR` als auch `1 - FLASH` ausgewählt sein. Klicke danach in der unteren Werkzeugleiste auf `Send`.

Rechts oben erscheint ein Zähler für die Zeit seit der letzten an die GPS-Platine gesendeten Nachricht. Direkt nach dem Klick auf `Send` sollte er `0s` anzeigen.


### Schritt 2.1.4: Fertig 🎉

Dein GPS-Modul ist jetzt für OpenMower eingerichtet. Du kannst es vom Windows-PC trennen.

{{% /tab %}}



{{% tab header="WitMotion Unicore UM9xx" %}}

<div class="prep-gps-um9xx-tab">

1. Verbinde dein UM9xx mit dem mitgelieferten USB-C-Kabel mit dem PC
1. Öffne ein serielles Terminal wie minicom, miniterm oder CuteCom mit 115200 Baud
1. Achte darauf, dass als Zeilenende CR/LF eingestellt ist
1. Sende `CONFIG`<kbd>↵ Enter</kbd>, um die Verbindung zu prüfen. Es sollte eine lesbare Ausgabe aus Schlüsseln und Werten erscheinen. Falls nicht, prüfe Kabel, Port und Berechtigungen.
1. Setze das Modul zurück und stelle die Baudrate auf 921600, indem du diese Befehle zeilenweise eingibst:
   > FRESET<kbd>↵ Enter</kbd><br>
   > CONFIG COM1 921600<kbd>↵ Enter</kbd>

   (Nach `FRESET` kann es einige Sekunden dauern, bis das Modul wieder antwortet.)
1. Prüfe die Verbindung erneut mit `CONFIG`. Falls die Ausgabe nicht wie zuvor aussieht, stelle dein serielles Terminal auf 921600 Baud um und öffne die Verbindung bei Bedarf neu. Führe `CONFIG` erneut aus, bis eine sinnvolle Antwort erscheint
1. Richte den Rover mit diesen Befehlen ein, jeweils eine Zeile nach der anderen:
   > MODE ROVER UAV<kbd>↵ Enter</kbd><br>
   > GPGSV COM1 2<kbd>↵ Enter</kbd><br>
   > GPRMC COM1 1<kbd>↵ Enter</kbd><br>
   > GPGSA COM1 1<kbd>↵ Enter</kbd><br>
   > GPVTG COM1 1<kbd>↵ Enter</kbd><br>
   > GPGST COM1 1<kbd>↵ Enter</kbd><br>
   > GPGGA COM1 0.2<kbd>↵ Enter</kbd><br>
   > SAVECONFIG<kbd>↵ Enter</kbd>

   Vergiss `SAVECONFIG` nicht. Der Befehl speichert die Einstellungen dauerhaft, sodass sie nach dem Aus- und Einschalten erhalten bleiben.
1. Trenne das USB-Kabel vom UM9x-Modul und setze es auf die Trägerplatine. Löte vorher bei Bedarf die benötigten Stiftleisten an.

</div>

{{< /tab >}}


{{% tab header="By-Nav M10/M20 – direkt per USB" %}}

<div class="prep-gps-um9xx-tab">
  
## Einrichtung über USB (cutecom)

**Beim M20 ersetzt du jedes COM1 durch COM2.**

1. Verbinde dein M10 über das mitgelieferte USB-C-Kabel mit dem PC.
2. Öffne das empfohlene Terminalprogramm cutecom.
3. Verbinde dich mit 115200 Baud.
4. Es sollte eine lesbare Ausgabe aus Schlüsseln und Werten erscheinen. Falls nicht, prüfe Kabel, Port und Berechtigungen.
5. Stelle sicher, dass das Zeilenende auf **CR/LF** eingestellt ist.
6. Du kannst die Ausgabe in cutecom ausblenden. Sie läuft weiter, wird aber nicht angezeigt.
7. Setze das Modul auf Werkseinstellungen zurück und deaktiviere die zyklischen Ausgaben mit diesen Befehlen, jeweils zeilenweise:

   > FRESET<kbd>↵ Enter</kbd><br>
   > (Nach `FRESET` kann es einige Sekunden dauern, bis das Modul wieder antwortet.)<br>

   > UNLOGALL<kbd>↵ Enter</kbd><br>

8. Blende die Ausgabe in cutecom wieder ein.
9. Prüfe die Verbindung erneut mit:

   > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

   Es sollte eine lesbare Ausgabe erscheinen.

10. Richte den Rover ein:

    > SERIALCONFIG COM1 460800<kbd>↵ Enter</kbd><br>

11. Prüfe die Verbindung erneut mit:

    > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

    Die Ausgabe sollte weiterhin lesbar sein, da wir über COM3 verbunden sind. Falls nicht, prüfe Verbindung und Baudrate.

12. Setze die Rover-Konfiguration fort:

    > LOG COMCONFIG ONCE<kbd>↵ Enter</kbd><br>   (COM1 sollte jetzt 460800 anzeigen)<br>
    > RTKTYPE ROVER<kbd>↵ Enter</kbd><br>
    > RTKTYPE<kbd>↵ Enter</kbd><br>
    > RTKTIMEOUT 5<kbd>↵ Enter</kbd><br>
    > RTKTIMEOUT<kbd>↵ Enter</kbd><br>

13. Lege die zyklischen Ausgaben fest:

    > LOG COM1 GPGSV ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPRMC ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGSA ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPVTG ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGST ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGGA ONTIME 0.1<kbd>↵ Enter</kbd><br>

14. Speichere die Änderungen zum Schluss im Flash-Speicher:

    > SAVECONFIG<kbd>↵ Enter</kbd><br>

    **Vergiss den Befehl `SAVECONFIG` nicht.** Er speichert die Einstellungen dauerhaft, damit sie nach dem Aus- und Einschalten erhalten bleiben.

15. Trenne das USB-Kabel vom M10-Modul und setze es auf die Trägerplatine. Löte vorher bei Bedarf die Stiftleisten an.

16. Passe auch die Baudrate in der OpenMower-ROS-Konfiguration an:

```yaml
gps:
  baud_rate: 460800
  protocol: "NMEA"
```

</div>

{{< /tab >}}

{{% tab header="By-Nav M10/M20 – über das Netzwerk" %}}

<div class="prep-gps-um9xx-tab">

## Einrichtung über TCP (by_connect)

Diese Methode funktioniert unter Linux und Windows. Unter Linux verwendest du by_connect mit Wine. Führe diesen Schritt erst durch, wenn dein OpenMower-System läuft. Die Konfiguration erfolgt aus der Ferne über TCP.

### Voraussetzungen

- Eine WitMotion-ByNav-M10-GPS-Platine (Standardbaudrate: 115200)
- Einen OpenMower mit installiertem OpenMowerOS
- Einen Windows- oder Linux-PC
- [by_connect-Software](https://www.bynav.com/media/upload/LargeFile/BY_Connect.zip) von bynav.com
- [Beschreibung des Schnittstellenprotokolls (PDF)](https://www.bynav.com/media/upload/cms_15/UG017_Interface%20Protocol_Bynav.pdf) — gültig für alle ByNav-Module (M10, M20 usw.)

**Beim M20 ersetzt du jedes COM1 durch COM2.**

1. Setze das M10 auf die Trägerplatine. Löte vorher bei Bedarf die Stiftleisten an.
2. Stelle die Baudrate in der OpenMower-ROS-Konfiguration auf 115200:

```yaml
gps:
  baud_rate: 115200
  protocol: "NMEA"
```

3. Stelle eine serielle Verbindung zum M10 über TCP her, indem du im SSH-Terminal deines OpenMower `openmower expose-gps` ausführst:
   ![GPS-Verbindung mit openmower expose-gps freigeben](openmower_expose-gps.png)

4. Öffne by_connect auf deinem PC, unter Linux mit Wine. Den Download findest du auf bynav.com. Verbinde dich als **TCP Client** mit Port 2000 des OpenMower. Eine Baudrate musst du hier nicht angeben:
   ![by_connect TCP Client](by_connect_tcp_client.png)

5. Es sollte eine lesbare Ausgabe aus Schlüsseln und Werten erscheinen. Falls nicht, prüfe die Verbindung.
6. Stelle sicher, dass das Zeilenende auf **CR/LF** eingestellt ist.
7. Du kannst die Ausgabe in by_connect ausblenden. Sie läuft weiter, wird aber nicht angezeigt:
   ![Eingabefeld in by_connect](by_connect_input.png)

8. Setze das Modul auf Werkseinstellungen zurück und deaktiviere die zyklischen Ausgaben mit diesen Befehlen, jeweils zeilenweise:

   > FRESET<kbd>↵ Enter</kbd><br>
   > (Nach `FRESET` kann es einige Sekunden dauern, bis das Modul wieder antwortet.)<br>

   > UNLOGALL<kbd>↵ Enter</kbd><br>

9. Blende die Ausgabe in by_connect wieder ein.
10. Prüfe die Verbindung erneut mit:

    > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

    Es sollte eine lesbare Ausgabe erscheinen.

11. Richte den Rover ein:

    > SERIALCONFIG COM1 460800<kbd>↵ Enter</kbd><br>

12. Prüfe die Verbindung erneut:

    > LOG VERSION ONCE<kbd>↵ Enter</kbd><br>

    Die Ausgabe ist jetzt unlesbar, weil sich die Baudrate geändert hat. Schließe die Verbindung, stelle in der OpenMower-ROS-Konfiguration die Baudrate auf **460800** und verbinde dich erneut über `openmower expose-gps`:
    ![Baudrate ändern](changeBaud1.png)

13. Öffne by_connect erneut, verbinde dich wieder als TCP Client und prüfe die Lesbarkeit der Ausgabe mit:

    > LOG COMCONFIG ONCE<kbd>↵ Enter</kbd><br>

14. Setze die Rover-Konfiguration fort:

    > RTKTYPE ROVER<kbd>↵ Enter</kbd><br>
    > RTKTIMEOUT 5<kbd>↵ Enter</kbd><br>

15. Wenn alles wie erwartet funktioniert und du `ok`-Antworten erhältst, speichere die Einstellungen im Flash. Andernfalls trenne die Verbindung, schalte den OpenMower aus und wieder ein und beginne von vorne:

    > SAVECONFIG<kbd>↵ Enter</kbd><br>

16. Lege die zyklischen Ausgaben fest:

    > LOG COM1 GPGSV ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPRMC ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGSA ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPVTG ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGST ONTIME 1<kbd>↵ Enter</kbd><br>
    > LOG COM1 GPGGA ONTIME 0.1<kbd>↵ Enter</kbd><br>

17. Speichere die Änderungen im Flash-Speicher:

    > SAVECONFIG<kbd>↵ Enter</kbd><br>

**Vergiss den Befehl `SAVECONFIG` nicht.** Er speichert die Einstellungen dauerhaft, damit sie nach dem Aus- und Einschalten erhalten bleiben.

</div>

{{< /tab >}}

{{< /tabpane >}}

Weiter mit [Schritt 2.2: SD-Karte vorbereiten]({{< relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-sd-card" >}})
