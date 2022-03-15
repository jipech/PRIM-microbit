from microbit import *

while True:
    if button_a.was_pressed():
        display.show("A")
        pin2.write_digital(1)
        sleep(500)
        pin2.write_digital(0)
    if button_b.was_pressed():
        display.show("B")
        pin2.write_digital(1)
        sleep(2000)
        pin2.write_digital(0)
    display.clear()