from microbit import *
compass.calibrate()
while True:
       display.scroll(compass.heading())
       sleep(1000)