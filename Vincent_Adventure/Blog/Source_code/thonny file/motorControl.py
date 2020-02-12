from machine import Pin
import time
import machine
# =====================================================================
int1 = 4 #Brown
int2 = 0 #Red
int3 = 2  #Orange
int4 = 15  #Yellow
en1 = 17
en2 = 16
# =====================================================================
motor1a = Pin(int1,Pin.OUT)
motor1b = Pin(int2,Pin.OUT)
motor2a = Pin(int3,Pin.OUT)
motor2b = Pin(int4,Pin.OUT)
enLeft = machine.PWM(machine.Pin(en1),freq = 500,duty = 500)
enRight = machine.PWM(machine.Pin(en2),freq = 500,duty = 500)
# =====================================================================
def fwd():     
    motor1a(1)
    motor1b(0)
    motor2a(1)
    motor2b(0)
def stop():    #
    motor1a(0)
    motor1b(0)
    motor2a(0)
    motor2b(0)
def back():
    motor1a(0)
    motor1b(1)
    motor2a(0)
    motor2b(1)  
def rotationLeft():
    motor1a(1)
    motor1b(0)
    motor2a(0)
    motor2b(1)
def rotationRight():
    motor1a(0)
    motor1b(1)
    motor2a(1)
    motor2b(0)
def rest():
    stop()
    time.sleep(1)
# =====================================================================