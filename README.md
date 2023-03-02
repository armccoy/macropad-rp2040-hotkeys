# Macropad RP2040 Hotkeys

A growing collection of [CircuitPython](https://circuitpython.org/board/adafruit_macropad_rp2040/)-based hotkey macros for the [Adafruit Macropad RP2040](https://learn.adafruit.com/adafruit-macropad-rp2040).

Currently, the following macro sets are included:

- `discord.py` - Discord (Win)
- `garageband.py` - Garageband (MacOS)
- `googlemeet.py` - Google Meet (MacOS)
- `media.py` - Media Control Hotkeys (MacOS)
- `numpad.py` - Universal numpad
- `sea-of-thieves` - [Sea of Thieves](https://www.seaofthieves.com/) (Win)
- `teams.py` - MS Teams (MacOS)
- `webex.py` - Webex (MacOS)
- `zoom.py` - Zoom (MacOS)

## Configuration

The `macros/` directory contains the collection of macros, each set in its own file with the `.py` extension. Each set contains the following:

- The name of the application that the macro targets
- List of macros, sorted by row

Any new macros added to the `macros/` directory will be scanned and included when the device boots. Also note that macros are loaded in alphanumerical order, so prepending each macro's filename with a numeral (e.g. `1_`, `2_`, etc.) is a handy way to bring your favorite macros to the top.

The `lib/` directory contains the necessary Adafruit Macropad libraries. See the README in the `lib/` directory in this project for more information.

## Installing

First make sure that your Macropad has the [latest version of CircuitPython installed](https://circuitpython.org/board/adafruit_macropad_rp2040/). See [https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython](https://learn.adafruit.com/adafruit-macropad-rp2040/circuitpython) for instructions on how to update the Macropad to have the latest version of CircuitPython.

The project files can then be uploaded to the root directory of the device.

## Updating

After first installing this code and rebooting the Macropad, the CIRCUITPY filesystem will be mounted as read-only. When mounting the device as read-only, Windows and MacOS won't complain if the device is unplugged or rebooted without unmounting it, making it more like a regular old HID device.

To update or edit the code on the device, or to modify the macros, reboot the device with the CIRCUITPY drive mounted in read/write mode. To do that, press the boot switch on the left of the Macropad, and then after releasing the button, immediately hold down the rotary encoder button. The text "Mounting Read/Write" should quickly appear on the screen, and then the CIRCUITPY drive will mount in read/write mode.

## Related Projects

Much thanks to the following related projects:

- [adafruit/Adafruit_CircuitPython_MacroPad](https://github.com/adafruit/Adafruit_CircuitPython_MacroPad)
- [Adafruit Macropad Project Bundle](https://learn.adafruit.com/macropad-hotkeys/project-code)
- [deckerego/Macropad_Hotkeys](https://github.com/deckerego/Macropad_Hotkeys)
