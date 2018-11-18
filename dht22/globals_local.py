# vim:ts=4:sw=4:sts=4:et:ai:fdm=marker

# Skal vi bruk nettverk?
use_networking = 0

# Pinner
pin_dht = 14        # D5
pin_led_r = 12      # D6
pin_led_g = 13      # D7
pin_led_b = 15      # D8
pin_led_o = 2       # onboard - logical low

pin_sda = 4         # D2 - I2C Send DAta
pin_scl = 5         # D1 - I2C Sync CLock - gul
#i2c_freq = 400000   # 400kHz?
i2c_freq = 8000000  # 8MHz?

measure_delay = 5   # Measure every <n> seconds

sta_if = ''
ap_if = ''

port = 4949
listen_addr = '0.0.0.0'
