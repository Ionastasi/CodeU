class DisjointSet:
    """Implementation of a Disjoint Set."""

    def __init__(self):
        """
        Fields:
            parents: link to the parent (header member) of the set
            rank:    helps to determine how to union two sets
                     (heuristic to improve time complexity of unionSet)
        As well as I want to use 1-based numeration of set, `parent` and `rank`
        contain first extra element.
        """
        self.parent = [0]
        self.rank = [0]
        self.setCount = 0

    def getSetCount(self):
        return self.setCount

    def makeSet(self):
        """Create new set and return its num."""
        newSetNum = len(self.parent)
        self.parent.append(newSetNum)
        self.rank.append(0)
        self.setCount += 1
        return newSetNum

    def findSet(self, v):
        """Return parent (header member) of the set with num `v`."""
        if v == self.parent[v]:
            return v
        # heuristic to improve time complexity:
        self.parent[v] = self.findSet(self.parent[v])
        return self.parent[v]

    def unionSets(self, a, b):
        """Unioin two sets with nums `a` and `b`."""
        a = self.findSet(a)
        b = self.findSet(b)
        if a == b:
            return
        self.setCount -= 1
        # now we need to connect one set to the other. heuristic `rank` helps us
        # to determine which set should be connected
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
