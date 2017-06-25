class DisjointSet:
    """Implementation of a Disjoint Set. Takes integers as keys."""

    def __init__(self):
        self.parent = list()
        self.rank = list()
        self.setAmount = 0

    def getSetAmount(self):
        return self.setAmount

    def makeSet(self, v):
        if len(self.parent) <= v:
            toAdd = v - len(self.parent) + 1
            self.parent += [0] * toAdd
            self.rank += [0] * toAdd
        self.parent[v] = v
        self.rank[v] = 0
        self.setAmount += 1

    def findSet(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.findSet(self.parent[v])
        return self.parent[v]

    def unionSets(self, a, b):
        a = self.findSet(a)
        b = self.findSet(b)
        if a == b:
            return
        self.setAmount -= 1
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.parent[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
