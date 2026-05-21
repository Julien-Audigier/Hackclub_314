import board
import digitalio

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

key_1 = digitalio = digitalio.DigitalInOut(board.D4)
key_1.direction = digitalio.Direction.INPUT
key_1.pull = digitalio.pull.UP

key_2 = digitalio = digitalio.DigitalInOut(board.D5)
key_2.direction = digitalio.Direction.INPUT
key_2.pull = digitalio.pull.UP

key_3 = digitalio = digitalio.DigitalInOut(board.D6)
key_3.direction = digitalio.Direction.INPUT
key_3.pull = digitalio.pull.UP

key_4 = digitalio = digitalio.DigitalInOut(board.D7)
key_4.direction = digitalio.Direction.INPUT
key_4.pull = digitalio.pull.UP

import rotaryio

encoder = rotaryio.IncrementalEncoder(
    board.D10,
    board.D9
    )
last_position = None


while True
    position = encoder.position
    if last_position is None or position != last_position
        if position > last_position:
            pass #Encoder turned clockwise
        else
            pass #Encoder counter-clockwise

    if key1.value:
        keyboard_layout.write(Keycode.ALT)
    if key2.value:
        keyboard_layout.write(Keycode.SHIFT)
    if key3.value:
        keyboard_layout.write(Keycode.CONTROL)
    if key4.value:
        keyboard_layout.write(Keycode.FUNCTION)
    
    time.sleep(0.1)