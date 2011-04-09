from xml.etree.ElementTree import parse as parse_xml
from .base import INT, UINT, FLOAT, STRING, UNICODE, DATE, BINARY, CONTAINER, Element, Schema


SPECDATA_TYPES = {
	'integer': INT,
	'uinteger': UINT,
	'float': FLOAT,
	'string': STRING,
	'utf-8': UNICODE,
	'date': DATE,
	'binary': BINARY,
	'master': CONTAINER
}


def parse_specdata(source, schema_name):
	"""
	
	Reads a schema specification from a file (e.g., specdata.xml) or file-like object, and returns a tuple containing:
	
		* a mapping of class names to Element subclasses
		* a Schema subclass
	
	:arg source: the file or file-like object
	:type source: str or file-like object
	:arg schema_name: the name of the schema
	:type schema_name: str
	:returns: tuple
	
	"""
	
	tree = parse_xml(source)
	elements = {}
	parent_elements = []
	
	for element_element in tree.getiterator('element'):
		raw_attrs = element_element.attrib
		
		element_name = '%sElement' % raw_attrs.get('cppname', raw_attrs.get('name'))
		element_level = int(raw_attrs['level'])
		element_attrs = {
			'__module__': None,
			'class_id': int(raw_attrs['id'], 0),
			'class_name': raw_attrs['name'],
			'data_type': SPECDATA_TYPES[raw_attrs['type']]
		}
		
		while parent_elements and element_level <= parent_elements[-1][0]:
			parent_elements.pop()
		
		if element_level == -1:
			element_attrs['class_global'] = True
			parent_elements = []
		elif element_level == 0:
			element_attrs['class_root'] = True
			parent_elements = []
		else:
			if raw_attrs.get('recursive', '0') == '1':
				element_attrs['class_parents'] = (parent_elements[-1][1], 'self')
			else:
				element_attrs['class_parents'] = (parent_elements[-1][1],)
		
		element = type(element_name, (Element,), element_attrs)
		elements[element_name] = element
		parent_elements.append((element_level, element))
	
	schema_attrs = {
		'__module__': None,
		'elements': tuple(elements.values())
	}
	schema = type(schema_name, (Schema,), schema_attrs)
	
	return elements, schema