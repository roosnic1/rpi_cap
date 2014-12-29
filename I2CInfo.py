#!/usr/bin/env python

class I2CInfo(object):

    def __init__(self, bus, address):
        self._bus = bus
        self._address = address

    def write_byte_data(self, register, value):
        self._bus.write_byte_data(self._address, register, value)

    def read_byte_data(self, register):
        return self._bus.read_byte_data(self._address, register)