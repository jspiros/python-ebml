import abc
try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO
from ..core import *


__all__ = ('UnknownElement', 'Element', 'Document', 'INT', 'UINT', 'FLOAT', 'STRING', 'UNICODE', 'DATE', 'BINARY', 'CONTAINER')


INT, UINT, FLOAT, STRING, UNICODE, DATE, BINARY, CONTAINER = range(0, 8)


READERS = {
	INT: read_signed_integer,
	UINT: read_unsigned_integer,
	FLOAT: read_float,
	STRING: read_string,
	UNICODE: read_unicode_string,
	DATE: read_date,
	BINARY: lambda stream, size: bytearray(stream.read(size))
}


ENCODERS = {
	INT: encode_signed_integer,
	UINT: encode_unsigned_integer,
	FLOAT: encode_float,
	STRING: encode_string,
	UNICODE: encode_unicode_string,
	DATE: encode_date,
	BINARY: lambda binary, length: binary
}


VALIDATORS = {
	INT: lambda value: True if isinstance(value, (int, long)) else False,
	UINT: lambda value: True if isinstance(value, (int, long)) and value == abs(value) else False,
	FLOAT: lambda value: True if isinstance(value, float) else False,
	STRING: lambda value: True if isinstance(value, str) else False,
	UNICODE: lambda value: True if isinstance(value, basestring) else False,
	DATE: lambda value: True if isinstance(value, datetime.datetime) else False,
	BINARY: lambda value: True if isinstance(value, (str, bytes, bytearray)) else False
}


class BaseElement(object):
	__metaclass__ = abc.ABCMeta
	
	id = abc.abstractproperty()
	name = abc.abstractproperty()
	type = abc.abstractproperty()
	default = None
	children = ()
	mandatory = False
	multiple = False


class UnknownElement(BaseElement):
	id = None
	name = 'Unknown'
	type = BINARY
	
	def __init__(self, id, encoding):
		self.id = id
		self.encoding = encoding


def read_elements(stream, size, document, children):
	elements = []
	while (size if size is not None else True):
		try:
			element_id, element_id_size = read_element_id(stream)
			element_size, element_size_size = read_element_size(stream)
			element_encoding = (element_size, bytearray(stream.read(element_size)))
		except:
			break
		else:
			element_class = None
			for child in (children + document.globals):
				if child.id == element_id:
					element_class = child
					break
			if element_class is None:
				element = UnknownElement(element_id, element_encoding)
			else:
				element = element_class(document, encoding=element_encoding)
			elements.append(element)
			if size is not None:
				size -= element_id_size + element_size_size + element_size
	return elements


class Element(BaseElement):
	@classmethod
	def check_value(cls, value):
		if cls.type in VALIDATORS:
			return VALIDATORS[cls.type](value)
		elif cls.type == CONTAINER:
			if isinstance(value, (list, tuple)):
				for item in value:
					if not isinstance(value, Element):
						return False
				return True
			elif isinstance(value, Element):
				return True
			else:
				return False
		else:
			raise NotImplementedError('Unsupported element type.')
	
	def __init__(self, document, value=None, encoding=None):
		self.document = document
		self._value = value
		self._encoding = encoding
	
	@property
	def value(self):
		if self._value is None and self._encoding is not None:
			if self.type in READERS:
				self._value = READERS[self.type](StringIO(self._encoding[1]), self._encoding[0])
			elif self.type == CONTAINER:
				self._value = read_elements(StringIO(self._encoding[1]), self._encoding[0], self.document, self.children)
		return self._value
	
	@value.setter
	def set_value(self, value):
		if not self.check_value(value):
			raise ValueError('Unsupported element value.')
		self._value = value
		self._encoding = None
	
	@property
	def encoding(self):
		if self._encoding is None:
			size = 0
			data = bytearray()
			if self._value is not None:
				if self.type in ENCODERS:
					data = ENCODERS[self.type](self._value)
					size = len(data)
				elif self.type == CONTAINER:
					for element in self._value:
						size += element.size
						data.extend(element.encoding[1])
			self._encoding = (size, data)
		return self._encoding
	
	@property
	def id_size(self):
		return len(encode_element_id(self.id))
	
	@property
	def size_size(self):
		return len(encode_element_size(self.body_size))
	
	@property
	def head_size(self):
		return self.id_size + self.size_size
	
	@property
	def body_size(self):
		return self.encoding[0]
	
	@property
	def size(self):
		return self.head_size + self.body_size


class Document(object):
	__metaclass__ = abc.ABCMeta
	
	type = abc.abstractproperty()
	version = abc.abstractproperty()
	children = ()
	globals = ()
	
	def __init__(self, stream):
		self.stream = stream
		self._roots = None
	
	@property
	def roots(self):
		if self._roots is None:
			self._roots = read_elements(self.stream, None, self, self.children)
		return self._roots