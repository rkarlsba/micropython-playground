# vim:ts=4:sw=4:sts=4:noet:ai

all:
	@echo Use 'make install'

install:
	@for fn in boot.py temperature.py temperature_client.py ; do \
		ampy --port /dev/tty.SLAB_USBtoUART put $$fn ; \
	done
	@ampy --port /dev/tty.SLAB_USBtoUART mkdir schedule || true
	@ampy --port /dev/tty.SLAB_USBtoUART put schedule/__init__.py schedule

