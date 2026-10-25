# Keypad & Display Tester — Raspberry Pi 4 Wiring Guide

This guide shows how to connect a **3×4 matrix keypad** (phone-style, 12 buttons), a **TM1637 4-digit 7-segment display** and a **power button** to a Raspberry Pi 4 using individual jumper wires. No prior experience is needed.

---

## What you need

| Item | Notes |
|---|---|
| Raspberry Pi 4 | Powered **off** while wiring |
| 3×4 matrix keypad | Has a flat ribbon ending in 7 connector pins |
| TM1637 4-digit display module | Small board with 4 pins labeled CLK, DIO, VCC, GND |
| Momentary push button | The kind that only connects while held down. It needs two legs or wire leads that a jumper can attach to |
| 13 female-to-female jumper wires | 7 for the keypad, 4 for the display, 2 for the button |
| *(Optional)* 1 LED, 1 × 330 Ω resistor, 2 extra jumpers | Status light that blinks on each key press |

---

## Before you start

1. **Shut down and unplug the Pi.** Never connect or move wires while it is powered.
2. **Never connect anything to a 5V pin.** The Pi's signal pins only handle 3.3V. Connecting 5V to them can permanently damage the Pi. Every connection in this guide avoids the 5V pins.
3. Use different wire colors where you can. It makes checking your work much easier.

---

## Finding your way around the header

The **header** is the double row of 40 metal pins along one edge of the Pi.

- Place the Pi flat on the table with the header along the **right-hand side**, so the **SD card slot is at the top** and the **USB ports are at the bottom**.
- The header now has two columns:
  - The **inner column** is closer to the middle of the board.
  - The **outer column** is closest to the board's edge.
- Count **rows from the top** (the SD card end). There are 20 rows.

Every connection below is given as a GPIO name plus its row and column, so you can find it by counting.

---

## Header map

```
  Row   inner column             outer column (board edge)
        ── SD card end ──
   1    3.3V                     5V        ⚠ do not use
   2    GPIO2                    5V        ⚠ do not use
   3    GPIO3   ← Power button   GND     ← Power button
   4    GPIO4                    GPIO14
   5    GND                      GPIO15
   6    GPIO17                   GPIO18
   7    GPIO27                   GND
   8    GPIO22                   GPIO23
   9    3.3V    ← Display VCC    GPIO24
  10    GPIO10  (leave empty)    GND
  11    GPIO9   ← Display DIO    GPIO25
  12    GPIO11  ← Display CLK    GPIO8
  13    GND     ← Display GND    GPIO7
  14    GPIO0                    GPIO1
  15    GPIO5   ← Keypad wire 1  GND
  16    GPIO6   ← Keypad wire 2  GPIO12
  17    GPIO13  ← Keypad wire 3  GND
  18    GPIO19  ← Keypad wire 4  GPIO16  ← Keypad wire 6
  19    GPIO26  ← Keypad wire 5  GPIO20  ← Keypad wire 7
  20    GND     ← LED (−)        GPIO21  ← LED (+)  (optional)
        ── USB port end ──
```

---

## Wiring diagram

The picture below shows every connection. The Pi is drawn in the same position as described above: header on the right, SD card at the top.

![Wiring diagram for the keypad, display, power button and LED on a Raspberry Pi 4](keypad-display-wiring-diagram.png)

---

## Step 1 — Connect the display

The display module has 4 pins with their names printed next to them on the board. Hold the display **face up** (digits readable) with its **pins facing you**. From **left to right**, the pins are:

```
  GND    VCC    DIO    CLK
```

| Display pin | Connect to | Header location |
|---|---|---|
| VCC | 3.3V | Row 9, inner column |
| DIO | GPIO9 | Row 11, inner column |
| CLK | GPIO11 | Row 12, inner column |
| GND | GND | Row 13, inner column |

Leave row 10 (GPIO10) empty.

> **Important:** VCC must go to **3.3V**, not 5V, even though the module may say it supports 5V. Powering it from 5V can push 5V into the Pi's signal pins and damage them.

All four display wires are in the inner column, rows 9 to 13.

---

## Step 2 — Connect the keypad

### Identify wire 1

Hold the keypad **face up** (buttons facing you) with the ribbon hanging down at the bottom. The ribbon ends in 7 connector pins. Counting **left to right**, these are wires 1 through 7.

### Make the connections

| Keypad wire | Function | Connect to | Header location |
|---|---|---|---|
| 1 | Column 2 | GPIO5 | Row 15, inner column |
| 2 | Row 1 | GPIO6 | Row 16, inner column |
| 3 | Column 1 | GPIO13 | Row 17, inner column |
| 4 | Row 4 | GPIO19 | Row 18, inner column |
| 5 | Column 3 | GPIO26 | Row 19, inner column |
| 6 | Row 3 | GPIO16 | Row 18, **outer** column |
| 7 | Row 2 | GPIO20 | Row 19, **outer** column |

The first five wires go down the inner column in order. The last two go in the outer column, directly beside wires 4 and 5.

> **Note:** The keypad does not need power or ground wires. All 7 of its wires are signal connections.

---

## Step 3 — Connect the power button

The button lets you shut the Pi down safely and start it again without unplugging it.

| Button leg | Connect to | Header location |
|---|---|---|
| Either leg | GPIO3 | Row 3, inner column |
| The other leg | GND | Row 3, outer column |

A momentary button has no polarity, so it doesn't matter which leg goes where. Both wires sit side by side in row 3.

> **Why GPIO3?** It's the only pin that can wake a Pi 4 after it has been shut down, so the button must use it.

If your button has four legs (a common square "tactile" button), the legs are connected in pairs. Use two legs on **opposite corners** of the button to be sure you get the switch and not a pair that's always connected.

---

## Step 4 (optional) — Connect the status LED

The LED lights briefly each time a key is pressed.

An LED has two legs. The **longer leg is positive (+)** and the shorter leg is negative (−). An LED must always have a resistor in line with it, or it can burn out and damage the Pi.

| LED part | Connect to | Header location |
|---|---|---|
| Long leg (+), through the 330 Ω resistor | GPIO21 | Row 20, outer column |
| Short leg (−) | GND | Row 20, inner column |

The resistor can go on either side of the LED, as long as it's in the path between GPIO21 and the LED.

---

## Step 5 — Check your work before powering on

Go through this list with the Pi still unplugged:

- [ ] Nothing is connected to either **5V** pin (rows 1 and 2, outer column).
- [ ] The power button's two wires are in **row 3**, one in each column.
- [ ] Display VCC goes to **3.3V** (row 9, inner column).
- [ ] Display GND goes to **GND** (row 13, inner column).
- [ ] Row 10, inner column (GPIO10) is **empty**.
- [ ] Keypad wires 1–5 are in rows 15–19 of the **inner** column, in order.
- [ ] Keypad wires 6 and 7 are in rows 18 and 19 of the **outer** column.
- [ ] Every wire is pushed fully onto its pin and none are touching each other.
- [ ] If using the LED: the long leg goes toward GPIO21 and the resistor is in place.

Once everything checks out, plug in the Pi.

---

## Step 6 — Turn on the power button

The button needs one line added to a settings file before it works. Do this once, on the Pi itself.

1. Open a terminal on the Pi.
2. Open the settings file in an editor:

   ```bash
   sudo nano /boot/firmware/config.txt
   ```

   (On older versions of Raspberry Pi OS, the file is `/boot/config.txt` instead.)
3. Use the arrow keys to go to the very bottom of the file and add this line:

   ```
   dtoverlay=gpio-shutdown
   ```

4. Save and exit: press **Ctrl+O**, then **Enter**, then **Ctrl+X**.
5. Restart the Pi:

   ```bash
   sudo reboot
   ```

### Using the button

- **To shut down:** press the button once. Wait until the green activity light on the Pi stops flashing before unplugging it.
- **To start up again:** press the button once more while the Pi is still plugged in.

The button only works while the Pi has power. If you unplug it, you'll need to plug it back in to start it.

---

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| Display stays blank | VCC or GND not connected, or CLK and DIO swapped. Check rows 9, 11, 12 and 13. |
| Display shows garbage | CLK and DIO swapped. Swap the wires in rows 11 and 12. |
| Pressing keys gives the wrong numbers | The keypad ribbon is connected in reverse order. Re-check which end is wire 1. |
| Some keys never respond | One keypad wire is loose or in the wrong position. Re-check the keypad table. |
| Power button does nothing | The `dtoverlay=gpio-shutdown` line is missing or the Pi wasn't restarted after adding it. Also check both button wires are in row 3. |
| Pi shuts down by itself right after starting | The button is using two legs that are always connected. Move one wire to the leg on the opposite corner. |
| Button shuts down but won't start the Pi | Make sure the Pi is still plugged in. If it is, the Pi's bootloader may have been set to cut power on shutdown; ask whoever set up the Pi. |
| LED never lights | LED is backwards (swap its legs) or the resistor is missing a connection. |
| Pi won't boot or resets | A wire may be touching a 5V or GND pin it shouldn't. Unplug immediately and check every connection. |

---

## Quick reference

| Component | Connection | GPIO |
|---|---|---|
| Power button | Either leg | GPIO3 |
| Power button | Other leg | GND |
| Display | DIO | GPIO9 |
| Display | CLK | GPIO11 |
| Display | VCC | 3.3V |
| Display | GND | GND |
| Keypad | Row 1 | GPIO6 |
| Keypad | Row 2 | GPIO20 |
| Keypad | Row 3 | GPIO16 |
| Keypad | Row 4 | GPIO19 |
| Keypad | Column 1 | GPIO13 |
| Keypad | Column 2 | GPIO5 |
| Keypad | Column 3 | GPIO26 |
| LED (optional) | + (via 330 Ω) | GPIO21 |
| LED (optional) | − | GND |
