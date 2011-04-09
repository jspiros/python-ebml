import os.path
from .specs import parse_specdata


_Elements, Matroska = parse_specdata(os.path.join(os.path.dirname(__file__), 'matroska.xml'), 'Matroska')


for name, element in _Elements.iteritems():
	globals()[name] = element