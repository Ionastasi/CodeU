"""Tests for kthInLinkedList()."""

from kthInLinkedList import *
import unittest

class kthInLinkedListTest(unittest.TestCase):
    def setUp(self):
        self.n = 15
        self.head = Node(self.n - 1)
        prev = self.head
        for i in range(self.n - 2, -1, -1):
            new = Node(i)
            prev.next = new
            prev = new

    def testBaseCases(self):
        for i in range(self.n):
            self.assertEqual(i, kthInLinkedList(self.head, i))

    def testSpecialCases(self):
        self.assertIsNone(kthInLinkedList(self.head, -1))
        self.assertIsNone(kthInLinkedList(self.head, self.n))
        self.assertIsNone(kthInLinkedList(None, 0))

if __name__ == '__main__':
    unittest.main()
