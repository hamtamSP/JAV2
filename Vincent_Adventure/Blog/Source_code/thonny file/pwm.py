import machine
import time

# =====================================================================
int1 = 4 #Brown
int2 = 0 #Red
int3 = 2  #Orange
int4 = 15  #Yellow
# =====================================================================
speedPercentage = 50 #1(min)-100(max)
spd = round((speedPercentage/100.0) * 1023)
# =====================================================================

motor1a = machine.PWM(machine.Pin(int1), duty=spd)
motor1b = machine.PWM(machine.Pin(int2), duty=spd)
motor2a = machine.PWM(machine.Pin(int3), duty=spd)
motor2b = machine.PWM(machine.Pin(int4), duty=spd)

# =====================================================================

off1a = machine.PWM(machine.Pin(int1), freq=0)
off1b = machine.PWM(machine.Pin(int2), freq=0)
off2a = machine.PWM(machine.Pin(int3), freq=0)
off2b = machine.PWM(machine.Pin(int4), freq=0)

# =====================================================================
def fwd():     
    motor1a
    off1b
    motor2a
    off2b
def stop():    
    off1a
    off1b
    off2a
    off2b
def back():
    off1a
    motor1b
    off2a
    motor2b
def rotationLeft():
    motor1a
    off1b
    off2a
    motor2b
def rotationRight():
    off1a
    motor1b
    motor2a
    off2b
def rest():
    stop()
    time.sleep(1)
# =====================================================================