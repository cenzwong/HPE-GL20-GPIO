# python - i2c

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
IO = GPIO(0)

while True:
    print(IO.digitalRead(IO.PIN0))
    time.sleep(0.1)
