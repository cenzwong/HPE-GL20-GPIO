# python - i2c

import pyGL20

print( bin(pyGL20.digitalReadAll()))
pyGL20.digitalWriteAll(0b10)
print(pyGL20.digitalRead(pyGL20.PIN0))
pyGL20.digitalWrite(pyGL20.PIN7, 1)
pyGL20.digitalWrite(pyGL20.PIN6, 0)
pyGL20.digitalWriteToggleAll()
pyGL20.digitalWriteToggle(pyGL20.PIN7)


