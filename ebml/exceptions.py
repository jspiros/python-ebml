class EBMLException(Exception):
	pass

class ParseError(EBMLException):
	pass

class ReservedElementIDError(EBMLException):
	pass