# Macros

A macro file contains a group of keybindings that can represent an app keyboard shortcuts, related functions, or any other keyboard-based functionality. Each macro file should contain the following:

- `name` - The title of the group of keybindings. This is displayed at the top of the OLED screen for each macro.
- `macros` - An array of keybinding definitions. There are twelve possible keybindings, grouped in rows of three to represent the twelve keys on the Macropad.

There are a few global key labels and other constants defined in [keyconfig.py](../keyconfig.py). These include:

- `KEY_BLANK` - Defines a visual placeholder for keys that do not have assigned keybindings.
- `LED_BLANK` - Defines the LED color for blank keys
- `LED_PRESS` - Defines the LED color displayed under a key when it is pressed.

The keycodes used in keybindings are defined in the [Python source bundle](https://circuitpython.org/libraries) in the file `/adafruit_hid/keycode.py`. Some examples are:

- `Keycode.CONTROL`
- `Keycode.ALT`
- `Keycode.[A-Z]`

A key combo is defined by a comma-separated list. For example, **Ctrl + Shift + V** would be defined as follows:

`Keycode.CONTROL, Keycode.SHIFT, Keycode.V`

See other macro files for more examples of use and context.