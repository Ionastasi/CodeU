"""Tests for wordSearch."""

from dictionary import Dictionary
from wordSearch import wordSearch
import unittest

class CommonAncestorTest(unittest.TestCase):
    def testBaseCases(self):
        grid = [['A', 'A', 'R'], ['T', 'C', 'D']]
        dictionary = Dictionary()
        dictionary.addWords(['CAR', 'CARD', 'CART', 'CAT'])
        self.assertEqual(wordSearch(len(grid), len(grid[0]), grid, dictionary),
                         {'CAR', 'CARD', 'CAT'})

        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        dictionary = Dictionary()
        dictionary.addWords(['ABA', 'abec', 'abcdefghi', 'abcfedghi', 'ihc',
                             'dbfh', 'abc', 'abcd', 'de', 'def'])
        self.assertEqual(wordSearch(len(grid), len(grid[0]), grid, dictionary),
                         {'abec', 'abcfedghi', 'dbfh', 'abc', 'de', 'def'})

    def testSpecialCases(self):
        grid1 = [['s', 'o', 'n']]
        grid2 = [['s'], ['o'], ['n']]
        grid3 = [['i']]
        dictionary = Dictionary()
        dictionary.addWords(['son', 'sun'])
        self.assertEqual(wordSearch(len(grid1), len(grid1[0]),
                                    grid1, dictionary), {'son'})
        self.assertEqual(wordSearch(len(grid2), len(grid2[0]),
                                    grid2, dictionary), {'son'})
        self.assertEqual(wordSearch(len(grid3), len(grid3[0]),
                                    grid3, dictionary), set())

        dictionary = Dictionary()
        dictionary.addWords(['i', 'ij', 'ji', 'abcd'])
        self.assertEqual(wordSearch(len(grid1), len(grid1[0]),
                                    grid1, dictionary), set())
        self.assertEqual(wordSearch(len(grid2), len(grid2[0]),
                                    grid2, dictionary), set())
        self.assertEqual(wordSearch(len(grid3), len(grid3[0]),
                                    grid3, dictionary), {'i'})

    def testEmptyGrid(self):
        dictionary = Dictionary()
        dictionary.addWords(['CAR', 'CARD', 'CART', 'CAT'])
        self.assertEqual(wordSearch(0, 0, [], dictionary), set())

    def testEmptyDict(self):
        grid = [['A', 'A', 'R'], ['T', 'C', 'D']]
        self.assertEqual(wordSearch(len(grid), len(grid[0]), grid,
                                    Dictionary()), set())

if __name__ == '__main__':
    unittest.main()
