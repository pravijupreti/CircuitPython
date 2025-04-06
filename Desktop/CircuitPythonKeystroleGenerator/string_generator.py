# string_generator.py

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

class StringGenerator:
    """Class to handle typing strings with the keyboard."""

    def __init__(self):
        self.kbd = Keyboard(usb_hid.devices)

    def type_string(self, string, delay=0.00001):
        """Type a given string with specified delays."""
        for char in string:
            if char.islower():  # Handle lowercase letters
                self.kbd.press(getattr(Keycode, char.upper()))
                self.kbd.release(getattr(Keycode, char.upper()))
            elif char == ' ':
                self.kbd.press(Keycode.SPACE)
                self.kbd.release(Keycode.SPACE)
            elif char.isupper():  # Handle uppercase letters
                self.kbd.press(Keycode.SHIFT)
                self.kbd.press(getattr(Keycode, char))
                self.kbd.release(getattr(Keycode, char))
                self.kbd.release(Keycode.SHIFT)
            elif char in '!@#$%^&*()_+-=[]{};:\'",.<>?/':
                self.kbd.press(getattr(Keycode, char))
                self.kbd.release(getattr(Keycode, char))

            # Delay for typing speed
            time.sleep(delay)

