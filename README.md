# cable-box
3d Printable Cable Box Model

The models were used to make a 3-d printed cable box replica to house a Raspberry Pi 5 for a cable simulation built using FieldStation42.


![A screenshot cable box model](docs/model0.png?raw=true)

To use the models, clone the repository and print both sets:

```
CableBox-main.stl - Contains the main box, trim pieces and foot screws.
CableBox-bottom.stl - Conains the bottom of the box.
```

## List of Materials Used
* [3x4 Matrix Keypad](https://www.adafruit.com/product/3845)
* [4 Digit 7 Segment TM1637 LED Display Board](https://www.amazon.com/dp/B0BFQNFX6D)
* [Raspberry Pi 5 - with active cooler](https://www.adafruit.com/product/5815)
* [F2F Jumper Wires](https://www.adafruit.com/product/1950)
* 12" HDMI Extender (pigtail)
* Plexiglass (1/8th inch)
* 4 M2.5 screws and nuts
* 4 M2 screws and nuts
* Superglue

## Process

### Step 1 - Printing
Print both models above. I used PLA with a .4 mm nozel on a textured plate - but ABS should work.

### Step 2 - Mounting the Pi
The printed model contains mounts for the raspberry pi 5 on the top of the box. There are cutouts in each mounting post for an M2.5 nut to fit into - secure it with superglue.

After the superglue is dried, just use M2.5 screws to secure it to the post.

Its important to use a pi with an active cooler - otherwise it will likely heat up and throttle perfomance. 

### Step 3 - Mount the Keypad
The keypad mounts using M2 screws and nuts in the corners of the cutout on the top of the box.

### Step 4 - Mount the LED Display
The display mounts in the cutout in the front of the box using superglue. The fit should be fairly tight, but it also works as long as it is glued to one of the two sides. There is room for improvement in this part of the design for sure.

Optional: cut plexiglass to <INSERT SIZE> and fit in front of the display.

Fit black trim piece over the display area.

### Step 5 Wire It Up!

| Raspberry PI  |LED Display    |
| ------------- | ------------- |
|A 5v |VCC |
|GND  |GND |
|GPIO17  |CLK |
|GPIO16  | DIO |

| Raspberry PI  |Keypad         |
| ------------- | ------------- |
|GPIO20|C2|
|GPIO05|R1|
|GPIO26|C1|
|GPIO19|R4|
|GPIO21|C3|
|GPIO13|R3|
|GPIO06|R2|

![A connection diagram](docs/cable-box-fritzing.png?raw=true)

Additional documentation with images is in-progress.



