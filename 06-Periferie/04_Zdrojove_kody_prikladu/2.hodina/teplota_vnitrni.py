from microbit import *

while True:
    teplota = temperature()
    display.scroll(teplota)
    sleep(10000)