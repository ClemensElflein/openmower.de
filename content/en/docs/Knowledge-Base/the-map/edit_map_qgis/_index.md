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
Select the ```file``` radio button and select ```map.geojson``` in the file selector.  Import the map, which should include a polygon layer and a line layer.  The polygon corresponds to map zones, while the line corresponds to the docking point.

## Import Survey Data
Many countries provide aerial cartography data free of charge.  Consult the list below for detailed tutorials related to your country.
* Switzerland : (https://www.gis-hub.uzh.ch/de/how-to-add-a-swisstopo-layer-in-qgis/)
  * Be sure to select the layer ```SWISSIMAGE Zeitreise``` for an orthorectified visual color image of your territory

If you do not live in a country or area with free cartography services, you can make an aerial map using hobby drones.  Be aware that you will need to do orthorectification yourself in order to have a usable map.  To do this, you must have multiple overlapping images to correct for parallax using DEM as explained in (https://gis.stackexchange.com/questions/80899/what-is-the-best-way-to-ortho-rectificate-image-from-the-plane)[this stackexchange post].

## Modify the polygon layers
Set the polygon layer transparency to something useable, so that you can see map features below it.  Use the editing tool to move verticies until you are satisfied with your map.

OpemMower appears to have issues with sharp corners, so be sure to round corners to at least 45 degrees, with radii larger than the robot.

The description of elements must match ```lawn```, ```obstacle```, or ```navigation```.  The color does not matter.

## Export map
Export the map by selecting the polygon layers, right clicking and exporting twice with the context menu.  The export tool can only work on one layer at a time.  The second export (with the same filename) will prompt you to ```Append to existing layers```.  Select yes.  The export should confirm that there is a polygon layer and a line layer.

You must then reformat the ```new_map.geojson``` file into ```map.bag``` and transfer it to OpenMower.
```
./geojson_to_bag.py new_map.geojson map.bag
scp map.bag openmower:/root/ros_home/.ros/map.bag
```
SSH into OpenMower and restart ```openmower.service```
```
ssh openmower
sudo service openmower restart
```
## Troubleshooting
If OpenMower defaults to Area_Recording mode, then either the map or the docking point was not successfully saved.  In the case of the docking point, it can either be re-recorded manually, or the map export can be retried.  In the case of the map being missing, the map should be re-exported.
