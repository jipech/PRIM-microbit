from microbit import *
import radio
radio.on()
radio.config(channel=23)
while True:
    zprava = radio.receive()
    if (zprava):
        display.scroll(zprava)
        zprava = ""
radio.off()