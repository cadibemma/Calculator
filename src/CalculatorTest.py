import unittest
from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CSVReader('Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(int(row['Result']), self.calculator.add(int(row['Value 1']), int(row['Value 2'])))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_results(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
