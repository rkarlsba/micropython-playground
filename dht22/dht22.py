# import the libs and setup dht22
import dht
import machine

# setup the dht22
sensor = dht.DHT22(machine.Pin(16))

#sensor.measure()

def gettemp(with_header=1):
    sensor.measure()
    temp = sensor.temperature()
    if with_header:
        print("Temperature = ", end='')
    print(temp)

def gethum(with_header=1):
    sensor.measure()
    hum = sensor.humidity()
    if with_header:
        print("Humidity = ", end='')
    print(hum)

