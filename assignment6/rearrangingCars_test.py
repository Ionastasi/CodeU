"""Tests for rearrangingCars."""

from rearrangingCars import rearrangingCars
import unittest

def checkResult(initialState, desiredState):
    moves = rearrangingCars(initialState.copy(), desiredState)
    for m in moves:
        # we can only move the car to an empty slot
        if initialState[m._to]:
            return False
        initialState[m._from], initialState[m._to] = (initialState[m._to],
                                                      initialState[m._from])
    return initialState == desiredState


class rearrangingCarsTest(unittest.TestCase):
    def testBaseCases(self):
        # As long as the result is a little bit non-determinate, all we can do
        # is just run the result and check, is the finsl state equal to desired.
        # Helper-function checkRusult uses for this.
        self.assertTrue(checkResult([1, 2, 0, 3], [3, 1, 2, 0]))
        self.assertTrue(checkResult([1, 2, 3, 0], [3, 1, 2, 0]))
        self.assertTrue(checkResult([3, 0, 1, 2], [0, 3, 2, 1]))

    def testEmptyCases(self):
        self.assertEqual(rearrangingCars([1, 2, 3, 4, 0], [1, 2, 3, 4, 0]), [])
        self.assertEqual(rearrangingCars([], []), [])
        self.assertEqual(rearrangingCars([0], [0]), [])


if __name__ == '__main__':
    unittest.main()
