import unittest
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from random import randint
from ..core import *


class ElementSizeTestsBase(object):
	def assert_roundtrip(self, value, min_length=1, max_length=EBMLMaxSizeLength):
		encoded = encode_element_size(value, min_length=min_length, max_length=max_length)
		encoded_stream = StringIO(encoded)
		self.assertEqual(value, read_element_size(encoded_stream, max_length=max_length)[0])


class ElementSizeTests(unittest.TestCase, ElementSizeTestsBase):
	def test_undefined(self):
		for length in xrange(1, 9):
			self.assert_roundtrip(None, min_length=length)
	
	def test_base_10(self):
		for value in (10**exp for exp in xrange(1, 16)):
			self.assert_roundtrip(value)
	
	def test_base_2(self):
		for value in (2**exp for exp in xrange(1, 56)):
			self.assert_roundtrip(value)
	
	def test_max_base_2(self):
		for value in ((2**exp) - 2 for exp in xrange(1, 57)):
			self.assert_roundtrip(value)
		
	def test_random(self):
		maximum = 2**56 - 2
		for value in (randint(0, maximum) for i in xrange(0, 200)):
			self.assert_roundtrip(value)


class LargeElementSizeTests(unittest.TestCase, ElementSizeTestsBase): # tests values that WILL be longer than 8 bytes (EBMLMaxSizeLength)
	def test_base_10(self):
		for value in (10**exp for exp in xrange(17, 300)):
			self.assert_roundtrip(value, max_length=1024)
	
	def test_base_2(self):
		for value in (2**exp for exp in xrange(56, 1024)):
			self.assert_roundtrip(value, max_length=1024)
	
	def test_max_base_2(self):
		for value in ((2**exp) - 2 for exp in xrange(57, 1024)):
			self.assert_roundtrip(value, max_length=1024)
	
	def test_random(self):
		for value in (randint(2**56 - 1, 2**10240) for i in xrange(0, 200)):
			self.assert_roundtrip(value, max_length=10240)


# class ElementIDTests(unittest.TestCase):
# 	def assert_roundtrip(self, value, max_length=EBMLMaxIDLength):
# 		encoded = encode_element_id(value, max_length=max_length)

if __name__ == '__main__':
	unittest.main()