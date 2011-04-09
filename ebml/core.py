import struct
import datetime
from .exceptions import *


EBMLMaxSizeLength = 8
EBMLMaxIDLength = 4


def _read_vint_to_bytearray(stream, max_width=EBMLMaxSizeLength):
	"""
	
	Reads a vint from stream and returns a bytearray containing all of the bytes without doing any decoding.
	
	:arg stream: the source of the bytes
	:type stream: a file-like object
	:arg max_width: the maximum length, in bytes, of the vint (defaults to :data:`EBMLMaxSizeLength`)
	:type max_width: int
	:returns: bytearray
	
	"""
	
	marker_found = False
	vint_bytes = bytearray()
	vint_len = -7
	while not marker_found:
		vint_len += 8
		if vint_len > max_width:
			raise ParseError('vint exceeds max_width (%(max_width)i)' % {
				'max_width': max_width
			})
		byte = ord(stream.read(1))
		vint_bytes.append(byte)
		for pos in range(0, 8):
			mask = 0b10000000 >> pos
			if byte & mask:
				vint_len += pos
				marker_found = True
				break
	
	remaining_bytes_len = vint_len - len(vint_bytes)
	if remaining_bytes_len > 0:
		vint_bytes.extend(ord(remaining_byte) for remaining_byte in stream.read(remaining_bytes_len))
	
	if len(vint_bytes) != vint_len:
		raise ParseError('Unable to read truncated vint of width %(vint_len)s from stream (%(vint_bytes)s bytes available)' % {
			'vint_len': vint_len,
			'vint_bytes': len(vint_bytes)
		})
	
	return vint_bytes


def read_element_size(stream, max_width=EBMLMaxSizeLength):
	"""
	
	Reads an EBML element size vint from stream and returns a tuple containing:
	
		* the size as an integer, or None if the size is undefined
		* the length in bytes of the size descriptor (the vint) itself
	
	:arg stream: the source of the bytes
	:type stream: a file-like object
	:arg max_width: the maximum length, in bytes, of the vint storing the element size (defaults to :data:`EBMLMaxSizeLength`)
	:type max_width: int
	:returns: tuple
	
	"""
	
	vint_bytes = _read_vint_to_bytearray(stream, max_width)
	vint_len = len(vint_bytes)
	
	int_bytes = vint_bytes[((vint_len - 1) // 8):]
	first_byte_mask = 0b10000000 >> ((vint_len - 1) % 8)
	max_bytes = 0
	
	value = int_bytes[0] & (first_byte_mask - 1)
	
	if value == (first_byte_mask - 1):
		max_bytes += 1
	
	for int_byte in int_bytes[1:]:
		if int_byte == 0b11111111:
			max_bytes += 1
		value = (value << 8) | int_byte
	
	if max_bytes == len(int_bytes):
		value = None
	
	return value, vint_len


def read_element_id(stream, max_width=EBMLMaxIDLength):
	"""
	
	Reads an EBML element ID vint from stream and returns a tuple containing:
	
		* the ID as an integer
		* the length in bytes of the ID descriptor (the vint) itself
	
	:arg stream: the source of the bytes
	:type stream: a file-like object
	:arg max_width: the maximum length, in bytes, of the vint storing the element ID (defaults to :data:`EBMLMaxIDLength`)
	:type max_width: int
	:returns: tuple
	
	"""
	
	vint_bytes = _read_vint_to_bytearray(stream, max_width)
	vint_len = len(vint_bytes)
	
	value = 0
	max_bytes = 0
	min_bytes = 0
	
	for vint_byte in vint_bytes:
		if vint_byte == 0b11111111:
			max_bytes += 1
		elif vint_byte == 0:
			min_bytes += 1
		value = (value << 8) | vint_byte
	
	if max_bytes == vint_len:
		raise ReservedElementIDError('All value bits set to 1')
	elif min_bytes == vint_len:
		raise ReservedElementIDError('All value bits set to 0')
	
	return value, vint_len


def read_int(stream, size):
	value = 0
	if size > 0:
		byte = ord(stream.read(1))
		if (byte & 0b10000000) == 0b10000000:
			value = -1 << 8
		value |= byte
		for i in range(1, size):
			byte = ord(stream.read(1))
			value = (value << 1) | byte
	return value


def read_uint(stream, size):
	value = 0
	for i in range(0, size):
		byte = ord(stream.read(1))
		value = (value << 8) | byte
	return value


def read_float(stream, size):
	if size not in (0, 4, 8):
		# http://www.matroska.org/technical/specs/rfc/index.html allows for 10-byte floats.
		# http://www.matroska.org/technical/specs/index.html specifies 4-byte and 8-byte only.
		# I'm following the latter due to it being more up-to-date than the former, and because it's easier to implement.
		raise ValueError('floats must be 0, 4, or 8 bytes long')
	value = 0.0
	if size in (4, 8):
		data = stream.read(size)
		value = struct.unpack({
			4: '>f',
			8: '>d'
		}[size], data)[0]
	return value


def read_string(stream, size):
	value = ''
	if size > 0:
		value = stream.read(size)
	return value


def read_unicode(stream, size):
	value = u''
	if size > 0:
		data = stream.read(size)
		value = unicode(data, 'utf_8')
	return value


def read_date(stream):
	size = 8 # date is always an 8-byte signed integer
	data = stream.read(size)
	nanoseconds = struct.unpack('>q', data)[0]
	delta = datetime.timedelta(microseconds=(nanoseconds // 1000))
	return datetime.datetime(2001, 1, 1) + delta


def read_binary(stream, size):
	return stream.read(size)