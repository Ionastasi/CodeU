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
                               should be a parent of a new node. `None` by
                               default, that means that any node in the tree
                               could be a parent of a new one;
            isLeft (optional): a bool, True if a new node should be a left child
                               and False if it should be a right child. `None`
                               by default, that means it doesn't matter which
                               child would be a new node. If `parent = None`
                               then `isLeft` should be `None`, otherwise it
                               raised an error.

        Return:
            None
        """
        if self.root is None:
            self.root = Node(key)
            self.size += 1
            return

        if self.find(key):
            raise ValueError("key is a duplicate, which not allowed")

        if parent is None:
            if isLeft is not None:
                raise ValueError("you should specify a parent if you want" +
                                 "to insert new node as left/right" +
                                 "child only")
            self._insert_internal(key, self.root)
        else:
            if not self.find(parent):
                raise ValueError("there is no node", parent, "in the tree")
            success = self._insert_internal(key, self.root, parent, isLeft)
            if not success:
                raise ValueError("impossible to insert a new node under node",
                                 parent)
        self.size += 1

    def _insert_internal(self, key, cur, parent = None, isLeft = None):
        """Internal iplementation of `insert(...)`.

        Args:
            key:               an integer, new key that should be inserted;
            cur:               a Node, current node in the tree that could be a
                               parent of a new one;
            parent (optional): see insert(...);
            isLeft (optional): see insert(...).

        Return:
            a bool, True if the new key was successfully added to the current
            node or some of its children, and False otherwise.
        """
        if cur is None:
            return False

        if parent is not None:
            if cur.key != parent:
                return (self._insert_internal(key, cur.left, parent, isLeft) or
                        self._insert_internal(key, cur.right, parent, isLeft))
            return self._insert_child(key, cur, isLeft)

        return ((self._insert_child(key, cur)) or
                (self._insert_internal(key, cur.right)) or
                (self._insert_internal(key, cur.left)))

    def _insert_child(self, key, cur, isLeft = None):
        """Helper function for _insert_internal(...).

        Args: the same as in _insert_internal(...).

        Return:
            a bool, True if the new key was successfully added to the current
            node, and False otherwise.
        """
        if isLeft is not None:
            if ((isLeft and cur.left is not None) or
                                     (not isLeft and cur.right is not None)):
                raise ValueError("This child doesn't available under this parent")
            if isLeft:
                cur.left = Node(key)
            else:
                cur.right = Node(key)
        else:
            if cur.left is None:
                cur.left = Node(key)
            elif cur.right is None:
                cur.right = Node(key)
            else:
                return False
        return True
