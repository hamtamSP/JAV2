# Servo control

### Introduction
there are existing codes written in Micropython to control servo motors. However, they did not work so I will be controlling the servo motor from scratch.

### How the Servo works

!(How the Servo works)[https://github.com/hamtamSP/JAV2/blob/master/Vincent_Adventure/Blog/pic/website/Servo%20Control/Servo%20Control%20works.png]

Servo Motor are controlled using pulse where we have adjust the pulse in such that the servomotor will rotation in the direction that we want. I will being using the standard pwm code to control a continuous servo motor the       

      frequency = 1000 = min_pulse (Anti-Clockwise)
      frequency = 500 = max_pulse (Clockwise)

In micropython, to control pwm, we need to state the frequency and the duty for the pwm to work correctly. For more info, please refer to (this Documentation)[https://docs.micropython.org/en/latest/esp8266/tutorial/pwm.html].


### My code to control the my servoMotor
I am using a(continuous servo motor(MG90S) for my project to rotate the worm gear that my team mate designed for our seed dispenser. The servo will required to rotate anti-clockwise to dispense the seeds out.


My servo will be connect to:

        3.3v     red
        Ground   Black
        Pin 5    Orange
My code

        import machine
        import time
        while True:
        servo = machine.PWM(machine.Pin(5), freq=1000)
        servo.duty(200)
        time.sleep(0.55*7)
