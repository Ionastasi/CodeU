"""Tests for commonAncestor."""

from commonAncestor import commonAncestor
from binarytree import BinaryTree
import unittest

class CommonAncestorTest(unittest.TestCase):
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
        if self.assertEqual(self.bst.getSize(), 8):
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
        self.assertEqual(9, commonAncestor(self.bst, 5, 14))
        self.assertEqual(16, commonAncestor(self.bst, 1, 19))
        self.assertEqual(3, commonAncestor(self.bst, 1, 5))

    def testBaseCasesWithTree(self):
        self.assertEqual(7, commonAncestor(self.tree, 11, 3))
        self.assertEqual(2, commonAncestor(self.tree, 6, 4))
        self.assertEqual(6, commonAncestor(self.tree, 5, 11))

    def testSpecialCasesWithBST(self):
        self.assertEqual(5, commonAncestor(self.bst, 5, 5))
        self.assertEqual(16, commonAncestor(self.bst, 16, 16))
        self.assertEqual(18, commonAncestor(self.bst, 18, 18))
        self.assertEqual(9, commonAncestor(self.bst, 9, 5))
        self.assertEqual(16, commonAncestor(self.bst, 1, 16))
        self.assertEqual(18, commonAncestor(self.bst, 19, 18))

    def testSpecialCasesWithTree(self):
        self.assertEqual(9, commonAncestor(self.tree, 9, 9))
        self.assertEqual(2, commonAncestor(self.tree, 2, 2))
        self.assertEqual(4, commonAncestor(self.tree, 4, 4))
        self.assertEqual(7, commonAncestor(self.tree, 7, 11))
        self.assertEqual(2, commonAncestor(self.tree, 5, 2))
        self.assertEqual(6, commonAncestor(self.tree, 5, 6))

    def testNoneCases(self):
        self.assertIsNone(commonAncestor(self.bst, 1, 2))
        self.assertIsNone(commonAncestor(self.bst, 7, 3))
        self.assertIsNone(commonAncestor(self.bst, 42, 20))
        self.assertIsNone(commonAncestor(self.tree, 9, 10))
        self.assertIsNone(commonAncestor(self.tree, 13, 40))
        self.assertIsNone(commonAncestor(self.tree, 42, 56))
        self.assertIsNone(commonAncestor(self.tree, 33, 33))
        self.assertIsNone(commonAncestor(self.empty, 10, 12))


if __name__ == '__main__':
    unittest.main()
