---
title: "Schritt 3.1: WLAN verbinden"
linkTitle: "WLAN verbinden"
weight: 10
description: >
  Verbinde den Mäher mit dem WLAN.
---
## Schritt 3.0: Stromversorgung sicherstellen
Sorge dafür, dass der Akku während der Einrichtung nicht leer wird. Ohne Stromversorgung ist er wahrscheinlich leer, bevor du fertig bist.
Normalerweise kannst du den Roboter dafür in die Ladestation stellen, außer beim Universal-Board.


## Schritt 3.1: Hotspot suchen
<div class="container-fluid m-0 p-0">
<div class="row">
<div class="col">
Schalte den Mäher ein und suche auf deinem Mobilgerät nach WLAN-Netzen.
OpenMowerOS erstellt automatisch einen Hotspot mit dem Namen `OpenMower-<Some Number>`, wobei am Ende eine Zahl steht. Verbinde dich mit diesem Hotspot.

Falls dein Mobilgerät meldet, dass das Netzwerk keinen Internetzugang hat, wähle aus, dass du es trotzdem verwenden möchtest.
</div>
<div class="col-3">

![connect_wifi_screen_1.png](images/connect_wifi_screen_1.png)

</div>
</div>
</div>

## Schritt 3.2: Konfigurationsseite im Browser öffnen
<div class="container-fluid m-0 p-0">
<div class="row">
<div class="col">
Manche Geräte erkennen, dass der Hotspot keinen Internetzugang bietet, und öffnen automatisch eine Konfigurationsseite.

Falls dein Gerät das nicht tut, öffne den Browser auf deinem Smartphone und rufe diese Adresse auf: [http://10.41.0.1/](http://10.41.0.1/).
</div>
<div class="col-3">

![connect_wifi_screen_1.png](images/connect_wifi_screen_1.png)

</div>
</div>
</div>

### Schritt 3.3: WLAN-Zugangsdaten eingeben
Wähle auf der Konfigurationsseite dein WLAN aus und gib das Passwort ein. Klicke dann auf „Connect“.

Das OpenMower-WLAN sollte verschwinden. Der Roboter verbindet sich nun mit deinem Heimnetzwerk.


### Schritt 3.4: Verbindung prüfen
Prüfe nun, ob der Mäher erfolgreich gestartet ist:
- Teste die Verbindung von einem anderen PC in deinem Netzwerk mit `ping openmower.local`. Das sollte funktionieren. Alternativ kannst du in der Routeroberfläche nachsehen, ob das Gerät verbunden ist.
- Prüfe, ob du den Mäher per SSH erreichst: `ssh openmower@openmower.local`, Passwort `openmower`.
- Prüfe, ob sich das Terminal des Mähers im Browser öffnen lässt. Rufe dazu diese Adresse auf: [http://openmower.local:7681/](http://openmower.local:7681/)

