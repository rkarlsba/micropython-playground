import network
import utelnetserver

ssid="roysittnett"
passord="hemmelig"

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, passord)

utelnetserver.start()
