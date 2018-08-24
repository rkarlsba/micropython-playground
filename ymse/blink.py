import utime
import machine

pin21 = machine.Pin(21, machine.Pin.OUT)

while True:
        pin21.value(1)
        utime.sleep_ms(500)
        pin21.value(0)
        utime.sleep_ms(500)
