from machine import Pin, I2C
import ssd1306
from time import sleep

# ESP32 Pin assignment 


i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
def reset():
    oled.fill(0)

def display_(line):
    reset()
    #         text     null,line
    oled.text(''+line[0], 0, 0)
    oled.text(''+line[1], 0, 10)
    oled.text(''+line[2], 0, 20)
    
    oled.show()
    