# Discord

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Discord', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x748cdc, 'Mut', [Keycode.CONTROL, Keycode.OPTION, Keycode.M]),
        (0x748cdc, 'Reply', ['r']),
        (0x748cdc, 'SS', [Keycode.CONTROL, Keycode.SHIFT, Keycode.V]),
        # 2nd row ----------
        (0x748cdc, 'VAD', [Keycode.CONTROL, Keycode.SHIFT, Keycode.Q]),
        (0x748cdc, 'Upld', [Keycode.CONTROL, Keycode.SHIFT, 'm']),
        (0x748cdc, 'PTT', ['d']),
        # 3rd row ----------
        (0x748cdc, 'Def', [Keycode.CONTROL, Keycode.SHIFT, 'd']),
        (0x748cdc, 'Acc', [Keycode.CONTROL, Keycode.ENTER]),
        (0x748cdc, 'Dec', [Keycode.ESCAPE]),
        # 4th row ----------
        (0x748cdc, 'Emoji', [Keycode.CONTROL, 'e']),
        (0x748cdc, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x800f00, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
}
