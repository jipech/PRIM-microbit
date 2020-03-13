from microbit import *

compass.calibrate()

while True:
    x = (375-compass.heading())//30
    if (x == 12):
        x = 0
    display.show(Image.ALL_CLOCKS[x])