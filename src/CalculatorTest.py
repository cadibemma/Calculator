import unittest
from Calculator import Calculator
from CSVReader import CSVReader


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data_a = CSVReader('/src/Unit Test Addition.csv').data
        for row in test_data_a:
            self.assertEqual(int(row['Result']), self.calculator.add(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_subtraction(self):
        test_data_s = CSVReader('/src/Unit Test Subtraction.csv').data
        for row in test_data_s:
            self.assertEqual(int(row['Result']), self.calculator.subtract(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_multiplication(self):
        test_data_m = CSVReader('/src/Unit Test Multiplication.csv').data
        for row in test_data_m:
            self.assertEqual(int(row['Result']), self.calculator.multiply(row['Value 1'], row['Value 2']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_division(self):
        test_data_d = CSVReader('/src/Unit Test Division.csv').data
        for row in test_data_d:
            self.assertEqual(float(row['Result']), self.calculator.divide(row['Value 1'], row['Value 2']))
            self.assertEqual(float(row['Result']), round(self.calculator.result, 9))

    def test_square(self):
        test_data_sq = CSVReader('/src/Unit Test Square.csv').data
        for row in test_data_sq:
            self.assertEqual(int(row['Result']), self.calculator.sq(row['Value 1']))
            self.assertEqual(int(row['Result']), self.calculator.result)

    def test_square_root(self):
        test_data_sqrt = CSVReader('/src/Unit Test Square Root.csv').data
        for row in test_data_sqrt:
            self.assertEqual(round(float(row['Result']), 8), self.calculator.sq_root(row['Value 1']))
            self.assertEqual(round(float(row['Result']), 8), round(self.calculator.result, 8))

    def test_results(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
