---
title: "Bau deinen ersten OpenMower"
linkTitle: "Erste Schritte"
weight: 10
description: "Plane deinen ersten OpenMower-Umbau: benötigte Kenntnisse, passende Mäher, Elektronik, RTK-Korrekturdaten, Kosten und die einzelnen Arbeitsschritte."
---
{{% toc %}}

## Das Wichtigste auf einen Blick

- **Bauzeit:** Ein Wochenende für einen Mäher der YardForce-Klasse; bei individuell angepassten Chassis entsprechend länger
- **Budget:** Die frühere Schätzung von etwa 700 € für den Umbau enthält weder den Mäher noch die RTK-Basisstation. [Ermittle vor dem Kauf die Kosten deiner ausgewählten Teile und Extras]({{% relref "/docs/knowledge-base/getting-started/shopping-list#plan-the-total-build-cost" %}}).
- **Kenntnisse:** Solide Grundkenntnisse in Elektronik, Linux und Mechanik
- **Community:** Über 2.000 Mitglieder auf Discord helfen beim Prüfen deines Aufbaus und bei der Fehlersuche

Du bist neu beim Projekt? Starte mit der [Übersicht]({{% relref "/docs/overview/" %}}). Lies vor dem Umbau auch die Seite zur [Systemarchitektur]({{% relref "/docs/knowledge-base/getting-started/architecture" %}}), um zu verstehen, wie App, ROS, Firmware und Hardware zusammenspielen.


## Wichtige Warnhinweise {#important-warnings}

{{% alert title="Vor dem Start lesen" color="warning" %}}
- **Laufende Entwicklung**: OpenMower wird ständig weiterentwickelt. Stell dich darauf ein, Fehler zu suchen und Software zu aktualisieren.
- **Sicherheit bei Lithium-Akkus**: Du baust deine eigene Ladeelektronik. Mach dich mit den Risiken beim Umgang mit Lithium-Akkus vertraut.
- **Deine Verantwortung**: Vergewissere dich vor jedem Umbauschritt, dass du ihn verstanden hast.
- **Lies die gesamte Dokumentation**, bevor du anfängst, und stelle sicher, dass du alle Umbauschritte verstanden hast.
- **Die Dokumentation wächst mit**: Wir verbessern diese Dokumentation laufend. Wenn du Fehler findest oder Fragen hast, **frag auf Discord nach**.
  {{% /alert %}}


## Ist dein Mäher kompatibel?

Prüfe vor dem ersten Kauf, ob dein Mäher mit OpenMower kompatibel ist.

### Offiziell unterstützte Mäher

Die folgenden Mäher werden mit eigenen Trägerplatinen vollständig unterstützt:

- **YardForce Classic 500(B)** - Am weitesten verbreitet und gut dokumentiert
- **Weitere YardForce-Modelle (SA-Serie)**
- **SABO MOWit 500F** (Serie I und II)
- **John Deere Tango E5** (Serie I und II)
- Viele weitere Modelle mit der universellen Trägerplatine
- Du kannst auch einen Mäher komplett selbst bauen

Weitere Modelle und Umbauten aus der Community findest du in der vollständigen [Liste kompatibler Mäher]({{% relref "/docs/knowledge-base/getting-started/compatible-mowers" %}}).



## Was du können solltest

### Benötigte Kenntnisse

- **Linux-Grundlagen**: Du kommst mit Terminalbefehlen, der Navigation im Dateisystem und dem Bearbeiten von Textdateien zurecht
- **Erfahrung mit dem Raspberry Pi**: Du kannst einen Raspberry Pi einrichten und konfigurieren
- **Elektronikkenntnisse**: Du hast Erfahrung mit Platinen und Steckverbindern und kennst die Grundlagen der elektrischen Sicherheit
- **Mechanische Fähigkeiten**: Du kannst deinen Mäher zerlegen und wieder zusammenbauen

{{% alert title="Hinweis" color="info" %}}
Die OpenMower-App erleichtert die Einrichtung. Trotzdem kann es nötig sein, per SSH nach Fehlern zu suchen oder Einstellungen von Hand anzupassen.
{{% /alert %}}


### Welche Teile du brauchst

Für OpenMower brauchst du diese Hauptkomponenten:

#### 1. Der Roboter
Du brauchst einen kompatiblen Mähroboter samt Gehäuse und Motoren. Seine Elektronik ersetzt du durch die OpenMower-Hardware.
Manche bauen sich auch ein eigenes Mäher-Chassis von Grund auf.

#### 2. OpenMower-Hardware
{{% alert title="Hardware-Version 2" color="success" %}}
Die OpenMower-v2-Hardware ist verfügbar und wird für alle neuen Umbauten empfohlen. Die v1-Hardware ist veraltet. Einzelheiten findest du in der [v2-Ankündigung]({{% relref "/updates" %}}).

**Wenn du v2-Hardware kaufen möchtest:** Wende dich auf Discord an @Apehaenger.
{{% /alert %}}

Die eigens entwickelte Elektronik besteht aus:

- **Core-Board**: Universelles Rechenmodul mit Raspberry Pi CM4, STM32-Controller und IMU
- **Trägerplatine**: Modellspezifische Platine (YardForce, SABO/John Deere oder Universal)
- **3× xESC-Board**: Motorcontroller für BLDC- oder DC-Motoren mit Positionsrückmeldung und geregelter Drehzahl


#### 3. RTK-GPS-System
RTK-GPS ermöglicht eine Genauigkeit im Zentimeterbereich. Dazu werden Korrekturdaten per WLAN oder Funk an den Roboter gesendet.
Du brauchst dafür einen oder zwei RTK-GPS-Empfänger:

- **Rover (erforderlich)**: GPS-Modul auf dem Roboter
- **Basisstation (optional)**: Ein fest installiertes GPS-Modul, das Korrekturdaten liefert, **ODER** Zugang zu einem externen NTRIP-Dienst, der diese Daten über das Internet bereitstellt. In einigen Ländern gibt es kostenlose RTK-Dienste.


## Der Umbau im Überblick

![OpenMower-Umbau im Überblick](flow_chart.jpg)

Beginne mit der [Kompatibilitätsprüfung]({{% relref "/docs/step-by-step/1-check-compatibility" %}}), folge dann der [Anleitung zum Roboterumbau und zur Software-Einrichtung]({{% relref "/docs/step-by-step" %}}). Zum Schluss [erfasst und testest du deine Mähflächen]({{% relref "/docs/step-by-step/4-record-areas-and-use-it" %}}).

## Bereit für den Einkauf? 
**Schau dir die ausführliche [Einkaufsliste]({{% relref "/docs/knowledge-base/getting-started/shopping-list" %}}) an.**


## Hier bekommst du Hilfe

### Discord-Community

In unserer aktiven Discord-Community findest du:
- Hilfe beim Umbau und bei der Fehlersuche
- Infos zur Verfügbarkeit der Hardware
- Tipps und Tricks zur Software
- Diskussionen über Funktionen

🔗 [Zum OpenMower-Discord](https://discord.gg/jE7QNaSxW7)

### Dokumentation und weitere Informationen

- **Diese Dokumentation**: Geprüfte, offizielle Informationen
- **YouTube-Kanal**: Videoanleitungen und Neuigkeiten zum Projekt

Alle Anlaufstellen findest du auf der Seite [Links]({{% relref "/docs/links" %}}).


## Nächste Schritte

Wenn du mit dem Umbau loslegen möchtest:

➡️ [Einkaufsliste durchgehen]({{% relref "/docs/knowledge-base/getting-started/shopping-list" %}})

➡️ [Schritt-für-Schritt-Anleitung lesen]({{% relref "/docs/step-by-step/" %}})
