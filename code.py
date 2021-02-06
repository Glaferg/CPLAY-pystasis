"""CircuitPython Essentials Internal RGB LED rainbow example"""
import time
import board

import neopixel

from digitalio import DigitalInOut, Direction, Pull

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

switch = DigitalInOut(board.D7)  # For Circuit Playground Express
switch.direction = Direction.INPUT
switch.pull = Pull.UP

def colorwheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return 0, 0, 0
    if pos < 85:
        return int(255 - pos * 3), int(pos * 3), 0
    if pos < 170:
        pos -= 85
        return 0, int(255 - pos * 3), int(pos * 3)
    pos -= 170
    return int(pos * 3), 0, int(255 - (pos * 3))


led.brightness = 0.05

i = 0
while True:
    if switch.value:
        ticker = 10
    else:
        pass

    if ticker != 0:
        i = (i + 1) % 256  # run from 0 to 255
        led.fill(colorwheel(i))
        time.sleep(0.01)