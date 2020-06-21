import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(Calculator, self.calculator)

    def test_addition(self):
        self.assertEqual(3, self.calculator.add(1, 2))
        self.assertEqual(3, self.calculator.result)

    def test_something(self):
         self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
