from microbit import *
import random


stone = Image("00000:"
              "00000:"
              "09990:"
              "09990:"
              "09990")

paper = Image("90990:"
              "90999:"
              "99999:"
              "99999:"
              "00000")

scissors = Image("90900:"
                 "99000:"
                 "99990:"
                 "99990:"
                 "00000")

game = [stone, paper, scissors]

random.seed()

while True:
    if accelerometer.was_gesture("shake"):
        obj = random.choice(game)
        display.show(obj)
        sleep(3000)
        
        