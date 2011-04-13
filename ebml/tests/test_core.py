import unittest
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from random import randint
from ..core import *


class ElementSizeTests(unittest.TestCase):
	def assert_roundtrip(self, value, length=None):
		encoded = encode_element_size(value, length=length)
		encoded_stream = StringIO(encoded)
		self.assertEqual(value, read_element_size(encoded_stream)[0])
	
	def test_unknown(self):
		for length in xrange(1, 9):
			self.assert_roundtrip(None, length=length)
	
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


class ElementIDTests(unittest.TestCase):
	ebml_ids = (
		0x1a45dfa3,
		0x4286,
		0x42f7,
		0x42f2,
		0x42f3,
		0x4282,
		0x4287,
		0x4285,
		0xbf,
		0xec
	)
	
	def assert_roundtrip(self, value):
		encoded = encode_element_id(value)
		encoded_stream = StringIO(encoded)
		self.assertEqual(value, read_element_id(encoded_stream)[0])
	
	def test_ebml_ids(self):
		for id_ in self.ebml_ids:
			self.assert_roundtrip(id_)


if __name__ == '__main__':
	unittest.main()