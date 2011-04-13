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


class ValueTestCase(unittest.TestCase):
	encoder = None
	reader = None
	
	def assert_roundtrip(self, value):
		if self.encoder is not None and self.reader is not None:
			encoded = self.encoder(value)
			encoded_stream = StringIO(encoded)
			self.assertEqual(value, self.reader(encoded_stream, len(encoded)))
		else:
			raise NotImplementedError


class UnsignedIntegerTests(ValueTestCase):
	encoder = staticmethod(encode_unsigned_integer)
	reader = staticmethod(read_unsigned_integer)
	maximum = 2**64 - 1
	
	def test_random(self):
		for value in (randint(0, self.maximum) for i in xrange(0, 10000)):
			self.assert_roundtrip(value)
	
	def test_maximum(self):
		self.assert_roundtrip(self.maximum)


class SignedIntegerTests(ValueTestCase):
	encoder = staticmethod(encode_signed_integer)
	reader = staticmethod(read_signed_integer)
	minimum = -(2**63)
	maximum = (2**63) - 1
	
	def test_random(self):
		for value in (randint(self.minimum, self.maximum) for i in xrange(0, 10000)):
			self.assert_roundtrip(value)
	
	def test_minimum(self):
		self.assert_roundtrip(self.minimum)
	
	def test_maximum(self):
		self.assert_roundtrip(self.maximum)


if __name__ == '__main__':
	unittest.main()