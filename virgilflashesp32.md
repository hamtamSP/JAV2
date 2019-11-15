# Introduction to ESP32

Author: Virgil D'souza

## Introduction

The ESP32 is a type of microcontroller
capable of operating in industrial
environments. It can operate at temperatures
ranging from -40&deg;C to 125&deg;C. It does
not require much power to function, making
it popular in applications for mobile
devices and IoT. The ESP32 is also capable of
WiFi and Bluetooth applications.

## Setting up the ESP32

The ESP32 is able to be programmed using Micropython provided
it is correctly configured. This section provides the essential
steps to wipe and flash the ESP32 with Micropython.

### Step 1: Installing python on Windows

To begin the flashing of the ESP32, python MUST be installed
onto the computer. Download from [here](python.org/downloads).
Ensure that you download the version that matches the operating
systems of the computer.

Once downloaded, start the install process. Follow the instructions
on the install wizard.

NOTE:
<br>Checkbox for creating a path should be checked.

### Step 2: Installing Binary File

Download the binary file for micropython from the
[Micropython downloads page](https://micropython.org/download#esp32).
Ensure that the file you download matches your operating system.
It is recommended that you choose the 'Generic' option.

Recommended: esp32-idf3-20191115-v1.11-580-g973f68780.bin

### Step 3: Installing ESPTool

Connect the ESP32 to the computer using micro-USB cable.

Run the command prompt and type in "pip install esptool".

The output on the command prompt should look like this:
C:\Users\dsouz>pip install esptool
Collecting esptool
  Downloading https://files.pythonhosted.org/packages/68/91/08c182f66fa3f12a96e754ae8ec7762abb2d778429834638f5746f81977a/esptool-2.8.tar.gz (84kB)
     |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 92kB 590kB/s
Collecting pyserial>=3.0 (from esptool)
  Downloading https://files.pythonhosted.org/packages/0d/e4/2a744dd9e3be04a0c0907414e2a01a7c88bb3915cbe3c8cc06e209f59c30/pyserial-3.4-py2.py3-none-any.whl (193kB)
     |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 194kB 1.3MB/s
Collecting pyaes (from esptool)
  Downloading https://files.pythonhosted.org/packages/44/66/2c17bae31c906613795711fc78045c285048168919ace2220daa372c7d72/pyaes-1.6.1.tar.gz
Collecting ecdsa (from esptool)
  Downloading https://files.pythonhosted.org/packages/a2/25/3bb32da623b39a27a07d194cd58e4540224421d924661de2e694304ae4fa/ecdsa-0.14.1-py2.py3-none-any.whl (79kB)
     |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 81kB 880kB/s
Collecting six (from ecdsa->esptool)
  Downloading https://files.pythonhosted.org/packages/65/26/32b8464df2a97e6dd1b656ed26b2c194606c16fe163c695a992b36c11cdf/six-1.13.0-py2.py3-none-any.whl
Installing collected packages: pyserial, pyaes, six, ecdsa, esptool
  Running setup.py install for pyaes ... done
  Running setup.py install for esptool ... done
Successfully installed ecdsa-0.14.1 esptool-2.8 pyaes-1.6.1 pyserial-3.4 six-1.13.0
WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

### Step 4: Flashing micropython to ESP32

Next, type in "esptool.py --port /dev/ttyUSB0 erase_flash"

NOTE: <br>
Replace "/dev/ttyUSB0" with your computer's communication port (COMX).

The output should look like this:

C:\Users\dsouz>esptool.py --chip esp32 --port COM6 erase_flash
esptool.py v2.8
Serial port COM6
Connecting.....
Chip is ESP32D0WDQ5 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 4c:11:ae:71:14:08
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 9.6s
Hard resetting via RTS pin...

Next, type in "esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin",
again replacing "/dev/ttyUSB0" with the COM port on your computer. To avoid
any typo, drag the file into the command prompt. The file name will
appear.

The output should look something like this:

C:\Users\dsouz>esptool.py --chip esp32 --port COM6 --baud 460800 write_flash -z 0x1000 C:\Users\dsouz\Downloads\esp32-idf3-20191113-v1.11-576-gd667bc642.bin
esptool.py v2.8
Serial port COM6
Connecting.....
Chip is ESP32D0WDQ5 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: 4c:11:ae:71:14:08
Uploading stub...
Running stub...
Stub running...
Changing baud rate to 460800
Changed.
Configuring flash size...
Auto-detected Flash size: 4MB
Compressed 1240160 bytes to 783158...
Wrote 1240160 bytes (783158 compressed) at 0x00001000 in 18.9 seconds (effective 524.5 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...

### Step 5: Launching Thonny

Launch Thonny, go to Run > select interpreter and select Micropython(generic).
Select the COM port according to your computer.

Once the options are selected, you should be able to see a
message that the ESP32 has been detected.
