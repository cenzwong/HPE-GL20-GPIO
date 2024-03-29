# HPE-GL20-GPIO
This is the sample python script for accessing the HPE GL20 IoT Gateway's GPIO. This is not the official module support, use it on your own risk.

# gRPC Service
You might want to use gRPC server to speed up deployment
https://github.com/helloezmeral/HPE-GL20-gRPC
## Getting Started
### Background
You need to have [HPE GL20 IoT Gateway](https://buy.hpe.com/us/en/servers/edgeline-systems/edgeline-systems/edgeline-intelligent-gateways/hpe-gl20-iot-gateway/p/1008670391),  purchase it via local channel: 

![image](https://user-images.githubusercontent.com/44856918/118230724-b185f980-b4c0-11eb-8078-986fca038465.png)

You can check the offical document [here](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00008434en_us)

### Important information

This configuration is routed internally and cannot be changed. Using other configuration could cause damgae to the internal circuitry.

![](https://github.com/helloezmeral/HPE-GL20-GPIO/blob/master/.doc/image/GL20_DIO.png?raw=true)\

| Digital I/O | PIN0-5 | PIN6-7 | PIN8-9|
---|---|---|---
| - | DI | DO | GND |

|||
|---|---|
| DI | Pull-up|
| DO | Open collector |

Note: \
**Pull-up**: If nothing is connected to input pins, it reads as logical high. Connect to ground\
**Open Collector**: Output high means Open Circuit; Output Low means Short Circuit
### STEP 1: Set up Environment

```sh
# Installing the i2ctools
sudo apt install i2c-tools
```

### STEP 2: Check the Environment Variable
```sh
# detect which smbus is the used

# run if devices is not visible on the initial list of i2c device. Run this:
# sudo modprobe i2c-i801 
sudo i2cdetect -l
```
**NOTE**: look for the one with name *SMBus I801 adapter at f040*. This will be in format of *i2c-x*.
![](https://github.com/helloezmeral/HPE-GL20-GPIO/blob/master/.doc/image/i2cdetect.png?raw=true)
- This output shows the I2C connector is conected as Bus 0.

### STEP 3: Python Setup
```sh
# install smbus2 library
sudo pip3 install smbus2
```

Happy hacking: Accessing the peripheral require root access
```sh
sudo python
```
### Getting Started

#### Import Module
```sh
# download the python module for connecting the GPIO
# put it under same directory
wget https://raw.githubusercontent.com/cenzwong/HPE-GL20-GPIO/master/pyGL20.py 
```
#### Python Code
```py
# import python pyGL20 GPIO module
from pyGL20 import GPIO

# Initiate I2C bus zero communication
IO = GPIO(0) # This means i2c-0

# Write Logic High on pin 6
IO.digitalWrite(IO.PIN6, True)

# Toggle Logic on pin 7 
IO.digitalToggle(IO.PIN(7), True)

# Read Logic on pin 1 
IO.digitalRead(IO.PIN(1))
```

### Module pyGL20 Code Example
- Example Blink code

```py
# blink.py
from pyGL20 import GPIO
import time

"""
Please run 
::
sudo i2cdetect -l
::
to find the coresponding i2c-x bus of "SMBus I801 adapter at f040"
replace the number x of the below variable.
"""
IO = GPIO(0) # This means i2c-0

while True:
    print(IO.digitalWrite(IO.PIN6, True))
    time.sleep(0.1)
    print(IO.digitalWrite(IO.PIN(6), False)) # both work
    time.sleep(0.1)
```

- More
#### digitalRead/digitalReadAll
- Read logical high/low on specific pin/all pins
```py
digitalReadAll(self) -> int:
"""Read all pin and return in byte form

Return
----------
int
    - a value specify all state including OUTPUT port. 0 is LOW, 1 is HIGH
"""
```

```py
digitalRead(self, PINx) -> bool:
"""Read a specific pin and return True if Logic HIGH

Parameters
----------
PINx : PIN0, PIN1, ... PIN7

Return
----------
bool
    - a value specify all state including OUTPUT port. 0 is LOW, 1 is HIGH
"""
```
#### digitalWrite/digitalWriteAll/digitalWriteToggle/digitalWriteToggleAll
- Write/Toggle logical high/low on specific pin/all pins
```py
digitalWriteAll(value: int):
"""Assign both PIN6 and PIN7 simultaneously

Parameters
----------
value : int
    - The value must be within *0-3*. 
    - This represent 0b00, 0b01, 0b10, 0b11
"""
```
```py
digitalWrite(PINx, logic: bool):
"""Write a specific pin

Parameters
----------
PINx : PIN6, PIN7 **ONLY**
Logic: 0,1,True, False
"""
```
```py
digitalWriteToggle(PINx):
"""Toggle the OUTPUT port specific pin (PIN6, PIN7)"""
```
```py
digitalWriteToggleAll():
"""Toggle the OUTPUT port pins (PIN6, PIN7)"""
```
