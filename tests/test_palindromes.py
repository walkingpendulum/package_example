from unittest import TestCase
from palindrome_checker.core import is_palindrome


class StrCheck(TestCase):
    def test_empty(self):
        self.assertTrue(is_palindrome(''))

    def test_palindromes(self):
        self.assertTrue(is_palindrome('abacaba'))
        self.assertTrue(is_palindrome('Step on no pets'))
        self.assertTrue(is_palindrome('Mr. Owl ate my metal worm!!'))

        self.assertFalse(is_palindrome('A rose is a rose is a rose is a rose'))
