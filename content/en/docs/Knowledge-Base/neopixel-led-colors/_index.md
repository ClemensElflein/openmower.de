---
title: "Neopixel LED Colors"
linkTitle: "Neopixel LED Colors"
resources:
- src: "**.jpg"

---

{{< imgproc neopixel-status-led Resize 250x />}}

| Color                    | Meaning                                                                                                                             |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **boot sequence**        |                                                                                                                                     |
| dim red                  | firmware booted                                                                                                                     |
| bright red               | RPi powered on                                                                                                                      |
| blinking blue            | halt, IMU not found                                                                                                                 |
| turquoise (blue+green)   | starting sound initialization                                                                                                       |
| blue                     | setting sound volume                                                                                                                |
| brown (red+green)        | sound volume is set                                                                                                                 |
| blinking blue            | warning, sound not available                                                                                                        |
| **end of boot sequence** |                                                                                                                                     |
| orange - red flashing    | emergency mode and ros is disconnected                                                                                              |
| green - red flashing     | emergency mode and ros is connected                                                                                                 |
| steady green	           | ros is connected and no emergency mode is detected<br/>(all voltages are OK, wheels aren't lifted, emergency button is not pressed) |
