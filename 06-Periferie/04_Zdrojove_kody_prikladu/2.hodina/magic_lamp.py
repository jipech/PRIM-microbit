from microbit import *
import random
A = [pin0, pin1, pin2]
last = 2
while True:    
    barva = random.randint(0, 2)
    while (barva == last):
        barva = random.randint(0, 2)
    delka = random.randint(1000, 5000)
    for I in range(0, 1024):
        A[barva].write_analog(I)
        A[last].write_analog(1023-I)
        sleep(2)
    sleep(delka)
    last = barva