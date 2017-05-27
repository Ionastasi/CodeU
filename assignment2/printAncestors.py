"""Given a Binary Tree and a key, write a function that prints all the ancestors
of the key in the given binary tree."""

from binarytree import BinaryTree

def findAncestors(tree, key):
    """Return all ancestors of the given key in the given binary tree.
    (This function is needed for testing.)

    Args:
        tree: a BinaryTree;
        key:  an integer, the key of the node in the given tree which ancestors
              we should print.

    Return: list of the ancestors of the given node.
    """
    def _findAncestors(cur):
        """Internal helper function that finds ancestors.

        Args:
            cur: a Node, current node in the tree.

        Return:
            a list with some ancestors of the required key that contains in the
            subtree of a current node.
        """
        nonlocal key
        if cur is None or cur.key == key:
            return []
        left, right = cur.left, cur.right
        if (left is not None and left.key == key or
           right is not None and right.key == key):
            return [cur.key]  # this is the parent of the required key
        childs = _findAncestors(left) + _findAncestors(right)
        if childs:
            return childs + [cur.key]
        return []

    return _findAncestors(tree.getRoot())

def printAncestors(tree, key):
    """Print all ancestors of the given key in the given binary tree."""
    print(findAncestors(tree, key))
