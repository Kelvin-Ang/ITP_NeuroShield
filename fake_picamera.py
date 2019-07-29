import numpy as np
# import platform
from wrappers import printf
from base import base


class BGR(object):
	"""Fake class"""

	@printf
	def __init__(self, sz):
		# constructor
		self.array = np.random.rand(*sz)

	@printf
	def truncate(self, num):
		# refreshes the fake image
		self.array = np.random.rand(*self.array.shape)


# class picamera(object):
# 	"""Fake class"""
class PiCamera(base):
	"""Fake class"""
	resolution = (0, 0)

	def __init__(self):
		# empty constructor
		# print('WARNING: Fake_RPi PiCamera on {}'.format(platform.system().lower()))
		base.__init__(self, self.__class__)
		pass

	def close(self):
		# this does nothing
		pass

	@printf
	def capture(self, image):
		# this does nothing
		pass


class array(object):
	"""Fake class"""

	@staticmethod
	def PiRGBArray(cam, size):
		return BGR(size)