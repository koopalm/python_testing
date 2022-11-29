import unittest
import words.words as words

class TestWords(unittest.TestCase):

    def test_reverse_words_longer_than_five(self):
        word = "Pluto"
        expected_result = "otulP"
        result = words.reverse_words(word)
        self.assertEqual(result, expected_result)

    def test_cap_two_letters(self):
        word = "is"
        expected_result = "IS"
        result = words.reverse_words(word)
        self.assertEqual(result, expected_result)
    




if __name__ == "__main__":
    unittest.main()