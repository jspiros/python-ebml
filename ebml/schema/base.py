__all__ = ('INT', 'UINT', 'FLOAT', 'STRING', 'UNICODE', 'DATE', 'BINARY', 'CONTAINER', 'Element', 'EBML')


INT, UINT, FLOAT, STRING, UNICODE, DATE, BINARY, CONTAINER = range(0, 8)


class Element(object):
	class_id = None
	class_name = 'Unknown'
	class_parents = ()
	class_global = False
	class_root = False
	data_type = BINARY


class EBMLElement(Element):
	class_id = 0x1A45DFA3
	class_name = 'EBML'
	class_root = True
	data_type = CONTAINER


class EBMLVersionElement(Element):
	class_id = 0x4286
	class_name = 'EBMLVersion'
	class_parents = (EBMLElement,)
	data_type = UINT


class EBMLReadVersionElement(Element):
	class_id = 0x42F7
	class_name = 'EBMLReadVersion'
	class_parents = (EBMLElement,)
	data_type = UINT


class EBMLMaxIDLengthElement(Element):
	class_id = 0x42F2
	class_name = 'EBMLMaxIDLength'
	class_parents = (EBMLElement,)
	data_type = UINT


class EBMLMaxSizeLengthElement(Element):
	class_id = 0x42F3
	class_name = 'EBMLMaxSizeLength'
	class_parents = (EBMLElement,)
	data_type = UINT


class DocTypeElement(Element):
	class_id = 0x4282
	class_name = 'DocType'
	class_parents = (EBMLElement,)
	data_type = STRING


class DocTypeVersionElement(Element):
	class_id = 0x4287
	class_name = 'DocTypeVersion'
	class_parents = (EBMLElement,)
	data_type = UINT


class DocTypeReadVersionElement(Element):
	class_id = 0x4285
	class_name = 'DocTypeReadVersion'
	class_parents = (EBMLElement,)
	data_type = UINT


class CRC32Element(Element):
	class_id = 0xBF
	class_name = 'CRC-32'
	class_global = True
	data_type = BINARY


class VoidElement(Element):
	class_id = 0xEC
	class_name = 'Void'
	class_global = True
	data_type = BINARY


class SignatureSlotElement(Element):
	class_id = 0x1B538667
	class_name = 'SignatureSlot'
	class_global = True
	data_type = CONTAINER


class SignatureAlgoElement(Element):
	class_id = 0x7E8A
	class_name = 'SignatureAlgo'
	class_parents = (SignatureSlotElement,)
	data_type = UINT


class SignatureHashElement(Element):
	class_id = 0x7E9A
	class_name = 'SignatureHash'
	class_parents = (SignatureSlotElement,)
	data_type = UINT


class SignaturePublicKeyElement(Element):
	class_id = 0x7EA5
	class_name = 'SignaturePublicKey'
	class_parents = (SignatureSlotElement,)
	data_type = BINARY


class SignatureElement(Element):
	class_id = 0x7EB5
	class_name = 'Signature'
	class_parents = (SignatureSlotElement,)
	data_type = BINARY


class SignatureElementsElement(Element):
	class_id = 0x7E5B
	class_name = 'SignatureElements'
	class_parents = (SignatureSlotElement,)
	data_type = CONTAINER


class SignatureElementListElement(Element):
	class_id = 0x7E7B
	class_name = 'SignatureElementList'
	class_parents = (SignatureElementsElement,)
	data_type = CONTAINER


class SignedElementElement(Element):
	class_id = 0x6532
	class_name = 'SignedElement'
	class_parents = (SignatureElementListElement,)
	data_type = BINARY


class Schema(object):
	doc_type = None
	version = None
	elements_by_class_id = None
	
	@classmethod
	def element_with_class_id(cls, class_id):
		if cls.elements_by_class_id is None:
			cls.elements_by_class_id = {}
			for element in cls.elements:
				cls.elements_by_class_id[element.class_id] = element
		return cls.elements_by_class_id[class_id]
	
	@classmethod
	def global_elements(cls):
		return [element for element in cls.elements if element.class_global]
	
	@classmethod
	def root_elements(cls):
		return [element for element in cls.elements if element.class_root]
	
	@classmethod
	def child_elements_of_element(cls, parent):
		children = [element for element in cls.elements if parent in element.class_parents]
		children += cls.global_elements()
		if 'self' in parent.class_parents and parent not in children:
			children.append(parent)
		return children


class EBML(Schema):
	elements = (
		EBMLElement,
		EBMLVersionElement,
		EBMLReadVersionElement,
		EBMLMaxIDLengthElement,
		EBMLMaxSizeLengthElement,
		DocTypeElement,
		DocTypeVersionElement,
		DocTypeReadVersionElement,
		CRC32Element,
		VoidElement,
		SignatureSlotElement,
		SignatureAlgoElement,
		SignatureHashElement,
		SignaturePublicKeyElement,
		SignatureElement,
		SignatureElementsElement,
		SignatureElementListElement,
		SignedElementElement
	)