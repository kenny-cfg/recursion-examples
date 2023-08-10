import unittest

from string_combinations import string_combination


class TestStringCombinations(unittest.TestCase):
    def test_works_with_length_1(self):
        char_set = {'a', 'b', 'c'}
        expected = {'a', 'b', 'c'}

        result = string_combination(char_set, 1)

        self.assertEqual(expected, result)

    def test_works_with_length_3(self):
        char_set = {'a', 'b'}
        expected = {
            'aaa',
            'aab',
            'aba',
            'abb',
            'baa',
            'bab',
            'bba',
            'bbb'
        }

        result = string_combination(char_set, 3)

        self.assertEqual(expected, result)
