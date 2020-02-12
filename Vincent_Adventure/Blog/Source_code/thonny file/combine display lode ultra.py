from machine import Pin, I2C
import ssd1306
import utime
from time import sleep
import machine
import sys
import time

trig=machine.Pin(25, machine.Pin.OUT)
echo=machine.Pin(26, machine.Pin.IN)

jaws_state="Stop" #Starting position is Stop, this will be reflected on the ESP html page

#Transducer portion

def depth(): #default is air
    t1=0
    t2=0
    trig.off() #//stop reading
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()

    while echo.value() == 0:
        pass
        t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
        t2 = utime.ticks_us()
    cm = ((t2 - t1)(340/10000))/2;

    print(cm)
    utime.sleep(2)
    return cm

cm = depth() #Run transducer once

def depthwood(): #wood depth
    t1=0
    t2=0
      #Transducer portion
    trig.off() #//stop reading
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()

    while echo.value() == 0:
        pass
        t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
        t2 = utime.ticks_us()
    cmw = ((t2 - t1)(12.25/10000))/2;
    print(cmw)
    utime.sleep(2)
    return cmw

def depthice(): #ice depth
    t1=0
    t2=0
      #Transducer portion
    trig.off() #//stop reading
    utime.sleep_us(2)
    trig.on()
    utime.sleep_us(10)
    trig.off()

    while echo.value() == 0:
        pass
        t1 = utime.ticks_us()
    while echo.value() == 1:
        pass
        t2 = utime.ticks_us()
    cmi = ((t2 - t1)*(4000/10000))/2;
    print(cmi)
    utime.sleep(2)
    return cmi

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))#SDA Yellow & SCL White; 3.3V Red & Gnd Black

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

cm = round(depth())

oled.text(' '+ str(cm), 0, 0)
oled.text('NOT SAFE', 0, 10)
oled.text('NOT SAFEree', 0, 20)
oled.text('NOT SAFEree', 0, 30)

oled.show()