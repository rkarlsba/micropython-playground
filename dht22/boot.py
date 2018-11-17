# vim:ts=4:sw=4:sts=4:et:ai:fdm=marker

import machine
import dht
import ssd1306
import network
#import schedule
#import os
import time
import socket

from ssid_local import ssid,password
from globals_local import *

# standardgreier
#import esp
#esp.osdebug(1)
import gc
#import webrepl
#webrepl.start()
gc.collect()

if (use_networking):
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    sta_if.active(True)
    ap_if.active(False)

sensor=dht.DHT22(machine.Pin(pin_dht))

# og LEDs
# RGB-led ikke i bruk for øyeblikket {{{
#led_r = machine.Pin(pin_led_r, machine.Pin.OUT)
#led_g = machine.Pin(pin_led_g, machine.Pin.OUT)
#led_b = machine.Pin(pin_led_b, machine.Pin.OUT)
# }}}
led_o = machine.Pin(pin_led_o, machine.Pin.OUT)
# RGB-led ikke i bruk for øyeblikket {{{
#led_r.off()
#led_g.off()
#led_b.off()
# }}}
led_o.on()

# Skjerm
i2c = machine.I2C(-1, scl=machine.Pin(pin_scl), sda=machine.Pin(pin_sda), freq=i2c_freq)
# i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# def df():
#     fs_stat = os.statvfs("/")
#     fs_size = fs_stat[0] * fs_stat[2]
#     fs_free = fs_stat[0] * fs_stat[3]
#     print("File System Size {:,} - Free Space {:,}".format(fs_size, fs_free))

def init():
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        machine.idle() # save power while waiting

# print("") # tom linje
# df()

def dhtmeasure():
    sensor.measure()
    time.sleep(0.2)
    sensor.measure()

def dhttemp():
    return sensor.temperature()

def dhthum():
    return sensor.humidity()

def temphum():
    dhtmeasure()
    print(dhttemp())
    print(dhthum())

def display_temphum():
    temp = str(dhttemp()) 
    hum = str(dhthum()) 
    oled.fill(0) 
    oled.text("Temp: " + temp, 0, 2) 
    oled.text("Hum:  " + hum, 0, 12) 
    oled.show()

def update_and_display_temphum():
    dhtmeasure()
    display_temphum()

# ikke her {{{
# addr = socket.getaddrinfo(listen_addr, port)[0][-1]
# sock = socket.socket()
# sock.bind(addr)
# sock.listen(1)
# print('Listening on', addr)
# }}}
temphum()
display_temphum()

schedule.every().minute.do(update_and_display_temphum)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# while 1:
#     dhtmeasure()
#     display_temphum()
#     time.sleep(5)
