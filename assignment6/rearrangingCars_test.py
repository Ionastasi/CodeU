"""Tests for rearrangingCars."""

from rearrangingCars import rearrangingCars
import unittest
from itertools import permutations

def checkResult(initial, desired):
    """
    As long as the result is a little bit non-determinate, all we can do is just
    run the result and check, is the final state equal to desired.
    Thats what this function do.
    """
    moves = rearrangingCars(initial, desired)
    for m in moves:
        # we can only move the car to an empty slot
        if initial[m.destination]:
            return False
        initial[m.origin], initial[m.destination] = (initial[m.destination],
                                                        initial[m.origin])
    return initial == desired


class rearrangingCarsTest(unittest.TestCase):
    def testKnownCases(self):
        self.assertTrue(checkResult([1, 2, 0, 3], [3, 1, 2, 0]))
        self.assertTrue(checkResult([1, 2, 3, 0], [3, 1, 2, 0]))
        self.assertTrue(checkResult([3, 0, 1, 2], [0, 3, 2, 1]))

    def testEmptyCases(self):
        self.assertEqual(rearrangingCars([1, 2, 3, 4, 0], [1, 2, 3, 4, 0]), [])
        self.assertEqual(rearrangingCars([], []), [])
        self.assertEqual(rearrangingCars([0], [0]), [])

    def testAllCasesWithBruteForce(self):
        n = 5
        for inital in permutations(range(n)):
            for final in permutations(range(n)):
                self.assertTrue(checkResult(list(inital), list(final)))


if __name__ == '__main__':
    unittest.main()
