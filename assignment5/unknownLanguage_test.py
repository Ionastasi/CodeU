"""Tests for unknownLanguage."""

from unknownLanguage import unknownLanguage
import unittest

class UnknownLanguageTest(unittest.TestCase):
    def testEqualLenghtCases(self):
        self.assertEqual(unknownLanguage(["TAR", "ART", "RAT", "CAT", "CAR"]),
                         ['T', 'A', 'R', 'C'])
        self.assertIn(unknownLanguage(["ART", "RAT", "CAT", "CAR"]),
                      [['A', 'T', 'R', 'C'],
                       ['T', 'A', 'R', 'C']])
        self.assertIn(unknownLanguage(["QHS", "QST", "OOQ", "OTS",
                                       "NTO", "NTS", "SNS", "TNS"]),
                      [['Q', 'H', 'O', 'N', 'S', 'T'],
                       ['Q', 'H', 'O', 'S', 'N', 'T'],
                       ['H', 'Q', 'O', 'N', 'S', 'T'],
                       ['H', 'Q', 'O', 'S', 'N', 'T']])

    def testDifferentLengthCase(self):
        self.assertEqual(unknownLanguage(["a", "ab", "ac", "bca", "bcad",
                                          "bcd", "cdba", "cdc", "daac"]),
                         ['a', 'b', 'c', 'd'])
        self.assertIn(unknownLanguage(["a", "dad", "ba", "bad", "bac", ""]),
                      [['a', 'd', 'c', 'b'],
                       ['a', 'd', 'b', 'c'],
                       ['d', 'a', 'c', 'b'],
                       ['d', 'a', 'b', 'c']])

    def testErrorCase(self):
        with self.assertRaises(ValueError):
            unknownLanguage(['ad', 'aa', 'b', 'c', 'd'])

    def testEmptyInputCase(self):
        self.assertEqual(unknownLanguage([]), [])


if __name__ == '__main__':
    unittest.main()
