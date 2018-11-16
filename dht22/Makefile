all:
	@echo Use 'make esp_install or server_install'

esp_install:
	@for fn in boot.py ffilib.py sqlite3.py ssid_local.py ; do \
		ampy --port /dev/tty.SLAB_USBtoUART put $$fn ; \
	done

server_install:
	@echo "Not imlemented - fix it yourself…"
