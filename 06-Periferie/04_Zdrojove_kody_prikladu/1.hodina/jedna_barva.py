from microbit import *
while True:
    for I in range(0, 1024):
        pin0.write_analog(I)
        sleep(2)
    sleep(1000)
    for I in range(1023, 0, -1):
        pin0.write_analog(I)
        sleep(2)
