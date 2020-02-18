---
title: Documentation
subtitle: Documentation Page for JAV²
layout: page
show_sidebar: false
menubar: documentation
hide_footer: true
---
[![GitHub Update](https://img.shields.io/badge/Last_Updated-19_Feb_2020-blue)](https://github.com/hamtamSP/JAV2)

## Table of Contents

- [Getting Started](#getting-started)
- [Electrical Components](#electrical-components)
  - [Charging Circuit](#charging-circuit)
  - [Boost Ciruit](#boost-circuit)
  - [Battery Monitor](#battery-monitor)
- [Software](#software)
  - [Installation of Software](#installation-of-software)
  - [ESP32 Setup](esp32-setup)

## Getting Started

Below are the Components That are Used

- ESP32
- HC-SR04 Ultrasonic Sensor
- L298N H-Bridge
- 2 x TP4056 Charging Module
- 2 x 18650 Battery
- 2 x 1n4001 Diode
- DPDT Switch
- 2 x Boost Converter
- SG90 Servo
- 2 x Motors
- I2C OLED Display
- 2 x 3.9MΩ Resistors
- 2 x 2.2MΩ Resistors

To Program the ESP32, You will also need the following Software
- [Python](https://www.python.org/downloads/)
- [ESPTool](https://github.com/espressif/esptool)
- [Thonny](https://thonny.org/)
- [MicroPython](https://micropython.org/download)

## Electrical Components

### Charging Circuit

The TP4056 Charging Module is a Single Cell Charging Board. Hence, in order to charge two batteries at the same time, we will connect the 2 TP4056 Modules in Parallel. This allows us to take advantage of the protection features of the board as well as the capacity of the 2 batteries. The outputs of each TP4056 Module is then connected to a 1n4001 Diode to prevent reverse current due to differences in voltages from the 2 modules. The 2 Diodes are then connect to a DPDT Switch actings as a ON/OFF Switch for the Tree Planting Vehicle and the 2 connections are conbimed later. This can be shown in the schematics provided below.

![Charging Circuit](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Charging%20Circuit.png)

### Boost Circuit

By connecting the output from the charging circuit to the input of the Boost Converter, we Can boost the voltage coming from the TP4056 to 11V for the L298N H-Bridge which is connected to the Output of the Boost Converter. The 5V Rail of the L298N can then be used to supply power to the ESP32 and the other pheripherials. This can be shown in the Schematics provided below.

![Boost Circuit with ESP32](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Boost%20Circuit%20with%20ESP32.png)

However, the above circuit can only supply 500mA through the 5V rail due to the L298N H-Bridge. Hence, the L298N H-Bridge will only be used to provide power to the motors and a sperate circuit will be used to supply power to the ESP32 and the other pheripherials. This can be shown in the Schematics provided below.

![Boost Circuit](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Boost%20Circuit.png)

### Battery Monitor

To relay the battery voltage to the ESP32 so that we will have the battery capacity, we would create a voltage divider as the ESP32 can only read up to 3.3V. Hence, we used 2 x 3.9MΩ Resistors and 2 x 2.2MΩ Resistors to create a voltage divider as shown in the schematics below.

![Battery Monitor](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Battery%20Voltage.png)

## Software

### Installation of Software

To Download Python, Head to [https://www.python.org/downloads/](https://www.python.org/downloads/) and download the latest release of python. When prompted check "include PATH". After Python has been installed, Open command Prompt and enter:

``` pip install esptool ```

The install process will run and a message will show when the install is completed. (Message may differ depending on the version)

``` Successfully installed ecdsa-0.13.3 esptool-2.8 pyaes-1.6.1 pyserial-3.4 ```

Now you can also download and install the latest version of Thonny at [https://thonny.org/](https://thonny.org/).
You can also download the relevant version of MicroPython at [https://micropython.org/download](https://micropython.org/download)

### ESP32 Setup

The ESP32 is usually preinstalled with Lua and NodeMCU. But since we are using MicroPython, we will need to erase the flash. we can do this by using the following command on Command Prompt:

``` esptool.py --chip esp32 -p COM3 erase_flash ```

Note that `COM3` is the corresponding port connected to the ESP32. However if you recieved an error message like: `'esptool.py' is not recognized as an internal or external command, operable program or batch file.` use the folling command instead:

``` esptool.exe --chip esp32 -p COM3 erase_flash ```

To install MicroPython, Use the following command:

``` esptool.exe --chip esp32 -p COM3 write_flash -z 0x1000 esp32-idf3-20191106-v1.11-558-gd209f9ebe.bin ```

Note that `esp32-idf3-20191106-v1.11-558-gd209f9ebe.bin` is the MicroPython file where you just downloaded and `COM3` is the corresponding port connected to the ESP32.
Now you are all set to program the ESP32 with Thonny!
