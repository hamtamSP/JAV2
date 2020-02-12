from hcsr04 import HCSR04
import time

while True:
    sensor = HCSR04(trigger_pin=18, echo_pin=19)
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    
    time.sleep(0.2)
