from microbit import *

while True:
    if button_a.is_pressed():
        display.show("A")
        pin1.write_digital(1)
    else:
        pin1.write_digital(0)
    if button_b.is_pressed():
        display.show("B")
        pin2.write_digital(1)
    else:
        pin2.write_digital(0)
    display.clear()
    sleep(10)
    