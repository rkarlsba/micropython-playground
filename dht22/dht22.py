# import the libs and setup dht22
import dht
import machine

# setup the dht22
sensor = dht.DHT22(machine.Pin(16))

sensor.measure()
temp = sensor.temperature()
hum = sensor.humidity()

def gettemp(with_header=1):
    if with_header:
        print("Temperature = ", end='')
    print(temp)

def gethum(with_header=1):
    if with_header:
        print("Humidity = ", end='')
    print(hum)

