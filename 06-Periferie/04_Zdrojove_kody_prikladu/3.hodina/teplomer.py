from microbit import *
while True:
    hodnota = pin0.read_analog()
    napeti = hodnota * (3170 / 1024)
    teplota = (napeti - 500) / 10
    display.scroll(round(teplota, 1))
    sleep(10000)