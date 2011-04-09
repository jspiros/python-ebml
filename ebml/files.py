from .schema import *
from .core import read_element_id, read_element_size, read_int, read_uint, read_float, read_string, read_unicode, read_date


__all__ = ('EBMLFile', 'MatroskaFile')


TYPE_READERS = {
	INT: read_int,
	UINT: read_uint,
	FLOAT: read_float,
	STRING: read_string,
	UNICODE: read_unicode,
	DATE: lambda stream, size: read_date(stream)
}


class EBMLFileElement(object):
	def __init__(self, stream, schema, parent=None):
		self.stream = stream
		self.schema = schema
		self.parent = parent
		self.class_id, self.class_id_len = read_element_id(self.stream)
		try:
			self.element = schema.element_with_class_id(self.class_id)
		except:
			self.element = None
		else:
			if self.parent is None:
				if not self.element in self.schema.root_elements():
					self.element = None
			else:
				if not self.element in self.schema.child_elements_of_element(self.parent):
					self.element = None
		self.size, self.size_len = read_element_size(self.stream)
		self.offset = self.stream.tell()
		self._read_contents()
	
	def _read_contents(self):
		contents = None
		if self.element is not None:
			if self.element.data_type in TYPE_READERS:
				contents = TYPE_READERS[self.element.data_type](self.stream, self.size)
			elif self.element.data_type == CONTAINER:
				read_len = 0
				contents = []
				while self.size > read_len:
					sub_el = EBMLFileElement(self.stream, self.schema, self.element)
					read_len += (sub_el.class_id_len + sub_el.size_len + sub_el.size)
					contents.append(sub_el)
			else:
				self.stream.seek(self.offset + self.size, 0)
		else:
			self.stream.seek(self.offset + self.size, 0)
		self.contents = contents
	
	def pprint(self, indent=0):
		sargs = {
			'class_name': self.element.class_name or 'Unknown',
			'class_id': self.class_id,
			'size': self.size,
			'value': self.contents or None
		}
		def pprint_(foo):
			print ('\t' * indent) + foo
		if not self.contents:
			pprint_('<%(class_name)s id=\'%(class_id)x\' size=\'%(size)i\' />' % sargs)
		else:
			if self.element.data_type == CONTAINER:
				pprint_('<%(class_name)s id=\'%(class_id)x\' size=\'%(size)i\'>' % sargs)
				for sub_el in self.contents:
					sub_el.pprint(indent + 1)
				pprint_('</%(class_name)s>' % sargs)
			else:
				pprint_('<%(class_name)s id=\'%(class_id)x\' size=\'%(size)i\'>%(value)s</%(class_name)s>' % sargs)
	
	def __repr__(self):
		return '<%(class_name)s id=%(class_id)x size=%(size)i>' % {
			'class_name': self.element.class_name or '?',
			'class_id': self.element.class_id or self.class_id,
			'size': self.size
		}


class EBMLFile(object):
	default_schema = EBML
	
	def __init__(self, name_or_stream, schema=None):
		if schema is None:
			schema = self.default_schema
		self.schema = schema
		
		if isinstance(name_or_stream, basestring):
			self.stream = open(name_or_stream, 'rb')
		else:
			self.stream = name_or_stream
		
		self._read_contents()
	
	def _read_contents(self):
		self.contents = []
		while True:
			try:
				self.contents.append(EBMLFileElement(self.stream, self.schema, None))
			except:
				break
	
	def pprint(self):
		for el in self.contents:
			el.pprint()


class MatroskaFile(EBMLFile):
	default_schema = Matroska