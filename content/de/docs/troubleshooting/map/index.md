---
title: "Probleme beim Kartieren und Erfassen von Flächen beheben"
linkTitle: "Karte"
description: "Hilfe bei Problemen mit der Kartierung und Flächenerfassung in OpenMower. Sichere oder lösche die Karte per SSH, um Mähflächen bei Bedarf neu zu erfassen."
tags: [mapping]
resources:
    - src: "**.png"
---
Diese Anleitung setzt voraus, dass du [eine Karte erfasst]({{< relref "/docs/Knowledge-Base/operation/record-areas" >}}) hast.

<br>

## Karte sichern oder löschen

Die Karte liegt standardmäßig unter
```bash
/home/openmower/ros/map.json
```

Du kannst deine aktuelle Karte jederzeit sichern, indem du dich per SSH anmeldest und die `map.json`-Datei kopierst.

Zum Herunterladen der Datei kannst du einen SFTP-Client wie WinSCP oder Cyberduck verwenden.
```bash
sudo cp /home/openmower/ros/map.json /home/openmower/ros/map.json.backup
```

So löschst du die Karte:
```bash
# stop the openmower service so that it doesnt access the map anymore
openmower stop
# check, if the map file is indeed there.
ls /home/openmower/ros
# delete the map
rm /home/openmower/ros/map.json
# restart OM
openmower start
```
