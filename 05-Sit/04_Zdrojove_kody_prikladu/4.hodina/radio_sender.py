# Write your code here :-)
from microbit import *
import radio
radio.on()
radio.config(channel=23)
while True:
    if button_a.is_pressed():
        radio.send("Blah blah")
    sleep(1000)
radio.off()

    