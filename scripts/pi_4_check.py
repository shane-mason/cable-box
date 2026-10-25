"""
Keypad & 7-segment display tester - Raspberry Pi 4 version.

Wiring (see keypad-display-wiring.md):
  Display:  CLK = GPIO11, DIO = GPIO9, VCC = 3.3V, GND = GND
  Keypad:   R1 = GPIO6,  R2 = GPIO20, R3 = GPIO16, R4 = GPIO19
            C1 = GPIO13, C2 = GPIO5,  C3 = GPIO26
  LED:      GPIO21 (optional, through a 330 ohm resistor)
  Power:    GPIO3 + GND button, handled by the OS (dtoverlay=gpio-shutdown),
            not by this script. Don't use GPIO3 here.

On the Pi, board.D<n> means GPIO<n>.
"""

import time
import board
import digitalio
import adafruit_matrixkeypad


# ---------------------------------------------------------------------------
# Minimal TM1637 driver (replaces tm1637_display, which targets the Pico)
# ---------------------------------------------------------------------------

# Segment bits: a=0x01 b=0x02 c=0x04 d=0x08 e=0x10 f=0x20 g=0x40
_FONT = {
    "0": 0x3F, "1": 0x06, "2": 0x5B, "3": 0x4F, "4": 0x66,
    "5": 0x6D, "6": 0x7D, "7": 0x07, "8": 0x7F, "9": 0x6F,
    "A": 0x77, "B": 0x7C, "C": 0x39, "D": 0x5E, "E": 0x79,
    "F": 0x71, "G": 0x3D, "H": 0x76, "I": 0x06, "J": 0x1E,
    "L": 0x38, "N": 0x54, "O": 0x3F, "P": 0x73, "R": 0x50,
    "S": 0x6D, "T": 0x78, "U": 0x3E, "Y": 0x6E,
    "-": 0x40, "_": 0x08, " ": 0x00,
}


class TM1637Display:
    def __init__(self, clk_pin, dio_pin, length=4, brightness=7):
        self.length = length
        self.brightness = brightness & 0x07
        self.clk = digitalio.DigitalInOut(clk_pin)
        self.clk.switch_to_output(value=True)
        self.dio = digitalio.DigitalInOut(dio_pin)
        self.dio.switch_to_output(value=True)
        self.clear()

    @staticmethod
    def _delay():
        time.sleep(0.00001)

    def _start(self):
        self.dio.value = True
        self.clk.value = True
        self._delay()
        self.dio.value = False
        self._delay()

    def _stop(self):
        self.clk.value = False
        self._delay()
        self.dio.value = False
        self._delay()
        self.clk.value = True
        self._delay()
        self.dio.value = True
        self._delay()

    def _write_byte(self, data):
        for _ in range(8):  # LSB first
            self.clk.value = False
            self._delay()
            self.dio.value = bool(data & 0x01)
            self._delay()
            self.clk.value = True
            self._delay()
            data >>= 1
        # Acknowledge clock: release DIO and let the chip pull it low
        self.clk.value = False
        self.dio.switch_to_input()
        self._delay()
        self.clk.value = True
        self._delay()
        self.clk.value = False
        self.dio.switch_to_output(value=False)
        self._delay()

    def _write_segments(self, segments):
        self._start()
        self._write_byte(0x40)            # data command: auto-increment address
        self._stop()
        self._start()
        self._write_byte(0xC0)            # start at digit 0
        for seg in segments:
            self._write_byte(seg)
        self._stop()
        self._start()
        self._write_byte(0x88 | self.brightness)  # display on + brightness
        self._stop()

    def clear(self):
        self._write_segments([0x00] * self.length)

    def print(self, value):
        """Show a number (right-aligned) or text (left-aligned)."""
        if isinstance(value, int):
            text = str(value).rjust(self.length)
        else:
            text = str(value).upper().ljust(self.length)
        text = text[: self.length]
        self._write_segments([_FONT.get(ch, 0x00) for ch in text])


# ---------------------------------------------------------------------------
# Hardware setup
# ---------------------------------------------------------------------------

led = digitalio.DigitalInOut(board.D21)
led.direction = digitalio.Direction.OUTPUT

display = TM1637Display(board.D11, board.D9, length=4)  # CLK, DIO
display.print("HELO")

cols = [digitalio.DigitalInOut(x) for x in (board.D13, board.D5, board.D26)]             # C1, C2, C3
rows = [digitalio.DigitalInOut(x) for x in (board.D6, board.D20, board.D16, board.D19)]  # R1, R2, R3, R4
keys = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        ('*', 0, '#'))

keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

try:
    while True:
        time.sleep(0.1)

        pressed = keypad.pressed_keys
        if pressed:
            led.value = True
            print("Pressed: ", pressed)
            if isinstance(pressed[0], int):
                display.print(pressed[0])
            elif pressed[0] == "*":
                display.print("AST")
            elif pressed[0] == "#":
                display.print("PND")
            else:
                display.print("ERR")
            # debounce
            time.sleep(0.25)
            led.value = False
except KeyboardInterrupt:
    display.clear()
    led.value = False
