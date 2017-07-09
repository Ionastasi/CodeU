"""Tests for countingIslands."""

from disjointset import DisjointSet
from countingIslands import countingIslands
import unittest

class countingIslandsTest(unittest.TestCase):
    def testBaseCases(self):
        islandsMap = [[False, True,  False, True],
                      [True,  True,  False, False],
                      [False, False, True,  False],
                      [False, False, True,  False]]
        self.assertEqual(countingIslands(islandsMap), 3)
        islandsMap = [[False, True, False],
                      [True,  True, True],
                      [False, True, False]]
        self.assertEqual(countingIslands(islandsMap), 1)
        islandsMap = [[False, True,  False],
                      [True,  False, True]]
        self.assertEqual(countingIslands(islandsMap), 3)
        islandsMap = [[True,  False, False, True,  True,  True,  False],
                      [False, True,  True,  True,  False, True,  False],
                      [True,  False, False, False, True,  True,  False],
                      [True,  False, True,  False, True,  False, True],
                      [False, True,  True,  True,  True,  False, True],
                      [True,  False, False, False, False, True,  False],
                      [False, False, True,  True,  True,  False, False]]
        self.assertEqual(countingIslands(islandsMap), 7)

    def testZeroCases(self):
        self.assertEqual(countingIslands([]), 0)
        islandsMap = [[False, False], [False, False]]
        self.assertEqual(countingIslands(islandsMap), 0)

    def testOneDimensionCases(self):
        islandsMap = [[False, True, True, False]]
        self.assertEqual(countingIslands(islandsMap), 1)
        islandsMap = [[False], [True], [True], [False]]
        self.assertEqual(countingIslands(islandsMap), 1)

if __name__ == '__main__':
    unittest.main()
