"""Tests for findAncestors."""

from printAncestors import findAncestors
from binarytree import BinaryTree
import unittest

class PrintAncestorsTest(unittest.TestCase):
    def setUp(self):
        # Binary Search Tree
        self.bst = BinaryTree(16)
        self.bst.insert(9, 16, True)
        self.bst.insert(18, 16, False)
        self.bst.insert(19, 18, False)
        self.bst.insert(14, 9, False)
        self.bst.insert(3, 9, True)
        self.bst.insert(1, 3, True)
        self.bst.insert(5, 3, False)
        if self.bst.getSize() != 8:
            print("Some problems with Binary Search Tree.")
            raise

        # Ordinary Binary Tree
        self.tree = BinaryTree(2)
        self.tree.insert(7, 2, True)
        self.tree.insert(13, 2, False)
        self.tree.insert(9, 13, False)
        self.tree.insert(4, 9, True)
        self.tree.insert(3, 7, True)
        self.tree.insert(6, 7, False)
        self.tree.insert(5, 6, True)
        self.tree.insert(11, 6, False)
        if self.tree.getSize() != 9:
            print("Some problems with ordinary Binary Tree.")
            raise

        # Empty Tree
        self.empty = BinaryTree()

    def testBaseCasesWithBST(self):
        self.assertEqual([3, 9, 16], findAncestors(self.bst, 5))
        self.assertEqual([9, 16], findAncestors(self.bst, 14))
        self.assertEqual([18, 16], findAncestors(self.bst, 19))
        self.assertEqual([16], findAncestors(self.bst, 18))

    def testBaseCasesWithTree(self):
        self.assertEqual([6, 7, 2], findAncestors(self.tree, 11))
        self.assertEqual([7, 2], findAncestors(self.tree, 3))
        self.assertEqual([13, 2], findAncestors(self.tree, 9))
        self.assertEqual([2], findAncestors(self.tree, 7))

    def testSpecialCases(self):
        self.assertEqual([], findAncestors(self.bst, 16))
        self.assertEqual([], findAncestors(self.tree, 2))
        self.assertEqual([], findAncestors(self.bst, 20))
        self.assertEqual([], findAncestors(self.tree, 1))
        self.assertEqual([], findAncestors(self.empty, 10))


if __name__ == '__main__':
    unittest.main()
