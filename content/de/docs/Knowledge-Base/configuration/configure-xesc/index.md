---
title: "xESC konfigurieren"
linkTitle: "xESC konfigurieren"
weight: 200
description: >
  xESC im Mäher konfigurieren 
---
Die xESC-Motorcontroller lassen sich für viele BLDC- und DC-Motoren konfigurieren.
Ihre Firmware basiert auf dem Open-Source-Projekt VESC. Deshalb kannst du sie mit dem VESC Configuration Tool einstellen.

### Voraussetzungen
- **Windows- oder Linux-Computer** für das VESC Configuration Tool
- **VESC Tool (https://vesc-project.com/vesc_tool)** Du kannst das Tool kostenlos herunterladen, indem du die „free“-Version in den Warenkorb legst und den Bestellvorgang abschließt.
- Die **OpenMower-Firmware** muss erfolgreich auf dem xCore-Board installiert sein. Das xCore stellt die Verbindung zwischen deinem Computer und dem xESC her. Falls das noch fehlt, folge der Anleitung [Firmware aktualisieren]({{< relref "/docs/Knowledge-Base/installation/firmware-update" >}}).
- **Optional, aber hilfreich:**<br/>Konfigurationsdateien für deinen Mäher.<br/>Suche im [OpenMower-Repository](https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC) nach den passenden Dateien für deinen Mäher. <br/>Du brauchst drei Dateien:
    - App-Konfiguration als XML: legt unter anderem die Baudrate fest und ist für alle drei xESC-Controller gleich
    - Mähmotor-Konfiguration als XML: Parameter des Mähmotors
    - Fahrmotor-Konfiguration als XML: Parameter der Radmotoren

### Konfigurationsablauf
#### Zugriffe von ROS auf die Controller stoppen
Führe `openmower stop` aus, damit ROS während der Konfiguration nicht auf die Controller zugreift.


#### ESC im Netzwerk bereitstellen
![ESC im Netzwerk bereitstellen]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/openmower-expose-xesc.png)
Führe `openmower expose-xesc [left|right|mower]` aus, um den gewünschten xESC-Controller bereitzustellen. Wähle `left`, `mower` oder `right`.<br/>Der Controller ist dann im lokalen Netzwerk unter `openmower:65102` erreichbar, bis du folgende Tastenkombination drückst: <kbd>Ctrl</kbd> + <kbd>C</kbd>.


#### Mit dem xESC verbinden
![VESC Tool mit dem ESC verbinden]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/ConnectToTheESC.png)
Öffne das VESC Configuration Tool und verbinde dich mit dem xESC:
- `Connection -> TCP` **[1]**
- Trage die IP-Adresse des Mähers oder `openmower` in das Feld „Address“ ein **[2]**.
- Setze den Port auf `65102` **[3]**
- Klicke auf `Connect` **[4]**

{{% alert title="Information" color="info" %}}
Falls diese Warnmeldung erscheint:

![Warnmeldung]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/Firmware_Version_Warning_Message.png)

kannst du sie ignorieren. Das VESC Tool ist mit der Firmware-Version auf dem xESC-Controller rückwärtskompatibel.
{{% /alert %}}


#### xESC konfigurieren

{{< tabpane text=true >}}
{{% tab header="**Wähle deinen Konfigurationsweg**:" disabled=true /%}}
{{% tab header="Fertige Konfigurationen (YardForce)" text=true %}}


#### Konfigurationen übertragen

<div class="tab-gallery">{{< image-gallery gallery_dir="images/upload-configurations" >}}</div>

Wenn das VESC Configuration Tool verbunden ist, übertrage die Konfiguration auf die xESC-Controller:
- **[Bild 1]**: Klicke auf `File -> Load Motor Configuration XML`
- **[Bild 2]**: Wähle die Motor-Konfigurationsdatei für den jeweiligen Motor. Mähmotor und Fahrmotoren verwenden unterschiedliche Dateien
- **[Bild 3]**: Ignoriere die Versionsmeldung, falls sie erscheint
- **[Bild 4]**: Klicke auf `Write Motor configuration`. Bei Erfolg erscheint ein grüner Hinweis.
- **[Bild 5]**: Klicke auf `File -> Load App Configuration XML`. Ignoriere die Versionsmeldung, falls sie erscheint
- **[Bild 6]**: Klicke auf `Write App configuration`. Bei Erfolg erscheint ein grüner Hinweis.
- Drücke im OpenMower-Terminal **<kbd>Strg</kbd> + <kbd>C</kbd>**, um die Netzwerkfreigabe des xESC-Controllers zu beenden.


**Wiederhole diese Schritte für alle drei xESC-Controller.**

{{% /tab %}}


{{% tab header="SABO/John Deere (Abstimmung)" text=true %}}

#### Notwendige Vorbereitungen

1. Baue das Mähmesser ab.
2. Wirklich: Nimm das Messer ab! Das ist ein großer Mäher mit einem starken Motor und einem großen Messer! :skull:
3. Bocke den Mäher hinten so auf, dass sich die Räder frei drehen können. Verwende dafür einen Karton, Klotz oder Ständer.
4. Baue das Mähmesser ab!
6. Kalibriere mit Akkustrom, nicht mit Strom aus der Ladestation. Achte auf einen ausreichend geladenen Akku.
7. Prüfe, ob du das Mähmesser wirklich abgebaut hast!


#### Fahrmotoren kalibrieren: erst links, dann rechts

Kalibriere zuerst den linken Antrieb und wiederhole den Vorgang danach rechts.

1. **Echtzeitdaten aktivieren:** Später prüfen wir die Kalibrierung anhand eines bekannten Referenzwerts. Auch während der Kalibrierung sind die Werte im mit 2 markierten Fenster hilfreich. Aktiviere deshalb zuerst die Echtzeitdaten:<br>
   ![RT Data]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_3_realtime_data.jpg)
1. Starte den **FOC Calibration Wizard**:<br>
   ![FOC-Kalibrierung starten]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_1.jpg)<br>

1. Gib nun die Motordaten ein. **Diese Werte gelten für den linken und rechten Fahrmotor.** Für den Mähmotor verwenden wir andere Werte:<br>
   <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_2.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_3.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_4.jpg" style="vertical-align: middle; width:31%"><br>

   <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_5.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_6.jpg" style="vertical-align: middle; width:31%"> 🡆 <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_7.jpg" style="vertical-align: middle; width:31%"><br>

1. Ändere nach der Kalibrierung **nicht die Drehrichtung**, auch wenn sich das linke Rad bei der Kalibrierung vorwärts und das rechte rückwärts dreht:

   <img src="{{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_4_voc_8.jpg" style="vertical-align: middle; width:31%">
9. Prüfe nach erfolgreicher Kalibrierung das Ergebnis:
   ![Test ausführen]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_5_test.jpg)<br>

   Teste mit „**D 0,4**“ (1) und drücke die Wiedergabetaste für „Duty cycle“ (2). Wenn die Stromaufnahme **≤ 0,15 A** (3) beträgt und der Motor unauffällig klingt, ist die Kalibrierung gut.<br>
   Teste auch höhere Tastgrade. Der Motor wird dabei lauter, sollte aber gleichmäßig laufen und unauffällig klingen. Falls nicht, drücke STOP (4).

10. Lade als letzten wichtigen Schritt über _File → Load App Configuration XML_ die passende ESC-App-Konfiguration `SABO_Drive-App.xml` (siehe [SABO-ESC-Konfigurationen](https://github.com/xtech/hw-openmower-sabo/tree/main/Configs/xESC)) und drücke rechts auf `↧A` („Write app configuration“).

Geschafft :satisfied:<br>
… **aber noch nicht fertig** :v: … Wiederhole den gesamten Vorgang für den rechten Antrieb.

Beende `openmower expose-xesc left` mit <kbd>Strg</kbd>+<kbd>C</kbd> und mache mit `openmower expose-xesc right` weiter.


#### Mähmotor kalibrieren

Für den ESC des Mähmotors verwendest du denselben Ablauf mit angepassten Werten:

1. `openmower expose-xesc mower`
1. Verwende im FOC Calibration Wizard diese Werte:
   - Tab "Motor" = Medium Inrunner ~750g
     - Advanced: Max Power Loss = 200, Motor Poles = 8
   - Tab "Battery"
     - Battery Capacity = 3.9Ah (wie zuvor)
   - Tab "Setup"
     - Gear Ratio = Check Direct Drive
     - Motor Poles = 8
     - Motor Temp. Sensor = disabled

1. Teste mit „**D 0,08**“. Die Stromaufnahme sollte **≤ 0,52 A** betragen, bei abgebautem Messer
1. Drehrichtung des Messers prüfen/anpassen:<br>
   Das Messer muss sich gegen den Uhrzeigersinn drehen, wenn du von unten auf die Achse schaust. Prüfe das bei niedriger Drehzahl, zum Beispiel mit „D 0,02“.

   Wenn es sich im Uhrzeigersinn dreht, ändere die Richtung über: _Motor Settings → General → Tab General → Invert Motor Direction_. **Vergiss nicht, die Änderung mit „Write motor configuration“ über `↧M` zu speichern!**

1. Lade über _File → Load App Configuration XML_ die passende ESC-App-Konfiguration `SABO_Mower-App.xml` (siehe [SABO-ESC-Konfigurationen](https://github.com/xtech/hw-openmower-sabo/tree/main/Configs/xESC)) und drücke rechts auf `↧A` („Write app configuration“).

1. Messerdrehzahl begrenzen:<br>
   Begrenze die maximale Drehzahl unbedingt auf den Wert des Originalmähers! Sonst können die Motorlager beschädigt werden. Noch gefährlicher: Das Messer könnte sich lösen und wegfliegen. :skull:
   ![Drehzahl begrenzen]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_8_mow_rpm.jpg)

1. Akkustrom begrenzen:<br>
   Begrenze den Akkustrom passend zur Hardware-Version deiner SABO-Trägerplatine:
   | SABO-Trägerplatinen-Version | VESC-Einstellung `Battery Current max.` | Akkusicherung             | Mähmotorsicherung  |
   | -------------------- | ----------------------------------- | ------------------------ | --------- |
   | v0.2.x               | 6A                                  | Konservativ: 4 A mittelträge   | -         |
   | v0.4.x               | 4.5A                                | Konservativ: 4 A mittelträge   | -         |
   | v0.5.x               | 9A                                  | 4 A mittelträge, hier aber nicht maßgeblich | 8 A mittelträge |
   
   > **Hinweis:** Die oben angegebenen Werte für `Battery Current max.` sind theoretische Auslegungsgrenzen auf Grundlage konservativer Berechnungen der Leiterbahnbreiten.  

   > **Warnung:** Wenn du einen Wert oberhalb des Nennstroms der Originalsicherung wählst, musst du damit rechnen, dass sie durchbrennt und durch eine Sicherung mit höherem Nennstrom ersetzt werden muss.

   ![Ströme begrenzen]({{< relref "/docs/Knowledge-Base/configuration/configure-xesc" >}}/images/sabo/vesc_9_mow_currents.jpg)

{{% /tab %}}


{{% tab header="Neues Modell? Finden wir die passenden Werte" %}}

Such dir deinen Weg. Dein Umbau, deine Regeln.

{{% /tab %}}

{{< /tabpane >}}
