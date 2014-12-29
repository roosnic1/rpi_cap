
import I2CInfo

class Captivity(object):
	def __init__(self, i2c_addr, i2c_bus, touch_offset = 0):

		"""
		i2c_addr: the address of the device on the given i2c bus
		i2c_bus: the SMBus instance to use for this device.
		touch_offset: If provided, an offset to be applied to the
		              reported touch indices (helpful when chaining
		              multiple units)
		"""

		self._i2c = I2CInfo(i2c_bus, i2c_addr)
		self._touch_offset = touch_offset

	def __str__(self):
		pass

	@property
    def driver_name(self):
        pass

	@property
    def is_i2c(self):

        """
        Returns true if we're configured to use I2C, false otherwise.
        """

        return self._i2c is not None

    @property
    def is_spi(self):

        """
        Returns true if we're configured to use SPI, false otherwise.
        """

        # TODO really implement this
        return not self.is_i2c

    def write_register(self, register, value):
    	pass

    def read_register(self, register):
    	pass

