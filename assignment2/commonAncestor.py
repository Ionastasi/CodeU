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
    def _commonAncestor(cur):
        """Internal inner function that finds lowest common ancestor.

        Args:
            cur: a Node, current node in the tree.

        Nonlocal variables:
            key1:         an integer, key of the first node;
            key2:         an integer, key of the second node;
            ancestor:     an integer that stores the key of the lowest common
                          ancestor. `None` if no ancestors were found.

        Return:
            an integer (0, 1 or 2) that represents how many required keys were
            found in the subtree of the current node.
        """
        nonlocal key1, key2, ancestor
        if ancestor is not None:
            return 2
        if cur is None:
            return 0
        foundDeeper = ((cur.key in (key1, key2)) + _commonAncestor(cur.left)
                                                 + _commonAncestor(cur.right))
        if ancestor is None and (foundDeeper == 2 or cur.key == key1 == key2):
            ancestor = cur.key
        return foundDeeper

    ancestor = None
    result = _commonAncestor(tree.getRoot())
    return ancestor
