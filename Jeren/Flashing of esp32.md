# Flashing of esp32
---
References
https://learn.sparkfun.com/tutorials/how-to-load-micropython-on-a-microcontroller-board/esp32-thing
***
What you need:
* Python 2.7 or Python 3.4 or newer
* esp32
---
## Steps:
#### 1) Install esptool
open command prompt and input this command
`pip install esptool`

### 2) Erase everything on the chip's flash memory
input this command:
`esptool.exe --chip esp32 -p <USB to serial port> erase_flash`
<USB to serial port> is got from device manager

### 3) Install firmware from https://micropython.org/download#esp32
There are 2 types of firmware for us to choose from
* Firmware built with ESP-IDF v3.x, with support for LAN and PPP but no bluetooth
* Firmware built with ESP-IDF v4.x, with support for bluetooth but no LAN or PPP

Recommended firmware: esp32-idf3-20191106-v1.11-558-gd209f9ebe.bin
This recommended firmware comes from the first catergory.
   
### 4) Flash the firmware with this command:
`esptool.exe --chip esp32 -p <USB-to-Serial Port> write_flash -z 0x1000 <path to .bin>`
<path to .bin> is the path to the location of the .bin file

##### With these steps, the Micropython firmware is now installed onto the esp32.
***
## Problems faced:
The main problem I faced was that I did not install python correctly and was struggling to get the code to work as there was a prompt that there was a syntax error. This happened because I did not check 'Add Python 3.8 to PATH'.
Another problem was that the reference website showed to use the command `esptool.py`, it did not work for me, which was very troubling. But this was solved as we noticed that the command was 'downloaded' as `esptool.exe`.
