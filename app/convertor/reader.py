import csv
#Read data from csv
class CSVreader(object):
	"""docstring for CSVreader"""
	def __init__(self, file_to_read=None,file_open_mode=None):
		self.file_to_read = file_to_read
		self.file_mode=file_open_mode


	#Read csv file from given file path
	def csv_read_f(self):
		try:
			with open(self.file_to_read,self.file_mode) as file_context:
				csv_reader= csv.DictReader(file_context)
				data=list(csv_reader)
				return data
		except Exception as e:
			return False