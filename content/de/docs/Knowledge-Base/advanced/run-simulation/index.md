---
asciinema: true
title: "Simulation starten"
linkTitle: "Simulation starten"
weight: 50
description: "Starte die vollständige OpenMower-Software mit einem simulierten Mäher in Docker. So kannst du Mähen, Navigation und App ohne Hardware ausprobieren."
---
## Überblick

In der Simulation laufen die **echte** `open_mower_ros`-Software und die OpenMower-App mit einem simulierten Mäher. `mower_logic`, Navigation, Flächenplanung, Überwachung und die übrigen Komponenten laufen unverändert. Der Knoten `mower_simulation` bildet dabei die Funktionen des Mainboards nach: Antrieb, Mähmotor, IMU, Stromversorgung und GPS.

Damit kannst du:

- OpenMower ausprobieren, bevor du Hardware kaufst oder umbaust.
- Bestimmte Kombinationen von `open_mower_ros`- und App-Versionen testen.
- Das Verhalten des Mähers nachstellen und Fehler untersuchen, ohne dafür einen Roboter im Garten fahren zu lassen.

Alles läuft in Docker und wird über das kleine Hilfsskript `sim.sh` gesteuert.

## Voraussetzungen

- **Docker** mit dem **Compose-v2-Plugin** (`docker compose`). Installation über <https://docs.docker.com/get-docker/>.
- Einen lokalen Checkout des Quellcodes von `open_mower_ros`. Die Simulation liegt dort im Verzeichnis `docker-simulation/`.

Eine GPU ist nicht nötig. Die Simulationsansicht verwendet standardmäßig Software-Rendering und funktioniert auf jedem Host und Betriebssystem: Linux, macOS und Windows.

## Schnellstart

Führe im Verzeichnis `open_mower_ros/docker-simulation/` aus:

```bash
./sim.sh up
```

Beim ersten Start wird das Simulations-Image lokal gebaut. Das kann einige Minuten dauern. Spätere Starts verwenden das fertige Image und dauern nur Sekunden.

Warte nach dem Start etwa eine Minute, bis die Simulation als betriebsbereit gemeldet wird. Öffne dann im Browser:

| URL | Inhalt |
|---|---|
| `http://localhost:6080` | Simulationsansicht (RViz) über noVNC, ohne Passwort und ohne eigenen VNC-Client |
| `http://localhost:3000` | Neue OpenMower-App mit Karteneditor |
| `http://localhost:8080` | Ältere, „blaue“ OpenMower-App auf Flutter-Basis |

Wenn Docker auf einem anderen Rechner läuft, ersetze `localhost` durch dessen Adresse.

<div class="container pb-3 pt-3">
<div class="row">
<div id="sim-up-terminal-player" class=""></div>
</div>
<div class="row">
<div>Die Simulation mit <code>./sim.sh up</code> starten und weitere Befehle von <code>sim.sh</code> sowie <code>rostopic echo</code> ausprobieren.</div>
</div>
</div>
<script>
    AsciinemaPlayer.create(
        '{{< relref "/docs/Knowledge-Base/advanced/run-simulation" >}}/cast/sim-up-terminal.cast',
        document.getElementById('sim-up-terminal-player'),
        { cols: 110, rows: 24, autoplay: false, loop: true }
    );
</script>

Eine Beispielkarte mit Mähfläche und Andockpunkt sowie eine passende Mäherkonfiguration sind bereits eingerichtet. Du kannst sofort losfahren.

## Simulationsansicht (noVNC)

Unter `http://localhost:6080` öffnest du RViz, die Darstellung des simulierten Mähers und seiner Karte. Hier kannst du beobachten, wie der Mäher seine Bahnen abfährt und an der Ladestation andockt.

![Simulationsansicht im Browser mit noVNC / RViz]({{< relref "/docs/Knowledge-Base/advanced/run-simulation" >}}/images/novnc-rviz.png)

Wenn du lieber einen nativen VNC-Client verwendest, verbinde ihn ohne Passwort mit `<host>:5900`.

## Die OpenMower-App

Öffne die App unter `http://localhost:8080`. Sie bietet dieselbe Oberfläche wie bei echter Hardware: Statusanzeige, manuelles Fahren, Flächenerfassung sowie Starten und Stoppen des Mähens funktionieren mit dem simulierten Mäher.

![OpenMower-App mit der Simulation verbunden]({{< relref "/docs/Knowledge-Base/advanced/run-simulation" >}}/images/app-status.png)

Du kannst einen Mähauftrag auf der vorbereiteten Fläche starten und in der Simulationsansicht beobachten, wie der Mäher die geplanten Bahnen abfährt.

## Testzustände in der Simulation erzeugen

Über die **sim-control**-Schnittstelle kannst du in der App gezielt bestimmte Situationen erzeugen. Mit einem echten Mäher wäre das oft aufwendig, zeitintensiv oder mit dem Risiko verbunden, die Hardware zu beschädigen. Die App zeigt den Zustand der Simulation dabei laufend an. So ergänzt die Simulation die Tests im Garten.

Du kannst:

- **Jederzeit manuell eingreifen** – In der Beispielkonfiguration ist `always_allow_joystick` gesetzt. Deine manuellen Fahrbefehle haben damit Vorrang, unabhängig davon, was die Software gerade tut. Du kannst ihn mitten beim Mähen vom Kurs abbringen und beobachten, wie er zurückfindet.
- **Not-Aus auslösen und zurücksetzen** – Prüfe, ob der Mäher korrekt stoppt und den Betrieb wieder aufnimmt.
- **Einen festgefahrenen Mäher simulieren** – Die Räder melden weiter Odometriedaten, während der Mäher tatsächlich auf der Stelle bleibt. So kannst du testen, ob er erkennt, dass er feststeckt, und sich wieder befreien kann.
- **Die Akkuspannung einstellen** – Senke sie ab, um Unterspannung und die Rückkehr zum Laden zu testen, oder simuliere einen Ladevorgang.
- **Die GPS-Qualität umschalten** – Wechsle zwischen einem guten RTK-Fix mit etwa 2 cm Genauigkeit und einem Zustand ohne Fix mit etwa 1 m Genauigkeit. So prüfst du, wie die Navigation auf GPS-Verlust reagiert.
- **Die Position versetzen oder springen lassen** – Versetze den Mäher oder ändere seine Ausrichtung leicht, um die Reaktion auf einen fehlerhaften GPS-Sprung zu testen.
- **Die Ladestation** an die aktuelle Mäherposition **verschieben**.

![Bedienfeld für Simulationszustände in der App]({{< relref "/docs/Knowledge-Base/advanced/run-simulation" >}}/images/sim-control-panel.png)

Diese Bedienelemente findest du in der neuen App unter `http://localhost:3000`. `APP_VERSION` in `.env` muss dafür aktuell genug sein; `edge` enthält sie.

## Versionen auswählen

Welche Versionen laufen, legst du in `.env` im Verzeichnis `docker-simulation/` fest. Die mitgelieferten Standardwerte funktionieren direkt. Passe sie an, um eine bestimmte Kombination zu testen:

| Variable | Bedeutung |
|---|---|
| `VERSION` | Image-Tag von `open_mower_ros`: Release-Tag wie `v1.2.3`, `edge` für den aktuellen main-Stand oder ein PR-/SHA-Tag |
| `APP_VERSION` | Image-Tag der neuen App mit Karteneditor und grünem Design |
| `LEGACY_APP_VERSION` | Image-Tag der älteren Flutter-App |
| `NOVNC_PORT` / `VNC_PORT` | Host-Ports der Simulationsansicht, falls `6080`/`5900` schon belegt sind |
| `DISPLAY_RESOLUTION` | Virtuelle Bildschirmauflösung der Simulationsansicht |

`VERSION` legt sowohl das `open_mower_ros`-Image als auch das daraus gebaute Simulations-Image fest. So passen die Nachrichten- und Dienstdefinitionen des Simulators immer zur getesteten Version.

Baue nach einer Versionsänderung neu, damit sie übernommen wird:

```bash
./sim.sh rebuild
```

`./sim.sh up` baut nie von selbst neu, sondern verwendet das bereits gebaute Image.

## Häufige Befehle

`./sim.sh` ruft `docker compose` auf und ergänzt verständlichere Fehlermeldungen. Die vollständige Liste erhältst du mit `./sim.sh help`.

| Befehl | Wirkung |
|---|---|
| `./sim.sh up` | Aktuelle Images herunterladen und die Umgebung im Hintergrund starten |
| `./sim.sh down` | Umgebung stoppen und ihre Container entfernen |
| `./sim.sh restart` | `down`, dann `up`; lädt auch Images herunter |
| `./sim.sh rebuild` | Neubau aus dem Quellcode erzwingen und starten; nach Änderungen an Code, Konfiguration oder `VERSION` verwenden |
| `./sim.sh logs [service]` | Logs mitlesen, zum Beispiel `./sim.sh logs open_mower_ros` |
| `./sim.sh ps` | Containerstatus anzeigen |
| `./sim.sh reset` | Mitgelieferte Beispielkarte und Parameter wiederherstellen |
| `./sim.sh clean` | **Löscht Daten:** Alle gespeicherten Simulationsdaten löschen; fragt vorher nach |

## Karte zurücksetzen

Karte, Parameter und ROS-Home-Verzeichnis bleiben als normale Dateien unter `./data/` erhalten. Sie sind per Bind-Mount eingebunden und überstehen daher `down` und Neustarts. So stellst du die mitgelieferte Beispielkarte wieder her:

```bash
./sim.sh reset
```

Um **alles** unter `./data/` zu löschen, also Karte, Parameter, ROS-Home und Aufzeichnungen:

```bash
./sim.sh clean
```

## Fehlerbehebung

Wenn die Umgebung festzuhängen scheint, prüfe den Zustand des Simulationscontainers und lies die Logs mit:

```bash
./sim.sh ps                          # mower_simulation_gui should be "healthy"
./sim.sh logs mower_simulation_gui
./sim.sh logs open_mower_ros
```

- **`open_mower_ros` wartet auf die Simulation.** `mower_simulation_gui` startet absichtlich zuerst und stellt den ROS-Master bereit. `open_mower_ros` startet erst, wenn der Container als funktionsfähig gemeldet wird. Das entspricht dem echten Startablauf, bei dem das Mainboard bereit sein muss, bevor die ROS-Software darauf zugreift.
- **Eine Änderung erscheint nicht?** Wenn die Umgebung schon lief, brauchst du wahrscheinlich `./sim.sh rebuild`. `up` allein baut nie selbstständig neu.
- **Ports bereits belegt?** Ändere `NOVNC_PORT` / `VNC_PORT` in `.env`.
- **GPU-Beschleunigung** ist standardmäßig ausgeschaltet und nicht nötig. Wenn du eine GPU hast, entferne die Kommentarzeichen des entsprechenden Blocks für `mower_simulation_gui` in `docker-compose.yaml`. Der Container erkennt die GPU automatisch und fällt auf Software-Rendering zurück, wenn sie nicht nutzbar ist.

## Lokale Quellcodeänderungen testen

Um `open_mower_ros` aus deinem lokalen Checkout statt aus einem veröffentlichten Image zu starten, baue es einmal:

```bash
./sim.sh build-from-source
```

Setze danach `BASE_IMAGE=local/open_mower_ros:local` in `.env` und führe `./sim.sh rebuild` aus.
