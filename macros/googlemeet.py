# Zoom Hotkeys (MacOS)

from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Google Meet', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x540908, 'Mic', [Keycode.COMMAND, Keycode.D]),
        (keyconfig.LED_BLANK, keyconfig.KEY_BLANK, []),
        (0x04541B, 'Video', [Keycode.COMMAND, Keycode.E]),
        # 2nd row ----------
        (0x000754, 'People', [Keycode.CONTROL, Keycode.COMMAND, Keycode.P]),
        (0x000754, 'Chat', [Keycode.CONTROL, Keycode.COMMAND, Keycode.C]),
        (0x000754, 'Leave', [Keycode.COMMAND, Keycode.W]),
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
