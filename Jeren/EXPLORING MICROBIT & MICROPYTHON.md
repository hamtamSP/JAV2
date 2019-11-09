# EXPLORING MICROBIT & MICROPYTHON
##### Week 2
***
### Introduction
As seen form the title, we will be looking into microbit. We will be coding with micropython with Thonny 
(version 3.2.1).
***
### What is a microbit?
A microbit is "a pocket-sized computer 70 times smaller and 18 times faster than the original BBC Micro computers used in schools. It has 25 red LED lights that can flash messages and be used to create games." a short description of the microbit from the [BBC microbit website](https://support.microbit.org/support/solutions/articles/19000013983-what-is-a-micro-bit-).
Microbits can be used in gaming consoles and communication devices.
***
### Coding
The first execise we tried in class was to make a heart appear on the microbit.
This is the code I wrote:
```
from microbit import *

display.show(Image.HEART)
```
This will display a heart on the lights of the microbit.

<img src="https://github.com/hamtamSP/JAV2/blob/master/Jeren/WhatsApp%20Image%202019-11-09%20at%205.24.56%20PM.jpeg" width ="300">

Writing the first line, `from microbit import *` is very important as it allows you to get saved data from the microbit, for example, the images
