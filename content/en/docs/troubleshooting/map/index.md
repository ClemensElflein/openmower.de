---
title: Troubleshoot mapping/recording areas
linkTitle: Map
tags: [map, mapping, maps]
resources:
    - src: "**.png"
---

We assume that you at least followed [Record a map]({{< relref "/docs/Knowledge-Base/record-areas" >}}).

<br>

# Making a backup and/or removing a map.

The default location of the map can be found under
```bash
/home/openmower/ros_home/map.json
```

You can always back up your current map by logging in via SSH and copying the .json file.

If you want to retrieve the file, you can use an SFTP client like WinSCP or Cyberduck.
```bash
sudo cp /home/openmower/ros_home/map.json /home/openmower/ros_home/map.json.backup
```

To delete the map
```bash
# stop the openmower service so that it doesnt access the map anymore
openmower stop
# check, if the map file is indeed there.
ls /home/openmower/ros_home
# delete maps (both .bag and .json)
rm /home/openmower/ros_home/map.bag
rm /home/openmower/ros_home/map.json
# restart OM
openmower stop
```
