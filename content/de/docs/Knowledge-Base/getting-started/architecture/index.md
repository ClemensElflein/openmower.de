---
title: "Systemarchitektur"
linkTitle: "Systemarchitektur"
weight: 30
description: >-
  Ein Überblick darüber, wie Software, Firmware und Hardware von OpenMower
  zusammenspielen.
---
OpenMower ist in mehrere Ebenen mit klaren Aufgaben aufgeteilt, die über definierte Schnittstellen miteinander verbunden sind. Dadurch kannst du an der Navigation arbeiten, ohne die Firmware anzufassen, oder eine neue Roboterplattform hinzufügen, ohne ROS zu ändern.

![Diagramm der Systemarchitektur mit den einzelnen OpenMower-Ebenen](images/architecture.svg)

## Die einzelnen Ebenen

### App – Benutzeroberfläche

Die OpenMower-App läuft auf dem Smartphone oder im Browser. Damit kannst du den Mäher steuern, Flächen erfassen und seinen Status verfolgen. Sie kommuniziert im lokalen Netzwerk über **MQTT** mit ROS. Ein eigener ROS-Knoten vermittelt dabei zwischen MQTT-Nachrichten und ROS-Topics.

### ROS – Navigation und Planung (Raspberry Pi CM4)

Auf dem Raspberry Pi Compute Module 4 läuft die gesamte ROS-Navigationssoftware. Hier fallen die übergeordneten Entscheidungen: Wohin soll der Mäher fahren, wie soll er eine Fläche mähen und wann soll er andocken? ROS erhält Sensordaten zu Position, Ausrichtung und Odometrie von der Firmware und sendet Fahrbefehle zurück.

ROS ist bewusst von der Hardware entkoppelt und spricht Motoren oder Sensoren nie direkt an.

### xbot_framework – die Verbindung

ROS und Firmware kommunizieren über **Ethernet** mithilfe von [xbot_framework](https://github.com/xtech/xbot_framework) – einer Middleware, die Nachrichten zwischen den beiden Ebenen austauscht und sie voneinander entkoppelt. Die Navigationssoftware muss deshalb nichts über die konkrete Hardwareplattform wissen.

### Firmware – Motorsteuerung und Sensoren (xCore · STM32H723)

Die Firmware läuft auf dem xCore-Board und steuert die Hardware direkt: Sie regelt die Motoren über xESC-Controller, liest GPS und IMU aus, verwaltet Akku und Ladeelektronik und sorgt dafür, dass die vorgesehenen Sicherheitszustände eingehalten werden. Der Not-Aus-Dienst kann die Stromversorgung unabhängig von ROS unterbrechen. Welche Roboterplattform der Firmware-Quellcode unterstützt, wird beim Kompilieren über die Konfiguration festgelegt.

### RTK-Basisstation – zentimetergenaue Positionsbestimmung

RTK-GPS vergleicht die Signale eines Rovers – des GPS-Empfängers auf dem Mäher – mit denen einer fest installierten Basisstation an einer bekannten Position. Die Basisstation sendet **RTCM-Korrekturdaten** per Funk oder über das Internet (NTRIP) an den GPS-Empfänger des Mähers. So sinkt der Positionsfehler von Metern auf Zentimeter. Die Basisstation muss außerhalb des Mähers stehen und ortsfest sein. Das ist eine grundlegende Voraussetzung von RTK und keine Einschränkung von OpenMower.
