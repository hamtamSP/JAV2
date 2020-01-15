#Led Pin is at pin 2 of esp32
from machine import Pin
import time
# =====================================================================

led = Pin(2,Pin.OUT)
while True:
    led(1)
    time.sleep(0.5)
    led(0)
    time.sleep(0.5)
