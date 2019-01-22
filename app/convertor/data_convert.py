
import re
from convertor.reader import *
from p_validator.validator import *	
from interfaces.idata_convertion import *
import sys
import os

#Write Data in different formate Json and xml
class DataFormate(IdataConvert):
	"""docstring for ClassName"""
	def __init__(self,path):

		self.path = path
		super(DataFormate,self).__init__(self.path,'r')
				
	#Converting data into xml formate
	def xml_convert(self):
		xmlFile =os.path.join(self.path.split(".")[0]+'.xml')


		try:
			success="file is converted into xml please check the directory {}".format(xmlFile)
			print(success)
			content=super(DataFormate,self).csv_read_f()
			with open(xmlFile, 'w') as xmlData:
				xmlData.write('<?xml version="1.0"?>' + "\n")
				xmlData.write('<hotel_data>' + "\n")
				for c in content:
					xmlData.write('<hotel>' + "\n")
					for i in c:		
						if i !='':
							xmlData.write('    ' + '<' + i + '>'+ c[i] + '</' + i + '>' + "\n")

					xmlData.write('<hotel>' + "\n")
				xmlData.write('<hotel_data>' + "\n")

			
		except Exception as e:
			print('file conversion failed '+ e)
			
			return False

	#Converting data into Josn formate
	def json_convert(self):
		jsonFile =os.path.join(self.path.split(".")[0]+'.json')


		try:
			success="file is converted into json please check the directory {}".format(jsonFile)
			print(success)
			content=super(DataFormate,self).csv_read_f()
			with open(jsonFile, 'w') as jsonData:
				jsonData.write('{"hotel_data":[' + "\n")
				for c in content:
					json.dump(c, jsonData,ensure_ascii=False)
					if c is content[-1]: 
						jsonData.write("\n")						
					else:
						
						jsonData.write(",\n")
				jsonData.write(']}' + "\n")
			
		except Exception as e:
			print('file conversion failed')
			
			return False

	
	#Closure and anonymus lamda used 
	def convert_type(self):

		# convert=lambda convert_type: self.xml_convert() if convert_type  == 'xml'	 if convert_type=='json' else False
		def convert(c_type):
			if c_type  == 'xml':
				self.xml_convert()
				return True
			elif c_type=='json':
				self.json_convert()
				return True
			else:
				return False				
			
		return convert	