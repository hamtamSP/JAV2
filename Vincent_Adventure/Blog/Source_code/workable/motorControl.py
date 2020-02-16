from machine import Pin
import time
# =====================================================================
int1 = 2 #Brown
int2 = 0 #Red
int3 = 4  #Orange
int4 = 16  #Yellow

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