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
* 6"+ Micro HDMI to HDMI Adapter (pigtail)
* Plexiglass (1/8th inch)
* 4 M2.5 screws and nuts
* 4 M2 screws and nuts
* Superglue

## Building the Box
The put it all together, follow the steps below. At the finish, you should have a box that looks like this:
![A cable box on a table with wired connecting components](docs/cable_cover_3.png?wired-box.pngraw=true)

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

Optional: cut plexiglass to SIZE and fit in front of the display.

Fit black trim piece over the display area.

### Step 5 Wire It Up!
In this step, you'll connect all the wires. Your setup should look like the picture below at the end of this step:

![A cable box on a table with wired connecting components](docs/wired-box.png?wired-box.pngraw=true)

#### TM1637 LED Display Board

The following table shows the connections between the Rasberry Pi 5 and the TM1637 LED Display Board.

| Raspberry PI  |LED Display    |
| ------------- | ------------- |
|A 5v |VCC |
|GND  |GND |
|GPIO17  |CLK |
|GPIO16  | DIO |

#### 3x4 Matrix Keypad

The following table shows the connections between the Raspberry Pi 5 and the 3x4 Matrix Keypad. For more information on the pinouts for this keypad and the Raspberry Pi 5, see [this Adafruit Learning Guide](https://learn.adafruit.com/matrix-keypad/overview).

| Raspberry PI  |Keypad         |
| ------------- | ------------- |
|GPIO20|C2|
|GPIO05|R1|
|GPIO26|C1|
|GPIO19|R4|
|GPIO21|C3|
|GPIO13|R3|
|GPIO06|R2|

#### Fritzing Diagram

The following diagram shows an overview of the connections.

![A connection diagram](docs/cable-box-fritzing.png?raw=true)

Additional documentation with images is in-progress.

### Step 5: Connect Power & HDMI

In this step, just connect the micro-HDMI to HDMI pigtail to the Pi's micro-HDMI output and the power cable to the Pi's USB C connector and run them through the openings on the side closest to the connectors. You will probably want to use use something to prevent the cables from being pulled, so I use some thick copper wire. A think ziptie or some tape wil work also. When this step is completed, it should look like the picture below.

![Cable box with wires](docs/cable_plugs.png?raw=true)

### Step 6: Secure Bottom
Use the foot screws in the first print to secure the bottom piece from the second print.

## Setting Up the Software

To use the cable box script, you will need to install the python drivers for the LED display and matrix keypad. The script is located in the FieldStation42 repo at `fs42/pi/cable_box.py` ([link](https://github.com/shane-mason/FieldStation42/blob/main/fs42/pi/cable_box.py)).

### Install Keypad Drivers

For the matrix keypad, you you first need to install Adafruit Blinka libraries. 
- [Follow this guide to install CircuitPython via Blinka](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi)

Next, install the matrix keypad driver using pip3 (after you activate your virtual env)

```
source env/bin/activate
pip3 install adafruit-circuitpython-matrixkeypad
```

### Install LED Drivers

Use pip to install tm1637 LED drivers

```
source env/bin/activate
pip3 install raspberrypi-tm1637
```

### Starting the Script on Startup

For ideas about how to use this at startup, see [this wiki page](https://github.com/shane-mason/FieldStation42/wiki/Autostart-on-Rasberry-Pi).

