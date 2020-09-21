"""
Please run 
::
sudo i2cdetect -l
::
to find the coresponding i2c-x bus of "SMBus I801 adapter at f040"
replace the number x of the below variable.

"""
i2c_bus = 0


i2c_addr = 0x27
i2c_cmd_INPUT = 0x00
i2c_cmd_OUTPUT = 0x02
i2c_cmd_CONFIG = 0x06

PIN0 = 7
PIN1 = 6
PIN2 = 5
PIN3 = 4
PIN4 = 3
PIN5 = 2
PIN6 = 1
PIN7 = 0

from smbus2 import SMBus


def digitalWriteAll(value: int):
    """Assign both PIN6 and PIN7 simultaneously
    
    Parameters
    ----------
    value : int
        - The value must be within *0-3*. 
        - This represent 0b00, 0b01, 0b10, 0b11
    """
    if value > 3 or value < 0:
        print("Value should be between 0 and 3")
        quit()
    else:
        with SMBus(i2c_bus) as bus:
            bus.write_byte_data(i2c_addr,i2c_cmd_OUTPUT, value)

def digitalReadAll() -> int:
    """Read all pin and return in byte form
    
    Return
    ----------
    int
        - a value specify all state including OUTPUT port. 0 is LOW, 1 is HIGH
    """
    with SMBus(i2c_bus) as bus:
        return bus.read_byte_data(i2c_addr,i2c_cmd_INPUT)

def digitalRead(PINx) -> bool:
    """Read a specific pin and return True if Logic HIGH
    
    Parameters
    ----------
    PINx : PIN0, PIN1, ... PIN7

    Return
    ----------
    bool
        - a value specify all state including OUTPUT port. 0 is LOW, 1 is HIGH
    """
    with SMBus(i2c_bus) as bus:
        b = bus.read_byte_data(i2c_addr,i2c_cmd_INPUT)
        return bool(b & (1 << PINx))

def digitalWrite(PINx, logic: bool):
    """Write a specific pin
    
    Parameters
    ----------
    PINx : PIN6, PIN7 **ONLY**
    Logic: 0,1,True, False
    """
    if logic == 1:
        # print(bin(digitalReadAll()))
        output = (digitalReadAll() | (1 << PINx)) & 0b11
        # print(bin(output))
    elif logic == 0:
        # print(bin(digitalReadAll()))
        output = (digitalReadAll() & ~(1 << PINx)) & 0b11
        # print(bin(output))
    with SMBus(i2c_bus) as bus:
        bus.write_byte_data(i2c_addr,i2c_cmd_OUTPUT, output)

def digitalWriteToggleAll():
    """Toggle the OUTPUT port pins (PIN6, PIN7)"""
    output = (~digitalReadAll() & 0b11)
    with SMBus(i2c_bus) as bus:
        bus.write_byte_data(i2c_addr,i2c_cmd_OUTPUT, output)

def digitalWriteToggle(PINx):
    """Toggle the OUTPUT port specific pin (PIN6, PIN7)"""
    # print(bin(digitalReadAll()))
    output = ~(~digitalReadAll() ^ (1 << PINx)) & 0b11
    # print(output)
    with SMBus(i2c_bus) as bus:
        bus.write_byte_data(i2c_addr,i2c_cmd_OUTPUT, output)
