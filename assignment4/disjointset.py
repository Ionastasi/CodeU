class DisjointSet:
    """This class is used to compute disjoint sets by merging elements.

       Elements are called set. You should create a new set using the
       makeSet() method, which returns the identifier of the new set.

       You can join two sets by calling the unionSets() method with two set
       identifiers and they will be merged into a single new set.

       Given a set identifier, you can find the canonical identifier for
       that set by calling findSet(). Two sets that have been merged will
       have the same canonical identifier. Note that the canonical
       identifier of a set might change every time unionSets() is called.
    """
    def __init__(self):
        self.__parent = [0]
        self.__rank = [0]
        self.__setCount = 0

    def getSetCount(self):
        return self.__setCount

    def makeSet(self):
        """Creates a new set.

        Returns:
          an integer, the identifier of the newly created set.
        """
        newSetNum = len(self.__parent)
        self.__parent.append(newSetNum)
        self.__rank.append(0)
        self.__setCount += 1
        return newSetNum

    def findSet(self, v):
        """Given a set identifier v, find the canonical identifier for that set.

        Returns:
            the canonical identifier.
        """
        if v == self.__parent[v]:
            return v
        # heuristic to improve time complexity:
        self.__parent[v] = self.findSet(self.__parent[v])
        return self.__parent[v]

    def unionSets(self, a, b):
        """Join two sets by their set identifiers into a single new set."""
        a = self.findSet(a)
        b = self.findSet(b)
        if a == b:
            return
        self.__setCount -= 1
        # now we need to connect one set to the other. heuristic `rank` helps us
        # to determine which set should be connected
        if self.__rank[a] < self.__rank[b]:
            a, b = b, a
        self.__parent[b] = a
        if self.__rank[a] == self.__rank[b]:
            self.__rank[a] += 1
