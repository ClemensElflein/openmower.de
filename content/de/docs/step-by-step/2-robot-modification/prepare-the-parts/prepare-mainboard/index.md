---
title: "Schritt 2.3: Mainboard vorbereiten"
linkTitle: "Mainboard"
weight: 40
description: "Bereite das Mainboard vor, indem du alle Module in die vorgesehenen Steckplätze einsetzt."
---
## Voraussetzungen

Du brauchst:

- **Ein OpenMower-v2-Mainboard**
- **1× xCore-Board**
- **1× Raspberry Pi 4 CM4**
- **3× xESC-Motorcontroller**
- **1× GPS-Modul**
- **Befestigungshalter für das xCore**
- **Optional: CM4-Kühlkörper**

## Schritt 2.3.1: CM4 auf dem xCore montieren

### Wenn du einen CM4-Kühlkörper verwendest

Lege die Abstandshalter wie auf dem Bild auf die beiden unteren Befestigungslöcher des CM4. Auf die beiden oberen Löcher kommen **keine** Abstandshalter:

![Abstandshalter am CM4](images/CM4-spacer.jpg)

Meine Abstandshalter sind 1,7 mm dick und lagen dem Kühlkörper bei.

Wenn du keinen CM4-Kühlkörper verwendest, kannst du diesen Schritt überspringen.

### CM4 auf dem xCore montieren

{{< image-gallery gallery_dir="images/mount-cm4/" >}}

Montiere nun das CM4 auf dem xCore:

1. Richte das CM4 wie auf dem Bild am xCore-Board aus.
2. Lege zwei Finger über die Steckverbinder von xCore und CM4.
3. Drücke vorsichtig nach unten, bis beide Steckverbinder hörbar und fühlbar einrasten.

## Schritt 2.3.2: CM4-Kühlkörper montieren

**Der Kühlkörper ist optional. Die am Ende gezeigten Abstandshalter musst du aber auch ohne Kühlkörper einsetzen.**

{{% alert title="Hinweis" color="info" %}}
Dieser Schritt hängt von deinem Kühlkörper ab. Die Bilder zeigen den Kühlkörper von Berry Base; bei anderen Modellen ist das Vorgehen ähnlich.

Verwende unbedingt Abstandshalter zwischen den Platinen. Sonst üben die Schrauben zu viel Druck auf die Steckverbinder aus.
{{% /alert %}}

{{< image-gallery gallery_dir="images/mount-heat-sink/" >}}

So montierst du den Kühlkörper auf dem CM4:

1. Befestige die Abstandshalter wie auf dem Bild am Kühlkörper.
2. Lege alle Wärmeleitpads auf die passenden Chips.<br />**Wichtig:** Die Pads haben **oben eine durchsichtige Schutzfolie** und unten eine Klebeschicht.<br />**Vergiss nicht, auch die obere Schutzfolie abzuziehen!**
3. Richte den Kühlkörper wie auf dem Bild am CM4 aus.
4. Befestige ihn mit den **beiden unteren Schrauben**. Die oberen beiden Löcher bleiben **frei**.
5. Drücke den 3D-gedruckten Abstandshalter wie auf dem Bild zwischen CM4 und xCore-Board.
6. Setze jetzt am besten die SD-Karte ein, außer bei der Version mit eMMC.

## Schritt 2.3.3: xCore in das Mainboard einsetzen

Das xCore-Board ist jetzt zusammengebaut und kann in das Mainboard eingesetzt werden.

{{% alert title="Hinweis" color="info" %}}
Prüfe vorher, ob die SD-Karte im CM4 steckt. Bei der Version mit eMMC entfällt dieser Schritt.
Je nach Mainboard-Layout kommst du später nur noch schwer an den SD-Kartensteckplatz.
{{% /alert %}}

{{< image-gallery gallery_dir="images/insert-xcore-into-mainboard/" >}}

1. Setze das xCore-Board in einem Winkel von etwa 45 Grad in den Steckplatz des Mainboards ein.
2. Drücke die Platine nach unten, bis sie parallel zum Mainboard liegt. Achte darauf, dass die seitlichen Halteklammern am xCore einrasten.
3. Sichere das xCore-Board mit zwei Schrauben am Mainboard. **Verwende hier keine Abstandshalter oder Ähnliches. Sonst passt das Mainboard nicht in den Mäher, zumindest beim YardForce Classic 500.**

## Schritt 2.3.4: xESCs und GPS in das Mainboard einsetzen

Zum Schluss setzt du die übrigen Module auf das Mainboard.

Richte die Pins der xESCs und der GPS-Platine an den passenden Anschlüssen des Mainboards aus. Es ist in Ordnung, wenn manche ESC-Pins keinen Gegenstecker haben: Sie werden nur zum erstmaligen Aufspielen der Firmware nach der Herstellung verwendet.

Das fertige Board sieht ungefähr so aus. Das Beispiel zeigt eine YardForce-Trägerplatine v1.1.0-beta:

![Fertiges Mainboard](images/finished-mainboard.jpg)

## Schritt 2.3.5: Fertig :tada:

Das Mainboard ist vorbereitet. Fahre jetzt mit der [Anleitung für dein Mähermodell]({{< relref "/docs/step-by-step/2-robot-modification/robot-specific-guides/_index.md" >}}) fort.
