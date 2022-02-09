# MS Teams Hotkeys (MacOS)

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'MS Teams', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Audio', [Keycode.COMMAND, Keycode.SHIFT, Keycode.M]),
        (0x000754, 'Chat', [Keycode.COMMAND, 2]),
        (0x04541B, 'Video', [Keycode.COMMAND, Keycode.SHIFT, Keycode.O]),
        # 2nd row ----------
        (0x002000, 'Share', [Keycode.COMMAND, Keycode.SHIFT, Keycode.E]),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (0x000754, 'Leave', [Keycode.COMMAND, Keycode.SHIFT, Keycode.H]),
        # 3rd row ----------
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        # 4th row ----------
        (0x200000, keyconfig.KEY_MUTE, [[ConsumerControlCode.MUTE]]),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]])
    ]
}
