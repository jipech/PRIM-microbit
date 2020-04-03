# Write your code here :-)
from microbit import *
import radio
radio.on()
radio.config(channel=23)
while True:
    if button_a.was_pressed():
        radio.send("Ahoj svete")
    sleep(1000)
radio.off()

    