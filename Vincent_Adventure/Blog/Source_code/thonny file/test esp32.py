from machine import Pin
import time
# =====================================================================

led = Pin(15,Pin.OUT)
while True:
    led(1)
    time.sleep(0.5)
    led(0)
    time.sleep(0.5)
    