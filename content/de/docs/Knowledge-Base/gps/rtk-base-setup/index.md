---
title: "GPS-Basisstation einrichten"
linkTitle: "GPS-Basisstation einrichten"
weight: 310
description: >
  Baue deine eigene RTK-GPS-Basisstation!
---
Dieser Teil der Dokumentation ist noch in Arbeit. Es gibt viele Möglichkeiten, eine RTK-Basisstation einzurichten. Hier zeigen wir eine Variante mit RPi 0W, ZED-F9P und der webbasierten Software RTKBase. Auf Discord kannst du karl.ranseier um Hilfe bitten.

## Voraussetzungen

- [Raspberry Pi 0W](https://amzn.to/48sGCVP)
- µSD-Karte
- Netzteil für den RPi
- [Ardusimple ZED-F9P](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)
- Ein Kabel oder eine Kabelkombination mit Micro-USB-Steckern an beiden Enden:
  - A) Direkt, zum Beispiel [dieses Kabel](https://amzn.to/3K7kfMs)
  - B) Adapter ([zum Beispiel dieser](https://amzn.to/4ifLYqG)) + Micro-USB-auf-USB-A-Kabel
- Ein Windows-PC
- Stabile Internetverbindung, die mindestens eine Stunde lang nicht abbricht


## Installation

Wenn du dich mit dem RPi auskennst und bereits ein funktionierendes Betriebssystem hast, kannst du zum Abschnitt „Software“ springen. Bei mir hat es mit einem älteren Image allerdings nicht funktioniert. 


### SD-Karte vorbereiten

- Lade [RPi Imager](https://www.raspberrypi.com/software/) für Windows herunter
- Starte den Imager:

  ![]() <img src="Imager1.png" width="120">
- Wähle deinen RPi aus, in meinem Fall RPi 0W. Ein falsch gewähltes Modell führt sehr wahrscheinlich zu vielen Problemen

  ![]() <img src="./Imager2.png" width="120">
- Wähle als Betriebssystem „Raspberry Pi OS lite (legacy, 32bit)“

  ![]() <img src="./Imager3.png" width="120">

  ![]() <img src="./Imager4.png" width="120">

- Wähle deine SD-Karte:

  ![]() <img src="./Imager5.png" width="120">
- Klicke auf „Next“. Danach erscheint:

  ![]() <img src="./Imager6.png" width="120">
- Passe die Einstellungen wie gezeigt an. Verwende deine eigenen WLAN-Daten und dein Land und vergib ein gutes Passwort für deinen Pi-Benutzer. Bei Benutzername und Passwort wird Groß- und Kleinschreibung unterschieden!

  ![]() <img src="./OSCustom1.png" width="120">
- Aktiviere SSH:

  ![]() <img src="./OSCustom.png" width="120">
- Klicke auf „Save“. Danach erscheint:

  ![]() <img src="./OSCustom2.png" width="120">

- Klicke auf „YES“ und bestätige das Überschreiben der SD-Karte, wenn du sicher bist, dass du die vorhandenen Daten nicht mehr brauchst. Der Download und das Schreiben beginnen:

  ![]() <img src="./Imager7.png" width="120">

- Warte, bis der Vorgang abgeschlossen ist. Je nach Internetverbindung kann das eine halbe Stunde dauern ;-)
  

### RTKBase-RPi starten

- Stecke die SD-Karte in den RPi
- Verbinde den ZED-F9P per USB mit dem RPi. Mach das NICHT erst nach der Installation, denn er wird während der Installation konfiguriert.
- Schließe die Stromversorgung des RPi an


### Mit dem RPi verbinden

- Lies die IP-Adresse des RPi in deinem Router ab
- Starte [PuTTY](https://putty.org) und verbinde dich mit der lokalen IP-Adresse deines RPi

  ![]() <img src="./Putty1.png" width="120">
- Gib deinen Benutzernamen Pi ein, drücke Enter und gib anschließend dein Passwort ein:

  ![]() <img src="./Putty2.png" width="120">

  ![]() <img src="./Putty3.png" width="120">


### Software

- Ist der ZED-F9P angeschlossen? Falls nicht, schließe ihn jetzt an!
- Wir verwenden [RTKBase](https://github.com/Stefal/rtkbase)
- Zur Installation kannst du die folgenden Zeilen zusammen kopieren und einfügen. Die ursprüngliche Empfehlung sieht kein sudo vor chmod vor. Bei mir hat das so aber nicht funktioniert.

  ```bash
  cd ~
  wget https://raw.githubusercontent.com/Stefal/rtkbase/master/tools/install.sh -O install.sh
  sudo chmod +x install.sh
  sudo ./install.sh --all release
  ```
- Es folgt eine sehr lange Ausgabe. Sie endet mit:
  ```bash
  GNSS Configuration: done
  ################################
  STARTING SERVICES
  ################################
  Created symlink /etc/systemd/system/multi-user.target.wants/str2str_tcp.service → /etc/systemd/system/str2str_tcp.service.
  Job for gpsd.service failed because the control process exited with error code.
  See "systemctl status gpsd.service" and "journalctl -xe" for details.
  ################################
  END OF INSTALLATION
  You can open your browser to http://192.168.178.34 (here the editor deleted IPV6)
  ################################
  Pi@RTKBase:~ $
  ```
- Die Installation ist abgeschlossen. Richte jetzt deine RTKBase ein

<br>

## RTKBase konfigurieren

- Öffne im Browser die IP-Adresse deiner RTKBase. Du siehst dann:

  ![]()<img src="./RTKBase01.png" width="120">

- Gib als Passwort admin ein. Klicke auf der nächsten Seite auf das Kopiersymbol rechts neben PPP.

  ![]()<img src="./RTKBase02.png" width="120">

- Öffne die Einstellungen, klicke rechts neben „Main Service“ auf „options“ und füge die Koordinaten unter „Base coordinates“ ein:

  ![]()<img src="./RTKBase03.png" width="120">

- Klicke erneut auf „options“ und dann auf „options“ rechts neben „Caster Service“

  ![]()<img src="./RTKBase04.png" width="120">
- Trage hier dieselben Einstellungen wie im Mäher ein. Standardmäßig lauten Benutzername und Passwort jeweils gps. Wähle den passenden Mountpoint. Ich habe ihn hier und in der Mäherkonfiguration nach meiner Stadt benannt.
- Speichere die Konfiguration
- Schalte „Caster Service“ und „File Service“ ein. Es sollte so aussehen:

  ![]()<img src="./RTKBase05.png" width="120">

- Ändere bei Bedarf unter diesen Optionen dein Passwort.
- Unter „Logs“ solltest du mindestens zwei Dateien finden:

  ![]()<img src="./RTKBase06.png" width="120">


### Position der RTKBase bestimmen

Es gibt mehrere Wege, die Position zu bestimmen. Für OpenMower muss sie nicht absolut perfekt sein. Die erste Variante ist deshalb eine gute Wahl, wenn du schnell ein brauchbares Ergebnis möchtest.


#### Einfacher Weg mit gutem Ergebnis

- Klicke auf das Symbol rechts neben PPP, um die Werte in die Zwischenablage zu kopieren:

  ![]()<img src="./RTKBase02.png" width="120">
- Trage diese Werte in den Optionen von MainService ein.

  ![]()<img src="./RTKBase03.png" width="120">
- Speichern
- NTRIP-Dienst erneut aktivieren
- Fertig!


#### Aufwendigerer, genauerer Weg

- Aktiviere wie oben beschrieben den „File Service“, um deine Position aufzuzeichnen. Warte einen Tag, damit die Werte für eine hochgenaue Position gemittelt werden können.
- Nach Mitternacht findest du unter „Logs“ eine ZIP-Datei. Diese kannst du in eine RINEX-Datei umwandeln. Wenn du das Format verstehen möchtest, lies [RINEX-Datei](http://walter.bislins.ch/bloge/index.asp?page=Understanding+GPS%2FGNSS+RINEX+Files+and+Relevant+Parameters) . Das ist für die Einrichtung aber nicht nötig.
- Klicke auf den Stift rechts neben der ZIP-Datei:

  ![]()<img src="./RTKBase07.png" width="120">

- "Create Rinex file":

  ![]()<img src="./RTKBase08.png" width="120">
- Lade die Datei herunter, sobald sie fertig ist. Das kann einige Minuten oder länger dauern
- Öffne den [Rechner](https://rgp.ign.fr/SERVICES/calcul_online.php), lade die RINEX-Datei hoch und gib deine E-Mail-Adresse ein. Vergiss die „Kein Roboter“-Bestätigung nicht.

  ![]()<img src="./ignfr.png" width="120">

- Suche in der erhaltenen E-Mail nach „ITRF2014“ oder „longitude“. Dort stehen Werte wie LONGITUDE 6.XXXXXXXXX° LATITUDE 51.XXXXXXXXX° HELL 79.9041

  ![]()<img src="./averaged.png" width="120">
- Trage die Werte in den Optionen von MainService ein. Achtung: Die Reihenfolge von LONGITUDE und LATITUDE ist vertauscht!

  ![]()<img src="./RTKBase03.png" width="120">
- Speichern
- NTRIP-Dienst erneut aktivieren
- Fertig!

<br>

Danke an Stefal und alle Mitwirkenden von RTKBase und den verwendeten Projekten.
