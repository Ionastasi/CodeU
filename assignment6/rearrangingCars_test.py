"""Tests for rearrangingCars."""

from rearrangingCars import Move, rearrangingCars
import unittest

class rearrangingCarsTest(unittest.TestCase):
    def testBaseCases(self):
        self.assertEqual(rearrangingCars([1, 2, 0, 3], [3, 1, 2, 0]),
                    [Move(1, 2), Move(0, 1), Move(3, 0)])
        self.assertEqual(rearrangingCars([1, 2, 3, 0], [3, 1, 2, 0]),
                    [Move(0, 3), Move(2, 0), Move(1, 2), Move(3, 1)])
        self.assertEqual(rearrangingCars([1, 2, 3, 4, 5, 0], [1, 2, 3, 4, 5, 0]),
                    [])

    def testCornerCases(self):
        self.assertEqual(rearrangingCars([], []), [])
        self.assertEqual(rearrangingCars([0], [0]), [])


if __name__ == '__main__':
    unittest.main()
