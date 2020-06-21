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
            self.assertEqual(int(row['Result']), self.calculator.add(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_subtraction(self):
        test_data = CSVReader('Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(int(row['Result']), self.calculator.subtract(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_multiplication(self):
        test_data = CSVReader('Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(int(row['Result']), self.calculator.multiply(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_division(self):
        test_data = CSVReader('Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(float(row['Result']), self.calculator.divide(row['Value 1'], row['Value 2']))
            self.assertEqual(float(row['Result']), round(self.calculator.result, 9))

    def test_square(self):
        test_data = CSVReader('Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(int(row['Result']), self.calculator.sq(row['Value 1']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_square_root(self):
        test_data = CSVReader('Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(round(float(row['Result']), 8), self.calculator.sq_root(row['Value 1']))
            self.assertEqual(round(float(row['Result']), 8), round(self.calculator.result, 8))

    def test_results(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
