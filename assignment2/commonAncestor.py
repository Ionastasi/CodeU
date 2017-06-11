"""Design an algorithm and write code to find the lowest common ancestor of two
nodes in a binary tree. Avoid storing additional nodes in a data structure."""

from binarytree import BinaryTree

def commonAncestor(tree, key1, key2):
    """Find the lowest common ancestors of the given nodes in the given Binary
    Tree.

    Args:
        tree: a BinaryTree;
        key1: an integer, key of the first node;
        key2: an integer, key of the second node.

    Return:
        an integer, key of the lowest common ancestors of two given nodes,
        or `None` if some of the given nodes doesn't exists in the given tree.
    """
    def _commonAncestor(cur, key1, key2):
        """Internal inner function that finds lowest common ancestor.

        Args:
            cur:          a Node, current node in the tree.
            key1, key2:   see commonAncestors(...).

        Nonlocal variables:
            ancestor:     an integer that stores the key of the lowest common
                          ancestor. `None` if no ancestors were found.

        Return:
            an integer (0, 1 or 2) that represents how many required keys were
            found in the subtree of the current node.
        """
        nonlocal ancestor

        if cur is None:
            return 0

        if ancestor is not None:
            # common ancestor already found
            return 2
        if cur.key == key1 == key2:
            ancestor = cur.key
            return 2

        foundDeeper = ((cur.key in (key1, key2))
                        + _commonAncestor(cur.left, key1, key2)
                        + _commonAncestor(cur.right, key1, key2))
        if ancestor is not None:
            # common ancestor was found somewhere in the subtree
            return 2
        if foundDeeper == 2:
            # both children was found and common ancestor is not specified =>
            # cur node is common ancestor
            ancestor = cur.key
        return foundDeeper

    ancestor = None
    result = _commonAncestor(tree.getRoot(), key1, key2)
    return ancestor
