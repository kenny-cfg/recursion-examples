import unittest

from string_combinations import string_combination


class TestStringCombinations(unittest.TestCase):
    def test_works_with_length_1(self):
        char_set = {'a', 'b', 'c'}
        expected = {'a', 'b', 'c'}

        result = string_combination(char_set, 1)

        self.assertEqual(expected, result)


"""
Return all possible combinations of strings of given length,
which can be formed from a set of supplied characters.

Input:
char_set = {'a', 'b'}, length = 3

Output:
aaa
aab
aba
abb
baa
bab
bba
bbb

NB: we cannot use itertools product or permutations functions.
"""
