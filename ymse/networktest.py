import network

wifi_ssid = "roysittnett"
wifi_password = "hemmelig"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(wifi_ssid, wifi_password)

