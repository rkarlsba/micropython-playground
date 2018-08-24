PORT=/dev/ttyUSB0
SPEED=115200

all:
	@echo "Usage: make install"

install:
	ampy --port $(PORT) --baud $(SPEED) put dht22.py
	ampy --port $(PORT) --baud $(SPEED) put main.py
