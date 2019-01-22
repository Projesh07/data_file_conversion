import abc
from convertor.reader import *
class IdataConvert(abc.ABC,CSVreader):
	"""docstring for Interface IdataConvert"""
	@abc.abstractmethod
	def xml_convert(self):
		pass
	@abc.abstractmethod
	def json_convert(self):
		pass

		