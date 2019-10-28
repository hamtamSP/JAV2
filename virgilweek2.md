# JAV²

Author: Virgil D'souza

## Programming a game on microbit

This week, I was tasked on creating a 'Space Invaders'
game using microbit. It was a very interesting
experience as it allowed me to discover the different
uses of microbit and Python programming.

I was able to code the game with success,
with an objective of avoiding the aliens.
Once the player hits an alien, the game is over.

### The code

from microbit import *<br>
import random

ship = 2<br>
a1 = random.randint(0, 4)<br>
a2 = 0

while True:<br>
    display.clear()<br>
    display.set_pixel(ship, 4, 5)<br>
    display.set_pixel(a1, a2, 9)

    a2 = a2 + 1
    if a2 > 4:
        a1 = random.randint(0, 4)
        a2 = 0

    if button_a.is_pressed():
        ship = ship - 1
    if button_b.is_pressed():
        ship = ship + 1

    if ship == a1 and a2 == 4:
        break

    sleep(250)

display.scroll("GAME OVER!", loop = True)

The code uses the microbit and random libraries
in micropython. According to the code,
Button A moves the ship left and Button B
moves the ship right. The randint() function
serves as a random generator for the position
of the alien.

### Problems

A problem that I encountered while coding the game
was how to prevent a program glitch when the alien
went out of range. To remedy this, I used an if
statement to reset the value of y to 0 and
added in another randint() function to regenerate
a new x value.

Another problem I encountered was how to
regenerate the alien. Using the same if
statement mentioned earlier, I called a new
randint() function to generate a new x value
and effectively, a regenerated alien.

### Pro Tip

A pro tip I would suggest is to use short sleep time
so that the ship reacts quickly to button press.

## Thonny Tutorial

https://www.youtube.com/watch?v=TK16sAk1sIk

This is a tutorial for Thonny IDE that I would
personally recommend as it covers the very basics
sufficient to get started.

It also touches on how to output values using
the text editor and shell.

## Python Programming for Beginners

https://www.youtube.com/watch?v=D48iCw3WWpI

This is a tutorial I would recommend for those
who are new to Python. It covers basic arithmetic
operations and data types. It gives tips on how
to declare variables. It also has exercises at
the end to test and refresh what you have learnt.
