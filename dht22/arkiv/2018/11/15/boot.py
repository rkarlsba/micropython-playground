# vim:ts=4:sw=4:sts=4:et:ai

import machine
import dht
import network
# from network import WLAN
import os
import time
import socket

# standardgreier
import esp
esp.osdebug(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

# mine ting
dhtpin = 5
ssid = 'secredssid'
password = 'asdf'
port = 4949
listen_addr = '0.0.0.0'

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(True)
ap_if.active(False)

sensor=dht.DHT22(machine.Pin(dhtpin))

def df():
    fs_stat = os.statvfs("/")
    fs_size = fs_stat[0] * fs_stat[2]
    fs_free = fs_stat[0] * fs_stat[3]
    print("File System Size {:,} - Free Space {:,}".format(fs_size, fs_free))

def init():
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        machine.idle() # save power while waiting

print("") # tom linje
df()

def tempfukt():
    sensor.measure()
    time.sleep(0.5)
    sensor.measure()
    print(sensor.temperature())
    print(sensor.humidity())

import temphumtcp

tempfukt()


