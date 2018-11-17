# vim:ts=4:sw=4:sts=4:noet:ai

all:
	@echo Use 'make esp_install or server_install'

esp_install:
	@for fn in boot.py ffilib.py globals_local.py sqlite3.py ssd1306.py ssid_local.py temphumtcp.py ; do \
		ampy --port /dev/tty.SLAB_USBtoUART put $$fn ; \
	done
	@ampy --port /dev/tty.SLAB_USBtoUART mkdir schedule || true
	@ampy --port /dev/tty.SLAB_USBtoUART put schedule/__init__.py schedule

server_install:
	@echo "Not imlemented - fix it yourself…"
