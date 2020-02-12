from microbit import *

while True:
    if (button_a.is_pressed() and button_b.is_pressed()):
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.HEART_SMALL)
        sleep(100)
    elif button_a.is_pressed():
        display.show(Image.SAD)
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
    else:
        display.show(Image.HAPPY)