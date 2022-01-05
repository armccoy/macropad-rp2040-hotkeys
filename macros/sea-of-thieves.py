# Sea of Thieves - A pirates best friend

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Sea of Thieves', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x6c9ea3, 'Comp', ['7']),
        (0x6c9ea3, 'Inst', ['I']),
        (0x6c9ea3, 'Lant', ['L']),
        # 2nd row ----------
        (0x00b4b4, 'Ball', ['4']),
        (0x00b4b4, 'PTT', ['j']),
        (0x00b4b4, 'Shov', ['6']),
        # 3rd row ----------
        (0xe38839, 'Gun', ['1']),
        (0xe38839, 'Sword', ['2']),
        (0xe38839, 'Food', ['3']),
        # 4th row ----------
        (0x4e1a23, 'Buck', ['B']),
        (0x4e1a23, 'Plank', ['5']),
        (0x4e1a23, 'Open', [Keycode.CONTROL, Keycode.SHIFT, 'P']),
    ]
}