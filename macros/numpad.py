# Universal Numpad

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Numpad', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004166, '7', ['7']),
        (0x004166, '8', ['8']),
        (0x004166, '9', ['9']),
        # 2nd row ----------
        (0x004166, '4', ['4']),
        (0x004166, '5', ['5']),
        (0x004166, '6', ['6']),
        # 3rd row ----------
        (0x004166, '1', ['1']),
        (0x004166, '2', ['2']),
        (0x004166, '3', ['3']),
        # 4th row ----------
        (0x004166, '0', ['0']),
        (0x640A66, '.', ['.']),
        (0x002000, 'ENTER', [Keycode.ENTER]),
    ]
}
