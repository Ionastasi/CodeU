class Node:
    """Implementation of a Binary Trees node.

    Fields:
        key:   an integer, key of the current node;
        left:  a Node, left child of the current node;
        right: a Node, right child of the current node.
    """
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)