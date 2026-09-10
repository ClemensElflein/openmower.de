---
title: "Flächen erfassen"
linkTitle: "Flächen erfassen"
weight: 500
description: "Schließe deinen Umbau ab, indem du Mähflächen erfasst und den Mäher in Betrieb nimmst."
---
Jetzt kannst du die ersten Testfahrten machen und prüfen, ob alles wie erwartet funktioniert. Danach erfasst du die Mähflächen in einer Karte, damit der Mäher selbstständig arbeiten kann.

## Voraussetzungen

- Ein Smartphone oder PC, alternativ ein [USB-Gamepad]({{< relref "/docs/Knowledge-Base/operation/using-a-gamepad" >}})
- Der umgebaute Roboter ist mit deinem Netzwerk verbunden
- Die OpenMower-Software läuft auf dem Roboter
- Die Ladestation ist eingeschaltet
- Der Mäher ist vollständig geladen

## Schritt 4.1: GPS prüfen

![Anzeige der GPS-Qualität]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}/images/gps_quality_indicator.jpg)

Stelle den Mäher in die Ladestation und schalte ihn ein. Nach dem Start sollte die Status-LED dauerhaft grün leuchten.

Damit RTK-GPS funktioniert, muss der Mäher unter freiem Himmel stehen. Versuche es nicht drinnen und decke den Mäher nicht ab.

Öffne die OpenMower-Web-App auf einem beliebigen Gerät im Browser unter [`http://openmower.local:8080`](http://openmower.local:8080/) oder `http://<your-openmower-IP>:8080`.

Warte, bis GPS eine Position ermittelt hat. Das kann bis zu 30 Minuten dauern.

Die aktuelle GPS-Qualität siehst du in der OpenMower-App, wie oben abgebildet.

**Für die folgenden Schritte brauchst du RTK Fixed.** Wenn du keinen guten GPS-Fix bekommst, prüfe deinen RTK-Aufbau und die Konfiguration.

## Schritt 4.2: Ausrichtung initialisieren

Neben seiner Position muss der Roboter auch seine Ausrichtung kennen. Da wir keinen Kompass verwenden, wird sie aus seiner Bewegung abgeleitet. Fahre deshalb zunächst ein Stück mit dem Roboter, damit er seine Ausrichtung bestimmen kann.

Dafür kannst du den Bildschirm-Joystick der OpenMower-App oder ein [per USB angeschlossenes Gamepad]({{< relref "/docs/Knowledge-Base/operation/using-a-gamepad" >}}) verwenden. Halte beim Gamepad die A-Taste gedrückt.

{{% alert title="Warnung" color="warning" %}}
Hebe den Mäher nicht an. Sonst geht die ermittelte Ausrichtung wieder verloren!
{{% /alert %}}

Fahre nun mindestens 50 m mit dem Mäher, teils geradeaus und teils in Achterfiguren. Der Roboter kann die Qualität seiner Ausrichtungsschätzung derzeit nicht selbst beurteilen. Du kannst sie aber beim Fahren in der App prüfen.

Die Ausrichtung ist korrekt initialisiert, wenn:

- sich das Mähersymbol in der App bei Geradeausfahrt ebenfalls geradeaus bewegt und nicht springt
- das Mähersymbol beim Drehen auf der Stelle an derselben Position bleibt und nicht springt

## Schritt 4.3: Eine einfache Karte erfassen

Für die ersten Tests erfassen wir eine einfache Karte. Halte sie zunächst übersichtlich. Zeichne deine eigentliche Karte auf, sobald du sicher bist, dass alles wie erwartet funktioniert.

Die Karte besteht aus drei Teilen: der **Andockposition**, mindestens einer **Mähfläche** und optionalen **Navigationsflächen**.

- **Mähflächen** sind die Bereiche, die gemäht werden sollen. Jede Mähfläche hat eine Umrandung und kann ausgeschlossene Bereiche enthalten, zum Beispiel feste Hindernisse.
- **Andockposition** bezeichnet Position und Ausrichtung der Ladestation. Sie muss nahe an einer Mäh- oder Navigationsfläche liegen, damit der Roboter den Weg zur Ladestation findet.
- **Navigationsflächen** bestehen wie Mähflächen aus einer Umrandung und optionalen Ausschlussbereichen. Der Mäher darf hier fahren, **mäht aber nicht**. Damit kannst du Mähflächen verbinden. Wenn die Ladestation nicht nahe genug an einer Mähfläche liegt, ermöglicht eine Navigationsfläche auch den Weg dorthin.

Der Roboter kennt jetzt seine Position, und du weißt, welche Bereiche du erfassen musst. Beginne mit deiner ersten Karte. Die folgenden Bilder zeigen ein Beispiel.

### Umrandung erfassen

![Umrandung erfassen]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}/images/record_outline.jpg)

- Steuere den Roboter an den Rand der Fläche und richte ihn so aus, dass du **gegen den Uhrzeigersinn** fahren kannst.
- Starte die Aufzeichnung mit **Start Recording**.
- Fahre um die Mähfläche herum. Achte darauf, dass der GPS-Status durchgehend „Fixed“ bleibt.
- Beende die Aufzeichnung mit **Stop Recording**.
- Die Umrandung sollte jetzt grün werden. Sie ist damit fertig erfasst, und du kannst Ausschlussbereiche aufnehmen.

### Optional: Ausschlussbereiche erfassen

![Hindernis erfassen]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}/images/record_obstacle.jpg)

Wenn du Bereiche ausschließen möchtest, zum Beispiel feste Hindernisse, gehe so vor:

- Fahre an den Rand des Ausschlussbereichs und richte den Roboter für die Fahrt **im Uhrzeigersinn** aus.
- Starte die Aufzeichnung mit **Start Recording**.
- Fahre um den auszuschließenden Bereich herum. Achte darauf, dass der GPS-Status durchgehend „Fixed“ bleibt.
- Beende die Aufzeichnung mit **Stop Recording**.
- Die Umrandung sollte jetzt rot werden. Sie ist fertig erfasst, und du kannst weitere Ausschlussbereiche aufnehmen.

### Fläche speichern

![Fläche speichern]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}/images/save_mowing_area.jpg)

Wenn du mit der Aufzeichnung zufrieden bist, klicke auf **Finish Area**. Im Dialog kannst du auswählen, ob du die Fläche als Mäh- oder Navigationsfläche speichern möchtest. Du kannst die Aufzeichnung dort auch verwerfen.

Nach dem Speichern wird die Fläche ausgefüllt dargestellt: Mähflächen grün, Navigationsflächen weiß.

### Andockposition erfassen

![Andockposition erfassen]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}/images/record_docking_position.jpg)

So erfasst du die Andockposition:

- Fahre zu einem Punkt etwa 2 m vor der Ladestation.
- Prüfe, ob du einen GPS-Fix hast, und drücke **Record Docking**.
- Fahre dicht an die Ladestation heran. Die Vorderräder sollten am Rand der Station stehen. **Fahre noch nicht vollständig in die Ladestation!**
- Prüfe erneut den GPS-Fix und drücke **Record Docking**.
- Die App sollte das **Home-Symbol** an deine aktuelle Position verschieben. Jetzt kannst du vollständig in die Ladestation fahren.

### Aufzeichnung abschließen

![Mähen starten]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}/images/start_mowing.jpg)

Beende die Flächenerfassung mit **Exit Recording**. Der Mäher sollte in den Modus **IDLE** wechseln. Mit **Start** startest du den Mähvorgang. Der Mäher dockt ab, wartet auf ein GPS-Signal und mäht die Fläche.
