#!/usr/bin/env python

import Adafruit_CAP1188


if __name__ == "__main__":

    bus = smbus.SMBus(1)
    cap2_addr = 0x29

    cap2 = Adafruit_CAP1188(cap2_addr, bus, touch_offset = 8)

    # Turn on multitouch
    cap2.multitouch_enabled = True

    # Link LEDs to touches
    cap2.leds_linked = True

    # Speed it up
    #cap2.write_register(Adafruit_CAP1188.STANDBYCFG, 0x30)

    print cap2

    while True:
    	t = cap2.touched
    	for x in t:
    		print "Touched: " + x