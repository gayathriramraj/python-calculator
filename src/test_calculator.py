
import unittest
from calculator import calculator

class TestCalculator(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(calculator("add", 2, 3), 5)

	def test_subtraction(self):
		self.assertEqual(calculator("subtract", 5, 3), 2)

	def test_invalid_operation(self):
		with self.assertRaises(ValueError):
			calculator("modulo", 2, 3)
#write one more test for addition with negative numbers.
	def test_addition_with_negative_numbers(self):
		self.assertEqual(calculator("add", -2, -3), -5)
		self.assertEqual(calculator("add", -2, 3), 1)
		self.assertEqual(calculator("add", 2, -3), -1)
#write one more test for subtraction with negative numbers.
	def test_subtraction_with_negative_numbers(self):
		self.assertEqual(calculator("subtract", -5, -3), -2)
		self.assertEqual(calculator("subtract", -5, 3), -8)
		self.assertEqual(calculator("subtract", 5, -3), 8)
        


#write test for multiplication.
	def test_multiplication(self):
		self.assertEqual(calculator("multiply", 2, 3), 6)
		self.assertEqual(calculator("multiply", -2, 3), -6)
		self.assertEqual(calculator("multiply", -2, -3), 6)

#write test for division.
	def test_division(self):
		self.assertEqual(calculator("divide", 6, 3), 2)
		self.assertEqual(calculator("divide", -6, 3), -2)
		self.assertEqual(calculator("divide", -6, -3), 2)

#write test for division by zero.
	def test_division_by_zero(self):
		with self.assertRaises(ValueError):
			calculator("divide", 6, 0)

if __name__ == "__main__":
	unittest.main()