---
title: "GPS Base Setup"
linkTitle: "GPS Base Setup"
weight: 200
description: >
  Build your own GPS RTK base!
---

This part of the documentation is work in progress. There are many ways of setting up the RTK base, here is one using RPi 0W, ZED-F9P and a web based software RTKBase.

## Prerequisites
- [Raspberry Pi 0W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
- sd card
- power supply for RPi
- [Ardusimple ZED-F9P](https://www.ardusimple.com/product/simplertk2b-basic-starter-kit-ip65/)
- A windows PC
- stable internet connection (no disconnection within one hour)
## Installation
If you know about RPi and have already a functional OS, you may head on to "Software", but in my case it did not work using a 32-bit RPi image. 
### Preparing sd card
- Download [RPi Imager](https://www.raspberrypi.com/software/) for windows
- Start Imager:
  
 ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/d476563b-2693-472f-bfa6-34cf1311e65d)
- Choose your RPI (in my case RPi 0W)
  
 ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/1a24f9cc-d0d0-4cb7-b892-90c5b1ba93a3)
- Choose Operating system "Raspberry Pi OS lite (64bit)
  ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/e6b44aa0-6470-44b6-833f-164fb7ae5dad)

 ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/f6b0b5a1-1b60-4c56-a379-392f302e5424)

- Select your sd card:
  
 ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/c2e0268b-58a8-44b0-91a2-a799bb4fc3af)
- Press next so this:
 
  ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/6016215b-4fb0-4987-825f-daec47b29621)
  - Edit settings like the following (and user your WiFi settings), where you set a good password for your Pi account. Username and password are case sensitive!
   
    ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/4768c937-6235-40fc-ab5e-42716a0524ea)
- activate SSH:
  
  ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/81771014-ea43-422a-90e1-d1e493a67990)
- Press save to see this:
  
 ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/d9713463-4c1e-4b56-9503-7fa8be259798)

- Click on YES and allow to overwrite the data on your sd card (if you are sure, that you will not miss them). It will start downloading and writing the data:
- 
  ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/8faf9864-f557-46c8-b4f9-0273558efd88)

- Wait until it is finished, it may take half an hour, depending on your internet connection ;-)
  
### Start your RTKBase RPi
- Put your sd card into your RPi
- Connect ZED-F9P via usb to your RPi (NOT after the installation, it will be configured during installation).
- Power your RPi
### Connect to RPi
- Get from your router the IP of your RPi
- Start [PuTTY](https://putty.org) and connect to RPi, where you enter the local IP of your RPi
  
  ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/f9ae280a-e766-4d49-b64b-75426b92418b)
- Enter your Username Pi, press enter and than enter your password:
  ![grafik](https://github.com/ClemensElflein/openmower.de/assets/43208283/e7cb379a-4689-4d7c-a210-36986e49abe2)

### Software
- Is your ZED-F9P connected? Do it!
- We will use [RTKBase](https://github.com/Stefal/rtkbase)
- To install it, you can use the following lines, which you can copy and paste together:
```bash
cd ~
sudo wget https://raw.githubusercontent.com/Stefal/rtkbase/master/tools/install.sh -O install.sh
sudo chmod +x install.sh
sudo ./install.sh --all release
```
## Setting up your RTKBase
Start a browser and enter the IP address of your RTKBase. You will get this:

### Options to activate
- Not documented yet
### Find the position of your RTKBase
- Not documented yet
