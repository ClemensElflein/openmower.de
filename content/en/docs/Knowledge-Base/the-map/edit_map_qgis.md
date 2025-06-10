---
title: "Modifying Map Data using Aerial Data with QGIS"
linkTitle: "Editing Maps with QGIS"
weight: 100
description: >-
     How to edit the mowing map using survey data.  QGIS is an open source geoinformatics tool capable of integrating vector data from OpenMower as well as commercially available survey data.
---

## Export Map Data from OpenMower

Copy the ```map.bag``` file from Openmower to your working directory, along with ```mower_config.txt```

```
scp openmower:/root/ros_home/.ros/map.bag . && scp openmower:/boot/openmower/mower_config.txt .
```
Download and install the OpenMower to GeoJSON tool from https://github.com/rovo89/open_mower_geojson:

```
git clone https://github.com/rovo89/open_mower_geojson
cd open_mower_geojson
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Convert the ```map.bag``` file into GeoJSON

```
source .venv/bin/activate
source /boot/openmower/mower_config.txt
./bag_to_geojson.py map.bag map.geojson
```
## Import GeoJSON into QGIS, along with survey data
Import GeoJSON file:
```
Layer -> Data Source manager -> Vector
```
Select the ```file``` radio button and select ```map.geojson``` in the file selector.
