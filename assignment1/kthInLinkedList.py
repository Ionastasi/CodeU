class Node:
    """A class that represents the node of the singly linked list.

    Fields:
        key: an integer, key of the node;
        next: a Node, the next element in the linked list.
    """
    def __init__(self, _key = 0, _next = None):
        self.key = _key
        self.next = _next

    def __str__(self):
        return str(self.key)

def kthInLinkedList(linkedList, k):
    """Function that finds the kth to last element of a singly linked list.

    Args:
        linledList: a Node, the first element in the linked list;
        k:          an integer that defines an element that we should return.

    Return:
        an integer, a key of the kth to last element of a given linked list,
        or `None` if such element doesn't exist.
    """
    if k < 0:
        return None
    ptr1 = ptr2 = linkedList
    # move ptr1 to the (k+1)th to first element in the linked list
    cnt = -1
    while cnt != k:
        if ptr1 is None:
            return None  # linked list have the size shorter than k+1
        ptr1 = ptr1.next
        cnt += 1
    # then move both pointers simultaneously
    while ptr1 is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr2.key
