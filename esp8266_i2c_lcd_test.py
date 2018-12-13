"""Implements a HD44780 character LCD connected via PCF8574 on I2C.
   This was tested with: https://www.wemos.cc/product/d1-mini.html"""

from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
sda = Pin(14)
scl = Pin(12)

def test_main():
    """Test function for verifying basic functionality."""
    print("Running test_main")
    i2c = I2C(scl=scl, sda=sda, freq=400000)
    scan = i2c.scan()
    addr = scan[0]
    lcd = I2cLcd(i2c, addr, 2, 16)
    lcd.putstr("It Works!\nSecond Line")
#if __name__ == "__main__":
test_main()
