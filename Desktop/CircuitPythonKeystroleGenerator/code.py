# code.py
import time
import sys
import os
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from string_generator import StringGenerator  # Import the StringGenerator class

# Print the version of CircuitPython
print("CircuitPython version:", sys.version)

# Optionally, if you want to indicate that you're on a Pico W
print("Running on board:", sys.platform)

kbd = Keyboard(usb_hid.devices)

# Delay to give time to open an editor or terminal
time.sleep(0.000003)

# Open the Run dialog (Windows Key + R)
kbd.press(Keycode.WINDOWS)
kbd.press(Keycode.R)
kbd.release_all()  # Release all keys
time.sleep(0.5)  # Allow cmd
#cmd time for the Run dialog to appear

# Create an instance of StringGenerator
string_gen = StringGenerator()

# Type 'notepad' using the StringGenerator class
string_gen.type_string("notepad", delay=0.00001)  # Tweak delay if needed

# Send Enter (Main Enter key)
kbd.press(Keycode.ENTER)
kbd.release(Keycode.ENTER)
time.sleep(1)  # Allow time for Notepad to open

string_gen.type_string("Sambrid lamo mugi", delay=0.1) 


# Type a message in Notepad
  