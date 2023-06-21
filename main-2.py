#Бабкин Даниил Группа 44-22-114 Вариант 2 Задание 2
import unittest

class CalculationTest(unittest.TestCase):
    def test_case_x_greater_than_1(self):
        result = calculate_value(2)
        self.assertEqual(result, 1 / (2 - 1))

    def test_case_x_less_than_or_equal_to_1(self):
        result = calculate_value(0.5)
        self.assertEqual(result, 2 * math.sin(3.14 + 0.5) ** 3)

if __name__ == '__main__':
    unittest.main()