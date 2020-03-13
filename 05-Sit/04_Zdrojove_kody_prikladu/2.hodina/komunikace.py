from microbit import *

while True:
    if pin1.read_digital():
        display.show(Image.HAPPY)
    else:
        display.clear()
    if button_a.is_pressed():
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
    sleep(100)