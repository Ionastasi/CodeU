"""Tests for kthToLastInLinkedList()."""

from kthToLastInLinkedList import kthToLastInLinkedList, Node
import unittest

class kthToLastInLinkedListTest(unittest.TestCase):
    def _createReverseSequenceOfLength(self, n):
        head = Node(n - 1)
        prev = head
        for i in range(n - 2, -1, -1):
            new = Node(i)
            prev.next = new
            prev = new
        return head

    def setUp(self):
        self.n = 15
        self.head = self._createReverseSequenceOfLength(self.n)

    def testBaseCases(self):
        for i in range(self.n):
            self.assertEqual(i, kthToLastInLinkedList(self.head, i))

    def testSpecialCases(self):
        self.assertIsNone(kthToLastInLinkedList(self.head, -1))
        self.assertIsNone(kthToLastInLinkedList(self.head, self.n))
        self.assertIsNone(kthToLastInLinkedList(None, 0))

if __name__ == '__main__':
    unittest.main()
