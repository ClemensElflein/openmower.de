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
If you know about RPi and have already a functional OS, you may head on to "Software", but in my case it did not work using an older image. 
### Preparing sd card
- Download [RPi Imager](https://www.raspberrypi.com/software/) for windows
- Start Imager:
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/d476563b-2693-472f-bfa6-34cf1311e65d" width="120">
- Choose your RPI (in my case RPi 0W, choosing wrong RPi will most probably result in many problems)
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/1a24f9cc-d0d0-4cb7-b892-90c5b1ba93a3" width="120">
- Choose Operating system "Raspberry Pi OS lite (legacy, 32bit)
  
  ![]() <img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/54dadde5-2595-4b1f-ab23-84c5f2a095cb" width="120">

  ![]() <img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/85015eb9-3098-494d-852e-aed4403cd6ef" width="120">

- Select your sd card:
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/c2e0268b-58a8-44b0-91a2-a799bb4fc3af" width="120">
- Press next so this will appear:
 
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/6016215b-4fb0-4987-825f-daec47b29621" width="120">
- Edit settings like the following (and use your personal WiFi settings and country), where you set a good password for your Pi account. Username and password are case sensitive!
   
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/4768c937-6235-40fc-ab5e-42716a0524ea" width="120">
- activate SSH:
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/81771014-ea43-422a-90e1-d1e493a67990" width="120">
- Press save to see this:
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/d9713463-4c1e-4b56-9503-7fa8be259798" width="120">

- Click on YES and allow to overwrite the data on your sd card (if you are sure, that you will not miss them). It will start downloading and writing the data:
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/8faf9864-f557-46c8-b4f9-0273558efd88" width="120">

- Wait until it is finished, it may take half an hour, depending on your internet connection ;-)
  
### Start your RTKBase RPi
- Put your sd card into your RPi
- Connect ZED-F9P via usb to your RPi (NOT after the installation, it will be configured during installation).
- Power your RPi
### Connect to RPi
- Get from your router the IP of your RPi
- Start [PuTTY](https://putty.org) and connect to RPi, where you enter the local IP of your RPi
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/f9ae280a-e766-4d49-b64b-75426b92418b" width="120">
- Enter your Username Pi, press enter and than enter your password:
  
  ![]() <img src="https://github.com/ClemensElflein/openmower.de/assets/43208283/e7cb379a-4689-4d7c-a210-36986e49abe2" width="120">
 
  ![]() <img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/00101910-7c7d-44cd-97c7-f08ac9ca32df" width="120">

### Software
- Is your ZED-F9P connected? Do it!
- We will use [RTKBase](https://github.com/Stefal/rtkbase)
- To install it, you can use the following lines, which you can copy and paste together:
  ```bash
  cd ~
  wget https://raw.githubusercontent.com/Stefal/rtkbase/master/tools/install.sh -O install.sh
  sudo chmod +x install.sh
  sudo ./install.sh --all release
  ```
- A very long output should follow. It ends with:
  ```bash
  GNSS Configuration: done
  ################################
  STARTING SERVICES
  ################################
  Created symlink /etc/systemd/system/multi-user.target.wants/str2str_tcp.service → /etc/systemd/system/str2str_tcp.service.
  Job for gpsd.service failed because the control process exited with error code.
  See "systemctl status gpsd.service" and "journalctl -xe" for details.
  ################################
  END OF INSTALLATION
  You can open your browser to http://192.168.178.34 (here the editor deleted IPV6)
  ################################
  Pi@RTKBase:~ $
  ```
- Installation finished, go on and configure your RTKBase
  
## Configuring your RTKBase
  - Start a browser and enter the IP address of your RTKBase. You will get this:
    
    ![]()<img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/cb9c01d6-637a-4a97-8f84-54acf576648c" width="120">

  - Enter as password admin. On the following site press the copy symbol right to PPP.
    
    ![]()<img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/72d24226-570f-4394-b615-04975b89ddf2" width="120">

  - Go to settings and press "options" right to "Main Service", than paste your coordinates to "Base coordinates":
    ![grafik](https://github.com/karlranseierausrom/openmower.de/assets/43208283/505978be-6c3e-4ead-bbd7-cdc914aa1c52" width="120">

  - Press on options again, than on options right to "Caster Service"
  
    ![]()<img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/0defa09d-ccb1-488c-abc3-c32eb67390f9" width="120">
  - Here you have to enter the setting set up in your mower, standard is: username gps and password gps. Select the right mount point. I have named it like my city, in mower config and here.
  - Save the config
  - Switch on "Caster Service" and "File Service", it should look like this:
    
    ![]()<img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/2fe64f78-dbf9-415b-8e52-5a53630dfa40" width="120">

  - Eventually change your password below these options.
  - At logs you should find at least two files:
    
    ![]()<img src="https://github.com/karlranseierausrom/openmower.de/assets/43208283/14ef9870-23a4-4a5f-a19d-1bf9718d5966" width="120">

### Find the position of your RTKBase
- You have set up the logging of your position as mentioned above by activating "file service". You need to wait for a day or week to be able to average all the values.
- Next step will be added soon.
  
