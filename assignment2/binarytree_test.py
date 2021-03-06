"""Tests for class BinaryTree"""

from binarytree import BinaryTree
import unittest

class BinaryTreeTest(unittest.TestCase):
    def testBST(self):  # Binary Search Tree
        bst = BinaryTree(16)
        bst.insert(9, 16, True)
        bst.insert(18, 16, False)
        bst.insert(19, 18, False)
        bst.insert(14, 9, False)
        bst.insert(3, 9, True)
        bst.insert(1, 3, True)
        bst.insert(5, 3, False)
        root = bst.getRoot()
        self.assertEqual(8, bst.getSize())
        self.assertEqual(16, root.key)
        self.assertEqual(18, root.right.key)
        self.assertEqual(19, root.right.right.key)
        self.assertEqual(9,  root.left.key)
        self.assertEqual(14, root.left.right.key)
        self.assertEqual(3,  root.left.left.key)
        self.assertEqual(1,  root.left.left.left.key)
        self.assertEqual(5,  root.left.left.right.key)
        self.assertTrue(bst.find(16))
        self.assertTrue(bst.find(18))
        self.assertTrue(bst.find(19))
        self.assertTrue(bst.find(14))
        self.assertTrue(bst.find(3))
        self.assertTrue(bst.find(1))
        self.assertTrue(bst.find(5))
        self.assertFalse(bst.find(10))
        self.assertFalse(bst.find(42))
        self.assertFalse(bst.find(2))

    def testTree(self):  # Ordinary Binary Tree
        tree = BinaryTree(2)
        tree.insert(7, 2, True)
        tree.insert(13, 2, False)
        tree.insert(9, 13, False)
        tree.insert(4, 9, True)
        tree.insert(3, 7, True)
        tree.insert(6, 7, False)
        tree.insert(5, 6, True)
        tree.insert(11, 6, False)
        root = tree.getRoot()
        self.assertEqual(9, tree.getSize())
        self.assertEqual(2, root.key)
        self.assertEqual(13, root.right.key)
        self.assertEqual(9, root.right.right.key)
        self.assertEqual(4, root.right.right.left.key)
        self.assertEqual(7, root.left.key)
        self.assertEqual(3, root.left.left.key)
        self.assertEqual(6, root.left.right.key)
        self.assertEqual(5, root.left.right.left.key)
        self.assertEqual(11, root.left.right.right.key)
        self.assertTrue(tree.find(2))
        self.assertTrue(tree.find(13))
        self.assertTrue(tree.find(9))
        self.assertTrue(tree.find(4))
        self.assertTrue(tree.find(7))
        self.assertTrue(tree.find(3))
        self.assertTrue(tree.find(6))
        self.assertTrue(tree.find(5))
        self.assertTrue(tree.find(11))
        self.assertFalse(tree.find(10))
        self.assertFalse(tree.find(42))
        self.assertFalse(tree.find(16))

    def testEmptyTree(self):
        empty = BinaryTree()
        self.assertEqual(0, empty.getSize())
        self.assertIsNone(empty.getRoot())

    def testDifferentInsertions(self):
        tree = BinaryTree()
        tree.insert(0)
        self.assertEqual(0, tree.getRoot().key)
        with self.assertRaises(ValueError):
            tree.insert(0)
        tree.insert(1)
        tree.insert(5, 0)
        with self.assertRaises(ValueError):
            tree.insert(6, 0)
        with self.assertRaises(ValueError):
            tree.insert(7, 8)
        self.assertFalse(tree.find(8))
        self.assertFalse(tree.find(7))
        self.assertEqual(3, tree.getSize())

if __name__ == '__main__':
    unittest.main()
