# EXPLORING MICROBIT & MICROPYTHON
##### Week 2
***
## Introduction
As seen form the title, we will be looking into microbit.
***
## What is a microbit?
A microbit is "a pocket-sized computer 70 times smaller and 18 times faster than the original BBC Micro computers used in schools. It has 25 red LED lights that can flash messages and be used to create games.", a short description of the microbit from the [BBC microbit website](https://support.microbit.org/support/solutions/articles/19000013983-what-is-a-micro-bit-).
Microbits can be used in gaming consoles and communication devices.
***
## Coding
##### What I used for these exercises:
* Microbit
* Thonny app (version 3.2.1) , to code the microbit using micropython
##### Code 1
The first execise we tried in class was to make a heart appear on the microbit.
This is the code I wrote:
```
from microbit import *

display.show(Image.HEART)
```
This will display a heart on the lights of the microbit.

<img src="https://github.com/hamtamSP/JAV2/blob/master/Jeren/WhatsApp%20Image%202019-11-09%20at%205.24.56%20PM.jpeg" width ="300">

What i learnt for this exercise:
* Writing the first line, `from microbit import *` is very important as it allows you to get saved data from the microbit, for example, the heart image.
* When writing the second line `display.show(Image.HEART)`, the word 'HEART' has to be capitalised, otherwise the word will not be recognised

##### Code 2
This second exercise was to learn about displaying messages.
This is the code i wrote:
```
from microbit import *

while True:
    display.scroll("Hello World")
```
The outcome was that the message in the quotes will scroll across the microbit LEDs, as seen below.

![Alt Text](https://media.giphy.com/media/elDFvIPaydy3pKCcGt/giphy.gif)

What I learnt from this exercise:
* Learnt the scroll function
* Using `while True:` gives you a loop that makes the message countiuously scoll across the LED

##### Code 3
The third exercise is to learn how to create our own personalized images with the LEDs. We were first tasked to design a boat.
This is the code i wrote:
```
from microbit import *

while True:
    boat = Image("00500:"
                  "00550:"
                  "00500:"
                  "55555:"
                  "05550")
    display.show(boat)
```
The numbers in the quotations represents the LEDs on the microbit in a 5x5, where '0' is off and any nuber from 1-9 is on, where 1 is the dimmest and 9 is the brightest. When the code is uploaded, the microbit will display a the image you create, a boat in this context.

<img src="https://github.com/hamtamSP/JAV2/blob/master/Jeren/boat_microbit.jpeg" width ="300">

The second part of this exercise was to make the boat look animated, floating up and down.
This is the code I wrote:
```
from microbit import *

while True:
    boat1 = Image("00500:"
                  "00550:"
                  "00500:"
                  "55555:"
                  "05550")
    display.show(boat1)
    sleep(1000)
    
    boat2 = Image("00000:"
                  "00500:"
                  "00550:"
                  "00500:"
                  "55555")
    display.show(boat2)
    sleep(1000)
```

What I learnt from this exercise:
* By using `sleep()`, we are able to make a delay so that the image on the LED does not change immediately.

##### Code 4
The forth code was to learn how to programme the 2 buttons on the microbit to change the LEDs.
Our task:
* Happy face shown when no buttons are pressed
* Sad face shown when Button A pressed
* Angry face shown when button B pressed

This is my code:
```
from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.SAD)
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
    else: display.show(Image.HAPPY)
```
This is how it turned out:

![Alt Text](https://media.giphy.com/media/RfAT0z5LG7mCSo7tOV/giphy.gif)

What i learnt from this exercise:
* The image you want to display when no buttons are pressed has to be at the back, because of priority, otherwise the microbit will flash both images at the same time
* Since i used C++ first, I was used to its functions, so when i wrote `else if`, it did not work for me and was confused. When I googled, I found out that `elif` had to be used
* For the `else:` function, you have to make sure to include the ':', otherwise it will not be recognised

Next, we had to make it so that when both buttons were pressed at the same time, something else would be displayed.
This is my code:
```
from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.HEART)
    elif button_a.is_pressed():
        display.show(Image.SAD)
    elif button_b.is_pressed():
        display.show(Image.ANGRY)
    else: display.show(Image.HAPPY)
```
What I learnt from this exercise:
* For the priority, the line for when both buttons were pressed was put on to so that it would prioritize that line first, otherwise it will not appear at all

##### Code 5
For this exercise, we were tasked to make the microbit display different images when different actions were done to the microbit. This exercise makes use of the microbit's motion sensors (accelerometer & compass).
These are the gestures (and codes) the microbit is able to recognise:
* up
* down
* left
* right
* face up
* face down
* freefall
* 3g
* 6g
* 8g
* shake

This is the code I wrote:
```
from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "face up":
        display.show(Image.HAPPY)
    elif gesture == "face down":
        display.show(Image.ANGRY)
    elif gesture == "left":
        display.show(Image.HEART)
    else: display.show(Image.SURPRISED)
```
