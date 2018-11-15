#import dht22
#import dhtsock
# vim:fdm=marker

# import the libs and setup dht22
import dht
import machine
import network
import socket
import sys
import time

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

machine.freq(160000000)

wifi_ssid='secredssid'
wifi_password='asdf'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if.connect(wifi_ssid, wifi_password)

isconnected=0

for attempt in range(10):
    if sta_if.isconnected():
        isconnected=1
        break
    else:
        time.sleep_ms(250)

if isconnected == 0:
    print("Failed to connect to wifi")
    sys.exit(1)

addr = socket.getaddrinfo('0.0.0.0', 5050)[0][-1]
s = socket.socket()
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
except socket.error as msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)

s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    line = "t:", sensor.measure(), "h:", sensor.measure()
    print('sending output "', line, '"');
    cl.send(line)
    cl.close()

