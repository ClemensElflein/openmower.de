---
title: "GPS-RTK: Hilfe bei Problemen"
linkTitle: "GPS-RTK"
description: "Behebe GPS-RTK-Probleme bei OpenMower. Prüfe Schritt für Schritt das UBX-Protokoll, den Satelliten-Fix, die NTRIP-Verbindung und die zentimetergenaue RTK-Position."
tags: [gps, gps-rtk, simplertk2b, zed-f9p, ntrip]
resources:
    - src: "**.png"
---
Wir setzen voraus, dass du die [Anleitung zur GPS-Einrichtung]({{< relref "/docs/step-by-step/2-robot-modification/prepare-the-parts/prepare-the-gps" >}}) durchgearbeitet hast. Falls der Mäher bereits zusammengebaut ist, öffne die obere Abdeckung.

Verbinde das GPS-Modul über ein Micro-USB-Kabel direkt mit deinem Windows-PC, genauso wie beim Übertragen der Konfiguration. 

Prüfe, ob rechts unten in der Statusleiste bei `Protocol of received messages` der Wert `UBX` steht, nicht `NMEA`. Falls nicht, übertrage die Konfiguration erneut. Trenne danach die Stromversorgung des GPS-Moduls, schließe sie wieder an und prüfe, ob weiterhin `UBX` angezeigt wird.

Schließe die Antenne an die Platine an und geh nach draußen, um zu prüfen, ob GPS grundsätzlich funktioniert. Ist der Mäher schon zusammengebaut und die Antenne angeschlossen, nimm einfach den ganzen Mäher mit.
Mit angeschlossener Antenne sollten selbst drinnen am Fenster erste Satelliten und weitere Informationen in u-center erscheinen. Nach einigen Minuten beginnt die LED `GPS Fix` auf der GPS-Platine zu blinken.

In der Abweichungskarte (`View -> Deviation Map, F12`) sollten die Werte innerhalb von ungefähr 1 m bleiben. Das entspricht der üblichen GPS-Genauigkeit. Alte, unbrauchbare Daten kannst du über `File -> Database clean` löschen.

Richte jetzt die NTRIP-Verbindung ein. Wir gehen davon aus, dass du entweder einen geeigneten [NTRIP-Knoten in der Nähe](https://discord.com/channels/958476543846412329/980099128879108137/980100319700742145) (<30 km) gefunden hast oder eine eigene [Basisstation]({{< relref "/docs/Knowledge-Base/gps/rtk-base-setup" >}}) betreibst.

Öffne `Receiver -> NTRIP Client...` und trage deine NTRIP-Zugangsdaten ein. Dieselben Einstellungen verwendest du später in der ROS-Konfigurationsdatei.
{{< imgproc ntrip-client Resize 500x />}}

Der NTRIP-Client sollte die Verbindung in der Statusleiste grün anzeigen. Die Abweichungskarte (`View -> Deviation Map, F12`) sollte genau in der Mitte bleiben. Die LED `No RTK` beginnt zu blinken oder erlischt ganz.
{{< imgproc gps-fix-and-deviation Resize 800x />}}


## GPS am Mainboard testen

GPS funktioniert für sich genommen. Prüfe jetzt das Zusammenspiel mit dem Mainboard: Stecke das GPS-Modul auf das Mainboard. Die Anzeigen sollten aufleuchten und anfangen zu blinken.  
Warte, bis die LED GRÜN oder GRÜN/ROT leuchtet.

{{% alert title="🔋 Stromversorgung des Mainboards" color="info" %}}
Wenn deine Ladestation noch nicht aufgebaut ist und du den Mäherakku schonen möchtest, kannst du das Mainboard über den Micro-USB-Anschluss des Pico-Dev-Boards direkt unter der GPS-Platine versorgen. Verwende eine Powerbank mit mindestens 1 A, da die 500 mA eines Computer-USB-Anschlusses möglicherweise nicht ausreichen.
{{% /alert %}}

{{< tabpane text=true >}}
{{% tab header="**OpenMowerOS-Version**:" disabled=true /%}}
{{% tab header="0.1.0" %}}
Melde dich dann per SSH bei deinem OpenMower an.  
Im Home-Verzeichnis (`~/`) liegt das Skript `start_ros_bash.sh`.  
Führe es mit `~/start_ros_bash.sh` aus. Damit gelangst du in eine Bash-Shell innerhalb des Containers.
{{% /tab %}}
{{< /tabpane >}}

Dort kannst du mit `rostopic list` alle Topics auflisten und mit `rostopic echo --clear -w 5  /ll/position/gps` die GPS-Daten ansehen.  
Die Ausgabe sieht zum Beispiel so aus:

```yaml
header:
  seq:    44
  stamp:
    secs: 1708328554
    nsecs: 51810942
  frame_id: "gps"
sensor_stamp: 114172000
received_stamp: 1711341013
source:     1
flags:     3
orientation_valid:     0
motion_vector_valid:     1
position_accuracy: 0.024
orientation_accuracy: 3.141
pose:
  pose:
    position:
      x: 1.975
      y: 4.819
      z: 114.9
    orientation:
      x: 0.000
      y: 0.000
      z: 0.201
      w: 0.979
  covariance: [88.21, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 88.21, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 88.21, 0.000, 0.000, 0.000, 0.000, 0.000, 10000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 10000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 9.869]
motion_vector:
  x: 0.045
  y: -0.05
  z: -0.01
vehicle_heading: 1.570
motion_heading: 0.405
---
```

Diese Zeilen sind dabei entscheidend:

- `flags:     3`  
    hier sollte eine `3` stehen: Sie bedeutet, dass der RTK-Status „fixed“ ist  
    `3` bedeutet „fix“, `5` bedeutet „float“ und `0` bedeutet „single“ (herkömmliches GNSS/GPS ohne RTK)

<br>

- `position_accuracy: 0.024`  
  der Wert wird in Metern angegeben. Im Beispiel beträgt die Genauigkeit etwa 2,5 cm – das ist sehr gut.  
  Es kann vorkommen, dass dieser Wert bereits gut ist, der RTK-Status aber noch nicht „fixed“ ist
