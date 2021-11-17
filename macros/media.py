# Media Control Hotkeys (MacOS)

from adafruit_hid.consumer_control_code import ConsumerControlCode
import keyconfig

app = {
    'name' : 'Media', # Application name
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, keyconfig.KEY_BLANK, []),
        (0x000000, keyconfig.KEY_BLANK, []),
        (0x000000, keyconfig.KEY_BLANK, []),
        # 2nd row ----------
        (0x000000, keyconfig.KEY_BLANK, []),
        (0x000000, keyconfig.KEY_BLANK, []),
        (0x000000, keyconfig.KEY_BLANK, []),
        # 3rd row ----------
        (0x200000, keyconfig.KEY_MUTE, [[ConsumerControlCode.MUTE]]),
        (0x080F54, keyconfig.KEY_VOL_DOWN, [[ConsumerControlCode.VOLUME_DECREMENT]]),
        (0x080F54, keyconfig.KEY_VOL_UP, [[ConsumerControlCode.VOLUME_INCREMENT]]),
        # 4th row ----------
        (0x202000, '<<', [[ConsumerControlCode.SCAN_PREVIOUS_TRACK]]),
        (0x002000, 'Play/Pause', [[ConsumerControlCode.PLAY_PAUSE]]),
        (0x202000, '>>', [[ConsumerControlCode.SCAN_NEXT_TRACK]]),
    ]
}
