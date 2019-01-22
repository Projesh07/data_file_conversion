
import unittest

from p_validator.validator import *
from convertor.reader import *
from convertor.data_convert import *	
class TestModule(unittest.TestCase):
	"""docstring for Testmodule"""

	def setUp(self):
		self.data_formate=DataFormate('app/test_file/test_hotels_data.csv')
		self.validate=Validate()

	def tearDown(self):
		pass	

	def test_xml_convert(self):

		self.data_formate=DataFormate('app/test_file/test_hotels_data.csv')	
		test=True
		if self.data_formate.xml_convert() is False:
			test=False
		self.assertEqual(test, True)

	def test_json_convert(self):

		test=True
		if self.data_formate.json_convert() is False:
			test=False
		self.assertEqual(test, True)

	def test_non_ascci(self):

		
		hotel_name='drom⇒'
		self.assertEqual(self.validate.non_ascci(hotel_name), True)

	def test_is_url(self):

		hotel_url='http://garden.com/'
		self.assertEqual(self.validate.is_url(hotel_url), True)

	def test_is_rating_valid(self):

		hotel_rating=0
		self.assertEqual(self.validate.is_rating_valid(hotel_rating), True)

	def test_csv_read_f(self):

		cv=CSVreader('app/test_file/test_hotels_data.csv','r')
		test=True

		if cv.csv_read_f() is False:
			test=False


		self.assertEqual(test, True)

	

if __name__ == '__main__':
	unittest.main()
