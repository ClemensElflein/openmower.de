---
title: "Notes on building an SA900ECO"
linkTitle: "SA900ECO Build"
weight: 100
description: >-
     This includes some notes on building an SA900ECO with the 0.13 mainboard from Vermut's shop.
---

## YardForce SAxxxECO series notes


Here are my findings for an SA900ECO build but the findings may also be useful for an SA650ECO which looks very similar:

Build Notes:
- Generally you can follow the steps for the Classic 500 build using Vermut 0.13x kit, it is broadly similar. https://openmower.de/docs/robot-assembly/assemble-the-robot/photo-guide/
- After opening up You can remove the front wire detector bar and put aside for now. Not needed.
- One way to mount the SimpleRTK antenna is to bold the square green board shield on top of the mower at the front, and run the cable inside the (now-removed) wire detector bar gromet a the front of the main housing. top on the front.
- Battery connector on the new vermut board i bought was a bit weak, and also the existing cable from the outer housing to the inner board was a bit short, so this connector snapped off.  It is probably worth upfront either putting an extension on the cable or solder some wires to the board in it's place with the connectors of your choice to extend the charging cable. I soldered a short 10cm cable onto the board with XT connectors to allow a bit more room when removing the cover for maintenance.
- The SA900 has x4 hall sensors for the x4 wheels, compared to just two for the 500 Classic I believe.  There are x4 Hall sensor sockets on the 0.13 version mainboard - x2 for the front wheels and x2 for the emergency stop.  However (personal choice) I plugged all four wheels into the
- Recommendation is to put a 4A slow fuse in the inside of the two fuse sockets, I would (Maybe fast-blow is better but just copying @ow !)
- When closing the mower up again make sure the cables underneath are tight and tidy and wont get cut by mower blades!
- When assembling the charger, it is largely similar but slightly different to the YF Classic 500 one, and you will need some flush cutters to hack out a small bit of plastic when you come to close it up again. You will see.  It’s not problem.


Mainboard Pico firmware:
- The hall sensors on the SA900ECO work the opposite way round to on the classic so you firstly need to edit the main Firmware/LowLevel/main.cpp file in the OpenMower repo to invert the hall sensors (remove the "!"'s leaving: approx line 150:
```
    uint8_t emergency_read =  gpio_get(PIN_EMERGENCY_3) << 1 | // Stop1
                              gpio_get(PIN_EMERGENCY_4) << 2 | // Stop2
                              gpio_get(PIN_EMERGENCY_1) << 3 | // Lift1
                              gpio_get(PIN_EMERGENCY_2) << 4 | // Lift2
```
- If like me you have connected all wheel hall sensors to the x4 sockets on the mainboard, then the Emergency STOP button isn't used this way, and pins 3&4 instead become two more lift sensors.

Firstly need to change datatypes.h to take stop button out of action and add x2 more lift sensors:
```
#define LL_EMERGENCY_BIT_LIFT1 LL_EMERGENCY_BIT_HALL1
#define LL_EMERGENCY_BIT_LIFT2 LL_EMERGENCY_BIT_HALL2
#define LL_EMERGENCY_BIT_LIFT3 LL_EMERGENCY_BIT_HALL3
#define LL_EMERGENCY_BIT_LIFT4 LL_EMERGENCY_BIT_HALL4
#define LL_EMERGENCY_BITS_LIFT (LL_EMERGENCY_BIT_LIFT1 | LL_EMERGENCY_BIT_LIFT2 | LL_EMERGENCY_BIT_LIFT3 | LL_EMERGENCY_BIT_LIFT4)
#define LL_EMERGENCY_BITS_STOP 0b01000000 // placeholder for SA900ECO config - this is wrong and this bit can never be achieved.
```
and then back in main.cpp change the lift logic to something akin to:
```
// Handle lifted (both wheels are lifted)
    // Calculate the number of lift emergency bits set
    int8_t bitsSetCount = 0; 
    for(int i = 0; i < 8; i++){
        bitsSetCount += ((emergency_read & LL_EMERGENCY_BITS_LIFT) >> i) & 0x01;
    }

    if (bitsSetCount > 1) {
        // If we just lifted (more than one wheel), store the timestamp
        if (lift_emergency_started == 0) {
            lift_emergency_started = millis();
        }
    } else {
        // Not lifted, reset the time
        lift_emergency_started = 0;
    }
```

Then build with platformIO and copy onto RasPi4 and then upload_firmware.sh flash onto PICO.


ESC's

- Download VESCtool and learn to connect to the x3 ESCs and upload the write XML config file onto each ESC for the SA650ECO (which is broadly similar).  I have set my mow motor max rpms to 12500 I think, FYI.  https://github.com/ClemensElflein/OpenMower/tree/main/configs/xESC
