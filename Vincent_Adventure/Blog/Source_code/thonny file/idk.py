from machine import Pin
import utime,machine,time

trigPin = 16
echoPin = 0

trig = Pin(trigPin,Pin.OUT)
echo = Pin(echoPin,Pin.IN)

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
    cm = ((t2 - t1)*(340/10000))/2;


    print(cm)
    utime.sleep(2)
    return cm

while True:
    distance = depth()
    print(distance)
    time.sleep(0.1)
    
    