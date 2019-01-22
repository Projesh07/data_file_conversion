import re
import json
from interfaces.ivalidator import *


#Perform validation 
class Validate(Ivalidator):
	"""docstring for Validate"""
	def __init__(self):
		super(Validate,self).__init__('hotels.csv','r')

	#Check name contain any non asccii values
	def non_ascci(self,mystring):

		for c in mystring:

			if 0 >= ord(c) or ord(c) >= 127:
				return True

		return False

	#Check url is valid or not
	def is_url(self,url_string):
		regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		if re.match(regex, url_string) is not None:
			return True
		return False
	#Check validation	
	def is_rating_valid(self,rating=0):
	        try:
	            val = rating
	            if val >= 0 and val <6:
	                return True
	            else:
	                return False
	        except ValueError:
	            return False
	#Removing non ascii values if any contains
	def removeNonAscii(self,s): 
		return "".join(filter(lambda x: ord(x)<128, s))