import network
import sys
import socket

wifi_ssid='roysittnett'
wifi_password='ikkeveldighemmelig'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if.connect(wifi_ssid, wifi_password)

isconnnected=0

for attempt in range(10):
    if sta_if.isconnected():
        isconnected=1
        break

if isconnected == 0:
    print("Failed to connect to wifi")
    sys.exit(1)

addr = socket.getaddrinfo('0.0.0.0', 5050)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    while True:
        line = cl_file.readline()
        if not line or line == b'\r\n':
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
    response = html % '\n'.join(rows)
    cl.send(response)
    cl.close()

