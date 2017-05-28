"""Tests for isPermutation()."""

from isPermutation import isPermutation
import unittest

class isPermutationTest(unittest.TestCase):
    def testBaseCases(self):
        self.assertTrue(isPermutation("Listen", "Silent"))
        self.assertTrue(isPermutation("Triangle", "Integral"))
        self.assertFalse(isPermutation("Apple", "Pabble"))
        self.assertTrue(isPermutation("aaa", "aaa"))
        self.assertFalse(isPermutation("aaa", "aaaa"))
        self.assertTrue(isPermutation("ABC", "abc"))

    def testSpecialCases(self):
        self.assertFalse(isPermutation("abcd", ""))
        self.assertTrue(isPermutation("", ""))
        self.assertFalse(isPermutation(None, "frfr"))
        self.assertFalse(isPermutation("", None))
        self.assertFalse(isPermutation(None, None))


if __name__ == '__main__':
    unittest.main()
