#!/usr/bin/env python

import smbus
import time
from Adafruit_CAP1188 import Adafruit_CAP1188 as CAP1188

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.IN)


if __name__ == "__main__":

    bus = smbus.SMBus(1)
    cap2_addr = 0x29

    cap2 = CAP1188(cap2_addr, bus, touch_offset = 0)

    #print "multitouch Status: " + str(cap2.multitouch_enabled)

    # Turn on multitouch
    cap2.multitouch_enabled = False

    #print "multitouch Status: " + str(cap2.multitouch_enabled)

    # Link LEDs to touches
    cap2.leds_linked = True

    # Enabled IRQ
    cap2.irq_enabled = True

    # Speed it up
    #cap2.write_register(Adafruit_CAP1188.STANDBYCFG, 0x30)

    print cap2

    while True:

        if(GPIO.input(29)):
            print "INPUT is HIGH"
        else:
            print "INPUT is LOW"
            t = cap2.touched
            for x in t:
                print "Touched: " + str(x)

        time.sleep(1)