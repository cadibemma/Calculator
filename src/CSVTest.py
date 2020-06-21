import unittest
from CSVReader import CSVReader, class_factory


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.csv_reader = CSVReader('/src/Unit Test Addition.csv')
        
    def test_return_data_as_object(self):
        num = self.csv_reader.return_data_as_object('number')
        self.assertIsInstance(num, list)
        test_class = class_factory('number', self.csv_reader.data[0])
        for number in num:
            self.assertEqual(number.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
