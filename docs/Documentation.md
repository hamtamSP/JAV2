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
- [Software](#software)

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
- 2 x 2.2MΩ Resistore

To Program the ESP32, You will also need the following Software
- [Python](https://www.python.org/downloads/)
- [ESPTool](https://github.com/espressif/esptool)
- [Thonny](https://thonny.org/)

## Electrical Components

### Charging Circuit

The TP4056 Charging Module is a Single Cell Charging Board. Hence, in order to charge two batteries at the same time, we will connect the 2 TP4056 Modules in Parallel. This allows us to take advantage of the protection features of the board as well as the capacity of the 2 batteries. The outputs of each TP4056 Module is then connected to a 1n4001 Diode to prevent reverse current due to differences in voltages from the 2 modules. The 2 Diodes are then connect to a DPDT Switch actings as a ON/OFF Switch for the Tree Planting Vehicle and the 2 connections are conbimed later. This can be shown in the schematics provided below.

![Charging Circuit](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Charging%20Circuit.png)

### Boost Circuit

By connecting the output from the charging circuit to the input of the Boost Converter, we Can boost the voltage coming from the TP4056 to 11V for the L298N H-Bridge which is connected to the Output of the Boost Converter. The 5V Rail of the L298N can then be used to supply power to the ESP32 and the other pheripherials. This can be shown in the Schematics provided below.

![Boost Circuit with ESP32](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Boost%20Circuit%20with%20ESP32.png)

However, the above circuit can only supply 500mA through the 5V rail due to the L298N H-Bridge. Hence, the L298N H-Bridge will only be used to provide power to the motors and a sperate circuit will be used to supply power to the ESP32 and the other pheripherials. This can be shown in the Schematics provided below.

![Boost Circuit](https://raw.githubusercontent.com/hamtamSP/JAV2/master/img/Boost%20Circuit.png)

## Software
