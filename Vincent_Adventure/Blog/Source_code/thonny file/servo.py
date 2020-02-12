import machine

servo = machine.PWM(machine.Pin(18), freq=1000)
servo.duty(00)