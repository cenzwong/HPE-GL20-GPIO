# HPE-GL20-GPIO
This is the sample python script for accessing the HPE GL20 IoT Gateway's GPIO. This is not the official module support, use it on your own risk.

## Getting Started
### Background
You need to have [HPE GL20 IoT Gateway](https://buy.hpe.com/us/en/servers/edgeline-systems/edgeline-systems/edgeline-intelligent-gateways/hpe-gl20-iot-gateway/p/1008670391),  purchase it via local channel: 

![HPE GL20 IoT Gateway](https://assets.ext.hpe.com/is/image/hpedam/s00004847?$thumbnail$&.png)

You can check the offical document [here](https://support.hpe.com/hpesc/public/docDisplay?docLocale=en_US&docId=a00008434en_us)

### Important information

This config is routed internally, cannot be changed. Using other config could cause damgae to the internal circuitry.

| Digital I/O | PIN0-5 | PIN6-7 | PIN8-9|
---|---|---|---
| - | DI | DO | GND |

|||
|---|---|
| DI | Pull-up|
| DO | Open collector |


### STEP 1: Set up Environment

```sh
# Installing the i2ctools
sudo apt install i2c-tools
```

### STEP 2: Check the Environment Variable
```sh
# detect which smbus is the used
sudo i2cdetect -l
```
**NOTE**: look for the one with name *SMBus I801 adapter at f040*. This will be in format of *i2c-x*.

### STEP 3: Python Setup
```sh
# install smbus2 library
sudo pip3 install smbus2
```

```sh
# download the python module for connecting the GPIO
# put it under same directory
wget https://raw.githubusercontent.com/cenzwong/HPE-GL20-GPIO/master/pyGL20.py 
```
Happy hacking: Accessing the peripheral require root access
```sh
sudo python
```

### Module pyGL20 Code Example
- Example Blink code

```py
# blink
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
    print(IO.digitalWrite(IO.PIN6, False))
    time.sleep(0.1)
```

- More
#### digitalRead/digitalReadAll
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
```
"""
#### digitalWrite/digitalWriteAll/digitalWriteToggle/digitalWriteToggleAll
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
