class Node:
    def __init__(self, _key = 0, _next = None):
        self.key = _key
        self.next = _next

    def __str__(self):
        return str(self.key)

def kthInLinkedList(linkedList, k):
    if k < 0:
        return None
    ptr1 = ptr2 = linkedList
    cnt = -1
    while cnt != k:
        if ptr1 is None:
            return None
        ptr1 = ptr1.next
        cnt += 1
    while ptr1 is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr2

def _test():
    while True:
        n = 15
        head = Node(n - 1)
        prev = head
        print("\nlinkedList:", head, end = ' ')
        for i in range(n-2, -1, -1):
            new = Node(i)
            prev.next = new
            prev = new
            print(new, end = ' ')
        print()
        k = int(input("input k: ".format(n)))
        print(kthInLinkedList(head, k))


if __name__ == "__main__":
    _test()
