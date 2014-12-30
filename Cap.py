
from I2CInfo import I2CInfo as I2C

class Captivity(object):


	"""
		i2c_addr: the address of the device on the given i2c bus
		i2c_bus: the SMBus instance to use for this device.
		touch_offset: If provided, an offset to be applied to the
		              reported touch indices (helpful when chaining
		              multiple units)
	"""
	def __init__(self, i2c_addr, i2c_bus, touch_offset = 0):
		self._i2c = I2C(i2c_bus, i2c_addr)
		self._touch_offset = touch_offset

	# Writes the given value to the given register as a single transaction and returns the result.
	def write_register(self, register, value):
		if self.is_i2c:
			return self._i2c.write_byte_data(register, value)

	# Reads a value from the given register and returns it.
	def read_register(self, register):
		if self.is_i2c:
			return self._i2c.read_byte_data(register)

	# Returns true if we're configured to use I2C, false otherwise.
	@property
	def is_i2c(self):
		return self._i2c is not None

	# Returns true if we're configured to use SPI, false otherwise.
	@property
	def is_spi(self):
		# TODO really implement this
		return not self.is_i2c

