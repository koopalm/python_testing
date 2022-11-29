import unittest
import calculator.calculator as calculator


class TestCalculator(unittest.TestCase):

    def test_plus_integerit(self):
        luku1 = luku2 = 2
        excepted_result = 4
        result = calculator.plus(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_plus_negatiiviset_numerot(self):
        luku1 = luku2 = -2
        excepted_result = -4
        result = calculator.plus(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_plus_floatit(self):
        luku1 = luku2 = 2.21
        excepted_result = 4.42
        result = calculator.plus(luku1, luku2)
        self.assertEqual(result, excepted_result)
    
    def test_plus_float_ja_integer(self):
        luku1 = 1
        luku2 = 2.21
        excepted_result = 3.21
        result = calculator.plus(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_plus(self):
        luku1 = luku2 = 2.41
        excepted_result = 4.82
        result = calculator.plus(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_sum_numbers_takes_rises_error_if_parameters_are_not_numbers(self):
        with self.assertRaises(TypeError):
            calculator.plus(1, "a")

    def test_miinus(self):
        luku1 = 3
        luku2 = 2
        excepted_result = 1
        result = calculator.miinus(luku1, luku2)
        self.assertAlmostEqual(result, excepted_result)

    def test_miinus_liukuluku(self):
        luku1 = 3.1
        luku2 = 3.2
        excepted_result = -0.1
        result = calculator.miinus(luku1, luku2)
        self.assertAlmostEqual(result, excepted_result)

    def test_jako(self):
        luku1 = luku2 = 2
        excepted_result = 1
        result = calculator.jako(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_jako_liukuluvut(self):
        luku1 = 2.4
        luku2 = 2.1
        excepted_result = 2.4/2.1
        result = calculator.jako(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_jako_nollalla(self):
        luku1 = 2
        luku2 = 0
        excepted_result = None
        result = calculator.jako(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_kerto(self):
        luku1 = luku2 = 2
        excepted_result = 4
        result = calculator.kerto(luku1, luku2)
        self.assertEqual(result, excepted_result)

    def test_kerto_liukuluvut(self):
        luku1 = luku2 = 2.5
        excepted_result = 6.25
        result = calculator.kerto(luku1, luku2)
        self.assertEqual(result, excepted_result)


if __name__ == "__main__":
    unittest.main()

#python -m unittest
#python -m unittest -v