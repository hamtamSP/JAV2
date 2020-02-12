from machine import I2C
i2c=I2C(1)
i2c.init(freq=1000000)
oled = SSD1306_I2C(128, 64, i2c)
console = FBConsole(oled)
os.dupterm(console)