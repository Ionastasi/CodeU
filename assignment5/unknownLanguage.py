def unknownLanguage(dictionary):
    """Given a dictionary of all words in an unknown/invented language, find the
    alphabet of that language.

    Args:
        dictionary: a list of words in lexicographic order.

    Returns:
        the alphabet, an ordered list of characters.
    """
    def dfs(v, visited):
        """
        Depth-first search with cycle search.
        """
        visited[v] = 1
        for u in adjList[v]:
            if visited[u] == 0:
                dfs(u, visited)
            elif visited[u] == 1:
                # in that case, we have cycles in our graph =>
                # it can't be topological sorted => it's not an alphabet
                raise ValueError("dictionary is not in lexicographic order")
        visited[v] = 2
        alphabet.append(v)

    def topologicalSort():
        """
        An ordinary topological sort based on dfs.
        """
        visited = dict()
        for v in adjList:
            visited[v] = 0
        for v in adjList:
            if not visited[v]:
                dfs(v, visited)
        alphabet.reverse()


    if not dictionary:
        return []

    # define adjacency list where nodes are letters, not nums
    adjList = dict()
    for word in dictionary:
        for let in word:
            if let not in adjList:
                adjList[let] = set()

    maxLen = max([len(word) for word in dictionary])

    # bruteforce all possible prefixes by they length
    for prefixLen in range(maxLen):
        curPrefix = None
        prevLetter = ''
        for word in dictionary:
            if curPrefix is None:  # so, previous word didn't have proper length
                # > because we want the NEXT letter after prefix
                if len(word) > prefixLen:
                    curPrefix = word[:prefixLen]
                    prevLetter = word[prefixLen]
                continue
            if len(word) > prefixLen:
                if word[:prefixLen] == curPrefix:  # we can compare two letters
                    curLetter = word[prefixLen]
                    if prevLetter != curLetter:  # we don't want to have loops
                        adjList[prevLetter].add(curLetter)
                    prevLetter = curLetter
                else:  # new prefix
                    curPrefix = word[:prefixLen]
                    prevLetter = word[prefixLen]
            else:  # this word is too short
                curPrefix = None

    alphabet = []
    topologicalSort()
    return alphabet
