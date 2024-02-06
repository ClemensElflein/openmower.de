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
  
  ![]() <img src="Imager1.png" width="120">
- Choose your RPI (in my case RPi 0W, choosing wrong RPi will most probably result in many problems)
  
  ![]() <img src="./Imager2.png" width="120">
- Choose Operating system "Raspberry Pi OS lite (legacy, 32bit)
  
  ![]() <img src="./Imager3.png" width="120">

  ![]() <img src="./Imager4.png" width="120">

- Select your sd card:
  
  ![]() <img src="./Imager5.png" width="120">
- Press next so this will appear:
 
  ![]() <img src="./Imager6.png" width="120">
- Edit settings like the following (and use your personal WiFi settings and country), where you set a good password for your Pi account. Username and password are case sensitive!
   
  ![]() <img src="./OSCustom1.png" width="120">
- activate SSH:
  
  ![]() <img src="./OSCustom.png" width="120">
- Press save to see this:
  
  ![]() <img src="./OSCustom2.png" width="120">

- Click on YES and allow to overwrite the data on your sd card (if you are sure, that you will not miss them). It will start downloading and writing the data:
  
  ![]() <img src="./Imager7.png" width="120">

- Wait until it is finished, it may take half an hour, depending on your internet connection ;-)
  
### Start your RTKBase RPi
- Put your sd card into your RPi
- Connect ZED-F9P via usb to your RPi (NOT after the installation, it will be configured during installation).
- Power your RPi
### Connect to RPi
- Get from your router the IP of your RPi
- Start [PuTTY](https://putty.org) and connect to RPi, where you enter the local IP of your RPi
  
  ![]() <img src="./Putty1.png" width="120">
- Enter your Username Pi, press enter and than enter your password:
  
  ![]() <img src="./Putty2.png" width="120">
 
  ![]() <img src="./Putty3.png" width="120">

### Software
- Is your ZED-F9P connected? Do it!
- We will use [RTKBase](https://github.com/Stefal/rtkbase)
- To install it, you can use the following lines, which you can copy and paste at once. The original recommendation is no sudo in front of chmod. That did not work for me.
  
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
    
    ![]()<img src="./RTKBase01.png" width="120">

  - Enter as password admin. On the following site press the copy symbol right to PPP.
    
    ![]()<img src="./RTKBase02.png" width="120">

  - Go to settings and press "options" right to "Main Service", than paste your coordinates to "Base coordinates":
    
    ![]()<img src="./RTKBase03.png" width="120">

  - Press on options again, than on options right to "Caster Service"
  
    ![]()<img src="./RTKBAse04.png" width="120">
  - Here you have to enter the setting set up in your mower, standard is: username gps and password gps. Select the right mount point. I have named it like my city, in mower config and here.
  - Save the config
  - Switch on "Caster Service" and "File Service", it should look like this:
    
    ![]()<img src="./RTKBase05.png" width="120">

  - Eventually change your password below these options.
  - At logs you should find at least two files:
    
    ![]()<img src="./RTKBase06.png" width="120">

### Find the position of your RTKBase
- You have to set up the logging of your position as mentioned above by activating "file service". You should wait for a day to average all the values to get a high precision position.
- After midnight you find a zip-file at logs. This you can convert to a Rinex file. To understand this file you may check [RINEX-File](http://walter.bislins.ch/bloge/index.asp?page=Understanding+GPS%2FGNSS+RINEX+Files+and+Relevant+Parameters) , but you don't need it.
- Press on the pencil right to the zip-file:

  ![]()<img src="./RTKBase07.png" width="120">

- "Create Rinex file":

    ![]()<img src="./RTKBase08.png" width="120">
- Download it when finished (may take a while, some minutes or longer)
- Go to [Calculator](https://rgp.ign.fr/SERVICES/calcul_online.php), upload your Rinex file and enter your email address. Don't forget to enter the "no robot"-verification.
  
    ![]()<img src="./ignfr.png" width="120">

- When you received the email, look at "ITRF2014" (or search for "longitude") and see your values like LONGITUDE 6.XXXXXXXXX°  LATITUDE 51.XXXXXXXXX° HELL 79.9041
  
   ![]()<img src="./averaged.png" width="120">
- You enter these values to your options at MainService. Be aware that the order of LONGITUDE and LATITUDE is switched!

   ![]()<img src="./RTKBase03.png" width="120">
- Save
- ReActivate Ntrip Service
- Finished!
  
Thanks to Stefal and all the contributors of RTKBase and the used recources.
