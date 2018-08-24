# This file is executed on every boot (including wake-boot from deepsleep)
# vim:ts=4:sw=4:sws=4:et:ai

import network
import machine
import esp
import gc
import time
#import webrepl

#esp.osdebug(None)

#webrepl.start()

def wifi_connect():
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('roysittnett', 'ikkeveldighemmelig')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

print("Let's wait a while...")
time.sleep(2)
wifi_connect()

gc.collect()
gc.enable()

