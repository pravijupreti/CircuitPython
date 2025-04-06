from adafruit_hid.keycode import Keycode

class KeyCodeMapper:
    def __init__(self):
        self.char_to_keycode = {
            'a': Keycode.A,
            'b': Keycode.B,
            'c': Keycode.C,
            'd': Keycode.D,
            'e': Keycode.E,
            'f': Keycode.F,
            'g': Keycode.G,
            'h': Keycode.H,
            'i': Keycode.I,
            'j': Keycode.J,
            'k': Keycode.K,
            'l': Keycode.L,
            'm': Keycode.M,
            'n': Keycode.N,
            'o': Keycode.O,
            'p': Keycode.P,
            'q': Keycode.Q,
            'r': Keycode.R,
            's': Keycode.S,
            't': Keycode.T,
            'u': Keycode.U,
            'v': Keycode.V,
            'w': Keycode.W,
            'x': Keycode.X,
            'y': Keycode.Y,
            'z': Keycode.Z,
            ' ': Keycode.SPACE,
            '\n': Keycode.ENTER,
            'win':Keycode.WINDOWS
        }

    def get_keycode(self, char):
        """Returns the keycode for the given character, or None if unsupported."""
        return self.char_to_keycode.get(char.lower())

    def is_supported(self, char):
        """Check if the character has a defined keycode."""
        return char.lower() in self.char_to_keycode
