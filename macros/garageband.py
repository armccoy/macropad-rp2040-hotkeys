# Garageband Control Hotkeys (MacOS)

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Garageband', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x034E59, 'Score', [Keycode.N]),
        (0x000754, 'Smart Ctl', [Keycode.B]),
        (0x4F0354, 'Roll', [Keycode.P]),
        # 2nd row ----------
        (0x04541B, '|<', [Keycode.ENTER]),
        (0x540908, 'Rec', [Keycode.R]),
        (0x544408, '>|', [Keycode.OPTION, Keycode.ENTER]),
        # 3rd row ----------
        (0x202000, '<<', [Keycode.COMMA]),
        (0x002000, 'Play/Pause', [Keycode.SPACEBAR]),
        (0x202000, '>>', [Keycode.PERIOD]),
        # 4th row ----------
        (0x200000, keyconfig.KEY_MUTE, [[ConsumerControlCode.MUTE]]),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]]),
    ]
}
