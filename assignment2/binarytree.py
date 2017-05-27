from random import randint
from node import *

class BinaryTree:
    """Implementation of a Binary Tree."""

    def __init__(self, rootKey = None):
        self.root = None
        self.size = 0
        if rootKey is not None:
            self.root = Node(rootKey)
            self.size += 1

    def getRoot(self):
        """Return a Node that represents the root of the tree."""
        return self.root

    def getSize(self):
        """Return the size of the tree."""
        return self.size

    def find(self, key):
        """Does tree contains a node with such key.

        Args:
            key: an integer, key which should be found in the tree.

        Returns:
            a bool, True if the tree contains such node, and False otherwise.
        """
        return self._find(key, self.root)

    def _find(self, key, cur):
        """Internal iplementation of `find(key)`.

        Args:
            key: an integer, key which should be found in the tree;
            cur: a Node, current node in the tree that we are checking now.

        Returns:
            a bool, True if key of current node or some of its childs equals to
            what we seeking for, or False otherwise.
        """
        if cur is None:
            return False
        if cur.key == key:
            return True
        return self._find(key, cur.right) or self._find(key, cur.left)

    def insert(self, key, parent = None, isLeft = None):
        """Insert a new given key in the tree.

        Args:
            key:               an integer, new key that should be inserted;
            parent (optional): an integer, key of some node in the tree, that
                               should be a parent of a new node, if it possible.
                               `None` by default, that means that any node in
                               the tree could be a parent of a new one;
            isLeft (optional): a bool, True if a new node should be a left child
                               (if it possible) and False if it should be a
                               right child (if it possible). `None` by default,
                               that means it doesn't matter which child would be
                               a new node. If `parent = None` then `isLeft`
                               won't be taken into account.

        Return:
            a bool, True if the new key was successfully inserted in the tree
            (even if conditions `parent` and `isLeft` are violated), and False
            otherwise.
        """
        if self.root is None:
            self.root = Node(key)
            self.size += 1
            return True
        else:
            if self.find(key):
                return False  # duplicated keys are not allowed
            if parent is None or not self.find(parent):
                parent = isLeft = None
            # check if it possible to insert a new node to this parent
            sucsees = self._add(key, self.root, parent, isLeft)
            if not sucsees:
                # just insert it somewhere (always possible)
                self._add(key, self.root)
            self.size += 1
            return True

    def _add(self, key, cur, parent = None, isLeft = None):
        """Internal iplementation of `insert(...)`.

        Args:
            key:               an integer, new key that should be inserted;
            cur:               a Node, current node in the tree that could be a
                               parent of a new one;
            parent (optional): an integer, key of some node in the tree, that
                               should be a parent of a new node, if it possible.
                               `None` by default, that means that any node in
                               the tree could be a parent of a new one;
            isLeft (optional): a bool, True if a new node should be a left child
                               (if it possible) and False if it should be a
                               right child (if it possible). `None` by default,
                               that means it doesn't matter which child would be
                               a new node.

        Return:
            a bool, True if the new key was successfully adde to the current
            node or some of its childs, and False otherwise
        """
        if cur is None:
            return False
        if parent is not None:
            if cur.key != parent:
                return (self._add(key, cur.left, parent, isLeft) or
                        self._add(key, cur.right, parent, isLeft))
            if cur.right is not None and cur.left is not None:
                return False  # parent node doesn't have any free childs
            if cur.right is not None:
                cur.left = Node(key)
            elif cur.left is not None:
                cur.right = Node(key)
            else:
                # randomly choose the child, if it doesn't specified.
                if isLeft is None:
                    isLeft = randint(0, 1)
                if isLeft:
                    cur.left = Node(key)
                else:
                    cur.right = Node(key)
            return True
        else:
            if cur.left is None and cur.right is None:
                if randint(0, 1):  # randomly choose the child
                    cur.left = Node(key)
                else:
                    cur.right = Node(key)
                return True
            elif cur.left is None:
                cur.left = Node(key)
                return True
            elif cur.right is None:
                cur.right = Node(key)
                return True
            return (self._add(key, cur.right) or
                    self._add(key, cur.left))
