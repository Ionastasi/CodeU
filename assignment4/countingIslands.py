from disjointset import DisjointSet

def countingIslands(islandsMap):
    """Given a 2-dimensional map of tiles. Each tile is either land or water.
    Counts the number of islands.

    Args:
        islandsMap: a 2-dimensional array of booleans, where False means water
                    and True means land.

    Returns:
        an integer, the number of islands.
    """
    islands = DisjointSet()
    counter = 0
    rows = len(islandsMap)
    if rows:
        cols = len(islandsMap[0])
    for x in range(rows):
        for y in range(cols):
            if not islandsMap[x][y]:
                continue
            counter += 1
            islandsMap[x][y] = counter
            islands.makeSet(counter)
            # iterate through adjacent cells that we already processed
            for dx, dy in [[-1, 0], [0, -1]]:
                xx, yy = x + dx, y + dy
                if 0 <= xx <= rows and 0 <= yy <= cols and islandsMap[xx][yy]:
                    islands.unionSets(counter, islandsMap[xx][yy])
    return islands.getSetAmount()
