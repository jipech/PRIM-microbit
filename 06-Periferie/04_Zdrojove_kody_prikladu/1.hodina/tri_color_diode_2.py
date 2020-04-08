from microbit import *
A = [pin0, pin1, pin2]
for I in A:
    I.write_digital(1)
    sleep(2000)
    I.write_digital(0)