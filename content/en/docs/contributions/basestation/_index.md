---
title: Adjusting map position after a basestation change
linkTitle: Basestation location change
description: >
  Sometimes you have to change the location of the NTRIP base station or you change to another NTRIP provider. In that
  case your map will probably shift position and you cannot use the mower anymore because it will not be accurate when
  mowing.
---


When you use the OM_DATUM_LAT and OM_DATUM_LONG DATUM fields in the mower_config.txt, you can shift the map around.

The procedure if you change the NTRIP base, is to change the DATUM Fields (`OM_DATUM_LAT` for the left and right,
`OM_DATUM_LONG` for up and down) in the mower_config.txt file. What you basically do when you change the DATUM fields is
shift the complete map up/down/left/right.

In order to position the map aligned with a fixed point on the map, you can use the docking position of the mower. To do
this properly, you have to undock the mower via the area recording buttons, drive a little bit around for an accurate
positioning of the mower and then dock the mower manually using the area recording buttons.

After docking, you see in the web interface that the mower is a bit off the docking position. You adjust the position of
the map just a bit. To move the map horizontally, you adjust the `OM_DATUM_LAT` a bit and to move the map vertically,
adjust the `OM_DATUM_LONG`.  (The precision is depending on your position on the globe, but the 7th digit will give you
about 1cm movement per digit). If you move the map down, the position of the mower will go up on the map and vise versa.

Remember to reload the exports (the easy way is a reboot of the pi if you are patient and lazy) and then drive around
again a bit via the area recording buttons and dock manually again. In that way, you have a constant correct location
when adjusting the map position. When you think it is all good, then go ahead, start mowing and let the mower return to
docking immediately to see if the docking works precisely and the mower docks automatically and properly.

Then start mowing, the mower will do the outline first (normally 4 rounds, check the 4th round very thoroughly, that is
the round closest to the edge). If all is ok, you are good to go.
