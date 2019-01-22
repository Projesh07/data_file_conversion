import os
from convertor.data_convert import *	

path = input('enter file to read ')
# current=os.getcwd()
path=str(path)
# path=os.path.join(current+'/app/'+path)
# print(path)
if os.path.exists(path):
	convert_type=input('please insert the conversion type xml / json')
	convert_type=str(convert_type).strip()
	csv_read=DataFormate(path)

	content=csv_read.convert_type()

	if content(convert_type):
		pass
		
	else:
		print ("Conversion type not implemented yet.")
			
else:
	print ("Directory/ file not exists.")