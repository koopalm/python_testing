import unittest
import FizzBuzz.FizzBuzz as FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_dived_by_3(self):
        number = 3
        excepted_result = "Fizz"
        result = FizzBuzz.FizzBuzz(number)
        self.assertEqual(result, excepted_result)

    def test_dived_by_5(self):
        number = 5
        excepted_result = "Buzz"
        result = FizzBuzz.FizzBuzz(number)
        self.assertEqual(result, excepted_result)
    
    def test_dived_by_5_and_3(self):
        number = 15
        excepted_result = "FizzBuzz"
        result = FizzBuzz.FizzBuzz(number)
        self.assertEqual(result, excepted_result)

    def test_not_dived_by_5_or_3(self):
        number = 2
        excepted_result = 2
        result = FizzBuzz.FizzBuzz(number)
        self.assertEqual(result, excepted_result)

if __name__ == "__main__":
    unittest.main()