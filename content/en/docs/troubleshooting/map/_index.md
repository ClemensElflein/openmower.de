---
title: Troubleshoot mapping/recording areas
linkTitle: Map
tags: [map, mapping, maps]
resources:
    - src: "**.png"
---

We assume that you at least followed [Record a map]({{< relref "/docs/software-setup/record-a-map/" >}}).

# Making a backup and/or removing a map.

The default location of the map can be found under
```bash
/root/ros_home/.ros/map.bag
```

You can always backup your current map by logging in via SSH and copying the .bag file.

If you want to retrieve the file you can use an SFTP client like WinSCP or Cyberduck.

```bash
sudo cp /root/ros_home/.ros/map.bag /root/ros_home/.ros/map.bag.backup
```

To delete the 

```bash
# stop the openmower service so that it doesnt access the map anymore
sudo service openmower stop
# check, if the map file is indeed there.
ls /root/ros_home/.ros/map.bag
# delete map
sudo rm /root/ros_home/.ros/map.bag
# restart OM
sudo service openmower start
```
# Map Editor

There's a WIP map editor made by Nekraus, JavaBoon and Eddi using Python which you can try and use to fix your map or add in obstacles.

[Map editor](https://github.com/0815eddi/OpenMower/blob/main/utils/map/mowareareader.py)