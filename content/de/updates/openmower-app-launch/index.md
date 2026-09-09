---
title: "Die neue OpenMower-App ist da"
date: 2026-03-16
author: "Clemens Elflein"
description: "Eine neue App für OpenMower steht zum Ausprobieren bereit, zunächst mit einem Karteneditor. Sie läuft auf OpenMowerOS v2 zusammen mit dem gerade veröffentlichten ROS v1.1.1."
---
Community-Mitglied [@rovo89](https://github.com/rovo89) hat im Hintergrund an etwas Tollem gearbeitet: der **OpenMower-App**, einer komplett neuen Anwendung für deinen OpenMower.

Du findest sie hier: **[github.com/xtech/openmower-app](https://github.com/xtech/openmower-app)**

### Was sie bisher kann

Aktuell enthält die App einen **Karteneditor** und einige Diagnoseinformationen. Den Karteneditor wollten wir euch zuerst zur Verfügung stellen: Er ist der nützlichste Einstieg und ermöglicht es, Mähflächen direkt im Browser zu verwalten.

Wenn du **OpenMowerOS v2** nutzt, ist die Einrichtung unkompliziert:

1. Öffne `http://<mower-ip>:5001/compose/openmower` im Browser.
2. Wechsle in den Bearbeitungsmodus und ergänze deine `compose.yaml` oberhalb der Zeile `# Dockge-specific extras` um Folgendes:

```yaml
  app:
    image: ghcr.io/xtech/openmower-app:edge
    container_name: app
    ports:
      - 3000:3000
    restart: unless-stopped
```

3. Ergänze die neue URL auch im Abschnitt `x-dockge`:

```yaml
x-dockge:
  urls:
    - http://${HOSTNAME}:8080
    - http://${HOSTNAME}:3000
```

4. Klicke auf **Deploy**. Die App ist dann unter `http://<mower-ip>:3000` erreichbar.

Du nutzt noch kein OSv2? Du kannst die App trotzdem ausprobieren, indem du den Container manuell startest.

### ROS-Version

Du solltest **ROS v1.1.1** verwenden, das [zeitgleich veröffentlicht wurde]({{< relref "ros-v1-1-1" >}}). Der Karteneditor funktioniert auch mit v1.1.0, allerdings wird dort das „active“-Flag der Mähflächen nicht berücksichtigt. Aktualisiere deshalb nach Möglichkeit.

### Warum „OpenMower-App“?

Nach einigem Überlegen haben wir uns für **OpenMower-App** entschieden, obwohl die bisherige App bereits so heißt. Sobald die neue App ausgereift ist, wird die alte abgelöst. Damit erledigt sich auch die Verwechslungsgefahr.

Weitere Funktionen sind unterwegs. Tolle Arbeit, rovo89 – das ist erst der Anfang!
