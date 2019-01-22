import abc
from convertor.reader import *

class Ivalidator(CSVreader):
	"""docstring for Interface Ivalidator"""
	@abc.abstractmethod
	def non_ascci(self,mystring):
		pass
	@abc.abstractmethod
	def is_url(self,url_string):
		pass
	@abc.abstractmethod
	def is_rating_valid(self,rating=0):
		pass


		