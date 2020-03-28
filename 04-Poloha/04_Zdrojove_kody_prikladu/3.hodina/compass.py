from microbit import *
compass.calibrate()
while True:
    uhel = ((compass.heading()-15) // 30)
    display.show(Image.ALL_CLOCKS[uhel])