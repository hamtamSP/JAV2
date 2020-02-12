from microbit import *
import random

scissors = Image("90090:"
                 "90900:"
                 "99900:"
                 "99990:"
                 "99990")

paper = Image("09990:"
              "09990:"
              "09990:"
              "09990:"
              "09990")

stone = Image("00000:"
              "00000:"
              "09990:"
              "09990:"
              "09990")

game=[stone, paper, scissors]

random.seed()
#Main Loop
while True:
    display.clear()
    if accelerometer.was_gesture("shake"):
        obj = random.choice(game)
        display.show(obj)
        sleep(3000)
    else:
        display.show(Image.HAPPY)

