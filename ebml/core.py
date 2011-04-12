import struct
import datetime
from math import log
from .exceptions import *


EBMLMaxSizeLength = 8
EBMLMaxIDLength = 4


def _read_vint_to_bytearray(stream, max_length=EBMLMaxSizeLength):
	"""
	
	Reads a vint from stream and returns a bytearray containing all of the bytes without doing any decoding.
	
	:arg stream: the source of the bytes
	:type stream: a file-like object
	:arg max_length: the maximum length, in bytes, of the vint (defaults to :data:`EBMLMaxSizeLength`)
	:type max_length: int
	:returns: bytearray
	
	"""
	
	marker_found = False
	vint_bytes = bytearray()
	vint_len = -7
	while not marker_found:
		vint_len += 8
		if vint_len > max_length:
			raise ParseError('vint length (%(vint_len)i) exceeds max_length (%(max_length)i)' % {
				'vint_len': vint_len,
				'max_length': max_length
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
		raise ParseError('Unable to read truncated vint of length %(vint_len)s from stream (%(vint_bytes)s bytes available)' % {
			'vint_len': vint_len,
			'vint_bytes': len(vint_bytes)
		})
	
	return vint_bytes


def read_element_size(stream, max_length=EBMLMaxSizeLength):
	"""
	
	Reads an EBML element size vint from stream and returns a tuple containing:
	
		* the size as an integer, or None if the size is undefined
		* the length in bytes of the size descriptor (the vint) itself
	
	:arg stream: the source of the bytes
	:type stream: a file-like object
	:arg max_length: the maximum length, in bytes, of the vint storing the element size (defaults to :data:`EBMLMaxSizeLength`)
	:type max_length: int
	:returns: tuple
	
	"""
	
	vint_bytes = _read_vint_to_bytearray(stream, max_length)
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


def encode_element_size(size, min_length=None, max_length=EBMLMaxSizeLength):
	"""
	
	Encode the size of an EBML element as a vint, optionally with a minimum length.
	
	:arg size: the element size, or None if undefined
	:type size: int or None
	:arg min_length: the minimum length, in bytes, of the resultant vint
	:type min_length: int
	:arg max_length: the maximum length, in bytes, of the vint storing the element size (defaults to :data:`EBMLMaxSizeLength`)
	:type max_length: int
	:returns: bytearray
	
	"""
	
	
	if size is not None:
		size_bits = bin(size).lstrip('-0b')
		size_bit_length = len(size_bits)
		length_required = (abs(size_bit_length - 1) // 7) + 1
		if size_bit_length % 7 == 0 and '1' in size_bits and '0' not in size_bits:
			length_required += 1
		length = max(length_required, min_length)
		
		alignment_bit_length = 0
		while ((length + alignment_bit_length + size_bit_length) // 8) < length:
			alignment_bit_length += 1
	else:
		length = min_length or 1
		required_bits = (length * 8) - length
		size_bit_length = required_bits
		size = (2**required_bits) - 1
		alignment_bit_length = 0
	
	if length > max_length:
		raise ValueError('Unable to encode size (%i) with length %i (longer than limit of %i)' % (size, length, max_length))
	
	data = bytearray(length)
	bytes_written = 0
	marker_written = False
	while bytes_written < length:
		index = (length - bytes_written) - 1
		if size:
			data[index] = size & 0b11111111
			size = size >> 8
			if not size and not size_bit_length % 8 == 0:
				if alignment_bit_length < (8 - (size_bit_length % 8)):
					mask = 0b10000000 >> ((length - 1) % 8)
					data[index] = data[index] | mask
					alignment_bit_length = 0
					marker_written = True
				else:
					alignment_bit_length -= (8 - (size_bit_length % 8))
			bytes_written += 1
		else:
			if alignment_bit_length:
				if alignment_bit_length < 8:
					data[index] = 0b10000000 >> ((length - 1) % 8)
					alignment_bit_length = 0
					bytes_written += 1
					marker_written = True
				else:
					data[index] = 0b00000000
					alignment_bit_length -= 8
					bytes_written += 1
			else:
				remaining_bytes = length - bytes_written
				if not marker_written:
					data[(remaining_bytes - 1)] = 0b00000001
					zero_range = range(0, (remaining_bytes - 1))
				else:
					zero_range = range(0, remaining_bytes)
				for index in zero_range:
					data[index] = 0b00000000
				bytes_written += remaining_bytes
	
	return data


def write_element_size(size, stream, min_length=None, max_length=EBMLMaxSizeLength):
	"""
	
	Write the size of an EBML element to stream, optionally with a minimum length.
	
	:arg size: the element size, or None if undefined
	:type size: int or None
	:arg min_length: the minimum length, in bytes, to write
	:type min_length: int
	:arg max_length: the maximum length, in bytes, to write (defaults to :data:`EBMLMaxSizeLength`)
	:type max_length: int
	:returns: None
	
	"""
	
	stream.write(encode_element_size(size, min_length, max_length))


def read_element_id(stream, max_length=EBMLMaxIDLength):
	"""
	
	Reads an EBML element ID vint from stream and returns a tuple containing:
	
		* the ID as an integer
		* the length in bytes of the ID descriptor (the vint) itself
	
	:arg stream: the source of the bytes
	:type stream: a file-like object
	:arg max_length: the maximum length, in bytes, of the vint storing the element ID (defaults to :data:`EBMLMaxIDLength`)
	:type max_length: int
	:returns: tuple
	
	"""
	
	vint_bytes = _read_vint_to_bytearray(stream, max_length)
	vint_len = len(vint_bytes)
	
	value = 0
	
	for vint_byte in vint_bytes:
		value = (value << 8) | vint_byte
	
	return value, vint_len


# def encode_element_id(class_id, max_length=EBMLMaxIDLength):
# 	length = int(((log(class_id, 2) - 1) // 7) + 1)
# 	
# 	if length > max_length:
# 		raise ValueError('Unable to encode ID (%x) with length %i (longer than limit of %i)' % (class_id, length, max_length))
# 	
# 	data = bytearray(length)
# 	
# 	bytes_written = 0
# 	while bytes_written < length:
# 		data[(length - bytes_written) - 1] = class_id & 0b11111111
# 		class_id >> 8
# 		bytes_written += 1
# 	
# 	return data
# 
# 
# def write_element_id(class_id, stream, max_length=EBMLMaxIDLength):
# 	stream.write(encode_element_id(class_id, max_length))


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