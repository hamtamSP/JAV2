# Basic Motor Control
## Introduction
Now that we have successfully flashed the esp32, we will try to use the esp32 to control a tracked vehicle

### Components needed for the setup
* [Tracked Vehicle (With 12V DC motor)](https://www.aliexpress.com/item/32821691519.html?spm=a2g0o.productlist.0.0.dd9f3504FIxJlO&algo_pvid=4bd80cc2-4a6f-4e2b-9bf1-29e588a22596&algo_expid=4bd80cc2-4a6f-4e2b-9bf1-29e588a22596-40&btsid=31add63b-820d-4040-a855-48db1088dcb4&ws_ab_test=searchweb0_0,searchweb201602_2,searchweb201603_53)
* [Esp32]((https://github.com/hamtamSP/JAV2/blob/master/Vincent_Adventure/Blog/3-esp32.md)
* L298N H-bridge
* Dupont wires
* 2 (3.7V 3000mAh 18650 Lithium-ion Battery)
* Lithium Ion battery holder
* Boost Converter

### Motor control
1. Firstly, ensure that Esp32 is [flashed](https://github.com/hamtamSP/JAV2/blob/master/Vincent_Adventure/Blog/3-esp32.md).
2. Connect the circuit according to the schematic below

        (Be Careful with lithium ion batteries, use a digital multimeter to find where is the positive side and the negative side)      
3. Adjust the Boost Converter such that it outputs 12v when you measure the voltage across Vout+ and Vout-
4. Open Thonny ,Connect the ESP32 via USB Cable to your computer and open a new file
5. Upload this code, save and run
        from machine import Pin
        import time
        # =====================================================================
        int1 = 2  #Brown
        int2 = 0  #Orange
        int3 = 4  #Pink
        int4 = 16 #Purple

        enA = 15
        enB = 17
        # =====================================================================
        motor1a = Pin(int1,Pin.OUT)
        motor1b = Pin(int2,Pin.OUT)
        motor2a = Pin(int3,Pin.OUT)
        motor2b = Pin(int4,Pin.OUT)
        pulseA = Pin(enA,Pin.OUT)
        pulseB = Pin(enB,Pin.OUT)
        pulseA(1)
        pulseB(1)
        # =====================================================================
        def fwd():     
            motor1a(0)
            motor1b(1)
            motor2a(0)
            motor2b(1)
        def stop():    #
            motor1a(0)
            motor1b(0)
            motor2a(0)
            motor2b(0)
        def back():
            motor1a(1)
            motor1b(0)
            motor2a(1)
            motor2b(0)
        def rotationLeft():
            motor1a(0)
            motor1b(1)
            motor2a(1)
            motor2b(0)
        def rotationRight():
            motor1a(1)
            motor1b(0)
            motor2a(0)
            motor2b(1)
        def rest():
            stop()
            time.sleep(1)
        # =====================================================================
6. use the Repl from Thonny to run the Motors
For Example:
        fwd()
7. Change the motor output accordingly, motor1a and motor1b must be in opposite Boolean logic, motor2a and motor2b must be in opposite Boolean logic,
8. After doing adjustments, save a copy of the file into ESP32 and lable it as
        MotorControl.py
